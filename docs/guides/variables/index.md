---
icon: lucide/book-marked
---

# SHARE Variable Dictionary

This section is generated from the Stata metadata embedded in the local SHARE release files stored in `data/`.

It is a file-level dictionary: for each wave and dataset, it lists every variable name together with the variable label, storage type, and Stata format.

Use this dictionary when you already know the wave and need to answer questions like:

- What does `ph006d10` mean in wave 9?
- Which variables are inside `technical_variables`?
- Does `gv_exrates` use `mergeid` or `country`?

Use the official SHARE sources below for complementary tasks:

- SHARE Data Documentation: <https://share-eric.eu/data/data-documentation>
- SHARE Data & Documentation Tool: <https://www.share-datadocutool.org/>
- SHARE Cross-Wave Comparison: <https://www.share-eric.eu/data/data-documentation/questionnaires/cross-wave-comparison>

For module selection and naming conventions, see the [module guide](../modules.md).

## Waves

| Wave | Release | Datasets | Variable entries | Page |
| --- | --- | --- | --- | --- |
| Wave 1 | `9-0-0` | 32 | 2,447 | [Wave 1](wave-1.md) |
| Wave 2 | `9-0-0` | 32 | 2,746 | [Wave 2](wave-2.md) |
| Wave 3 | `9-0-0` | 18 | 3,409 | [Wave 3](wave-3.md) |
| Wave 4 | `9-0-0` | 33 | 4,811 | [Wave 4](wave-4.md) |
| Wave 5 | `9-0-0` | 34 | 4,812 | [Wave 5](wave-5.md) |
| Wave 6 | `9-0-0` | 36 | 5,796 | [Wave 6](wave-6.md) |
| Wave 7 | `9-0-0` | 43 | 8,415 | [Wave 7](wave-7.md) |
| Wave 8 | `9-0-0` | 40 | 7,025 | [Wave 8](wave-8.md) |
| Wave 9 | `9-0-0` | 35 | 6,301 | [Wave 9](wave-9.md) |

## Notes

- The pages in this section reflect the files currently available in the local `data/` directory.
- Regenerate this section with `uv run python scripts/generate_variable_dictionary.py`.
- Variable names can change meaning across waves for SHARELIFE datasets, especially in wave 3. Check the wave-specific page before comparing short module codes like `ac`, `cs`, or `hc`.
- This dictionary is not a cross-wave harmonisation table. For cross-wave item correspondences, use the official SHARE Cross-Wave Comparison.
