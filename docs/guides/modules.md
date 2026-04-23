---
icon: lucide/folder-tree
---

# Choosing SHARE modules

This page is a practical guide to SHARE module names as they appear in the downloaded `.dta` files and in `pyshare`.

For the exact variable-by-variable dictionary within each wave, see the [variable dictionary](./variables/index.md).

The key point is simple:

- The `module` argument used by `pyshare.read_share_module()` is the exact dataset suffix in the filename.
- That suffix is not always the same as the short label used in the official release guide tables.

## How dataset filenames work

SHARE filenames follow this pattern:

```text
sharew{wave}_rel{release}_{module}.dta
```

Examples:

- `sharew9_rel9-0-0_ph.dta` -> wave 9, release `9-0-0`, module `ph`
- `sharew9_rel9-0-0_technical_variables.dta` -> module `technical_variables`
- `sharew8_rel9-0-0_gv_accelerometer_day.dta` -> generated module `gv_accelerometer_day`

In `pyshare`, you load the module using the final part of the filename:

```py
import pyshare as ps

ph = ps.read_share_module("ph", wave=9)
tc = ps.read_share_module("technical_variables", wave=9)
```

## Official labels vs file names

The release guide often uses questionnaire abbreviations, while the files sometimes use a more explicit name.

| Release guide label | File / `pyshare` module name |
| --- | --- |
| `CV_R` | `cv_r` |
| `DO` | `dropoff` |
| `TC` | `technical_variables` |
| `VI` | `vignettes` |
| Interviewer Survey | `interviewer_survey` |
| Accelerometry generated files | `gv_accelerometer_total`, `gv_accelerometer_day`, `gv_accelerometer_hour`, `gv_accelerometer_sleep` |

Derived modules always start with `gv_`.

## How SHARE variable names work

The SHARE release guide defines the main variable naming pattern as:

```text
mmXXXyyy_LL
```

- `mm`: module identifier, such as `dn` or `ph`
- `XXX`: question number
- `yyy`: optional suffix used for special cases
- `_LL`: optional loop index or category index

Common patterns:

- `ph006_`: question 006 from module `ph`
- `ft003_1`: looped question in module `ft`
- `br005d1`: dummy variable for response category 1
- `ep078e_1`: Euro-converted amount
- `ep078ub_1`: unfolding-bracket summary variable

Special cases from the release guide:

- Wave 3 SHARELIFE variables are generally prefixed with `sl_`.
- In wave 3, some module names collide with regular-wave names. For example, `ac` means Activities in regular waves, but Retrospective Accommodation in wave 3.

## Wave 3 names to watch closely

Wave 3 is a SHARELIFE retrospective wave, so a few short module names do not mean the same thing as in the regular waves.

| `pyshare` module | Wave 3 meaning | Regular-wave meaning |
| --- | --- | --- |
| `st` | SHARELIFE demographics | `dn` is used for demographics in regular waves |
| `ac` | Retrospective Accommodation | Activities |
| `cs` | Childhood Section | Chair Stand |
| `hc` | Retrospective Health Care | Health Care |

## Before choosing a module

These rules are usually enough:

- Use `cv_r` as the starting point when you need one row per observed household member in a wave.
- Use `dn` for demographic background variables in regular waves, and `st` for wave 3 SHARELIFE demographics.
- Use the thematic module prefix when you want original questionnaire variables, such as `ph`, `mh`, `hc`, `ep`, `ch`, `sp`, `ft`, `ho`, or `as`.
- Use a `gv_` module when you want harmonised or derived outputs, such as weights, imputed values, education recodes, or summary indicators.

Also note that not every dataset is a one-row-per-person module:

- `interviewer_survey` uses `intid`, not `mergeid`
- `gv_exrates` is country-level and joins on `country`
- `gv_accelerometer_day`, `gv_accelerometer_hour`, and `gv_accelerometer_sleep` have repeated rows per respondent

Those modules are usually better loaded with `read_share_module()` than merged through `read_share_wave()`.

## Common module choices

| If you need... | Start with these modules |
| --- | --- |
| Household roster, interview status, partner IDs | `cv_r` |
| Basic demographics, education, marital history, parents, spouses | `dn` |
| Children and intergenerational ties | `ch`, `sp`, `ft`, `gv_children` |
| Physical and functional health | `ph`, `hc`, `br`, `gs`, `pf`, `ws`, `cs`, `gv_health` |
| Mental health and cognition | `mh`, `cf`, `gv_health` |
| Employment, pensions, income, assets, spending | `ep`, `hh`, `co`, `as`, `ft`, `gv_imputations`, `gv_exrates` |
| Housing | `ho`, `gv_housing` |
| Social networks | `sn`, `gv_networks` |
| Weights | `gv_weights` |
| Harmonised education coding | `gv_isced` |
| Questionnaire routing or respondent roles | `technical_variables` |
| Interviewer answers about interview conditions | `iv` |

## Module dictionary

### Core interview modules

| `pyshare` module | Waves | Meaning | Load this when you need... |
| --- | --- | --- | --- |
| `cv_r` | 1-9 | Coverscreen on individual level | household roster, interview participation, partner IDs, entry wave |
| `dn` | 1, 2, 4-9 | Demographics | background, education, marital status, parents, spouses |
| `sn` | 4, 6, 8, 9 | Social Networks | named confidants and network ties |
| `ch` | 1, 2, 4-9 | Children | characteristics of respondents' children |
| `ph` | 1, 2, 4-9 | Physical Health | diagnoses, symptoms, ADL/IADL, disability |
| `br` | 1, 2, 4-9 | Behavioural Risks | smoking, alcohol, physical activity |
| `cf` | 1, 2, 4-9 | Cognitive Function | memory, numeracy, fluency, concentration |
| `mh` | 1, 2, 4-9 | Mental Health | depression, well-being, emotional health |
| `hc` | 1, 2, 4-9 | Health Care | doctor visits, hospital stays, insurance |
| `ep` | 1, 2, 4-9 | Employment and Pensions | labour status, earnings, pensions |
| `it` | 5-9 | Computer Use | frequency and skills in computer use |
| `mc` | 5 | Mini Childhood | short childhood module for non-SHARELIFE respondents |
| `gs` | 1, 2, 4-9 | Grip Strength | dynamometer measurement |
| `ws` | 1, 2 | Walking Speed | timed walking test |
| `cs` | 2, 5 | Chair Stand | sit-to-stand performance test |
| `bs` | 6 | Blood Sample | dried blood spot collection process |
| `pf` | 2, 4, 6 | Peak Flow | expiratory lung force |
| `sp` | 1, 2, 4-9 | Social Support | help given and received |
| `ft` | 1, 2, 4-9 | Financial Transfers | transfers, gifts, inheritances |
| `ho` | 1, 2, 4-9 | Housing | dwelling characteristics, tenure, mortgages, rent |
| `hh` | 1, 2, 4-9 | Household Income | household income summaries |
| `co` | 1, 2, 4-9 | Consumption | household spending |
| `as` | 1, 2, 4-9 | Assets | financial and non-financial assets |
| `ac` | 1, 2, 4-9 | Activities | activities, life satisfaction, Big Five items in waves 7-9 |
| `ex` | 1, 2, 4-9 | Expectations | expectations, probabilities, trust, orientation |
| `sr` | 8 | Saving Regrets | retrospective saving and spending regrets |
| `te` | 8, 9 | Time Expenditure | how respondents spend time |
| `iv` | 1-9 | Interviewer Observations | interview circumstances recorded by interviewer |
| `xt` | 2-9 | End-of-Life Interview | proxy interview after a respondent's death |
| `dropoff` | 1, 2, 4-9 | Paper-and-pencil drop-off | self-completion supplement, often country-specific |
| `vignettes` | 1, 2 | Vignettes | anchoring vignette questionnaire |
| `technical_variables` | 1, 2, 4-9 | Technical variables (`MN#` in the questionnaire) | routing flags, baseline/longitudinal status, respondent roles |
| `interviewer_survey` | 5, 6, 7, 9 | Interviewer Survey | separate interviewer questionnaire, keyed by `intid` |
| `ep_ilextra` | 1 | Israel EP add-on | wave 1 Israeli EP re-interview and routing corrections |
| `ax` | 8 | Accelerometry | consent and participation for accelerometer collection |

### SHARELIFE modules

Wave 3 is retrospective SHARELIFE only. Wave 7 contains both regular modules and additional SHARELIFE modules for respondents who did not complete SHARELIFE in wave 3.

| `pyshare` module | Waves | Meaning | Notes |
| --- | --- | --- | --- |
| `st` | 3 | SHARELIFE demographics | wave 3 retrospective demographics |
| `ac` | 3 | Retrospective Accommodation | different from regular-wave `ac` |
| `cs` | 3 | Childhood Section | different from regular-wave `cs` |
| `dq` | 3, 7 | Disability | SHARELIFE module |
| `fs` | 3, 7 | Financial Section | SHARELIFE module |
| `gl` | 3, 7 | General Life and Persecution | SHARELIFE module |
| `hc` | 3 | Retrospective Health Care | different from regular-wave `hc` |
| `hs` | 3, 7 | Health History / Health Section | SHARELIFE module |
| `rc` | 3, 7 | Retrospective Children History | SHARELIFE module |
| `re` | 3, 7 | Retrospective Employment | SHARELIFE module |
| `rp` | 3, 7 | Retrospective Partner History | SHARELIFE module |
| `wq` | 3, 7 | Work Quality | SHARELIFE module |
| `ra` | 7 | Retrospective Accommodation | wave 7 name used to avoid collision with regular `ac` |
| `cc` | 7 | Childhood Circumstances | wave 7 name used to avoid collision with regular `cs` |
| `rh` | 7 | Retrospective Health Care | wave 7 name used to avoid collision with regular `hc` |

### Generated modules

These modules are already processed or harmonised by SHARE and therefore often easier to use than the raw questionnaire variables.

| `pyshare` module | Waves | Meaning | Load this when you need... |
| --- | --- | --- | --- |
| `gv_weights` | 1-9 | Cross-sectional weights | survey weights for a specific wave |
| `gv_imputations` | 1, 2, 4-9 | Multiple imputations | harmonised imputed economic variables |
| `gv_isced` | 1, 2, 4-9 | ISCED education recodes | comparable education coding |
| `gv_health` | 1, 2, 4-9 | Generated health indicators | BMI, grip summaries, cognition summaries, health indices |
| `gv_housing` | 1, 2, 4-9 | Housing generated variables | harmonised housing indicators and NUTS codes |
| `gv_networks` | 4, 6, 8, 9 | Generated social network variables | network summaries and linked alters |
| `gv_exrates` | 1-9 | Exchange rates and PPP variables | currency conversion inputs, keyed by `country` |
| `gv_grossnet` | 1 | Net income derived from gross income | wave 1 only |
| `gv_isco` | 1 | Occupation/industry coding | wave 1 only |
| `gv_ssw` | 4 | Social security wealth | wave 4 only |
| `gv_deprivation` | 5 | Material and social deprivation | wave 5 only |
| `gv_children` | 4-9 | Generated child-level summaries | harmonised child information across CH, SN, SP, FT |
| `gv_dbs` | 6 | Dried blood spot generated variables | DBS process and expected values |
| `gv_big5` | 7-9 | Big Five traits | personality indicators derived from activities items |
| `gv_accelerometer_total` | 8 | Accelerometer summary dataset | respondent-level physical activity summaries |
| `gv_accelerometer_day` | 8 | Accelerometer day-level dataset | one row per respondent-day |
| `gv_accelerometer_hour` | 8 | Accelerometer hour-level dataset | one row per respondent-hour |
| `gv_accelerometer_sleep` | 8 | Accelerometer sleep dataset | sleep-interval outputs |

## Discovery workflow in `pyshare`

Use `available_share_modules()` to inspect what exists in a wave, then load only the modules you need.

```py
import pyshare as ps

ps.available_share_modules(9)
# ['ac', 'as', 'br', 'cf', 'ch', 'co', 'cv_r', 'dn', 'dropoff', ...]

ps.available_share_modules(9, include_derived=True)
# adds 'gv_*' modules such as 'gv_weights' and 'gv_health'

health = ps.read_share_wave(
    wave=9,
    modules=["cv_r", "dn", "ph", "hc", "mh", "cf"],
)
```

Once you know which module you need, use the [variable dictionary](./variables/index.md) to look up the exact variable labels inside that module for a specific wave.

## Practical rules of thumb

- If you want original questionnaire variables, start with the short thematic modules such as `dn`, `ph`, `ep`, `sp`, and `ft`.
- If you want a cleaned summary output, check whether a `gv_` module already provides it.
- If you are working with wave 3, always verify whether the module is a SHARELIFE retrospective module rather than a regular-wave module with the same short name.
- If a dataset is not one row per `mergeid`, load it separately with `read_share_module()` and merge it manually on the right key.

The descriptions on this page follow the SHARE Release Guide 9.0.0, chapter 12 on variable naming and chapter 13 on questionnaire modules, plus the module names present in the local `data/` directory.
