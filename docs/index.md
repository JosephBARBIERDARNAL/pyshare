---
icon: lucide/rocket
---

# pyshare

Python interface to work with SHARE data (Survey of Health, Ageing and Retirement in Europe)

<br>

## Installation

```
pip install git+https://github.com/JosephBARBIERDARNAL/pyshare.git
```

<br>

## Quick start

In order to read SHARE data, it requires you to have access to them, to download them locally (Stata version) and unzip them. By default it looks for the `data/` directory.

```py
import pyshare as ps

# All data from wave 9
df = ps.read_share_wave(9)
df.shape
#> (97365, 4462)
```

!!! note

     It always return a polars dataframe.

- For much faster read time specify which modules you want:

```py
import pyshare as ps

df = ps.read_share_wave(9 , modules=["dn", "ph", "hc"])
df.shape
#> (69447, 401)
```

- `pyshare` also bundles a few mapping dictionnary to make the data more human-readable:

```py
from pyshare import MAP_ID_TO_COUNTRY
import pyshare as ps

(
   ps.read_share_wave(9, modules=["dn"])
   # Get country in "human" format
   .with_columns(pl.col("country").replace_strict(ps.MAP_ID_TO_COUNTRY))
)
```

The exhaustive list is:

- MAP_ID_TO_COUNTRY
- MAP_YES_NO
- MAP_CANCER
- MAP_GENDER
- MAP_COMPUTER_SKILLS
- MAP_HEALTH_LITERACY_HELP
- MAP_ENDS_MEET
- MAP_ISCED_1997
- MAP_SHARE_MISSING_CODES
- MAP_SHARE_FINANCIAL_MISSING_CODES

If you are unsure which dataset to load, start with the [module guide](./guides/modules.md). It explains how SHARE filenames map to `pyshare` module names and includes a module dictionary by topic and wave.

If you already know the wave and need the exact meaning of a variable name, use the [variable dictionary](./guides/variables/index.md). It is generated from the Stata metadata embedded in the local SHARE files.

Learn more in the [reference page](./reference/read.md).
