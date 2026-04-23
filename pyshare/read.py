from __future__ import annotations

import re
from collections.abc import Iterable
from pathlib import Path
from typing import Literal

import polars as pl
from polars_readstat import read_readstat

SHARE_FILE_RE = re.compile(
    r"^sharew(?P<wave>\d+)_rel(?P<release>[^_]+)_(?P<module>.+)\.dta$"
)

COMMON_SHARE_COLUMNS = {
    "country",
    "language",
    "hhid",
    "hhid1",
    "hhid2",
    "mergeidp1",
    "mergeidp2",
    "coupleid",
    "coupleid1",
    "coupleid2",
    "waveid",
    "waveid_hh",
    "firstwave",
    "firstwave_hh",
    "int_year",
    "int_month",
}

JoinHow = Literal["inner", "left", "right", "full", "semi", "anti", "cross", "outer"]


def _parse_share_file(path: Path) -> dict[str, str] | None:
    match = SHARE_FILE_RE.match(path.name)
    if match is None:
        return None
    return match.groupdict()


def _wave_files(*, wave: int, path: str | Path = "data") -> list[tuple[str, Path]]:
    data_path = Path(path)
    files: list[tuple[str, Path]] = []

    for file_path in sorted(data_path.glob(f"sharew{wave}_rel*.dta")):
        parsed = _parse_share_file(file_path)
        if parsed is None or int(parsed["wave"]) != wave:
            continue
        files.append((parsed["module"], file_path))

    return files


def available_share_modules(
    *, wave: int, path: str | Path = "data", include_derived: bool = False
) -> list[str]:
    modules = []

    for module, _ in _wave_files(wave=wave, path=path):
        if not include_derived and module.startswith("gv_"):
            continue
        modules.append(module)

    return modules


def _find_share_file(*, wave: int, module: str, path: str | Path = "data") -> Path:
    matches = [
        file_path
        for found_module, file_path in _wave_files(wave=wave, path=path)
        if found_module == module
    ]

    if not matches:
        available = ", ".join(
            available_share_modules(wave=wave, path=path, include_derived=True)
        )
        raise FileNotFoundError(
            f"Could not find SHARE wave {wave} module {module!r} in {Path(path)}. "
            f"Available modules: {available}"
        )

    if len(matches) > 1:
        files = ", ".join(str(match) for match in matches)
        raise ValueError(
            f"Found more than one SHARE file for wave {wave} module {module!r}: {files}"
        )

    return matches[0]


def read_share_module(
    *, wave: int, module: str, path: str | Path = "data"
) -> pl.DataFrame:
    return read_readstat(_find_share_file(wave=wave, module=module, path=path))


def _require_mergeid(module: str, df: pl.DataFrame) -> None:
    if "mergeid" not in df.columns:
        raise ValueError(
            f"Module {module!r} cannot be merged because it has no 'mergeid' column."
        )

    duplicate_count = df.height - df.select("mergeid").n_unique()
    if duplicate_count > 0:
        raise ValueError(
            f"Module {module!r} cannot be merged because 'mergeid' is not unique "
            f"({duplicate_count} duplicates)."
        )


def _prepare_for_join(left: pl.DataFrame, right: pl.DataFrame) -> pl.DataFrame:
    overlapping = set(left.columns) & set(right.columns)
    overlapping.discard("mergeid")

    drop_from_right = sorted(overlapping & COMMON_SHARE_COLUMNS)
    if drop_from_right:
        right = right.drop(drop_from_right)

    return right


def _unique_modules(modules: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []

    for module in modules:
        if module in seen:
            continue
        seen.add(module)
        ordered.append(module)

    return ordered


def read_share_wave(
    *,
    wave: int,
    path: str | Path = "data",
    modules: Iterable[str] | None = None,
    base_module: str = "cv_r",
    include_derived: bool = False,
    how: JoinHow = "left",
) -> pl.DataFrame:
    explicit_modules = modules is not None
    if modules is None:
        selected_input = available_share_modules(
            wave=wave,
            path=path,
            include_derived=include_derived,
        )
    else:
        selected_input = modules

    selected_modules = _unique_modules(selected_input)

    if not selected_modules:
        raise ValueError(f"No SHARE modules found for wave {wave} in {Path(path)}.")

    if base_module in selected_modules:
        ordered_modules = [
            base_module,
            *[m for m in selected_modules if m != base_module],
        ]
    else:
        ordered_modules = selected_modules

    merged: pl.DataFrame | None = None

    for module in ordered_modules:
        frame = read_share_module(wave=wave, module=module, path=path)

        try:
            _require_mergeid(module, frame)
        except ValueError:
            if explicit_modules:
                raise
            continue

        if merged is None:
            merged = frame
            continue

        mergeable_frame = _prepare_for_join(merged, frame)
        merged = merged.join(
            mergeable_frame,
            on="mergeid",
            how=how,
            suffix=f"__{module}",
        )

    if merged is None:
        raise ValueError(
            f"No mergeable SHARE modules found for wave {wave} in {Path(path)}."
        )

    return merged
