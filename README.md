# pyshare

Python interface to work with SHARE data (Survey of Health, Ageing and Retirement in Europe)

<br>

## Installation

```
pip install git+https://github.com/JosephBARBIERDARNAL/pyshare.git
```

<br>

## Quick start

In order to read SHARE data, it requires you to have access to them, to download them locally (Stata version) and unzip them. By default it looks for the `data` directory.

```py
import pyshare as ps

df = ps.read_share_wave(wave=9)
df.shape
#> (97365, 4462)
```

If you are unsure which dataset to load, start with the documentation module guide at `docs/guides/modules.md`.
If you need exact variable labels for a specific wave and dataset, use `docs/guides/variables/index.md`.
