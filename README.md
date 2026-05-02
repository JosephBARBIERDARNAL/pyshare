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

> [!NOTE]
> It always return a polars dataframe.

- For much faster read time specify which modules you want:

```py
import pyshare as ps

df = ps.read_share_wave(9 , modules=["dn", "ph", "hc"])
df.shape
#> (69447, 401)
```

- `pyshare` also bundles a few mapping dictionnary to make the data more human-readable:

```py
```

Learn more in the [documentation website](https://josephbarbierdarnal.github.io/pyshare/).
