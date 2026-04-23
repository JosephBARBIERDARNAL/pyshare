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

In order to read SHARE data, it requires you to have access to them, to download them locally (Stata version) and unzip them. By default it looks for the `data` directory.

```py
import pyshare as ps

df = ps.read_share_wave(wave=9)
df.shape
#> (97365, 4462)
```

If you are unsure which dataset to load, start with the [module guide](./guides/modules.md). It explains how SHARE filenames map to `pyshare` module names and includes a module dictionary by topic and wave.

If you already know the wave and need the exact meaning of a variable name, use the [variable dictionary](./guides/variables/index.md). It is generated from the Stata metadata embedded in the local SHARE files.

Learn more in the [reference page](./reference/read.md).
