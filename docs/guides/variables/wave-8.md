---
icon: lucide/list-tree
---

# Wave 8 Variable Dictionary

This page is generated from the local SHARE wave 8 release `9-0-0` Stata files.

It covers 40 datasets and 7,025 variable entries for the files currently available in `data/`.

[Back to variable dictionary](./index.md)

## Overview

| Module | Category | Meaning | Key | Variables | Rows | File |
| --- | --- | --- | --- | --- | --- | --- |
| `ac` | core | Activities | `mergeid` | 48 | 53,695 | `sharew8_rel9-0-0_ac.dta` |
| `as` | core | Assets | `mergeid` | 95 | 53,695 | `sharew8_rel9-0-0_as.dta` |
| `br` | core | Behavioural Risks | `mergeid` | 25 | 53,695 | `sharew8_rel9-0-0_br.dta` |
| `cf` | core | Cognitive Function | `mergeid` | 75 | 53,695 | `sharew8_rel9-0-0_cf.dta` |
| `ch` | core | Children | `mergeid` | 1,516 | 53,695 | `sharew8_rel9-0-0_ch.dta` |
| `co` | core | Consumption | `mergeid` | 27 | 53,695 | `sharew8_rel9-0-0_co.dta` |
| `cv_r` | core | Coverscreen on individual level | `mergeid` | 64 | 106,436 | `sharew8_rel9-0-0_cv_r.dta` |
| `dn` | core | Demographics | `mergeid` | 144 | 53,695 | `sharew8_rel9-0-0_dn.dta` |
| `ep` | core | Employment and Pensions | `mergeid` | 403 | 53,695 | `sharew8_rel9-0-0_ep.dta` |
| `ex` | core | Expectations | `mergeid` | 26 | 53,695 | `sharew8_rel9-0-0_ex.dta` |
| `ft` | core | Financial Transfers | `mergeid` | 69 | 53,695 | `sharew8_rel9-0-0_ft.dta` |
| `gs` | core | Grip Strength | `mergeid` | 23 | 53,695 | `sharew8_rel9-0-0_gs.dta` |
| `hc` | core | Health Care | `mergeid` | 67 | 53,695 | `sharew8_rel9-0-0_hc.dta` |
| `hh` | core | Household Income | `mergeid` | 20 | 53,695 | `sharew8_rel9-0-0_hh.dta` |
| `ho` | core | Housing | `mergeid` | 127 | 53,695 | `sharew8_rel9-0-0_ho.dta` |
| `it` | core | Computer Use | `mergeid` | 10 | 53,695 | `sharew8_rel9-0-0_it.dta` |
| `iv` | core | Interviewer Observations | `mergeid` | 27 | 53,695 | `sharew8_rel9-0-0_iv.dta` |
| `mh` | core | Mental Health | `mergeid` | 27 | 53,695 | `sharew8_rel9-0-0_mh.dta` |
| `ph` | core | Physical Health | `mergeid` | 196 | 53,695 | `sharew8_rel9-0-0_ph.dta` |
| `sn` | core | Social Networks | `mergeid` | 106 | 53,695 | `sharew8_rel9-0-0_sn.dta` |
| `sp` | core | Social Support | `mergeid` | 174 | 53,695 | `sharew8_rel9-0-0_sp.dta` |
| `sr` | core | Saving Regrets | `mergeid` | 58 | 53,695 | `sharew8_rel9-0-0_sr.dta` |
| `te` | core | Time Expenditure | `mergeid` | 40 | 53,695 | `sharew8_rel9-0-0_te.dta` |
| `xt` | core | End-of-Life Interview | `mergeid` | 202 | 4,175 | `sharew8_rel9-0-0_xt.dta` |
| `ax` | special | Accelerometry | `mergeid` | 16 | 53,695 | `sharew8_rel9-0-0_ax.dta` |
| `dropoff` | special | Paper-and-pencil drop-off | `mergeid` | 860 | 34,873 | `sharew8_rel9-0-0_dropoff.dta` |
| `technical_variables` | special | Technical variables | `mergeid` | 19 | 53,695 | `sharew8_rel9-0-0_technical_variables.dta` |
| `gv_accelerometer_day` | generated | Accelerometer day-level dataset | `mergeid` + `measurementday` | 320 | 5,945 | `sharew8_rel9-0-0_gv_accelerometer_day.dta` |
| `gv_accelerometer_hour` | generated | Accelerometer hour-level dataset | `mergeid` + hour-level repeated rows | 281 | 142,680 | `sharew8_rel9-0-0_gv_accelerometer_hour.dta` |
| `gv_accelerometer_sleep` | generated | Accelerometer sleep dataset | `mergeid` + sleep-interval repeated rows | 11 | 6,254 | `sharew8_rel9-0-0_gv_accelerometer_sleep.dta` |
| `gv_accelerometer_total` | generated | Accelerometer summary dataset | `mergeid` | 271 | 855 | `sharew8_rel9-0-0_gv_accelerometer_total.dta` |
| `gv_big5` | generated | Big Five traits | `mergeid` | 11 | 53,695 | `sharew8_rel9-0-0_gv_big5.dta` |
| `gv_children` | generated | Generated child-level summaries | `mergeid` | 947 | 53,695 | `sharew8_rel9-0-0_gv_children.dta` |
| `gv_exrates` | generated | Exchange rates and PPP variables | `country` | 76 | 29 | `sharew8_rel9-0-0_gv_exrates.dta` |
| `gv_health` | generated | Generated health indicators | `mergeid` | 43 | 53,695 | `sharew8_rel9-0-0_gv_health.dta` |
| `gv_housing` | generated | Housing generated variables | `mergeid` | 10 | 53,695 | `sharew8_rel9-0-0_gv_housing.dta` |
| `gv_imputations` | generated | Multiple imputations | `mergeid` | 299 | 268,475 | `sharew8_rel9-0-0_gv_imputations.dta` |
| `gv_isced` | generated | ISCED education recodes | `mergeid` | 54 | 53,695 | `sharew8_rel9-0-0_gv_isced.dta` |
| `gv_networks` | generated | Generated social network variables | `mergeid` | 222 | 53,695 | `sharew8_rel9-0-0_gv_networks.dta` |
| `gv_weights` | generated | Cross-sectional weights | `mergeid` | 16 | 53,695 | `sharew8_rel9-0-0_gv_weights.dta` |

## Core Interview Modules

### `ac` - Activities

- Dataset: `sharew8_rel9-0-0_ac.dta`
- Read with: `ps.read_share_module("ac", wave=8)`
- Rows: 53,695
- Variables: 48
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ac012_` | How satisfied with life | `Numeric(Byte)` | `%10.0g` |
| `ac014_` | Age prevents from doing things | `Numeric(Byte)` | `%11.0g` |
| `ac015_` | Out of control | `Numeric(Byte)` | `%11.0g` |
| `ac016_` | Feel left out of things | `Numeric(Byte)` | `%11.0g` |
| `ac017_` | Do the things you want to do | `Numeric(Byte)` | `%11.0g` |
| `ac018_` | Family responsibilities prevent | `Numeric(Byte)` | `%11.0g` |
| `ac019_` | Shortage of money stops | `Numeric(Byte)` | `%11.0g` |
| `ac020_` | Look forward to each day | `Numeric(Byte)` | `%11.0g` |
| `ac021_` | Life has meaning | `Numeric(Byte)` | `%11.0g` |
| `ac022_` | Look back on life with happiness | `Numeric(Byte)` | `%11.0g` |
| `ac023_` | Feel full of energy | `Numeric(Byte)` | `%11.0g` |
| `ac024_` | Full of opportunities | `Numeric(Byte)` | `%11.0g` |
| `ac025_` | Future looks good | `Numeric(Byte)` | `%11.0g` |
| `ac035d1` | Activities in last year: done voluntary or charity work | `Numeric(Byte)` | `%12.0g` |
| `ac035d4` | Activities in last year: attended an educational or training course | `Numeric(Byte)` | `%12.0g` |
| `ac035d5` | Activities in last year: gone to a sport, social or other kind of club | `Numeric(Byte)` | `%12.0g` |
| `ac035d7` | Activities in last year: taken part in a political or community-related organiza | `Numeric(Byte)` | `%12.0g` |
| `ac035d8` | Activities in last year: read books, magazines or newspapers | `Numeric(Byte)` | `%12.0g` |
| `ac035d9` | Activities in last year: did word or number games (crossword puzzles/Sudoku...) | `Numeric(Byte)` | `%12.0g` |
| `ac035d10` | Activities in last year: played cards or games such as chess | `Numeric(Byte)` | `%12.0g` |
| `ac035dno` | Activities in last year: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac036_1` | How often done voluntary/charity work the last 12 months | `Numeric(Byte)` | `%19.0g` |
| `ac036_4` | How often attended an educational or training course the last 12 months | `Numeric(Byte)` | `%19.0g` |
| `ac036_5` | How often gone to a sport/social/other kind of club the last 12 months | `Numeric(Byte)` | `%19.0g` |
| `ac036_7` | How often taken part in a political/community-related organization the last 12 m | `Numeric(Byte)` | `%19.0g` |
| `ac036_8` | How often read books, magazines or newspapers the last 12 months | `Numeric(Byte)` | `%19.0g` |
| `ac036_9` | How often did word or number games the last 12 months | `Numeric(Byte)` | `%19.0g` |
| `ac036_10` | How often played cards or games such as chess the last 12 months | `Numeric(Byte)` | `%19.0g` |
| `ac037_` | Satisfied with activities | `Numeric(Byte)` | `%10.0g` |
| `ac038_` | Satisfied with no activities | `Numeric(Byte)` | `%10.0g` |
| `ac701_` | I see myself as someone who is reserved | `Numeric(Byte)` | `%26.0g` |
| `ac702_` | I see myself as someone who is generally trusting | `Numeric(Byte)` | `%26.0g` |
| `ac703_` | I see myself as someone who tends to be lazy | `Numeric(Byte)` | `%26.0g` |
| `ac704_` | I see myself as someone who is relaxed, handles stress well | `Numeric(Byte)` | `%26.0g` |
| `ac705_` | I see myself as someone who has few artistic interests | `Numeric(Byte)` | `%26.0g` |
| `ac706_` | I see myself as someone who is outgoing, sociable | `Numeric(Byte)` | `%26.0g` |
| `ac707_` | I see myself as someone who tends to find fault with others | `Numeric(Byte)` | `%26.0g` |
| `ac708_` | I see myself as someone who does a thorough job | `Numeric(Byte)` | `%26.0g` |
| `ac709_` | I see myself as someone who gets nervous easily | `Numeric(Byte)` | `%26.0g` |
| `ac710_` | I see myself as someone who has an active imagination | `Numeric(Byte)` | `%26.0g` |
| `ac711_` | I see myself as someone who is considerate and kind to almost everyone | `Numeric(Byte)` | `%26.0g` |
| `ac740_` | Who answered questions in ac | `Numeric(Byte)` | `%62.0g` |

### `as` - Assets

- Dataset: `sharew8_rel9-0-0_as.dta`
- Read with: `ps.read_share_module("as", wave=8)`
- Rows: 53,695
- Variables: 95
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `as003e` | Amount bank account | `Numeric(Float)` | `%10.0g` |
| `as003ub` | Amount bank account ub | `Numeric(Byte)` | `%32.0g` |
| `as003v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as003v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as003v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as007e` | Amount in bonds | `Numeric(Float)` | `%10.0g` |
| `as007ub` | Amount in bonds ub | `Numeric(Byte)` | `%32.0g` |
| `as007v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as007v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as007v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `as011e` | Amount in stocks | `Numeric(Float)` | `%10.0g` |
| `as011ub` | Amount in stocks ub | `Numeric(Byte)` | `%32.0g` |
| `as011v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as011v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as011v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `as017e` | Amount in mutual funds | `Numeric(Float)` | `%10.0g` |
| `as017ub` | Amount in mutual funds ub | `Numeric(Byte)` | `%32.0g` |
| `as017v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as017v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as017v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `as019_` | Mutual funds mostly stocks or bonds | `Numeric(Byte)` | `%32.0g` |
| `as020_` | Who has individual retirement accounts | `Numeric(Byte)` | `%25.0g` |
| `as021e` | Amount individual retirement accounts | `Numeric(Float)` | `%10.0g` |
| `as021ub` | Amount individual retirement accounts ub | `Numeric(Byte)` | `%32.0g` |
| `as021v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as021v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as021v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as023_` | Individual retirement accounts mostly in stocks or bonds | `Numeric(Byte)` | `%32.0g` |
| `as024e` | Partner amount individual retirement accounts | `Numeric(Float)` | `%10.0g` |
| `as024ub` | Partner amount individual retirement accounts ub | `Numeric(Byte)` | `%32.0g` |
| `as024v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as024v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as024v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as026_` | Partner individual retirement accounts mostly in stocks or bonds | `Numeric(Byte)` | `%32.0g` |
| `as027e` | Amount contractual saving for housing | `Numeric(Float)` | `%10.0g` |
| `as027ub` | Amount contractual saving for housing ub | `Numeric(Byte)` | `%32.0g` |
| `as027v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as027v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as027v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as029_` | Life insurance policies term or whole life | `Numeric(Byte)` | `%23.0g` |
| `as030e` | Face value of whole life policies | `Numeric(Float)` | `%10.0g` |
| `as030ub` | Face value of whole life policies ub | `Numeric(Byte)` | `%32.0g` |
| `as030v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as030v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as030v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `as044_` | Percentage share firm owned | `Numeric(Byte)` | `%10.0g` |
| `as044ub` | Percentage share firm owned ub | `Numeric(Byte)` | `%32.0g` |
| `as044v1` | Bracket value 1 | `Numeric(Byte)` | `%8.0g` |
| `as044v2` | Bracket value 2 | `Numeric(Byte)` | `%8.0g` |
| `as044v3` | Bracket value 3 | `Numeric(Byte)` | `%8.0g` |
| `as051e` | Amount selling cars | `Numeric(Float)` | `%10.0g` |
| `as051ub` | Amount selling cars ub | `Numeric(Byte)` | `%32.0g` |
| `as051v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as051v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as051v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as054d1` | Owe money: debt on cars and other vehicles (vans/motorcycles/boats, etc.) | `Numeric(Byte)` | `%12.0g` |
| `as054d2` | Owe money: debt on credit cards/store cards | `Numeric(Byte)` | `%12.0g` |
| `as054d3` | Owe money: loans (from bank, building society, other financial institution) | `Numeric(Byte)` | `%12.0g` |
| `as054d4` | Owe money: debts to relatives or friends | `Numeric(Byte)` | `%12.0g` |
| `as054d5` | Owe money: student loans | `Numeric(Byte)` | `%12.0g` |
| `as054d6` | Owe money: overdue bills (phone, electricity, heating, rent) | `Numeric(Byte)` | `%12.0g` |
| `as054dno` | Owe money: none of these | `Numeric(Byte)` | `%12.0g` |
| `as054dot` | Owe money: other | `Numeric(Byte)` | `%12.0g` |
| `as055e` | Amount owing money in total | `Numeric(Float)` | `%10.0g` |
| `as055ub` | Amount owing money in total ub | `Numeric(Byte)` | `%32.0g` |
| `as055v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as055v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as055v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `as057_` | Who answered the question in as | `Numeric(Byte)` | `%47.0g` |
| `as060_` | Has bank account | `Numeric(Byte)` | `%10.0g` |
| `as062_` | Has bonds | `Numeric(Byte)` | `%10.0g` |
| `as063_` | Has stocks | `Numeric(Byte)` | `%10.0g` |
| `as064_` | Has mutual funds | `Numeric(Byte)` | `%10.0g` |
| `as065_` | Has individual retirement accounts | `Numeric(Byte)` | `%10.0g` |
| `as066_` | Has contractual saving | `Numeric(Byte)` | `%10.0g` |
| `as067_` | Has life insurance | `Numeric(Byte)` | `%10.0g` |
| `as070e` | Interest or dividend income | `Numeric(Float)` | `%10.0g` |
| `as070ub` | Interest or dividend income ub | `Numeric(Byte)` | `%32.0g` |
| `as070v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `as070v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `as070v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as641_` | Own firm/company/business (entirely or partial ownership) | `Numeric(Byte)` | `%10.0g` |
| `as642e` | Amount selling firm | `Numeric(Float)` | `%10.0g` |
| `as642ub` | Amount selling firm ub | `Numeric(Byte)` | `%32.0g` |
| `as642v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `as642v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as642v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `as649_` | Number of cars | `Numeric(Byte)` | `%10.0g` |

### `br` - Behavioural Risks

- Dataset: `sharew8_rel9-0-0_br.dta`
- Read with: `ps.read_share_module("br", wave=8)`
- Rows: 53,695
- Variables: 25
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `br001_` | Ever smoked daily | `Numeric(Byte)` | `%10.0g` |
| `br002_` | Smoke at the present time | `Numeric(Byte)` | `%10.0g` |
| `br003_` | How many years smoked | `Numeric(Byte)` | `%10.0g` |
| `br005d1` | Do or did smoke: cigarettes | `Numeric(Byte)` | `%12.0g` |
| `br005d2` | Do or did smoke: pipe | `Numeric(Byte)` | `%12.0g` |
| `br005d3` | Do or did smoke: cigars or cigarillos | `Numeric(Byte)` | `%12.0g` |
| `br005d4` | Do or did smoke: e-cigarettes with nicotine solution | `Numeric(Byte)` | `%12.0g` |
| `br006_` | Average amount of cigarettes per day | `Numeric(Int)` | `%10.0g` |
| `br015_` | Sports or activities that are vigorous | `Numeric(Byte)` | `%31.0g` |
| `br016_` | Activities requiring a moderate level of energy | `Numeric(Byte)` | `%31.0g` |
| `br017_` | Who answered the questions in br | `Numeric(Byte)` | `%47.0g` |
| `br026_` | How often serving of dairy products | `Numeric(Byte)` | `%34.0g` |
| `br027_` | How often serving of legumes or eggs | `Numeric(Byte)` | `%34.0g` |
| `br028_` | How often serving of meat, fish or chicken | `Numeric(Byte)` | `%34.0g` |
| `br029_` | How often serving of fruits or vegetables | `Numeric(Byte)` | `%34.0g` |
| `br033_` | Not eating meat, fish or chicken more often because ... | `Numeric(Byte)` | `%73.0g` |
| `br039_` | At least one alcoholic beverage the last 7 days | `Numeric(Byte)` | `%10.0g` |
| `br040_` | Units of alcoholic beverage the last seven days | `Numeric(Int)` | `%10.0g` |
| `br623_` | How often 6 or more drinks the last 3 months | `Numeric(Byte)` | `%48.0g` |

### `cf` - Cognitive Function

- Dataset: `sharew8_rel9-0-0_cf.dta`
- Read with: `ps.read_share_module("cf", wave=8)`
- Rows: 53,695
- Variables: 75
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `cf001_` | Self-rated reading skills | `Numeric(Byte)` | `%16.0g` |
| `cf002_` | Self-rated writing skills | `Numeric(Byte)` | `%16.0g` |
| `cf003_` | Date: day of month | `Numeric(Byte)` | `%50.0g` |
| `cf004_` | Date: month | `Numeric(Byte)` | `%50.0g` |
| `cf005_` | Date: year | `Numeric(Byte)` | `%48.0g` |
| `cf006_` | Date: day of the week | `Numeric(Byte)` | `%58.0g` |
| `cf010_` | Verbal fluency score: number of animals | `Numeric(Byte)` | `%10.0g` |
| `cf012_` | Numeracy: chance disease 10% of 1000 | `Numeric(Byte)` | `%19.0g` |
| `cf013_` | Numeracy: half price | `Numeric(Byte)` | `%19.0g` |
| `cf014_` | Numeracy: 6000 is two-thirds what is total price | `Numeric(Byte)` | `%21.0g` |
| `cf015_` | Numeracy: amount in the savings account | `Numeric(Byte)` | `%20.0g` |
| `cf017_` | Contextual factors during the cognitive function test | `Numeric(Byte)` | `%10.0g` |
| `cf018d1` | Who present during cf: respondent alone | `Numeric(Byte)` | `%12.0g` |
| `cf018d2` | Who present during cf: partner present | `Numeric(Byte)` | `%12.0g` |
| `cf018d3` | Who present during cf: child(ren) present | `Numeric(Byte)` | `%12.0g` |
| `cf018d4` | Who present during cf: other(s) | `Numeric(Byte)` | `%12.0g` |
| `cf103_` | Memory | `Numeric(Byte)` | `%16.0g` |
| `cf104tot` | Ten words list learning first trail | `Numeric(Byte)` | `%9.0g` |
| `cf105tot` | Ten words list learning first trail | `Numeric(Byte)` | `%9.0g` |
| `cf106tot` | Ten words list learning first trail | `Numeric(Byte)` | `%9.0g` |
| `cf107tot` | Ten words list learning first trail | `Numeric(Byte)` | `%9.0g` |
| `cf108_` | Numeracy: subtraction 1 | `Numeric(Double)` | `%10.0g` |
| `cf109_` | Numeracy: subtraction 2 | `Numeric(Double)` | `%10.0g` |
| `cf110_` | Numeracy: subtraction 3 | `Numeric(Double)` | `%10.0g` |
| `cf111_` | Numeracy: subtraction 4 | `Numeric(Double)` | `%10.0g` |
| `cf112_` | Numeracy: subtraction 5 | `Numeric(Long)` | `%10.0g` |
| `cf113tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `cf114tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `cf115tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `cf116tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `cf719_` | Who answered questions in cf | `Numeric(Byte)` | `%62.0g` |
| `cf820_` | Self-rated memory change | `Numeric(Byte)` | `%13.0g` |
| `cf821_` | Counting backwards: intro 1 | `Numeric(Byte)` | `%10.0g` |
| `cf822_` | Counting backwards: trail 1 end | `Numeric(Byte)` | `%10.0g` |
| `cf823_` | Counting backwards: stop 1 | `Numeric(Byte)` | `%23.0g` |
| `cf824_` | Counting backwards: intro 2 | `Numeric(Byte)` | `%10.0g` |
| `cf825_` | Counting backwards: trail 2 end | `Numeric(Byte)` | `%10.0g` |
| `cf826_` | Counting backwards: stop 2 | `Numeric(Byte)` | `%13.0g` |
| `cf827_` | Describe object: scissors | `Numeric(Byte)` | `%37.0g` |
| `cf828_` | Describe object: cactus | `Numeric(Byte)` | `%56.0g` |
| `cf829_` | Describe object: pharmacy | `Numeric(Byte)` | `%38.0g` |
| `cf830_` | Draw: infinity | `Numeric(Byte)` | `%96.0g` |
| `cf831_` | Draw: cube | `Numeric(Byte)` | `%130.0g` |
| `cf832_` | Draw: clock face intro | `Numeric(Byte)` | `%10.0g` |
| `cf833_` | Draw: clock face all correct | `Numeric(Byte)` | `%97.0g` |
| `cf834_` | Draw: clock face numbers correct | `Numeric(Byte)` | `%10.0g` |
| `cf835_` | Draw: clock face circle correct | `Numeric(Byte)` | `%10.0g` |
| `cf836_` | Draw: clock hands intro | `Numeric(Byte)` | `%10.0g` |
| `cf837_` | Draw: clock hands all correct | `Numeric(Byte)` | `%10.0g` |
| `cf838_` | Draw: clock hands length interchanged | `Numeric(Byte)` | `%10.0g` |
| `cf839_` | Draw: clock hands one hand correct | `Numeric(Byte)` | `%10.0g` |
| `cf841_` | Proxy: respondent's memory | `Numeric(Byte)` | `%16.0g` |
| `cf842_` | Proxy: respondent's memory change | `Numeric(Byte)` | `%13.0g` |
| `cf843_` | Proxy: respondent's memory family | `Numeric(Byte)` | `%57.0g` |
| `cf844_` | Proxy: respondent's memory events | `Numeric(Byte)` | `%57.0g` |
| `cf845_` | Proxy: srespondent's memory conversations | `Numeric(Byte)` | `%57.0g` |
| `cf846_` | Proxy: respondent's memory date | `Numeric(Byte)` | `%57.0g` |
| `cf847_` | Proxy: respondent's memory learning | `Numeric(Byte)` | `%57.0g` |
| `cf848_` | Proxy: respondent's memory decisions | `Numeric(Byte)` | `%57.0g` |
| `cf849_` | Proxy: respondent's memory finances | `Numeric(Byte)` | `%57.0g` |
| `cf850_` | Proxy: R gets lost | `Numeric(Byte)` | `%10.0g` |
| `cf851_` | Proxy: R wanders off | `Numeric(Byte)` | `%10.0g` |
| `cf852_` | Proxy: R can be left alone | `Numeric(Byte)` | `%10.0g` |
| `cf853_` | Proxy: R hears or sees things that do not exist | `Numeric(Byte)` | `%10.0g` |
| `cf855d1` | Who present in addition to proxy: proxy alone | `Numeric(Byte)` | `%12.0g` |
| `cf855d2` | Who present in addition to proxy: respondent | `Numeric(Byte)` | `%12.0g` |
| `cf855d3` | Who present in addition to proxy: partner | `Numeric(Byte)` | `%12.0g` |
| `cf855d4` | Who present in addition to proxy: child(ren) | `Numeric(Byte)` | `%12.0g` |
| `cf855d5` | Who present in addition to proxy: other(s) | `Numeric(Byte)` | `%12.0g` |

### `ch` - Children

- Dataset: `sharew8_rel9-0-0_ch.dta`
- Read with: `ps.read_share_module("ch", wave=8)`
- Rows: 53,695
- Variables: 1,516
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `childid_1` | Child identifier (fix across modules and waves): Child 1 | `Str(14)` | `%14s` |
| `childid_2` | Child identifier (fix across modules and waves): Child 2 | `Str(14)` | `%14s` |
| `childid_3` | Child identifier (fix across modules and waves): Child 3 | `Str(14)` | `%14s` |
| `childid_4` | Child identifier (fix across modules and waves): Child 4 | `Str(14)` | `%14s` |
| `childid_5` | Child identifier (fix across modules and waves): Child 5 | `Str(14)` | `%14s` |
| `childid_6` | Child identifier (fix across modules and waves): Child 6 | `Str(14)` | `%14s` |
| `childid_7` | Child identifier (fix across modules and waves): Child 7 | `Str(14)` | `%14s` |
| `childid_8` | Child identifier (fix across modules and waves): Child 8 | `Str(14)` | `%14s` |
| `childid_9` | Child identifier (fix across modules and waves): Child 9 | `Str(14)` | `%14s` |
| `childid_10` | Child identifier (fix across modules and waves): Child 10 | `Str(14)` | `%14s` |
| `childid_11` | Child identifier (fix across modules and waves): Child 11 | `Str(14)` | `%14s` |
| `childid_12` | Child identifier (fix across modules and waves): Child 12 | `Str(14)` | `%14s` |
| `childid_13` | Child identifier (fix across modules and waves): Child 13 | `Str(14)` | `%14s` |
| `childid_14` | Child identifier (fix across modules and waves): Child 14 | `Str(14)` | `%14s` |
| `childid_15` | Child identifier (fix across modules and waves): Child 15 | `Str(14)` | `%14s` |
| `childid_16` | Child identifier (fix across modules and waves): Child 16 | `Str(14)` | `%14s` |
| `childid_17` | Child identifier (fix across modules and waves): Child 17 | `Str(14)` | `%14s` |
| `childid_18` | Child identifier (fix across modules and waves): Child 18 | `Str(14)` | `%14s` |
| `childid_19` | Child identifier (fix across modules and waves): Child 19 | `Str(1)` | `%9s` |
| `childid_20` | Child identifier (fix across modules and waves): Child 20 | `Str(14)` | `%14s` |
| `ch001_` | Number of children | `Numeric(Byte)` | `%10.0g` |
| `ch005_1` | Child 1 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_2` | Child 2 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_3` | Child 3 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_4` | Child 4 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_5` | Child 5 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_6` | Child 6 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_7` | Child 7 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_8` | Child 8 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_9` | Child 9 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_10` | Child 10 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_11` | Child 11 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_12` | Child 12 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_13` | Child 13 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_14` | Child 14 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_15` | Child 15 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_16` | Child 16 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_17` | Child 17 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_18` | Child 18 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_19` | Child 19 gender | `Numeric(Byte)` | `%12.0g` |
| `ch005_20` | Child 20 gender | `Numeric(Byte)` | `%12.0g` |
| `ch006_1` | Child 1 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_2` | Child 2 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_3` | Child 3 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_4` | Child 4 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_5` | Child 5 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_6` | Child 6 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_7` | Child 7 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_8` | Child 8 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_9` | Child 9 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_10` | Child 10 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_11` | Child 11 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_12` | Child 12 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_13` | Child 13 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_14` | Child 14 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_15` | Child 15 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_16` | Child 16 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_17` | Child 17 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_18` | Child 18 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_19` | Child 19 year of birth | `Numeric(Byte)` | `%10.0g` |
| `ch006_20` | Child 20 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch007_1` | Child 1 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_2` | Child 2 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_3` | Child 3 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_4` | Child 4 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_5` | Child 5 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_6` | Child 6 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_7` | Child 7 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_8` | Child 8 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_9` | Child 9 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_10` | Child 10 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_11` | Child 11 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_12` | Child 12 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_13` | Child 13 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_14` | Child 14 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_15` | Child 15 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_16` | Child 16 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_17` | Child 17 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_18` | Child 18 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_19` | Child 19 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_20` | Child 20 where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch012_1` | Child 1 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_2` | Child 2 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_3` | Child 3 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_4` | Child 4 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_5` | Child 5 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_6` | Child 6 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_7` | Child 7 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_8` | Child 8 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_9` | Child 9 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_10` | Child 10 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_11` | Child 11 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_12` | Child 12 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_13` | Child 13 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_14` | Child 14 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_15` | Child 15 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_16` | Child 16 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_17` | Child 17 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_18` | Child 18 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_19` | Child 19 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch012_20` | Child 20 marital status | `Numeric(Byte)` | `%59.0g` |
| `ch013_1` | Child 1 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_2` | Child 2 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_3` | Child 3 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_4` | Child 4 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_5` | Child 5 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_6` | Child 6 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_7` | Child 7 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_8` | Child 8 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_9` | Child 9 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_10` | Child 10 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_11` | Child 11 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_12` | Child 12 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_13` | Child 13 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_14` | Child 14 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_15` | Child 15 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_16` | Child 16 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_17` | Child 17 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_18` | Child 18 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_19` | Child 19 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_20` | Child 20 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch014_1` | Child 1 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_2` | Child 2 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_3` | Child 3 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_4` | Child 4 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_5` | Child 5 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_6` | Child 6 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_7` | Child 7 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_8` | Child 8 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_9` | Child 9 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_10` | Child 10 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_11` | Child 11 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_12` | Child 12 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_13` | Child 13 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_14` | Child 14 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_15` | Child 15 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_16` | Child 16 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_17` | Child 17 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_18` | Child 18 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_19` | Child 19 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch014_20` | Child 20 contact with child | `Numeric(Byte)` | `%30.0g` |
| `ch015_1` | Child 1 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_2` | Child 2 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_3` | Child 3 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_4` | Child 4 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_5` | Child 5 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_6` | Child 6 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_7` | Child 7 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_8` | Child 8 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_9` | Child 9 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_10` | Child 10 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_11` | Child 11 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_12` | Child 12 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_13` | Child 13 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_14` | Child 14 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_15` | Child 15 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_16` | Child 16 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_17` | Child 17 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_18` | Child 18 year moved out | `Numeric(Byte)` | `%33.0g` |
| `ch015_19` | Child 19 year moved out | `Numeric(Byte)` | `%33.0g` |
| `ch015_20` | Child 20 year moved out | `Numeric(Byte)` | `%33.0g` |
| `ch016_1` | Child 1 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_2` | Child 2 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_3` | Child 3 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_4` | Child 4 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_5` | Child 5 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_6` | Child 6 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_7` | Child 7 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_8` | Child 8 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_9` | Child 9 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_10` | Child 10 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_11` | Child 11 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_12` | Child 12 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_13` | Child 13 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_14` | Child 14 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_15` | Child 15 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_16` | Child 16 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_17` | Child 17 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_18` | Child 18 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_19` | Child 19 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch016_20` | Child 20 employment status | `Numeric(Byte)` | `%61.0g` |
| `ch017_1` | Child 1 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_2` | Child 2 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_3` | Child 3 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_4` | Child 4 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_5` | Child 5 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_6` | Child 6 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_7` | Child 7 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_8` | Child 8 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_9` | Child 9 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_10` | Child 10 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_11` | Child 11 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_12` | Child 12 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_13` | Child 13 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_14` | Child 14 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_15` | Child 15 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_16` | Child 16 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_17` | Child 17 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_18` | Child 18 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_19` | Child 19 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch017_20` | Child 20 highest school degree | `Numeric(Byte)` | `%167.0g` |
| `ch018d1_1` | Child 1 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_2` | Child 2 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_3` | Child 3 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_4` | Child 4 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_5` | Child 5 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_6` | Child 6 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_7` | Child 7 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_8` | Child 8 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_9` | Child 9 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_10` | Child 10 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_11` | Child 11 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_12` | Child 12 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_13` | Child 13 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_14` | Child 14 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_15` | Child 15 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_16` | Child 16 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_17` | Child 17 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_18` | Child 18 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_19` | Child 19 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_20` | Child 20 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_1` | Child 1 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_2` | Child 2 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_3` | Child 3 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_4` | Child 4 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_5` | Child 5 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_6` | Child 6 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_7` | Child 7 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_8` | Child 8 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_9` | Child 9 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_10` | Child 10 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_11` | Child 11 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_12` | Child 12 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_13` | Child 13 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_14` | Child 14 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_15` | Child 15 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_16` | Child 16 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_17` | Child 17 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_18` | Child 18 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_19` | Child 19 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_20` | Child 20 further education: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_1` | Child 1 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_2` | Child 2 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_3` | Child 3 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_4` | Child 4 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_5` | Child 5 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_6` | Child 6 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_7` | Child 7 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_8` | Child 8 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_9` | Child 9 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_10` | Child 10 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_11` | Child 11 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_12` | Child 12 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_13` | Child 13 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_14` | Child 14 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_15` | Child 15 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_16` | Child 16 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_17` | Child 17 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_18` | Child 18 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_19` | Child 19 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_20` | Child 20 further education: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_1` | Child 1 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_2` | Child 2 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_3` | Child 3 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_4` | Child 4 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_5` | Child 5 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_6` | Child 6 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_7` | Child 7 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_8` | Child 8 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_9` | Child 9 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_10` | Child 10 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_11` | Child 11 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_12` | Child 12 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_13` | Child 13 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_14` | Child 14 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_15` | Child 15 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_16` | Child 16 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_17` | Child 17 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_18` | Child 18 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_19` | Child 19 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_20` | Child 20 further education: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_1` | Child 1 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_2` | Child 2 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_3` | Child 3 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_4` | Child 4 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_5` | Child 5 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_6` | Child 6 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_7` | Child 7 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_8` | Child 8 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_9` | Child 9 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_10` | Child 10 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_11` | Child 11 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_12` | Child 12 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_13` | Child 13 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_14` | Child 14 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_15` | Child 15 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_16` | Child 16 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_17` | Child 17 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_18` | Child 18 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_19` | Child 19 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_20` | Child 20 further education: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_1` | Child 1 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_2` | Child 2 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_3` | Child 3 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_4` | Child 4 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_5` | Child 5 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_6` | Child 6 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_7` | Child 7 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_8` | Child 8 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_9` | Child 9 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_10` | Child 10 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_11` | Child 11 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_12` | Child 12 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_13` | Child 13 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_14` | Child 14 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_15` | Child 15 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_16` | Child 16 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_17` | Child 17 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_18` | Child 18 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_19` | Child 19 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_20` | Child 20 further education: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_1` | Child 1 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_2` | Child 2 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_3` | Child 3 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_4` | Child 4 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_5` | Child 5 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_6` | Child 6 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_7` | Child 7 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_8` | Child 8 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_9` | Child 9 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_10` | Child 10 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_11` | Child 11 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_12` | Child 12 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_13` | Child 13 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_14` | Child 14 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_15` | Child 15 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_16` | Child 16 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_17` | Child 17 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_18` | Child 18 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_19` | Child 19 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_20` | Child 20 further education: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_1` | Child 1 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_2` | Child 2 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_3` | Child 3 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_4` | Child 4 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_5` | Child 5 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_6` | Child 6 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_7` | Child 7 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_8` | Child 8 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_9` | Child 9 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_10` | Child 10 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_11` | Child 11 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_12` | Child 12 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_13` | Child 13 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_14` | Child 14 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_15` | Child 15 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_16` | Child 16 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_17` | Child 17 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_18` | Child 18 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_19` | Child 19 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_20` | Child 20 further education: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_1` | Child 1 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_2` | Child 2 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_3` | Child 3 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_4` | Child 4 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_5` | Child 5 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_6` | Child 6 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_7` | Child 7 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_8` | Child 8 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_9` | Child 9 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_10` | Child 10 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_11` | Child 11 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_12` | Child 12 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_13` | Child 13 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_14` | Child 14 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_15` | Child 15 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_16` | Child 16 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_17` | Child 17 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_18` | Child 18 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_19` | Child 19 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_20` | Child 20 further education: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_1` | Child 1 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_2` | Child 2 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_3` | Child 3 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_4` | Child 4 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_5` | Child 5 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_6` | Child 6 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_7` | Child 7 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_8` | Child 8 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_9` | Child 9 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_10` | Child 10 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_11` | Child 11 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_12` | Child 12 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_13` | Child 13 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_14` | Child 14 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_15` | Child 15 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_16` | Child 16 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_17` | Child 17 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_18` | Child 18 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_19` | Child 19 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_20` | Child 20 further education: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_1` | Child 1 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_2` | Child 2 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_3` | Child 3 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_4` | Child 4 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_5` | Child 5 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_6` | Child 6 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_7` | Child 7 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_8` | Child 8 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_9` | Child 9 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_10` | Child 10 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_11` | Child 11 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_12` | Child 12 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_13` | Child 13 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_14` | Child 14 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_15` | Child 15 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_16` | Child 16 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_17` | Child 17 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_18` | Child 18 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_19` | Child 19 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_20` | Child 20 further education: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_1` | Child 1 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_2` | Child 2 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_3` | Child 3 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_4` | Child 4 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_5` | Child 5 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_6` | Child 6 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_7` | Child 7 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_8` | Child 8 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_9` | Child 9 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_10` | Child 10 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_11` | Child 11 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_12` | Child 12 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_13` | Child 13 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_14` | Child 14 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_15` | Child 15 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_16` | Child 16 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_17` | Child 17 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_18` | Child 18 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_19` | Child 19 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_20` | Child 20 further education: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_1` | Child 1 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_2` | Child 2 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_3` | Child 3 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_4` | Child 4 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_5` | Child 5 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_6` | Child 6 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_7` | Child 7 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_8` | Child 8 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_9` | Child 9 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_10` | Child 10 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_11` | Child 11 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_12` | Child 12 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_13` | Child 13 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_14` | Child 14 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_15` | Child 15 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_16` | Child 16 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_17` | Child 17 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_18` | Child 18 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_19` | Child 19 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_20` | Child 20 further education: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_1` | Child 1 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_2` | Child 2 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_3` | Child 3 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_4` | Child 4 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_5` | Child 5 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_6` | Child 6 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_7` | Child 7 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_8` | Child 8 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_9` | Child 9 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_10` | Child 10 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_11` | Child 11 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_12` | Child 12 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_13` | Child 13 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_14` | Child 14 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_15` | Child 15 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_16` | Child 16 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_17` | Child 17 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_18` | Child 18 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_19` | Child 19 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_20` | Child 20 further education: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_1` | Child 1 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_2` | Child 2 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_3` | Child 3 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_4` | Child 4 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_5` | Child 5 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_6` | Child 6 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_7` | Child 7 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_8` | Child 8 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_9` | Child 9 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_10` | Child 10 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_11` | Child 11 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_12` | Child 12 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_13` | Child 13 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_14` | Child 14 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_15` | Child 15 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_16` | Child 16 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_17` | Child 17 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_18` | Child 18 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_19` | Child 19 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d15_20` | Child 20 further education: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_1` | Child 1 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_2` | Child 2 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_3` | Child 3 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_4` | Child 4 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_5` | Child 5 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_6` | Child 6 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_7` | Child 7 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_8` | Child 8 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_9` | Child 9 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_10` | Child 10 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_11` | Child 11 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_12` | Child 12 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_13` | Child 13 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_14` | Child 14 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_15` | Child 15 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_16` | Child 16 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_17` | Child 17 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_18` | Child 18 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_19` | Child 19 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d16_20` | Child 20 further education: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_1` | Child 1 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_2` | Child 2 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_3` | Child 3 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_4` | Child 4 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_5` | Child 5 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_6` | Child 6 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_7` | Child 7 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_8` | Child 8 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_9` | Child 9 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_10` | Child 10 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_11` | Child 11 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_12` | Child 12 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_13` | Child 13 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_14` | Child 14 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_15` | Child 15 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_16` | Child 16 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_17` | Child 17 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_18` | Child 18 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_19` | Child 19 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d17_20` | Child 20 further education: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_1` | Child 1 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_2` | Child 2 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_3` | Child 3 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_4` | Child 4 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_5` | Child 5 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_6` | Child 6 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_7` | Child 7 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_8` | Child 8 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_9` | Child 9 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_10` | Child 10 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_11` | Child 11 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_12` | Child 12 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_13` | Child 13 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_14` | Child 14 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_15` | Child 15 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_16` | Child 16 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_17` | Child 17 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_18` | Child 18 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_19` | Child 19 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d18_20` | Child 20 further education: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_1` | Child 1 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_2` | Child 2 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_3` | Child 3 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_4` | Child 4 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_5` | Child 5 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_6` | Child 6 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_7` | Child 7 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_8` | Child 8 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_9` | Child 9 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_10` | Child 10 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_11` | Child 11 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_12` | Child 12 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_13` | Child 13 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_14` | Child 14 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_15` | Child 15 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_16` | Child 16 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_17` | Child 17 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_18` | Child 18 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_19` | Child 19 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d19_20` | Child 20 further education: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_1` | Child 1 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_2` | Child 2 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_3` | Child 3 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_4` | Child 4 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_5` | Child 5 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_6` | Child 6 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_7` | Child 7 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_8` | Child 8 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_9` | Child 9 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_10` | Child 10 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_11` | Child 11 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_12` | Child 12 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_13` | Child 13 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_14` | Child 14 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_15` | Child 15 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_16` | Child 16 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_17` | Child 17 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_18` | Child 18 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_19` | Child 19 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_20` | Child 20 still in higher education | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_1` | Child 1 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_2` | Child 2 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_3` | Child 3 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_4` | Child 4 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_5` | Child 5 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_6` | Child 6 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_7` | Child 7 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_8` | Child 8 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_9` | Child 9 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_10` | Child 10 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_11` | Child 11 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_12` | Child 12 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_13` | Child 13 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_14` | Child 14 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_15` | Child 15 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_16` | Child 16 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_17` | Child 17 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_18` | Child 18 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_19` | Child 19 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_20` | Child 20 higher education: other | `Numeric(Byte)` | `%12.0g` |
| `ch019_1` | Child 1 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_2` | Child 2 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_3` | Child 3 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_4` | Child 4 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_5` | Child 5 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_6` | Child 6 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_7` | Child 7 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_8` | Child 8 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_9` | Child 9 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_10` | Child 10 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_11` | Child 11 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_12` | Child 12 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_13` | Child 13 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_14` | Child 14 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_15` | Child 15 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_16` | Child 16 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_17` | Child 17 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_18` | Child 18 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_19` | Child 19 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_20` | Child 20 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch020_1` | Child 1 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_2` | Child 2 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_3` | Child 3 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_4` | Child 4 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_5` | Child 5 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_6` | Child 6 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_7` | Child 7 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_8` | Child 8 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_9` | Child 9 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_10` | Child 10 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_11` | Child 11 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_12` | Child 12 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_13` | Child 13 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_14` | Child 14 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_15` | Child 15 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_16` | Child 16 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch020_17` | Child 17 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch020_18` | Child 18 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch020_19` | Child 19 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch020_20` | Child 20 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch021_` | Number of grandchildren | `Numeric(Int)` | `%10.0g` |
| `ch022_` | Has great-grandchildren | `Numeric(Byte)` | `%10.0g` |
| `ch023_` | Who answered questions in section CH | `Numeric(Byte)` | `%47.0g` |
| `ch102_1` | Child 1 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_2` | Child 2 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_3` | Child 3 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_4` | Child 4 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_5` | Child 5 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_6` | Child 6 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_7` | Child 7 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_8` | Child 8 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_9` | Child 9 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_10` | Child 10 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_11` | Child 11 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_12` | Child 12 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_13` | Child 13 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_14` | Child 14 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_15` | Child 15 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_16` | Child 16 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_17` | Child 17 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_18` | Child 18 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_19` | Child 19 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch102_20` | Child 20 natural child of R | `Numeric(Byte)` | `%10.0g` |
| `ch103_1` | Child 1 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_2` | Child 2 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_3` | Child 3 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_4` | Child 4 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_5` | Child 5 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_6` | Child 6 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_7` | Child 7 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_8` | Child 8 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_9` | Child 9 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_10` | Child 10 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_11` | Child 11 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_12` | Child 12 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_13` | Child 13 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_14` | Child 14 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_15` | Child 15 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_16` | Child 16 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_17` | Child 17 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_18` | Child 18 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_19` | Child 19 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch103_20` | Child 20 natural child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch104_1` | Child 1 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_2` | Child 2 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_3` | Child 3 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_4` | Child 4 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_5` | Child 5 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_6` | Child 6 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_7` | Child 7 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_8` | Child 8 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_9` | Child 9 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_10` | Child 10 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_11` | Child 11 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_12` | Child 12 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_13` | Child 13 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_14` | Child 14 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_15` | Child 15 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_16` | Child 16 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_17` | Child 17 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_18` | Child 18 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_19` | Child 19 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch104_20` | Child 20 child of former relationship of R | `Numeric(Byte)` | `%10.0g` |
| `ch105_1` | Child 1 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_2` | Child 2 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_3` | Child 3 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_4` | Child 4 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_5` | Child 5 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_6` | Child 6 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_7` | Child 7 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_8` | Child 8 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_9` | Child 9 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_10` | Child 10 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_11` | Child 11 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_12` | Child 12 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_13` | Child 13 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_14` | Child 14 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_15` | Child 15 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_16` | Child 16 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_17` | Child 17 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_18` | Child 18 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_19` | Child 19 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch105_20` | Child 20 child of former relationship of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch106_1` | Child 1 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_2` | Child 2 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_3` | Child 3 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_4` | Child 4 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_5` | Child 5 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_6` | Child 6 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_7` | Child 7 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_8` | Child 8 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_9` | Child 9 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_10` | Child 10 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_11` | Child 11 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_12` | Child 12 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_13` | Child 13 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_14` | Child 14 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_15` | Child 15 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_16` | Child 16 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_17` | Child 17 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_18` | Child 18 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_19` | Child 19 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch106_20` | Child 20 adopted child of R | `Numeric(Byte)` | `%10.0g` |
| `ch107_1` | Child 1 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_2` | Child 2 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_3` | Child 3 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_4` | Child 4 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_5` | Child 5 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_6` | Child 6 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_7` | Child 7 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_8` | Child 8 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_9` | Child 9 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_10` | Child 10 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_11` | Child 11 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_12` | Child 12 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_13` | Child 13 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_14` | Child 14 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_15` | Child 15 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_16` | Child 16 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_17` | Child 17 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_18` | Child 18 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_19` | Child 19 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch107_20` | Child 20 adopted child of current spouse/partner | `Numeric(Byte)` | `%10.0g` |
| `ch108_1` | Child 1 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_2` | Child 2 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_3` | Child 3 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_4` | Child 4 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_5` | Child 5 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_6` | Child 6 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_7` | Child 7 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_8` | Child 8 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_9` | Child 9 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_10` | Child 10 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_11` | Child 11 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_12` | Child 12 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_13` | Child 13 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_14` | Child 14 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_15` | Child 15 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_16` | Child 16 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_17` | Child 17 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_18` | Child 18 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_19` | Child 19 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch108_20` | Child 20 is a foster child | `Numeric(Byte)` | `%10.0g` |
| `ch302_` | All children are natural children | `Numeric(Byte)` | `%10.0g` |
| `ch303d1` | Child 1 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d2` | Child 2 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d3` | Child 3 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d4` | Child 4 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d5` | Child 5 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d6` | Child 6 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d7` | Child 7 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d8` | Child 8 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d9` | Child 9 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d10` | Child 10 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d11` | Child 11 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d12` | Child 12 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d13` | Child 13 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d14` | Child 14 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d15` | Child 15 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d16` | Child 16 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d17` | Child 17 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d18` | Child 18 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d19` | Child 19 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch303d20` | Child 20 common natural child of R and current spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ch505_1` | Child 1 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_2` | Child 2 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_3` | Child 3 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_4` | Child 4 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_5` | Child 5 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_6` | Child 6 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_7` | Child 7 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_8` | Child 8 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_9` | Child 9 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_10` | Child 10 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_11` | Child 11 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_12` | Child 12 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_13` | Child 13 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_14` | Child 14 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_15` | Child 15 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_16` | Child 16 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_17` | Child 17 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_18` | Child 18 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_19` | Child 19 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch505_20` | Child 20 equal to which child | `Numeric(Byte)` | `%13.0g` |
| `ch508_` | Check children education changed | `Numeric(Byte)` | `%10.0g` |
| `ch509d1` | Child 1 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d2` | Child 2 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d3` | Child 3 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d4` | Child 4 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d5` | Child 5 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d6` | Child 6 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d7` | Child 7 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d8` | Child 8 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d9` | Child 9 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d10` | Child 10 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d11` | Child 11 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d12` | Child 12 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d13` | Child 13 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d14` | Child 14 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d15` | Child 15 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d16` | Child 16 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d17` | Child 17 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d18` | Child 18 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d19` | Child 19 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch509d20` | Child 20 education changed | `Numeric(Byte)` | `%12.0g` |
| `ch510_1` | Child 1 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_2` | Child 2 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_3` | Child 3 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_4` | Child 4 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_5` | Child 5 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_6` | Child 6 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_7` | Child 7 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_8` | Child 8 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_9` | Child 9 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_10` | Child 10 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_11` | Child 11 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_12` | Child 12 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_13` | Child 13 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_14` | Child 14 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_15` | Child 15 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_16` | Child 16 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_17` | Child 17 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_18` | Child 18 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_19` | Child 19 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch510_20` | Child 20 new educational degree | `Numeric(Byte)` | `%167.0g` |
| `ch511_` | Check children further education changed | `Numeric(Byte)` | `%10.0g` |
| `ch512d1` | Child 1 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d2` | Child 2 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d3` | Child 3 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d4` | Child 4 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d5` | Child 5 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d6` | Child 6 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d7` | Child 7 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d8` | Child 8 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d9` | Child 9 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d10` | Child 10 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d11` | Child 11 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d12` | Child 12 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d13` | Child 13 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d14` | Child 14 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d15` | Child 15 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d16` | Child 16 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d17` | Child 17 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d18` | Child 18 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d19` | Child 19 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch512d20` | Child 20 further education changed | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_1` | Child 1 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_2` | Child 2 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_3` | Child 3 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_4` | Child 4 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_5` | Child 5 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_6` | Child 6 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_7` | Child 7 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_8` | Child 8 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_9` | Child 9 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_10` | Child 10 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_11` | Child 11 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_12` | Child 12 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_13` | Child 13 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_14` | Child 14 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_15` | Child 15 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_16` | Child 16 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_17` | Child 17 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_18` | Child 18 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_19` | Child 19 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d1_20` | Child 20 no higher education/vocational training | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_1` | Child 1 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_2` | Child 2 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_3` | Child 3 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_4` | Child 4 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_5` | Child 5 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_6` | Child 6 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_7` | Child 7 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_8` | Child 8 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_9` | Child 9 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_10` | Child 10 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_11` | Child 11 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_12` | Child 12 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_13` | Child 13 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_14` | Child 14 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_15` | Child 15 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_16` | Child 16 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_17` | Child 17 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_18` | Child 18 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_19` | Child 19 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d2_20` | Child 20 degree obtained: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_1` | Child 1 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_2` | Child 2 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_3` | Child 3 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_4` | Child 4 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_5` | Child 5 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_6` | Child 6 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_7` | Child 7 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_8` | Child 8 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_9` | Child 9 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_10` | Child 10 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_11` | Child 11 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_12` | Child 12 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_13` | Child 13 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_14` | Child 14 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_15` | Child 15 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_16` | Child 16 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_17` | Child 17 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_18` | Child 18 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_19` | Child 19 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d3_20` | Child 20 degree obtained: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_1` | Child 1 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_2` | Child 2 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_3` | Child 3 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_4` | Child 4 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_5` | Child 5 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_6` | Child 6 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_7` | Child 7 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_8` | Child 8 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_9` | Child 9 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_10` | Child 10 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_11` | Child 11 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_12` | Child 12 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_13` | Child 13 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_14` | Child 14 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_15` | Child 15 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_16` | Child 16 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_17` | Child 17 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_18` | Child 18 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_19` | Child 19 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d4_20` | Child 20 degree obtained: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_1` | Child 1 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_2` | Child 2 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_3` | Child 3 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_4` | Child 4 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_5` | Child 5 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_6` | Child 6 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_7` | Child 7 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_8` | Child 8 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_9` | Child 9 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_10` | Child 10 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_11` | Child 11 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_12` | Child 12 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_13` | Child 13 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_14` | Child 14 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_15` | Child 15 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_16` | Child 16 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_17` | Child 17 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_18` | Child 18 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_19` | Child 19 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d5_20` | Child 20 degree obtained: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_1` | Child 1 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_2` | Child 2 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_3` | Child 3 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_4` | Child 4 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_5` | Child 5 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_6` | Child 6 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_7` | Child 7 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_8` | Child 8 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_9` | Child 9 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_10` | Child 10 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_11` | Child 11 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_12` | Child 12 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_13` | Child 13 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_14` | Child 14 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_15` | Child 15 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_16` | Child 16 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_17` | Child 17 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_18` | Child 18 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_19` | Child 19 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d6_20` | Child 20 degree obtained: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_1` | Child 1 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_2` | Child 2 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_3` | Child 3 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_4` | Child 4 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_5` | Child 5 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_6` | Child 6 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_7` | Child 7 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_8` | Child 8 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_9` | Child 9 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_10` | Child 10 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_11` | Child 11 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_12` | Child 12 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_13` | Child 13 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_14` | Child 14 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_15` | Child 15 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_16` | Child 16 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_17` | Child 17 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_18` | Child 18 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_19` | Child 19 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d7_20` | Child 20 degree obtained: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_1` | Child 1 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_2` | Child 2 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_3` | Child 3 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_4` | Child 4 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_5` | Child 5 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_6` | Child 6 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_7` | Child 7 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_8` | Child 8 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_9` | Child 9 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_10` | Child 10 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_11` | Child 11 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_12` | Child 12 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_13` | Child 13 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_14` | Child 14 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_15` | Child 15 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_16` | Child 16 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_17` | Child 17 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_18` | Child 18 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_19` | Child 19 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d8_20` | Child 20 degree obtained: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_1` | Child 1 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_2` | Child 2 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_3` | Child 3 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_4` | Child 4 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_5` | Child 5 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_6` | Child 6 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_7` | Child 7 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_8` | Child 8 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_9` | Child 9 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_10` | Child 10 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_11` | Child 11 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_12` | Child 12 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_13` | Child 13 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_14` | Child 14 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_15` | Child 15 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_16` | Child 16 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_17` | Child 17 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_18` | Child 18 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_19` | Child 19 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d9_20` | Child 20 degree obtained: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_1` | Child 1 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_2` | Child 2 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_3` | Child 3 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_4` | Child 4 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_5` | Child 5 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_6` | Child 6 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_7` | Child 7 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_8` | Child 8 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_9` | Child 9 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_10` | Child 10 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_11` | Child 11 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_12` | Child 12 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_13` | Child 13 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_14` | Child 14 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_15` | Child 15 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_16` | Child 16 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_17` | Child 17 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_18` | Child 18 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_19` | Child 19 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d10_20` | Child 20 degree obtained: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_1` | Child 1 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_2` | Child 2 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_3` | Child 3 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_4` | Child 4 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_5` | Child 5 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_6` | Child 6 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_7` | Child 7 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_8` | Child 8 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_9` | Child 9 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_10` | Child 10 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_11` | Child 11 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_12` | Child 12 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_13` | Child 13 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_14` | Child 14 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_15` | Child 15 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_16` | Child 16 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_17` | Child 17 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_18` | Child 18 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_19` | Child 19 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d11_20` | Child 20 degree obtained: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_1` | Child 1 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_2` | Child 2 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_3` | Child 3 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_4` | Child 4 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_5` | Child 5 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_6` | Child 6 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_7` | Child 7 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_8` | Child 8 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_9` | Child 9 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_10` | Child 10 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_11` | Child 11 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_12` | Child 12 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_13` | Child 13 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_14` | Child 14 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_15` | Child 15 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_16` | Child 16 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_17` | Child 17 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_18` | Child 18 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_19` | Child 19 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d12_20` | Child 20 degree obtained: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_1` | Child 1 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_2` | Child 2 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_3` | Child 3 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_4` | Child 4 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_5` | Child 5 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_6` | Child 6 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_7` | Child 7 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_8` | Child 8 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_9` | Child 9 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_10` | Child 10 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_11` | Child 11 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_12` | Child 12 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_13` | Child 13 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_14` | Child 14 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_15` | Child 15 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_16` | Child 16 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_17` | Child 17 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_18` | Child 18 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_19` | Child 19 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d13_20` | Child 20 degree obtained: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_1` | Child 1 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_2` | Child 2 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_3` | Child 3 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_4` | Child 4 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_5` | Child 5 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_6` | Child 6 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_7` | Child 7 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_8` | Child 8 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_9` | Child 9 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_10` | Child 10 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_11` | Child 11 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_12` | Child 12 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_13` | Child 13 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_14` | Child 14 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_15` | Child 15 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_16` | Child 16 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_17` | Child 17 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_18` | Child 18 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_19` | Child 19 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d14_20` | Child 20 degree obtained: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_1` | Child 1 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_2` | Child 2 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_3` | Child 3 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_4` | Child 4 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_5` | Child 5 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_6` | Child 6 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_7` | Child 7 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_8` | Child 8 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_9` | Child 9 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_10` | Child 10 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_11` | Child 11 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_12` | Child 12 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_13` | Child 13 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_14` | Child 14 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_15` | Child 15 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_16` | Child 16 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_17` | Child 17 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_18` | Child 18 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_19` | Child 19 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d15_20` | Child 20 degree obtained: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_1` | Child 1 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_2` | Child 2 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_3` | Child 3 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_4` | Child 4 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_5` | Child 5 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_6` | Child 6 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_7` | Child 7 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_8` | Child 8 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_9` | Child 9 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_10` | Child 10 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_11` | Child 11 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_12` | Child 12 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_13` | Child 13 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_14` | Child 14 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_15` | Child 15 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_16` | Child 16 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_17` | Child 17 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_18` | Child 18 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_19` | Child 19 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d16_20` | Child 20 degree obtained: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_1` | Child 1 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_2` | Child 2 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_3` | Child 3 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_4` | Child 4 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_5` | Child 5 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_6` | Child 6 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_7` | Child 7 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_8` | Child 8 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_9` | Child 9 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_10` | Child 10 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_11` | Child 11 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_12` | Child 12 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_13` | Child 13 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_14` | Child 14 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_15` | Child 15 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_16` | Child 16 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_17` | Child 17 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_18` | Child 18 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_19` | Child 19 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d17_20` | Child 20 degree obtained: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_1` | Child 1 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_2` | Child 2 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_3` | Child 3 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_4` | Child 4 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_5` | Child 5 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_6` | Child 6 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_7` | Child 7 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_8` | Child 8 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_9` | Child 9 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_10` | Child 10 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_11` | Child 11 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_12` | Child 12 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_13` | Child 13 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_14` | Child 14 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_15` | Child 15 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_16` | Child 16 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_17` | Child 17 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_18` | Child 18 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_19` | Child 19 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d18_20` | Child 20 degree obtained: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_1` | Child 1 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_2` | Child 2 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_3` | Child 3 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_4` | Child 4 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_5` | Child 5 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_6` | Child 6 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_7` | Child 7 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_8` | Child 8 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_9` | Child 9 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_10` | Child 10 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_11` | Child 11 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_12` | Child 12 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_13` | Child 13 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_14` | Child 14 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_15` | Child 15 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_16` | Child 16 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_17` | Child 17 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_18` | Child 18 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_19` | Child 19 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d19_20` | Child 20 degree obtained: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_1` | Child 1 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_2` | Child 2 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_3` | Child 3 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_4` | Child 4 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_5` | Child 5 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_6` | Child 6 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_7` | Child 7 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_8` | Child 8 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_9` | Child 9 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_10` | Child 10 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_11` | Child 11 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_12` | Child 12 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_13` | Child 13 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_14` | Child 14 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_15` | Child 15 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_16` | Child 16 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_17` | Child 17 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_18` | Child 18 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_19` | Child 19 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513d95_20` | Child 20 still in education | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_1` | Child 1 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_2` | Child 2 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_3` | Child 3 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_4` | Child 4 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_5` | Child 5 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_6` | Child 6 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_7` | Child 7 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_8` | Child 8 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_9` | Child 9 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_10` | Child 10 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_11` | Child 11 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_12` | Child 12 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_13` | Child 13 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_14` | Child 14 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_15` | Child 15 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_16` | Child 16 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_17` | Child 17 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_18` | Child 18 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_19` | Child 19 other | `Numeric(Byte)` | `%12.0g` |
| `ch513dot_20` | Child 20 other | `Numeric(Byte)` | `%12.0g` |
| `ch514_` | Check children marital status changed | `Numeric(Byte)` | `%10.0g` |
| `ch515d1` | Child 1 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d2` | Child 2 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d3` | Child 3 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d4` | Child 4 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d5` | Child 5 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d6` | Child 6 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d7` | Child 7 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d8` | Child 8 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d9` | Child 9 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d10` | Child 10 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d11` | Child 11 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d12` | Child 12 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d13` | Child 13 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d14` | Child 14 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d15` | Child 15 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d16` | Child 16 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d17` | Child 17 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d18` | Child 18 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d19` | Child 19 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch515d20` | Child 20 marital status changed | `Numeric(Byte)` | `%12.0g` |
| `ch516_1` | Child 1 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_2` | Child 2 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_3` | Child 3 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_4` | Child 4 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_5` | Child 5 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_6` | Child 6 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_7` | Child 7 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_8` | Child 8 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_9` | Child 9 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_10` | Child 10 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_11` | Child 11 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_12` | Child 12 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_13` | Child 13 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_14` | Child 14 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_15` | Child 15 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_16` | Child 16 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_17` | Child 17 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_18` | Child 18 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_19` | Child 19 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch516_20` | Child 20 new marital status | `Numeric(Byte)` | `%59.0g` |
| `ch517_` | Check children parenthood changed | `Numeric(Byte)` | `%10.0g` |
| `ch518d1` | Child 1 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d2` | Child 2 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d3` | Child 3 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d4` | Child 4 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d5` | Child 5 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d6` | Child 6 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d7` | Child 7 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d8` | Child 8 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d9` | Child 9 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d10` | Child 10 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d11` | Child 11 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d12` | Child 12 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d13` | Child 13 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d14` | Child 14 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d15` | Child 15 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d16` | Child 16 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d17` | Child 17 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d18` | Child 18 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d19` | Child 19 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch518d20` | Child 20 parenthood changed | `Numeric(Byte)` | `%12.0g` |
| `ch519_1` | Child 1 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_2` | Child 2 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_3` | Child 3 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_4` | Child 4 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_5` | Child 5 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_6` | Child 6 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_7` | Child 7 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_8` | Child 8 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_9` | Child 9 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_10` | Child 10 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_11` | Child 11 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_12` | Child 12 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_13` | Child 13 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_14` | Child 14 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_15` | Child 15 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_16` | Child 16 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_17` | Child 17 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_18` | Child 18 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_19` | Child 19 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch519_20` | Child 20 new number of children | `Numeric(Byte)` | `%10.0g` |
| `ch520_1` | Child 1 new youngest born | `Numeric(Int)` | `%10.0g` |
| `ch520_2` | Child 2 new youngest born | `Numeric(Int)` | `%10.0g` |
| `ch520_3` | Child 3 new youngest born | `Numeric(Int)` | `%10.0g` |
| `ch520_4` | Child 4 new youngest born | `Numeric(Int)` | `%10.0g` |
| `ch520_5` | Child 5 new youngest born | `Numeric(Int)` | `%10.0g` |
| `ch520_6` | Child 6 new youngest born | `Numeric(Int)` | `%10.0g` |
| `ch520_7` | Child 7 new youngest born | `Numeric(Int)` | `%10.0g` |
| `ch520_8` | Child 8 new youngest born | `Numeric(Int)` | `%10.0g` |
| `ch520_9` | Child 9 new youngest born | `Numeric(Int)` | `%10.0g` |
| `ch520_10` | Child 10 new youngest born | `Numeric(Int)` | `%10.0g` |
| `ch520_11` | Child 11 new youngest born | `Numeric(Int)` | `%10.0g` |
| `ch520_12` | Child 12 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_13` | Child 13 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_14` | Child 14 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_15` | Child 15 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_16` | Child 16 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_17` | Child 17 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_18` | Child 18 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_19` | Child 19 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_20` | Child 20 new youngest born | `Numeric(Int)` | `%10.0g` |
| `ch524_` | Check location of children changed | `Numeric(Byte)` | `%10.0g` |
| `ch525d1` | Child 1 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d2` | Child 2 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d3` | Child 3 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d4` | Child 4 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d5` | Child 5 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d6` | Child 6 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d7` | Child 7 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d8` | Child 8 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d9` | Child 9 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d10` | Child 10 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d11` | Child 11 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d12` | Child 12 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d13` | Child 13 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d14` | Child 14 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d15` | Child 15 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d16` | Child 16 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d17` | Child 17 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d18` | Child 18 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d19` | Child 19 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch525d20` | Child 20 location changed | `Numeric(Byte)` | `%12.0g` |
| `ch526_1` | Child 1 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_2` | Child 2 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_3` | Child 3 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_4` | Child 4 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_5` | Child 5 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_6` | Child 6 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_7` | Child 7 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_8` | Child 8 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_9` | Child 9 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_10` | Child 10 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_11` | Child 11 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_12` | Child 12 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_13` | Child 13 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_14` | Child 14 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_15` | Child 15 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_16` | Child 16 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_17` | Child 17 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_18` | Child 18 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_19` | Child 19 where does child live | `Numeric(Byte)` | `%42.0g` |
| `ch526_20` | Child 20 where does child live | `Numeric(Byte)` | `%42.0g` |
| `child_sn_loop_1` | Child 1 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_2` | Child 2 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_3` | Child 3 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_4` | Child 4 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_5` | Child 5 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_6` | Child 6 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_7` | Child 7 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_8` | Child 8 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_9` | Child 9 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_10` | Child 10 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_11` | Child 11 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_12` | Child 12 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_13` | Child 13 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_14` | Child 14 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_15` | Child 15 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_16` | Child 16 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_17` | Child 17 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_18` | Child 18 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_19` | Child 19 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_20` | Child 20 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_dead_1` | Indicator: Child 1 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_2` | Indicator: Child 2 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_3` | Indicator: Child 3 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_4` | Indicator: Child 4 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_5` | Indicator: Child 5 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_6` | Indicator: Child 6 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_7` | Indicator: Child 7 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_8` | Indicator: Child 8 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_9` | Indicator: Child 9 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_10` | Indicator: Child 10 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_11` | Indicator: Child 11 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_12` | Indicator: Child 12 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_13` | Indicator: Child 13 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_14` | Indicator: Child 14 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_15` | Indicator: Child 15 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_16` | Indicator: Child 16 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_17` | Indicator: Child 17 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_18` | Indicator: Child 18 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_19` | Indicator: Child 19 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_20` | Indicator: Child 20 dead | `Numeric(Byte)` | `%11.0g` |

### `co` - Consumption

- Dataset: `sharew8_rel9-0-0_co.dta`
- Read with: `ps.read_share_module("co", wave=8)`
- Rows: 53,695
- Variables: 27
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `co002e` | Amount spent on food at home | `Numeric(Float)` | `%10.0g` |
| `co002ub` | Amount spent on food at home ub | `Numeric(Byte)` | `%32.0g` |
| `co002v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `co002v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `co002v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `co003e` | Amount spent on food outside the home | `Numeric(Float)` | `%10.0g` |
| `co003ub` | Amount spent on food outside the home ub | `Numeric(Byte)` | `%32.0g` |
| `co003v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `co003v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `co003v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `co007_` | Is household able to make ends meet | `Numeric(Byte)` | `%31.0g` |
| `co009_` | Who answered the questions in co | `Numeric(Byte)` | `%47.0g` |
| `co010_` | Consume home produced food | `Numeric(Byte)` | `%10.0g` |
| `co011e` | Value of home produced food | `Numeric(Float)` | `%10.0g` |
| `co011ub` | Value of home produced food ub | `Numeric(Byte)` | `%32.0g` |
| `co011v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `co011v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `co011v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `co206_` | Afford to pay an unexpected expense without borrowing money | `Numeric(Byte)` | `%10.0g` |
| `co209_` | To help keeping living costs down: put up with feeling cold | `Numeric(Byte)` | `%10.0g` |

### `cv_r` - Coverscreen on individual level

- Dataset: `sharew8_rel9-0-0_cv_r.dta`
- Read with: `ps.read_share_module("cv_r", wave=8)`
- Rows: 106,436
- Variables: 64
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `waveid` | Identifier of original wave (person) | `Numeric(Int)` | `%9.0g` |
| `waveid_hh` | Identifier of original wave (household) | `Numeric(Int)` | `%9.0g` |
| `firstwave` | First appearance of person in SHARE | `Numeric(Byte)` | `%9.0g` |
| `firstwave_hh` | Wave household was sampled/first participated | `Numeric(Byte)` | `%9.0g` |
| `cvresp` | Coverscreen respondent | `Numeric(Byte)` | `%38.0g` |
| `deceased` | Deceased | `Numeric(Byte)` | `%10.0g` |
| `gender` | Male or female | `Numeric(Byte)` | `%10.0g` |
| `mobirth` | Month of birth | `Numeric(Byte)` | `%10.0g` |
| `yrbirth` | Year of birth | `Numeric(Int)` | `%10.0g` |
| `age2020` | Age in 2020 | `Numeric(Int)` | `%14.0g` |
| `age_int` | Age of respondent at the time of interview | `Numeric(Int)` | `%14.0g` |
| `mobirthp` | Month of birth spouse/partner | `Numeric(Byte)` | `%14.0g` |
| `yrbirthp` | Year of birth spouse/partner | `Numeric(Int)` | `%14.0g` |
| `agep2020` | Age of partner in 2020 | `Numeric(Int)` | `%14.0g` |
| `partnerinhh` | Partner in household | `Numeric(Byte)` | `%14.0g` |
| `relrpers` | Relation to coverscreen respondent | `Numeric(Int)` | `%47.0g` |
| `hhsize` | Household size | `Numeric(Byte)` | `%9.0g` |
| `fam_resp` | Family respondent | `Numeric(Byte)` | `%21.0g` |
| `fin_resp` | Financial respondent | `Numeric(Byte)` | `%24.0g` |
| `hou_resp` | Household respondent | `Numeric(Byte)` | `%24.0g` |
| `ILgroup` | Population group (Israel only) | `Numeric(Byte)` | `%38.0g` |
| `interview` | Interview done in wave 8 | `Numeric(Byte)` | `%21.0g` |
| `int_year` | Interview year | `Numeric(Int)` | `%14.0g` |
| `int_month` | Interview month | `Numeric(Byte)` | `%14.0g` |
| `interview_ca` | COVID-19 CATI interview (ca) done in wave 8 | `Numeric(Byte)` | `%10.0g` |
| `int_year_ca` | COVID-19 CATI interview (ca) interview year | `Numeric(Int)` | `%14.0g` |
| `int_month_ca` | COVID-19 CATI interview (ca) interview month | `Numeric(Byte)` | `%14.0g` |
| `deceased_update_ca` | Deceased - after CA update | `Numeric(Byte)` | `%10.0g` |
| `hhsize_update_ca` | Household size - after CA update | `Numeric(Byte)` | `%9.0g` |
| `partnerinhh_update_ca` | Partner in household - after CA update | `Numeric(Byte)` | `%14.0g` |
| `mergeidp8_update_ca` | Partner identifier (wave 8) - after CA update | `Str(12)` | `%12s` |
| `coupleid8_update_ca` | Couple identifier (wave 8) - after CA update | `Str(15)` | `%15s` |
| `relrpers_update_ca` | Relation to coverscreen respondent - after CA update | `Numeric(Int)` | `%47.0g` |
| `cvdate` | Coverscreen from field phase | `Numeric(Byte)` | `%23.0g` |
| `hhmoved` | Household moved | `Numeric(Byte)` | `%10.0g` |
| `nursinghome` | Nursing home | `Numeric(Byte)` | `%10.0g` |
| `rel_mergeid8_1` | Household member identifier (wave 8) | `Str(12)` | `%12s` |
| `rel_relationtype8_1` | Relation to household member (wave 8) | `Numeric(Int)` | `%47.0g` |
| `rel_mergeid8_2` | Household member identifier (wave 8) | `Str(12)` | `%12s` |
| `rel_relationtype8_2` | Relation to household member (wave 8) | `Numeric(Int)` | `%47.0g` |
| `rel_mergeid8_3` | Household member identifier (wave 8) | `Str(12)` | `%12s` |
| `rel_relationtype8_3` | Relation to household member (wave 8) | `Numeric(Int)` | `%47.0g` |
| `rel_mergeid8_4` | Household member identifier (wave 8) | `Str(12)` | `%12s` |
| `rel_relationtype8_4` | Relation to household member (wave 8) | `Numeric(Byte)` | `%47.0g` |
| `rel_mergeid8_5` | Household member identifier (wave 8) | `Str(12)` | `%12s` |
| `rel_relationtype8_5` | Relation to household member (wave 8) | `Numeric(Byte)` | `%47.0g` |
| `rel_mergeid8_6` | Household member identifier (wave 8) | `Str(12)` | `%12s` |
| `rel_relationtype8_6` | Relation to household member (wave 8) | `Numeric(Byte)` | `%47.0g` |
| `rel_mergeid8_7` | Household member identifier (wave 8) | `Str(12)` | `%12s` |
| `rel_relationtype8_7` | Relation to household member (wave 8) | `Numeric(Byte)` | `%47.0g` |
| `rel_mergeid8_8` | Household member identifier (wave 8) | `Str(12)` | `%12s` |
| `rel_relationtype8_8` | Relation to household member (wave 8) | `Numeric(Byte)` | `%47.0g` |
| `rel_mergeid8_9` | Household member identifier (wave 8) | `Str(12)` | `%12s` |
| `rel_relationtype8_9` | Relation to household member (wave 8) | `Numeric(Byte)` | `%47.0g` |
| `rel_mergeid8_10` | Household member identifier (wave 8) | `Str(12)` | `%12s` |
| `rel_relationtype8_10` | Relation to household member (wave 8) | `Numeric(Byte)` | `%47.0g` |
| `rel_mergeid8_11` | Household member identifier (wave 8) | `Str(12)` | `%12s` |
| `rel_relationtype8_11` | Relation to household member (wave 8) | `Numeric(Byte)` | `%47.0g` |

### `dn` - Demographics

- Dataset: `sharew8_rel9-0-0_dn.dta`
- Read with: `ps.read_share_module("dn", wave=8)`
- Rows: 53,695
- Variables: 144
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `dn002_` | Month of birth | `Numeric(Byte)` | `%12.0g` |
| `dn003_` | Year of birth | `Numeric(Int)` | `%10.0g` |
| `dn004_` | Born in the country of interview | `Numeric(Byte)` | `%10.0g` |
| `dn005c` | Foreign country of birth coding | `Numeric(Int)` | `%46.0g` |
| `dn006_` | Year came to live in country | `Numeric(Int)` | `%10.0g` |
| `dn007_` | Citizenship country of interview | `Numeric(Byte)` | `%10.0g` |
| `dn008c` | Other citizenship coding | `Numeric(Int)` | `%46.0g` |
| `dn009_` | Country-specific question | `Numeric(Byte)` | `%25.0g` |
| `dn010_` | Highest school degree obtained | `Numeric(Byte)` | `%167.0g` |
| `dn012d1` | Further education: country-specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `dn012d2` | Further education: country-specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `dn012d3` | Further education: country-specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `dn012d4` | Further education: country-specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `dn012d5` | Further education: country-specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `dn012d6` | Further education: country-specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `dn012d7` | Further education: country-specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `dn012d8` | Further education: country-specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `dn012d9` | Further education: country-specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `dn012d10` | Further education: country-specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `dn012d11` | Further education: country-specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `dn012d12` | Further education: country-specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `dn012d13` | Further education: country-specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `dn012d14` | Further education: country-specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `dn012d15` | Further education: country-specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `dn012d16` | Further education: country-specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `dn012d17` | Further education: country-specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `dn012d18` | Further education: country-specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `dn012d19` | Further education: country-specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `dn012d20` | Further education: country-specific category 20 | `Numeric(Byte)` | `%12.0g` |
| `dn012d95` | Further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `dn012dot` | Further education: other | `Numeric(Byte)` | `%12.0g` |
| `dn014_` | Marital status | `Numeric(Byte)` | `%59.0g` |
| `dn015_` | Year of marriage, if living together | `Numeric(Int)` | `%10.0g` |
| `dn016_` | Year of registered partnership | `Numeric(Int)` | `%10.0g` |
| `dn017_` | Year of marriage, if living separated | `Numeric(Int)` | `%10.0g` |
| `dn018_` | Since when divorced | `Numeric(Int)` | `%10.0g` |
| `dn019_` | Since when widowed | `Numeric(Int)` | `%10.0g` |
| `dn020_` | Year of birth of former partner | `Numeric(Int)` | `%10.0g` |
| `dn021_` | Highest educational degree of former partner | `Numeric(Byte)` | `%167.0g` |
| `dn023d1` | Further education former partner: country-specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `dn023d2` | Further education former partner: country-specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `dn023d3` | Further education former partner: country-specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `dn023d4` | Further education former partner: country-specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `dn023d5` | Further education former partner: country-specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `dn023d6` | Further education former partner: country-specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `dn023d7` | Further education former partner: country-specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `dn023d8` | Further education former partner: country-specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `dn023d9` | Further education former partner: country-specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `dn023d10` | Further education former partner: country-specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `dn023d11` | Further education former partner: country-specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `dn023d12` | Further education former partner: country-specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `dn023d13` | Further education former partner: country-specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `dn023d14` | Further education former partner: country-specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `dn023d15` | Further education former partner: country-specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `dn023d16` | Further education former partner: country-specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `dn023d17` | Further education former partner: country-specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `dn023d18` | Further education former partner: country-specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `dn023d19` | Further education former partner: country-specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `dn023d20` | Further education partner: country-specific category 20 | `Numeric(Byte)` | `%12.0g` |
| `dn023d95` | Further education former partner: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `dn023dot` | Further education former partner: other | `Numeric(Byte)` | `%12.0g` |
| `dn026_1` | Is natural parent still alive: mother | `Numeric(Byte)` | `%10.0g` |
| `dn026_2` | Is natural parent still alive: father | `Numeric(Byte)` | `%10.0g` |
| `dn027_1` | Age of death of parent: mother | `Numeric(Int)` | `%10.0g` |
| `dn027_2` | Age of death of parent: father | `Numeric(Int)` | `%10.0g` |
| `dn028_1` | Age of natural parent: mother | `Numeric(Int)` | `%10.0g` |
| `dn028_2` | Age of natural parent: father | `Numeric(Byte)` | `%10.0g` |
| `dn029isco_1` | ISCO code-08 of mother when respondent was 10 | `Numeric(Int)` | `%13.0g` |
| `dn029isco_2` | ISCO code-08 of father when respondent was 10 | `Numeric(Int)` | `%13.0g` |
| `dn030_1` | Where does parent live: mother | `Numeric(Byte)` | `%48.0g` |
| `dn030_2` | Where does parent live: father | `Numeric(Byte)` | `%48.0g` |
| `dn032_1` | Personal contact with parent during past 12 months: mother | `Numeric(Byte)` | `%30.0g` |
| `dn032_2` | Personal contact with parent during past 12 months: father | `Numeric(Byte)` | `%30.0g` |
| `dn033_1` | Health of parent: mother | `Numeric(Byte)` | `%16.0g` |
| `dn033_2` | Health of parent: father | `Numeric(Byte)` | `%16.0g` |
| `dn034_` | Ever had any siblings | `Numeric(Byte)` | `%10.0g` |
| `dn036_` | How many brothers alive | `Numeric(Byte)` | `%10.0g` |
| `dn037_` | How many sisters alive | `Numeric(Byte)` | `%10.0g` |
| `dn038_` | Who answered the questions in dn | `Numeric(Byte)` | `%47.0g` |
| `dn040_` | Partner outside household | `Numeric(Byte)` | `%10.0g` |
| `dn041_` | Years education | `Numeric(Byte)` | `%35.0g` |
| `dn042_` | Male or female | `Numeric(Byte)` | `%12.0g` |
| `dn043_` | Confirm month/year birth | `Numeric(Byte)` | `%10.0g` |
| `dn044_` | Marital status changed | `Numeric(Byte)` | `%47.0g` |
| `dn051_1` | Highest school certificate/degree: mother | `Numeric(Byte)` | `%167.0g` |
| `dn051_2` | Highest school certificate/degree: father | `Numeric(Byte)` | `%167.0g` |
| `dn053d1_1` | Further education mother: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `dn053d1_2` | Further education father: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `dn053d2_1` | Further education mother: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `dn053d2_2` | Further education father: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `dn053d3_1` | Further education mother: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `dn053d3_2` | Further education father: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `dn053d4_1` | Further education mother: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `dn053d4_2` | Further education father: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `dn053d5_1` | Further education mother: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `dn053d5_2` | Further education father: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `dn053d6_1` | Further education mother: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `dn053d6_2` | Further education father: country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `dn053d7_1` | Further education mother: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `dn053d7_2` | Further education father: country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `dn053d8_1` | Further education mother: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `dn053d8_2` | Further education father: country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `dn053d9_1` | Further education mother: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `dn053d9_2` | Further education father: country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `dn053d10_1` | Further education mother: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `dn053d10_2` | Further education father: country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `dn053d11_1` | Further education mother: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `dn053d11_2` | Further education father: country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `dn053d12_1` | Further education mother: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `dn053d12_2` | Further education father: country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `dn053d13_1` | Further education mother: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `dn053d13_2` | Further education father: country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `dn053d14_1` | Further education mother: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `dn053d14_2` | Further education father: country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `dn053d15_1` | Further education mother: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `dn053d15_2` | Further education father: country specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `dn053d16_1` | Further education mother: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `dn053d16_2` | Further education father: country specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `dn053d17_1` | Further education mother: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `dn053d17_2` | Further education father: country specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `dn053d18_1` | Further education mother: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `dn053d18_2` | Further education father: country specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `dn053d19_1` | Further education mother: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `dn053d19_2` | Further education father: country specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `dn053d20_1` | Further education mother: country specific category 20 | `Numeric(Byte)` | `%12.0g` |
| `dn053d20_2` | Further education father: country specific category 20 | `Numeric(Byte)` | `%12.0g` |
| `dn053d95_1` | Still in education: mother | `Numeric(Byte)` | `%12.0g` |
| `dn053d95_2` | Still in education: father | `Numeric(Byte)` | `%12.0g` |
| `dn053dot_1` | Other degree of education: mother | `Numeric(Byte)` | `%12.0g` |
| `dn053dot_2` | Other degree of education: father | `Numeric(Byte)` | `%12.0g` |
| `dn127_1` | Year of death of parent: mother | `Numeric(Int)` | `%10.0g` |
| `dn127_2` | Year of death of parent: father | `Numeric(Int)` | `%10.0g` |
| `dn502_` | Year of becoming citizen of country of interview | `Numeric(Int)` | `%10.0g` |
| `dn503_` | Born a citizen of country of interview | `Numeric(Byte)` | `%10.0g` |
| `dn504c` | Country of birth coded: mother | `Numeric(Int)` | `%46.0g` |
| `dn505c` | Country of birth coded: father | `Numeric(Int)` | `%46.0g` |
| `dn629_1` | Employment situation when you were 10: mother | `Numeric(Byte)` | `%65.0g` |
| `dn629_2` | Employment situation when you were 10: father | `Numeric(Byte)` | `%65.0g` |

### `ep` - Employment and Pensions

- Dataset: `sharew8_rel9-0-0_ep.dta`
- Read with: `ps.read_share_module("ep", wave=8)`
- Rows: 53,695
- Variables: 403
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `ep002_` | Did nevertheless any paid work last four weeks | `Numeric(Byte)` | `%10.0g` |
| `ep005_` | Current job situation | `Numeric(Byte)` | `%65.0g` |
| `ep006_` | Ever done paid work | `Numeric(Byte)` | `%10.0g` |
| `ep007_` | Currently more than one job | `Numeric(Byte)` | `%10.0g` |
| `ep009_` | Employee or self-employed | `Numeric(Byte)` | `%63.0g` |
| `ep010_` | Start of current job (year) | `Numeric(Int)` | `%10.0g` |
| `ep013_` | Total hours usually working per week | `Numeric(Int)` | `%10.0g` |
| `ep018_` | Kind of industry working in | `Numeric(Byte)` | `%121.0g` |
| `ep024_` | Number of employees | `Numeric(Byte)` | `%16.0g` |
| `ep026_` | Satisfied with (main) job | `Numeric(Byte)` | `%29.0g` |
| `ep027_` | (Main) job physically demanding | `Numeric(Byte)` | `%29.0g` |
| `ep028_` | Time pressure due to a heavy workload in (main) job | `Numeric(Byte)` | `%29.0g` |
| `ep029_` | Little freedom to decide how I do my work in (main) job | `Numeric(Byte)` | `%29.0g` |
| `ep030_` | Opportunity to develop new skills in (main) job | `Numeric(Byte)` | `%29.0g` |
| `ep031_` | Receive support in difficult situations in (main) job | `Numeric(Byte)` | `%29.0g` |
| `ep032_` | Receive recognition for work in (main) job | `Numeric(Byte)` | `%29.0g` |
| `ep033_` | Salary or earnings are adequate in (main) job | `Numeric(Byte)` | `%29.0g` |
| `ep034_` | Poor prospects for (main) job advancement | `Numeric(Byte)` | `%29.0g` |
| `ep035_` | Poor (main) job security | `Numeric(Byte)` | `%29.0g` |
| `ep036_` | Look for early retirement in (main) job | `Numeric(Byte)` | `%10.0g` |
| `ep037_` | Afraid health limits ability to work before regular retirement in (main) job | `Numeric(Byte)` | `%10.0g` |
| `ep050_` | Year last job ended | `Numeric(Int)` | `%10.0g` |
| `ep051_` | Employee or a self employed in last job | `Numeric(Byte)` | `%64.0g` |
| `ep054_` | Kind of industry working in last job | `Numeric(Byte)` | `%121.0g` |
| `ep061_` | Number of employees, last job | `Numeric(Byte)` | `%16.0g` |
| `ep064d1` | Reason retirement: country-specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ep064d2` | Reason retirement: country-specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ep064d3` | Reason retirement: country-specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ep064d4` | Reason retirement: country-specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ep064d5` | Reason retirement: country-specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ep064d6` | Reason retirement: country-specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ep064d7` | Reason retirement: country-specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ep064d8` | Reason retirement: country-specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ep064d9` | Reason retirement: country-specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ep064d10` | Reason retirement: country-specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ep067_` | How became unemployed | `Numeric(Byte)` | `%58.0g` |
| `ep069d1` | Reason stopped working: health problems | `Numeric(Byte)` | `%12.0g` |
| `ep069d2` | Reason stopped working: too tiring | `Numeric(Byte)` | `%12.0g` |
| `ep069d3` | Reason stopped working: too expensive to hire someone to look after home/family | `Numeric(Byte)` | `%12.0g` |
| `ep069d4` | Reason stopped working: wanted to take care of (grand)children | `Numeric(Byte)` | `%12.0g` |
| `ep069d5` | Reason stopped working: laid off, or workplace/office closed | `Numeric(Byte)` | `%12.0g` |
| `ep069d6` | Reason stopped working: family income sufficient | `Numeric(Byte)` | `%12.0g` |
| `ep069d7` | Reason stopped working: to care for old/sick family member | `Numeric(Byte)` | `%12.0g` |
| `ep069dot` | Reason stopped working: other | `Numeric(Byte)` | `%12.0g` |
| `ep074_1` | Period of income source c1 (ep671d1) | `Numeric(Byte)` | `%32.0g` |
| `ep074_2` | Period of income source c2 (ep671d2) | `Numeric(Byte)` | `%32.0g` |
| `ep074_3` | Period of income source c3 (ep671d3) | `Numeric(Byte)` | `%32.0g` |
| `ep074_4` | Period of income source c4 (ep671d4) | `Numeric(Byte)` | `%32.0g` |
| `ep074_5` | Period of income source c5 (ep671d5) | `Numeric(Byte)` | `%32.0g` |
| `ep074_6` | Period of income source c6 (ep671d6) | `Numeric(Byte)` | `%32.0g` |
| `ep074_7` | Period of income source c7 (ep671d7) | `Numeric(Byte)` | `%32.0g` |
| `ep074_8` | Period of income source c8 (ep671d8) | `Numeric(Byte)` | `%32.0g` |
| `ep074_9` | Period of income source c9 (ep671d9) | `Numeric(Byte)` | `%32.0g` |
| `ep074_10` | Period of income source c10 (ep671d10) | `Numeric(Byte)` | `%32.0g` |
| `ep074_11` | Period of income source c11 (ep671d11) | `Numeric(Byte)` | `%32.0g` |
| `ep074_12` | Period of income source c12 (ep671d12) | `Numeric(Byte)` | `%32.0g` |
| `ep074_13` | Period of income source c13 (ep671d13) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_1` | Typical payment of pension in c1 last year (ep671d1) | `Numeric(Float)` | `%10.0g` |
| `ep078e_2` | Typical payment of pension in c2 last year (ep671d2) | `Numeric(Float)` | `%10.0g` |
| `ep078e_3` | Typical payment of pension in c3 last year (ep671d3) | `Numeric(Float)` | `%10.0g` |
| `ep078e_4` | Typical payment of pension in c4 last year (ep671d4) | `Numeric(Float)` | `%10.0g` |
| `ep078e_5` | Typical payment of pension in c5 last year (ep671d5) | `Numeric(Float)` | `%10.0g` |
| `ep078e_6` | Typical payment of pension in c6 last year (ep671d6) | `Numeric(Float)` | `%10.0g` |
| `ep078e_7` | Typical payment of pension in c7 last year (ep671d7) | `Numeric(Float)` | `%10.0g` |
| `ep078e_8` | Typical payment of pension in c8 last year (ep671d8) | `Numeric(Float)` | `%10.0g` |
| `ep078e_9` | Typical payment of pension in c9 last year (ep671d9) | `Numeric(Float)` | `%10.0g` |
| `ep078e_10` | Typical payment of pension in c10 last year (ep671d10) | `Numeric(Float)` | `%10.0g` |
| `ep078e_11` | Typical payment of pension in c11 last year (ep671d11) | `Numeric(Float)` | `%10.0g` |
| `ep078e_12` | Typical payment of pension in c12 last year (ep671d12) | `Numeric(Float)` | `%10.0g` |
| `ep078e_13` | Typical payment of pension in c13 last year (ep671d13) | `Numeric(Float)` | `%10.0g` |
| `ep078ub_1` | Typical payment of pension in c1 last year ub (ep671d1) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_2` | Typical payment of pension in c2 last year ub (ep671d2) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_3` | Typical payment of pension in c3 last year ub (ep671d3) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_4` | Typical payment of pension in c4 last year ub (ep671d4) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_5` | Typical payment of pension in c5 last year ub (ep671d5) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_6` | Typical payment of pension in c6 last year ub (ep671d6) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_7` | Typical payment of pension in c7 last year ub (ep671d7) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_8` | Typical payment of pension in c8 last year ub (ep671d8) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_9` | Typical payment of pension in c9 last year ub (ep671d9) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_10` | Typical payment of pension in c10 last year ub (ep671d10) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_11` | Typical payment of pension in c11 last year ub (ep671d11) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_12` | Typical payment of pension in c12 last year ub (ep671d12) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_13` | Typical payment of pension in c13 last year ub (ep671d13) | `Numeric(Byte)` | `%32.0g` |
| `ep078v1` | Bracket value 1 | `Numeric(Float)` | `%9.0g` |
| `ep078v2` | Bracket value 2 | `Numeric(Float)` | `%9.0g` |
| `ep078v3` | Bracket value 3 | `Numeric(Float)` | `%9.0g` |
| `ep081_1` | Lump sum payment income source c1 (ep671d1) | `Numeric(Byte)` | `%10.0g` |
| `ep081_2` | Lump sum payment income source c2 (ep671d2) | `Numeric(Byte)` | `%10.0g` |
| `ep081_3` | Lump sum payment income source c3 (ep671d3) | `Numeric(Byte)` | `%10.0g` |
| `ep081_4` | Lump sum payment income source c4 (ep671d4) | `Numeric(Byte)` | `%10.0g` |
| `ep081_5` | Lump sum payment income source c5 (ep671d5) | `Numeric(Byte)` | `%10.0g` |
| `ep081_6` | Lump sum payment income source c6 (ep671d6) | `Numeric(Byte)` | `%10.0g` |
| `ep081_7` | Lump sum payment income source c7 (ep671d7) | `Numeric(Byte)` | `%10.0g` |
| `ep081_8` | Lump sum payment income source c8 (ep671d8) | `Numeric(Byte)` | `%10.0g` |
| `ep081_9` | Lump sum payment income source c9 (ep671d9) | `Numeric(Byte)` | `%10.0g` |
| `ep081_10` | Lump sum payment income source c10 (ep671d10) | `Numeric(Byte)` | `%10.0g` |
| `ep081_11` | Lump sum payment income source c11 (ep671d11) | `Numeric(Byte)` | `%10.0g` |
| `ep081_12` | Lump sum payment income source c12 (ep671d12) | `Numeric(Byte)` | `%10.0g` |
| `ep081_13` | Lump sum payment income source c13 (ep671d13) | `Numeric(Byte)` | `%10.0g` |
| `ep082e_1` | Total amount of lump sum payment income source c1 last year (ep671d1) | `Numeric(Float)` | `%10.0g` |
| `ep082e_2` | Total amount of lump sum payment income source c2 last year (ep671d2) | `Numeric(Float)` | `%10.0g` |
| `ep082e_3` | Total amount of lump sum payment income source c3 last year (ep671d3) | `Numeric(Float)` | `%10.0g` |
| `ep082e_4` | Total amount of lump sum payment income source c4 last year (ep671d4) | `Numeric(Float)` | `%10.0g` |
| `ep082e_5` | Total amount of lump sum payment income source c5 last year (ep671d5) | `Numeric(Float)` | `%10.0g` |
| `ep082e_6` | Total amount of lump sum payment income source c6 last year (ep671d6) | `Numeric(Float)` | `%10.0g` |
| `ep082e_7` | Total amount of lump sum payment income source c7 last year (ep671d7) | `Numeric(Float)` | `%10.0g` |
| `ep082e_8` | Total amount of lump sum payment income source c8 last year (ep671d8) | `Numeric(Float)` | `%10.0g` |
| `ep082e_9` | Total amount of lump sum payment income source c9 last year (ep671d9) | `Numeric(Float)` | `%10.0g` |
| `ep082e_10` | Total amount of lump sum payment income source c10 last year (ep671d10) | `Numeric(Float)` | `%10.0g` |
| `ep082e_11` | Total amount of lump sum payment income source c11 last year (ep671d11) | `Numeric(Float)` | `%10.0g` |
| `ep082e_12` | Total amount of lump sum payment income source c12 last year (ep671d12) | `Numeric(Float)` | `%10.0g` |
| `ep082e_13` | Total amount of lump sum payment income source c13 last year (ep671d13) | `Numeric(Float)` | `%10.0g` |
| `ep082ub_1` | Total amount of lump sum payment income source c1 ub last year (ep671d1) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_2` | Total amount of lump sum payment income source c2 ub last year (ep671d2) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_3` | Total amount of lump sum payment income source c3 ub last year (ep671d3) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_4` | Total amount of lump sum payment income source c4 ub last year (ep671d4) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_5` | Total amount of lump sum payment income source c5 ub last year (ep671d5) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_6` | Total amount of lump sum payment income source c6 ub last year (ep671d6) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_7` | Total amount of lump sum payment income source c7 ub last year (ep671d7) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_8` | Total amount of lump sum payment income source c8 ub last year (ep671d8) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_9` | Total amount of lump sum payment income source c9 ub last year (ep671d9) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_10` | Total amount of lump sum payment income source c10 ub last year (ep671d10) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_11` | Total amount of lump sum payment income source c11 ub last year (ep671d11) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_12` | Total amount of lump sum payment income source c12 ub last year (ep671d12) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_13` | Total amount of lump sum payment income source c13 ub last year (ep671d13) | `Numeric(Byte)` | `%32.0g` |
| `ep082v1` | Bracket value 1 | `Numeric(Float)` | `%9.0g` |
| `ep082v2` | Bracket value 2 | `Numeric(Float)` | `%9.0g` |
| `ep082v3` | Bracket value 3 | `Numeric(Float)` | `%9.0g` |
| `ep089d1` | Regular payments received: life insurance | `Numeric(Byte)` | `%12.0g` |
| `ep089d2` | Regular payments received: private annuity/private personal pension | `Numeric(Byte)` | `%12.0g` |
| `ep089d3` | Regular payments received: alimony | `Numeric(Byte)` | `%12.0g` |
| `ep089d4` | Regular payments received: from charities | `Numeric(Byte)` | `%12.0g` |
| `ep089d5` | Regular payments received: long-term care private insurance | `Numeric(Byte)` | `%12.0g` |
| `ep089dno` | Regular payments received: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep090_1` | Period received payment c1 | `Numeric(Byte)` | `%32.0g` |
| `ep090_2` | Period received payment c2 | `Numeric(Byte)` | `%32.0g` |
| `ep090_3` | Period received payment c3 | `Numeric(Byte)` | `%32.0g` |
| `ep090_4` | Period received payment c4 | `Numeric(Byte)` | `%32.0g` |
| `ep090_5` | Period received payment c5 | `Numeric(Byte)` | `%32.0g` |
| `ep092_1` | Additional payments for this benefit in last year, payment c1 | `Numeric(Byte)` | `%10.0g` |
| `ep092_2` | Additional payments for this benefit in last year, payment c2 | `Numeric(Byte)` | `%10.0g` |
| `ep092_3` | Additional payments for this benefit in last year, payment c3 | `Numeric(Byte)` | `%10.0g` |
| `ep092_4` | Additional payments for this benefit in last year, payment c4 | `Numeric(Byte)` | `%10.0g` |
| `ep092_5` | Additional payments for this benefit in last year, payment c5 | `Numeric(Byte)` | `%10.0g` |
| `ep094e_1` | Total amount payment c1 last year | `Numeric(Float)` | `%10.0g` |
| `ep094e_2` | Total amount payment c2 last year | `Numeric(Float)` | `%10.0g` |
| `ep094e_3` | Total amount payment c3 last year | `Numeric(Float)` | `%10.0g` |
| `ep094e_4` | Total amount payment c4 last year | `Numeric(Float)` | `%10.0g` |
| `ep094e_5` | Total amount payment c5 last year | `Numeric(Float)` | `%10.0g` |
| `ep094ub_1` | Total amount payment c1 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094ub_2` | Total amount payment c2 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094ub_3` | Total amount payment c3 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094ub_4` | Total amount payment c4 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094ub_5` | Total amount payment c5 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094v1` | Bracket value 1 | `Numeric(Float)` | `%9.0g` |
| `ep094v2` | Bracket value 2 | `Numeric(Float)` | `%9.0g` |
| `ep094v3` | Bracket value 3 | `Numeric(Float)` | `%9.0g` |
| `ep096_1` | Months received payment c1 | `Numeric(Byte)` | `%10.0g` |
| `ep096_2` | Months received payment c2 | `Numeric(Byte)` | `%10.0g` |
| `ep096_3` | Months received payment c3 | `Numeric(Byte)` | `%10.0g` |
| `ep096_4` | Months received payment c4 | `Numeric(Byte)` | `%10.0g` |
| `ep096_5` | Months received payment c5 | `Numeric(Byte)` | `%10.0g` |
| `ep097_` | Pension claims | `Numeric(Byte)` | `%10.0g` |
| `ep098d1` | Type of pension entitled to: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ep098d2` | Type of pension entitled to: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ep098d3` | Type of pension entitled to: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ep098d4` | Type of pension entitled to: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ep098d5` | Type of pension entitled to: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ep102_1` | Compulsory or voluntary participation in pension c1 | `Numeric(Byte)` | `%16.0g` |
| `ep102_2` | Compulsory or voluntary participation in pension c2 | `Numeric(Byte)` | `%16.0g` |
| `ep102_3` | Compulsory or voluntary participation in pension c3 | `Numeric(Byte)` | `%16.0g` |
| `ep102_4` | Compulsory or voluntary participation in pension c4 | `Numeric(Byte)` | `%16.0g` |
| `ep102_5` | Compulsory or voluntary participation in pension c5 | `Numeric(Byte)` | `%16.0g` |
| `ep103_1` | Years contributing to plan, pension c1 | `Numeric(Byte)` | `%10.0g` |
| `ep103_2` | Years contributing to plan, pension c2 | `Numeric(Byte)` | `%10.0g` |
| `ep103_3` | Years contributing to plan, pension c3 | `Numeric(Byte)` | `%10.0g` |
| `ep103_4` | Years contributing to plan, pension c4 | `Numeric(Byte)` | `%10.0g` |
| `ep103_5` | Years contributing to plan, pension c5 | `Numeric(Byte)` | `%10.0g` |
| `ep106_1` | Expected age to collect pension c1 | `Numeric(Byte)` | `%10.0g` |
| `ep106_2` | Expected age to collect pension c2 | `Numeric(Byte)` | `%10.0g` |
| `ep106_3` | Expected age to collect pension c3 | `Numeric(Byte)` | `%10.0g` |
| `ep106_4` | Expected age to collect pension c4 | `Numeric(Byte)` | `%10.0g` |
| `ep106_5` | Expected age to collect pension c5 | `Numeric(Byte)` | `%10.0g` |
| `ep125_` | Continuously working | `Numeric(Byte)` | `%10.0g` |
| `ep127_1` | Period from month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep127_2` | Period from month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep127_3` | Period from month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep127_4` | Period from month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep127_5` | Period from month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep127_6` | Period from month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep127_7` | Period from month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep127_8` | Period from month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep127_9` | Period from month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep127_10` | Period from month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep127_11` | Period from month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep127_12` | Period from month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep127_13` | Period from month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep127_14` | Period from month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep127_21` | Period from month (unemployed) | `Numeric(Byte)` | `%12.0g` |
| `ep127_22` | Period from month (unemployed) | `Numeric(Byte)` | `%12.0g` |
| `ep127_23` | Period from month (unemployed) | `Numeric(Byte)` | `%12.0g` |
| `ep127_24` | Period from month (unemployed) | `Numeric(Byte)` | `%12.0g` |
| `ep127_25` | Period from month (unemployed) | `Numeric(Byte)` | `%12.0g` |
| `ep127_26` | Period from month (unemployed) | `Numeric(Byte)` | `%12.0g` |
| `ep128_1` | Period from year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep128_2` | Period from year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep128_3` | Period from year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep128_4` | Period from year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep128_5` | Period from year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep128_6` | Period from year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep128_7` | Period from year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep128_8` | Period from year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep128_9` | Period from year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep128_10` | Period from year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep128_11` | Period from year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep128_12` | Period from year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep128_13` | Period from year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep128_14` | Period from year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep128_21` | Period from year (unemployed) | `Numeric(Byte)` | `%20.0g` |
| `ep128_22` | Period from year (unemployed) | `Numeric(Byte)` | `%20.0g` |
| `ep128_23` | Period from year (unemployed) | `Numeric(Byte)` | `%20.0g` |
| `ep128_24` | Period from year (unemployed) | `Numeric(Byte)` | `%20.0g` |
| `ep128_25` | Period from year (unemployed) | `Numeric(Byte)` | `%20.0g` |
| `ep128_26` | Period from year (unemployed) | `Numeric(Byte)` | `%20.0g` |
| `ep129_1` | Period to month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep129_2` | Period to month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep129_3` | Period to month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep129_4` | Period to month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep129_5` | Period to month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep129_6` | Period to month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep129_7` | Period to month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep129_8` | Period to month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep129_9` | Period to month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep129_10` | Period to month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep129_11` | Period to month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep129_12` | Period to month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep129_13` | Period to month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep129_14` | Period to month (working) | `Numeric(Byte)` | `%12.0g` |
| `ep129_21` | Period to month (unemployed) | `Numeric(Byte)` | `%12.0g` |
| `ep129_22` | Period to month (unemployed) | `Numeric(Byte)` | `%12.0g` |
| `ep129_23` | Period to month (unemployed) | `Numeric(Byte)` | `%12.0g` |
| `ep129_24` | Period to month (unemployed) | `Numeric(Byte)` | `%12.0g` |
| `ep129_25` | Period to month (unemployed) | `Numeric(Byte)` | `%12.0g` |
| `ep129_26` | Period to month (unemployed) | `Numeric(Byte)` | `%12.0g` |
| `ep130_1` | Period to year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep130_2` | Period to year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep130_3` | Period to year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep130_4` | Period to year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep130_5` | Period to year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep130_6` | Period to year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep130_7` | Period to year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep130_8` | Period to year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep130_9` | Period to year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep130_10` | Period to year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep130_11` | Period to year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep130_12` | Period to year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep130_13` | Period to year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep130_14` | Period to year (working) | `Numeric(Byte)` | `%20.0g` |
| `ep130_21` | Period to year (unemployed) | `Numeric(Byte)` | `%20.0g` |
| `ep130_22` | Period to year (unemployed) | `Numeric(Byte)` | `%20.0g` |
| `ep130_23` | Period to year (unemployed) | `Numeric(Byte)` | `%20.0g` |
| `ep130_24` | Period to year (unemployed) | `Numeric(Byte)` | `%20.0g` |
| `ep130_25` | Period to year (unemployed) | `Numeric(Byte)` | `%20.0g` |
| `ep130_26` | Period to year (unemployed) | `Numeric(Byte)` | `%20.0g` |
| `ep133_1` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_2` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_3` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_4` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_5` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_6` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_7` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_8` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_9` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_10` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_11` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_12` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_13` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_14` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_21` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_22` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_23` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_24` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_25` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_26` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep141d1` | Change in job: type of employment | `Numeric(Byte)` | `%12.0g` |
| `ep141d2` | Change in job: employer | `Numeric(Byte)` | `%12.0g` |
| `ep141d3` | Change in job: promotion | `Numeric(Byte)` | `%12.0g` |
| `ep141d4` | Change in job: job location | `Numeric(Byte)` | `%12.0g` |
| `ep141d5` | Change in job: contract length | `Numeric(Byte)` | `%12.0g` |
| `ep141dno` | Change in job: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep152isco` | ISCO-08 code: respondent's last job | `Numeric(Int)` | `%13.0g` |
| `ep204_` | Any earnings from employment previous year | `Numeric(Byte)` | `%10.0g` |
| `ep205e` | Earnings employment per year after taxes | `Numeric(Float)` | `%10.0g` |
| `ep205ub` | Earnings employment per year after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep205v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `ep205v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ep205v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ep206_` | Income from self-employment previous year | `Numeric(Byte)` | `%10.0g` |
| `ep207e` | Earnings self-employment per year after taxes | `Numeric(Float)` | `%10.0g` |
| `ep207ub` | Earnings self-employment per year after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep207v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `ep207v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ep207v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ep208_1` | How many months received income source c1 (ep671d1) | `Numeric(Byte)` | `%10.0g` |
| `ep208_2` | How many months received income source c2 (ep671d2) | `Numeric(Byte)` | `%10.0g` |
| `ep208_3` | How many months received income source c3 (ep671d3) | `Numeric(Byte)` | `%10.0g` |
| `ep208_4` | How many months received income source c4 (ep671d4) | `Numeric(Byte)` | `%10.0g` |
| `ep208_5` | How many months received income source c5 (ep671d5) | `Numeric(Byte)` | `%10.0g` |
| `ep208_6` | How many months received income source c6 (ep671d6) | `Numeric(Byte)` | `%10.0g` |
| `ep208_7` | How many months received income source c7 (ep671d7) | `Numeric(Byte)` | `%10.0g` |
| `ep208_8` | How many months received income source c8 (ep671d8) | `Numeric(Byte)` | `%10.0g` |
| `ep208_9` | How many months received income source c9 (ep671d9) | `Numeric(Byte)` | `%10.0g` |
| `ep208_10` | How many months received income source c10 (ep671d10) | `Numeric(Byte)` | `%10.0g` |
| `ep208_11` | How many months received income source c11 (ep671d11) | `Numeric(Byte)` | `%10.0g` |
| `ep208_12` | How many months received income source c12 (ep671d12) | `Numeric(Byte)` | `%10.0g` |
| `ep208_13` | How many months received income source c13 (ep671d13) | `Numeric(Byte)` | `%10.0g` |
| `ep209e_1` | Additional payments c1 after taxes | `Numeric(Float)` | `%10.0g` |
| `ep209e_2` | Additional payments c2 after taxes | `Numeric(Float)` | `%10.0g` |
| `ep209e_3` | Additional payments c3 after taxes | `Numeric(Float)` | `%10.0g` |
| `ep209e_4` | Additional payments c4 after taxes | `Numeric(Float)` | `%10.0g` |
| `ep209e_5` | Additional payments c5 after taxes | `Numeric(Float)` | `%10.0g` |
| `ep209ub_1` | Additional payments c1 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209ub_2` | Additional payments c2 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209ub_3` | Additional payments c3 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209ub_4` | Additional payments c4 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209ub_5` | Additional payments c5 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209v1` | Bracket value 1 | `Numeric(Float)` | `%9.0g` |
| `ep209v2` | Bracket value 2 | `Numeric(Float)` | `%9.0g` |
| `ep209v3` | Bracket value 3 | `Numeric(Float)` | `%9.0g` |
| `ep210_` | Who answered section ep | `Numeric(Byte)` | `%47.0g` |
| `ep213_1` | First year received income source c1 (ep671d1) | `Numeric(Int)` | `%10.0g` |
| `ep213_2` | First year received income source c2 (ep671d2) | `Numeric(Int)` | `%10.0g` |
| `ep213_3` | First year received income source c3 (ep671d3) | `Numeric(Int)` | `%10.0g` |
| `ep213_4` | First year received income source c4 (ep671d4) | `Numeric(Int)` | `%10.0g` |
| `ep213_5` | First year received income source c5 (ep671d5) | `Numeric(Int)` | `%10.0g` |
| `ep213_6` | First year received income source c6 (ep671d6) | `Numeric(Int)` | `%10.0g` |
| `ep213_7` | First year received income source c7 (ep671d7) | `Numeric(Int)` | `%10.0g` |
| `ep213_8` | First year received income source c8 (ep671d8) | `Numeric(Int)` | `%10.0g` |
| `ep213_9` | First year received income source c9 (ep671d9) | `Numeric(Int)` | `%10.0g` |
| `ep213_10` | First year received income source c10 (ep671d10) | `Numeric(Int)` | `%10.0g` |
| `ep213_11` | First year received income source c11 (ep671d11) | `Numeric(Int)` | `%10.0g` |
| `ep213_12` | First year received income source c12 (ep671d12) | `Numeric(Int)` | `%10.0g` |
| `ep213_13` | First year received income source c13 (ep671d13) | `Numeric(Int)` | `%10.0g` |
| `ep325_` | Unemployed since last interview | `Numeric(Byte)` | `%10.0g` |
| `ep328_` | Retirement month | `Numeric(Byte)` | `%12.0g` |
| `ep329_` | Retirement year | `Numeric(Int)` | `%10.0g` |
| `ep337_` | Currently looking for job | `Numeric(Byte)` | `%10.0g` |
| `ep609e_1` | Amount of first monthly benefit from pension 1 (ep098d1) | `Numeric(Float)` | `%10.0g` |
| `ep609e_2` | Amount of first monthly benefit from pension 2 (ep098d2) | `Numeric(Float)` | `%10.0g` |
| `ep609e_3` | Amount of first monthly benefit from pension 3 (ep098d3) | `Numeric(Float)` | `%10.0g` |
| `ep609e_4` | Amount of first monthly benefit from pension 4 (ep098d4) | `Numeric(Float)` | `%10.0g` |
| `ep609e_5` | Amount of first monthly benefit from pension 5 (ep098d5) | `Numeric(Float)` | `%10.0g` |
| `ep612_1` | First received income source c1 before last interview (ep671d1) | `Numeric(Byte)` | `%35.0g` |
| `ep612_2` | First received income source c2 before last interview (ep671d2) | `Numeric(Byte)` | `%35.0g` |
| `ep612_3` | First received income source c3 before last interview (ep671d3) | `Numeric(Byte)` | `%35.0g` |
| `ep612_4` | First received income source c4 before last interview (ep671d4) | `Numeric(Byte)` | `%35.0g` |
| `ep612_5` | First received income source c5 before last interview (ep671d5) | `Numeric(Byte)` | `%35.0g` |
| `ep612_6` | First received income source c6 before last interview (ep671d6) | `Numeric(Byte)` | `%35.0g` |
| `ep612_7` | First received income source c7 before last interview (ep671d7) | `Numeric(Byte)` | `%35.0g` |
| `ep612_8` | First received income source c8 before last interview (ep671d8) | `Numeric(Byte)` | `%35.0g` |
| `ep612_9` | First received income source c9 before last interview (ep671d9) | `Numeric(Byte)` | `%35.0g` |
| `ep612_10` | First received income source c10 before last interview (ep671d10) | `Numeric(Byte)` | `%35.0g` |
| `ep612_11` | First received income source c11 before last interview (ep671d11) | `Numeric(Byte)` | `%35.0g` |
| `ep612_12` | First received income source c12 before last interview (ep671d12) | `Numeric(Byte)` | `%35.0g` |
| `ep612_13` | First received income source c13 before last interview (ep671d13) | `Numeric(Byte)` | `%35.0g` |
| `ep613_` | Year started collecting first occupational pension | `Numeric(Int)` | `%10.0g` |
| `ep616isco` | ISCO code-08: respondent's current main job | `Numeric(Int)` | `%13.0g` |
| `ep621_` | Started collecting first occupational pension before last interview | `Numeric(Byte)` | `%35.0g` |
| `ep624_` | Income from any occupational pension last year | `Numeric(Byte)` | `%10.0g` |
| `ep649_` | Years worked in last job | `Numeric(Byte)` | `%10.0g` |
| `ep671d1` | Income sources: public old age pension | `Numeric(Byte)` | `%12.0g` |
| `ep671d2` | Income sources: public old age supplementary/second pension | `Numeric(Byte)` | `%12.0g` |
| `ep671d3` | Income sources: public early/pre-retirement pension | `Numeric(Byte)` | `%12.0g` |
| `ep671d4` | Income sources: main public sickness benefits | `Numeric(Byte)` | `%12.0g` |
| `ep671d5` | Income sources: main public disability insurance pension | `Numeric(Byte)` | `%12.0g` |
| `ep671d6` | Income sources: secondary public disability insurance pension | `Numeric(Byte)` | `%12.0g` |
| `ep671d7` | Income sources: secondary public sickness benefits | `Numeric(Byte)` | `%12.0g` |
| `ep671d8` | Income sources: public unemployment benefit/insurance | `Numeric(Byte)` | `%12.0g` |
| `ep671d9` | Income sources: main public survivor pension from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ep671d10` | Income sources: secondary public survivor pension from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `ep671d11` | Income sources: public war pension | `Numeric(Byte)` | `%12.0g` |
| `ep671d12` | Income sources: public long-term care insurance | `Numeric(Byte)` | `%12.0g` |
| `ep671d13` | Income sources: social assistance | `Numeric(Byte)` | `%12.0g` |
| `ep671dno` | Income sources: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep678e` | Amount received from all occupational pensions last year | `Numeric(Float)` | `%10.0g` |
| `ep678ub` | Amount received from all occupational pensions last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep678v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `ep678v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ep678v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ep681_` | Received additional/extra/lump-sum payment from occupational pension last year | `Numeric(Byte)` | `%10.0g` |
| `ep682e` | Amount received as additional/extra/lump-sum payment | `Numeric(Float)` | `%10.0g` |
| `ep682ub` | Amount received as additional/extra/lump-sum payment ub | `Numeric(Byte)` | `%32.0g` |
| `ep682v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ep682v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ep682v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ep811_` | Term of job | `Numeric(Byte)` | `%30.0g` |

### `ex` - Expectations

- Dataset: `sharew8_rel9-0-0_ex.dta`
- Read with: `ps.read_share_module("ex", wave=8)`
- Rows: 53,695
- Variables: 26
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ex001_` | Introduction and example | `Numeric(Byte)` | `%10.0g` |
| `ex007_` | Chance government reduces pension | `Numeric(Byte)` | `%10.0g` |
| `ex008_` | Chance government raises retirement age | `Numeric(Byte)` | `%10.0g` |
| `ex009_` | Life expectancy | `Numeric(Byte)` | `%10.0g` |
| `ex009age` | Life expectancy target age | `Numeric(Int)` | `%10.0g` |
| `ex023_` | End non proxy | `Numeric(Byte)` | `%62.0g` |
| `ex025_` | Chance to work after age of 63 | `Numeric(Byte)` | `%10.0g` |
| `ex026_` | Trust in other people | `Numeric(Byte)` | `%10.0g` |
| `ex029_` | Frequency of praying | `Numeric(Byte)` | `%34.0g` |
| `ex104_` | Partner ever done paid work | `Numeric(Byte)` | `%10.0g` |
| `ex105_` | Partner employee or a self-employed | `Numeric(Byte)` | `%64.0g` |
| `ex110_` | Risk aversion | `Numeric(Byte)` | `%121.0g` |
| `ex111_` | Planning horizon of saving and spending | `Numeric(Byte)` | `%27.0g` |
| `ex123_` | Consent to recontact | `Numeric(Byte)` | `%48.0g` |
| `ex602_` | Amount of years spouse/partner been in school | `Numeric(Int)` | `%10.0g` |
| `ex603_` | Partner current job situation | `Numeric(Byte)` | `%65.0g` |
| `ex613isco` | ISCO-08 code: Most recent job of spouse/partner | `Numeric(Int)` | `%13.0g` |
| `ex800_` | Partner participates afterwards | `Numeric(Byte)` | `%10.0g` |
| `ex801_` | Chances to run out of money in the future | `Numeric(Byte)` | `%10.0g` |
| `ex802_` | Financial situation today compared to expectations at age 45 | `Numeric(Byte)` | `%27.0g` |

### `ft` - Financial Transfers

- Dataset: `sharew8_rel9-0-0_ft.dta`
- Read with: `ps.read_share_module("ft", wave=8)`
- Rows: 53,695
- Variables: 69
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ft002_` | Given financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft003_1` | To whom given gift, person 1 | `Numeric(Byte)` | `%60.0g` |
| `ft003_2` | To whom given gift, person 2 | `Numeric(Byte)` | `%60.0g` |
| `ft003_3` | To whom given gift, person 3 | `Numeric(Byte)` | `%60.0g` |
| `ft007_1` | Other persons given financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft007_2` | Other persons given financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft007_3` | Other persons given financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft009_` | Received financial gift of 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft010_1` | From whom recieved gift, person 1 | `Numeric(Byte)` | `%60.0g` |
| `ft010_2` | From whom recieved gift, person 2 | `Numeric(Byte)` | `%60.0g` |
| `ft010_3` | From whom recieved gift, person 3 | `Numeric(Byte)` | `%60.0g` |
| `ft014_1` | From other persons received financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft014_2` | From other persons received financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft014_3` | From other persons received financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft015_` | Ever received gift or inheritance (worth 5000 euros or more) | `Numeric(Byte)` | `%10.0g` |
| `ft016_1` | Year, inheritance or large gift 1 received | `Numeric(Int)` | `%10.0g` |
| `ft016_2` | Year, inheritance or large gift 2 received | `Numeric(Int)` | `%10.0g` |
| `ft016_3` | Year, inheritance or large gift 3 received | `Numeric(Int)` | `%10.0g` |
| `ft016_4` | Year, inheritance or large gift 4 received | `Numeric(Int)` | `%10.0g` |
| `ft016_5` | Year, inheritance or large gift 5 received | `Numeric(Int)` | `%10.0g` |
| `ft017_1` | From whom inheritance or large gift 1 | `Numeric(Byte)` | `%60.0g` |
| `ft017_2` | From whom inheritance or large gift 2 | `Numeric(Byte)` | `%60.0g` |
| `ft017_3` | From whom inheritance or large gift 3 | `Numeric(Byte)` | `%60.0g` |
| `ft017_4` | From whom inheritance or large gift 4 | `Numeric(Byte)` | `%60.0g` |
| `ft017_5` | From whom inheritance or large gift 5 | `Numeric(Byte)` | `%60.0g` |
| `ft020_1` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft020_2` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft020_3` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft020_4` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft020_5` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft021_` | Who answered the questions in ft | `Numeric(Byte)` | `%47.0g` |
| `ft025_` | Ever given gift 5000 or more | `Numeric(Byte)` | `%10.0g` |
| `ft026_1` | In which year given gift | `Numeric(Int)` | `%10.0g` |
| `ft026_2` | In which year given gift | `Numeric(Int)` | `%10.0g` |
| `ft026_3` | In which year given gift | `Numeric(Int)` | `%10.0g` |
| `ft026_4` | In which year given gift | `Numeric(Int)` | `%10.0g` |
| `ft026_5` | In which year given gift | `Numeric(Int)` | `%10.0g` |
| `ft027_1` | To whom given 5000 or more | `Numeric(Byte)` | `%60.0g` |
| `ft027_2` | To whom given 5000 or more | `Numeric(Byte)` | `%60.0g` |
| `ft027_3` | To whom given 5000 or more | `Numeric(Byte)` | `%60.0g` |
| `ft027_4` | To whom given 5000 or more | `Numeric(Byte)` | `%60.0g` |
| `ft027_5` | To whom given 5000 or more | `Numeric(Byte)` | `%60.0g` |
| `ft031_1` | Any further gift | `Numeric(Byte)` | `%10.0g` |
| `ft031_2` | Any further gift | `Numeric(Byte)` | `%10.0g` |
| `ft031_3` | Any further gift | `Numeric(Byte)` | `%10.0g` |
| `ft031_4` | Any further gift | `Numeric(Byte)` | `%10.0g` |
| `ft031_5` | Any further gift | `Numeric(Byte)` | `%10.0g` |
| `ft032_1` | To which child given financial gift | `Numeric(Byte)` | `%21.0g` |
| `ft032_2` | To which child given financial gift | `Numeric(Byte)` | `%21.0g` |
| `ft032_3` | To which child given financial gift | `Numeric(Byte)` | `%21.0g` |
| `ft034_1` | From which child received financial gift | `Numeric(Byte)` | `%21.0g` |
| `ft034_2` | From which child received financial gift | `Numeric(Byte)` | `%21.0g` |
| `ft034_3` | From which child received financial gift | `Numeric(Byte)` | `%21.0g` |
| `ft036_1` | From which child inheritance or large gift | `Numeric(Byte)` | `%21.0g` |
| `ft036_2` | From which child inheritance or large gift | `Numeric(Byte)` | `%21.0g` |
| `ft036_3` | From which child inheritance or large gift | `Numeric(Byte)` | `%21.0g` |
| `ft036_4` | From which child inheritance or large gift | `Numeric(Byte)` | `%21.0g` |
| `ft036_5` | From which child inheritance or large gift | `Numeric(Byte)` | `%21.0g` |
| `ft038_1` | To which child given 5000 or more | `Numeric(Byte)` | `%21.0g` |
| `ft038_2` | To which child given 5000 or more | `Numeric(Byte)` | `%21.0g` |
| `ft038_3` | To which child given 5000 or more | `Numeric(Byte)` | `%21.0g` |
| `ft038_4` | To which child given 5000 or more | `Numeric(Byte)` | `%21.0g` |
| `ft038_5` | To which child given 5000 or more | `Numeric(Byte)` | `%21.0g` |

### `gs` - Grip Strength

- Dataset: `sharew8_rel9-0-0_gs.dta`
- Read with: `ps.read_share_module("gs", wave=8)`
- Rows: 53,695
- Variables: 23
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `gs002_` | Record respondent status | `Numeric(Byte)` | `%54.0g` |
| `gs004_` | Dominant hand | `Numeric(Byte)` | `%16.0g` |
| `gs006_` | 1st measurement: left hand | `Numeric(Byte)` | `%10.0g` |
| `gs007_` | 2nd measurement: left hand | `Numeric(Byte)` | `%10.0g` |
| `gs008_` | 1st measurement: right hand | `Numeric(Byte)` | `%10.0g` |
| `gs009_` | 2nd measurement: right hand | `Numeric(Byte)` | `%10.0g` |
| `gs010d1` | Why not completed gs test: r felt it would not be safe | `Numeric(Byte)` | `%12.0g` |
| `gs010d2` | Why not completed gs test: iwer felt it would not be safe | `Numeric(Byte)` | `%12.0g` |
| `gs010d3` | Why not completed gs test: r refused, no reason given | `Numeric(Byte)` | `%12.0g` |
| `gs010d4` | Why not completed gs test: r tried but was unable to complete test | `Numeric(Byte)` | `%12.0g` |
| `gs010d5` | Why not completed gs test: r did not understand the instructions | `Numeric(Byte)` | `%12.0g` |
| `gs010d6` | Why not completed gs test: r had surgery, injury, swelling, etc. | `Numeric(Byte)` | `%12.0g` |
| `gs010dot` | Why not completed gs test: others | `Numeric(Byte)` | `%12.0g` |
| `gs012_` | How much effort gave r | `Numeric(Byte)` | `%124.0g` |
| `gs013_` | The position of r for this test | `Numeric(Byte)` | `%10.0g` |
| `gs014_` | R rested his/her arms on a support | `Numeric(Byte)` | `%10.0g` |
| `gs701_` | Willing to have handgrip measured | `Numeric(Byte)` | `%61.0g` |

### `hc` - Health Care

- Dataset: `sharew8_rel9-0-0_hc.dta`
- Read with: `ps.read_share_module("hc", wave=8)`
- Rows: 53,695
- Variables: 67
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `hc010_` | Seen a dentist/dental hygienist in the last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc012_` | Stayed over night in hospital last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc013_` | Times being patient in hospital | `Numeric(Byte)` | `%10.0g` |
| `hc014_` | Total nights stayed in hospital | `Numeric(Int)` | `%10.0g` |
| `hc029_` | In a nursing home during last 12 months | `Numeric(Byte)` | `%16.0g` |
| `hc031_` | Weeks stayed in a nursing home or residential care facility | `Numeric(Byte)` | `%10.0g` |
| `hc033_` | Weeks received professional nursing care | `Numeric(Byte)` | `%10.0g` |
| `hc034_` | Hours received professional nursing care | `Numeric(Int)` | `%10.0g` |
| `hc035_` | Weeks received paid domestic help | `Numeric(Byte)` | `%10.0g` |
| `hc036_` | Hours received paid domestic help | `Numeric(Int)` | `%10.0g` |
| `hc037_` | Weeks received meals-on-wheels | `Numeric(Byte)` | `%10.0g` |
| `hc063_` | Who answered the questions in hc | `Numeric(Byte)` | `%47.0g` |
| `hc064_` | In other institutions last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc066_` | Total nights stayed in other institutions | `Numeric(Int)` | `%10.0g` |
| `hc097e` | Amount payed for stay in nursing home/residential care facility last 12 months | `Numeric(Float)` | `%10.0g` |
| `hc097ub` | Amount payed for stay in nursing home/residential care facility last 12 months u | `Numeric(Byte)` | `%32.0g` |
| `hc097v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `hc097v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `hc097v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `hc113_` | Has supplementary health insurance | `Numeric(Byte)` | `%10.0g` |
| `hc116d1` | Long-term care insurances: public (country deviations!) | `Numeric(Byte)` | `%12.0g` |
| `hc116d2` | Long-term care insurances: private mandatory (country deviations!) | `Numeric(Byte)` | `%12.0g` |
| `hc116d3` | Long-term care insurances: private voluntary/supplementary (country deviations!) | `Numeric(Byte)` | `%12.0g` |
| `hc116dno` | Long-term care insurances: none of these (country deviations!) | `Numeric(Byte)` | `%12.0g` |
| `hc125_` | Satisfaction with own coverage in basic health insurance/national health system | `Numeric(Byte)` | `%22.0g` |
| `hc127d1` | Received professional services: help with personal care in own home | `Numeric(Byte)` | `%12.0g` |
| `hc127d2` | Received professional services: help with domestic tasks in own home | `Numeric(Byte)` | `%12.0g` |
| `hc127d3` | Received professional services: meals-on-wheels | `Numeric(Byte)` | `%12.0g` |
| `hc127d4` | Received professional services: help with other activies | `Numeric(Byte)` | `%12.0g` |
| `hc127dno` | Received professional services: none of these | `Numeric(Byte)` | `%12.0g` |
| `hc602_` | Times talked to medical doctor/nurse about your health last 12 months | `Numeric(Int)` | `%10.0g` |
| `hc696_` | Payed anything yourself:stay in nursing home/residential care facility last 12 m | `Numeric(Byte)` | `%10.0g` |
| `hc751_` | Certified nurse | `Numeric(Byte)` | `%10.0g` |
| `hc841d1` | Forgo care due to cost: general practitioner | `Numeric(Byte)` | `%12.0g` |
| `hc841d2` | Forgo care due to cost: specialist physician | `Numeric(Byte)` | `%12.0g` |
| `hc841d3` | Forgo care due to cost: drugs | `Numeric(Byte)` | `%12.0g` |
| `hc841d4` | Forgo care due to cost: dental care | `Numeric(Byte)` | `%12.0g` |
| `hc841d5` | Forgo care due to cost: optical care | `Numeric(Byte)` | `%12.0g` |
| `hc841d6` | Forgo care due to cost: home care | `Numeric(Byte)` | `%12.0g` |
| `hc841d7` | Forgo care due to cost: paid home help | `Numeric(Byte)` | `%12.0g` |
| `hc841dno` | Forgo care due to cost: none of these | `Numeric(Byte)` | `%12.0g` |
| `hc841dot` | Forgo care due to cost: other | `Numeric(Byte)` | `%12.0g` |
| `hc843d1` | Forgo care due to unavailability: general practitioner | `Numeric(Byte)` | `%12.0g` |
| `hc843d2` | Forgo care due to unavailability: specialist physician | `Numeric(Byte)` | `%12.0g` |
| `hc843d3` | Forgo care due to unavailability: drugs | `Numeric(Byte)` | `%12.0g` |
| `hc843d4` | Forgo care due to unavailability: dental care | `Numeric(Byte)` | `%12.0g` |
| `hc843d5` | Forgo care due to unavailability: optical care | `Numeric(Byte)` | `%12.0g` |
| `hc843d6` | Forgo care due to unavailability: home care | `Numeric(Byte)` | `%12.0g` |
| `hc843d7` | Forgo care due to unavailability: paid home help | `Numeric(Byte)` | `%12.0g` |
| `hc843dno` | Forgo care due to unavailability: none of these | `Numeric(Byte)` | `%12.0g` |
| `hc843dot` | Forgo care due to unavailability: other | `Numeric(Byte)` | `%12.0g` |
| `hc876_` | Contacts general practitioner | `Numeric(Int)` | `%10.0g` |
| `hc877_` | Contacts specialist | `Numeric(Int)` | `%10.0g` |
| `hc884_` | Flu vaccination | `Numeric(Byte)` | `%10.0g` |
| `hc885_` | Eye exam | `Numeric(Byte)` | `%10.0g` |
| `hc886_` | Mammogram | `Numeric(Byte)` | `%10.0g` |
| `hc887_` | Colon cancer screening | `Numeric(Byte)` | `%10.0g` |
| `hc888_` | Hospitalisation: planned or emergency | `Numeric(Byte)` | `%34.0g` |
| `hc889_` | Health literacy: how often help needed | `Numeric(Byte)` | `%11.0g` |
| `hc890_` | Hospitalisations: planned or emergency | `Numeric(Byte)` | `%34.0g` |

### `hh` - Household Income

- Dataset: `sharew8_rel9-0-0_hh.dta`
- Read with: `ps.read_share_module("hh", wave=8)`
- Rows: 53,695
- Variables: 20
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `hh001_` | Other contributor to household income | `Numeric(Byte)` | `%10.0g` |
| `hh010_` | Income from other sources | `Numeric(Byte)` | `%10.0g` |
| `hh011e` | Additional income received by all hh-members last year | `Numeric(Float)` | `%10.0g` |
| `hh011ub` | Additional income received by all hh-members last year ub | `Numeric(Byte)` | `%32.0g` |
| `hh011v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `hh011v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `hh011v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `hh014_` | Who answered the question in hh | `Numeric(Byte)` | `%47.0g` |
| `hh017e` | Total income received by all hh members an average month last year | `Numeric(Float)` | `%10.0g` |
| `hh017ub` | Total income received by all hh-members an average month last year ub | `Numeric(Byte)` | `%32.0g` |
| `hh017v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `hh017v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `hh017v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |

### `ho` - Housing

- Dataset: `sharew8_rel9-0-0_ho.dta`
- Read with: `ps.read_share_module("ho", wave=8)`
- Rows: 53,695
- Variables: 127
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `ho001_` | Interview in house of respondent | `Numeric(Byte)` | `%10.0g` |
| `ho002_` | Owner, tenant or rent free | `Numeric(Byte)` | `%23.0g` |
| `ho003_` | Rent payment period | `Numeric(Byte)` | `%26.0g` |
| `ho007_` | Last rent payment included all charges and services | `Numeric(Byte)` | `%10.0g` |
| `ho008e` | Amount charges and services | `Numeric(Float)` | `%10.0g` |
| `ho008ub` | Amount charges and services ub | `Numeric(Byte)` | `%32.0g` |
| `ho008v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ho008v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ho008v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `ho010_` | More than two months behind with rent | `Numeric(Byte)` | `%10.0g` |
| `ho012_` | Year acquired property | `Numeric(Int)` | `%10.0g` |
| `ho013_` | Mortgages or loans on property | `Numeric(Byte)` | `%10.0g` |
| `ho014_` | Years left of mortgage or loan | `Numeric(Byte)` | `%10.0g` |
| `ho015e` | Amount still to pay on mortgage or loan | `Numeric(Float)` | `%10.0g` |
| `ho015ub` | Amount still to pay on mortgage or loan ub | `Numeric(Byte)` | `%32.0g` |
| `ho015v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `ho015v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ho015v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `ho017_` | Regularly repay mortgage or loans | `Numeric(Byte)` | `%10.0g` |
| `ho022_` | Behind with regular repay mortgage or loan | `Numeric(Byte)` | `%10.0g` |
| `ho023_` | Sublet or let parts of accommodation | `Numeric(Byte)` | `%10.0g` |
| `ho024e` | Value of property | `Numeric(Float)` | `%10.0g` |
| `ho024ub` | Value of property ub | `Numeric(Byte)` | `%32.0g` |
| `ho024v1` | Bracket value 1 | `Numeric(Double)` | `%12.0g` |
| `ho024v2` | Bracket value 2 | `Numeric(Double)` | `%12.0g` |
| `ho024v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `ho026_` | Own other real estate | `Numeric(Byte)` | `%10.0g` |
| `ho027e` | Value of other real estate | `Numeric(Float)` | `%10.0g` |
| `ho027ub` | Value of other real estate ub | `Numeric(Byte)` | `%32.0g` |
| `ho027v1` | Bracket value 1 | `Numeric(Double)` | `%12.0g` |
| `ho027v2` | Bracket value 2 | `Numeric(Double)` | `%12.0g` |
| `ho027v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `ho029_` | Received income or rent of other real estate | `Numeric(Byte)` | `%10.0g` |
| `ho030e` | Amount income or rent of other real estate last year | `Numeric(Float)` | `%10.0g` |
| `ho030ub` | Amount income or rent of other real estate last year ub | `Numeric(Byte)` | `%32.0g` |
| `ho030v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `ho030v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ho030v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ho032_` | Number of rooms in accommodation | `Numeric(Byte)` | `%10.0g` |
| `ho034_` | Years in accommodation | `Numeric(Byte)` | `%10.0g` |
| `ho037_` | Area where respondent lives | `Numeric(Byte)` | `%38.0g` |
| `ho041_` | Who answered the questions in ho | `Numeric(Byte)` | `%47.0g` |
| `ho043_` | Number of steps to entrance | `Numeric(Byte)` | `%14.0g` |
| `ho054_` | Elevator | `Numeric(Byte)` | `%10.0g` |
| `ho060_` | Partner years in accomodation | `Numeric(Int)` | `%10.0g` |
| `ho061_` | Years in accommodation | `Numeric(Byte)` | `%10.0g` |
| `ho067e` | Amount similar dwelling todays market | `Numeric(Float)` | `%10.0g` |
| `ho067ub` | Amount similar dwelling todays market ub | `Numeric(Byte)` | `%32.0g` |
| `ho067v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `ho067v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ho067v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ho070_` | Percentage of house owned | `Numeric(Byte)` | `%10.0g` |
| `ho074e` | Income from sublet of accomodation | `Numeric(Float)` | `%10.0g` |
| `ho074ub` | Income from sublet of accomodation ub | `Numeric(Byte)` | `%32.0g` |
| `ho074v1` | Bracket value | `Numeric(Float)` | `%8.0g` |
| `ho074v2` | Bracket value | `Numeric(Double)` | `%8.0g` |
| `ho074v3` | Bracket value | `Numeric(Double)` | `%8.0g` |
| `ho075_` | Own other real estate/houses | `Numeric(Byte)` | `%10.0g` |
| `ho076e` | Worth of properties if now sold | `Numeric(Float)` | `%10.0g` |
| `ho076ub` | Worth of properties if now sold ub | `Numeric(Byte)` | `%32.0g` |
| `ho076v1` | Bracket value 1 | `Numeric(Double)` | `%12.0g` |
| `ho076v2` | Bracket value 2 | `Numeric(Double)` | `%12.0g` |
| `ho076v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `ho077_` | Receive rent or income from properties | `Numeric(Byte)` | `%10.0g` |
| `ho078e` | Amount of income from properties | `Numeric(Float)` | `%10.0g` |
| `ho078ub` | Amount of income from properties ub | `Numeric(Byte)` | `%32.0g` |
| `ho078v1` | Bracket value 1 | `Numeric(Int)` | `%8.0g` |
| `ho078v2` | Bracket value 2 | `Numeric(Int)` | `%8.0g` |
| `ho078v3` | Bracket value 3 | `Numeric(Long)` | `%8.0g` |
| `ho079_` | Lives in social/public housing sector | `Numeric(Byte)` | `%10.0g` |
| `ho080d1` | Income used to cover nursing home: pensions | `Numeric(Byte)` | `%12.0g` |
| `ho080d2` | Income used to cover nursing home: rents/annuities/... | `Numeric(Byte)` | `%12.0g` |
| `ho080d3` | Income used to cover nursing home: assets/savings | `Numeric(Byte)` | `%12.0g` |
| `ho080d4` | Income used to cover nursing home: (grand-)children | `Numeric(Byte)` | `%12.0g` |
| `ho080d5` | Income used to cover nursing home: housing allowance/public benefits | `Numeric(Byte)` | `%12.0g` |
| `ho080d6` | Income used to cover nursing home: public long-term care service | `Numeric(Byte)` | `%12.0g` |
| `ho080d7` | Income used to cover nursing home: private long-term care service | `Numeric(Byte)` | `%12.0g` |
| `ho080dot` | Income used to cover nursing home: other | `Numeric(Byte)` | `%12.0g` |
| `ho605e` | Amount of last gross rent payment | `Numeric(Float)` | `%10.0g` |
| `ho605ub` | Amount of last gross rent payment ub | `Numeric(Byte)` | `%32.0g` |
| `ho605v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ho605v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ho605v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ho611d1` | How property acquired: own means | `Numeric(Byte)` | `%12.0g` |
| `ho611d2` | How property acquired: loan/mortgage | `Numeric(Byte)` | `%12.0g` |
| `ho611d3` | How property acquired: help from family | `Numeric(Byte)` | `%12.0g` |
| `ho611d4` | How property acquired: bequest | `Numeric(Byte)` | `%12.0g` |
| `ho611d5` | How property acquired: gift | `Numeric(Byte)` | `%12.0g` |
| `ho611d6` | How property acquired: other means | `Numeric(Byte)` | `%12.0g` |
| `ho620e` | Amount payed for mortgages/loans on property last 12 months | `Numeric(Float)` | `%10.0g` |
| `ho620ub` | Amount payed for mortgages/loans on property last 12 months ub | `Numeric(Byte)` | `%32.0g` |
| `ho620v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `ho620v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ho620v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ho633d1` | Special features in accommodation: widened doors/corridors | `Numeric(Byte)` | `%12.0g` |
| `ho633d2` | Special features in accommodation: ramps/street level entrance | `Numeric(Byte)` | `%12.0g` |
| `ho633d3` | Special features in accommodation: hand rails | `Numeric(Byte)` | `%12.0g` |
| `ho633d4` | Special features in accommodation: automatic/easy open doors | `Numeric(Byte)` | `%12.0g` |
| `ho633d5` | Special features in accommodation: bathroom/toilet modifications | `Numeric(Byte)` | `%12.0g` |
| `ho633d6` | Special features in accommodation: kitchen modifications | `Numeric(Byte)` | `%12.0g` |
| `ho633d7` | Special features in accommodation: chair lifts/stair glides | `Numeric(Byte)` | `%12.0g` |
| `ho633d8` | Special features in accommodation: alerting devices | `Numeric(Byte)` | `%12.0g` |
| `ho633dno` | Special features in accommodation: none of these | `Numeric(Byte)` | `%12.0g` |
| `ho633dot` | Special features in accommodation: other | `Numeric(Byte)` | `%12.0g` |
| `ho636_` | Type of building | `Numeric(Byte)` | `%97.0g` |
| `ho662_` | Has to pay out-of-pocket for nursing home accommodation | `Numeric(Byte)` | `%10.0g` |
| `ho665e` | Amount paying out-of-pocket for nursing home a typical month | `Numeric(Float)` | `%10.0g` |
| `ho665ub` | Amount paying out-of-pocket for nursing home a typical month ub | `Numeric(Byte)` | `%32.0g` |
| `ho665v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ho665v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ho665v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `ho666d1` | Payment nursinghome covers: lodging (room) | `Numeric(Byte)` | `%12.0g` |
| `ho666d2` | Payment nursinghome covers: meals | `Numeric(Byte)` | `%12.0g` |
| `ho666d3` | Payment nursinghome covers: nursing/care service | `Numeric(Byte)` | `%12.0g` |
| `ho666d4` | Payment nursinghome covers: rehabilitation/other health services | `Numeric(Byte)` | `%12.0g` |
| `ho666d5` | Payment nursinghome covers: laundry | `Numeric(Byte)` | `%12.0g` |
| `ho666d6` | Payment nursinghome covers: charges and services | `Numeric(Byte)` | `%12.0g` |
| `ho666d7` | Payment nursinghome covers: other expenses | `Numeric(Byte)` | `%12.0g` |
| `ho666dno` | Payment nursinghome covers: none of these | `Numeric(Byte)` | `%12.0g` |
| `ho782_` | Certified nurse | `Numeric(Byte)` | `%10.0g` |

### `it` - Computer Use

- Dataset: `sharew8_rel9-0-0_it.dta`
- Read with: `ps.read_share_module("it", wave=8)`
- Rows: 53,695
- Variables: 10
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `it001_` | Current job requires using a computer | `Numeric(Byte)` | `%10.0g` |
| `it002_` | Last job before retiring required using a computer | `Numeric(Byte)` | `%10.0g` |
| `it003_` | Computer skills | `Numeric(Byte)` | `%54.0g` |
| `it004_` | Use of internet in past 7 days | `Numeric(Byte)` | `%10.0g` |

### `iv` - Interviewer Observations

- Dataset: `sharew8_rel9-0-0_iv.dta`
- Read with: `ps.read_share_module("iv", wave=8)`
- Rows: 53,695
- Variables: 27
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `intidwX` | Interviewer identifier (fix across waves) | `Str(11)` | `%11s` |
| `intid` | Interviewer identifier (wave-specific) | `Str(10)` | `%10s` |
| `iv002d1` | Present during interview: nobody else | `Numeric(Byte)` | `%12.0g` |
| `iv002d2` | Present during interview: spouse or partner | `Numeric(Byte)` | `%12.0g` |
| `iv002d3` | Present during interview: parent(s) | `Numeric(Byte)` | `%12.0g` |
| `iv002d4` | Present during interview: child(ren) | `Numeric(Byte)` | `%12.0g` |
| `iv002d5` | Present during interview: other relative(s) | `Numeric(Byte)` | `%12.0g` |
| `iv002d6` | Present during interview: other person(s) | `Numeric(Byte)` | `%12.0g` |
| `iv003_` | Intervened in interview | `Numeric(Byte)` | `%17.0g` |
| `iv004_` | Willingness to answer | `Numeric(Byte)` | `%61.0g` |
| `iv005d1` | Why willingness worse: respondent was losing interest | `Numeric(Byte)` | `%12.0g` |
| `iv005d2` | Why willingness worse: respondent was losing concentration | `Numeric(Byte)` | `%12.0g` |
| `iv005d3` | Why willingness worse: other | `Numeric(Byte)` | `%12.0g` |
| `iv007_` | Respondent asked for clarification | `Numeric(Byte)` | `%12.0g` |
| `iv008_` | Respondent understood questions | `Numeric(Byte)` | `%12.0g` |
| `iv009_` | Which area building located | `Numeric(Byte)` | `%38.0g` |
| `iv012_` | Number of steps to entrance | `Numeric(Byte)` | `%14.0g` |
| `iv018_` | Help needed reading showcards | `Numeric(Byte)` | `%33.0g` |
| `iv020_` | Relationship proxy | `Numeric(Byte)` | `%43.0g` |
| `iv610_` | Type of building hh lives in | `Numeric(Byte)` | `%97.0g` |
| `iv621_` | Certified nurse | `Numeric(Byte)` | `%10.0g` |

### `mh` - Mental Health

- Dataset: `sharew8_rel9-0-0_mh.dta`
- Read with: `ps.read_share_module("mh", wave=8)`
- Rows: 53,695
- Variables: 27
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `mh002_` | Sad or depressed last month | `Numeric(Byte)` | `%10.0g` |
| `mh003_` | Hopes for the future | `Numeric(Byte)` | `%34.0g` |
| `mh004_` | Suicidal feelings or wish to be dead | `Numeric(Byte)` | `%64.0g` |
| `mh005_` | Feels guilty | `Numeric(Byte)` | `%131.0g` |
| `mh006_` | Blame for what | `Numeric(Byte)` | `%189.0g` |
| `mh007_` | Trouble sleeping | `Numeric(Byte)` | `%76.0g` |
| `mh008_` | Less or same interest in things | `Numeric(Byte)` | `%49.0g` |
| `mh009_` | Keeps up interest | `Numeric(Byte)` | `%10.0g` |
| `mh010_` | Irritability | `Numeric(Byte)` | `%10.0g` |
| `mh011_` | Appetite | `Numeric(Byte)` | `%49.0g` |
| `mh012_` | Eating more or less | `Numeric(Byte)` | `%21.0g` |
| `mh013_` | Fatigue | `Numeric(Byte)` | `%10.0g` |
| `mh014_` | Concentration on entertainment | `Numeric(Byte)` | `%77.0g` |
| `mh015_` | Concentration on reading | `Numeric(Byte)` | `%51.0g` |
| `mh016_` | Enjoyment | `Numeric(Byte)` | `%74.0g` |
| `mh017_` | Tearfulness | `Numeric(Byte)` | `%10.0g` |
| `mh032_` | End non proxy | `Numeric(Byte)` | `%62.0g` |
| `mh034_` | Feels lack of companionship | `Numeric(Byte)` | `%20.0g` |
| `mh035_` | Feels left out | `Numeric(Byte)` | `%20.0g` |
| `mh036_` | Feels isolated from others | `Numeric(Byte)` | `%20.0g` |
| `mh037_` | Feels lonely | `Numeric(Byte)` | `%20.0g` |

### `ph` - Physical Health

- Dataset: `sharew8_rel9-0-0_ph.dta`
- Read with: `ps.read_share_module("ph", wave=8)`
- Rows: 53,695
- Variables: 196
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ph003_` | Health in general question 2 | `Numeric(Byte)` | `%16.0g` |
| `ph004_` | Long-term illness | `Numeric(Byte)` | `%10.0g` |
| `ph005_` | Limited in activities because of health | `Numeric(Byte)` | `%35.0g` |
| `ph006d1` | Heart attack: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d2` | High blood pressure or hypertension: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d3` | High blood cholesterol: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d4` | Stroke: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d5` | Diabetes or high blood sugar: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d6` | Chronic lung disease: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d10` | Cancer: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d11` | Stomach or duodenal ulcer, peptic ulcer: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d12` | Parkinson disease: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d13` | Cataracts: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d14` | Hip fracture or femoral fracture: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d15` | Other fractures: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d16` | Alzheimer's disease, dementia, senility: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d18` | Other affective/emotional disorders: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d19` | Rheumatoid arthritis: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d20` | Osteoarthritis/other rheumatism: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d21` | Chronic kidney disease: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006dno` | None: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006dot` | Other: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph008d1` | Cancer in: brain | `Numeric(Byte)` | `%12.0g` |
| `ph008d2` | Cancer in: oral cavity | `Numeric(Byte)` | `%12.0g` |
| `ph008d3` | Cancer in: larynx | `Numeric(Byte)` | `%12.0g` |
| `ph008d4` | Cancer in: other pharynx | `Numeric(Byte)` | `%12.0g` |
| `ph008d5` | Cancer in: thyroid | `Numeric(Byte)` | `%12.0g` |
| `ph008d6` | Cancer in: lung | `Numeric(Byte)` | `%12.0g` |
| `ph008d7` | Cancer in: breast | `Numeric(Byte)` | `%12.0g` |
| `ph008d8` | Cancer in: oesophagus | `Numeric(Byte)` | `%12.0g` |
| `ph008d9` | Cancer in: stomach | `Numeric(Byte)` | `%12.0g` |
| `ph008d10` | Cancer in: liver | `Numeric(Byte)` | `%12.0g` |
| `ph008d11` | Cancer in: pancreas | `Numeric(Byte)` | `%12.0g` |
| `ph008d12` | Cancer in: kidney | `Numeric(Byte)` | `%12.0g` |
| `ph008d13` | Cancer in: prostate | `Numeric(Byte)` | `%12.0g` |
| `ph008d14` | Cancer in: testicle | `Numeric(Byte)` | `%12.0g` |
| `ph008d15` | Cancer in: ovary | `Numeric(Byte)` | `%12.0g` |
| `ph008d16` | Cancer in: cervix | `Numeric(Byte)` | `%12.0g` |
| `ph008d17` | Cancer in: endometrium | `Numeric(Byte)` | `%12.0g` |
| `ph008d18` | Cancer in: colon or rectum | `Numeric(Byte)` | `%12.0g` |
| `ph008d19` | Cancer in: bladder | `Numeric(Byte)` | `%12.0g` |
| `ph008d20` | Cancer in: skin | `Numeric(Byte)` | `%12.0g` |
| `ph008d21` | Cancer in: non-hodgkin lymphoma | `Numeric(Byte)` | `%12.0g` |
| `ph008d22` | Cancer in: leukaemia | `Numeric(Byte)` | `%12.0g` |
| `ph008dot` | Cancer in: other organ | `Numeric(Byte)` | `%12.0g` |
| `ph009_1` | Age heart attack or other heart problems | `Numeric(Byte)` | `%10.0g` |
| `ph009_2` | Age high blood pressure | `Numeric(Byte)` | `%10.0g` |
| `ph009_3` | Age high blood cholesterol | `Numeric(Byte)` | `%10.0g` |
| `ph009_4` | Age stroke or cerebral vascular disease | `Numeric(Byte)` | `%10.0g` |
| `ph009_5` | Age diabetes | `Numeric(Byte)` | `%10.0g` |
| `ph009_6` | Age chronic lung disease | `Numeric(Byte)` | `%10.0g` |
| `ph009_10` | Age cancer or malignant tumour | `Numeric(Byte)` | `%10.0g` |
| `ph009_11` | Age stomach, duodenal or peptic ulcer | `Numeric(Byte)` | `%10.0g` |
| `ph009_12` | Age parkinson disease | `Numeric(Byte)` | `%10.0g` |
| `ph009_13` | Age cataracts | `Numeric(Byte)` | `%10.0g` |
| `ph009_14` | Age hip or femoral fracture | `Numeric(Byte)` | `%10.0g` |
| `ph009_15` | Age other fractures | `Numeric(Byte)` | `%10.0g` |
| `ph009_16` | Age alzheimer's disease | `Numeric(Byte)` | `%10.0g` |
| `ph009_18` | Age affective or emotional disorders | `Numeric(Byte)` | `%10.0g` |
| `ph009_19` | Age rheumatoid arthritis | `Numeric(Byte)` | `%10.0g` |
| `ph009_20` | Age osteoarthritis, or other rheumatism | `Numeric(Byte)` | `%10.0g` |
| `ph009_21` | Age chronic kidney disease | `Numeric(Byte)` | `%10.0g` |
| `ph009_other` | Age other condition | `Numeric(Byte)` | `%10.0g` |
| `ph011d1` | Drugs for: high blood cholesterol | `Numeric(Byte)` | `%12.0g` |
| `ph011d2` | Drugs for: high blood pressure | `Numeric(Byte)` | `%12.0g` |
| `ph011d3` | Drugs for: coronary diseases | `Numeric(Byte)` | `%12.0g` |
| `ph011d4` | Drugs for: other heart diseases | `Numeric(Byte)` | `%12.0g` |
| `ph011d6` | Drugs for: diabetes | `Numeric(Byte)` | `%12.0g` |
| `ph011d7` | Drugs for: joint pain | `Numeric(Byte)` | `%12.0g` |
| `ph011d8` | Drugs for: other pain | `Numeric(Byte)` | `%12.0g` |
| `ph011d9` | Drugs for: sleep problems | `Numeric(Byte)` | `%12.0g` |
| `ph011d10` | Drugs for: anxiety or depression | `Numeric(Byte)` | `%12.0g` |
| `ph011d11` | Drugs for: osteoporosis | `Numeric(Byte)` | `%12.0g` |
| `ph011d13` | Drugs for: stomach burns | `Numeric(Byte)` | `%12.0g` |
| `ph011d14` | Drugs for: chronic bronchitis | `Numeric(Byte)` | `%12.0g` |
| `ph011d15` | Drugs for: suppressing inflammation (only glucocorticoids or steroids) | `Numeric(Byte)` | `%12.0g` |
| `ph011dno` | Drugs for: none | `Numeric(Byte)` | `%12.0g` |
| `ph011dot` | Drugs for: other | `Numeric(Byte)` | `%12.0g` |
| `ph012_` | Weight of respondent | `Numeric(Int)` | `%10.0g` |
| `ph013_` | How tall are you? | `Numeric(Int)` | `%10.0g` |
| `ph041_` | Wears glasses/contact lenses | `Numeric(Byte)` | `%10.0g` |
| `ph043_` | Eyesight distance | `Numeric(Byte)` | `%16.0g` |
| `ph044_` | Eyesight reading | `Numeric(Byte)` | `%16.0g` |
| `ph045_` | Use hearing aid | `Numeric(Byte)` | `%10.0g` |
| `ph046_` | Hearing | `Numeric(Byte)` | `%16.0g` |
| `ph048d1` | Difficulties: walking 100 metres | `Numeric(Byte)` | `%12.0g` |
| `ph048d2` | Difficulties: sitting two hours | `Numeric(Byte)` | `%12.0g` |
| `ph048d3` | Difficulties: getting up from chair | `Numeric(Byte)` | `%12.0g` |
| `ph048d4` | Difficulties: climbing several flights of stairs | `Numeric(Byte)` | `%12.0g` |
| `ph048d5` | Difficulties: climbing one flight of stairs | `Numeric(Byte)` | `%12.0g` |
| `ph048d6` | Difficulties: stooping, kneeling, crouching | `Numeric(Byte)` | `%12.0g` |
| `ph048d7` | Difficulties: reaching or extending arms above shoulder | `Numeric(Byte)` | `%12.0g` |
| `ph048d8` | Difficulties: pulling or pushing large objects | `Numeric(Byte)` | `%12.0g` |
| `ph048d9` | Difficulties: lifting or carrying weights over 5 kilos | `Numeric(Byte)` | `%12.0g` |
| `ph048d10` | Difficulties: picking up a small coin from a table | `Numeric(Byte)` | `%12.0g` |
| `ph048dno` | Difficulties: none of these | `Numeric(Byte)` | `%12.0g` |
| `ph049d1` | Difficulties: dressing, including shoes and socks | `Numeric(Byte)` | `%12.0g` |
| `ph049d2` | Difficulties: walking across a room | `Numeric(Byte)` | `%12.0g` |
| `ph049d3` | Difficulties: bathing or showering | `Numeric(Byte)` | `%12.0g` |
| `ph049d4` | Difficulties: eating, cutting up food | `Numeric(Byte)` | `%12.0g` |
| `ph049d5` | Difficulties: getting in or out of bed | `Numeric(Byte)` | `%12.0g` |
| `ph049d6` | Difficulties: using the toilet, incl getting up or down | `Numeric(Byte)` | `%12.0g` |
| `ph049d7` | Difficulties: using a map in a strange place | `Numeric(Byte)` | `%12.0g` |
| `ph049d8` | Difficulties: preparing a hot meal | `Numeric(Byte)` | `%12.0g` |
| `ph049d9` | Difficulties: shopping for groceries | `Numeric(Byte)` | `%12.0g` |
| `ph049d10` | Difficulties: telephone calls | `Numeric(Byte)` | `%12.0g` |
| `ph049d11` | Difficulties: taking medications | `Numeric(Byte)` | `%12.0g` |
| `ph049d12` | Difficulties: doing work around the house or garden | `Numeric(Byte)` | `%12.0g` |
| `ph049d13` | Difficulties: managing money | `Numeric(Byte)` | `%12.0g` |
| `ph049d14` | Difficulties: leaving the house independently/accessing transportation | `Numeric(Byte)` | `%12.0g` |
| `ph049d15` | Difficulties: doing personal laundry | `Numeric(Byte)` | `%12.0g` |
| `ph049dno` | Difficulties: none of these | `Numeric(Byte)` | `%12.0g` |
| `ph050_` | Help activities | `Numeric(Byte)` | `%10.0g` |
| `ph051_` | Help meets needs | `Numeric(Byte)` | `%15.0g` |
| `ph054_` | Who answered the questions in ph | `Numeric(Byte)` | `%47.0g` |
| `ph059d1` | Use of aids: a cane or walking stick | `Numeric(Byte)` | `%12.0g` |
| `ph059d2` | Use of aids: a zimmer frame or walker | `Numeric(Byte)` | `%12.0g` |
| `ph059d3` | Use of aids: a manual wheelchair | `Numeric(Byte)` | `%12.0g` |
| `ph059d4` | Use of aids: an electric wheelchair | `Numeric(Byte)` | `%12.0g` |
| `ph059d5` | Use of aids: a buggy or scooter | `Numeric(Byte)` | `%12.0g` |
| `ph059d6` | Use of aids: special eating utensils | `Numeric(Byte)` | `%12.0g` |
| `ph059d7` | Use of aids: a personal alarm | `Numeric(Byte)` | `%12.0g` |
| `ph059d8` | Use of aids: bars/grabs/rails | `Numeric(Byte)` | `%12.0g` |
| `ph059d9` | Use of aids: raised toilet seat | `Numeric(Byte)` | `%12.0g` |
| `ph059d10` | Use of aids: incontinence pads | `Numeric(Byte)` | `%12.0g` |
| `ph059dno` | Use of aids: none of these | `Numeric(Byte)` | `%12.0g` |
| `ph059dot` | Use of aids: other | `Numeric(Byte)` | `%12.0g` |
| `ph061_` | Health problem that limits paid work | `Numeric(Byte)` | `%10.0g` |
| `ph065_` | Check: lost weight | `Numeric(Byte)` | `%10.0g` |
| `ph066_` | Reason lost weight | `Numeric(Byte)` | `%54.0g` |
| `ph071_1` | How many heart attacks since last interview | `Numeric(Byte)` | `%14.0g` |
| `ph071_2` | How many strokes/diagnosed cerebral vascular disease since last interview | `Numeric(Byte)` | `%14.0g` |
| `ph071_3` | How often diagnosed with cancer since last interview | `Numeric(Byte)` | `%14.0g` |
| `ph071_4` | How often suffered a hip fracture since last interview | `Numeric(Byte)` | `%14.0g` |
| `ph072_1` | Had a heart attack since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph072_2` | Had a stroke/diagnosed with cerebral vascular disease since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph072_3` | Been diagnosed with cancer since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph072_4` | Suffered a hip fracture since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph076_1` | Year most recent condition: heart atttack | `Numeric(Int)` | `%10.0g` |
| `ph076_2` | Year most recent condition: stroke/cerebral vascular disease | `Numeric(Int)` | `%10.0g` |
| `ph076_3` | Year most recent condition: cancer | `Numeric(Int)` | `%10.0g` |
| `ph076_4` | Year most recent condition: hip fracture | `Numeric(Int)` | `%10.0g` |
| `ph077_1` | Month most recent condition: heart atttack | `Numeric(Byte)` | `%12.0g` |
| `ph077_2` | Month most recent condition: stroke/cerebral vascular disease | `Numeric(Byte)` | `%12.0g` |
| `ph077_3` | Month most recent condition: cancer | `Numeric(Byte)` | `%12.0g` |
| `ph077_4` | Month most recent condition: hip fracture | `Numeric(Byte)` | `%12.0g` |
| `ph080d1` | Cancer in which organs: brain | `Numeric(Byte)` | `%12.0g` |
| `ph080d2` | Cancer in which organs: oral cavity | `Numeric(Byte)` | `%12.0g` |
| `ph080d3` | Cancer in which organs: larynx | `Numeric(Byte)` | `%12.0g` |
| `ph080d4` | Cancer in which organs: other pharynx | `Numeric(Byte)` | `%12.0g` |
| `ph080d5` | Cancer in which organs: thyroid | `Numeric(Byte)` | `%12.0g` |
| `ph080d6` | Cancer in which organs: lung | `Numeric(Byte)` | `%12.0g` |
| `ph080d7` | Cancer in which organs: breast | `Numeric(Byte)` | `%12.0g` |
| `ph080d8` | Cancer in which organs: oesophagus | `Numeric(Byte)` | `%12.0g` |
| `ph080d9` | Cancer in which organs: stomach | `Numeric(Byte)` | `%12.0g` |
| `ph080d10` | Cancer in which organs: liver | `Numeric(Byte)` | `%12.0g` |
| `ph080d11` | Cancer in which organs: pancreas | `Numeric(Byte)` | `%12.0g` |
| `ph080d12` | Cancer in which organs: kidney | `Numeric(Byte)` | `%12.0g` |
| `ph080d13` | Cancer in which organs: prostate | `Numeric(Byte)` | `%12.0g` |
| `ph080d14` | Cancer in which organs: testicle | `Numeric(Byte)` | `%12.0g` |
| `ph080d15` | Cancer in which organs: ovary | `Numeric(Byte)` | `%12.0g` |
| `ph080d16` | Cancer in which organs: cervix | `Numeric(Byte)` | `%12.0g` |
| `ph080d17` | Cancer in which organs: endometrium | `Numeric(Byte)` | `%12.0g` |
| `ph080d18` | Cancer in which organs: colon or rectum | `Numeric(Byte)` | `%12.0g` |
| `ph080d19` | Cancer in which organs: bladder | `Numeric(Byte)` | `%12.0g` |
| `ph080d20` | Cancer in which organs: skin | `Numeric(Byte)` | `%12.0g` |
| `ph080d21` | Cancer in which organs: lymphoma | `Numeric(Byte)` | `%12.0g` |
| `ph080d22` | Cancer in which organs: leukaemia | `Numeric(Byte)` | `%12.0g` |
| `ph080dot` | Cancer in which organs: other | `Numeric(Byte)` | `%12.0g` |
| `ph082_` | At least taking 5 different drugs a typical day | `Numeric(Byte)` | `%10.0g` |
| `ph084_` | Troubled with pain | `Numeric(Byte)` | `%10.0g` |
| `ph085_` | Level of pain | `Numeric(Byte)` | `%16.0g` |
| `ph087d1` | Pain location: back | `Numeric(Byte)` | `%12.0g` |
| `ph087d2` | Pain location: hips | `Numeric(Byte)` | `%12.0g` |
| `ph087d3` | Pain location: knees | `Numeric(Byte)` | `%12.0g` |
| `ph087d4` | Pain location: other joints | `Numeric(Byte)` | `%12.0g` |
| `ph087d5` | Pain location: mouth/teeth | `Numeric(Byte)` | `%12.0g` |
| `ph087d6` | Pain location: other parts of the body but not joints | `Numeric(Byte)` | `%12.0g` |
| `ph087d7` | Pain location: all over | `Numeric(Byte)` | `%12.0g` |
| `ph089d1` | Bothered by frailty: falling down | `Numeric(Byte)` | `%12.0g` |
| `ph089d2` | Bothered by frailty: fear of falling down | `Numeric(Byte)` | `%12.0g` |
| `ph089d3` | Bothered by frailty: dizziness, faints or blackouts | `Numeric(Byte)` | `%12.0g` |
| `ph089d4` | Bothered by frailty: fatigue | `Numeric(Byte)` | `%12.0g` |
| `ph089dno` | Bothered by frailty: none | `Numeric(Byte)` | `%12.0g` |
| `ph095_` | How much loss of weight (in kg) | `Numeric(Byte)` | `%10.0g` |
| `ph690d1` | Type of glases/contact lenses: bifocal/progressive | `Numeric(Byte)` | `%12.0g` |
| `ph690d2` | Type of glases/contact lenses: reading (single vision glasses) | `Numeric(Byte)` | `%12.0g` |
| `ph690d3` | Type of glases/contact lenses: distance (single vision glasses) | `Numeric(Byte)` | `%12.0g` |
| `ph690d4` | Type of glases/contact lenses: other | `Numeric(Byte)` | `%12.0g` |
| `ph745_` | Have hearing aid | `Numeric(Byte)` | `%10.0g` |

### `sn` - Social Networks

- Dataset: `sharew8_rel9-0-0_sn.dta`
- Read with: `ps.read_share_module("sn", wave=8)`
- Rows: 53,695
- Variables: 106
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sn002a_1` | Any more persons with whom you often discuss: sn person 1 | `Numeric(Byte)` | `%10.0g` |
| `sn002a_2` | Any more persons with whom you often discuss: sn person 2 | `Numeric(Byte)` | `%10.0g` |
| `sn002a_3` | Any more persons with whom you often discuss: sn person 3 | `Numeric(Byte)` | `%10.0g` |
| `sn002a_4` | Any more persons with whom you often discuss: sn person 4 | `Numeric(Byte)` | `%10.0g` |
| `sn002a_5` | Any more persons with whom you often discuss: sn person 5 | `Numeric(Byte)` | `%10.0g` |
| `sn002a_6` | Any more persons with whom you often discuss: sn person 6 | `Numeric(Byte)` | `%10.0g` |
| `sn002a_7` | Any more persons with whom you often discuss: sn person 7 | `Numeric(Byte)` | `%10.0g` |
| `sn003a_` | Anyone else very important | `Numeric(Byte)` | `%10.0g` |
| `sn005_1` | Network relationship: sn person 1 | `Numeric(Byte)` | `%60.0g` |
| `sn005_2` | Network relationship: sn person 2 | `Numeric(Byte)` | `%60.0g` |
| `sn005_3` | Network relationship: sn person 3 | `Numeric(Byte)` | `%60.0g` |
| `sn005_4` | Network relationship: sn person 4 | `Numeric(Byte)` | `%60.0g` |
| `sn005_5` | Network relationship: sn person 5 | `Numeric(Byte)` | `%60.0g` |
| `sn005_6` | Network relationship: sn person 6 | `Numeric(Byte)` | `%60.0g` |
| `sn005_7` | Network relationship: sn person 7 | `Numeric(Byte)` | `%60.0g` |
| `sn005a_1` | Network person gender: sn person 1 | `Numeric(Byte)` | `%12.0g` |
| `sn005a_2` | Network person gender: sn person 2 | `Numeric(Byte)` | `%12.0g` |
| `sn005a_3` | Network person gender: sn person 3 | `Numeric(Byte)` | `%12.0g` |
| `sn005a_4` | Network person gender: sn person 4 | `Numeric(Byte)` | `%12.0g` |
| `sn005a_5` | Network person gender: sn person 5 | `Numeric(Byte)` | `%12.0g` |
| `sn005a_6` | Network person gender: sn person 6 | `Numeric(Byte)` | `%12.0g` |
| `sn005a_7` | Network person gender: sn person 7 | `Numeric(Byte)` | `%12.0g` |
| `sn006_1` | Network proximity: sn person 1 | `Numeric(Byte)` | `%42.0g` |
| `sn006_2` | Network proximity: sn person 2 | `Numeric(Byte)` | `%42.0g` |
| `sn006_3` | Network proximity: sn person 3 | `Numeric(Byte)` | `%42.0g` |
| `sn006_4` | Network proximity: sn person 4 | `Numeric(Byte)` | `%42.0g` |
| `sn006_5` | Network proximity: sn person 5 | `Numeric(Byte)` | `%42.0g` |
| `sn006_6` | Network proximity: sn person 6 | `Numeric(Byte)` | `%42.0g` |
| `sn006_7` | Network proximity: sn person 7 | `Numeric(Byte)` | `%42.0g` |
| `sn007_1` | Network contact: sn person 1 | `Numeric(Byte)` | `%30.0g` |
| `sn007_2` | Network contact: sn person 2 | `Numeric(Byte)` | `%30.0g` |
| `sn007_3` | Network contact: sn person 3 | `Numeric(Byte)` | `%30.0g` |
| `sn007_4` | Network contact: sn person 4 | `Numeric(Byte)` | `%30.0g` |
| `sn007_5` | Network contact: sn person 5 | `Numeric(Byte)` | `%30.0g` |
| `sn007_6` | Network contact: sn person 6 | `Numeric(Byte)` | `%30.0g` |
| `sn007_7` | Network contact: sn person 7 | `Numeric(Byte)` | `%30.0g` |
| `sn009_1` | Network closeness: sn person 1 | `Numeric(Byte)` | `%18.0g` |
| `sn009_2` | Network closeness: sn person 2 | `Numeric(Byte)` | `%18.0g` |
| `sn009_3` | Network closeness: sn person 3 | `Numeric(Byte)` | `%18.0g` |
| `sn009_4` | Network closeness: sn person 4 | `Numeric(Byte)` | `%18.0g` |
| `sn009_5` | Network closeness: sn person 5 | `Numeric(Byte)` | `%18.0g` |
| `sn009_6` | Network closeness: sn person 6 | `Numeric(Byte)` | `%18.0g` |
| `sn009_7` | Network closeness: sn person 7 | `Numeric(Byte)` | `%18.0g` |
| `sn012_` | Network satisfaction | `Numeric(Byte)` | `%10.0g` |
| `sn014_` | Privacy SN | `Numeric(Byte)` | `%97.0g` |
| `sn015d1` | Who was present: respondent alone | `Numeric(Byte)` | `%12.0g` |
| `sn015d2` | Who was present: partner present | `Numeric(Byte)` | `%12.0g` |
| `sn015d3` | Who was present: child(ren) present | `Numeric(Byte)` | `%12.0g` |
| `sn015dot` | Who was present: other(s) | `Numeric(Byte)` | `%12.0g` |
| `sn017_` | Empty network satisfaction | `Numeric(Byte)` | `%10.0g` |
| `sn023_1` | Reason did not mention sn person 1 | `Numeric(Byte)` | `%67.0g` |
| `sn023_2` | Reason did not mention sn person 2 | `Numeric(Byte)` | `%67.0g` |
| `sn023_3` | Reason did not mention sn person 3 | `Numeric(Byte)` | `%67.0g` |
| `sn023_4` | Reason did not mention sn person 4 | `Numeric(Byte)` | `%67.0g` |
| `sn023_5` | Reason did not mention sn person 5 | `Numeric(Byte)` | `%67.0g` |
| `sn023_6` | Reason did not mention sn person 6 | `Numeric(Byte)` | `%67.0g` |
| `sn023_7` | Reason did not mention sn person 7 | `Numeric(Byte)` | `%67.0g` |
| `sn023_8` | Reason did not mention sn person 8 | `Numeric(Byte)` | `%67.0g` |
| `sn023_9` | Reason did not mention sn person 9 | `Numeric(Byte)` | `%67.0g` |
| `sn023_10` | Reason did not mention sn person 10 | `Numeric(Byte)` | `%67.0g` |
| `sn023_11` | Reason did not mention sn person 11 | `Numeric(Byte)` | `%67.0g` |
| `sn023_12` | Reason did not mention sn person 12 | `Numeric(Byte)` | `%67.0g` |
| `sn023_13` | Reason did not mention sn person 13 | `Numeric(Byte)` | `%67.0g` |
| `sn023_14` | Reason did not mention sn person 14 | `Numeric(Byte)` | `%67.0g` |
| `sn027_1` | Year of birth sn person 1 | `Numeric(Int)` | `%10.0g` |
| `sn027_2` | Year of birth sn person 2 | `Numeric(Int)` | `%10.0g` |
| `sn027_3` | Year of birth sn person 3 | `Numeric(Int)` | `%10.0g` |
| `sn027_4` | Year of birth sn person 4 | `Numeric(Int)` | `%10.0g` |
| `sn027_5` | Year of birth sn person 5 | `Numeric(Int)` | `%10.0g` |
| `sn027_6` | Year of birth sn person 6 | `Numeric(Int)` | `%10.0g` |
| `sn027_7` | Year of birth sn person 7 | `Numeric(Int)` | `%10.0g` |
| `sn840_1` | Confirm mismatched relation: sn person 1 | `Numeric(Byte)` | `%21.0g` |
| `sn840_2` | Confirm mismatched relation: sn person 2 | `Numeric(Byte)` | `%21.0g` |
| `sn840_3` | Confirm mismatched relation: sn person 3 | `Numeric(Byte)` | `%21.0g` |
| `sn840_4` | Confirm mismatched relation: sn person 4 | `Numeric(Byte)` | `%21.0g` |
| `sn840_5` | Confirm mismatched relation: sn person 5 | `Numeric(Byte)` | `%21.0g` |
| `sn840_6` | Confirm mismatched relation: sn person 6 | `Numeric(Byte)` | `%21.0g` |
| `sn840_7` | Confirm mismatched relation: sn person 7 | `Numeric(Byte)` | `%21.0g` |
| `sn840_8` | Confirm mismatched relation: sn person 8 | `Numeric(Byte)` | `%21.0g` |
| `sn840_9` | Confirm mismatched relation: sn person 9 | `Numeric(Byte)` | `%21.0g` |
| `sn840_10` | Confirm mismatched relation: sn person 10 | `Numeric(Byte)` | `%21.0g` |
| `sn840_11` | Confirm mismatched relation: sn person 11 | `Numeric(Byte)` | `%21.0g` |
| `sn840_12` | Confirm mismatched relation: sn person 12 | `Numeric(Byte)` | `%21.0g` |
| `sn840_13` | Confirm mismatched relation: sn person 13 | `Numeric(Byte)` | `%21.0g` |
| `sn840_14` | Confirm mismatched relation: sn person 14 | `Numeric(Byte)` | `%21.0g` |
| `sn841_` | Who answered questions in sn | `Numeric(Byte)` | `%62.0g` |
| `sn_child_loop_1` | Child link: sn person 1 mentioned as child (loop) | `Numeric(Byte)` | `%13.0g` |
| `sn_child_loop_2` | Child link: sn person 2 mentioned as child (loop) | `Numeric(Byte)` | `%13.0g` |
| `sn_child_loop_3` | Child link: sn person 3 mentioned as child (loop) | `Numeric(Byte)` | `%13.0g` |
| `sn_child_loop_4` | Child link: sn person 4 mentioned as child (loop) | `Numeric(Byte)` | `%13.0g` |
| `sn_child_loop_5` | Child link: sn person 5 mentioned as child (loop) | `Numeric(Byte)` | `%13.0g` |
| `sn_child_loop_6` | Child link: sn person 6 mentioned as child (loop) | `Numeric(Byte)` | `%13.0g` |
| `sn_child_loop_7` | Child link: sn person 7 mentioned as child (loop) | `Numeric(Byte)` | `%13.0g` |
| `sn_childid_1` | Child link: sn person 1 child identifier (fix across modules and waves) | `Str(14)` | `%14s` |
| `sn_childid_2` | Child link: sn person 2 child identifier (fix across modules and waves) | `Str(14)` | `%14s` |
| `sn_childid_3` | Child link: sn person 3 child identifier (fix across modules and waves) | `Str(14)` | `%14s` |
| `sn_childid_4` | Child link: sn person 4 child identifier (fix across modules and waves) | `Str(14)` | `%14s` |
| `sn_childid_5` | Child link: sn person 5 child identifier (fix across modules and waves) | `Str(14)` | `%14s` |
| `sn_childid_6` | Child link: sn person 6 child identifier (fix across modules and waves) | `Str(14)` | `%14s` |
| `sn_childid_7` | Child link: sn person 7 child identifier (fix across modules and waves) | `Str(14)` | `%14s` |

### `sp` - Social Support

- Dataset: `sharew8_rel9-0-0_sp.dta`
- Read with: `ps.read_share_module("sp", wave=8)`
- Rows: 53,695
- Variables: 174
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sp002_` | Received help from others (outside hh) | `Numeric(Byte)` | `%10.0g` |
| `sp003_1` | Who gave help: person 1 | `Numeric(Byte)` | `%60.0g` |
| `sp003_2` | Who gave help: person 2 | `Numeric(Byte)` | `%60.0g` |
| `sp003_3` | Who gave help: person 3 | `Numeric(Byte)` | `%60.0g` |
| `sp004d1_1` | Help provided from person 1: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp004d1_2` | Help provided from person 2: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp004d1_3` | Help provided from person 3: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp004d2_1` | Help provided from person 1: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp004d2_2` | Help provided from person 2: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp004d2_3` | Help provided from person 3: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp004d3_1` | Help provided from person 1: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp004d3_2` | Help provided from person 2: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp004d3_3` | Help provided from person 3: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp005_1` | How often received help: from person 1 | `Numeric(Byte)` | `%25.0g` |
| `sp005_2` | How often received help: from person 2 | `Numeric(Byte)` | `%25.0g` |
| `sp005_3` | How often received help: from person 3 | `Numeric(Byte)` | `%25.0g` |
| `sp007_1` | Any other helper from outside the household | `Numeric(Byte)` | `%10.0g` |
| `sp007_2` | Any other helper from outside the household | `Numeric(Byte)` | `%10.0g` |
| `sp007_3` | Any other helper from outside the household | `Numeric(Byte)` | `%10.0g` |
| `sp008_` | Given help last twelve months | `Numeric(Byte)` | `%10.0g` |
| `sp009_1` | To whom did you give help: person 1 | `Numeric(Byte)` | `%60.0g` |
| `sp009_2` | To whom did you give help: person 2 | `Numeric(Byte)` | `%60.0g` |
| `sp009_3` | To whom did you give help: person 3 | `Numeric(Byte)` | `%60.0g` |
| `sp010d1_1` | Help given person 1: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp010d1_2` | Help given person 2: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp010d1_3` | Help given person 3: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp010d2_1` | Help given person 1: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp010d2_2` | Help given person 2: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp010d2_3` | Help given person 3: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp010d3_1` | Help given person 1: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp010d3_2` | Help given person 2: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp010d3_3` | Help given person 3: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp011_1` | How often given help to person 1 | `Numeric(Byte)` | `%25.0g` |
| `sp011_2` | How often given help to person 2 | `Numeric(Byte)` | `%25.0g` |
| `sp011_3` | How often given help to person 3 | `Numeric(Byte)` | `%25.0g` |
| `sp013_1` | Have you given help to others | `Numeric(Byte)` | `%10.0g` |
| `sp013_2` | Have you given help to others | `Numeric(Byte)` | `%10.0g` |
| `sp013_3` | Have you given help to others | `Numeric(Byte)` | `%10.0g` |
| `sp014_` | Looked after grandchildren | `Numeric(Byte)` | `%10.0g` |
| `sp015d1` | Looked after child of child 1 | `Numeric(Byte)` | `%12.0g` |
| `sp015d2` | Looked after child of child 2 | `Numeric(Byte)` | `%12.0g` |
| `sp015d3` | Looked after child of child 3 | `Numeric(Byte)` | `%12.0g` |
| `sp015d4` | Looked after child of child 4 | `Numeric(Byte)` | `%12.0g` |
| `sp015d5` | Looked after child of child 5 | `Numeric(Byte)` | `%12.0g` |
| `sp015d6` | Looked after child of child 6 | `Numeric(Byte)` | `%12.0g` |
| `sp015d7` | Looked after child of child 7 | `Numeric(Byte)` | `%12.0g` |
| `sp015d8` | Looked after child of child 8 | `Numeric(Byte)` | `%12.0g` |
| `sp015d9` | Looked after child of child 9 | `Numeric(Byte)` | `%12.0g` |
| `sp015d10` | Looked after child of child 10 | `Numeric(Byte)` | `%12.0g` |
| `sp015d11` | Looked after child of child 11 | `Numeric(Byte)` | `%12.0g` |
| `sp015d12` | Looked after child of child 12 | `Numeric(Byte)` | `%12.0g` |
| `sp015d13` | Looked after child of child 13 | `Numeric(Byte)` | `%12.0g` |
| `sp015d14` | Looked after child of child 14 | `Numeric(Byte)` | `%12.0g` |
| `sp015d15` | Looked after child of child 15 | `Numeric(Byte)` | `%12.0g` |
| `sp015d16` | Looked after child of child 16 | `Numeric(Byte)` | `%12.0g` |
| `sp015d17` | Looked after child of child 17 | `Numeric(Byte)` | `%12.0g` |
| `sp015d18` | Looked after child of child 18 | `Numeric(Byte)` | `%12.0g` |
| `sp015d19` | Looked after child of child 19 | `Numeric(Byte)` | `%12.0g` |
| `sp015d20` | Looked after child of child 20 | `Numeric(Byte)` | `%12.0g` |
| `sp015d21` | Looked after child of deceased child | `Numeric(Byte)` | `%12.0g` |
| `sp016_1` | How often did you look after child of child 1 | `Numeric(Byte)` | `%25.0g` |
| `sp016_2` | How often did you look after child of child 2 | `Numeric(Byte)` | `%25.0g` |
| `sp016_3` | How often did you look after child of child 3 | `Numeric(Byte)` | `%25.0g` |
| `sp016_4` | How often did you look after child of child 4 | `Numeric(Byte)` | `%25.0g` |
| `sp016_5` | How often did you look after child of child 5 | `Numeric(Byte)` | `%25.0g` |
| `sp016_6` | How often did you look after child of child 6 | `Numeric(Byte)` | `%25.0g` |
| `sp016_7` | How often did you look after child of child 7 | `Numeric(Byte)` | `%25.0g` |
| `sp016_8` | How often did you look after child of child 8 | `Numeric(Byte)` | `%25.0g` |
| `sp016_9` | How often did you look after child of child 9 | `Numeric(Byte)` | `%25.0g` |
| `sp016_10` | How often did you look after child of child 10 | `Numeric(Byte)` | `%25.0g` |
| `sp016_11` | How often did you look after child of child 11 | `Numeric(Byte)` | `%25.0g` |
| `sp016_12` | How often did you look after child of child 12 | `Numeric(Byte)` | `%25.0g` |
| `sp016_13` | How often did you look after child of child 13 | `Numeric(Byte)` | `%25.0g` |
| `sp016_14` | How often did you look after child of child 14 | `Numeric(Byte)` | `%25.0g` |
| `sp016_15` | How often do you look after child of child 15 | `Numeric(Byte)` | `%25.0g` |
| `sp016_16` | How often do you look after child of child 16 | `Numeric(Byte)` | `%25.0g` |
| `sp016_17` | How often do you look after child of child 17 | `Numeric(Byte)` | `%25.0g` |
| `sp016_18` | How often do you look after child of child 18 | `Numeric(Byte)` | `%25.0g` |
| `sp016_19` | How often do you look after child of child 19 | `Numeric(Byte)` | `%25.0g` |
| `sp016_20` | How often do you look after child of child 20 | `Numeric(Byte)` | `%25.0g` |
| `sp018_` | Given help to someone with personal care in the household | `Numeric(Byte)` | `%10.0g` |
| `sp019d1` | R provided help with personal care to: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sp019d2` | R provided help with personal care to: mother | `Numeric(Byte)` | `%12.0g` |
| `sp019d3` | R provided help with personal care to: father | `Numeric(Byte)` | `%12.0g` |
| `sp019d4` | R provided help with personal care to: mother-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp019d5` | R provided help with personal care to: father-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp019d6` | R provided help with personal care to: stepmother | `Numeric(Byte)` | `%12.0g` |
| `sp019d7` | R provided help with personal care to: stepfather | `Numeric(Byte)` | `%12.0g` |
| `sp019d8` | R provided help with personal care to: brother | `Numeric(Byte)` | `%12.0g` |
| `sp019d9` | R provided help with personal care to: sister | `Numeric(Byte)` | `%12.0g` |
| `sp019d10` | R provided help with personal care to: child | `Numeric(Byte)` | `%12.0g` |
| `sp019d11` | R provided help with personal care to: step-child/current partner's child | `Numeric(Byte)` | `%12.0g` |
| `sp019d20` | R provided help with personal care to: son-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp019d21` | R provided help with personal care to: daughter-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp019d22` | R provided help with personal care to: grandchild | `Numeric(Byte)` | `%12.0g` |
| `sp019d23` | R provided help with personal care to: grandparent | `Numeric(Byte)` | `%12.0g` |
| `sp019d24` | R provided help with personal care to: aunt | `Numeric(Byte)` | `%12.0g` |
| `sp019d25` | R provided help with personal care to: uncle | `Numeric(Byte)` | `%12.0g` |
| `sp019d26` | R provided help with personal care to: niece | `Numeric(Byte)` | `%12.0g` |
| `sp019d27` | R provided help with personal care to: nephew | `Numeric(Byte)` | `%12.0g` |
| `sp019d28` | R provided help with personal care to: other relative | `Numeric(Byte)` | `%12.0g` |
| `sp019d29` | R provided help with personal care to: friend | `Numeric(Byte)` | `%12.0g` |
| `sp019d30` | R provided help with personal care to: (ex-)colleague | `Numeric(Byte)` | `%12.0g` |
| `sp019d31` | R provided help with personal care to: neighbour | `Numeric(Byte)` | `%12.0g` |
| `sp019d32` | R provided help with personal care to: ex-spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sp019d35` | R provided help with personal care to: minister, priest, other clergy | `Numeric(Byte)` | `%12.0g` |
| `sp019d36` | R provided help with personal care to: therapist/professional helper | `Numeric(Byte)` | `%12.0g` |
| `sp019d37` | R provided help with personal care to: housekeeper/home health care provider | `Numeric(Byte)` | `%12.0g` |
| `sp019dno` | R provided help with personal care to: none of these | `Numeric(Byte)` | `%12.0g` |
| `sp020_` | Someone in this household helped you regularly with personal care | `Numeric(Byte)` | `%10.0g` |
| `sp021d1` | R received help with personal care from: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sp021d2` | R received help with personal care from: mother | `Numeric(Byte)` | `%12.0g` |
| `sp021d3` | R received help with personal care from: father | `Numeric(Byte)` | `%12.0g` |
| `sp021d4` | R received help with personal care from: mother-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp021d5` | R received help with personal care from: father-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp021d6` | R received help with personal care from: stepmother | `Numeric(Byte)` | `%12.0g` |
| `sp021d7` | R received help with personal care from: stepfather | `Numeric(Byte)` | `%12.0g` |
| `sp021d8` | R received help with personal care from: brother | `Numeric(Byte)` | `%12.0g` |
| `sp021d9` | R received help with personal care from: sister | `Numeric(Byte)` | `%12.0g` |
| `sp021d10` | R received help with personal care from: child | `Numeric(Byte)` | `%12.0g` |
| `sp021d11` | R received help with personal care from: step-child/current partner's child | `Numeric(Byte)` | `%12.0g` |
| `sp021d20` | R received help with personal care from: son-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp021d21` | R received help with personal care from: daughter-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp021d22` | R received help with personal care from: grandchild | `Numeric(Byte)` | `%12.0g` |
| `sp021d23` | R received help with personal care from: grandparent | `Numeric(Byte)` | `%12.0g` |
| `sp021d24` | R received help with personal care from: aunt | `Numeric(Byte)` | `%12.0g` |
| `sp021d25` | R received help with personal care from: uncle | `Numeric(Byte)` | `%12.0g` |
| `sp021d26` | R received help with personal care from: niece | `Numeric(Byte)` | `%12.0g` |
| `sp021d27` | R received help with personal care from: nephew | `Numeric(Byte)` | `%12.0g` |
| `sp021d28` | R received help with personal care from: other relative | `Numeric(Byte)` | `%12.0g` |
| `sp021d29` | R received help with personal care from: friend | `Numeric(Byte)` | `%12.0g` |
| `sp021d30` | R received help with personal care from: (ex-)colleague | `Numeric(Byte)` | `%12.0g` |
| `sp021d31` | R received help with personal care from: neighbour | `Numeric(Byte)` | `%12.0g` |
| `sp021d32` | R received help with personal care from: ex-spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sp021d35` | R received help with personal care from: minister, priest, other clergy | `Numeric(Byte)` | `%12.0g` |
| `sp021d36` | R received help with personal care from: therapist/professional helper | `Numeric(Byte)` | `%12.0g` |
| `sp021d37` | R received help with personal care from: housekeeper/home health care provider | `Numeric(Byte)` | `%12.0g` |
| `sp021dno` | R received help with personal care from: none of these | `Numeric(Byte)` | `%12.0g` |
| `sp022_` | Who answered the questions in sp | `Numeric(Byte)` | `%47.0g` |
| `sp027_1` | From which child R received help | `Numeric(Byte)` | `%21.0g` |
| `sp027_2` | From which child R received help | `Numeric(Byte)` | `%21.0g` |
| `sp027_3` | From which child R received help | `Numeric(Byte)` | `%21.0g` |
| `sp028_1` | From which SN member R received help | `Numeric(Byte)` | `%23.0g` |
| `sp028_2` | From which SN member R received help | `Numeric(Byte)` | `%23.0g` |
| `sp028_3` | From which SN member R received help | `Numeric(Byte)` | `%23.0g` |
| `sp029_1` | To which child R gave help | `Numeric(Byte)` | `%21.0g` |
| `sp029_2` | To which child R gave help | `Numeric(Byte)` | `%21.0g` |
| `sp029_3` | To which child R gave help | `Numeric(Byte)` | `%21.0g` |
| `sp030_1` | To which SN member R gave help | `Numeric(Byte)` | `%23.0g` |
| `sp030_2` | To which SN member R gave help | `Numeric(Byte)` | `%23.0g` |
| `sp030_3` | To which SN member R gave help | `Numeric(Byte)` | `%23.0g` |
| `sp031_1` | To which child in household R gave help with personal care | `Numeric(Byte)` | `%21.0g` |
| `sp031_2` | To which child in household R gave help with personal care | `Numeric(Byte)` | `%21.0g` |
| `sp031_3` | To which child in household R gave help with personal care | `Numeric(Byte)` | `%21.0g` |
| `sp031_4` | To which child in household R gave help with personal care | `Numeric(Byte)` | `%21.0g` |
| `sp032_1` | To which SN member in household R gave help with personal care | `Numeric(Byte)` | `%23.0g` |
| `sp032_2` | To which SN member in household R gave help with personal care | `Numeric(Byte)` | `%23.0g` |
| `sp033_1` | From which child in household R received help with personal care | `Numeric(Byte)` | `%21.0g` |
| `sp033_2` | From which child in household R received help with personal care | `Numeric(Byte)` | `%21.0g` |
| `sp033_3` | From which child in household R received help with personal care | `Numeric(Byte)` | `%21.0g` |
| `sp033_4` | From which child in household R received help with personal care | `Numeric(Byte)` | `%21.0g` |
| `sp033_5` | From which child in household R received help with personal care | `Numeric(Byte)` | `%21.0g` |
| `sp033_6` | From which child in household R received help with personal care | `Numeric(Byte)` | `%21.0g` |
| `sp033_7` | From which child in household R received help with personal care | `Numeric(Byte)` | `%21.0g` |
| `sp034_1` | From which SN member in household R received help with personal care | `Numeric(Byte)` | `%23.0g` |
| `sp034_2` | From which SN member in household R received help with personal care | `Numeric(Byte)` | `%23.0g` |
| `sp034_3` | From which SN member in household R received help with personal care | `Numeric(Byte)` | `%23.0g` |
| `sp034_4` | From which SN member in household R received help with personal care | `Numeric(Byte)` | `%23.0g` |

### `sr` - Saving Regrets

- Dataset: `sharew8_rel9-0-0_sr.dta`
- Read with: `ps.read_share_module("sr", wave=8)`
- Rows: 53,695
- Variables: 58
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sr002d1` | Positive Shock: Salary or earnings were higher than expected | `Numeric(Byte)` | `%12.0g` |
| `sr002d2` | Positive Shock: SpouseÂ´s salary or earnings were higher than expected | `Numeric(Byte)` | `%12.0g` |
| `sr002d3` | Positive Shock: I retired later than expected | `Numeric(Byte)` | `%12.0g` |
| `sr002d4` | Positive Shock: Spouse retired later than expected | `Numeric(Byte)` | `%12.0g` |
| `sr002d5` | Positive Shock: Household spending was lower than expected | `Numeric(Byte)` | `%12.0g` |
| `sr002d6` | Positive Shock: My/our investments or business performed better than expected | `Numeric(Byte)` | `%12.0g` |
| `sr002d7` | Positive Shock: Received financial help from family | `Numeric(Byte)` | `%12.0g` |
| `sr002d8` | Positive Shock: Received an inheritance | `Numeric(Byte)` | `%12.0g` |
| `sr002d9` | Positive Shock: Pension benefits were higher than expected | `Numeric(Byte)` | `%12.0g` |
| `sr002dno` | Positive Shock: None of these | `Numeric(Byte)` | `%12.0g` |
| `sr002dot` | Positive Shock: Other | `Numeric(Byte)` | `%12.0g` |
| `sr004d1` | Negative Shock: Bad health affected work | `Numeric(Byte)` | `%12.0g` |
| `sr004d2` | Negative Shock: Large unexpected health expenses | `Numeric(Byte)` | `%12.0g` |
| `sr004d3` | Negative Shock: Unemployment | `Numeric(Byte)` | `%12.0g` |
| `sr004d4` | Negative Shock: Retired earlier than expected | `Numeric(Byte)` | `%12.0g` |
| `sr004d5` | Negative Shock: Salary or earnings were less than expected | `Numeric(Byte)` | `%12.0g` |
| `sr004d6` | Negative Shock: My/our investments or business performed worse than expected | `Numeric(Byte)` | `%12.0g` |
| `sr004d7` | Negative Shock: Needed to provide financial help to family members | `Numeric(Byte)` | `%12.0g` |
| `sr004d8` | Negative Shock: Divorce or separation | `Numeric(Byte)` | `%12.0g` |
| `sr004d9` | Negative Shock: Death in the family | `Numeric(Byte)` | `%12.0g` |
| `sr004d10` | Negative Shock: Large expenses other than health expenses | `Numeric(Byte)` | `%12.0g` |
| `sr004d11` | Negative Shock: Pension benefits were lower than expected | `Numeric(Byte)` | `%12.0g` |
| `sr004dno` | Negative Shock: None of these | `Numeric(Byte)` | `%12.0g` |
| `sr004dot` | Negative Shock: Other | `Numeric(Byte)` | `%12.0g` |
| `sr006_` | Hindsight Saving 1: Suppose you could re-do your spending and saving | `Numeric(Byte)` | `%29.0g` |
| `sr007_` | Hindsight Saving 2: Suppose you could re-do your spending and saving | `Numeric(Byte)` | `%44.0g` |
| `sr008_` | How strongly do you wish you could redo your spending and saving? | `Numeric(Byte)` | `%25.0g` |
| `sr009d1` | Where spend less: Housing | `Numeric(Byte)` | `%12.0g` |
| `sr009d2` | Where spend less: Food | `Numeric(Byte)` | `%12.0g` |
| `sr009d3` | Where spend less: Clothing | `Numeric(Byte)` | `%12.0g` |
| `sr009d4` | Where spend less: Appliances and home furnishings | `Numeric(Byte)` | `%12.0g` |
| `sr009d5` | Where spend less: Car | `Numeric(Byte)` | `%12.0g` |
| `sr009d6` | Where spend less: Vacation | `Numeric(Byte)` | `%12.0g` |
| `sr009d7` | Where spend less: Leisure | `Numeric(Byte)` | `%12.0g` |
| `sr009d8` | Where spend less: Childrenâ€™s education or other child-related expenses | `Numeric(Byte)` | `%12.0g` |
| `sr009d9` | Where spend less: Providing financial help | `Numeric(Byte)` | `%12.0g` |
| `sr009d10` | Where spend less: I/we would have worked more or longer | `Numeric(Byte)` | `%12.0g` |
| `sr009dno` | Where spend less: No way I/we could have cut spending | `Numeric(Byte)` | `%12.0g` |
| `sr009dot` | Where spend less: Other | `Numeric(Byte)` | `%12.0g` |
| `sr011d1` | Where spend more: Housing | `Numeric(Byte)` | `%12.0g` |
| `sr011d2` | Where spend more: Food | `Numeric(Byte)` | `%12.0g` |
| `sr011d3` | Where spend more: Clothing | `Numeric(Byte)` | `%12.0g` |
| `sr011d4` | Where spend more: Appliances and home furnishings | `Numeric(Byte)` | `%12.0g` |
| `sr011d5` | Where spend more: Car | `Numeric(Byte)` | `%12.0g` |
| `sr011d6` | Where spend more: Vacation | `Numeric(Byte)` | `%12.0g` |
| `sr011d7` | Where spend more: Leisure | `Numeric(Byte)` | `%12.0g` |
| `sr011d8` | Where spend more: Childrenâ€™s education or other child-related expenses | `Numeric(Byte)` | `%12.0g` |
| `sr011d9` | Where spend more: Providing financial help | `Numeric(Byte)` | `%12.0g` |
| `sr011d10` | Where spend more: I/we would have worked less or retired earlier | `Numeric(Byte)` | `%12.0g` |
| `sr011dno` | Where spend more: I/we would not really have wanted to spend more | `Numeric(Byte)` | `%12.0g` |
| `sr011dot` | Where spend more: Other | `Numeric(Byte)` | `%12.0g` |
| `sr013_` | Who answered the questions sr | `Numeric(Byte)` | `%62.0g` |

### `te` - Time Expenditure

- Dataset: `sharew8_rel9-0-0_te.dta`
- Read with: `ps.read_share_module("te", wave=8)`
- Rows: 53,695
- Variables: 40
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `te002_` | What day was yesterday? | `Numeric(Byte)` | `%13.0g` |
| `te003_` | Was yesterday a normal day for you? | `Numeric(Byte)` | `%70.0g` |
| `te005_` | Hours spent on chores | `Numeric(Byte)` | `%10.0g` |
| `te006_` | Minutes spent on chores | `Numeric(Byte)` | `%10.0g` |
| `te011_` | Hours spent on personal care | `Numeric(Byte)` | `%10.0g` |
| `te012_` | Minutes spent on personal care | `Numeric(Byte)` | `%10.0g` |
| `te014_` | Hours spent on children | `Numeric(Byte)` | `%10.0g` |
| `te015_` | Minutes spent on children | `Numeric(Byte)` | `%10.0g` |
| `te017_` | Hours spent on helping parents | `Numeric(Byte)` | `%10.0g` |
| `te018_` | Minutes spent on helping parents | `Numeric(Byte)` | `%10.0g` |
| `te020_` | Hours spent on helping partner | `Numeric(Byte)` | `%10.0g` |
| `te021_` | Minutes spent on helping partner | `Numeric(Byte)` | `%10.0g` |
| `te023_` | Hours spent on helping other family members or other people | `Numeric(Byte)` | `%10.0g` |
| `te024_` | Minutes spent on helping other family members or other people | `Numeric(Byte)` | `%10.0g` |
| `te026_` | Hours spent on leisure time activities | `Numeric(Byte)` | `%10.0g` |
| `te027_` | Minutes spent on leisure time activities | `Numeric(Byte)` | `%10.0g` |
| `te032_` | Hours spent on administrative chores and own family finances | `Numeric(Byte)` | `%10.0g` |
| `te033_` | Minutes spent on administrative chores and own family finances | `Numeric(Byte)` | `%10.0g` |
| `te035_` | Hours spent on paid work | `Numeric(Byte)` | `%10.0g` |
| `te036_` | Minutes spent on paid work | `Numeric(Byte)` | `%10.0g` |
| `te038_` | Hours spent on voluntary work | `Numeric(Byte)` | `%10.0g` |
| `te039_` | Minutes spent on voluntary work | `Numeric(Byte)` | `%10.0g` |
| `te041_` | Hours spent on traveling to and from work | `Numeric(Byte)` | `%10.0g` |
| `te042_` | Minutes spent on traveling to and from work | `Numeric(Byte)` | `%10.0g` |
| `te047_` | Hours spent on napping and resting during daytime | `Numeric(Byte)` | `%10.0g` |
| `te048_` | Minutes spent on napping and resting during daytime | `Numeric(Byte)` | `%10.0g` |
| `te050_` | Hours spent on sleeping at night time | `Numeric(Byte)` | `%10.0g` |
| `te051_` | Minutes spent on sleeping at night time | `Numeric(Byte)` | `%10.0g` |
| `te052_` | Did you spend time yesterday on other activities | `Numeric(Byte)` | `%10.0g` |
| `te055_` | Hours spent on other activity | `Numeric(Byte)` | `%10.0g` |
| `te056_` | Minutes spent on other activity | `Numeric(Byte)` | `%10.0g` |
| `te058_` | Hours spent on leisure time activities with partner | `Numeric(Byte)` | `%10.0g` |
| `te059_` | Minutes spent on leisure time activities with partner | `Numeric(Byte)` | `%10.0g` |
| `te060_` | Who answered the questions in te | `Numeric(Byte)` | `%47.0g` |

### `xt` - End-of-Life Interview

- Dataset: `sharew8_rel9-0-0_xt.dta`
- Read with: `ps.read_share_module("xt", wave=8)`
- Rows: 4,175
- Variables: 202
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language_xt` | Language: End of life interview | `Numeric(Byte)` | `%44.0g` |
| `gender_xt` | Gender of the deceased | `Numeric(Byte)` | `%10.0g` |
| `yrbirth_xt` | Year of birth of the deceased | `Numeric(Int)` | `%10.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `xt002_` | Relationship to the deceased | `Numeric(Byte)` | `%53.0g` |
| `xt005_` | How often contact last twelve month | `Numeric(Byte)` | `%30.0g` |
| `xt006_` | Proxy respondent's sex | `Numeric(Byte)` | `%12.0g` |
| `xt007_` | Year of birth proxy | `Numeric(Int)` | `%10.0g` |
| `xt008_` | Month of decease | `Numeric(Byte)` | `%12.0g` |
| `xt009_` | Year of decease | `Numeric(Int)` | `%10.0g` |
| `xt010_` | Age at the moment of decease | `Numeric(Int)` | `%10.0g` |
| `xt011_` | Main cause of death | `Numeric(Byte)` | `%106.0g` |
| `xt012c` | Main cause of death: xt012 coded | `Numeric(Byte)` | `%60.0g` |
| `xt013_` | How long been ill before decease | `Numeric(Byte)` | `%72.0g` |
| `xt014_` | Place of dying | `Numeric(Byte)` | `%74.0g` |
| `xt016_` | Total time in hospital last year before dying | `Numeric(Byte)` | `%56.0g` |
| `xt018_1` | Type of medical care in last 12 months: care from a general practitioner | `Numeric(Byte)` | `%10.0g` |
| `xt018_2` | Type of medical care in last 12 months: care from specialist physicians | `Numeric(Byte)` | `%10.0g` |
| `xt018_3` | Type of medical care in last 12 months: hospital stays | `Numeric(Byte)` | `%10.0g` |
| `xt018_4` | Type of medical care in last 12 months: care in a nursing home | `Numeric(Byte)` | `%10.0g` |
| `xt018_5` | Type of medical care in last 12 months: hospice stays | `Numeric(Byte)` | `%10.0g` |
| `xt018_6` | Type of medical care in last 12 months: medication | `Numeric(Byte)` | `%10.0g` |
| `xt018_7` | Type of medical care in last 12 months: aids and appliances | `Numeric(Byte)` | `%10.0g` |
| `xt018_8` | Type of medical care last 12 months: help with personal care due to disability | `Numeric(Byte)` | `%10.0g` |
| `xt018_9` | Type of medical care last 12 months: help with domestic tasks due to disability | `Numeric(Byte)` | `%10.0g` |
| `xt020d1` | Difficulties doing activities: dressing, including putting on shoes and socks | `Numeric(Byte)` | `%12.0g` |
| `xt020d2` | Difficulties doing activities: walking across a room | `Numeric(Byte)` | `%12.0g` |
| `xt020d3` | Difficulties doing activities: bathing or showering | `Numeric(Byte)` | `%12.0g` |
| `xt020d4` | Difficulties doing activities: eating, such as cutting up your food | `Numeric(Byte)` | `%12.0g` |
| `xt020d5` | Difficulties doing activities: getting in or out of bed | `Numeric(Byte)` | `%12.0g` |
| `xt020d6` | Difficulties doing activities: using the toilet, including getting up or down | `Numeric(Byte)` | `%12.0g` |
| `xt020dno` | Difficulties doing activities: none of these | `Numeric(Byte)` | `%12.0g` |
| `xt022_` | Anyone helped with ADL | `Numeric(Byte)` | `%10.0g` |
| `xt023d1` | Who has helped with ADL: yourself (proxy respondent) | `Numeric(Byte)` | `%12.0g` |
| `xt023d2` | Who has helped with ADL: spouse/partner of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt023d3` | Who has helped with ADL: mother/father of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt023d4` | Who has helped with ADL: son of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt023d5` | Who has helped with ADL: son-in-law of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt023d6` | Who has helped with ADL: daughter of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt023d7` | Who has helped with ADL: daughter-in-law of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt023d8` | Who has helped with ADL: grandson of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt023d9` | Who has helped with ADL: granddaughter of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt023d10` | Who has helped with ADL: sister of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt023d11` | Who has helped with ADL: brother of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt023d12` | Who has helped with ADL: other relative | `Numeric(Byte)` | `%12.0g` |
| `xt023d13` | Who has helped with ADL: unpaid volunteer | `Numeric(Byte)` | `%12.0g` |
| `xt023d14` | Who has helped with ADL: professional helper | `Numeric(Byte)` | `%12.0g` |
| `xt023d15` | Who has helped with ADL: friend/neighbor of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt023dot` | Who has helped with ADL: other person | `Numeric(Byte)` | `%12.0g` |
| `xt024_` | Time the deceased received help | `Numeric(Byte)` | `%54.0g` |
| `xt025_` | Hours of help necessary during typical day | `Numeric(Byte)` | `%10.0g` |
| `xt026_` | The deceased had a will | `Numeric(Byte)` | `%10.0g` |
| `xt027d1` | Beneficiaries of the estate: yourself (proxy) | `Numeric(Byte)` | `%12.0g` |
| `xt027d2` | Beneficiaries of the estate: spouse/partner of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt027d3` | Beneficiaries of the estate: children of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt027d4` | Beneficiaries of the estate: grandchildren of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt027d5` | Beneficiaries of the estate: siblings of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt027d6` | Beneficiaries of the estate: other relatives of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt027d7` | Beneficiaries of the estate: other non-relatives | `Numeric(Byte)` | `%12.0g` |
| `xt027d8` | Beneficiaries of the estate: church, foundation or charitable organization | `Numeric(Byte)` | `%12.0g` |
| `xt027d9` | Beneficiaries of the estate: deceased did not leave anything at all (SPONTANEOUS | `Numeric(Byte)` | `%12.0g` |
| `xt027d10` | Beneficiaries of the estate: not decided yet (SPONTANEOUS) | `Numeric(Byte)` | `%12.0g` |
| `xt030_` | The deceased owned home | `Numeric(Byte)` | `%10.0g` |
| `xt031e` | Value of home after mortgages | `Numeric(Float)` | `%10.0g` |
| `xt031ub` | Values home after mortgages ub | `Numeric(Byte)` | `%32.0g` |
| `xt031v1` | Bracket value 1 | `Numeric(Double)` | `%12.0g` |
| `xt031v2` | Bracket value 2 | `Numeric(Double)` | `%12.0g` |
| `xt031v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `xt032d1` | Who inherited the home of the deceased: yourself (proxy) | `Numeric(Byte)` | `%12.0g` |
| `xt032d2` | Who inherited the home of the deceased: spouse/partner of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt032d3` | Who inherited the home of the deceased: sons/daughters | `Numeric(Byte)` | `%12.0g` |
| `xt032d4` | Who inherited the home of the deceased: grandchildren of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt032d5` | Who inherited the home of the deceased: siblings of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt032d6` | Who inherited the home of the deceased: other relatives | `Numeric(Byte)` | `%12.0g` |
| `xt032d7` | Who inherited the home of the deceased: other non-relatives | `Numeric(Byte)` | `%12.0g` |
| `xt033_` | Deceased owned any life insurance policies | `Numeric(Byte)` | `%10.0g` |
| `xt034e` | Value of all life insurance policies | `Numeric(Float)` | `%10.0g` |
| `xt035d1` | Beneficiaries of the life insurance policies: yourself (proxy) | `Numeric(Byte)` | `%12.0g` |
| `xt035d2` | Beneficiaries of the life insurance policies: spouse/partner of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt035d3` | Beneficiaries of the life insurance policies: sons/daughters | `Numeric(Byte)` | `%12.0g` |
| `xt035d4` | Beneficiaries of the life insurance policies: grandchildren of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt035d5` | Beneficiaries of the life insurance policies: siblings of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt035d6` | Beneficiaries of the life insurance policies: other relatives | `Numeric(Byte)` | `%12.0g` |
| `xt035d7` | Beneficiaries of the life insurance policies: other non-relatives | `Numeric(Byte)` | `%12.0g` |
| `xt039_` | Number of children (still alive) deceased had at the end | `Numeric(Byte)` | `%10.0g` |
| `xt040a_` | Estate divided among children | `Numeric(Byte)` | `%70.0g` |
| `xt040b_` | Some children received more to make up for previous gifts | `Numeric(Byte)` | `%10.0g` |
| `xt040c_` | Some children received more to give them financial support | `Numeric(Byte)` | `%10.0g` |
| `xt040d_` | Some children received more because they helped/cared for deceased | `Numeric(Byte)` | `%10.0g` |
| `xt040e_` | Some children received more because of other reasons | `Numeric(Byte)` | `%10.0g` |
| `xt041_` | Funeral was accompanied by a religious ceremony | `Numeric(Byte)` | `%10.0g` |
| `xt043_` | Interview mode | `Numeric(Byte)` | `%26.0g` |
| `xt105_` | Difficulties remembering where he/she was | `Numeric(Byte)` | `%10.0g` |
| `xt106_` | Difficulties remembering the year | `Numeric(Byte)` | `%10.0g` |
| `xt107_` | Difficulties recognizing | `Numeric(Byte)` | `%10.0g` |
| `xt109_` | Deceased married at time of death | `Numeric(Byte)` | `%10.0g` |
| `xt119e_1` | Costs: care from a general practitioner | `Numeric(Float)` | `%10.0g` |
| `xt119e_2` | Costs: care from specialist physicians | `Numeric(Float)` | `%10.0g` |
| `xt119e_3` | Costs: hospital stays | `Numeric(Float)` | `%10.0g` |
| `xt119e_4` | Costs: care in a nursing home | `Numeric(Float)` | `%10.0g` |
| `xt119e_5` | Costs: hospice stays | `Numeric(Float)` | `%10.0g` |
| `xt119e_6` | Costs: medication | `Numeric(Float)` | `%10.0g` |
| `xt119e_7` | Costs: aids and appliances | `Numeric(Float)` | `%10.0g` |
| `xt119e_8` | Costs: help with personal care due to disability | `Numeric(Float)` | `%10.0g` |
| `xt119e_9` | Costs: help with domestic tasks due to disability | `Numeric(Float)` | `%10.0g` |
| `xt119ub_1` | Costs: care from a general practitioner ub | `Numeric(Byte)` | `%32.0g` |
| `xt119ub_2` | Costs: care from specialist physicians ub | `Numeric(Byte)` | `%32.0g` |
| `xt119ub_3` | Costs: hospital stays ub | `Numeric(Byte)` | `%32.0g` |
| `xt119ub_4` | Costs: care in a nursing home ub | `Numeric(Byte)` | `%32.0g` |
| `xt119ub_5` | Costs: hospice stays ub | `Numeric(Byte)` | `%32.0g` |
| `xt119ub_6` | Costs: medication ub | `Numeric(Byte)` | `%32.0g` |
| `xt119ub_7` | Costs: aids and appliances ub | `Numeric(Byte)` | `%32.0g` |
| `xt119ub_8` | Costs: help with personal care due to disability ub | `Numeric(Byte)` | `%32.0g` |
| `xt119ub_9` | Costs: help with domestic tasks due to disability ub | `Numeric(Byte)` | `%32.0g` |
| `xt119v1_1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `xt119v1_2` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `xt119v1_3` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `xt119v1_4` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt119v1_5` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `xt119v1_6` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `xt119v1_7` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `xt119v1_8` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt119v1_9` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `xt119v2_1` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `xt119v2_2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt119v2_3` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt119v2_4` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt119v2_5` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `xt119v2_6` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt119v2_7` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `xt119v2_8` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt119v2_9` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt119v3_1` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt119v3_2` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt119v3_3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt119v3_4` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt119v3_5` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `xt119v3_6` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt119v3_7` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `xt119v3_8` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt119v3_9` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt615_` | Times in hospital last year before dying | `Numeric(Int)` | `%10.0g` |
| `xt620d1` | Difficulties doing activities II: preparing a hot meal | `Numeric(Byte)` | `%12.0g` |
| `xt620d2` | Difficulties doing activities II: shopping for groceries | `Numeric(Byte)` | `%12.0g` |
| `xt620d3` | Difficulties doing activities II: making telephone calls | `Numeric(Byte)` | `%12.0g` |
| `xt620d4` | Difficulties doing activities II: taking medication | `Numeric(Byte)` | `%12.0g` |
| `xt620d5` | Difficulties doing activities II: using a map | `Numeric(Byte)` | `%12.0g` |
| `xt620d6` | Difficulties doing activities II: doing work around the house/garden | `Numeric(Byte)` | `%12.0g` |
| `xt620d7` | Difficulties doing activities II: managing money | `Numeric(Byte)` | `%12.0g` |
| `xt620d8` | Difficulties doing activities II: leaving the house independently | `Numeric(Byte)` | `%12.0g` |
| `xt620d9` | Difficulties doing activities II: doing personal laundry | `Numeric(Byte)` | `%12.0g` |
| `xt620d10` | Difficulties doing activities II: continence over urination/defecation | `Numeric(Byte)` | `%12.0g` |
| `xt620dno` | Difficulties doing activities II: none of these | `Numeric(Byte)` | `%12.0g` |
| `xt637_1` | Deceased owned assets: business, including land or permises | `Numeric(Byte)` | `%10.0g` |
| `xt637_2` | Deceased owned assets: other real estate | `Numeric(Byte)` | `%10.0g` |
| `xt637_3` | Deceased owned assets: cars | `Numeric(Byte)` | `%10.0g` |
| `xt637_4` | Deceased owned assets: financial assets, e.g. cash/bonds/stocks | `Numeric(Byte)` | `%10.0g` |
| `xt637_5` | Deceased owned assets: jewelry or antiquities | `Numeric(Byte)` | `%10.0g` |
| `xt638e_1` | Value of assets: business, including land or permises | `Numeric(Float)` | `%10.0g` |
| `xt638e_2` | Value of assets: other real estate | `Numeric(Float)` | `%10.0g` |
| `xt638e_3` | Value of assets: cars | `Numeric(Float)` | `%10.0g` |
| `xt638e_4` | Value of assets: financial assets, e.g. cash, bonds or stocks | `Numeric(Float)` | `%10.0g` |
| `xt638e_5` | Value of assets: jewelry or antiquities | `Numeric(Float)` | `%10.0g` |
| `xt638ub_1` | Value of assets: business, including land or permises ub | `Numeric(Byte)` | `%32.0g` |
| `xt638ub_2` | Value of assets: other real estate ub | `Numeric(Byte)` | `%32.0g` |
| `xt638ub_3` | Value of assets: cars ub | `Numeric(Byte)` | `%32.0g` |
| `xt638ub_4` | Value of assets: financial assets, e.g. cash, bonds or stocks ub | `Numeric(Byte)` | `%32.0g` |
| `xt638ub_5` | Value of assets: jewelry or antiquities ub | `Numeric(Byte)` | `%32.0g` |
| `xt638v1_1` | Bracket value 1 | `Numeric(Double)` | `%12.0g` |
| `xt638v1_2` | Bracket value 1 | `Numeric(Double)` | `%12.0g` |
| `xt638v1_3` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt638v1_4` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt638v1_5` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt638v2_1` | Bracket value 2 | `Numeric(Double)` | `%12.0g` |
| `xt638v2_2` | Bracket value 2 | `Numeric(Double)` | `%12.0g` |
| `xt638v2_3` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt638v2_4` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt638v2_5` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt638v3_1` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `xt638v3_2` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `xt638v3_3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt638v3_4` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt638v3_5` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt750_` | Intensive care unit | `Numeric(Byte)` | `%10.0g` |
| `xt751_` | Palliative care or inpatient hospice unit | `Numeric(Byte)` | `%10.0g` |
| `xt752_` | Inpatient hospice unit | `Numeric(Byte)` | `%10.0g` |
| `xt753_` | Residential provided by hospice | `Numeric(Byte)` | `%10.0g` |
| `xt754_` | Reason no hospice or palliative care | `Numeric(Byte)` | `%60.0g` |
| `xt757_` | Hospice or palliative care | `Numeric(Byte)` | `%10.0g` |
| `xt758_` | Take medicine for pain | `Numeric(Byte)` | `%10.0g` |
| `xt759_` | Medication amount | `Numeric(Byte)` | `%16.0g` |
| `xt760_` | Trouble breathing | `Numeric(Byte)` | `%10.0g` |
| `xt761_` | How much help breathing | `Numeric(Byte)` | `%13.0g` |
| `xt762_` | Feelings of anxiety or sadness | `Numeric(Byte)` | `%10.0g` |
| `xt763_` | How much help with anxiety or sadness | `Numeric(Byte)` | `%13.0g` |
| `xt764_` | How often personal care needs met | `Numeric(Byte)` | `%73.0g` |
| `xt765_` | How often was staff caring and respectful | `Numeric(Byte)` | `%72.0g` |
| `xt766_` | Rate care | `Numeric(Byte)` | `%16.0g` |
| `xt767_` | Certified nurse | `Numeric(Byte)` | `%10.0g` |


## Special Modules

### `ax` - Accelerometry

- Dataset: `sharew8_rel9-0-0_ax.dta`
- Read with: `ps.read_share_module("ax", wave=8)`
- Rows: 53,695
- Variables: 16
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ax002_` | Willingness to participate in Accelerometry study | `Numeric(Byte)` | `%10.0g` |
| `ax003_` | Reasons why R does not participate in Accelerometry study | `Numeric(Byte)` | `%68.0g` |
| `ax004c` | Reasons why R does not participate in Accelerometry study: xt004 coded | `Numeric(Byte)` | `%27.0g` |
| `ax007_` | Refusal conversion: not active | `Numeric(Byte)` | `%10.0g` |
| `ax008_` | Refusal conversion: too old | `Numeric(Byte)` | `%10.0g` |
| `ax009_` | Refusal conversion: work or hobby | `Numeric(Byte)` | `%10.0g` |
| `ax010_` | Refusal conversion: absence | `Numeric(Byte)` | `%10.0g` |
| `ax011_` | Refusal conversion: burden | `Numeric(Byte)` | `%10.0g` |
| `ax012_` | Refusal conversion: privacy | `Numeric(Byte)` | `%10.0g` |
| `ax013_` | Refusal conversion: skin | `Numeric(Byte)` | `%10.0g` |

### `dropoff` - Paper-and-pencil drop-off

- Dataset: `sharew8_rel9-0-0_dropoff.dta`
- Read with: `ps.read_share_module("dropoff", wave=8)`
- Rows: 34,873
- Variables: 860
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `yrbirth_do` | Year of birth | `Numeric(Int)` | `%10.0g` |
| `gender_do` | Gender | `Numeric(Byte)` | `%27.0g` |
| `int_year_do` | Dropoff interview year | `Numeric(Int)` | `%33.0g` |
| `int_month_do` | Dropoff interview month | `Numeric(Byte)` | `%33.0g` |
| `at_f1` | Witness Cases of dementia | `Numeric(Byte)` | `%65.0g` |
| `at_f2` | Feel sufficiently informed about dementia | `Numeric(Byte)` | `%50.0g` |
| `at_f3_1` | Informed about dementia: GP | `Numeric(Byte)` | `%14.0g` |
| `at_f3_2` | Informed about dementia: Doctor for neurology, psychiatry, psychotherapist | `Numeric(Byte)` | `%14.0g` |
| `at_f3_3` | Informed about dementia: Psychologist | `Numeric(Byte)` | `%14.0g` |
| `at_f3_4` | Informed about dementia: Hospital | `Numeric(Byte)` | `%14.0g` |
| `at_f3_5` | Informed about dementia: Support group | `Numeric(Byte)` | `%14.0g` |
| `at_f3_6` | Informed about dementia: Municipality (events, leaflets, etc.) | `Numeric(Byte)` | `%14.0g` |
| `at_f3_7` | Informed about dementia: Social services | `Numeric(Byte)` | `%14.0g` |
| `at_f3_8` | Informed about dementia: The media (journals, tv, internet, etc.) | `Numeric(Byte)` | `%14.0g` |
| `at_f3_9` | Informed about dementia: Relatives, friends, etc. | `Numeric(Byte)` | `%14.0g` |
| `at_f4_1` | Additional info on dementia: from GP | `Numeric(Byte)` | `%14.0g` |
| `at_f4_2` | Additional info on dementia: doctor for neurology, psychiatry, psychotherapist | `Numeric(Byte)` | `%14.0g` |
| `at_f4_3` | Additional info on dementia: psychologist | `Numeric(Byte)` | `%14.0g` |
| `at_f4_4` | Additional info on dementia: hospital | `Numeric(Byte)` | `%14.0g` |
| `at_f4_5` | Additional info on dementia: support group | `Numeric(Byte)` | `%14.0g` |
| `at_f4_6` | Additional info on dementia: municipality (events, leaflets, etc.) | `Numeric(Byte)` | `%14.0g` |
| `at_f4_7` | Additional info on dementia: social services | `Numeric(Byte)` | `%14.0g` |
| `at_f4_8` | Additional info on dementia: media (journals, tv, internet, etc.) | `Numeric(Byte)` | `%14.0g` |
| `at_f4_9` | Additional info on dementia: relatives, friends, etc. | `Numeric(Byte)` | `%14.0g` |
| `at_f5` | Institutions respond to needs of people w/dementia | `Numeric(Byte)` | `%96.0g` |
| `at_f6` | Feel sufficiently informed about care options | `Numeric(Byte)` | `%36.0g` |
| `at_f7_1` | Learn more about care: Nursing allowance | `Numeric(Byte)` | `%14.0g` |
| `at_f7_2` | Learn more about care: Mobile Social Services | `Numeric(Byte)` | `%14.0g` |
| `at_f7_3` | Learn more about care: 24h-care | `Numeric(Byte)` | `%14.0g` |
| `at_f7_4` | Learn more about care: Care homes, residences | `Numeric(Byte)` | `%14.0g` |
| `at_f7_5` | Learn more about care: Dementia | `Numeric(Byte)` | `%14.0g` |
| `at_f7_6` | Learn more about care: Access to medical aids | `Numeric(Byte)` | `%14.0g` |
| `at_f7_7` | Learn more about care: Barrier-free living | `Numeric(Byte)` | `%14.0g` |
| `at_f7_8` | Learn more about care: Consultancy options | `Numeric(Byte)` | `%14.0g` |
| `at_f7_9` | Learn more about care: Support groups / regularâ€™s tables | `Numeric(Byte)` | `%14.0g` |
| `at_f7_10` | Learn more about care: Courses for nursing relatives | `Numeric(Byte)` | `%14.0g` |
| `at_f7_11` | Learn more about care: Practical care advice | `Numeric(Byte)` | `%14.0g` |
| `at_f8_1` | More or better info on care: GP | `Numeric(Byte)` | `%14.0g` |
| `at_f8_2` | More or better info on care: local services institutions | `Numeric(Byte)` | `%14.0g` |
| `at_f8_3` | More or better info on care: by postal mail | `Numeric(Byte)` | `%14.0g` |
| `at_f8_4` | More or better info on care: municipality | `Numeric(Byte)` | `%14.0g` |
| `at_f8_5` | More or better info on care: journals, media | `Numeric(Byte)` | `%14.0g` |
| `at_f8_6` | More or better info on care: family, friends, relatives | `Numeric(Byte)` | `%14.0g` |
| `at_f9a` | Climate change: number of extra hot days | `Numeric(Byte)` | `%28.0g` |
| `at_f9b` | Climate change: number and duration of droughts over the year | `Numeric(Byte)` | `%28.0g` |
| `at_f9c` | Climate change: number of days with a full snow blanket in winter | `Numeric(Byte)` | `%28.0g` |
| `at_f9d` | Climate change: number and intensity of storms and strong winds | `Numeric(Byte)` | `%28.0g` |
| `at_f9e` | Climate change: number and intensity of strong rains and floods | `Numeric(Byte)` | `%28.0g` |
| `at_f9f` | Climate change: average temperature over the year | `Numeric(Byte)` | `%28.0g` |
| `at_f9g` | Climate change: extreme weather events in general | `Numeric(Byte)` | `%28.0g` |
| `at_f10a` | We have the right to reshape nature according to our needs | `Numeric(Byte)` | `%20.0g` |
| `at_f10b` | Plants and animals are existing mostly to be utilised by humans | `Numeric(Byte)` | `%20.0g` |
| `at_f10c` | Animals should have similar rights to live as we do | `Numeric(Byte)` | `%20.0g` |
| `at_f10d` | Austria needs economical growth to be able to protect the environment | `Numeric(Byte)` | `%20.0g` |
| `at_f10e` | There are limits to growth that the industrial world has surpassed/will surpass | `Numeric(Byte)` | `%20.0g` |
| `at_f10f` | Science/technology will solve environmental problems: no changes in way of life | `Numeric(Byte)` | `%20.0g` |
| `at_f10g` | We trust too much in science and technology and too little in what we feel | `Numeric(Byte)` | `%20.0g` |
| `at_f10h` | Most of the things created by science/technology are harmful for environment | `Numeric(Byte)` | `%20.0g` |
| `at_f10i` | Disturbing to think of environmental conditions our (grand-)children live in | `Numeric(Byte)` | `%20.0g` |
| `at_f10j` | Reading newspaper or watching TV on environmental problems I feel outraged | `Numeric(Byte)` | `%20.0g` |
| `at_f10k` | If we keep going on like this we are heading for an environmental disaster | `Numeric(Byte)` | `%20.0g` |
| `at_f11a` | Raise taxes on fossil fuels | `Numeric(Byte)` | `%20.0g` |
| `at_f11b` | Supply our energy by nuclear power | `Numeric(Byte)` | `%20.0g` |
| `at_f11c` | Use public funds to finance renewable energy | `Numeric(Byte)` | `%20.0g` |
| `at_f11d` | Raise price of electricity to reduce consumption | `Numeric(Byte)` | `%20.0g` |
| `at_f11e` | Use public funds to finance thermal insulation of housing | `Numeric(Byte)` | `%20.0g` |
| `at_f11f` | Ban on selling white goods that not energy efficient | `Numeric(Byte)` | `%20.0g` |
| `at_f11g` | Use public funds to prepare AT for effects of climate change | `Numeric(Byte)` | `%20.0g` |
| `at_f11h` | Provide funds to developing countries to respond to extreme weather events | `Numeric(Byte)` | `%20.0g` |
| `be_fr_q1` | Percentage of population 65+ | `Numeric(Byte)` | `%12.0g` |
| `be_fr_q2` | Risk of being poor | `Numeric(Byte)` | `%55.0g` |
| `be_fr_q3` | Statutory retirement age (comparable person): old-age pension without penalty | `Numeric(Byte)` | `%12.0g` |
| `be_fr_q4` | Postponed (retired) or will postpone (working) retirement due to pension reform | `Numeric(Byte)` | `%12.0g` |
| `be_fr_q5` | If yes(q4), by how long | `Numeric(Byte)` | `%12.0g` |
| `be_fr_q5a_months` | Number of months | `Numeric(Byte)` | `%12.0g` |
| `be_fr_q5b_years` | Number of years | `Numeric(Byte)` | `%12.0g` |
| `be_fr_q6` | Percentage of GDP going into public pension payments | `Numeric(Byte)` | `%13.0g` |
| `be_fr_q7` | Main funding source for paying public pension in this country | `Numeric(Byte)` | `%36.0g` |
| `be_fr_q8a` | Allocate fewer resources to pensions and more to help unemployed | `Numeric(Byte)` | `%21.0g` |
| `be_fr_q8b` | Population aging makes the public pension system unsustainable | `Numeric(Byte)` | `%21.0g` |
| `be_fr_q8c` | Low growth and low contributions by young threaten pension system | `Numeric(Byte)` | `%21.0g` |
| `be_fr_q8d` | To keep public pension system sustainable: increase the retirement age | `Numeric(Byte)` | `%21.0g` |
| `be_fr_q8e` | If life expectancy increases, retirement age needs to increase accordingly | `Numeric(Byte)` | `%21.0g` |
| `be_fr_q8f` | Flexible retirement age, but pension cuts for early retirees | `Numeric(Byte)` | `%21.0g` |
| `be_fr_q9` | Allocation of savings: A - 1% interest vs. B - community project | `Numeric(Byte)` | `%20.0g` |
| `be_fr_q10` | Single companyâ€™s stock safer than stock mutual fund? | `Numeric(Byte)` | `%12.0g` |
| `be_fr_q11` | Disposable income in your country: Position of household | `Numeric(Byte)` | `%22.0g` |
| `be_fr_q12_day` | Payment day | `Numeric(Byte)` | `%39.0g` |
| `be_fr_q12_month` | Payment month | `Numeric(Byte)` | `%39.0g` |
| `be_fr_q12_year` | Payment year | `Numeric(Int)` | `%39.0g` |
| `be_fr_q13a` | Satisfaction w/ability of daily activities (dress.,toilet) | `Numeric(Byte)` | `%34.0g` |
| `be_fr_q13b` | Satisfaction w/ability of physical daily activities (bending, carrying bags) | `Numeric(Byte)` | `%34.0g` |
| `be_fr_q13c` | Satisfaction w/health, long-term chronic ilnesses (cancer, diabetes, heart) | `Numeric(Byte)` | `%34.0g` |
| `be_fr_q13d` | Satisfaction w/cognition (memory, simple calculations) | `Numeric(Byte)` | `%34.0g` |
| `be_fr_q13e` | Satisfaction w/social contacts | `Numeric(Byte)` | `%34.0g` |
| `be_fr_q13f` | Satisfaction w/extent you help family, friends with household tasks and care | `Numeric(Byte)` | `%34.0g` |
| `be_fr_q13g` | Satisfaction w/life (all aspects together) | `Numeric(Byte)` | `%34.0g` |
| `be_fr_q14a` | Satisfied w/situation (medium scenario) | `Numeric(Byte)` | `%34.0g` |
| `be_fr_q14b` | Satisfied w/situation (high scenario) | `Numeric(Byte)` | `%34.0g` |
| `be_fr_q14c` | Satisfied w/situation (low scenario) | `Numeric(Byte)` | `%34.0g` |
| `be_nl_q1` | Percentage of population 65+ | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q2` | Risk of being poor | `Numeric(Byte)` | `%55.0g` |
| `be_nl_q3` | Statutory retirement age (comparable person): old-age pension without penalty | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q4` | Postponed (retired) or will postpone (working) retirement due to pension reform | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q5` | If yes(q4), by how long | `Numeric(Byte)` | `%14.0g` |
| `be_nl_q5a_months` | Number of months | `Numeric(Byte)` | `%14.0g` |
| `be_nl_q5b_years` | Number of years | `Numeric(Byte)` | `%14.0g` |
| `be_nl_q6` | Percentage of GDP going into public pension payments | `Numeric(Byte)` | `%13.0g` |
| `be_nl_q7` | Main funding source for paying public pension in this country | `Numeric(Byte)` | `%36.0g` |
| `be_nl_q8a` | Allocate fewer resources to pensions and more to help unemployed | `Numeric(Byte)` | `%21.0g` |
| `be_nl_q8b` | Population aging makes the public pension system unsustainable | `Numeric(Byte)` | `%21.0g` |
| `be_nl_q8c` | Low growth and low contributions by young threaten pension system | `Numeric(Byte)` | `%21.0g` |
| `be_nl_q8d` | To keep public pension system sustainable: increase the retirement age | `Numeric(Byte)` | `%21.0g` |
| `be_nl_q8e` | If life expectancy increases, retirement age needs to increase accordingly | `Numeric(Byte)` | `%21.0g` |
| `be_nl_q8f` | Flexible retirement age, but pension cuts for early retirees | `Numeric(Byte)` | `%21.0g` |
| `be_nl_q9` | Allocation of savings: A - 1% interest vs. B - community project | `Numeric(Byte)` | `%20.0g` |
| `be_nl_q10` | Single companyâ€™s stock safer than stock mutual fund? | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q11` | Disposable income in your country: Position of household | `Numeric(Byte)` | `%22.0g` |
| `be_nl_q12_day` | Payment day | `Numeric(Byte)` | `%39.0g` |
| `be_nl_q12_month` | Payment month | `Numeric(Byte)` | `%39.0g` |
| `be_nl_q12_year` | Payment year | `Numeric(Int)` | `%39.0g` |
| `be_nl_q13a` | Satisfaction w/ability of daily activities (dress.,toilet) | `Numeric(Byte)` | `%34.0g` |
| `be_nl_q13b` | Satisfaction w/ability of physical daily activities (bending, carrying bags) | `Numeric(Byte)` | `%34.0g` |
| `be_nl_q13c` | Satisfaction w/health, long-term chronic ilnesses (cancer, diabetes, heart) | `Numeric(Byte)` | `%34.0g` |
| `be_nl_q13d` | Satisfaction w/cognition (memory, simple calculations) | `Numeric(Byte)` | `%34.0g` |
| `be_nl_q13e` | Satisfaction w/social contacts | `Numeric(Byte)` | `%34.0g` |
| `be_nl_q13f` | Satisfaction w/extent you help family, friends with household tasks and care | `Numeric(Byte)` | `%34.0g` |
| `be_nl_q13g` | Satisfaction w/life (all aspects together) | `Numeric(Byte)` | `%34.0g` |
| `be_nl_q14a` | Satisfied w/situation (medium scenario) | `Numeric(Byte)` | `%34.0g` |
| `be_nl_q14b` | Satisfied w/situation (high scenario) | `Numeric(Byte)` | `%34.0g` |
| `be_nl_q14c` | Satisfied w/situation (low scenario) | `Numeric(Byte)` | `%34.0g` |
| `ch_q1_a` | Comfortable dealing - information on treatment | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_b` | Comfortable dealing - find professional help | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_c` | Comfortable dealing - understand doctor | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_d` | Comfortable dealing - understand leaflet | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_e` | Comfortable dealing - medicine instruction | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_f` | Comfortable dealing - treatment options | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_g` | Comfortable dealing - second opinion | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_h` | Comfortable dealing - illness-related decisions | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_i` | Comfortable dealing - follow instructions | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_j` | Comfortable dealing - mental health problems | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_k` | Comfortable dealing - health warnings | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_l` | Comfortable dealing - health screenings | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_m` | Comfortable dealing - information on risks in the media | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_n` | Comfortable dealing - protect oneself from illness | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_o` | Comfortable dealing - activities good for mental well-being | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_p` | Comfortable dealing - political changes affecting health | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_q` | Comfortable dealing - understand health advice | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_r` | Comfortable dealing - understand how to get healthier | `Numeric(Byte)` | `%33.0g` |
| `ch_q1_s` | Comfortable dealing - everyday behaviour | `Numeric(Byte)` | `%33.0g` |
| `ch_q2_a` | Specialized vocabulary - prognosis | `Numeric(Byte)` | `%33.0g` |
| `ch_q2_b` | Specialized vocabulary - intubation | `Numeric(Byte)` | `%33.0g` |
| `ch_q2_c` | Specialized vocabulary - palliative care | `Numeric(Byte)` | `%33.0g` |
| `ch_q2_d` | Specialized vocabulary - cardiopulmonary resuscitation | `Numeric(Byte)` | `%33.0g` |
| `ch_q2_e` | Specialized vocabulary - artificial nutrition | `Numeric(Byte)` | `%33.0g` |
| `ch_q2_f` | Specialized vocabulary - sedation | `Numeric(Byte)` | `%33.0g` |
| `ch_q3_a` | Today's treatments' wish - breathing machines | `Numeric(Byte)` | `%33.0g` |
| `ch_q3_b` | Today's treatments' wish - artificial nutrition | `Numeric(Byte)` | `%33.0g` |
| `ch_q3_c` | Today's treatments' wish - blood transfusions | `Numeric(Byte)` | `%33.0g` |
| `ch_q3_d` | Today's treatments' wish - antibiotics | `Numeric(Byte)` | `%33.0g` |
| `ch_q3_e` | Today's treatments' wish - cardiopulmonary resuscitation | `Numeric(Byte)` | `%33.0g` |
| `ch_q4_a` | Feel comfortable - define overtreatment | `Numeric(Byte)` | `%33.0g` |
| `ch_q4_b` | Feel comfortable - talk about end-of-life preferences | `Numeric(Byte)` | `%33.0g` |
| `ch_q4_c` | Feel comfortable - learn more about end-of-life treatments | `Numeric(Byte)` | `%33.0g` |
| `ch_q4_d` | Feel comfortable - advance directive forms | `Numeric(Byte)` | `%33.0g` |
| `ch_q4_e` | Feel comfortable - make decisions regarding treatments | `Numeric(Byte)` | `%33.0g` |
| `ch_q4_f` | Feel comfortable - treatment type if terminal disease | `Numeric(Byte)` | `%33.0g` |
| `ch_q4_g` | Feel comfortable - define conditions when to be left to die | `Numeric(Byte)` | `%33.0g` |
| `ch_q5_a` | Importance of feeling useful to others | `Numeric(Byte)` | `%33.0g` |
| `ch_q5_b` | Importance of avoiding to be a burden | `Numeric(Byte)` | `%33.0g` |
| `ch_q5_c` | Importance of planning events following death | `Numeric(Byte)` | `%33.0g` |
| `ch_q5_d` | Importance of choosing where to die | `Numeric(Byte)` | `%33.0g` |
| `ch_q5_e` | Importance of not dying alone | `Numeric(Byte)` | `%33.0g` |
| `ch_q5_f` | Importance of talking about fears | `Numeric(Byte)` | `%33.0g` |
| `ch_q5_g` | Importance of receiving spiritual or religious assistance | `Numeric(Byte)` | `%33.0g` |
| `ch_q5_h` | Importance of avoiding overtreatment | `Numeric(Byte)` | `%33.0g` |
| `ch_q5_i` | Importance of having physical contact | `Numeric(Byte)` | `%33.0g` |
| `ch_q5_j` | Importance of being able to communicate | `Numeric(Byte)` | `%33.0g` |
| `ch_q5_k` | Importance of being able to feed oneself | `Numeric(Byte)` | `%33.0g` |
| `ch_q5_l` | Importance of using all available medical treatments | `Numeric(Byte)` | `%33.0g` |
| `ch_q5_m` | Importance of living without pain | `Numeric(Byte)` | `%33.0g` |
| `ch_q5_n` | Importance of being fully mentally aware | `Numeric(Byte)` | `%33.0g` |
| `ch_q6_a` | Having made medical decision for someone | `Numeric(Byte)` | `%33.0g` |
| `ch_q6_b` | Having accompanied someone dying | `Numeric(Byte)` | `%33.0g` |
| `ch_q6_c` | Having cared for someone dying | `Numeric(Byte)` | `%33.0g` |
| `ch_q7` | Experience a cardiac and/or respiratory arrest | `Numeric(Byte)` | `%33.0g` |
| `ch_q8` | Incapacitated without hope to recover | `Numeric(Byte)` | `%33.0g` |
| `ch_q9` | Suffering of unbearable pain and symptoms | `Numeric(Byte)` | `%33.0g` |
| `ch_q10_a` | Trust relatives | `Numeric(Byte)` | `%33.0g` |
| `ch_q10_b` | Trust physicians | `Numeric(Byte)` | `%33.0g` |
| `ch_q10_c` | Trust healthcare insurances | `Numeric(Byte)` | `%33.0g` |
| `ch_q10_d` | Trust the Swiss healthcare system | `Numeric(Byte)` | `%33.0g` |
| `ch_q10_e` | Trust the Swiss legal system (justice) | `Numeric(Byte)` | `%33.0g` |
| `ch_q10_f` | Trust religious authorities | `Numeric(Byte)` | `%33.0g` |
| `ch_q11` | Having Discussed wishes for the end of life | `Numeric(Byte)` | `%33.0g` |
| `ch_q12_a` | Discussed end-of-life wishes with partner | `Numeric(Byte)` | `%33.0g` |
| `ch_q12_b` | Discussed end-of-life wishes with child | `Numeric(Byte)` | `%33.0g` |
| `ch_q12_c` | Discussed end-of-life wishes with sibling | `Numeric(Byte)` | `%33.0g` |
| `ch_q12_d` | Discussed end-of-life wishes with friend | `Numeric(Byte)` | `%33.0g` |
| `ch_q12_e` | Discussed end-of-life wishes with physician | `Numeric(Byte)` | `%33.0g` |
| `ch_q12_f` | Discussed end-of-life wishes with other person | `Numeric(Byte)` | `%33.0g` |
| `ch_q13` | Completed an advance directive | `Numeric(Byte)` | `%33.0g` |
| `ch_q14_a` | No advance directive - not aware of their existence | `Numeric(Byte)` | `%33.0g` |
| `ch_q14_b` | No advance directive - it is difficult to determine what to write | `Numeric(Byte)` | `%33.0g` |
| `ch_q14_c` | No advance directive - family or physician will make decisions | `Numeric(Byte)` | `%33.0g` |
| `ch_q14_d` | No advance directive - it is too early | `Numeric(Byte)` | `%33.0g` |
| `ch_q14_e` | No advance directive - afraid of not receiving adequate healthcare | `Numeric(Byte)` | `%33.0g` |
| `ch_q14_f` | No advance directive - deciding in advance is pointless | `Numeric(Byte)` | `%33.0g` |
| `ch_q14_g` | No advance directive - did not have time to complete one | `Numeric(Byte)` | `%33.0g` |
| `ch_q14_h` | No advance directive - other reason | `Numeric(Byte)` | `%33.0g` |
| `ch_q15` | Likelihood to have advance directives in the future | `Numeric(Byte)` | `%33.0g` |
| `ch_q16` | Appointed someone to make medical decisions | `Numeric(Byte)` | `%33.0g` |
| `ch_q17_a` | Appointed partner | `Numeric(Byte)` | `%33.0g` |
| `ch_q17_b` | Appointed child | `Numeric(Byte)` | `%33.0g` |
| `ch_q17_c` | Appointed sibling | `Numeric(Byte)` | `%33.0g` |
| `ch_q17_d` | Appointed friend | `Numeric(Byte)` | `%33.0g` |
| `ch_q17_e` | Appointed physician | `Numeric(Byte)` | `%33.0g` |
| `ch_q17_f` | Appointed an other person | `Numeric(Byte)` | `%33.0g` |
| `ch_q18` | Likelihood to appoint someone to make medical decision in the future | `Numeric(Byte)` | `%33.0g` |
| `ch_q19` | Support legality of assisted suicide as is currently the case in Switzerland | `Numeric(Byte)` | `%33.0g` |
| `ch_q20` | Consider asking for assisted suicide under certain circumstances | `Numeric(Byte)` | `%33.0g` |
| `ch_q21` | Member of a right-to-die organisation | `Numeric(Byte)` | `%33.0g` |
| `ch_q22` | Likelihood to become member of a right-to-die organisation | `Numeric(Byte)` | `%33.0g` |
| `ch_q23` | Has a partner | `Numeric(Byte)` | `%33.0g` |
| `ch_q24_a` | Know partner's wishes for the end-of-life in general | `Numeric(Byte)` | `%33.0g` |
| `ch_q24_b` | Know partner's wishes for medical treamtent at the end-of-life | `Numeric(Byte)` | `%33.0g` |
| `ch_q25_a` | Partner knows respondent's wishes for the end-of-life in general | `Numeric(Byte)` | `%33.0g` |
| `ch_q25_b` | Partner knows respondent's wishes for medical treatment at the end-of-life | `Numeric(Byte)` | `%33.0g` |
| `ch_q26_a` | Importance of feeling useful | `Numeric(Byte)` | `%33.0g` |
| `ch_q26_b` | Importance of avoiding to be a burden | `Numeric(Byte)` | `%33.0g` |
| `ch_q26_c` | Importance of choosing where to die | `Numeric(Byte)` | `%33.0g` |
| `ch_q26_d` | Importance of not dying alone | `Numeric(Byte)` | `%33.0g` |
| `ch_q26_e` | Importance of receiving spiritual or religious assistance | `Numeric(Byte)` | `%33.0g` |
| `ch_q26_f` | Importance of avoiding overtreatment | `Numeric(Byte)` | `%33.0g` |
| `ch_q26_g` | Importance of being able to communicate | `Numeric(Byte)` | `%33.0g` |
| `ch_q26_h` | Importance of being able to feed oneself | `Numeric(Byte)` | `%33.0g` |
| `ch_q26_i` | Importance of using all available medical treatments | `Numeric(Byte)` | `%33.0g` |
| `ch_q26_j` | Importance of living without pain | `Numeric(Byte)` | `%33.0g` |
| `ch_q26_k` | Importance of being fully mentally aware | `Numeric(Byte)` | `%33.0g` |
| `ch_q27` | Partner's wishes in case of cardiac and/or respiratory arrest | `Numeric(Byte)` | `%33.0g` |
| `ch_q28` | Partner's wishes in case of incapacity without hope to recover | `Numeric(Byte)` | `%35.0g` |
| `ch_q29` | Partner's wishes in case of unbearable pain and symptoms | `Numeric(Byte)` | `%33.0g` |
| `ch_q30_a` | Likelihood to die in a nursing home | `Numeric(Byte)` | `%33.0g` |
| `ch_q30_b` | Likelihood to die in a hospital | `Numeric(Byte)` | `%33.0g` |
| `ch_q30_c` | Likelihood to die at home | `Numeric(Byte)` | `%33.0g` |
| `ch_q30_d` | Likelihood to suffer from dementia at 75 | `Numeric(Byte)` | `%33.0g` |
| `ch_q30_e` | Likelihood of benefitting from artificial nutrition when imminent dying | `Numeric(Byte)` | `%33.0g` |
| `ch_q30_f` | Likelihood of successful pain treatment when imminent dying | `Numeric(Byte)` | `%33.0g` |
| `ch_q30_g` | Likelihood of benefitting pneumonia treatment when imminent dying | `Numeric(Byte)` | `%33.0g` |
| `ch_q30_h` | Likelihood of surviving from cardiopulmonary resuscitation | `Numeric(Byte)` | `%33.0g` |
| `ch_q30_i` | Likelihood of being asked to make medical decisions for partner | `Numeric(Byte)` | `%33.0g` |
| `ch_q30_j` | Likelihood of suffering from dementia at 95 | `Numeric(Byte)` | `%33.0g` |
| `ch_q30_k` | Likelihood of success of a fourth chemotherapy when advanced cancer | `Numeric(Byte)` | `%33.0g` |
| `ch_q30_l` | Likelihood to accept a fourth chemotherapy in case of advanced cancer | `Numeric(Byte)` | `%33.0g` |
| `ch_q33` | Difficulty to answer the questionnaire | `Numeric(Byte)` | `%33.0g` |
| `cz_A1` | Human life extension | `Numeric(Byte)` | `%34.0g` |
| `cz_A2a` | Body ageing cosmetics | `Numeric(Byte)` | `%10.0g` |
| `cz_A2b` | Body ageing aesthetics | `Numeric(Byte)` | `%10.0g` |
| `cz_A2c` | Body ageing surgical | `Numeric(Byte)` | `%10.0g` |
| `cz_A2d` | Body ageing other | `Numeric(Byte)` | `%10.0g` |
| `cz_A3a` | Body procedure reaction | `Numeric(Byte)` | `%10.0g` |
| `cz_A3b` | Body procedure feelings | `Numeric(Byte)` | `%10.0g` |
| `cz_A3c` | Body procedure doctor | `Numeric(Byte)` | `%10.0g` |
| `cz_B1` | Hours TV | `Numeric(Byte)` | `%10.0g` |
| `cz_B2` | Hours radio | `Numeric(Byte)` | `%10.0g` |
| `cz_B3` | Hours reading | `Numeric(Byte)` | `%10.0g` |
| `cz_B4` | Hours internet | `Numeric(Byte)` | `%10.0g` |
| `cz_B5` | Hours social media | `Numeric(Byte)` | `%10.0g` |
| `cz_C1a` | HC travel time GP | `Numeric(Byte)` | `%14.0g` |
| `cz_C1b` | HC travel time dentist | `Numeric(Byte)` | `%14.0g` |
| `cz_C1c` | HC travel time gynecology | `Numeric(Byte)` | `%14.0g` |
| `cz_C1d` | HC travel time pharmacy | `Numeric(Byte)` | `%14.0g` |
| `cz_C1e` | HC travel time hospital | `Numeric(Byte)` | `%14.0g` |
| `cz_C1f` | HC travel time ER | `Numeric(Byte)` | `%14.0g` |
| `cz_C2a` | HC travel means GP | `Numeric(Byte)` | `%16.0g` |
| `cz_C2b` | HC travel means dentist | `Numeric(Byte)` | `%16.0g` |
| `cz_C2c` | HC travel means gynecology | `Numeric(Byte)` | `%16.0g` |
| `cz_C2d` | HC travel means pharmacy | `Numeric(Byte)` | `%16.0g` |
| `cz_C2e` | HC travel means hospital | `Numeric(Byte)` | `%16.0g` |
| `cz_C2f` | HC travel means ER | `Numeric(Byte)` | `%16.0g` |
| `cz_D1` | Nutrition full meals | `Numeric(Byte)` | `%10.0g` |
| `cz_D2` | Nutrition drinks | `Numeric(Byte)` | `%12.0g` |
| `cz_D3` | Nutrition state | `Numeric(Byte)` | `%14.0g` |
| `cz_D4` | Nutrition weigh | `Numeric(Byte)` | `%14.0g` |
| `cz_D5` | Nutrition GP weigh | `Numeric(Byte)` | `%20.0g` |
| `cz_D6` | Nutrition GP eating | `Numeric(Byte)` | `%19.0g` |
| `cz_D7` | Nutrition special diet | `Numeric(Byte)` | `%37.0g` |
| `cz_D8a` | Diet Info GP | `Numeric(Byte)` | `%10.0g` |
| `cz_D8b` | Diet Info nutrition therapist | `Numeric(Byte)` | `%10.0g` |
| `cz_D8c` | Diet Info another specialist | `Numeric(Byte)` | `%10.0g` |
| `cz_D8d` | Diet Info myself | `Numeric(Byte)` | `%10.0g` |
| `cz_D8e` | Diet Info never had diet | `Numeric(Byte)` | `%10.0g` |
| `cz_D8f` | Diet Info none | `Numeric(Byte)` | `%10.0g` |
| `cz_D9` | Nutrition therapist | `Numeric(Byte)` | `%16.0g` |
| `cz_D10` | Nutrition therapist paid | `Numeric(Byte)` | `%25.0g` |
| `cz_D11` | Nutrition supplements | `Numeric(Byte)` | `%15.0g` |
| `cz_E1` | Sex frequency | `Numeric(Byte)` | `%19.0g` |
| `cz_E2` | Sex importance | `Numeric(Byte)` | `%10.0g` |
| `cz_E3` | Sex desire | `Numeric(Byte)` | `%12.0g` |
| `cz_E4` | Sex internet | `Numeric(Byte)` | `%19.0g` |
| `cz_E5` | Sex online dating | `Numeric(Byte)` | `%15.0g` |
| `cz_F1a` | Law help no one | `Numeric(Byte)` | `%10.0g` |
| `cz_F1b` | Law help friends | `Numeric(Byte)` | `%10.0g` |
| `cz_F1c` | Law help online | `Numeric(Byte)` | `%10.0g` |
| `cz_F1d` | Law help bureau | `Numeric(Byte)` | `%10.0g` |
| `cz_F1e` | Law help attorney | `Numeric(Byte)` | `%10.0g` |
| `cz_F1f` | Law help court | `Numeric(Byte)` | `%10.0g` |
| `cz_F1g` | Law help authority | `Numeric(Byte)` | `%10.0g` |
| `cz_F1h` | Law help none | `Numeric(Byte)` | `%10.0g` |
| `cz_F2a` | Law learn neighbor | `Numeric(Byte)` | `%10.0g` |
| `cz_F2b` | Law learn scam | `Numeric(Byte)` | `%10.0g` |
| `cz_F2c` | Law learn inheritance | `Numeric(Byte)` | `%10.0g` |
| `cz_F2d` | Law learn house | `Numeric(Byte)` | `%10.0g` |
| `cz_F2e` | Law learn contracts | `Numeric(Byte)` | `%10.0g` |
| `cz_F2f` | Law learn goods | `Numeric(Byte)` | `%10.0g` |
| `cz_F2g` | Law learn none | `Numeric(Byte)` | `%10.0g` |
| `cz_F2h` | Law learn noanswer | `Numeric(Byte)` | `%10.0g` |
| `cz_F3a` | Law consumer withdrew | `Numeric(Byte)` | `%10.0g` |
| `cz_F3b` | Law consumer complaint | `Numeric(Byte)` | `%10.0g` |
| `cz_F3c` | Law consumer sued | `Numeric(Byte)` | `%10.0g` |
| `cz_F3d` | Law consumer settlement | `Numeric(Byte)` | `%10.0g` |
| `cz_F3e` | Law consumer CTIA | `Numeric(Byte)` | `%10.0g` |
| `cz_F3f` | Law consumer none | `Numeric(Byte)` | `%10.0g` |
| `cz_F4a` | Law assets none | `Numeric(Byte)` | `%10.0g` |
| `cz_F4b` | Law assets will | `Numeric(Byte)` | `%10.0g` |
| `cz_F4c` | Law assets deed | `Numeric(Byte)` | `%10.0g` |
| `cz_F4d` | Law assets agreement | `Numeric(Byte)` | `%10.0g` |
| `cz_F4e` | Law assets transfer | `Numeric(Byte)` | `%10.0g` |
| `cz_F4f` | Law assets none | `Numeric(Byte)` | `%10.0g` |
| `cz_F5a` | Law healthcare never | `Numeric(Byte)` | `%10.0g` |
| `cz_F5b` | Law healthcare nothing | `Numeric(Byte)` | `%10.0g` |
| `cz_F5c` | Law healthcare transfer | `Numeric(Byte)` | `%10.0g` |
| `cz_F5d` | Law healthcare complaint | `Numeric(Byte)` | `%10.0g` |
| `cz_F5e` | Law healthcare complaint hospital | `Numeric(Byte)` | `%10.0g` |
| `cz_F5f` | Law healthcare complaint CMC | `Numeric(Byte)` | `%10.0g` |
| `cz_F5g` | Law healthcare sued | `Numeric(Byte)` | `%10.0g` |
| `cz_F5h` | Law healthcare none | `Numeric(Byte)` | `%10.0g` |
| `cz_G1` | Execution | `Numeric(Byte)` | `%10.0g` |
| `cz_G2a` | Execution year start | `Numeric(Int)` | `%14.0g` |
| `cz_G2b` | Execution year end | `Numeric(Int)` | `%14.0g` |
| `cz_G3a` | Execution money | `Numeric(Byte)` | `%14.0g` |
| `cz_G3b` | Execution assets | `Numeric(Byte)` | `%14.0g` |
| `cz_G3c` | Execution family friends | `Numeric(Byte)` | `%14.0g` |
| `cz_G3d` | Execution more debt institutions | `Numeric(Byte)` | `%14.0g` |
| `cz_G3e` | Execution more debt other | `Numeric(Byte)` | `%14.0g` |
| `cz_G3f` | Execution none | `Numeric(Byte)` | `%14.0g` |
| `cz_G4a` | Execution situation paid | `Numeric(Byte)` | `%14.0g` |
| `cz_G4b` | Execution situation bankrupt | `Numeric(Byte)` | `%14.0g` |
| `cz_G4c` | Execution situation property | `Numeric(Byte)` | `%14.0g` |
| `cz_G4d` | Execution situation debt friends relatives | `Numeric(Byte)` | `%14.0g` |
| `cz_G4e` | Execution situation debt insitutions | `Numeric(Byte)` | `%14.0g` |
| `cz_G4f` | Execution situation debt other | `Numeric(Byte)` | `%14.0g` |
| `cz_G4g` | Execution situation none | `Numeric(Byte)` | `%14.0g` |
| `cz_H1` | Transformation | `Numeric(Byte)` | `%16.0g` |
| `cz_I1` | Property ownership | `Numeric(Byte)` | `%10.0g` |
| `cz_I2` | Property ownership acquired | `Numeric(Byte)` | `%14.0g` |
| `cz_I3` | Property ownership finances | `Numeric(Byte)` | `%23.0g` |
| `cz_J1a` | Care death | `Numeric(Byte)` | `%10.0g` |
| `cz_J1b` | Care cared | `Numeric(Byte)` | `%10.0g` |
| `cz_J2` | Care info prognosis | `Numeric(Byte)` | `%18.0g` |
| `cz_J3` | Care info course | `Numeric(Byte)` | `%18.0g` |
| `cz_J4` | Care prolong improve | `Numeric(Byte)` | `%10.0g` |
| `cz_J5a` | Care decision me | `Numeric(Byte)` | `%15.0g` |
| `cz_J5b` | Care decision doctor | `Numeric(Byte)` | `%15.0g` |
| `cz_J5c` | Care decision family | `Numeric(Byte)` | `%15.0g` |
| `cz_Ka` | Memory impairement | `Numeric(Byte)` | `%10.0g` |
| `cz_Kb` | Memory daily life | `Numeric(Byte)` | `%10.0g` |
| `cz_Kc` | Memory orientation | `Numeric(Byte)` | `%10.0g` |
| `cz_Kd` | Memory content book | `Numeric(Byte)` | `%10.0g` |
| `cz_Ke` | Memory content film | `Numeric(Byte)` | `%10.0g` |
| `cz_Kf` | Memory info news | `Numeric(Byte)` | `%10.0g` |
| `cz_Kg` | Memory info conversation | `Numeric(Byte)` | `%10.0g` |
| `cz_Kh` | Memory repeat questions | `Numeric(Byte)` | `%10.0g` |
| `cz_Ki` | Memory repeat info | `Numeric(Byte)` | `%10.0g` |
| `cz_Kj` | Memory remember while | `Numeric(Byte)` | `%10.0g` |
| `cz_Kk` | Memory remember day | `Numeric(Byte)` | `%10.0g` |
| `cz_Kl` | Memory remember yesterday | `Numeric(Byte)` | `%10.0g` |
| `cz_Km` | Memory remember times | `Numeric(Byte)` | `%10.0g` |
| `cz_Kn` | Memory difficulty story | `Numeric(Byte)` | `%10.0g` |
| `cz_Ko` | Memory difficulty health | `Numeric(Byte)` | `%10.0g` |
| `cz_Kp` | Memory difficulty medication | `Numeric(Byte)` | `%10.0g` |
| `cz_M0` | Retire retired | `Numeric(Byte)` | `%10.0g` |
| `cz_M1` | Retirement age | `Numeric(Byte)` | `%10.0g` |
| `cz_M2` | Retirement stop work | `Numeric(Int)` | `%10.0g` |
| `cz_M3a` | Retire later earnings | `Numeric(Byte)` | `%10.0g` |
| `cz_M3b` | Retire later benefits | `Numeric(Byte)` | `%10.0g` |
| `cz_M3c` | Retire later part-time | `Numeric(Byte)` | `%10.0g` |
| `cz_M3d` | Retire later conditions | `Numeric(Byte)` | `%10.0g` |
| `cz_M3e` | Retire later tasks | `Numeric(Byte)` | `%10.0g` |
| `cz_M3f` | Retire later recognition | `Numeric(Byte)` | `%10.0g` |
| `cz_M3g` | Retire later none | `Numeric(Byte)` | `%10.0g` |
| `cz_M3ap` | Retire earnings percent | `Numeric(Byte)` | `%10.0g` |
| `cz_M3bp` | Retire benefits percent | `Numeric(Long)` | `%10.0g` |
| `cz_M4` | Retire ends meet | `Numeric(Byte)` | `%16.0g` |
| `cz_M5a` | Retire income minimal fall | `Numeric(Byte)` | `%16.0g` |
| `cz_M5b` | Retire income average fall | `Numeric(Byte)` | `%16.0g` |
| `cz_M5c` | Retire income maximal fall | `Numeric(Byte)` | `%16.0g` |
| `cz_M5d` | Retire income your fall | `Numeric(Byte)` | `%16.0g` |
| `cz_M6` | Retire pension eligible | `Numeric(Byte)` | `%10.0g` |
| `de_q1` | Importance of surveys for society | `Numeric(Byte)` | `%16.0f` |
| `de_q2` | Surveys are wasted time | `Numeric(Byte)` | `%16.0f` |
| `de_q3` | Answering many questions is exhausting | `Numeric(Byte)` | `%16.0f` |
| `de_q4` | Results of surveys are mostly trustworthy | `Numeric(Byte)` | `%16.0f` |
| `de_q5` | Importance of knowing the institution | `Numeric(Byte)` | `%20.0f` |
| `de_q6` | Confidence in scientific institutions | `Numeric(Byte)` | `%23.0f` |
| `de_q7` | Confidence in opinion research institutions | `Numeric(Byte)` | `%23.0f` |
| `de_q8` | Confidence in authorities | `Numeric(Byte)` | `%23.0f` |
| `de_q9` | Concern: privacy | `Numeric(Byte)` | `%20.0f` |
| `de_q10` | Concern: data theft or abuse | `Numeric(Byte)` | `%20.0f` |
| `de_q11` | Concern of others: sharing too much info | `Numeric(Byte)` | `%20.0f` |
| `de_q12` | Trust in other people | `Numeric(Byte)` | `%20.0f` |
| `de_q13` | Embarassed to share income | `Numeric(Byte)` | `%16.0f` |
| `de_q14` | Should not talk about income | `Numeric(Byte)` | `%16.0f` |
| `de_q15` | Response to future income question | `Numeric(Byte)` | `%39.0f` |
| `de_q16` | Much to learn from SHARE | `Numeric(Byte)` | `%16.0f` |
| `de_q17` | SHARE questions: too personal | `Numeric(Byte)` | `%16.0f` |
| `de_q18` | SHARE questions: too boring | `Numeric(Byte)` | `%16.0f` |
| `de_q19` | SHARE questions: made me reflect | `Numeric(Byte)` | `%16.0f` |
| `de_q20` | Liked participating in SHARE | `Numeric(Byte)` | `%16.0f` |
| `de_q21` | Reasons for liking/disliking interview | `Numeric(Byte)` | `%16.0f` |
| `de_q22` | Concern: SHARE data leak | `Numeric(Byte)` | `%20.0f` |
| `de_q23` | Concern: receive adverts due to SHARE | `Numeric(Byte)` | `%20.0f` |
| `de_q24` | Concern of others: participation in SHARE | `Numeric(Byte)` | `%20.0f` |
| `de_q25` | Importance: Questions about health status | `Numeric(Byte)` | `%20.0f` |
| `de_q26` | Importance: Questions about income | `Numeric(Byte)` | `%20.0f` |
| `de_q27` | Importance: Questions about social contacts | `Numeric(Byte)` | `%20.0f` |
| `de_q28` | Importance: Questions about hobbies | `Numeric(Byte)` | `%20.0f` |
| `de_q29` | Expectations on life changes | `Numeric(Byte)` | `%16.0f` |
| `de_q31` | Further comments | `Numeric(Byte)` | `%16.0f` |
| `de_mode` | Mode | `Numeric(Byte)` | `%33.0g` |
| `dk_S1` | Member of Evangelical Lutheran Church or other religious community? | `Numeric(Byte)` | `%12.0g` |
| `dk_S2` | How often do you go to church (or the like: mosque, synagogue)? | `Numeric(Byte)` | `%12.0g` |
| `dk_S3` | How often do you pray to God (apart from services)? | `Numeric(Byte)` | `%12.0g` |
| `dk_S4` | How important a role does God play in your life today? | `Numeric(Int)` | `%12.0g` |
| `dk_S5` | Experienced serious life-event(s) that strengthened your faith? | `Numeric(Byte)` | `%12.0g` |
| `dk_S6` | How would you rate your physical fitness compared to your peers? | `Numeric(Int)` | `%12.0g` |
| `dk_S7` | Would you like to be more physical active than today? | `Numeric(Byte)` | `%12.0g` |
| `dk_S8` | Likelihood: More physically active in a year from now | `Numeric(Int)` | `%12.0g` |
| `dk_S9_1` | Willingness to accept tax increase: treatment in public hospitals | `Numeric(Byte)` | `%12.0g` |
| `dk_S9_2` | Willingness to accept tax increase: treatment by general practitioners | `Numeric(Byte)` | `%12.0g` |
| `dk_S9_3` | Willingness to accept tax increase: public home care treatment | `Numeric(Byte)` | `%12.0g` |
| `dk_S10_1` | Willingness to accept user charge: treatment in public hospitals | `Numeric(Byte)` | `%12.0g` |
| `dk_S10_2` | Willingness to accept user charge: treatment by general practitioners | `Numeric(Byte)` | `%12.0g` |
| `dk_S10_3` | Willingness to accept user charge: public home care treatment | `Numeric(Byte)` | `%12.0g` |
| `dk_S11` | Experienced less recognition at workplace due to age? | `Numeric(Byte)` | `%12.0g` |
| `ee_k12` | How well do you know the Estonian language. Can you ... | `Numeric(Byte)` | `%37.0g` |
| `ee_K16` | Can you use public transportation? | `Numeric(Byte)` | `%22.0g` |
| `ee_K17` | Can you visit a food and convenience store? | `Numeric(Byte)` | `%22.0g` |
| `ee_K18` | When necessary, can you visit the nearest pharmacy? | `Numeric(Byte)` | `%22.0g` |
| `ee_K19` | When necessary, can you visit your family doctor or nurse? | `Numeric(Byte)` | `%22.0g` |
| `ee_K20` | When necessary, can you visit the city or rural municipality government? | `Numeric(Byte)` | `%22.0g` |
| `ee_K21` | When need cash, can you get it from the nearest ATM/bank/post office or store? | `Numeric(Byte)` | `%22.0g` |
| `ee_K22` | When you wish, can you get to cult. event, sports practice or training course? | `Numeric(Byte)` | `%22.0g` |
| `ee_K231` | If you need access, in what ways have you reached food and convenience store | `Numeric(Byte)` | `%49.0g` |
| `ee_K232` | If you need access, in what ways have you reached pharmacy | `Numeric(Byte)` | `%49.0g` |
| `ee_K233` | If you need access, in what ways have you reached family doctor/nurse | `Numeric(Byte)` | `%49.0g` |
| `ee_K234` | If you need access, in what ways have you reached city/rural municipal. gov. | `Numeric(Byte)` | `%49.0g` |
| `ee_K235` | If you need access, in what ways have you reached ATM/bank/post office(store) | `Numeric(Byte)` | `%49.0g` |
| `ee_K236` | If you need access, in what ways have you reached cult.building, theatre, sports | `Numeric(Byte)` | `%49.0g` |
| `ee_K24` | Has a social worker evaluated your need for a benefit of service? | `Numeric(Byte)` | `%16.0g` |
| `ee_K25` | Has a care plan been prepared for you? | `Numeric(Byte)` | `%16.0g` |
| `ee_K26` | Have been assigned a caregiver by the local gov.? | `Numeric(Byte)` | `%16.0g` |
| `ee_K261` | (If yes) Who has compensated the care service/care for special needs? | `Numeric(Byte)` | `%48.0g` |
| `ee_K28` | Do you receive home services organised by the local gov.? | `Numeric(Byte)` | `%16.0g` |
| `ee_K281` | (If yes) What type of home services the local gov. organises for you? | `Numeric(Byte)` | `%24.0g` |
| `ee_K29` | Other services that improve your coping by the local gov.? | `Numeric(Byte)` | `%19.0g` |
| `ee_K30` | Social rehabilitation plan composed by the SIB in the last 12 months? | `Numeric(Byte)` | `%16.0g` |
| `ee_K301` | (If yes) Assigned a social or work rehabilitation plan? | `Numeric(Byte)` | `%16.0g` |
| `ee_K302` | (If yes) Which rehabilitation services by SIB received in the last 12 months? | `Numeric(Byte)` | `%18.0g` |
| `ee_K31` | In the last 12 month have you obtained any technical aids? | `Numeric(Byte)` | `%16.0g` |
| `ee_K311` | (If yes) Have these technical aids been compensated to you? | `Numeric(Byte)` | `%32.0g` |
| `eg_P1` | Usual bedtime | `Numeric(Double)` | `%tcHH:MM:SS` |
| `eg_P2` | Minutes to fall asleep | `Numeric(Double)` | `%tcHH:MM:SS` |
| `eg_P3` | Usual get up time | `Numeric(Double)` | `%tcHH:MM:SS` |
| `eg_P4` | Hours sleep per night | `Numeric(Double)` | `%tcHH:MM:SS` |
| `eg_P5a` | Cannot get to sleep within 30 minutes | `Numeric(Byte)` | `%26.0g` |
| `eg_P5b` | Wake up in the middle of the night or early morning | `Numeric(Byte)` | `%26.0g` |
| `eg_P5c` | Have to get up to use the bathroom | `Numeric(Byte)` | `%26.0g` |
| `eg_P5d` | Cannot breathe comfortably | `Numeric(Byte)` | `%26.0g` |
| `eg_P5e` | Cough or snore loudly | `Numeric(Byte)` | `%26.0g` |
| `eg_P5f` | Feel cold | `Numeric(Byte)` | `%26.0g` |
| `eg_p5g` | Feel to hot | `Numeric(Byte)` | `%26.0g` |
| `eg_P5h` | Have bad dreams | `Numeric(Byte)` | `%26.0g` |
| `eg_P5i` | Have pain | `Numeric(Byte)` | `%26.0g` |
| `eg_P5j` | Other reasons | `Numeric(Byte)` | `%26.0g` |
| `eg_P6` | Sleep quality | `Numeric(Byte)` | `%26.0g` |
| `eg_P7` | Pharmaceuticals to help to sleep | `Numeric(Byte)` | `%26.0g` |
| `eg_P8` | Trouble staying awake | `Numeric(Byte)` | `%26.0g` |
| `eg_P9` | Problem to get things done | `Numeric(Byte)` | `%26.0g` |
| `eg_P10` | Bed partner or roommate | `Numeric(Byte)` | `%37.0g` |
| `eg_P11a` | Snored loudly | `Numeric(Byte)` | `%26.0g` |
| `eg_P11b` | Long pauses wetween breaths while asleep | `Numeric(Byte)` | `%26.0g` |
| `eg_P11c` | Legs twitching or jerking while asleep | `Numeric(Byte)` | `%26.0g` |
| `eg_P11d` | Episodes of dirorientation or confusion during sleep | `Numeric(Byte)` | `%26.0g` |
| `eg_P11e` | Other restlessness wile asleep | `Numeric(Byte)` | `%26.0g` |
| `eg_P12` | Satisfied with sleep | `Numeric(Byte)` | `%17.0g` |
| `eg_P13` | Awake without dozing | `Numeric(Byte)` | `%17.0g` |
| `eg_P14` | Asleep between 2:00 and 4:00 | `Numeric(Byte)` | `%17.0g` |
| `eg_P15` | Less than 30 awake at night | `Numeric(Byte)` | `%17.0g` |
| `eg_P16` | Sleep between 6 and 8 hours/day | `Numeric(Byte)` | `%17.0g` |
| `eg_G1` | Feeling that you don't care abotu what goes on around | `Numeric(Byte)` | `%15.0g` |
| `eg_G2` | Surprised by the behavior of people | `Numeric(Byte)` | `%17.0g` |
| `eg_G3` | People disappointed | `Numeric(Byte)` | `%17.0g` |
| `eg_G4` | Life goals or purpose | `Numeric(Byte)` | `%32.0g` |
| `eg_G5` | Feeling being treated unfairly | `Numeric(Byte)` | `%15.0g` |
| `eg_G6` | Feeling being in unfamilar situation | `Numeric(Byte)` | `%15.0g` |
| `eg_G7` | Doing things is a... | `Numeric(Byte)` | `%40.0g` |
| `eg_G8` | Mixed-up feeling and ideas | `Numeric(Byte)` | `%15.0g` |
| `eg_G9` | Feelings inside you would not feel | `Numeric(Byte)` | `%15.0g` |
| `eg_G10` | Feeling loser | `Numeric(Byte)` | `%15.0g` |
| `eg_G11` | When something happened, you have found that... | `Numeric(Byte)` | `%50.0g` |
| `eg_G12` | Feeling little meaning in the things you do | `Numeric(Byte)` | `%15.0g` |
| `eg_G13` | Keeping under control | `Numeric(Byte)` | `%15.0g` |
| `es_q1` | Percentage of population 65+ | `Numeric(Byte)` | `%12.0g` |
| `es_q2` | Risk of being poor | `Numeric(Byte)` | `%63.0g` |
| `es_q3` | Statutory retirement age (comparable person): old-age pension without penalty | `Numeric(Byte)` | `%12.0g` |
| `es_q4` | Postponed (retired) or will postpone (working) retirement due to pension reform | `Numeric(Byte)` | `%10.0g` |
| `es_q5` | If yes(q4), by how long | `Numeric(Byte)` | `%17.0g` |
| `es_q5a_months` | Number of months | `Numeric(Byte)` | `%10.0g` |
| `es_q5b_years` | Number of years | `Numeric(Byte)` | `%10.0g` |
| `es_q6` | Percentage of GDP going into public pension payments | `Numeric(Byte)` | `%13.0g` |
| `es_q7` | Main funding source for paying public pension in this country | `Numeric(Byte)` | `%66.0g` |
| `es_q8a` | Allocate fewer resources to pensions and more to help unemployed | `Numeric(Byte)` | `%26.0g` |
| `es_q8b` | Population aging makes the public pension system unsustainable | `Numeric(Byte)` | `%26.0g` |
| `es_q8c` | Low growth and low contributions by young threaten pension system | `Numeric(Byte)` | `%26.0g` |
| `es_q8d` | To keep public pension system sustainable: increase the retirement age | `Numeric(Byte)` | `%26.0g` |
| `es_q8e` | If life expectancy increases, retirement age needs to increase accordingly | `Numeric(Byte)` | `%26.0g` |
| `es_q8f` | Flexible retirement age, but pension cuts for early retirees | `Numeric(Byte)` | `%26.0g` |
| `es_q9` | Allocation of savings: A - 1% interest vs. B - community project | `Numeric(Byte)` | `%60.0g` |
| `es_q10` | Single companyâ€™s stock safer than stock mutual fund? | `Numeric(Byte)` | `%12.0g` |
| `es_q11` | Disposable income in your country: Position of household | `Numeric(Byte)` | `%17.0g` |
| `fi_h01_1` | employment status | `Numeric(Byte)` | `%47.0g` |
| `fi_h01_2` | employment status again if two ticks in q1 | `Numeric(Byte)` | `%47.0g` |
| `fi_h01_3` | year of part time retirement | `Numeric(Int)` | `%10.0g` |
| `fi_h01_4` | year of retirement | `Numeric(Int)` | `%10.0g` |
| `fi_h02` | working capacity 0-10 | `Numeric(Byte)` | `%10.0g` |
| `fi_h03` | more or less wage work | `Numeric(Byte)` | `%42.0g` |
| `fi_h04` | more or less volunteer work | `Numeric(Byte)` | `%47.0g` |
| `fi_h05` | how often social media | `Numeric(Byte)` | `%38.0g` |
| `fi_h06` | self assesment social media | `Numeric(Byte)` | `%39.0g` |
| `fi_h07` | partnership situation | `Numeric(Byte)` | `%45.0g` |
| `fi_h08` | ideal partnership situation | `Numeric(Byte)` | `%45.0g` |
| `fi_h09` | satisfaction without partner | `Numeric(Byte)` | `%30.0g` |
| `fi_h10` | looking for partner | `Numeric(Byte)` | `%90.0g` |
| `fi_h12_1` | communication to one another | `Numeric(Byte)` | `%17.0g` |
| `fi_h12_2` | understading | `Numeric(Byte)` | `%17.0g` |
| `fi_h12_3` | physical closeness | `Numeric(Byte)` | `%17.0g` |
| `fi_h12_4` | partner appreciates | `Numeric(Byte)` | `%17.0g` |
| `fi_h12_5` | love for one another | `Numeric(Byte)` | `%17.0g` |
| `fi_h12_6` | feeling of togetherness | `Numeric(Byte)` | `%17.0g` |
| `fi_h12_7` | support from partner | `Numeric(Byte)` | `%17.0g` |
| `fi_h12_8` | thinking about breakup | `Numeric(Byte)` | `%17.0g` |
| `fi_h12_9` | satisfaction economic issues | `Numeric(Byte)` | `%17.0g` |
| `fi_h12_10` | satisfaction time spent together | `Numeric(Byte)` | `%17.0g` |
| `fi_h13_1` | fight chores | `Numeric(Byte)` | `%28.0g` |
| `fi_h13_2` | fight money | `Numeric(Byte)` | `%28.0g` |
| `fi_h13_3` | fight free time | `Numeric(Byte)` | `%28.0g` |
| `fi_h13_4` | fight sexual life | `Numeric(Byte)` | `%28.0g` |
| `fi_h13_5` | fight unfaithfulness or jealousy | `Numeric(Byte)` | `%28.0g` |
| `fi_h13_6` | fight friends | `Numeric(Byte)` | `%28.0g` |
| `fi_h13_7` | fight children | `Numeric(Byte)` | `%28.0g` |
| `fi_h13_8` | fight my relatives | `Numeric(Byte)` | `%28.0g` |
| `fi_h13_9` | fight partner's relatives | `Numeric(Byte)` | `%28.0g` |
| `fi_h13_10` | fight divorce or blended families | `Numeric(Byte)` | `%28.0g` |
| `fi_h13_11` | fight alcohol or substances | `Numeric(Byte)` | `%28.0g` |
| `fi_h13_12` | fight own work | `Numeric(Byte)` | `%28.0g` |
| `fi_h13_13` | fight partner's work | `Numeric(Byte)` | `%28.0g` |
| `fi_h13_14` | fight own retirement | `Numeric(Byte)` | `%28.0g` |
| `fi_h13_15` | fight partner's retirement | `Numeric(Byte)` | `%28.0g` |
| `fr_do01_ald` | Exemption of out-of-pockets and deductibles for health care (ALD) | `Numeric(Byte)` | `%10.0g` |
| `fr_do02_sup` | Supplementary health insurance (SHI) | `Numeric(Byte)` | `%10.0g` |
| `fr_do03_cmu` | Free supplementary health insurance coverage (CMUC) | `Numeric(Byte)` | `%10.0g` |
| `fr_do04_emp` | SHI provided by employer | `Numeric(Byte)` | `%10.0g` |
| `fr_do05_acs` | SHI - subsidize suscription (ACS) | `Numeric(Byte)` | `%10.0g` |
| `fr_do06_spe` | Satisfaction SHI coverage for specialist care | `Numeric(Byte)` | `%21.0g` |
| `fr_do06_dru` | Satisfaction SHI coverage for drugs | `Numeric(Byte)` | `%21.0g` |
| `fr_do06_hos` | Satisfaction SHI coverage for inpatient hospital care | `Numeric(Byte)` | `%21.0g` |
| `fr_do06_den` | Satisfaction SHI coverage for dental care | `Numeric(Byte)` | `%21.0g` |
| `fr_do06_hea` | Satisfaction SHI coverage for hearing aids | `Numeric(Byte)` | `%21.0g` |
| `fr_do07_pay` | SHI premium amount | `Numeric(Long)` | `%10.0g` |
| `fr_do07_per` | SHI premium - monthly vs annually | `Numeric(Byte)` | `%10.0g` |
| `fr_do08_peo` | SHI - number of people covered | `Numeric(Byte)` | `%10.0g` |
| `fr_do09_aff` | No SHI - cannot afford | `Numeric(Byte)` | `%12.0g` |
| `fr_do09_ald` | No SHI - fully covered (ALD) | `Numeric(Byte)` | `%12.0g` |
| `fr_do09_nee` | No SHI - don't need coverage | `Numeric(Byte)` | `%12.0g` |
| `fr_do09_ret` | No SHI - retirement or unemployment | `Numeric(Byte)` | `%12.0g` |
| `fr_do09_tim` | No SHI - no time for this | `Numeric(Byte)` | `%12.0g` |
| `fr_do09_how` | No SHI - don't know how | `Numeric(Byte)` | `%12.0g` |
| `fr_do09_sub` | No SHI - in process of subscription | `Numeric(Byte)` | `%12.0g` |
| `fr_do09_oth` | No SHI - other | `Numeric(Byte)` | `%12.0g` |
| `fr_do09_dkw` | No SHI - Don't know | `Numeric(Byte)` | `%12.0g` |
| `fr_do10_job` | Difficulties - job loss | `Numeric(Byte)` | `%12.0g` |
| `fr_do10_ret` | Difficulties - retirement | `Numeric(Byte)` | `%12.0g` |
| `fr_do10_sit` | Difficulties - change in family situation | `Numeric(Byte)` | `%12.0g` |
| `fr_do10_los` | Difficulties - loss of social benefit | `Numeric(Byte)` | `%12.0g` |
| `fr_do10_oth` | Difficulties - other reason | `Numeric(Byte)` | `%12.0g` |
| `fr_do10_no` | Difficulties - no | `Numeric(Byte)` | `%12.0g` |
| `fr_do10_dkw` | Difficulties - don't know | `Numeric(Byte)` | `%12.0g` |
| `fr_do11_sup` | Denied coverage - SHI | `Numeric(Byte)` | `%12.0g` |
| `fr_do11_ltc` | Denied coverage - long-term care/disability insurance | `Numeric(Byte)` | `%12.0g` |
| `fr_do11_loa` | Denied coverage - loan insurance | `Numeric(Byte)` | `%12.0g` |
| `fr_do11_oth` | Denied coverage - another type | `Numeric(Byte)` | `%12.0g` |
| `fr_do11_no` | Denied coverage - no | `Numeric(Byte)` | `%12.0g` |
| `fr_do11_dkw` | Denied coverage - don't know | `Numeric(Byte)` | `%12.0g` |
| `fr_do12_ris` | Risk-aversion | `Numeric(Byte)` | `%32.0g` |
| `fr_do13_fut` | Concerns about future | `Numeric(Byte)` | `%30.0g` |
| `fr_do14_imp` | Impatience/impulsivity | `Numeric(Byte)` | `%34.0g` |
| `fr_do15_urn` | Ambiguity aversion | `Numeric(Byte)` | `%31.0g` |
| `fr_do16_don` | Time preferences - Present | `Numeric(Byte)` | `%19.0g` |
| `fr_do17_don` | Time preferences - Future | `Numeric(Byte)` | `%19.0g` |
| `fr_do18_mon` | Correlation aversion | `Numeric(Byte)` | `%29.0g` |
| `fr_do19_5y` | Self-perception disability - 5 years | `Numeric(Byte)` | `%10.0g` |
| `fr_do19_10y` | Self-perception disability - 10 years | `Numeric(Byte)` | `%10.0g` |
| `fr_do19_20y` | Self-perception disability - 20 years | `Numeric(Byte)` | `%10.0g` |
| `fr_do20_5y` | Self-perception life expectancy - 5 years | `Numeric(Byte)` | `%10.0g` |
| `fr_do20_10y` | Self-perception life expectancy - 10 years | `Numeric(Byte)` | `%10.0g` |
| `fr_do20_20y` | Self-perception life expectancy - 20 years | `Numeric(Byte)` | `%10.0g` |
| `il_Q1` | Age feel most of the time | `Numeric(Double)` | `%10.0g` |
| `il_Q2_1` | Treated condescendingly or was belittled | `Numeric(Byte)` | `%14.0g` |
| `il_Q2_2` | Not accepted to work or was denied a promotion due to my age | `Numeric(Byte)` | `%14.0g` |
| `il_Q2_3` | Difficulties obtaining a loan or getting a mortgage due to my age | `Numeric(Byte)` | `%14.0g` |
| `il_Q2_4` | Prevented from taking part in activities due to my age | `Numeric(Byte)` | `%14.0g` |
| `il_Q2_5` | Received poorer treatment than others because of my age | `Numeric(Byte)` | `%14.0g` |
| `il_Q2_6` | Not taken seriously or was ignored because of my age | `Numeric(Byte)` | `%14.0g` |
| `il_Q2_7` | Doctor or nurse assumed my illness was due to my age | `Numeric(Byte)` | `%14.0g` |
| `il_Q2_8` | Was denied medical treatment because of my age | `Numeric(Byte)` | `%14.0g` |
| `il_Q2_9` | Assumed I would fail to understand something because of my age | `Numeric(Byte)` | `%14.0g` |
| `il_Q2_10` | Was financially exploited because of my age | `Numeric(Byte)` | `%14.0g` |
| `il_Q3_1` | I'm sufficiently familiar with long-term care insurance | `Numeric(Byte)` | `%16.0g` |
| `il_Q3_2` | Cannot afford the insurance | `Numeric(Byte)` | `%16.0g` |
| `il_Q3_3` | Believe the chances I will need long-term care are slim | `Numeric(Byte)` | `%16.0g` |
| `il_Q3_4` | Have sufficient financial resources for long-term care | `Numeric(Byte)` | `%16.0g` |
| `il_Q3_5` | Satisfied with the long-term care coverage given by Social Security | `Numeric(Byte)` | `%16.0g` |
| `il_Q3_6` | Count on my relatives to care for me if I will ever need long-term care | `Numeric(Byte)` | `%16.0g` |
| `il_Q3_7` | Count on my insurance company to provide me with the necessary coverage | `Numeric(Byte)` | `%16.0g` |
| `il_Q3_8` | Insurance can reduce financial burden on my family | `Numeric(Byte)` | `%16.0g` |
| `il_Q4_1` | Ever discussed with family of friends wishes regarding end of life treatment | `Numeric(Byte)` | `%14.0g` |
| `il_Q4_2` | Professional ever spoken to you about signing advanced directives | `Numeric(Byte)` | `%14.0g` |
| `il_Q4_3` | Signed one or more of the following documents | `Numeric(Byte)` | `%14.0g` |
| `il_Q5_1` | Treatment given for incurable life-threatening illnesses | `Numeric(Byte)` | `%10.0g` |
| `il_Q5_2` | Treatment that alleviates suffering | `Numeric(Byte)` | `%10.0g` |
| `il_Q5_3` | Alleeviates suffering | `Numeric(Byte)` | `%10.0g` |
| `il_Q5_4` | Given only for several weeks | `Numeric(Byte)` | `%10.0g` |
| `il_Q5_5` | Does not shorten life | `Numeric(Byte)` | `%10.0g` |
| `il_Q5_6` | Given only to patients suffering from different types of cancer | `Numeric(Byte)` | `%10.0g` |
| `il_Q6_1` | Support with personal care and household affairs | `Numeric(Byte)` | `%19.0g` |
| `il_Q6_2` | Provision of basic household equipment or transport | `Numeric(Byte)` | `%19.0g` |
| `il_Q6_3` | Participation in social clubs | `Numeric(Byte)` | `%19.0g` |
| `il_Q6_4` | Participation in day centers | `Numeric(Byte)` | `%19.0g` |
| `il_Q6_5` | Membership in the 'Supportive Community' program | `Numeric(Byte)` | `%19.0g` |
| `il_Q6_6` | Online connection to services | `Numeric(Byte)` | `%19.0g` |
| `il_Q6_7` | Regular participation in senior citizen groups | `Numeric(Byte)` | `%19.0g` |
| `il_Q7_1` | Downloading and printing government forms | `Numeric(Byte)` | `%14.0g` |
| `il_Q7_2` | Filling out government forms | `Numeric(Byte)` | `%14.0g` |
| `il_Q7_3` | Payment to government authorities | `Numeric(Byte)` | `%14.0g` |
| `il_Q7a_4` | Experienced difficulties using he services | `Numeric(Byte)` | `%14.0g` |
| `il_Q7b_5` | Using these services helped you | `Numeric(Byte)` | `%14.0g` |
| `il_Q7c_6` | Utilization of governemnt sevices increased as a result | `Numeric(Byte)` | `%14.0g` |
| `it_q1` | Percentage of population 65+ | `Numeric(Byte)` | `%11.0g` |
| `it_q2` | Risk of being poor | `Numeric(Byte)` | `%53.0g` |
| `it_q3` | Statutory retirement age (comparable person): old-age pension without penalty | `Numeric(Byte)` | `%12.0g` |
| `it_q4` | Postponed (retired) or will postpone (working) retirement due to pension reform | `Numeric(Byte)` | `%10.0g` |
| `it_q5` | If yes(q4), by how long | `Numeric(Byte)` | `%10.0g` |
| `it_q5a_months` | Number of months | `Numeric(Byte)` | `%10.0g` |
| `it_q5b_years` | Number of years | `Numeric(Byte)` | `%10.0g` |
| `it_q6` | Percentage of GDP going into public pension payments | `Numeric(Byte)` | `%13.0g` |
| `it_q7` | Main funding source for paying public pension in this country | `Numeric(Byte)` | `%38.0g` |
| `it_q8a` | Allocate fewer resources to pensions and more to help unemployed | `Numeric(Byte)` | `%26.0g` |
| `it_q8b` | Population aging makes the public pension system unsustainable | `Numeric(Byte)` | `%26.0g` |
| `it_q8c` | Low growth and low contributions by young threaten pension system | `Numeric(Byte)` | `%26.0g` |
| `it_q8d` | To keep public pension system sustainable: increase the retirement age | `Numeric(Byte)` | `%26.0g` |
| `it_q8e` | If life expectancy increases, retirement age needs to increase accordingly | `Numeric(Byte)` | `%26.0g` |
| `it_q8f` | Flexible retirement age, but pension cuts for early retirees | `Numeric(Byte)` | `%26.0g` |
| `it_q9` | Allocation of savings: A - 1% interest vs. B - community project | `Numeric(Byte)` | `%30.0g` |
| `it_q10` | Single companyâ€™s stock safer than stock mutual fund? | `Numeric(Byte)` | `%11.0g` |
| `it_q11` | Disposable income in your country: Position of household | `Numeric(Byte)` | `%17.0g` |
| `lu_CAT` | Version of questionnaire | `Numeric(Byte)` | `%10.0g` |
| `lu_Q1_a1` | Transfer ressources - option A - inheritor 1 | `Numeric(Double)` | `%10.0g` |
| `lu_Q1_a2` | Transfer ressources - option A - inheritor 2 | `Numeric(Double)` | `%10.0g` |
| `lu_Q1_b1` | Transfer ressources - option B - inheritor 1 | `Numeric(Double)` | `%10.0g` |
| `lu_Q1_b2` | Transfer ressources - option B - inheritor 2 | `Numeric(Double)` | `%10.0g` |
| `lu_Q2_` | Leave a legs to surviving | `Numeric(Byte)` | `%20.0g` |
| `lu_Q3_` | Legacy sharing between children | `Numeric(Byte)` | `%35.0g` |
| `lu_Q4_1` | Large difference incomes | `Numeric(Byte)` | `%26.0g` |
| `lu_Q4_2` | Reduce differences incomes | `Numeric(Byte)` | `%26.0g` |
| `lu_Q4_3` | Inheritance as unfair source | `Numeric(Byte)` | `%26.0g` |
| `lu_Q4_4` | Inheritances taxes | `Numeric(Byte)` | `%26.0g` |
| `lu_Q5_` | Main reason why a person is poor | `Numeric(Byte)` | `%25.0g` |
| `lu_Q6_` | Main reason why a person is rich | `Numeric(Byte)` | `%27.0g` |
| `lu_Q7_` | Amount of inheritances could receive | `Numeric(Byte)` | `%17.0g` |
| `lu_Q8_1` | Taxes on income over 100,000 | `Numeric(Double)` | `%10.0g` |
| `lu_Q8_2` | Taxes on income over 500,000 | `Numeric(Double)` | `%10.0g` |
| `lu_Q8_3` | Taxes on income over 1,000,000 | `Numeric(Double)` | `%10.0g` |
| `lu_Q9_` | Favorite option among taxes | `Numeric(Byte)` | `%10.0g` |
| `pl_Q1d1` | How often watched news on TV | `Numeric(Byte)` | `%31.0f` |
| `pl_Q1d2` | How often watched films on TV | `Numeric(Byte)` | `%31.0f` |
| `pl_Q1d3` | How often watched drama on TV | `Numeric(Byte)` | `%31.0f` |
| `pl_Q1d4` | How often watched documents on TV | `Numeric(Byte)` | `%31.0f` |
| `pl_Q1d5` | How often listened to concert transmission | `Numeric(Byte)` | `%31.0f` |
| `pl_Q1d6` | How often listened to audiobooks | `Numeric(Byte)` | `%31.0f` |
| `pl_Q1d7` | How often listened to serialized novels | `Numeric(Byte)` | `%31.0f` |
| `pl_Q1d8` | How often listened to scientific programs | `Numeric(Byte)` | `%31.0f` |
| `pl_Q2d1` | If watched a film in a movie theater | `Numeric(Byte)` | `%16.0f` |
| `pl_Q2d2` | If been to theatre | `Numeric(Byte)` | `%16.0f` |
| `pl_Q2d3` | If been to an exhibition | `Numeric(Byte)` | `%16.0f` |
| `pl_Q2d4` | If been to a trip within PL | `Numeric(Byte)` | `%16.0f` |
| `pl_Q2d5` | If been to a trip abroad | `Numeric(Byte)` | `%16.0f` |
| `pl_Q2d6` | If been to a pilgrimage | `Numeric(Byte)` | `%16.0f` |
| `pl_Q2d7` | If been to a local picnic | `Numeric(Byte)` | `%16.0f` |
| `pl_Q2d8` | If been to other cultural event | `Numeric(Byte)` | `%16.0f` |
| `pl_Q3d1` | If goes to library | `Numeric(Byte)` | `%37.0f` |
| `pl_Q3d2` | If goes to religious ceremony | `Numeric(Byte)` | `%37.0f` |
| `pl_Q3d3` | If goes to Older People Club | `Numeric(Byte)` | `%37.0f` |
| `pl_Q3d4` | If goes to classes of the Third Age Uni. | `Numeric(Byte)` | `%37.0f` |
| `pl_Q3d5` | If goes to classes in other institutions | `Numeric(Byte)` | `%37.0f` |
| `pl_Q4d1` | If attended a meeting of a trade union | `Numeric(Byte)` | `%16.0f` |
| `pl_Q4d2` | If attended a protest | `Numeric(Byte)` | `%16.0f` |
| `pl_Q4d3` | If supported social campaigns | `Numeric(Byte)` | `%16.0f` |
| `pl_Q4d4` | If attended a meeting with politicians | `Numeric(Byte)` | `%16.0f` |
| `pl_Q5d1` | If participated in training improving professional competencies | `Numeric(Byte)` | `%16.0f` |
| `pl_Q5d2` | If participated in training developing personal hobbies | `Numeric(Byte)` | `%16.0f` |
| `pl_Q6d1` | If engages in aerobik | `Numeric(Byte)` | `%17.0f` |
| `pl_Q6d2` | If engages in running | `Numeric(Byte)` | `%17.0f` |
| `pl_Q6d3` | If engages in gym | `Numeric(Byte)` | `%17.0f` |
| `pl_Q6d4` | If engages in cycling | `Numeric(Byte)` | `%17.0f` |
| `pl_Q6d5` | If engages in skiing | `Numeric(Byte)` | `%17.0f` |
| `pl_Q6d6` | If engages in swimming | `Numeric(Byte)` | `%17.0f` |
| `pl_Q6d7` | If engages in football | `Numeric(Byte)` | `%17.0f` |
| `pl_Q6d8` | If engages in gardening | `Numeric(Byte)` | `%17.0f` |
| `pl_Q6d9` | If engages in walks | `Numeric(Byte)` | `%17.0f` |
| `pl_Q6d10` | If engages in another physical exercise | `Numeric(Byte)` | `%17.0f` |
| `pl_Q6dno` | If does not engage in any mentioned activity | `Numeric(Byte)` | `%17.0f` |
| `pl_Q7` | How often meets for social purposes | `Numeric(Byte)` | `%32.0f` |
| `pl_Q8d1` | How often reads instructions | `Numeric(Byte)` | `%52.0f` |
| `pl_Q8d2` | How often reads e-mails | `Numeric(Byte)` | `%52.0f` |
| `pl_Q8d3` | How often reads articles in newspapers | `Numeric(Byte)` | `%52.0f` |
| `pl_Q8d4` | How often reads articles in journals | `Numeric(Byte)` | `%52.0f` |
| `pl_Q8d5` | How often reads books | `Numeric(Byte)` | `%52.0f` |
| `pl_Q8d6` | How often reads manuals | `Numeric(Byte)` | `%52.0f` |
| `pl_Q8d7` | How often reads bills | `Numeric(Byte)` | `%52.0f` |
| `pl_Q8d8` | How often reads diagrams | `Numeric(Byte)` | `%52.0f` |
| `pl_Q9d1` | How often writes e-mails | `Numeric(Byte)` | `%52.0f` |
| `pl_Q9d2` | How often writes articles | `Numeric(Byte)` | `%52.0f` |
| `pl_Q9d3` | How often writes reports | `Numeric(Byte)` | `%52.0f` |
| `pl_Q9d4` | How often fills in forms | `Numeric(Byte)` | `%52.0f` |
| `pl_Q10d1` | How often calculates budgets | `Numeric(Byte)` | `%52.0f` |
| `pl_Q10d2` | How often uses fractions | `Numeric(Byte)` | `%52.0f` |
| `pl_Q10d3` | How often uses a calculator | `Numeric(Byte)` | `%52.0f` |
| `pl_Q10d4` | How often prepares charts | `Numeric(Byte)` | `%52.0f` |
| `pl_Q10d5` | How often uses algebra | `Numeric(Byte)` | `%52.0f` |
| `pl_Q10d6` | How often uses advanced math | `Numeric(Byte)` | `%52.0f` |
| `pl_Q11` | If uses a computer/mobile device | `Numeric(Byte)` | `%16.0f` |
| `pl_Q12` | How often used a computer/mobile device | `Numeric(Byte)` | `%52.0f` |
| `pl_Q13` | How often uses the Internet for personal interests | `Numeric(Byte)` | `%52.0f` |
| `pl_Q14d1` | How often uses email | `Numeric(Byte)` | `%52.0f` |
| `pl_Q14d2` | How often uses the Internet to better understand issues | `Numeric(Byte)` | `%52.0f` |
| `pl_Q14d3` | How often conducts transactions on the Internet | `Numeric(Byte)` | `%52.0f` |
| `pl_Q14d4` | How often uses spreadsheets | `Numeric(Byte)` | `%52.0f` |
| `pl_Q14d5` | How often uses a word processor | `Numeric(Byte)` | `%52.0f` |
| `pl_Q14d6` | How often uses a programming language | `Numeric(Byte)` | `%52.0f` |
| `pl_Q14d7` | How often participates in real-time discussions on the Internet | `Numeric(Byte)` | `%52.0f` |
| `pl_Q15a` | If needed to see a doctor but could not because of cost | `Numeric(Byte)` | `%21.0f` |
| `pl_Q15b` | If needed to see a doctor but could not because of waiting | `Numeric(Byte)` | `%21.0f` |
| `pl_Q16` | If postponed visits to the dentist to keep living costs down | `Numeric(Byte)` | `%21.0f` |
| `pl_Q17` | Vandalism or crime is a big problem in this area | `Numeric(Byte)` | `%32.0f` |
| `pl_sample` | Type of sample | `Numeric(Byte)` | `%9.0g` |
| `ro_A1` | Amount in bank account after 5Y with 2% interest rate/year | `Numeric(Byte)` | `%21.0g` |
| `ro_A2` | Amount in bank account after 5Y with 20% interest rate/year | `Numeric(Byte)` | `%21.0g` |
| `ro_A3` | How much could you buy if the interest is 2% and inflation is 2%? | `Numeric(Byte)` | `%21.0g` |
| `ro_A4` | Who is richer: friend inherits X Lei today vs sibling inherits X Lei in 3 years | `Numeric(Byte)` | `%21.0g` |
| `ro_A5` | How much will you be able to buy in 2020 if both income and prices double? | `Numeric(Byte)` | `%21.0g` |
| `ro_B1` | Which statement describes the main function of the stock market? | `Numeric(Byte)` | `%83.0g` |
| `ro_B2` | If somebody buys the stock of firm B in the stock market: | `Numeric(Byte)` | `%31.0g` |
| `ro_B3` | Which statement about mutual funds is correct? | `Numeric(Byte)` | `%86.0g` |
| `ro_B4` | What happens if somebody buys a bond of firm B? | `Numeric(Byte)` | `%33.0g` |
| `ro_B5` | Which asset normally gives the highest return on long term (10-20 years)? | `Numeric(Byte)` | `%21.0g` |
| `ro_B6` | Which asset displays the highest fluctuations over time | `Numeric(Byte)` | `%21.0g` |
| `ro_B7` | Spreading money among different assets, the risk of losing money ... | `Numeric(Byte)` | `%21.0g` |
| `ro_B8` | Cannot sell a 10-year bond after 5 years without incurring a penalty | `Numeric(Byte)` | `%21.0g` |
| `ro_B9` | Stocks are normally riskier than bonds. True or false? | `Numeric(Byte)` | `%21.0g` |
| `ro_B10` | Buying a company fund usually provides a safer return than a stock mutual | `Numeric(Byte)` | `%21.0g` |
| `ro_B11` | If the interest rate falls, what should happen to bond prices? | `Numeric(Byte)` | `%21.0g` |
| `ro_D1` | I am a person who is willing to take risks | `Numeric(Byte)` | `%17.0g` |
| `ro_D2` | I rather go without something today in order to be able to afford more tomorrow | `Numeric(Byte)` | `%17.0g` |
| `ro_D3` | I tend to procrastinate | `Numeric(Byte)` | `%17.0g` |
| `ro_D4` | I am prepared to spend now and let the future take care of itself | `Numeric(Byte)` | `%17.0g` |
| `ro_D5` | For me, money is a tool to accomplish goals | `Numeric(Byte)` | `%17.0g` |
| `ro_D6` | Motto: Money gives me the freedom to do what I feel like | `Numeric(Byte)` | `%17.0g` |
| `ro_D7` | For me, money is a tool to make friends | `Numeric(Byte)` | `%17.0g` |
| `ro_D8` | I am prepared to do what it takes to get money | `Numeric(Byte)` | `%17.0g` |
| `ro_D9` | Financial matters are complicated | `Numeric(Byte)` | `%17.0g` |
| `ro_E1` | Family related person who work abroad | `Numeric(Byte)` | `%10.0g` |
| `ro_E2` | Sending money to you | `Numeric(Byte)` | `%14.0g` |
| `ro_E3` | Frequency of sending money | `Numeric(Byte)` | `%19.0g` |
| `ro_E4` | The amount you usually spend | `Numeric(Byte)` | `%19.0g` |
| `ro_F` | Risk - coin flip: choose 1 out of 6 options | `Numeric(Byte)` | `%14.0g` |
| `ro_G1` | Money allocated to option 1 (receive today) | `Numeric(Byte)` | `%10.0g` |
| `ro_G2` | Money allocated to option 2 (receive doubled in 4 weeks) | `Numeric(Byte)` | `%10.0g` |
| `si_q1need_1` | Need help: dressing, including shoes and socks | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_1` | Receive help: dressing, including shoes and socks | `Numeric(Byte)` | `%46.0g` |
| `si_q1need_2` | Need help: walking across a room | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_2` | Receive help: walking across a room | `Numeric(Byte)` | `%46.0g` |
| `si_q1need_3` | Need help: bathing or showering | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_3` | Receive help: bathing or showering | `Numeric(Byte)` | `%46.0g` |
| `si_q1need_4` | Need help: eating, cutting up food | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_4` | Receive help: eating, cutting up food | `Numeric(Byte)` | `%46.0g` |
| `si_q1need_5` | Need help: getting in or out of bed | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_5` | Receive help: getting in or out of bed | `Numeric(Byte)` | `%46.0g` |
| `si_q1need_6` | Need help: using the toilet, incl. getting up or down | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_6` | Receive help: using the toilet, incl. getting up or down | `Numeric(Byte)` | `%46.0g` |
| `si_q1need_7` | Need help: using a map in a strange place | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_7` | Receive help: using a map in a strange place | `Numeric(Byte)` | `%46.0g` |
| `si_q1need_8` | Need help: preparing a hot meal | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_8` | Receive help: preparing a hot meal | `Numeric(Byte)` | `%46.0g` |
| `si_q1need_9` | Need help: shopping for groceries | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_9` | Receive help: shopping for groceries | `Numeric(Byte)` | `%46.0g` |
| `si_q1need_10` | Need help: telephone calls | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_10` | Receive help: telephone calls | `Numeric(Byte)` | `%46.0g` |
| `si_q1need_11` | Need help: taking medications | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_11` | Receive help: taking medications | `Numeric(Byte)` | `%46.0g` |
| `si_q1need_12` | Need help: doing work around the house or garden | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_12` | Receive help: doing work around the house or garden | `Numeric(Byte)` | `%46.0g` |
| `si_q1need_13` | Need help: managing money | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_13` | Receive help: managing money | `Numeric(Byte)` | `%46.0g` |
| `si_q1need_14` | Need help: leaving the house independently/accessing transportation | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_14` | Receive help: leaving the house independently/accessing transportation | `Numeric(Byte)` | `%46.0g` |
| `si_q1need_15` | Need help: doing personal laundry | `Numeric(Byte)` | `%43.0g` |
| `si_q1rcv_15` | Receive help: doing personal laundry | `Numeric(Byte)` | `%46.0g` |
| `si_q2` | Filter: proxy interview | `Numeric(Byte)` | `%10.0g` |
| `si_q3` | Filter: age=<70 | `Numeric(Byte)` | `%10.0g` |
| `si_q4a` | Retire later, if: a bonus in addition to your salary | `Numeric(Byte)` | `%29.0g` |
| `si_q4b` | Retire later, if: additional pension during retirement | `Numeric(Byte)` | `%29.0g` |
| `si_q4c` | Retire later, if: more flexible working hours | `Numeric(Byte)` | `%29.0g` |
| `si_q4d` | Retire later, if: working conditions adjusted to reduced working ability | `Numeric(Byte)` | `%29.0g` |
| `si_q4e` | Retire later, if: more help from colleagues/superiors | `Numeric(Byte)` | `%29.0g` |
| `si_q4f` | Retire later, if: more training in relation to work | `Numeric(Byte)` | `%29.0g` |
| `si_q4g` | Retire later, if: less demanding work | `Numeric(Byte)` | `%29.0g` |
| `si_q4h` | Retire later, if: superiors supported your intention | `Numeric(Byte)` | `%29.0g` |
| `si_q4i` | Retire later, if: colleagues supported your intention | `Numeric(Byte)` | `%29.0g` |
| `si_q4j` | Simply would not work longer | `Numeric(Byte)` | `%29.0g` |
| `si_q5a` | Employment satisfaction: fell respected by my immediate superior | `Numeric(Byte)` | `%29.0g` |
| `si_q5b` | Employment satisfaction: have enough time to do my job | `Numeric(Byte)` | `%29.0g` |
| `si_q5c` | Employment satisfaction: have difficulty due to health limitations | `Numeric(Byte)` | `%29.0g` |
| `si_q5d` | Employment satisfaction: employer appreciates my experience | `Numeric(Byte)` | `%29.0g` |
| `si_q5e` | Employment satisfaction: can influence decisions relevant to my work | `Numeric(Byte)` | `%29.0g` |
| `si_q5f` | Employment satisfaction: my ability to work has reduced | `Numeric(Byte)` | `%29.0g` |
| `si_q5g` | Employment satisfaction: often feel discriminated against | `Numeric(Byte)` | `%29.0g` |
| `si_q5h` | Employment satisfaction: can balance my family and work life | `Numeric(Byte)` | `%29.0g` |
| `si_q5i` | Employment satisfaction: feel satisfied knowing that I do my job well | `Numeric(Byte)` | `%29.0g` |
| `si_q6` | Filter: (self)employed on a regular basis | `Numeric(Byte)` | `%10.0g` |
| `si_q7a` | Taken care of partner/parent over the past 12 months? | `Numeric(Byte)` | `%33.0g` |
| `si_q7b` | Balance work and care for partner/parent | `Numeric(Byte)` | `%14.0g` |
| `si_q8` | How many hours a week would you work? | `Numeric(Byte)` | `%44.0g` |
| `si_q9` | I would postpone retirement for â€¦ | `Numeric(Byte)` | `%14.0g` |

### `technical_variables` - Technical variables

- Dataset: `sharew8_rel9-0-0_technical_variables.dta`
- Read with: `ps.read_share_module("technical_variables", wave=8)`
- Rows: 53,695
- Variables: 19
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `fam_resp` | Family respondent | `Numeric(Byte)` | `%21.0g` |
| `fin_resp` | Financial respondent | `Numeric(Byte)` | `%24.0g` |
| `hou_resp` | Household respondent | `Numeric(Byte)` | `%24.0g` |
| `mn005_` | Single or couple interview | `Numeric(Byte)` | `%40.0g` |
| `mn024_` | Nursing home interview | `Numeric(Byte)` | `%20.0g` |
| `mn026_` | First respondent from couple or single | `Numeric(Byte)` | `%10.0g` |
| `mn029_` | Eligible for linkage | `Numeric(Byte)` | `%16.0g` |
| `mn032_` | Eligible for social exclusion items | `Numeric(Byte)` | `%10.0g` |
| `mn038_` | Eligible for Accelerometry | `Numeric(Byte)` | `%10.0g` |
| `mn040_` | Need to ask consent question (ex123) | `Numeric(Byte)` | `%10.0g` |
| `mn041_` | Need to ask retirement info | `Numeric(Byte)` | `%10.0g` |
| `mn101_` | Questionnaire version | `Numeric(Byte)` | `%26.0g` |
| `mn104_` | Household moved | `Numeric(Byte)` | `%10.0g` |


## Generated Modules

### `gv_accelerometer_day` - Accelerometer day-level dataset

- Dataset: `sharew8_rel9-0-0_gv_accelerometer_day.dta`
- Read with: `ps.read_share_module("gv_accelerometer_day", wave=8)`
- Rows: 5,945
- Variables: 320
- Key hint: `mergeid` + `measurementday`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `month` | Month of measurement | `Numeric(Byte)` | `%10.0g` |
| `year` | Year of measurement | `Numeric(Int)` | `%9.0g` |
| `measurementday` | Consecutive days of wear time | `Numeric(Byte)` | `%9.0g` |
| `weekday` | Weekday | `Numeric(Byte)` | `%10.0g` |
| `device_id` | Device ID | `Numeric(Float)` | `%9.0g` |
| `frequency` | Sampling frequency | `Numeric(Byte)` | `%9.0g` |
| `position` | Wearing position: Left or right thigh | `Numeric(Byte)` | `%10.0g` |
| `reported_N_valid_hours_day` | Wear time reported by respondent | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_N_valid_hours_day` | ActiPASS detected valid hours per day | `Numeric(Float)` | `%9.0g` |
| `GGIR_N_valid_hours_day` | GGIR detected valid hours per day | `Numeric(Double)` | `%9.0g` |
| `OxCGRT_stay_at_home` | OxCGRT stay at home requirements (mode over observation time by person) | `Numeric(Byte)` | `%128.0g` |
| `OxCGRT_stringency_index` | OxCGRT stringency index (mean over observation time by person) | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_QC_day` | ActiPASS Check: Any warning | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_NoSleepInt_day` | ActiPASS Check: No sleep interval | `Numeric(Byte)` | `%8.0g` |
| `ActiPASS_NoWalk_day` | ActiPASS Check: < 30 sec walking | `Numeric(Byte)` | `%8.0g` |
| `ActiPASS_TooMuchBedtime_day` | ActiPASS Check: > 16 h bedtime | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_TooMuchOther_day` | ActiPASS Check: > 30 min other | `Numeric(Byte)` | `%8.0g` |
| `ActiPASS_TooMuchStair_day` | ActiPASS Check: > 120 min stair | `Numeric(Byte)` | `%8.0g` |
| `ActiPASS_Bedtime_day` | The time within this calendar day which is flagged as belonging to a bedtime | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_LieStill_day` | The total time of possible sleep outside a bedtime | `Numeric(Byte)` | `%8.0g` |
| `ActiPASS_Sleep_day` | Total sleep time of this calendar day | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_SleepInterval_day` | The time of this calendar day which is flagged as belonging to a sleep-interval | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Awake_day` | The time of this calendar day which is not flagged as belonging to a sleep-inter | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Walk_Slow_day` | Time of walking with a cadence lower than 100 | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Walk_Fast_day` | Time of walking with a cadence equal or higher than 100 | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Lie_day` | Time of lying | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Sit_day` | Time of sitting | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_SitLie_day` | Time of sitting or lying | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Stand_day` | Time of standing | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Move_day` | The time of 'move' | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_StandMove_day` | Time of standing or moving | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Walk_day` | Time of walking | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Run_day` | Time of running | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Stair_day` | Time of stair-walking (all stair walking like activities) | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Cycle_day` | Time of cycling | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Upright_day` | Time of all upright activities/postures (i.e. Stand + Move + Walk + Run + Stair) | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Other_day` | Time of activities in 'Other' postures/activities | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_NonWear_day` | Non-wear time | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_INT1_day` | Time spent on activities classified as sedentary | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_INT2_day` | Time spent on activities classified as low physical activity | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_INT3_day` | Time spent on activities classified as moderate physical activity | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_INT4_day` | Time spent on activities classified as vigorousÂ  physical activity | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_INT34_day` | Time spent on activities classified as moderate and vigorousÂ physical activity | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Steps_day` | Total number of steps | `Numeric(Long)` | `%8.0g` |
| `GGIR_mean_ENMO_day` | Mean ENMO | `Numeric(Double)` | `%9.0g` |
| `GGIR_ig_rsquared_ENMO_day` | IG R-squared | `Numeric(Double)` | `%9.0g` |
| `GGIR_ig_gradient_ENMO_day` | IG Gradient | `Numeric(Double)` | `%9.0g` |
| `GGIR_ig_intercept_ENMO_day` | IG Intercept | `Numeric(Double)` | `%9.0g` |
| `GGIR_0_25_ENMO_day` | Minutes in ENMO Level: [0-25) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_25_50_ENMO_day` | Minutes in ENMO Level: [25-50) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_50_75_ENMO_day` | Minutes in ENMO Level: [50-75) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_75_100_ENMO_day` | Minutes in ENMO Level: [75-100) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_100_125_ENMO_day` | Minutes in ENMO Level: [100-125) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_125_150_ENMO_day` | Minutes in ENMO Level: [125-150) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_150_175_ENMO_day` | Minutes in ENMO Level: [150-175) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_175_200_ENMO_day` | Minutes in ENMO Level: [175-200) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_200_225_ENMO_day` | Minutes in ENMO Level: [200-225) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_225_250_ENMO_day` | Minutes in ENMO Level: [225-250) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_250_275_ENMO_day` | Minutes in ENMO Level: [250-275) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_275_300_ENMO_day` | Minutes in ENMO Level: [275-300) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_300_325_ENMO_day` | Minutes in ENMO Level: [300-325) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_325_350_ENMO_day` | Minutes in ENMO Level: [325-350) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_350_375_ENMO_day` | Minutes in ENMO Level: [350-375) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_375_400_ENMO_day` | Minutes in ENMO Level: [375-400) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_400_425_ENMO_day` | Minutes in ENMO Level: [400-425) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_425_450_ENMO_day` | Minutes in ENMO Level: [425-450) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_450_475_ENMO_day` | Minutes in ENMO Level: [450-475) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_475_500_ENMO_day` | Minutes in ENMO Level: [475-500) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_500_525_ENMO_day` | Minutes in ENMO Level: [500-525) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_525_550_ENMO_day` | Minutes in ENMO Level: [525-550) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_550_575_ENMO_day` | Minutes in ENMO Level: [550-575) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_575_600_ENMO_day` | Minutes in ENMO Level: [575-600) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_600_625_ENMO_day` | Minutes in ENMO Level: [600-625) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_625_650_ENMO_day` | Minutes in ENMO Level: [625-650) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_650_675_ENMO_day` | Minutes in ENMO Level: [650-675) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_675_700_ENMO_day` | Minutes in ENMO Level: [675-700) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_700_725_ENMO_day` | Minutes in ENMO Level: [700-725) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_725_750_ENMO_day` | Minutes in ENMO Level: [725-750) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_750_775_ENMO_day` | Minutes in ENMO Level: [750-775) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_775_800_ENMO_day` | Minutes in ENMO Level: [775-800) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_800_825_ENMO_day` | Minutes in ENMO Level: [800-825) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_825_850_ENMO_day` | Minutes in ENMO Level: [825-850) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_850_875_ENMO_day` | Minutes in ENMO Level: [850-875) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_875_900_ENMO_day` | Minutes in ENMO Level: [875-900) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_900_925_ENMO_day` | Minutes in ENMO Level: [900-925) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_925_950_ENMO_day` | Minutes in ENMO Level: [925-950) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_950_975_ENMO_day` | Minutes in ENMO Level: [950-975) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_975_1000_ENMO_day` | Minutes in ENMO Level: [975-1000) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1000_1025_ENMO_day` | Minutes in ENMO Level: [1000-1025) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1025_1050_ENMO_day` | Minutes in ENMO Level: [1025-1050) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1050_1075_ENMO_day` | Minutes in ENMO Level: [1050-1075) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1075_1100_ENMO_day` | Minutes in ENMO Level: [1075-1100) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1100_1125_ENMO_day` | Minutes in ENMO Level: [1100-1125) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1125_1150_ENMO_day` | Minutes in ENMO Level: [1125-1150) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1150_1175_ENMO_day` | Minutes in ENMO Level: [1150-1175) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1175_1200_ENMO_day` | Minutes in ENMO Level: [1175-1200) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1200_1225_ENMO_day` | Minutes in ENMO Level: [1200-1225) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1225_1250_ENMO_day` | Minutes in ENMO Level: [1225-1250) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1250_1275_ENMO_day` | Minutes in ENMO Level: [1250-1275) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1275_1300_ENMO_day` | Minutes in ENMO Level: [1275-1300) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1300_1325_ENMO_day` | Minutes in ENMO Level: [1300-1325) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1325_1350_ENMO_day` | Minutes in ENMO Level: [1325-1350) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1350_1375_ENMO_day` | Minutes in ENMO Level: [1350-1375) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1375_1400_ENMO_day` | Minutes in ENMO Level: [1375-1400) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1400_1425_ENMO_day` | Minutes in ENMO Level: [1400-1425) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1425_1450_ENMO_day` | Minutes in ENMO Level: [1425-1450) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1450_1475_ENMO_day` | Minutes in ENMO Level: [1450-1475) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1475_1500_ENMO_day` | Minutes in ENMO Level: [1475-1500) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1500_1525_ENMO_day` | Minutes in ENMO Level: [1500-1525) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1525_1550_ENMO_day` | Minutes in ENMO Level: [1525-1550) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1550_1575_ENMO_day` | Minutes in ENMO Level: [1550-1575) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1575_1600_ENMO_day` | Minutes in ENMO Level: [1575-1600) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1600_1625_ENMO_day` | Minutes in ENMO Level: [1600-1625) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1625_1650_ENMO_day` | Minutes in ENMO Level: [1625-1650) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1650_1675_ENMO_day` | Minutes in ENMO Level: [1650-1675) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1675_1700_ENMO_day` | Minutes in ENMO Level: [1675-1700) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1700_1725_ENMO_day` | Minutes in ENMO Level: [1700-1725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_1725_1750_ENMO_day` | Minutes in ENMO Level: [1725-1750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_1750_1775_ENMO_day` | Minutes in ENMO Level: [1750-1775) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1775_1800_ENMO_day` | Minutes in ENMO Level: [1775-1800) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1800_1825_ENMO_day` | Minutes in ENMO Level: [1800-1825) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1825_1850_ENMO_day` | Minutes in ENMO Level: [1825-1850) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1850_1875_ENMO_day` | Minutes in ENMO Level: [1850-1875) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1875_1900_ENMO_day` | Minutes in ENMO Level: [1875-1900) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1900_1925_ENMO_day` | Minutes in ENMO Level: [1900-1925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_1925_1950_ENMO_day` | Minutes in ENMO Level: [1925-1950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_1950_1975_ENMO_day` | Minutes in ENMO Level: [1950-1975) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1975_2000_ENMO_day` | Minutes in ENMO Level: [1975-2000) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2000_2025_ENMO_day` | Minutes in ENMO Level: [2000-2025) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2025_2050_ENMO_day` | Minutes in ENMO Level: [2025-2050) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2050_2075_ENMO_day` | Minutes in ENMO Level: [2050-2075) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2075_2100_ENMO_day` | Minutes in ENMO Level: [2075-2100) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2100_2125_ENMO_day` | Minutes in ENMO Level: [2100-2125) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2125_2150_ENMO_day` | Minutes in ENMO Level: [2125-2150) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2150_2175_ENMO_day` | Minutes in ENMO Level: [2150-2175) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2175_2200_ENMO_day` | Minutes in ENMO Level: [2175-2200) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2200_2225_ENMO_day` | Minutes in ENMO Level: [2200-2225) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2225_2250_ENMO_day` | Minutes in ENMO Level: [2225-2250) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2250_2275_ENMO_day` | Minutes in ENMO Level: [2250-2275) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2275_2300_ENMO_day` | Minutes in ENMO Level: [2275-2300) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2300_2325_ENMO_day` | Minutes in ENMO Level: [2300-2325) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2325_2350_ENMO_day` | Minutes in ENMO Level: [2325-2350) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2350_2375_ENMO_day` | Minutes in ENMO Level: [2350-2375) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2375_2400_ENMO_day` | Minutes in ENMO Level: [2375-2400) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2400_2425_ENMO_day` | Minutes in ENMO Level: [2400-2425) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2425_2450_ENMO_day` | Minutes in ENMO Level: [2425-2450) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2450_2475_ENMO_day` | Minutes in ENMO Level: [2450-2475) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2475_2500_ENMO_day` | Minutes in ENMO Level: [2475-2500) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2500_2525_ENMO_day` | Minutes in ENMO Level: [2500-2525) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2525_2550_ENMO_day` | Minutes in ENMO Level: [2525-2550) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2550_2575_ENMO_day` | Minutes in ENMO Level: [2550-2575) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2575_2600_ENMO_day` | Minutes in ENMO Level: [2575-2600) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2600_2625_ENMO_day` | Minutes in ENMO Level: [2600-2625) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2625_2650_ENMO_day` | Minutes in ENMO Level: [2625-2650) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2650_2675_ENMO_day` | Minutes in ENMO Level: [2650-2675) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2675_2700_ENMO_day` | Minutes in ENMO Level: [2675-2700) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2700_2725_ENMO_day` | Minutes in ENMO Level: [2700-2725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2725_2750_ENMO_day` | Minutes in ENMO Level: [2725-2750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2750_2775_ENMO_day` | Minutes in ENMO Level: [2750-2775) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2775_2800_ENMO_day` | Minutes in ENMO Level: [2775-2800) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2800_2825_ENMO_day` | Minutes in ENMO Level: [2800-2825) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2825_2850_ENMO_day` | Minutes in ENMO Level: [2825-2850) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2850_2875_ENMO_day` | Minutes in ENMO Level: [2850-2875) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2875_2900_ENMO_day` | Minutes in ENMO Level: [2875-2900) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2900_2925_ENMO_day` | Minutes in ENMO Level: [2900-2925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2925_2950_ENMO_day` | Minutes in ENMO Level: [2925-2950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2950_2975_ENMO_day` | Minutes in ENMO Level: [2950-2975) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2975_3000_ENMO_day` | Minutes in ENMO Level: [2975-3000) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3000_3025_ENMO_day` | Minutes in ENMO Level: [3000-3025) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3025_3050_ENMO_day` | Minutes in ENMO Level: [3025-3050) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3050_3075_ENMO_day` | Minutes in ENMO Level: [3050-3075) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3075_3100_ENMO_day` | Minutes in ENMO Level: [3075-3100) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3100_3125_ENMO_day` | Minutes in ENMO Level: [3100-3125) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3125_3150_ENMO_day` | Minutes in ENMO Level: [3125-3150) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3150_3175_ENMO_day` | Minutes in ENMO Level: [3150-3175) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3175_3200_ENMO_day` | Minutes in ENMO Level: [3175-3200) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3200_3225_ENMO_day` | Minutes in ENMO Level: [3200-3225) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3225_3250_ENMO_day` | Minutes in ENMO Level: [3225-3250) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3250_3275_ENMO_day` | Minutes in ENMO Level: [3250-3275) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3275_3300_ENMO_day` | Minutes in ENMO Level: [3275-3300) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3300_3325_ENMO_day` | Minutes in ENMO Level: [3300-3325) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3325_3350_ENMO_day` | Minutes in ENMO Level: [3325-3350) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3350_3375_ENMO_day` | Minutes in ENMO Level: [3350-3375) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3375_3400_ENMO_day` | Minutes in ENMO Level: [3375-3400) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3400_3425_ENMO_day` | Minutes in ENMO Level: [3400-3425) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3425_3450_ENMO_day` | Minutes in ENMO Level: [3425-3450) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3450_3475_ENMO_day` | Minutes in ENMO Level: [3450-3475) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3475_3500_ENMO_day` | Minutes in ENMO Level: [3475-3500) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3500_3525_ENMO_day` | Minutes in ENMO Level: [3500-3525) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3525_3550_ENMO_day` | Minutes in ENMO Level: [3525-3550) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3550_3575_ENMO_day` | Minutes in ENMO Level: [3550-3575) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3575_3600_ENMO_day` | Minutes in ENMO Level: [3575-3600) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3600_3625_ENMO_day` | Minutes in ENMO Level: [3600-3625) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3625_3650_ENMO_day` | Minutes in ENMO Level: [3625-3650) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3650_3675_ENMO_day` | Minutes in ENMO Level: [3650-3675) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3675_3700_ENMO_day` | Minutes in ENMO Level: [3675-3700) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3700_3725_ENMO_day` | Minutes in ENMO Level: [3700-3725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3725_3750_ENMO_day` | Minutes in ENMO Level: [3725-3750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3750_3775_ENMO_day` | Minutes in ENMO Level: [3750-3775) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3775_3800_ENMO_day` | Minutes in ENMO Level: [3775-3800) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3800_3825_ENMO_day` | Minutes in ENMO Level: [3800-3825) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3825_3850_ENMO_day` | Minutes in ENMO Level: [3825-3850) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3850_3875_ENMO_day` | Minutes in ENMO Level: [3850-3875) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3875_3900_ENMO_day` | Minutes in ENMO Level: [3875-3900) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3900_3925_ENMO_day` | Minutes in ENMO Level: [3900-3925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3925_3950_ENMO_day` | Minutes in ENMO Level: [3925-3950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3950_3975_ENMO_day` | Minutes in ENMO Level: [3950-3975) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3975_4000_ENMO_day` | Minutes in ENMO Level: [3975-4000) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4000_4025_ENMO_day` | Minutes in ENMO Level: [4000-4025) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4025_4050_ENMO_day` | Minutes in ENMO Level: [4025-4050) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4050_4075_ENMO_day` | Minutes in ENMO Level: [4050-4075) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4075_4100_ENMO_day` | Minutes in ENMO Level: [4075-4100) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4100_4125_ENMO_day` | Minutes in ENMO Level: [4100-4125) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4125_4150_ENMO_day` | Minutes in ENMO Level: [4125-4150) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4150_4175_ENMO_day` | Minutes in ENMO Level: [4150-4175) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4175_4200_ENMO_day` | Minutes in ENMO Level: [4175-4200) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4200_4225_ENMO_day` | Minutes in ENMO Level: [4200-4225) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4225_4250_ENMO_day` | Minutes in ENMO Level: [4225-4250) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4250_4275_ENMO_day` | Minutes in ENMO Level: [4250-4275) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4275_4300_ENMO_day` | Minutes in ENMO Level: [4275-4300) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4300_4325_ENMO_day` | Minutes in ENMO Level: [4300-4325) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4325_4350_ENMO_day` | Minutes in ENMO Level: [4325-4350) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4350_4375_ENMO_day` | Minutes in ENMO Level: [4350-4375) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4375_4400_ENMO_day` | Minutes in ENMO Level: [4375-4400) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4400_4425_ENMO_day` | Minutes in ENMO Level: [4400-4425) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4425_4450_ENMO_day` | Minutes in ENMO Level: [4425-4450) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4450_4475_ENMO_day` | Minutes in ENMO Level: [4450-4475) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4475_4500_ENMO_day` | Minutes in ENMO Level: [4475-4500) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4500_4525_ENMO_day` | Minutes in ENMO Level: [4500-4525) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4525_4550_ENMO_day` | Minutes in ENMO Level: [4525-4550) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4550_4575_ENMO_day` | Minutes in ENMO Level: [4550-4575) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4575_4600_ENMO_day` | Minutes in ENMO Level: [4575-4600) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4600_4625_ENMO_day` | Minutes in ENMO Level: [4600-4625) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4625_4650_ENMO_day` | Minutes in ENMO Level: [4625-4650) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4650_4675_ENMO_day` | Minutes in ENMO Level: [4650-4675) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4675_4700_ENMO_day` | Minutes in ENMO Level: [4675-4700) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4700_4725_ENMO_day` | Minutes in ENMO Level: [4700-4725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4725_4750_ENMO_day` | Minutes in ENMO Level: [4725-4750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4750_4775_ENMO_day` | Minutes in ENMO Level: [4750-4775) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4775_4800_ENMO_day` | Minutes in ENMO Level: [4775-4800) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4800_4825_ENMO_day` | Minutes in ENMO Level: [4800-4825) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4825_4850_ENMO_day` | Minutes in ENMO Level: [4825-4850) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4850_4875_ENMO_day` | Minutes in ENMO Level: [4850-4875) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4875_4900_ENMO_day` | Minutes in ENMO Level: [4875-4900) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4900_4925_ENMO_day` | Minutes in ENMO Level: [4900-4925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4925_4950_ENMO_day` | Minutes in ENMO Level: [4925-4950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4950_4975_ENMO_day` | Minutes in ENMO Level: [4950-4975) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4975_5000_ENMO_day` | Minutes in ENMO Level: [4975-5000) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5000_5025_ENMO_day` | Minutes in ENMO Level: [5000-5025) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5025_5050_ENMO_day` | Minutes in ENMO Level: [5025-5050) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5050_5075_ENMO_day` | Minutes in ENMO Level: [5050-5075) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5075_5100_ENMO_day` | Minutes in ENMO Level: [5075-5100) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5100_5125_ENMO_day` | Minutes in ENMO Level: [5100-5125) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5125_5150_ENMO_day` | Minutes in ENMO Level: [5125-5150) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5150_5175_ENMO_day` | Minutes in ENMO Level: [5150-5175) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5175_5200_ENMO_day` | Minutes in ENMO Level: [5175-5200) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5200_5225_ENMO_day` | Minutes in ENMO Level: [5200-5225) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5225_5250_ENMO_day` | Minutes in ENMO Level: [5225-5250) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5250_5275_ENMO_day` | Minutes in ENMO Level: [5250-5275) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5275_5300_ENMO_day` | Minutes in ENMO Level: [5275-5300) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5300_5325_ENMO_day` | Minutes in ENMO Level: [5300-5325) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5325_5350_ENMO_day` | Minutes in ENMO Level: [5325-5350) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5350_5375_ENMO_day` | Minutes in ENMO Level: [5350-5375) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5375_5400_ENMO_day` | Minutes in ENMO Level: [5375-5400) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5400_5425_ENMO_day` | Minutes in ENMO Level: [5400-5425) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5425_5450_ENMO_day` | Minutes in ENMO Level: [5425-5450) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5450_5475_ENMO_day` | Minutes in ENMO Level: [5450-5475) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5475_5500_ENMO_day` | Minutes in ENMO Level: [5475-5500) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5500_5525_ENMO_day` | Minutes in ENMO Level: [5500-5525) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5525_5550_ENMO_day` | Minutes in ENMO Level: [5525-5550) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5550_5575_ENMO_day` | Minutes in ENMO Level: [5550-5575) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5575_5600_ENMO_day` | Minutes in ENMO Level: [5575-5600) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5600_5625_ENMO_day` | Minutes in ENMO Level: [5600-5625) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5625_5650_ENMO_day` | Minutes in ENMO Level: [5625-5650) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5650_5675_ENMO_day` | Minutes in ENMO Level: [5650-5675) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5675_5700_ENMO_day` | Minutes in ENMO Level: [5675-5700) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5700_5725_ENMO_day` | Minutes in ENMO Level: [5700-5725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5725_5750_ENMO_day` | Minutes in ENMO Level: [5725-5750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5750_5775_ENMO_day` | Minutes in ENMO Level: [5750-5775) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5775_5800_ENMO_day` | Minutes in ENMO Level: [5775-5800) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5800_5825_ENMO_day` | Minutes in ENMO Level: [5800-5825) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5825_5850_ENMO_day` | Minutes in ENMO Level: [5825-5850) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5850_5875_ENMO_day` | Minutes in ENMO Level: [5850-5875) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5875_5900_ENMO_day` | Minutes in ENMO Level: [5875-5900) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5900_5925_ENMO_day` | Minutes in ENMO Level: [5900-5925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5925_5950_ENMO_day` | Minutes in ENMO Level: [5925-5950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5950_5975_ENMO_day` | Minutes in ENMO Level: [5950-5975) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5975_6000_ENMO_day` | Minutes in ENMO Level: [5975-6000) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_6000_15000_ENMO_day` | Minutes in ENMO Level: [6000-15000) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_L05_hr` | Least active 0.5 hour: Time started | `Numeric(Double)` | `%9.0g` |
| `GGIR_L05_mean_ENMO` | Least active 0.5 hour: Mean ENMO | `Numeric(Double)` | `%9.0g` |
| `GGIR_M05_hr` | Most active 0.5 hour: Time started | `Numeric(Double)` | `%9.0g` |
| `GGIR_M05_mean_ENMO` | Most active 0.5 hour: Mean ENMO | `Numeric(Double)` | `%9.0g` |
| `GGIR_L1_hr` | Least active 1 hour: Time started | `Numeric(Double)` | `%9.0g` |
| `GGIR_L1_mean_ENMO` | Least active 1 hour: Mean ENMO | `Numeric(Double)` | `%9.0g` |
| `GGIR_M1_hr` | Most active 1 hour: Time started | `Numeric(Double)` | `%9.0g` |
| `GGIR_M1_mean_ENMO` | Most active 1 hour: Mean ENMO | `Numeric(Double)` | `%9.0g` |
| `GGIR_L2_hr` | Least active 2 hours: Time started | `Numeric(Double)` | `%9.0g` |
| `GGIR_L2_mean_ENMO` | Least active 2 hours: Mean ENMO | `Numeric(Double)` | `%9.0g` |
| `GGIR_M2_hr` | Most active 2 hours: Time started | `Numeric(Double)` | `%9.0g` |
| `GGIR_M2_mean_ENMO` | Most active 2 hours: Mean ENMO | `Numeric(Double)` | `%9.0g` |
| `GGIR_L5_hr` | Least active 5 hours: Time started | `Numeric(Double)` | `%9.0g` |
| `GGIR_L5_mean_ENMO` | Least active 5 hours: Mean ENMO | `Numeric(Double)` | `%9.0g` |
| `GGIR_M5_hr` | Most active 5 hours: Time started | `Numeric(Double)` | `%9.0g` |
| `GGIR_M5_mean_ENMO` | Most active 5 hours: Mean ENMO | `Numeric(Double)` | `%9.0g` |
| `GGIR_L8_hr` | Least active 8 hours: Time started | `Numeric(Double)` | `%9.0g` |
| `GGIR_L8_mean_ENMO` | Least active 8 hours: Mean ENMO | `Numeric(Double)` | `%9.0g` |
| `GGIR_M8_hr` | Most active 8 hours: Time started | `Numeric(Double)` | `%9.0g` |
| `GGIR_M8_mean_ENMO` | Most active 8 hours: Mean ENMO | `Numeric(Double)` | `%9.0g` |
| `GGIR_L10_hr` | Least active 10 hours: Time started | `Numeric(Double)` | `%9.0g` |
| `GGIR_L10_mean_ENMO` | Least active 10 hours: Mean ENMO | `Numeric(Double)` | `%9.0g` |
| `GGIR_M10_hr` | Most active 10 hours: Time started | `Numeric(Double)` | `%9.0g` |
| `GGIR_M10_mean_ENMO` | Most active 10 hours: Mean ENMO | `Numeric(Double)` | `%9.0g` |
| `GGIR_L16_hr` | Least active 16 hours: Time started | `Numeric(Double)` | `%9.0g` |
| `GGIR_L16_mean_ENMO` | Least active 16 hours: Mean ENMO | `Numeric(Double)` | `%9.0g` |
| `GGIR_M16_hr` | Most active 16 hours: Time started | `Numeric(Double)` | `%9.0g` |
| `GGIR_M16_mean_ENMO` | Most active 16 hours: Mean ENMO | `Numeric(Double)` | `%9.0g` |

### `gv_accelerometer_hour` - Accelerometer hour-level dataset

- Dataset: `sharew8_rel9-0-0_gv_accelerometer_hour.dta`
- Read with: `ps.read_share_module("gv_accelerometer_hour", wave=8)`
- Rows: 142,680
- Variables: 281
- Key hint: `mergeid` + hour-level repeated rows

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `month` | Month of measurement | `Numeric(Byte)` | `%10.0g` |
| `year` | Year of measurement | `Numeric(Int)` | `%9.0g` |
| `weekday` | Weekday | `Numeric(Byte)` | `%10.0g` |
| `measurementday` | Consecutive days of wear time | `Numeric(Byte)` | `%9.0g` |
| `hour` | Hour | `Numeric(Byte)` | `%10.0g` |
| `GGIR_N_valid_hours_hour` | GGIR detected valid hours per hour | `Numeric(Double)` | `%9.0g` |
| `GGIR_N_valid_hours_day` | GGIR detected valid hours per day | `Numeric(Double)` | `%9.0g` |
| `GGIR_N_valid_days` | Number of valid days detected by GGIR | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_N_valid_hours_day` | ActiPASS detected valid hours per day | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_N_valid_days` | ActiPASS detected valid days | `Numeric(Byte)` | `%9.0g` |
| `OxCGRT_stay_at_home` | OxCGRT stay at home requirements (mode over observation time by person) | `Numeric(Byte)` | `%128.0g` |
| `OxCGRT_stringency_index` | OxCGRT stringency index (mean over observation time by person) | `Numeric(Byte)` | `%9.0g` |
| `device_id` | Device ID | `Numeric(Float)` | `%9.0g` |
| `frequency` | Sampling frequency | `Numeric(Byte)` | `%9.0g` |
| `position` | Wearing position: left or right thigh | `Numeric(Byte)` | `%10.0g` |
| `ActiPASS_QC_day` | ActiPASS Check: Any warning | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_NoSleepInt_day` | ActiPASS Check: No sleep interval | `Numeric(Byte)` | `%8.0g` |
| `ActiPASS_NoWalk_day` | ActiPASS Check: < 30 sec walking | `Numeric(Byte)` | `%8.0g` |
| `ActiPASS_TooMuchBedtime_day` | ActiPASS Check: > 16 h bedtime | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_TooMuchOther_day` | ActiPASS Check: > 30 min other | `Numeric(Byte)` | `%8.0g` |
| `ActiPASS_TooMuchStair_day` | ActiPASS Check: > 120 min stair | `Numeric(Byte)` | `%8.0g` |
| `ActiPASS_Bedtime_hour` | Time which is flagged as belonging to a bedtime | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_LieStill_hour` | Time of possible sleep outside a bedtime | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_Sleep_hour` | Time of sleeping | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_SleepInterval_hour` | Time which is flagged as belonging to a sleep-interval | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Lie_hour` | Time of lying | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Sit_hour` | Time of sitting | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Stand_hour` | Time of standing | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Move_hour` | The time of 'move' | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Walk_hour` | Time of walking | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Run_hour` | Time of running | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Stair_hour` | Time of stair-walking (all stair walking like activities) | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Cycle_hour` | Time of cycling | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Other_hour` | Time of activities in 'Other' postures/activities | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_NonWear_hour` | Non-wear time | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_Steps_hour` | Total number of steps | `Numeric(Float)` | `%9.0g` |
| `GGIR_mean_ENMO_hour` | Mean ENMO (per hour) | `Numeric(Double)` | `%9.0g` |
| `GGIR_0_25_ENMO_hour` | Minutes in ENMO Level: [0-25) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_25_50_ENMO_hour` | Minutes in ENMO Level: [25-50) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_50_75_ENMO_hour` | Minutes in ENMO Level: [50-75) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_75_100_ENMO_hour` | Minutes in ENMO Level: [75-100) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_100_125_ENMO_hour` | Minutes in ENMO Level: [100-125) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_125_150_ENMO_hour` | Minutes in ENMO Level: [125-150) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_150_175_ENMO_hour` | Minutes in ENMO Level: [150-175) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_175_200_ENMO_hour` | Minutes in ENMO Level: [175-200) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_200_225_ENMO_hour` | Minutes in ENMO Level: [200-225) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_225_250_ENMO_hour` | Minutes in ENMO Level: [225-250) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_250_275_ENMO_hour` | Minutes in ENMO Level: [250-275) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_275_300_ENMO_hour` | Minutes in ENMO Level: [275-300) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_300_325_ENMO_hour` | Minutes in ENMO Level: [300-325) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_325_350_ENMO_hour` | Minutes in ENMO Level: [325-350) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_350_375_ENMO_hour` | Minutes in ENMO Level: [350-375) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_375_400_ENMO_hour` | Minutes in ENMO Level: [375-400) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_400_425_ENMO_hour` | Minutes in ENMO Level: [400-425) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_425_450_ENMO_hour` | Minutes in ENMO Level: [425-450) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_450_475_ENMO_hour` | Minutes in ENMO Level: [450-475) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_475_500_ENMO_hour` | Minutes in ENMO Level: [475-500) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_500_525_ENMO_hour` | Minutes in ENMO Level: [500-525) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_525_550_ENMO_hour` | Minutes in ENMO Level: [525-550) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_550_575_ENMO_hour` | Minutes in ENMO Level: [550-575) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_575_600_ENMO_hour` | Minutes in ENMO Level: [575-600) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_600_625_ENMO_hour` | Minutes in ENMO Level: [600-625) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_625_650_ENMO_hour` | Minutes in ENMO Level: [625-650) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_650_675_ENMO_hour` | Minutes in ENMO Level: [650-675) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_675_700_ENMO_hour` | Minutes in ENMO Level: [675-700) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_700_725_ENMO_hour` | Minutes in ENMO Level: [700-725) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_725_750_ENMO_hour` | Minutes in ENMO Level: [725-750) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_750_775_ENMO_hour` | Minutes in ENMO Level: [750-775) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_775_800_ENMO_hour` | Minutes in ENMO Level: [775-800) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_800_825_ENMO_hour` | Minutes in ENMO Level: [800-825) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_825_850_ENMO_hour` | Minutes in ENMO Level: [825-850) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_850_875_ENMO_hour` | Minutes in ENMO Level: [850-875) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_875_900_ENMO_hour` | Minutes in ENMO Level: [875-900) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_900_925_ENMO_hour` | Minutes in ENMO Level: [900-925) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_925_950_ENMO_hour` | Minutes in ENMO Level: [925-950) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_950_975_ENMO_hour` | Minutes in ENMO Level: [950-975) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_975_1000_ENMO_hour` | Minutes in ENMO Level: [975-1000) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1000_1025_ENMO_hour` | Minutes in ENMO Level: [1000-1025) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1025_1050_ENMO_hour` | Minutes in ENMO Level: [1025-1050) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1050_1075_ENMO_hour` | Minutes in ENMO Level: [1050-1075) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1075_1100_ENMO_hour` | Minutes in ENMO Level: [1075-1100) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1100_1125_ENMO_hour` | Minutes in ENMO Level: [1100-1125) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1125_1150_ENMO_hour` | Minutes in ENMO Level: [1125-1150) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1150_1175_ENMO_hour` | Minutes in ENMO Level: [1150-1175) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1175_1200_ENMO_hour` | Minutes in ENMO Level: [1175-1200) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1200_1225_ENMO_hour` | Minutes in ENMO Level: [1200-1225) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1225_1250_ENMO_hour` | Minutes in ENMO Level: [1225-1250) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1250_1275_ENMO_hour` | Minutes in ENMO Level: [1250-1275) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1275_1300_ENMO_hour` | Minutes in ENMO Level: [1275-1300) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1300_1325_ENMO_hour` | Minutes in ENMO Level: [1300-1325) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1325_1350_ENMO_hour` | Minutes in ENMO Level: [1325-1350) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1350_1375_ENMO_hour` | Minutes in ENMO Level: [1350-1375) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1375_1400_ENMO_hour` | Minutes in ENMO Level: [1375-1400) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1400_1425_ENMO_hour` | Minutes in ENMO Level: [1400-1425) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1425_1450_ENMO_hour` | Minutes in ENMO Level: [1425-1450) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1450_1475_ENMO_hour` | Minutes in ENMO Level: [1450-1475) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1475_1500_ENMO_hour` | Minutes in ENMO Level: [1475-1500) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1500_1525_ENMO_hour` | Minutes in ENMO Level: [1500-1525) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1525_1550_ENMO_hour` | Minutes in ENMO Level: [1525-1550) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1550_1575_ENMO_hour` | Minutes in ENMO Level: [1550-1575) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1575_1600_ENMO_hour` | Minutes in ENMO Level: [1575-1600) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1600_1625_ENMO_hour` | Minutes in ENMO Level: [1600-1625) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1625_1650_ENMO_hour` | Minutes in ENMO Level: [1625-1650) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1650_1675_ENMO_hour` | Minutes in ENMO Level: [1650-1675) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1675_1700_ENMO_hour` | Minutes in ENMO Level: [1675-1700) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1700_1725_ENMO_hour` | Minutes in ENMO Level: [1700-1725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_1725_1750_ENMO_hour` | Minutes in ENMO Level: [1725-1750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_1750_1775_ENMO_hour` | Minutes in ENMO Level: [1750-1775) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1775_1800_ENMO_hour` | Minutes in ENMO Level: [1775-1800) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1800_1825_ENMO_hour` | Minutes in ENMO Level: [1800-1825) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1825_1850_ENMO_hour` | Minutes in ENMO Level: [1825-1850) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1850_1875_ENMO_hour` | Minutes in ENMO Level: [1850-1875) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1875_1900_ENMO_hour` | Minutes in ENMO Level: [1875-1900) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1900_1925_ENMO_hour` | Minutes in ENMO Level: [1900-1925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_1925_1950_ENMO_hour` | Minutes in ENMO Level: [1925-1950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_1950_1975_ENMO_hour` | Minutes in ENMO Level: [1950-1975) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_1975_2000_ENMO_hour` | Minutes in ENMO Level: [1975-2000) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2000_2025_ENMO_hour` | Minutes in ENMO Level: [2000-2025) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2025_2050_ENMO_hour` | Minutes in ENMO Level: [2025-2050) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2050_2075_ENMO_hour` | Minutes in ENMO Level: [2050-2075) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2075_2100_ENMO_hour` | Minutes in ENMO Level: [2075-2100) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2100_2125_ENMO_hour` | Minutes in ENMO Level: [2100-2125) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2125_2150_ENMO_hour` | Minutes in ENMO Level: [2125-2150) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2150_2175_ENMO_hour` | Minutes in ENMO Level: [2150-2175) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2175_2200_ENMO_hour` | Minutes in ENMO Level: [2175-2200) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2200_2225_ENMO_hour` | Minutes in ENMO Level: [2200-2225) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2225_2250_ENMO_hour` | Minutes in ENMO Level: [2225-2250) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2250_2275_ENMO_hour` | Minutes in ENMO Level: [2250-2275) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2275_2300_ENMO_hour` | Minutes in ENMO Level: [2275-2300) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2300_2325_ENMO_hour` | Minutes in ENMO Level: [2300-2325) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2325_2350_ENMO_hour` | Minutes in ENMO Level: [2325-2350) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2350_2375_ENMO_hour` | Minutes in ENMO Level: [2350-2375) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2375_2400_ENMO_hour` | Minutes in ENMO Level: [2375-2400) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2400_2425_ENMO_hour` | Minutes in ENMO Level: [2400-2425) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2425_2450_ENMO_hour` | Minutes in ENMO Level: [2425-2450) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2450_2475_ENMO_hour` | Minutes in ENMO Level: [2450-2475) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2475_2500_ENMO_hour` | Minutes in ENMO Level: [2475-2500) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2500_2525_ENMO_hour` | Minutes in ENMO Level: [2500-2525) mg | `Numeric(Double)` | `%9.0g` |
| `GGIR_2525_2550_ENMO_hour` | Minutes in ENMO Level: [2525-2550) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2550_2575_ENMO_hour` | Minutes in ENMO Level: [2550-2575) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2575_2600_ENMO_hour` | Minutes in ENMO Level: [2575-2600) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2600_2625_ENMO_hour` | Minutes in ENMO Level: [2600-2625) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2625_2650_ENMO_hour` | Minutes in ENMO Level: [2625-2650) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2650_2675_ENMO_hour` | Minutes in ENMO Level: [2650-2675) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2675_2700_ENMO_hour` | Minutes in ENMO Level: [2675-2700) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2700_2725_ENMO_hour` | Minutes in ENMO Level: [2700-2725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2725_2750_ENMO_hour` | Minutes in ENMO Level: [2725-2750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2750_2775_ENMO_hour` | Minutes in ENMO Level: [2750-2775) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2775_2800_ENMO_hour` | Minutes in ENMO Level: [2775-2800) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2800_2825_ENMO_hour` | Minutes in ENMO Level: [2800-2825) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2825_2850_ENMO_hour` | Minutes in ENMO Level: [2825-2850) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2850_2875_ENMO_hour` | Minutes in ENMO Level: [2850-2875) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2875_2900_ENMO_hour` | Minutes in ENMO Level: [2875-2900) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2900_2925_ENMO_hour` | Minutes in ENMO Level: [2900-2925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2925_2950_ENMO_hour` | Minutes in ENMO Level: [2925-2950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2950_2975_ENMO_hour` | Minutes in ENMO Level: [2950-2975) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2975_3000_ENMO_hour` | Minutes in ENMO Level: [2975-3000) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3000_3025_ENMO_hour` | Minutes in ENMO Level: [3000-3025) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3025_3050_ENMO_hour` | Minutes in ENMO Level: [3025-3050) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3050_3075_ENMO_hour` | Minutes in ENMO Level: [3050-3075) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3075_3100_ENMO_hour` | Minutes in ENMO Level: [3075-3100) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3100_3125_ENMO_hour` | Minutes in ENMO Level: [3100-3125) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3125_3150_ENMO_hour` | Minutes in ENMO Level: [3125-3150) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3150_3175_ENMO_hour` | Minutes in ENMO Level: [3150-3175) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3175_3200_ENMO_hour` | Minutes in ENMO Level: [3175-3200) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3200_3225_ENMO_hour` | Minutes in ENMO Level: [3200-3225) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3225_3250_ENMO_hour` | Minutes in ENMO Level: [3225-3250) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3250_3275_ENMO_hour` | Minutes in ENMO Level: [3250-3275) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3275_3300_ENMO_hour` | Minutes in ENMO Level: [3275-3300) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3300_3325_ENMO_hour` | Minutes in ENMO Level: [3300-3325) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3325_3350_ENMO_hour` | Minutes in ENMO Level: [3325-3350) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3350_3375_ENMO_hour` | Minutes in ENMO Level: [3350-3375) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3375_3400_ENMO_hour` | Minutes in ENMO Level: [3375-3400) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3400_3425_ENMO_hour` | Minutes in ENMO Level: [3400-3425) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3425_3450_ENMO_hour` | Minutes in ENMO Level: [3425-3450) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3450_3475_ENMO_hour` | Minutes in ENMO Level: [3450-3475) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3475_3500_ENMO_hour` | Minutes in ENMO Level: [3475-3500) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3500_3525_ENMO_hour` | Minutes in ENMO Level: [3500-3525) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3525_3550_ENMO_hour` | Minutes in ENMO Level: [3525-3550) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3550_3575_ENMO_hour` | Minutes in ENMO Level: [3550-3575) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3575_3600_ENMO_hour` | Minutes in ENMO Level: [3575-3600) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3600_3625_ENMO_hour` | Minutes in ENMO Level: [3600-3625) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3625_3650_ENMO_hour` | Minutes in ENMO Level: [3625-3650) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3650_3675_ENMO_hour` | Minutes in ENMO Level: [3650-3675) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3675_3700_ENMO_hour` | Minutes in ENMO Level: [3675-3700) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3700_3725_ENMO_hour` | Minutes in ENMO Level: [3700-3725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3725_3750_ENMO_hour` | Minutes in ENMO Level: [3725-3750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3750_3775_ENMO_hour` | Minutes in ENMO Level: [3750-3775) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3775_3800_ENMO_hour` | Minutes in ENMO Level: [3775-3800) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3800_3825_ENMO_hour` | Minutes in ENMO Level: [3800-3825) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3825_3850_ENMO_hour` | Minutes in ENMO Level: [3825-3850) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3850_3875_ENMO_hour` | Minutes in ENMO Level: [3850-3875) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3875_3900_ENMO_hour` | Minutes in ENMO Level: [3875-3900) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3900_3925_ENMO_hour` | Minutes in ENMO Level: [3900-3925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3925_3950_ENMO_hour` | Minutes in ENMO Level: [3925-3950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3950_3975_ENMO_hour` | Minutes in ENMO Level: [3950-3975) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3975_4000_ENMO_hour` | Minutes in ENMO Level: [3975-4000) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4000_4025_ENMO_hour` | Minutes in ENMO Level: [4000-4025) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4025_4050_ENMO_hour` | Minutes in ENMO Level: [4025-4050) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4050_4075_ENMO_hour` | Minutes in ENMO Level: [4050-4075) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4075_4100_ENMO_hour` | Minutes in ENMO Level: [4075-4100) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4100_4125_ENMO_hour` | Minutes in ENMO Level: [4100-4125) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4125_4150_ENMO_hour` | Minutes in ENMO Level: [4125-4150) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4150_4175_ENMO_hour` | Minutes in ENMO Level: [4150-4175) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4175_4200_ENMO_hour` | Minutes in ENMO Level: [4175-4200) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4200_4225_ENMO_hour` | Minutes in ENMO Level: [4200-4225) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4225_4250_ENMO_hour` | Minutes in ENMO Level: [4225-4250) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4250_4275_ENMO_hour` | Minutes in ENMO Level: [4250-4275) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4275_4300_ENMO_hour` | Minutes in ENMO Level: [4275-4300) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4300_4325_ENMO_hour` | Minutes in ENMO Level: [4300-4325) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4325_4350_ENMO_hour` | Minutes in ENMO Level: [4325-4350) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4350_4375_ENMO_hour` | Minutes in ENMO Level: [4350-4375) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4375_4400_ENMO_hour` | Minutes in ENMO Level: [4375-4400) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4400_4425_ENMO_hour` | Minutes in ENMO Level: [4400-4425) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4425_4450_ENMO_hour` | Minutes in ENMO Level: [4425-4450) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4450_4475_ENMO_hour` | Minutes in ENMO Level: [4450-4475) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4475_4500_ENMO_hour` | Minutes in ENMO Level: [4475-4500) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4500_4525_ENMO_hour` | Minutes in ENMO Level: [4500-4525) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4525_4550_ENMO_hour` | Minutes in ENMO Level: [4525-4550) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4550_4575_ENMO_hour` | Minutes in ENMO Level: [4550-4575) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4575_4600_ENMO_hour` | Minutes in ENMO Level: [4575-4600) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4600_4625_ENMO_hour` | Minutes in ENMO Level: [4600-4625) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4625_4650_ENMO_hour` | Minutes in ENMO Level: [4625-4650) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4650_4675_ENMO_hour` | Minutes in ENMO Level: [4650-4675) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4675_4700_ENMO_hour` | Minutes in ENMO Level: [4675-4700) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4700_4725_ENMO_hour` | Minutes in ENMO Level: [4700-4725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4725_4750_ENMO_hour` | Minutes in ENMO Level: [4725-4750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4750_4775_ENMO_hour` | Minutes in ENMO Level: [4750-4775) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4775_4800_ENMO_hour` | Minutes in ENMO Level: [4775-4800) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4800_4825_ENMO_hour` | Minutes in ENMO Level: [4800-4825) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4825_4850_ENMO_hour` | Minutes in ENMO Level: [4825-4850) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4850_4875_ENMO_hour` | Minutes in ENMO Level: [4850-4875) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4875_4900_ENMO_hour` | Minutes in ENMO Level: [4875-4900) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4900_4925_ENMO_hour` | Minutes in ENMO Level: [4900-4925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4925_4950_ENMO_hour` | Minutes in ENMO Level: [4925-4950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4950_4975_ENMO_hour` | Minutes in ENMO Level: [4950-4975) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4975_5000_ENMO_hour` | Minutes in ENMO Level: [4975-5000) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5000_5025_ENMO_hour` | Minutes in ENMO Level: [5000-5025) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5025_5050_ENMO_hour` | Minutes in ENMO Level: [5025-5050) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5050_5075_ENMO_hour` | Minutes in ENMO Level: [5050-5075) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5075_5100_ENMO_hour` | Minutes in ENMO Level: [5075-5100) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5100_5125_ENMO_hour` | Minutes in ENMO Level: [5100-5125) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5125_5150_ENMO_hour` | Minutes in ENMO Level: [5125-5150) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5150_5175_ENMO_hour` | Minutes in ENMO Level: [5150-5175) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5175_5200_ENMO_hour` | Minutes in ENMO Level: [5175-5200) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5200_5225_ENMO_hour` | Minutes in ENMO Level: [5200-5225) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5225_5250_ENMO_hour` | Minutes in ENMO Level: [5225-5250) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5250_5275_ENMO_hour` | Minutes in ENMO Level: [5250-5275) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5275_5300_ENMO_hour` | Minutes in ENMO Level: [5275-5300) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5300_5325_ENMO_hour` | Minutes in ENMO Level: [5300-5325) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5325_5350_ENMO_hour` | Minutes in ENMO Level: [5325-5350) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5350_5375_ENMO_hour` | Minutes in ENMO Level: [5350-5375) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5375_5400_ENMO_hour` | Minutes in ENMO Level: [5375-5400) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5400_5425_ENMO_hour` | Minutes in ENMO Level: [5400-5425) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5425_5450_ENMO_hour` | Minutes in ENMO Level: [5425-5450) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5450_5475_ENMO_hour` | Minutes in ENMO Level: [5450-5475) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5475_5500_ENMO_hour` | Minutes in ENMO Level: [5475-5500) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5500_5525_ENMO_hour` | Minutes in ENMO Level: [5500-5525) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5525_5550_ENMO_hour` | Minutes in ENMO Level: [5525-5550) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5550_5575_ENMO_hour` | Minutes in ENMO Level: [5550-5575) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5575_5600_ENMO_hour` | Minutes in ENMO Level: [5575-5600) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5600_5625_ENMO_hour` | Minutes in ENMO Level: [5600-5625) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5625_5650_ENMO_hour` | Minutes in ENMO Level: [5625-5650) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5650_5675_ENMO_hour` | Minutes in ENMO Level: [5650-5675) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5675_5700_ENMO_hour` | Minutes in ENMO Level: [5675-5700) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5700_5725_ENMO_hour` | Minutes in ENMO Level: [5700-5725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5725_5750_ENMO_hour` | Minutes in ENMO Level: [5725-5750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5750_5775_ENMO_hour` | Minutes in ENMO Level: [5750-5775) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5775_5800_ENMO_hour` | Minutes in ENMO Level: [5775-5800) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5800_5825_ENMO_hour` | Minutes in ENMO Level: [5800-5825) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5825_5850_ENMO_hour` | Minutes in ENMO Level: [5825-5850) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5850_5875_ENMO_hour` | Minutes in ENMO Level: [5850-5875) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5875_5900_ENMO_hour` | Minutes in ENMO Level: [5875-5900) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5900_5925_ENMO_hour` | Minutes in ENMO Level: [5900-5925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5925_5950_ENMO_hour` | Minutes in ENMO Level: [5925-5950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5950_5975_ENMO_hour` | Minutes in ENMO Level: [5950-5975) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5975_6000_ENMO_hour` | Minutes in ENMO Level: [5975-6000) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_6000_15000_ENMO_hour` | Minutes in ENMO Level: [6000-15000) mg | `Numeric(Byte)` | `%9.0g` |

### `gv_accelerometer_sleep` - Accelerometer sleep dataset

- Dataset: `sharew8_rel9-0-0_gv_accelerometer_sleep.dta`
- Read with: `ps.read_share_module("gv_accelerometer_sleep", wave=8)`
- Rows: 6,254
- Variables: 11
- Key hint: `mergeid` + sleep-interval repeated rows

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ActiPASS_LongBedtime` | ActiPASS Check: > 16 h bedtime | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_LongSleep` | ActiPASS Check: > 16 h sleep interval | `Numeric(Byte)` | `%9.0g` |
| `measurementday_SleepStart` | Start day sleep spell (detected by ActiPASS) | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_Time_SleepStart` | Start time sleep spell (detected by ActiPASS) | `Numeric(Float)` | `%9.0g` |
| `measurementday_SleepEnd` | End day sleep spell (detected by ActiPASS) | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_Time_SleepEnd` | End time sleep spell (detected by ActiPASS) | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_SleepInterval` | Sleep Interval: Duration (detected by ActiPASS) | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_TotalSleep` | Sleep duration (detected by ActiPASS) | `Numeric(Float)` | `%9.0g` |

### `gv_accelerometer_total` - Accelerometer summary dataset

- Dataset: `sharew8_rel9-0-0_gv_accelerometer_total.dta`
- Read with: `ps.read_share_module("gv_accelerometer_total", wave=8)`
- Rows: 855
- Variables: 271
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `month` | Month of measurement | `Numeric(Byte)` | `%10.0g` |
| `year` | Year of measurement | `Numeric(Int)` | `%9.0g` |
| `ActiPASS_N_valid_days` | Number of valid days detected by ActiPASS | `Numeric(Byte)` | `%9.0g` |
| `GGIR_N_valid_days` | Number of valid days detected by GGIR | `Numeric(Byte)` | `%9.0g` |
| `GGIR_N_valid_hours_total` | GGIR detected total valid hours | `Numeric(Float)` | `%9.0g` |
| `reported_N_valid_hours_total` | Reported total valid hours | `Numeric(Float)` | `%9.0g` |
| `OxCGRT_stay_at_home` | OxCGRT stay at home requirements (mode over observation time by person) | `Numeric(Byte)` | `%128.0g` |
| `OxCGRT_stringency_index` | OxCGRT stringency index (mean over observation time by person) | `Numeric(Byte)` | `%9.0g` |
| `device_id` | Device ID | `Numeric(Float)` | `%9.0g` |
| `frequency` | Sampling frequency | `Numeric(Byte)` | `%9.0g` |
| `position` | Wearing position: Left or right thigh | `Numeric(Byte)` | `%10.0g` |
| `ActiPASS_QC_total` | ActiPASS Check: 1+ day with any warning | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_NoSleepInt_total` | ActiPASS Check: 1+ day with no sleep interval | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_NoWalk_total` | ActiPASS Check: 1+ day with < 30 sec walking | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_TooMuchBedtime_total` | ActiPASS Check: 1+ day with > 16 h bedtime | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_TooMuchOther_total` | ActiPASS Check: 1+ day with > 30 min other | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_TooMuchStair_total` | ActiPASS Check: 1+ day with > 120 min stair | `Numeric(Byte)` | `%9.0g` |
| `ActiPASS_Steps_total` | Mean Steps per day (over whole observation time by person) | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_INT1_total` | Mean sedentary time per day (over whole observation time by person) | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_INT2_total` | Mean low PA time per day (over whole observation time by person) | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_INT3_total` | Mean moderate PA time per day (over whole observation time by person) | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_INT4_total` | Mean vigorousÂ PA time per day (over whole observation time by person) | `Numeric(Float)` | `%9.0g` |
| `ActiPASS_INT34_total` | Mean moderate + vigorousÂ PA time per day (over whole observation time by perso | `Numeric(Float)` | `%9.0g` |
| `GGIR_mean_ENMO_total` | Mean ENMO (over whole observation time by person) | `Numeric(Float)` | `%9.0g` |
| `GGIR_ig_rsquared_ENMO_total` | IG R-squared (calculated over whole observation time by person) | `Numeric(Float)` | `%9.0g` |
| `GGIR_ig_gradient_ENMO_total` | IG Gradient (calculated over whole observation time by person) | `Numeric(Float)` | `%9.0g` |
| `GGIR_ig_intercept_ENMO_total` | IG Intercept (calculated over whole observation time by person) | `Numeric(Float)` | `%9.0g` |
| `GGIR_0_25_ENMO_total` | Minutes in ENMO Level: [0-25) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_25_50_ENMO_total` | Minutes in ENMO Level: [25-50) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_50_75_ENMO_total` | Minutes in ENMO Level: [50-75) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_75_100_ENMO_total` | Minutes in ENMO Level: [75-100) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_100_125_ENMO_total` | Minutes in ENMO Level: [100-125) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_125_150_ENMO_total` | Minutes in ENMO Level: [125-150) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_150_175_ENMO_total` | Minutes in ENMO Level: [150-175) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_175_200_ENMO_total` | Minutes in ENMO Level: [175-200) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_200_225_ENMO_total` | Minutes in ENMO Level: [200-225) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_225_250_ENMO_total` | Minutes in ENMO Level: [225-250) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_250_275_ENMO_total` | Minutes in ENMO Level: [250-275) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_275_300_ENMO_total` | Minutes in ENMO Level: [275-300) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_300_325_ENMO_total` | Minutes in ENMO Level: [300-325) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_325_350_ENMO_total` | Minutes in ENMO Level: [325-350) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_350_375_ENMO_total` | Minutes in ENMO Level: [350-375) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_375_400_ENMO_total` | Minutes in ENMO Level: [375-400) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_400_425_ENMO_total` | Minutes in ENMO Level: [400-425) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_425_450_ENMO_total` | Minutes in ENMO Level: [425-450) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_450_475_ENMO_total` | Minutes in ENMO Level: [450-475) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_475_500_ENMO_total` | Minutes in ENMO Level: [475-500) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_500_525_ENMO_total` | Minutes in ENMO Level: [500-525) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_525_550_ENMO_total` | Minutes in ENMO Level: [525-550) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_550_575_ENMO_total` | Minutes in ENMO Level: [550-575) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_575_600_ENMO_total` | Minutes in ENMO Level: [575-600) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_600_625_ENMO_total` | Minutes in ENMO Level: [600-625) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_625_650_ENMO_total` | Minutes in ENMO Level: [625-650) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_650_675_ENMO_total` | Minutes in ENMO Level: [650-675) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_675_700_ENMO_total` | Minutes in ENMO Level: [675-700) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_700_725_ENMO_total` | Minutes in ENMO Level: [700-725) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_725_750_ENMO_total` | Minutes in ENMO Level: [725-750) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_750_775_ENMO_total` | Minutes in ENMO Level: [750-775) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_775_800_ENMO_total` | Minutes in ENMO Level: [775-800) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_800_825_ENMO_total` | Minutes in ENMO Level: [800-825) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_825_850_ENMO_total` | Minutes in ENMO Level: [825-850) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_850_875_ENMO_total` | Minutes in ENMO Level: [850-875) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_875_900_ENMO_total` | Minutes in ENMO Level: [875-900) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_900_925_ENMO_total` | Minutes in ENMO Level: [900-925) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_925_950_ENMO_total` | Minutes in ENMO Level: [925-950) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_950_975_ENMO_total` | Minutes in ENMO Level: [950-975) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_975_1000_ENMO_total` | Minutes in ENMO Level: [975-1000) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1000_1025_ENMO_total` | Minutes in ENMO Level: [1000-1025) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1025_1050_ENMO_total` | Minutes in ENMO Level: [1025-1050) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1050_1075_ENMO_total` | Minutes in ENMO Level: [1050-1075) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1075_1100_ENMO_total` | Minutes in ENMO Level: [1075-1100) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1100_1125_ENMO_total` | Minutes in ENMO Level: [1100-1125) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1125_1150_ENMO_total` | Minutes in ENMO Level: [1125-1150) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1150_1175_ENMO_total` | Minutes in ENMO Level: [1150-1175) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1175_1200_ENMO_total` | Minutes in ENMO Level: [1175-1200) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1200_1225_ENMO_total` | Minutes in ENMO Level: [1200-1225) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1225_1250_ENMO_total` | Minutes in ENMO Level: [1225-1250) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1250_1275_ENMO_total` | Minutes in ENMO Level: [1250-1275) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1275_1300_ENMO_total` | Minutes in ENMO Level: [1275-1300) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1300_1325_ENMO_total` | Minutes in ENMO Level: [1300-1325) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1325_1350_ENMO_total` | Minutes in ENMO Level: [1325-1350) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1350_1375_ENMO_total` | Minutes in ENMO Level: [1350-1375) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1375_1400_ENMO_total` | Minutes in ENMO Level: [1375-1400) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1400_1425_ENMO_total` | Minutes in ENMO Level: [1400-1425) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1425_1450_ENMO_total` | Minutes in ENMO Level: [1425-1450) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1450_1475_ENMO_total` | Minutes in ENMO Level: [1450-1475) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1475_1500_ENMO_total` | Minutes in ENMO Level: [1475-1500) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1500_1525_ENMO_total` | Minutes in ENMO Level: [1500-1525) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1525_1550_ENMO_total` | Minutes in ENMO Level: [1525-1550) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1550_1575_ENMO_total` | Minutes in ENMO Level: [1550-1575) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1575_1600_ENMO_total` | Minutes in ENMO Level: [1575-1600) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1600_1625_ENMO_total` | Minutes in ENMO Level: [1600-1625) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1625_1650_ENMO_total` | Minutes in ENMO Level: [1625-1650) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1650_1675_ENMO_total` | Minutes in ENMO Level: [1650-1675) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1675_1700_ENMO_total` | Minutes in ENMO Level: [1675-1700) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1700_1725_ENMO_total` | Minutes in ENMO Level: [1700-1725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_1725_1750_ENMO_total` | Minutes in ENMO Level: [1725-1750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_1750_1775_ENMO_total` | Minutes in ENMO Level: [1750-1775) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1775_1800_ENMO_total` | Minutes in ENMO Level: [1775-1800) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1800_1825_ENMO_total` | Minutes in ENMO Level: [1800-1825) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1825_1850_ENMO_total` | Minutes in ENMO Level: [1825-1850) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1850_1875_ENMO_total` | Minutes in ENMO Level: [1850-1875) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1875_1900_ENMO_total` | Minutes in ENMO Level: [1875-1900) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1900_1925_ENMO_total` | Minutes in ENMO Level: [1900-1925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_1925_1950_ENMO_total` | Minutes in ENMO Level: [1925-1950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_1950_1975_ENMO_total` | Minutes in ENMO Level: [1950-1975) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_1975_2000_ENMO_total` | Minutes in ENMO Level: [1975-2000) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_2000_2025_ENMO_total` | Minutes in ENMO Level: [2000-2025) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_2025_2050_ENMO_total` | Minutes in ENMO Level: [2025-2050) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_2050_2075_ENMO_total` | Minutes in ENMO Level: [2050-2075) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2075_2100_ENMO_total` | Minutes in ENMO Level: [2075-2100) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_2100_2125_ENMO_total` | Minutes in ENMO Level: [2100-2125) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2125_2150_ENMO_total` | Minutes in ENMO Level: [2125-2150) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2150_2175_ENMO_total` | Minutes in ENMO Level: [2150-2175) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_2175_2200_ENMO_total` | Minutes in ENMO Level: [2175-2200) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2200_2225_ENMO_total` | Minutes in ENMO Level: [2200-2225) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_2225_2250_ENMO_total` | Minutes in ENMO Level: [2225-2250) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_2250_2275_ENMO_total` | Minutes in ENMO Level: [2250-2275) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_2275_2300_ENMO_total` | Minutes in ENMO Level: [2275-2300) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2300_2325_ENMO_total` | Minutes in ENMO Level: [2300-2325) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2325_2350_ENMO_total` | Minutes in ENMO Level: [2325-2350) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_2350_2375_ENMO_total` | Minutes in ENMO Level: [2350-2375) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2375_2400_ENMO_total` | Minutes in ENMO Level: [2375-2400) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_2400_2425_ENMO_total` | Minutes in ENMO Level: [2400-2425) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2425_2450_ENMO_total` | Minutes in ENMO Level: [2425-2450) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2450_2475_ENMO_total` | Minutes in ENMO Level: [2450-2475) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2475_2500_ENMO_total` | Minutes in ENMO Level: [2475-2500) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2500_2525_ENMO_total` | Minutes in ENMO Level: [2500-2525) mg | `Numeric(Float)` | `%9.0g` |
| `GGIR_2525_2550_ENMO_total` | Minutes in ENMO Level: [2525-2550) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2550_2575_ENMO_total` | Minutes in ENMO Level: [2550-2575) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2575_2600_ENMO_total` | Minutes in ENMO Level: [2575-2600) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2600_2625_ENMO_total` | Minutes in ENMO Level: [2600-2625) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2625_2650_ENMO_total` | Minutes in ENMO Level: [2625-2650) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2650_2675_ENMO_total` | Minutes in ENMO Level: [2650-2675) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2675_2700_ENMO_total` | Minutes in ENMO Level: [2675-2700) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2700_2725_ENMO_total` | Minutes in ENMO Level: [2700-2725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2725_2750_ENMO_total` | Minutes in ENMO Level: [2725-2750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2750_2775_ENMO_total` | Minutes in ENMO Level: [2750-2775) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2775_2800_ENMO_total` | Minutes in ENMO Level: [2775-2800) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2800_2825_ENMO_total` | Minutes in ENMO Level: [2800-2825) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2825_2850_ENMO_total` | Minutes in ENMO Level: [2825-2850) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2850_2875_ENMO_total` | Minutes in ENMO Level: [2850-2875) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2875_2900_ENMO_total` | Minutes in ENMO Level: [2875-2900) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2900_2925_ENMO_total` | Minutes in ENMO Level: [2900-2925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2925_2950_ENMO_total` | Minutes in ENMO Level: [2925-2950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2950_2975_ENMO_total` | Minutes in ENMO Level: [2950-2975) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_2975_3000_ENMO_total` | Minutes in ENMO Level: [2975-3000) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3000_3025_ENMO_total` | Minutes in ENMO Level: [3000-3025) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3025_3050_ENMO_total` | Minutes in ENMO Level: [3025-3050) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3050_3075_ENMO_total` | Minutes in ENMO Level: [3050-3075) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3075_3100_ENMO_total` | Minutes in ENMO Level: [3075-3100) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3100_3125_ENMO_total` | Minutes in ENMO Level: [3100-3125) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3125_3150_ENMO_total` | Minutes in ENMO Level: [3125-3150) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3150_3175_ENMO_total` | Minutes in ENMO Level: [3150-3175) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3175_3200_ENMO_total` | Minutes in ENMO Level: [3175-3200) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3200_3225_ENMO_total` | Minutes in ENMO Level: [3200-3225) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3225_3250_ENMO_total` | Minutes in ENMO Level: [3225-3250) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3250_3275_ENMO_total` | Minutes in ENMO Level: [3250-3275) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3275_3300_ENMO_total` | Minutes in ENMO Level: [3275-3300) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3300_3325_ENMO_total` | Minutes in ENMO Level: [3300-3325) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3325_3350_ENMO_total` | Minutes in ENMO Level: [3325-3350) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3350_3375_ENMO_total` | Minutes in ENMO Level: [3350-3375) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3375_3400_ENMO_total` | Minutes in ENMO Level: [3375-3400) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3400_3425_ENMO_total` | Minutes in ENMO Level: [3400-3425) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3425_3450_ENMO_total` | Minutes in ENMO Level: [3425-3450) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3450_3475_ENMO_total` | Minutes in ENMO Level: [3450-3475) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3475_3500_ENMO_total` | Minutes in ENMO Level: [3475-3500) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3500_3525_ENMO_total` | Minutes in ENMO Level: [3500-3525) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3525_3550_ENMO_total` | Minutes in ENMO Level: [3525-3550) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3550_3575_ENMO_total` | Minutes in ENMO Level: [3550-3575) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3575_3600_ENMO_total` | Minutes in ENMO Level: [3575-3600) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3600_3625_ENMO_total` | Minutes in ENMO Level: [3600-3625) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3625_3650_ENMO_total` | Minutes in ENMO Level: [3625-3650) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3650_3675_ENMO_total` | Minutes in ENMO Level: [3650-3675) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3675_3700_ENMO_total` | Minutes in ENMO Level: [3675-3700) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3700_3725_ENMO_total` | Minutes in ENMO Level: [3700-3725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3725_3750_ENMO_total` | Minutes in ENMO Level: [3725-3750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3750_3775_ENMO_total` | Minutes in ENMO Level: [3750-3775) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3775_3800_ENMO_total` | Minutes in ENMO Level: [3775-3800) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3800_3825_ENMO_total` | Minutes in ENMO Level: [3800-3825) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3825_3850_ENMO_total` | Minutes in ENMO Level: [3825-3850) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3850_3875_ENMO_total` | Minutes in ENMO Level: [3850-3875) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3875_3900_ENMO_total` | Minutes in ENMO Level: [3875-3900) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3900_3925_ENMO_total` | Minutes in ENMO Level: [3900-3925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3925_3950_ENMO_total` | Minutes in ENMO Level: [3925-3950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3950_3975_ENMO_total` | Minutes in ENMO Level: [3950-3975) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_3975_4000_ENMO_total` | Minutes in ENMO Level: [3975-4000) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4000_4025_ENMO_total` | Minutes in ENMO Level: [4000-4025) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4025_4050_ENMO_total` | Minutes in ENMO Level: [4025-4050) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4050_4075_ENMO_total` | Minutes in ENMO Level: [4050-4075) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4075_4100_ENMO_total` | Minutes in ENMO Level: [4075-4100) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4100_4125_ENMO_total` | Minutes in ENMO Level: [4100-4125) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4125_4150_ENMO_total` | Minutes in ENMO Level: [4125-4150) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4150_4175_ENMO_total` | Minutes in ENMO Level: [4150-4175) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4175_4200_ENMO_total` | Minutes in ENMO Level: [4175-4200) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4200_4225_ENMO_total` | Minutes in ENMO Level: [4200-4225) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4225_4250_ENMO_total` | Minutes in ENMO Level: [4225-4250) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4250_4275_ENMO_total` | Minutes in ENMO Level: [4250-4275) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4275_4300_ENMO_total` | Minutes in ENMO Level: [4275-4300) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4300_4325_ENMO_total` | Minutes in ENMO Level: [4300-4325) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4325_4350_ENMO_total` | Minutes in ENMO Level: [4325-4350) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4350_4375_ENMO_total` | Minutes in ENMO Level: [4350-4375) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4375_4400_ENMO_total` | Minutes in ENMO Level: [4375-4400) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4400_4425_ENMO_total` | Minutes in ENMO Level: [4400-4425) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4425_4450_ENMO_total` | Minutes in ENMO Level: [4425-4450) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4450_4475_ENMO_total` | Minutes in ENMO Level: [4450-4475) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4475_4500_ENMO_total` | Minutes in ENMO Level: [4475-4500) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4500_4525_ENMO_total` | Minutes in ENMO Level: [4500-4525) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4525_4550_ENMO_total` | Minutes in ENMO Level: [4525-4550) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4550_4575_ENMO_total` | Minutes in ENMO Level: [4550-4575) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4575_4600_ENMO_total` | Minutes in ENMO Level: [4575-4600) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4600_4625_ENMO_total` | Minutes in ENMO Level: [4600-4625) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4625_4650_ENMO_total` | Minutes in ENMO Level: [4625-4650) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4650_4675_ENMO_total` | Minutes in ENMO Level: [4650-4675) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4675_4700_ENMO_total` | Minutes in ENMO Level: [4675-4700) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4700_4725_ENMO_total` | Minutes in ENMO Level: [4700-4725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4725_4750_ENMO_total` | Minutes in ENMO Level: [4725-4750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4750_4775_ENMO_total` | Minutes in ENMO Level: [4750-4775) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4775_4800_ENMO_total` | Minutes in ENMO Level: [4775-4800) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4800_4825_ENMO_total` | Minutes in ENMO Level: [4800-4825) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4825_4850_ENMO_total` | Minutes in ENMO Level: [4825-4850) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4850_4875_ENMO_total` | Minutes in ENMO Level: [4850-4875) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4875_4900_ENMO_total` | Minutes in ENMO Level: [4875-4900) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4900_4925_ENMO_total` | Minutes in ENMO Level: [4900-4925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4925_4950_ENMO_total` | Minutes in ENMO Level: [4925-4950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4950_4975_ENMO_total` | Minutes in ENMO Level: [4950-4975) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_4975_5000_ENMO_total` | Minutes in ENMO Level: [4975-5000) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5000_5025_ENMO_total` | Minutes in ENMO Level: [5000-5025) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5025_5050_ENMO_total` | Minutes in ENMO Level: [5025-5050) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5050_5075_ENMO_total` | Minutes in ENMO Level: [5050-5075) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5075_5100_ENMO_total` | Minutes in ENMO Level: [5075-5100) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5100_5125_ENMO_total` | Minutes in ENMO Level: [5100-5125) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5125_5150_ENMO_total` | Minutes in ENMO Level: [5125-5150) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5150_5175_ENMO_total` | Minutes in ENMO Level: [5150-5175) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5175_5200_ENMO_total` | Minutes in ENMO Level: [5175-5200) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5200_5225_ENMO_total` | Minutes in ENMO Level: [5200-5225) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5225_5250_ENMO_total` | Minutes in ENMO Level: [5225-5250) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5250_5275_ENMO_total` | Minutes in ENMO Level: [5250-5275) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5275_5300_ENMO_total` | Minutes in ENMO Level: [5275-5300) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5300_5325_ENMO_total` | Minutes in ENMO Level: [5300-5325) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5325_5350_ENMO_total` | Minutes in ENMO Level: [5325-5350) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5350_5375_ENMO_total` | Minutes in ENMO Level: [5350-5375) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5375_5400_ENMO_total` | Minutes in ENMO Level: [5375-5400) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5400_5425_ENMO_total` | Minutes in ENMO Level: [5400-5425) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5425_5450_ENMO_total` | Minutes in ENMO Level: [5425-5450) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5450_5475_ENMO_total` | Minutes in ENMO Level: [5450-5475) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5475_5500_ENMO_total` | Minutes in ENMO Level: [5475-5500) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5500_5525_ENMO_total` | Minutes in ENMO Level: [5500-5525) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5525_5550_ENMO_total` | Minutes in ENMO Level: [5525-5550) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5550_5575_ENMO_total` | Minutes in ENMO Level: [5550-5575) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5575_5600_ENMO_total` | Minutes in ENMO Level: [5575-5600) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5600_5625_ENMO_total` | Minutes in ENMO Level: [5600-5625) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5625_5650_ENMO_total` | Minutes in ENMO Level: [5625-5650) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5650_5675_ENMO_total` | Minutes in ENMO Level: [5650-5675) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5675_5700_ENMO_total` | Minutes in ENMO Level: [5675-5700) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5700_5725_ENMO_total` | Minutes in ENMO Level: [5700-5725) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5725_5750_ENMO_total` | Minutes in ENMO Level: [5725-5750) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5750_5775_ENMO_total` | Minutes in ENMO Level: [5750-5775) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5775_5800_ENMO_total` | Minutes in ENMO Level: [5775-5800) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5800_5825_ENMO_total` | Minutes in ENMO Level: [5800-5825) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5825_5850_ENMO_total` | Minutes in ENMO Level: [5825-5850) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5850_5875_ENMO_total` | Minutes in ENMO Level: [5850-5875) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5875_5900_ENMO_total` | Minutes in ENMO Level: [5875-5900) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5900_5925_ENMO_total` | Minutes in ENMO Level: [5900-5925) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5925_5950_ENMO_total` | Minutes in ENMO Level: [5925-5950) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5950_5975_ENMO_total` | Minutes in ENMO Level: [5950-5975) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_5975_6000_ENMO_total` | Minutes in ENMO Level: [5975-6000) mg | `Numeric(Byte)` | `%9.0g` |
| `GGIR_6000_15000_ENMO_total` | Minutes in ENMO Level: [6000-15000) mg | `Numeric(Byte)` | `%9.0g` |

### `gv_big5` - Big Five traits

- Dataset: `sharew8_rel9-0-0_gv_big5.dta`
- Read with: `ps.read_share_module("gv_big5", wave=8)`
- Rows: 53,695
- Variables: 11
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `bfi10_extra` | Extraversion (Big Five personality inventory) | `Numeric(Float)` | `%9.0g` |
| `bfi10_agree` | Agreeableness (Big Five personality inventory) | `Numeric(Float)` | `%9.0g` |
| `bfi10_consc` | Conscientiousness (Big Five personality inventory) | `Numeric(Float)` | `%9.0g` |
| `bfi10_neuro` | Neuroticism (Big Five personality inventory) | `Numeric(Float)` | `%9.0g` |
| `bfi10_open` | Openness (Big Five personality inventory) | `Numeric(Float)` | `%9.0g` |

### `gv_children` - Generated child-level summaries

- Dataset: `sharew8_rel9-0-0_gv_children.dta`
- Read with: `ps.read_share_module("gv_children", wave=8)`
- Rows: 53,695
- Variables: 947
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `childid_1` | Child identifier (fix across modules and waves): Child 1 | `Str(14)` | `%14s` |
| `childid_2` | Child identifier (fix across modules and waves): Child 2 | `Str(14)` | `%14s` |
| `childid_3` | Child identifier (fix across modules and waves): Child 3 | `Str(14)` | `%14s` |
| `childid_4` | Child identifier (fix across modules and waves): Child 4 | `Str(14)` | `%14s` |
| `childid_5` | Child identifier (fix across modules and waves): Child 5 | `Str(14)` | `%14s` |
| `childid_6` | Child identifier (fix across modules and waves): Child 6 | `Str(14)` | `%14s` |
| `childid_7` | Child identifier (fix across modules and waves): Child 7 | `Str(14)` | `%14s` |
| `childid_8` | Child identifier (fix across modules and waves): Child 8 | `Str(14)` | `%14s` |
| `childid_9` | Child identifier (fix across modules and waves): Child 9 | `Str(14)` | `%14s` |
| `childid_10` | Child identifier (fix across modules and waves): Child 10 | `Str(14)` | `%14s` |
| `childid_11` | Child identifier (fix across modules and waves): Child 11 | `Str(14)` | `%14s` |
| `childid_12` | Child identifier (fix across modules and waves): Child 12 | `Str(14)` | `%14s` |
| `childid_13` | Child identifier (fix across modules and waves): Child 13 | `Str(14)` | `%14s` |
| `childid_14` | Child identifier (fix across modules and waves): Child 14 | `Str(14)` | `%14s` |
| `childid_15` | Child identifier (fix across modules and waves): Child 15 | `Str(14)` | `%14s` |
| `childid_16` | Child identifier (fix across modules and waves): Child 16 | `Str(14)` | `%14s` |
| `childid_17` | Child identifier (fix across modules and waves): Child 17 | `Str(14)` | `%14s` |
| `childid_18` | Child identifier (fix across modules and waves): Child 18 | `Str(14)` | `%14s` |
| `childid_19` | Child identifier (fix across modules and waves): Child 19 | `Str(1)` | `%9s` |
| `childid_20` | Child identifier (fix across modules and waves): Child 20 | `Str(14)` | `%14s` |
| `ch001_` | Number of children | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_1` | Child gender, based on ch005_1 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_2` | Child gender, based on ch005_2 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_3` | Child gender, based on ch005_3 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_4` | Child gender, based on ch005_4 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_5` | Child gender, based on ch005_5 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_6` | Child gender, based on ch005_6 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_7` | Child gender, based on ch005_7 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_8` | Child gender, based on ch005_8 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_9` | Child gender, based on ch005_9 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_10` | Child gender, based on ch005_10 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_11` | Child gender, based on ch005_11 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_12` | Child gender, based on ch005_12 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_13` | Child gender, based on ch005_13 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_14` | Child gender, based on ch005_14 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_15` | Child gender, based on ch005_15 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_16` | Child gender, based on ch005_16 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_17` | Child gender, based on ch005_17 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_18` | Child gender, based on ch005_18 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_19` | Child gender, based on ch005_19 | `Numeric(Byte)` | `%12.0g` |
| `ch_gender_20` | Child gender, based on ch005_20 | `Numeric(Byte)` | `%12.0g` |
| `ch_yrbirth_1` | Child year of birth, based on ch006_1 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_2` | Child year of birth, based on ch006_2 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_3` | Child year of birth, based on ch006_3 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_4` | Child year of birth, based on ch006_4 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_5` | Child year of birth, based on ch006_5 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_6` | Child year of birth, based on ch006_6 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_7` | Child year of birth, based on ch006_7 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_8` | Child year of birth, based on ch006_8 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_9` | Child year of birth, based on ch006_9 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_10` | Child year of birth, based on ch006_10 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_11` | Child year of birth, based on ch006_11 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_12` | Child year of birth, based on ch006_12 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_13` | Child year of birth, based on ch006_13 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_14` | Child year of birth, based on ch006_14 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_15` | Child year of birth, based on ch006_15 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_16` | Child year of birth, based on ch006_16 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_17` | Child year of birth, based on ch006_17 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_18` | Child year of birth, based on ch006_18 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_19` | Child year of birth, based on ch006_19 | `Numeric(Byte)` | `%10.0g` |
| `ch_yrbirth_20` | Child year of birth, based on ch006_20 | `Numeric(Int)` | `%10.0g` |
| `ch_relation_1` | Relation to child 1, based on ch302_, ch303_1 and ch102_1 to ch108_1 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_2` | Relation to child 2, based on ch302_, ch303_2 and ch102_2 to ch108_2 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_3` | Relation to child 3, based on ch302_, ch303_3 and ch102_3 to ch108_3 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_4` | Relation to child 4, based on ch302_, ch303_4 and ch102_4 to ch108_4 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_5` | Relation to child 5, based on ch302_, ch303_5 and ch102_5 to ch108_5 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_6` | Relation to child 6, based on ch302_, ch303_6 and ch102_6 to ch108_6 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_7` | Relation to child 7, based on ch302_, ch303_7 and ch102_7 to ch108_7 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_8` | Relation to child 8, based on ch302_, ch303_8 and ch102_8 to ch108_8 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_9` | Relation to child 9, based on ch302_, ch303_9 and ch102_9 to ch108_9 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_10` | Relation to child 10, based on ch302_, ch303_10 and ch102_10 to ch108_10 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_11` | Relation to child 11, based on ch302_, ch303_11 and ch102_11 to ch108_11 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_12` | Relation to child 12, based on ch302_, ch303_12 and ch102_12 to ch108_12 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_13` | Relation to child 13, based on ch302_, ch303_13 and ch102_13 to ch108_13 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_14` | Relation to child 14, based on ch302_, ch303_14 and ch102_14 to ch108_14 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_15` | Relation to child 15, based on ch302_, ch303_15 and ch102_15 to ch108_15 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_16` | Relation to child 16, based on ch302_, ch303_16 and ch102_16 to ch108_16 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_17` | Relation to child 17, based on ch302_, ch303_17 and ch102_17 to ch108_17 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_18` | Relation to child 18, based on ch302_, ch303_18 and ch102_18 to ch108_18 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_19` | Relation to child 19, based on ch302_, ch303_19 and ch102_19 to ch108_19 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_20` | Relation to child 20, based on ch302_, ch303_20 and ch102_20 to ch108_20 | `Numeric(Byte)` | `%43.0g` |
| `ch_contact_1` | Contact to child 1, based on ch014_1 & sn007_1 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_2` | Contact to child 2, based on ch014_2 & sn007_2 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_3` | Contact to child 3, based on ch014_3 & sn007_3 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_4` | Contact to child 4, based on ch014_4 & sn007_4 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_5` | Contact to child 5, based on ch014_5 & sn007_5 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_6` | Contact to child 6, based on ch014_6 & sn007_6 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_7` | Contact to child 7, based on ch014_7 & sn007_7 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_8` | Contact to child 8, based on ch014_8 & sn007_8 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_9` | Contact to child 9, based on ch014_9 & sn007_9 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_10` | Contact to child 10, based on ch014_10 & sn007_10 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_11` | Contact to child 11, based on ch014_11 & sn007_11 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_12` | Contact to child 12, based on ch014_12 & sn007_12 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_13` | Contact to child 13, based on ch014_13 & sn007_13 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_14` | Contact to child 14, based on ch014_14 & sn007_14 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_15` | Contact to child 15, based on ch014_15 & sn007_15 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_16` | Contact to child 16, based on ch014_16 & sn007_16 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_17` | Contact to child 17, based on ch014_17 & sn007_17 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_18` | Contact to child 18, based on ch014_18 & sn007_18 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_19` | Contact to child 19, based on ch014_19 & sn007_19 | `Numeric(Byte)` | `%30.0g` |
| `ch_contact_20` | Contact to child 20, based on ch014_20 & sn007_20 | `Numeric(Byte)` | `%30.0g` |
| `ch_proximity_1` | Proximity to child 1, based on ch007_1, ch526_1 or sn006_1 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_2` | Proximity to child 2, based on ch007_2, ch526_2 or sn006_2 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_3` | Proximity to child 3, based on ch007_3, ch526_3 or sn006_3 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_4` | Proximity to child 4, based on ch007_4, ch526_4 or sn006_4 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_5` | Proximity to child 5, based on ch007_5, ch526_5 or sn006_5 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_6` | Proximity to child 6, based on ch007_6, ch526_6 or sn006_6 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_7` | Proximity to child 7, based on ch007_7, ch526_7 or sn006_7 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_8` | Proximity to child 8, based on ch007_8, ch526_8 or sn006_8 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_9` | Proximity to child 9, based on ch007_9, ch526_9 or sn006_9 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_10` | Proximity to child 10, based on ch007_10, ch526_10 or sn006_10 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_11` | Proximity to child 11, based on ch007_11, ch526_11 or sn006_11 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_12` | Proximity to child 12, based on ch007_12, ch526_12 or sn006_12 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_13` | Proximity to child 13, based on ch007_13, ch526_13 or sn006_13 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_14` | Proximity to child 14, based on ch007_14, ch526_14 or sn006_14 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_15` | Proximity to child 15, based on ch007_15, ch526_15 or sn006_15 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_16` | Proximity to child 16, based on ch007_16, ch526_16 or sn006_16 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_17` | Proximity to child 17, based on ch007_17, ch526_17 or sn006_17 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_18` | Proximity to child 18, based on ch007_18, ch526_18 or sn006_18 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_19` | Proximity to child 19, based on ch007_19, ch526_19 or sn006_19 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_20` | Proximity to child 20, based on ch007_20, ch526_20 or sn006_20 | `Numeric(Byte)` | `%48.0g` |
| `ch_move_out_year_1` | Year when child 1 moved out, based on ch015_1 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_2` | Year when child 2 moved out, based on ch015_2 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_3` | Year when child 3 moved out, based on ch015_3 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_4` | Year when child 4 moved out, based on ch015_4 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_5` | Year when child 5 moved out, based on ch015_5 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_6` | Year when child 6 moved out, based on ch015_6 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_7` | Year when child 7 moved out, based on ch015_7 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_8` | Year when child 8 moved out, based on ch015_8 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_9` | Year when child 9 moved out, based on ch015_9 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_10` | Year when child 10 moved out, based on ch015_10 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_11` | Year when child 11 moved out, based on ch015_11 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_12` | Year when child 12 moved out, based on ch015_12 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_13` | Year when child 13 moved out, based on ch015_13 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_14` | Year when child 14 moved out, based on ch015_14 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_15` | Year when child 15 moved out, based on ch015_15 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_16` | Year when child 16 moved out, based on ch015_16 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_17` | Year when child 17 moved out, based on ch015_17 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_18` | Year when child 18 moved out, based on ch015_18 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_19` | Year when child 19 moved out, based on ch015_19 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_20` | Year when child 20 moved out, based on ch015_20 | `Numeric(Byte)` | `%33.0g` |
| `ch_marital_status_1` | Marital status of child 1, based on ch012_1 & ch516_1 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_2` | Marital status of child 2, based on ch012_2 & ch516_2 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_3` | Marital status of child 3, based on ch012_3 & ch516_3 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_4` | Marital status of child 4, based on ch012_4 & ch516_4 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_5` | Marital status of child 5, based on ch012_5 & ch516_5 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_6` | Marital status of child 6, based on ch012_6 & ch516_6 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_7` | Marital status of child 7, based on ch012_7 & ch516_7 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_8` | Marital status of child 8, based on ch012_8 & ch516_8 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_9` | Marital status of child 9, based on ch012_9 & ch516_9 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_10` | Marital status of child 10, based on ch012_10 & ch516_10 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_11` | Marital status of child 11, based on ch012_11 & ch516_11 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_12` | Marital status of child 12, based on ch012_12 & ch516_12 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_13` | Marital status of child 13, based on ch012_13 & ch516_13 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_14` | Marital status of child 14, based on ch012_14 & ch516_14 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_15` | Marital status of child 15, based on ch012_15 & ch516_15 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_16` | Marital status of child 16, based on ch012_16 & ch516_16 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_17` | Marital status of child 17, based on ch012_17 & ch516_17 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_18` | Marital status of child 18, based on ch012_18 & ch516_18 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_19` | Marital status of child 19, based on ch012_19 & ch516_19 | `Numeric(Byte)` | `%59.0g` |
| `ch_marital_status_20` | Marital status of child 20, based on ch012_20 & ch516_20 | `Numeric(Byte)` | `%59.0g` |
| `ch_partner_status_1` | Relationship status of child 1 (if not married/reg.p.), based on ch013_1 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_2` | Relationship status of child 2 (if not married/reg.p.), based on ch013_2 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_3` | Relationship status of child 3 (if not married/reg.p.), based on ch013_3 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_4` | Relationship status of child 4 (if not married/reg.p.), based on ch013_4 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_5` | Relationship status of child 5 (if not married/reg.p.), based on ch013_5 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_6` | Relationship status of child 6 (if not married/reg.p.), based on ch013_6 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_7` | Relationship status of child 7 (if not married/reg.p.), based on ch013_7 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_8` | Relationship status of child 8 (if not married/reg.p.), based on ch013_8 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_9` | Relationship status of child 9 (if not married/reg.p.), based on ch013_9 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_10` | Relationship status of child 10 (if not married/reg.p.), based on ch013_10 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_11` | Relationship status of child 11 (if not married/reg.p.), based on ch013_11 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_12` | Relationship status of child 12 (if not married/reg.p.), based on ch013_12 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_13` | Relationship status of child 13 (if not married/reg.p.), based on ch013_13 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_14` | Relationship status of child 14 (if not married/reg.p.), based on ch013_14 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_15` | Relationship status of child 15 (if not married/reg.p.), based on ch013_15 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_16` | Relationship status of child 16 (if not married/reg.p.), based on ch013_16 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_17` | Relationship status of child 17 (if not married/reg.p.), based on ch013_17 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_18` | Relationship status of child 18 (if not married/reg.p.), based on ch013_18 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_19` | Relationship status of child 19 (if not married/reg.p.), based on ch013_19 | `Numeric(Byte)` | `%10.0g` |
| `ch_partner_status_20` | Relationship status of child 20 (if not married/reg.p.), based on ch013_20 | `Numeric(Byte)` | `%10.0g` |
| `ch_closeness_1` | Emotional closeness to child 1 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_2` | Emotional closeness to child 2 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_3` | Emotional closeness to child 3 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_4` | Emotional closeness to child 4 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_5` | Emotional closeness to child 5 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_6` | Emotional closeness to child 6 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_7` | Emotional closeness to child 7 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_8` | Emotional closeness to child 8 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_9` | Emotional closeness to child 9 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_10` | Emotional closeness to child 10 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_11` | Emotional closeness to child 11 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_12` | Emotional closeness to child 12 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_13` | Emotional closeness to child 13 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_14` | Emotional closeness to child 14 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_15` | Emotional closeness to child 15 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_16` | Emotional closeness to child 16 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_17` | Emotional closeness to child 17 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_18` | Emotional closeness to child 18 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_19` | Emotional closeness to child 19 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_closeness_20` | Emotional closeness to child 20 (only if child in SN) | `Numeric(Byte)` | `%39.0g` |
| `ch_occupation_1` | Occupational status of child 1, based on ch016_1 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_2` | Occupational status of child 2, based on ch016_2 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_3` | Occupational status of child 3, based on ch016_3 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_4` | Occupational status of child 4, based on ch016_4 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_5` | Occupational status of child 5, based on ch016_5 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_6` | Occupational status of child 6, based on ch016_6 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_7` | Occupational status of child 7, based on ch016_7 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_8` | Occupational status of child 8, based on ch016_8 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_9` | Occupational status of child 9, based on ch016_9 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_10` | Occupational status of child 10, based on ch016_10 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_11` | Occupational status of child 11, based on ch016_11 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_12` | Occupational status of child 12, based on ch016_12 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_13` | Occupational status of child 13, based on ch016_13 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_14` | Occupational status of child 14, based on ch016_14 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_15` | Occupational status of child 15, based on ch016_15 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_16` | Occupational status of child 16, based on ch016_16 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_17` | Occupational status of child 17, based on ch016_17 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_18` | Occupational status of child 18, based on ch016_18 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_19` | Occupational status of child 19, based on ch016_19 | `Numeric(Byte)` | `%61.0g` |
| `ch_occupation_20` | Occupational status of child 20, based on ch016_20 | `Numeric(Byte)` | `%61.0g` |
| `ch_number_of_children_1` | Number of children child 1, based on ch019_1 & ch519_1 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_2` | Number of children child 2, based on ch019_2 & ch519_2 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_3` | Number of children child 3, based on ch019_3 & ch519_3 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_4` | Number of children child 4, based on ch019_4 & ch519_4 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_5` | Number of children child 5, based on ch019_5 & ch519_5 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_6` | Number of children child 6, based on ch019_6 & ch519_6 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_7` | Number of children child 7, based on ch019_7 & ch519_7 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_8` | Number of children child 8, based on ch019_8 & ch519_8 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_9` | Number of children child 9, based on ch019_9 & ch519_9 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_10` | Number of children child 10, based on ch019_10 & ch519_10 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_11` | Number of children child 11, based on ch019_11 & ch519_11 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_12` | Number of children child 12, based on ch019_12 & ch519_12 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_13` | Number of children child 13, based on ch019_13 & ch519_13 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_14` | Number of children child 14, based on ch019_14 & ch519_14 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_15` | Number of children child 15, based on ch019_15 & ch519_15 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_16` | Number of children child 16, based on ch019_16 & ch519_16 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_17` | Number of children child 17, based on ch019_17 & ch519_17 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_18` | Number of children child 18, based on ch019_18 & ch519_18 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_19` | Number of children child 19, based on ch019_19 & ch519_19 | `Numeric(Byte)` | `%10.0g` |
| `ch_number_of_children_20` | Number of children child 20, based on ch019_20 & ch519_20 | `Numeric(Byte)` | `%10.0g` |
| `ch_yrbirth_youngest_child_1` | Yrbirth youngest child of child 1, based on ch020_1 & ch520_1 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_2` | Yrbirth youngest child of child 2, based on ch020_2 & ch520_2 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_3` | Yrbirth youngest child of child 3, based on ch020_3 & ch520_3 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_4` | Yrbirth youngest child of child 4, based on ch020_4 & ch520_4 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_5` | Yrbirth youngest child of child 5, based on ch020_5 & ch520_5 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_6` | Yrbirth youngest child of child 6, based on ch020_6 & ch520_6 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_7` | Yrbirth youngest child of child 7, based on ch020_7 & ch520_7 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_8` | Yrbirth youngest child of child 8, based on ch020_8 & ch520_8 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_9` | Yrbirth youngest child of child 9, based on ch020_9 & ch520_9 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_10` | Yrbirth youngest child of child 10, based on ch020_10 & ch520_10 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_11` | Yrbirth youngest child of child 11, based on ch020_11 & ch520_11 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_12` | Yrbirth youngest child of child 12, based on ch020_12 & ch520_12 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_13` | Yrbirth youngest child of child 13, based on ch020_13 & ch520_13 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_14` | Yrbirth youngest child of child 14, based on ch020_14 & ch520_14 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_15` | Yrbirth youngest child of child 15, based on ch020_15 & ch520_15 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_16` | Yrbirth youngest child of child 16, based on ch020_16 & ch520_16 | `Numeric(Byte)` | `%15.0g` |
| `ch_yrbirth_youngest_child_17` | Yrbirth youngest child of child 17, based on ch020_17 & ch520_17 | `Numeric(Byte)` | `%15.0g` |
| `ch_yrbirth_youngest_child_18` | Yrbirth youngest child of child 18, based on ch020_18 & ch520_18 | `Numeric(Byte)` | `%15.0g` |
| `ch_yrbirth_youngest_child_19` | Yrbirth youngest child of child 19, based on ch020_19 & ch520_19 | `Numeric(Byte)` | `%15.0g` |
| `ch_yrbirth_youngest_child_20` | Yrbirth youngest child of child 20, based on ch020_20 & ch520_20 | `Numeric(Int)` | `%15.0g` |
| `ch_babysit_1` | Looked after child of child 1, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_2` | Looked after child of child 2, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_3` | Looked after child of child 3, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_4` | Looked after child of child 4, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_5` | Looked after child of child 5, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_6` | Looked after child of child 6, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_7` | Looked after child of child 7, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_8` | Looked after child of child 8, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_9` | Looked after child of child 9, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_10` | Looked after child of child 10, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_11` | Looked after child of child 11, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_12` | Looked after child of child 12, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_13` | Looked after child of child 13, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_14` | Looked after child of child 14, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_15` | Looked after child of child 15, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_16` | Looked after child of child 16, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_17` | Looked after child of child 17, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_18` | Looked after child of child 18, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_19` | Looked after child of child 19, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_babysit_20` | Looked after child of child 20, based on sp015* | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_1` | Financial gift given to child 1 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_2` | Financial gift given to child 2 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_3` | Financial gift given to child 3 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_4` | Financial gift given to child 4 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_5` | Financial gift given to child 5 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_6` | Financial gift given to child 6 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_7` | Financial gift given to child 7 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_8` | Financial gift given to child 8 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_9` | Financial gift given to child 9 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_10` | Financial gift given to child 10 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_11` | Financial gift given to child 11 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_12` | Financial gift given to child 12 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_13` | Financial gift given to child 13 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_14` | Financial gift given to child 14 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_15` | Financial gift given to child 15 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_16` | Financial gift given to child 16 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_17` | Financial gift given to child 17 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_18` | Financial gift given to child 18 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_19` | Financial gift given to child 19 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_gave_20` | Financial gift given to child 20 (based on ft032_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_1` | Financial gift received from child 1 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_2` | Financial gift received from child 2 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_3` | Financial gift received from child 3 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_4` | Financial gift received from child 4 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_5` | Financial gift received from child 5 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_6` | Financial gift received from child 6 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_7` | Financial gift received from child 7 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_8` | Financial gift received from child 8 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_9` | Financial gift received from child 9 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_10` | Financial gift received from child 10 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_11` | Financial gift received from child 11 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_12` | Financial gift received from child 12 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_13` | Financial gift received from child 13 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_14` | Financial gift received from child 14 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_15` | Financial gift received from child 15 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_16` | Financial gift received from child 16 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_17` | Financial gift received from child 17 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_18` | Financial gift received from child 18 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_19` | Financial gift received from child 19 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_fin_received_20` | Financial gift received from child 20 (based on ft034_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_1` | Gift received from child 1 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_2` | Gift received from child 2 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_3` | Gift received from child 3 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_4` | Gift received from child 4 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_5` | Gift received from child 5 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_6` | Gift received from child 6 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_7` | Gift received from child 7 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_8` | Gift received from child 8 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_9` | Gift received from child 9 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_10` | Gift received from child 10 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_11` | Gift received from child 11 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_12` | Gift received from child 12 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_13` | Gift received from child 13 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_14` | Gift received from child 14 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_15` | Gift received from child 15 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_16` | Gift received from child 16 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_17` | Gift received from child 17 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_18` | Gift received from child 18 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_19` | Gift received from child 19 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_received_20` | Gift received from child 20 (based on ft036_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_1` | Gift given to child 1 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_2` | Gift given to child 2 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_3` | Gift given to child 3 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_4` | Gift given to child 4 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_5` | Gift given to child 5 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_6` | Gift given to child 6 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_7` | Gift given to child 7 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_8` | Gift given to child 8 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_9` | Gift given to child 9 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_10` | Gift given to child 10 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_11` | Gift given to child 11 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_12` | Gift given to child 12 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_13` | Gift given to child 13 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_14` | Gift given to child 14 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_15` | Gift given to child 15 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_16` | Gift given to child 16 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_17` | Gift given to child 17 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_18` | Gift given to child 18 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_19` | Gift given to child 19 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_gift_gave_20` | Gift given to child 20 (based on ft038_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_1` | Outside HH: received help from child 1 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_2` | Outside HH: received help from child 2 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_3` | Outside HH: received help from child 3 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_4` | Outside HH: received help from child 4 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_5` | Outside HH: received help from child 5 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_6` | Outside HH: received help from child 6 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_7` | Outside HH: received help from child 7 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_8` | Outside HH: received help from child 8 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_9` | Outside HH: received help from child 9 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_10` | Outside HH: received help from child 10 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_11` | Outside HH: received help from child 11 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_12` | Outside HH: received help from child 12 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_13` | Outside HH: received help from child 13 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_14` | Outside HH: received help from child 14 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_15` | Outside HH: received help from child 15 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_16` | Outside HH: received help from child 16 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_17` | Outside HH: received help from child 17 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_18` | Outside HH: received help from child 18 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_19` | Outside HH: received help from child 19 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_receive_care_20` | Outside HH: received help from child 20 (based on sp027_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_1` | Outside HH: gave help to child 1 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_2` | Outside HH: gave help to child 2 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_3` | Outside HH: gave help to child 3 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_4` | Outside HH: gave help to child 4 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_5` | Outside HH: gave help to child 5 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_6` | Outside HH: gave help to child 6 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_7` | Outside HH: gave help to child 7 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_8` | Outside HH: gave help to child 8 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_9` | Outside HH: gave help to child 9 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_10` | Outside HH: gave help to child 10 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_11` | Outside HH: gave help to child 11 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_12` | Outside HH: gave help to child 12 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_13` | Outside HH: gave help to child 13 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_14` | Outside HH: gave help to child 14 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_15` | Outside HH: gave help to child 15 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_16` | Outside HH: gave help to child 16 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_17` | Outside HH: gave help to child 17 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_18` | Outside HH: gave help to child 18 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_19` | Outside HH: gave help to child 19 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_outhh_gave_care_20` | Outside HH: gave help to child 20 (based on sp029_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_1` | Inside HH: gave help to child 1 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_2` | Inside HH: gave help to child 2 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_3` | Inside HH: gave help to child 3 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_4` | Inside HH: gave help to child 4 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_5` | Inside HH: gave help to child 5 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_6` | Inside HH: gave help to child 6 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_7` | Inside HH: gave help to child 7 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_8` | Inside HH: gave help to child 8 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_9` | Inside HH: gave help to child 9 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_10` | Inside HH: gave help to child 10 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_11` | Inside HH: gave help to child 11 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_12` | Inside HH: gave help to child 12 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_13` | Inside HH: gave help to child 13 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_14` | Inside HH: gave help to child 14 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_15` | Inside HH: gave help to child 15 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_16` | Inside HH: gave help to child 16 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_17` | Inside HH: gave help to child 17 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_18` | Inside HH: gave help to child 18 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_19` | Inside HH: gave help to child 19 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_gave_care_20` | Inside HH: gave help to child 20 (based on sp031_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_1` | Inside HH: Received help from child 1 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_2` | Inside HH: Received help from child 2 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_3` | Inside HH: Received help from child 3 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_4` | Inside HH: Received help from child 4 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_5` | Inside HH: Received help from child 5 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_6` | Inside HH: Received help from child 6 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_7` | Inside HH: Received help from child 7 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_8` | Inside HH: Received help from child 8 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_9` | Inside HH: Received help from child 9 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_10` | Inside HH: Received help from child 10 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_11` | Inside HH: Received help from child 11 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_12` | Inside HH: Received help from child 12 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_13` | Inside HH: Received help from child 13 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_14` | Inside HH: Received help from child 14 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_15` | Inside HH: Received help from child 15 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_16` | Inside HH: Received help from child 16 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_17` | Inside HH: Received help from child 17 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_18` | Inside HH: Received help from child 18 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_19` | Inside HH: Received help from child 19 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_hh_receive_care_20` | Inside HH: Received help from child 20 (based on sp033_*) | `Numeric(Byte)` | `%12.0g` |
| `ch_school_education_1` | School degree of child 1, based on ch017_1 & ch510_1 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_2` | School degree of child 2, based on ch017_2 & ch510_2 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_3` | School degree of child 3, based on ch017_3 & ch510_3 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_4` | School degree of child 4, based on ch017_4 & ch510_4 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_5` | School degree of child 5, based on ch017_5 & ch510_5 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_6` | School degree of child 6, based on ch017_6 & ch510_6 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_7` | School degree of child 7, based on ch017_7 & ch510_7 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_8` | School degree of child 8, based on ch017_8 & ch510_8 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_9` | School degree of child 9, based on ch017_9 & ch510_9 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_10` | School degree of child 10, based on ch017_10 & ch510_10 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_11` | School degree of child 11, based on ch017_11 & ch510_11 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_12` | School degree of child 12, based on ch017_12 & ch510_12 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_13` | School degree of child 13, based on ch017_13 & ch510_13 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_14` | School degree of child 14, based on ch017_14 & ch510_14 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_15` | School degree of child 15, based on ch017_15 & ch510_15 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_16` | School degree of child 16, based on ch017_16 & ch510_16 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_17` | School degree of child 17, based on ch017_17 & ch510_17 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_18` | School degree of child 18, based on ch017_18 & ch510_18 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_19` | School degree of child 19, based on ch017_19 & ch510_19 | `Numeric(Byte)` | `%167.0g` |
| `ch_school_education_20` | School degree of child 20, based on ch017_20 & ch510_20 | `Numeric(Byte)` | `%167.0g` |
| `ch_further_education_1_1` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_2` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_3` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_4` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_5` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_6` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_7` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_8` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_9` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_10` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_11` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_12` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_13` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_14` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_15` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_16` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_17` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_18` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_19` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_20` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_21` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_1_22` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_1` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_2` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_3` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_4` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_5` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_6` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_7` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_8` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_9` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_10` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_11` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_12` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_13` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_14` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_15` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_16` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_17` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_18` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_19` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_20` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_21` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_2_22` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_1` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_2` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_3` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_4` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_5` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_6` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_7` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_8` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_9` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_10` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_11` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_12` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_13` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_14` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_15` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_16` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_17` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_18` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_19` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_20` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_21` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_3_22` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_1` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_2` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_3` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_4` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_5` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_6` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_7` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_8` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_9` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_10` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_11` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_12` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_13` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_14` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_15` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_16` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_17` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_18` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_19` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_20` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_21` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_4_22` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_1` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_2` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_3` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_4` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_5` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_6` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_7` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_8` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_9` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_10` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_11` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_12` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_13` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_14` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_15` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_16` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_17` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_18` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_19` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_20` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_21` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_5_22` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_1` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_2` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_3` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_4` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_5` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_6` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_7` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_8` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_9` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_10` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_11` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_12` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_13` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_14` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_15` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_16` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_17` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_18` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_19` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_20` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_21` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_6_22` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_1` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_2` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_3` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_4` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_5` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_6` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_7` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_8` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_9` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_10` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_11` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_12` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_13` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_14` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_15` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_16` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_17` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_18` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_19` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_20` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_21` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_7_22` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_1` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_2` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_3` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_4` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_5` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_6` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_7` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_8` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_9` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_10` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_11` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_12` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_13` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_14` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_15` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_16` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_17` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_18` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_19` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_20` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_21` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_8_22` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_1` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_2` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_3` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_4` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_5` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_6` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_7` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_8` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_9` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_10` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_11` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_12` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_13` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_14` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_15` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_16` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_17` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_18` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_19` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_20` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_21` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_9_22` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_1` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_2` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_3` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_4` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_5` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_6` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_7` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_8` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_9` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_10` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_11` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_12` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_13` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_14` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_15` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_16` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_17` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_18` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_19` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_20` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_21` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_10_22` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_1` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_2` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_3` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_4` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_5` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_6` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_7` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_8` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_9` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_10` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_11` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_12` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_13` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_14` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_15` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_16` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_17` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_18` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_19` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_20` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_21` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_11_22` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_1` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_2` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_3` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_4` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_5` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_6` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_7` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_8` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_9` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_10` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_11` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_12` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_13` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_14` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_15` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_16` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_17` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_18` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_19` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_20` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_21` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_12_22` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_1` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_2` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_3` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_4` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_5` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_6` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_7` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_8` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_9` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_10` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_11` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_12` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_13` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_14` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_15` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_16` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_17` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_18` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_19` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_20` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_21` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_13_22` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_1` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_2` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_3` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_4` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_5` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_6` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_7` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_8` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_9` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_10` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_11` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_12` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_13` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_14` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_15` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_16` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_17` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_18` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_19` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_20` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_21` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_14_22` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_1` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_2` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_3` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_4` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_5` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_6` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_7` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_8` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_9` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_10` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_11` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_12` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_13` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_14` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_15` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_16` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_17` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_18` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_19` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_20` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_21` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_15_22` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_1` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_2` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_3` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_4` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_5` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_6` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_7` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_8` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_9` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_10` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_11` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_12` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_13` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_14` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_15` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_16` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_17` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_18` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_19` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_20` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_21` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_16_22` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_1` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_2` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_3` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_4` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_5` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_6` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_7` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_8` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_9` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_10` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_11` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_12` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_13` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_14` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_15` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_16` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_17` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_18` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_19` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_20` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_21` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_17_22` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_1` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_2` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_3` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_4` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_5` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_6` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_7` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_8` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_9` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_10` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_11` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_12` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_13` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_14` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_15` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_16` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_17` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_18` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_19` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_20` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_21` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_18_22` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_1` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_2` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_3` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_4` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_5` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_6` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_7` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_8` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_9` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_10` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_11` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_12` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_13` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_14` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_15` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_16` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_17` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_18` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_19` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_20` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_21` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_19_22` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_1` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_2` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_3` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_4` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_5` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_6` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_7` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_8` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_9` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_10` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_11` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_12` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_13` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_14` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_15` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_16` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_17` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_18` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_19` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_20` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_21` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `ch_further_education_20_22` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%112.0g` |
| `child_sn_loop_1` | Child 1 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_2` | Child 2 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_3` | Child 3 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_4` | Child 4 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_5` | Child 5 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_6` | Child 6 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_7` | Child 7 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_8` | Child 8 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_9` | Child 9 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_10` | Child 10 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_11` | Child 11 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_12` | Child 12 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_13` | Child 13 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_14` | Child 14 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_15` | Child 15 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_16` | Child 16 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_17` | Child 17 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_18` | Child 18 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_19` | Child 19 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_sn_loop_20` | Child 20 mentioned as social network member (loop) | `Numeric(Byte)` | `%9.0g` |
| `child_dead_1` | Indicator: Child 1 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_2` | Indicator: Child 2 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_3` | Indicator: Child 3 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_4` | Indicator: Child 4 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_5` | Indicator: Child 5 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_6` | Indicator: Child 6 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_7` | Indicator: Child 7 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_8` | Indicator: Child 8 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_9` | Indicator: Child 9 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_10` | Indicator: Child 10 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_11` | Indicator: Child 11 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_12` | Indicator: Child 12 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_13` | Indicator: Child 13 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_14` | Indicator: Child 14 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_15` | Indicator: Child 15 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_16` | Indicator: Child 16 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_17` | Indicator: Child 17 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_18` | Indicator: Child 18 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_19` | Indicator: Child 19 dead | `Numeric(Byte)` | `%11.0g` |
| `child_dead_20` | Indicator: Child 20 dead | `Numeric(Byte)` | `%11.0g` |

### `gv_exrates` - Exchange rates and PPP variables

- Dataset: `sharew8_rel9-0-0_gv_exrates.dta`
- Read with: `ps.read_share_module("gv_exrates", wave=8)`
- Rows: 29
- Variables: 76
- Key hint: `country`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `euro` | Euro country | `Numeric(Byte)` | `%15.0g` |
| `currency` | currency | `Str(16)` | `%16s` |
| `exrate_w1` | Exchange rate used for wave 1 | `Numeric(Double)` | `%14.0g` |
| `exrate_w2` | Exchange rate used for wave 2 | `Numeric(Double)` | `%14.0g` |
| `exrate_w3` | Exchange rate used for wave 3 | `Numeric(Double)` | `%14.0g` |
| `exrate_w4` | Exchange rate used for wave 4 | `Numeric(Double)` | `%14.0g` |
| `exrate_w5` | Exchange rate used for wave 5 | `Numeric(Double)` | `%14.0g` |
| `exrate_w6` | Exchange rate used for wave 6 | `Numeric(Double)` | `%14.0g` |
| `exrate_w7` | Exchange rate used for wave 7 | `Numeric(Double)` | `%14.0g` |
| `exrate_w8` | Exchange rate used for wave 8 | `Numeric(Double)` | `%14.0g` |
| `exrate_w8ca` | Exchange rate used for COVID-19 survey 1 (8ca) | `Numeric(Double)` | `%14.0g` |
| `exrate_w9ca` | Exchange rate used for COVID-19 survey 2 (9ca) | `Numeric(Double)` | `%14.0g` |
| `exrate_w9` | Exchange rate used for wave 9 | `Numeric(Double)` | `%14.0g` |
| `nomx2003` | Nominal exchange rate (national currency/Euro), annual average, 2003 | `Numeric(Double)` | `%10.0g` |
| `nomx2004` | Nominal exchange rate (national currency/Euro), annual average, 2004 | `Numeric(Double)` | `%10.0g` |
| `nomx2005` | Nominal exchange rate (national currency/Euro), annual average, 2005 | `Numeric(Double)` | `%10.0g` |
| `nomx2006` | Nominal exchange rate (national currency/Euro), annual average, 2006 | `Numeric(Double)` | `%10.0g` |
| `nomx2007` | Nominal exchange rate (national currency/Euro), annual average, 2007 | `Numeric(Double)` | `%10.0g` |
| `nomx2008` | Nominal exchange rate (national currency/Euro), annual average, 2008 | `Numeric(Double)` | `%10.0g` |
| `nomx2009` | Nominal exchange rate (national currency/Euro), annual average, 2009 | `Numeric(Double)` | `%10.0g` |
| `nomx2010` | Nominal exchange rate (national currency/Euro), annual average, 2010 | `Numeric(Double)` | `%10.0g` |
| `nomx2011` | Nominal exchange rate (national currency/Euro), annual average, 2011 | `Numeric(Double)` | `%10.0g` |
| `nomx2012` | Nominal exchange rate (national currency/Euro), annual average, 2012 | `Numeric(Double)` | `%10.0g` |
| `nomx2013` | Nominal exchange rate (national currency/Euro), annual average, 2013 | `Numeric(Double)` | `%10.0g` |
| `nomx2014` | Nominal exchange rate (national currency/Euro), annual average, 2014 | `Numeric(Double)` | `%10.0g` |
| `nomx2015` | Nominal exchange rate (national currency/Euro), annual average, 2015 | `Numeric(Double)` | `%10.0g` |
| `nomx2016` | Nominal exchange rate (national currency/Euro), annual average, 2016 | `Numeric(Double)` | `%10.0g` |
| `nomx2017` | Nominal exchange rate (national currency/Euro), annual average, 2017 | `Numeric(Double)` | `%10.0g` |
| `nomx2018` | Nominal exchange rate (national currency/Euro), annual average, 2018 | `Numeric(Double)` | `%10.0g` |
| `nomx2019` | Nominal exchange rate (national currency/Euro), annual average, 2019 | `Numeric(Double)` | `%10.0g` |
| `nomx2020` | Nominal exchange rate (national currency/Euro), annual average, 2020 | `Numeric(Double)` | `%10.0g` |
| `nomx2021` | Nominal exchange rate (national currency/Euro), annual average, 2021 | `Numeric(Double)` | `%10.0g` |
| `nomx2022` | Nominal exchange rate (national currency/Euro), annual average, 2022 | `Numeric(Double)` | `%10.0g` |
| `pppc2003` | Current PPP exchange rate (national currency/Euro), 2003 | `Numeric(Double)` | `%10.0g` |
| `pppc2004` | Current PPP exchange rate (national currency/Euro), 2004 | `Numeric(Double)` | `%10.0g` |
| `pppc2005` | Current PPP exchange rate (national currency/Euro), 2005 | `Numeric(Double)` | `%10.0g` |
| `pppc2006` | Current PPP exchange rate (national currency/Euro), 2006 | `Numeric(Double)` | `%10.0g` |
| `pppc2007` | Current PPP exchange rate (national currency/Euro), 2007 | `Numeric(Double)` | `%10.0g` |
| `pppc2008` | Current PPP exchange rate (national currency/Euro), 2008 | `Numeric(Double)` | `%10.0g` |
| `pppc2009` | Current PPP exchange rate (national currency/Euro), 2009 | `Numeric(Double)` | `%10.0g` |
| `pppc2010` | Current PPP exchange rate (national currency/Euro), 2010 | `Numeric(Double)` | `%10.0g` |
| `pppc2011` | Current PPP exchange rate (national currency/Euro), 2011 | `Numeric(Double)` | `%10.0g` |
| `pppc2012` | Current PPP exchange rate (national currency/Euro), 2012 | `Numeric(Double)` | `%10.0g` |
| `pppc2013` | Current PPP exchange rate (national currency/Euro), 2013 | `Numeric(Double)` | `%10.0g` |
| `pppc2014` | Current PPP exchange rate (national currency/Euro), 2014 | `Numeric(Double)` | `%10.0g` |
| `pppc2015` | Current PPP exchange rate (national currency/Euro), 2015 | `Numeric(Double)` | `%10.0g` |
| `pppc2016` | Current PPP exchange rate (national currency/Euro), 2016 | `Numeric(Double)` | `%10.0g` |
| `pppc2017` | Current PPP exchange rate (national currency/Euro), 2017 | `Numeric(Double)` | `%10.0g` |
| `pppc2018` | Current PPP exchange rate (national currency/Euro), 2018 | `Numeric(Double)` | `%10.0g` |
| `pppc2019` | Current PPP exchange rate (national currency/Euro), 2019 | `Numeric(Double)` | `%10.0g` |
| `pppc2020` | Current PPP exchange rate (national currency/Euro), 2020 | `Numeric(Double)` | `%10.0g` |
| `pppc2021` | Current PPP exchange rate (national currency/Euro), 2021 | `Numeric(Double)` | `%10.0g` |
| `pppc2022` | Current PPP exchange rate (national currency/Euro), 2022 | `Numeric(Double)` | `%10.0g` |
| `pppk2003` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2003 | `Numeric(Double)` | `%10.0g` |
| `pppk2004` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2004 | `Numeric(Double)` | `%10.0g` |
| `pppk2005` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2005 | `Numeric(Double)` | `%10.0g` |
| `pppk2006` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2006 | `Numeric(Double)` | `%10.0g` |
| `pppk2007` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2007 | `Numeric(Double)` | `%10.0g` |
| `pppk2008` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2008 | `Numeric(Double)` | `%10.0g` |
| `pppk2009` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2009 | `Numeric(Double)` | `%10.0g` |
| `pppk2010` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2010 | `Numeric(Double)` | `%10.0g` |
| `pppk2011` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2011 | `Numeric(Double)` | `%10.0g` |
| `pppk2012` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2012 | `Numeric(Double)` | `%10.0g` |
| `pppk2013` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2013 | `Numeric(Double)` | `%10.0g` |
| `pppk2014` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2014 | `Numeric(Double)` | `%10.0g` |
| `pppk2015` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2015 | `Numeric(Double)` | `%10.0g` |
| `pppk2016` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2016 | `Numeric(Double)` | `%10.0g` |
| `pppk2017` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2017 | `Numeric(Double)` | `%10.0g` |
| `pppk2018` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2018 | `Numeric(Double)` | `%10.0g` |
| `pppk2019` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2019 | `Numeric(Double)` | `%10.0g` |
| `pppk2020` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2020 | `Numeric(Double)` | `%10.0g` |
| `pppk2021` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2021 | `Numeric(Double)` | `%10.0g` |
| `pppk2022` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2022 | `Numeric(Double)` | `%10.0g` |
| `currency_pre` | Currency pre-euro | `Str(33)` | `%33s` |
| `exrate_pre` | Nominal exchange rate for pre-euro currencies | `Numeric(Double)` | `%14.0g` |

### `gv_health` - Generated health indicators

- Dataset: `sharew8_rel9-0-0_gv_health.dta`
- Read with: `ps.read_share_module("gv_health", wave=8)`
- Rows: 53,695
- Variables: 43
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `adl` | Number of limitations with activities of daily living (adl) | `Numeric(Byte)` | `%10.0g` |
| `adl2` | 1+ adl limitations | `Numeric(Byte)` | `%18.0g` |
| `bmi` | Body mass index | `Numeric(Float)` | `%28.0g` |
| `bmi2` | Bmi categories | `Numeric(Byte)` | `%27.0g` |
| `casp` | CASP index for quality of life and well-being | `Numeric(Byte)` | `%10.0g` |
| `cf008tot` | Ten words list learning first trial total | `Numeric(Byte)` | `%9.0g` |
| `cf016tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `chronic2w8` | 2+ chronic diseases (w8 version) | `Numeric(Byte)` | `%20.0g` |
| `chronicw8` | Number of chronic diseases (w8 version) | `Numeric(Byte)` | `%10.0g` |
| `euro1` | Depression(part of EURO-D) | `Numeric(Byte)` | `%12.0g` |
| `euro2` | Pessimism (part of EURO-D) | `Numeric(Byte)` | `%12.0g` |
| `euro3` | Suicidality (part of EURO-D) | `Numeric(Byte)` | `%12.0g` |
| `euro4` | Guilt (part of EURO-D) | `Numeric(Byte)` | `%12.0g` |
| `euro5` | Sleep (part of EURO-D) | `Numeric(Byte)` | `%12.0g` |
| `euro6` | Interest (part of EURO-D) | `Numeric(Byte)` | `%12.0g` |
| `euro7` | Irritability (part of EURO-D) | `Numeric(Byte)` | `%12.0g` |
| `euro8` | Appetite (part of EURO-D) | `Numeric(Byte)` | `%12.0g` |
| `euro9` | Fatigue (part of EURO-D) | `Numeric(Byte)` | `%12.0g` |
| `euro10` | Concentration (part of EURO-D) | `Numeric(Byte)` | `%12.0g` |
| `euro11` | Enjoyment (part of EURO-D) | `Numeric(Byte)` | `%12.0g` |
| `euro12` | Tearfulness (part of EURO-D) | `Numeric(Byte)` | `%12.0g` |
| `eurod` | Depression scale EURO-D - high is depressed | `Numeric(Byte)` | `%14.0g` |
| `eurodcat` | EURO-D caseness | `Numeric(Byte)` | `%10.0g` |
| `gali` | Limitations with activities - gali | `Numeric(Byte)` | `%11.0g` |
| `iadl` | Limitations with instrumental activities of daily living (iadl) | `Numeric(Byte)` | `%10.0g` |
| `iadl2` | 1+ iadl limitations | `Numeric(Byte)` | `%19.0g` |
| `loneliness` | Loneliness (short version of R-UCLA Loneliness Scale) - high is lonely | `Numeric(Byte)` | `%11.0g` |
| `maxgrip` | Max. of grip strength measure | `Numeric(Byte)` | `%10.0g` |
| `mobilit2` | 1+ mobility, arm function and fine motor limitations | `Numeric(Byte)` | `%10.0g` |
| `mobilit3` | 3+ mobility, arm function and fine motor limitations | `Numeric(Byte)` | `%15.0g` |
| `mobility` | Mobility, arm function and fine motor limitations | `Numeric(Byte)` | `%10.0g` |
| `numeracy` | Numeracy score: mathematical performance (percentage) | `Numeric(Byte)` | `%10.0g` |
| `numeracy2` | Numeracy score 2: mathematical performance (subtraction) | `Numeric(Byte)` | `%10.0g` |
| `orienti` | Orientation to date, month,year and day of week | `Numeric(Byte)` | `%10.0g` |
| `phactiv` | Physical inactivity | `Numeric(Byte)` | `%45.0g` |
| `sphus` | Self-perceived health - us version | `Numeric(Byte)` | `%10.0g` |
| `sphus2` | Sphus-less than very good health | `Numeric(Byte)` | `%19.0g` |

### `gv_housing` - Housing generated variables

- Dataset: `sharew8_rel9-0-0_gv_housing.dta`
- Read with: `ps.read_share_module("gv_housing", wave=8)`
- Rows: 53,695
- Variables: 10
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `areabldgi` | Area of building | `Numeric(Byte)` | `%38.0g` |
| `typebldgi6` | Type of building (since w6) | `Numeric(Byte)` | `%57.0g` |
| `nstepsi` | Number of steps to entrance | `Numeric(Byte)` | `%12.0g` |
| `nuts1_2016` | NUTS 2016 level 1: nomenclature of territorial units for statistics | `Str(40)` | `%40s` |

### `gv_imputations` - Multiple imputations

- Dataset: `sharew8_rel9-0-0_gv_imputations.dta`
- Read with: `ps.read_share_module("gv_imputations", wave=8)`
- Rows: 268,475
- Variables: 299
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `implicat` | Implicat number | `Numeric(Byte)` | `%9.0g` |
| `htype` | Household type | `Numeric(Byte)` | `%16.0g` |
| `fam_resp` | Family respondent | `Numeric(Byte)` | `%14.0g` |
| `fin_resp` | Financial respondent | `Numeric(Byte)` | `%14.0g` |
| `hou_resp` | Household respondent | `Numeric(Byte)` | `%14.0g` |
| `exrate` | Exchange rate | `Numeric(Float)` | `%9.0g` |
| `nursinghome` | Living in nursing home | `Numeric(Byte)` | `%14.0g` |
| `perho` | Percentage of house owned | `Numeric(Byte)` | `%14.0g` |
| `otrf` | Owner, tenant or rent free | `Numeric(Byte)` | `%27.0g` |
| `single` | Single | `Numeric(Byte)` | `%14.0g` |
| `couple` | Couple | `Numeric(Byte)` | `%14.0g` |
| `partner` | Partner in the couple | `Numeric(Byte)` | `%14.0g` |
| `p_nrp` | Partner of nonresponding partner | `Numeric(Byte)` | `%14.0g` |
| `sample1` | Imputation sample for single | `Numeric(Byte)` | `%14.0g` |
| `sample2` | Imputation sample for couples 2R | `Numeric(Byte)` | `%14.0g` |
| `sample3` | Imputation sample for all couples | `Numeric(Byte)` | `%14.0g` |
| `ydip` | Earnings from employment | `Numeric(Double)` | `%9.0g` |
| `yind` | Earnings from self-employment | `Numeric(Double)` | `%9.0g` |
| `ypen1` | Old age, early retirement, and survivor pensions | `Numeric(Double)` | `%9.0g` |
| `ypen2` | Private and occupational pensions | `Numeric(Double)` | `%9.0g` |
| `ypen3` | Disability pensions/benefits | `Numeric(Double)` | `%9.0g` |
| `ypen4` | Unemployment benefits/insurances | `Numeric(Double)` | `%9.0g` |
| `ypen5` | Social assistance | `Numeric(Double)` | `%9.0g` |
| `ypen6` | Sickness benefits | `Numeric(Double)` | `%9.0g` |
| `ylsp1` | LS payments from old age, early retirement, and survivor pensions | `Numeric(Double)` | `%9.0g` |
| `ylsp2` | LS payments from private and occupational pensions | `Numeric(Double)` | `%9.0g` |
| `ylsp3` | LS payments from disability pensions/benefits | `Numeric(Double)` | `%9.0g` |
| `ylsp4` | LS payments from unemployment benefits/insurances | `Numeric(Double)` | `%9.0g` |
| `ylsp5` | LS payments from social assistance | `Numeric(Double)` | `%9.0g` |
| `ylsp6` | LS payments from sickness benefits | `Numeric(Double)` | `%9.0g` |
| `yreg1` | Regular private payments | `Numeric(Double)` | `%9.0g` |
| `yreg2` | Other regular private transfers | `Numeric(Double)` | `%9.0g` |
| `ylsr1` | LS from private payments | `Numeric(Double)` | `%9.0g` |
| `ylsr2` | LS from other private transfers | `Numeric(Double)` | `%9.0g` |
| `home` | Value of main residence | `Numeric(Double)` | `%9.0g` |
| `mort` | Mortgage on main residence | `Numeric(Double)` | `%9.0g` |
| `rhre` | Rent and home-related expenditures | `Numeric(Double)` | `%9.0g` |
| `ores` | Value of real estate - Amount | `Numeric(Double)` | `%9.0g` |
| `ysrent` | Income from rent/sublet | `Numeric(Double)` | `%9.0g` |
| `yaohm` | Income from other household members | `Numeric(Double)` | `%9.0g` |
| `fahc` | Amount spent on food at home | `Numeric(Double)` | `%9.0g` |
| `fohc` | Amount spent on food outside home | `Numeric(Double)` | `%9.0g` |
| `hprf` | Value of home produced food | `Numeric(Double)` | `%9.0g` |
| `bacc` | Bank accounts | `Numeric(Double)` | `%9.0g` |
| `bsmf` | Bond, stock and mutual funds | `Numeric(Double)` | `%9.0g` |
| `ybabsmf` | Interest/dividend from bank account, bond, stock and mutual funds | `Numeric(Double)` | `%9.0g` |
| `slti` | Savings for long-term investments | `Numeric(Double)` | `%9.0g` |
| `vbus` | Value of own business | `Numeric(Double)` | `%9.0g` |
| `sbus` | Share of own business | `Numeric(Float)` | `%9.0g` |
| `car` | Value of cars | `Numeric(Double)` | `%9.0g` |
| `liab` | Financial liabilities | `Numeric(Double)` | `%9.0g` |
| `thinc2` | Total household income - Version B | `Numeric(Double)` | `%9.0g` |
| `thinc` | Total household income - Version A | `Numeric(Double)` | `%9.0g` |
| `thexp` | Total household expenditure | `Numeric(Double)` | `%9.0g` |
| `hnetw` | Household net worth | `Numeric(Double)` | `%9.0g` |
| `yincnrp` | Income from nonresponding partner | `Numeric(Double)` | `%9.0g` |
| `hrass` | Household real assets | `Numeric(Double)` | `%9.0g` |
| `hgfass` | Household gross financial assets | `Numeric(Double)` | `%9.0g` |
| `hnfass` | Household net financial assets | `Numeric(Double)` | `%9.0g` |
| `gender` | Gender | `Numeric(Byte)` | `%14.0g` |
| `age` | Age | `Numeric(Int)` | `%14.0g` |
| `age_p` | Age of partner | `Numeric(Int)` | `%14.0g` |
| `yedu` | Years of education | `Numeric(Float)` | `%20.0g` |
| `yedu_p` | Years of education of partner | `Numeric(Float)` | `%20.0g` |
| `isced` | ISCED 1997 coding of education | `Numeric(Byte)` | `%15.0g` |
| `sphus` | Self-perceived health - US scale | `Numeric(Byte)` | `%14.0g` |
| `mstat` | Marital status | `Numeric(Byte)` | `%31.0g` |
| `nchild` | Number of children | `Numeric(Byte)` | `%14.0g` |
| `ngrchild` | Number of grandchildren | `Numeric(Byte)` | `%14.0g` |
| `gali` | Limitation with activities | `Numeric(Byte)` | `%14.0g` |
| `chronic` | Number of chronic deseases | `Numeric(Byte)` | `%14.0g` |
| `eyesightr` | Eyesight reading | `Numeric(Byte)` | `%14.0g` |
| `hearing` | Hearing | `Numeric(Byte)` | `%14.0g` |
| `bmi` | Body mass index | `Numeric(Double)` | `%14.0g` |
| `weight` | Weight | `Numeric(Int)` | `%14.0g` |
| `height` | Height | `Numeric(Int)` | `%14.0g` |
| `mobility` | Mobility limitations | `Numeric(Byte)` | `%14.0g` |
| `adl` | Limitations with activities of daily living | `Numeric(Byte)` | `%14.0g` |
| `iadl` | Limitations with instrumental activities of daily living | `Numeric(Byte)` | `%14.0g` |
| `esmoked` | Ever smoked daily | `Numeric(Byte)` | `%14.0g` |
| `phinact` | Physical inactivity | `Numeric(Byte)` | `%14.0g` |
| `dairyp` | How often consume dairy products | `Numeric(Byte)` | `%21.0g` |
| `legeggs` | How often consume legumes, beans or eggs | `Numeric(Byte)` | `%21.0g` |
| `meat` | How often consume meat, fish or poultry | `Numeric(Byte)` | `%21.0g` |
| `fruit` | How often consume fruits or vegetables | `Numeric(Byte)` | `%21.0g` |
| `reading` | Self-rated reading skills | `Numeric(Byte)` | `%14.0g` |
| `writing` | Self-rated writing skills | `Numeric(Byte)` | `%14.0g` |
| `orienti` | Score of orientation in time test | `Numeric(Byte)` | `%9.0g` |
| `wllft` | Score of words list learning test - trial 1 | `Numeric(Byte)` | `%14.0g` |
| `wllst` | Score of words list learning test - trial 2 | `Numeric(Byte)` | `%14.0g` |
| `fluency` | Score of verbal fluency test | `Numeric(Byte)` | `%14.0g` |
| `numeracy` | Score of first numeracy test | `Numeric(Byte)` | `%14.0g` |
| `numeracy2` | Score of second numeracy test | `Numeric(Byte)` | `%14.0g` |
| `memory` | Score of memory test | `Numeric(Byte)` | `%14.0g` |
| `maxgrip` | Maximum of grip strength measures | `Numeric(Byte)` | `%14.0g` |
| `eurod` | EURO depression scale | `Numeric(Byte)` | `%14.0g` |
| `doctor` | Seen/Talked to medical doctor | `Numeric(Int)` | `%14.0g` |
| `hospital` | In hospital last 12 months | `Numeric(Byte)` | `%14.0g` |
| `thospital` | Times being patient in hospital | `Numeric(Byte)` | `%10.0g` |
| `nhospital` | Total nights stayed in hospital | `Numeric(Int)` | `%14.0g` |
| `cjs` | Current job situation | `Numeric(Byte)` | `%93.0g` |
| `pwork` | Did any paid work | `Numeric(Byte)` | `%14.0g` |
| `empstat` | Employee or self-employed | `Numeric(Byte)` | `%38.0g` |
| `lookjob` | Looking for job | `Numeric(Byte)` | `%14.0g` |
| `internet` | Use internet | `Numeric(Byte)` | `%14.0g` |
| `pcskill` | PC skills | `Numeric(Byte)` | `%23.0g` |
| `cjobpc` | Use PC in current job | `Numeric(Byte)` | `%14.0g` |
| `ljobpc` | Use PC in last job | `Numeric(Byte)` | `%14.0g` |
| `rhfo` | Received help from others (how many) | `Numeric(Byte)` | `%14.0g` |
| `ghto` | Given help to others (how many) | `Numeric(Byte)` | `%14.0g` |
| `ghih` | Given help in the household (how many) | `Numeric(Byte)` | `%14.0g` |
| `rhih` | Received help in the household (how many) | `Numeric(Byte)` | `%14.0g` |
| `gfg` | Number of given financial gifts 250 or more | `Numeric(Byte)` | `%14.0g` |
| `rfg` | Number of received financial gifts 250 or more | `Numeric(Byte)` | `%14.0g` |
| `rggp` | Number of received gifts, goods, properties 5000 or more | `Numeric(Byte)` | `%14.0g` |
| `gggp` | Given gift, good, property 5000 or more | `Numeric(Byte)` | `%14.0g` |
| `fdistress` | Household able to make ends meet | `Numeric(Byte)` | `%21.0g` |
| `naly` | Number of activities last year | `Numeric(Byte)` | `%14.0g` |
| `saly` | Satisfied with no activities | `Numeric(Byte)` | `%23.0g` |
| `lifesat` | Life satisfaction | `Numeric(Byte)` | `%23.0g` |
| `lifehap` | Life happiness | `Numeric(Byte)` | `%14.0g` |
| `lifex` | Living in ten years | `Numeric(Byte)` | `%14.0g` |
| `bfi10_extra` | Extraversion (Big Five personality inventory) | `Numeric(Float)` | `%14.0g` |
| `bfi10_agree` | Agreeableness (Big Five personality inventory) | `Numeric(Float)` | `%14.0g` |
| `bfi10_consc` | Conscientiousness (Big Five personality inventory) | `Numeric(Float)` | `%14.0g` |
| `bfi10_neuro` | Neuroticism (Big Five personality inventory) | `Numeric(Float)` | `%14.0g` |
| `bfi10_open` | Openness (Big Five personality inventory) | `Numeric(Float)` | `%14.0g` |
| `te_weekday` | Time expenditure: what day yesterday | `Numeric(Byte)` | `%14.0g` |
| `te_special` | Time expenditure: normal day yesterday | `Numeric(Byte)` | `%32.0g` |
| `te_chores` | Time expenditure: chores (mins) | `Numeric(Int)` | `%14.0g` |
| `te_pcare` | Time expenditure: personal care (mins) | `Numeric(Int)` | `%14.0g` |
| `te_children` | Time expenditure: children (mins) | `Numeric(Int)` | `%14.0g` |
| `te_parents` | Time expenditure: parents (mins) | `Numeric(Int)` | `%14.0g` |
| `te_partner` | Time expenditure: partner (mins) | `Numeric(Int)` | `%14.0g` |
| `te_family` | Time expenditure: other family members (mins) | `Numeric(Int)` | `%14.0g` |
| `te_leisure` | Time expenditure: leisure (mins) | `Numeric(Int)` | `%14.0g` |
| `te_admin` | Time expenditure: administration (mins) | `Numeric(Int)` | `%14.0g` |
| `te_pwork` | Time expenditure: paid work (mins) | `Numeric(Int)` | `%14.0g` |
| `te_vwork` | Time expenditure: voluntary work (mins) | `Numeric(Int)` | `%14.0g` |
| `te_travel` | Time expenditure: traveling from/to work (mins) | `Numeric(Int)` | `%14.0g` |
| `te_nap` | Time expenditure: napping (mins) | `Numeric(Int)` | `%14.0g` |
| `te_sleep` | Time expenditure: sleeping (mins) | `Numeric(Int)` | `%14.0g` |
| `te_other` | Time expenditure: other activities     (mins) | `Numeric(Int)` | `%14.0g` |
| `tppdi` | Third persons present during the interview | `Numeric(Byte)` | `%14.0g` |
| `willans` | Willingness to answer | `Numeric(Byte)` | `%21.0g` |
| `clarif` | Respondent asked for clarifications | `Numeric(Byte)` | `%14.0g` |
| `undersq` | Respondent understood questions | `Numeric(Byte)` | `%14.0g` |
| `hnrsc` | Help needed to read showcards | `Numeric(Byte)` | `%19.0g` |
| `ydip_f` | Earnings from employment - Flag | `Numeric(Byte)` | `%21.0g` |
| `yind_f` | Earnings from self-employment - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen1_f` | Old age, early retirement, and survivor pensions - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen2_f` | Private and occupational pensions - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen3_f` | Disability pensions/benefits - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen4_f` | Unemployment benefits/insurances - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen5_f` | Social assistance - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen6_f` | Sickness benefits - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsp1_f` | LS payments from old age, early retirement, and survivor pensions - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsp2_f` | LS payments from private and occupational pensions - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsp3_f` | LS payments from disability pensions/benefits - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsp4_f` | LS payments from unemployment benefits/insurances - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsp5_f` | LS payments from social assistance - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsp6_f` | LS payments from sickness benefits - Flag | `Numeric(Byte)` | `%21.0g` |
| `yreg1_f` | Regular private payments - Flag | `Numeric(Byte)` | `%21.0g` |
| `yreg2_f` | Other regular private transfers - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsr1_f` | LS from private payments - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsr2_f` | LS from other private transfers - Flag | `Numeric(Byte)` | `%21.0g` |
| `home_f` | Value of main residence - Flag | `Numeric(Byte)` | `%21.0g` |
| `mort_f` | Mortgage on main residence - Flag | `Numeric(Byte)` | `%21.0g` |
| `rhre_f` | Rent and home-related expenditures - Flag | `Numeric(Byte)` | `%21.0g` |
| `ores_f` | Value of real estate - Flag | `Numeric(Byte)` | `%21.0g` |
| `ysrent_f` | Income from rent/sublet - Flag | `Numeric(Byte)` | `%21.0g` |
| `yaohm_f` | Income from other household members - Flag | `Numeric(Byte)` | `%21.0g` |
| `fahc_f` | Amount spent on food at home - Flag | `Numeric(Byte)` | `%21.0g` |
| `fohc_f` | Amount spent on food outside home - Flag | `Numeric(Byte)` | `%21.0g` |
| `hprf_f` | Value of home produced food - Flag | `Numeric(Byte)` | `%21.0g` |
| `bacc_f` | Bank accounts - Flag | `Numeric(Byte)` | `%21.0g` |
| `bsmf_f` | Bond, stock and mutual funds - Flag | `Numeric(Byte)` | `%21.0g` |
| `ybabsmf_f` | Interest/dividend from bank account, bond, stock and mutual funds - Flag | `Numeric(Byte)` | `%21.0g` |
| `slti_f` | Savings for long-term investments - Flag | `Numeric(Byte)` | `%21.0g` |
| `vbus_f` | Value of own business - Flag | `Numeric(Byte)` | `%21.0g` |
| `sbus_f` | Share of own business - Flag | `Numeric(Byte)` | `%21.0g` |
| `car_f` | Value of cars - Flag | `Numeric(Byte)` | `%21.0g` |
| `liab_f` | Financial liabilities - Flag | `Numeric(Byte)` | `%21.0g` |
| `thinc2_f` | Total household income - Version B - Flag | `Numeric(Byte)` | `%21.0g` |
| `thinc_f` | Total household income - Version A - Flag | `Numeric(Byte)` | `%20.0g` |
| `yincnrp_f` | Income from nonresponding partner - Flag | `Numeric(Byte)` | `%20.0g` |
| `thexp_f` | Total household expenditure - Flag | `Numeric(Byte)` | `%20.0g` |
| `hrass_f` | Household real assets - Flag | `Numeric(Byte)` | `%20.0g` |
| `hgfass_f` | Household gross financial assets - Flag | `Numeric(Byte)` | `%20.0g` |
| `hnfass_f` | Household net financial assets - Flag | `Numeric(Byte)` | `%20.0g` |
| `hnetw_f` | Household net worth - Flag | `Numeric(Byte)` | `%20.0g` |
| `gender_f` | Gender - Flag | `Numeric(Byte)` | `%20.0g` |
| `age_f` | Age - Flag | `Numeric(Byte)` | `%20.0g` |
| `age_p_f` | Age of partner - Flag | `Numeric(Byte)` | `%20.0g` |
| `yedu_f` | Years of education - Flag | `Numeric(Byte)` | `%20.0g` |
| `yedu_p_f` | Years of education of partner - Flag | `Numeric(Byte)` | `%20.0g` |
| `isced_f` | ISCED 1997 coding of education - Flag | `Numeric(Byte)` | `%20.0g` |
| `sphus_f` | Self-perceived health - US scale - Flag | `Numeric(Byte)` | `%20.0g` |
| `mstat_f` | Marital status - Flag | `Numeric(Byte)` | `%20.0g` |
| `nchild_f` | Number of children - Flag | `Numeric(Byte)` | `%20.0g` |
| `ngrchild_f` | Number of grandchildren - Flag | `Numeric(Byte)` | `%20.0g` |
| `gali_f` | Limitation with activities - Flag | `Numeric(Byte)` | `%20.0g` |
| `chronic_f` | Number of chronic deseases - Flag | `Numeric(Byte)` | `%20.0g` |
| `eyesightr_f` | Eyesight reading - Flag | `Numeric(Byte)` | `%20.0g` |
| `hearing_f` | Hearing - Flag | `Numeric(Byte)` | `%20.0g` |
| `bmi_f` | Body mass index - Flag | `Numeric(Byte)` | `%20.0g` |
| `weight_f` | Weight - Flag | `Numeric(Byte)` | `%20.0g` |
| `height_f` | Height - Flag | `Numeric(Byte)` | `%20.0g` |
| `mobility_f` | Mobility limitations - Flag | `Numeric(Byte)` | `%20.0g` |
| `adl_f` | Limitations with activities of daily living - Flag | `Numeric(Byte)` | `%20.0g` |
| `iadl_f` | Limitations with instrumental activities of daily living - Flag | `Numeric(Byte)` | `%20.0g` |
| `esmoked_f` | Ever smoked daily - Flag | `Numeric(Byte)` | `%20.0g` |
| `phinact_f` | Physical inactivity - Flag | `Numeric(Byte)` | `%20.0g` |
| `dairyp_f` | How often consume dairy products - Flag | `Numeric(Byte)` | `%20.0g` |
| `legeggs_f` | How often consume legumes, beans or eggs - Flag | `Numeric(Byte)` | `%20.0g` |
| `meat_f` | How often consume meat, fish or poultry - Flag | `Numeric(Byte)` | `%20.0g` |
| `fruit_f` | How often consume fruits or vegetables - Flag | `Numeric(Byte)` | `%20.0g` |
| `reading_f` | Self-rated reading skills - Flag | `Numeric(Byte)` | `%20.0g` |
| `writing_f` | Self-rated writing skills - Flag | `Numeric(Byte)` | `%20.0g` |
| `orienti_f` | Score of orientation in time test - Flag | `Numeric(Byte)` | `%20.0g` |
| `wllft_f` | Score of words list learning test - trial 1 - Flag | `Numeric(Byte)` | `%20.0g` |
| `wllst_f` | Score of words list learning test - trial 2 - Flag | `Numeric(Byte)` | `%20.0g` |
| `fluency_f` | Score of verbal fluency test - Flag | `Numeric(Byte)` | `%20.0g` |
| `numeracy_f` | Score of first numeracy test - Flag | `Numeric(Byte)` | `%20.0g` |
| `numeracy2_f` | Score of second numeracy test - Flag | `Numeric(Byte)` | `%20.0g` |
| `memory_f` | Score of memory test - Flag | `Numeric(Byte)` | `%20.0g` |
| `maxgrip_f` | Maximum of grip strength measures - Flag | `Numeric(Byte)` | `%20.0g` |
| `eurod_f` | EURO depression scale - Flag | `Numeric(Byte)` | `%20.0g` |
| `doctor_f` | Seen/Talked to medical doctor - Flag | `Numeric(Byte)` | `%20.0g` |
| `hospital_f` | In hospital last 12 months - Flag | `Numeric(Byte)` | `%20.0g` |
| `thospital_f` | Times being patient in hospital - Flag | `Numeric(Byte)` | `%20.0g` |
| `nhospital_f` | Total nights stayed in hospital - Flag | `Numeric(Byte)` | `%20.0g` |
| `cjs_f` | Current job situation - Flag | `Numeric(Byte)` | `%20.0g` |
| `pwork_f` | Did any paid work - Flag | `Numeric(Byte)` | `%20.0g` |
| `empstat_f` | Employee or self-employed - Flag | `Numeric(Byte)` | `%20.0g` |
| `lookjob_f` | Looking for job - Flag | `Numeric(Byte)` | `%20.0g` |
| `internet_f` | Use internet - Flag | `Numeric(Byte)` | `%20.0g` |
| `pcskill_f` | PC skills - Flag | `Numeric(Byte)` | `%20.0g` |
| `cjobpc_f` | Use PC in current job - Flag | `Numeric(Byte)` | `%20.0g` |
| `ljobpc_f` | Use PC in last job - Flag | `Numeric(Byte)` | `%20.0g` |
| `rhfo_f` | Received help from others (how many) - Flag | `Numeric(Byte)` | `%20.0g` |
| `ghto_f` | Given help to others (how many) - Flag | `Numeric(Byte)` | `%20.0g` |
| `ghih_f` | Given help in the household (how many) - Flag | `Numeric(Byte)` | `%20.0g` |
| `rhih_f` | Received help in the household (how many) - Flag | `Numeric(Byte)` | `%20.0g` |
| `gfg_f` | Number of given financial gifts 250 or more - Flag | `Numeric(Byte)` | `%20.0g` |
| `rfg_f` | Number of received financial gifts 250 or more - Flag | `Numeric(Byte)` | `%20.0g` |
| `rggp_f` | Number of received gifts, goods, properties 5000 or more - Flag | `Numeric(Byte)` | `%20.0g` |
| `gggp_f` | Given gift, good, property 5000 or more - Flag | `Numeric(Byte)` | `%20.0g` |
| `otrf_f` | Owner, tenant or rent free - Flag | `Numeric(Byte)` | `%20.0g` |
| `perho_f` | Percentage of house owned - Flag | `Numeric(Byte)` | `%20.0g` |
| `fdistress_f` | Household able to make ends meet - Flag | `Numeric(Byte)` | `%20.0g` |
| `naly_f` | Number of activities last year - Flag | `Numeric(Byte)` | `%20.0g` |
| `saly_f` | Satisfied with no activities - Flag | `Numeric(Byte)` | `%20.0g` |
| `lifesat_f` | Life satisfaction - Flag | `Numeric(Byte)` | `%20.0g` |
| `lifehap_f` | Life happiness - Flag | `Numeric(Byte)` | `%20.0g` |
| `lifex_f` | Living in ten years - Flag | `Numeric(Byte)` | `%20.0g` |
| `bfi10_extra_f` | Extraversion (Big Five personality inventory) - Flag | `Numeric(Byte)` | `%20.0g` |
| `bfi10_agree_f` | Agreeableness (Big Five personality inventory) - Flag | `Numeric(Byte)` | `%20.0g` |
| `bfi10_consc_f` | Conscientiousness (Big Five personality inventory) - Flag | `Numeric(Byte)` | `%20.0g` |
| `bfi10_neuro_f` | Neuroticism (Big Five personality inventory) - Flag | `Numeric(Byte)` | `%20.0g` |
| `bfi10_open_f` | Openness (Big Five personality inventory) - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_weekday_f` | Time expenditure: what day yesterday - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_special_f` | Time expenditure: normal day yesterday - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_chores_f` | Time expenditure: chores - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_pcare_f` | Time expenditure: personal care - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_children_f` | Time expenditure: children - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_parents_f` | Time expenditure: parents - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_partner_f` | Time expenditure: partner - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_family_f` | Time expenditure: other family members - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_leisure_f` | Time expenditure: leisure - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_admin_f` | Time expenditure: administration - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_pwork_f` | Time expenditure: paid work - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_vwork_f` | Time expenditure: voluntary work - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_travel_f` | Time expenditure: traveling from/to work - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_nap_f` | Time expenditure: napping - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_sleep_f` | Time expenditure: sleeping - Flag | `Numeric(Byte)` | `%20.0g` |
| `te_other_f` | Time expenditure: other activities - Flag | `Numeric(Byte)` | `%20.0g` |
| `tppdi_f` | Third persons present during the interview - Flag | `Numeric(Byte)` | `%20.0g` |
| `willans_f` | Willingness to answer - Flag | `Numeric(Byte)` | `%20.0g` |
| `clarif_f` | Respondent asked for clarifications - Flag | `Numeric(Byte)` | `%20.0g` |
| `undersq_f` | Respondent understood questions - Flag | `Numeric(Byte)` | `%20.0g` |
| `hnrsc_f` | Help needed to read showcards â€“ Flag | `Numeric(Byte)` | `%20.0g` |
| `currency` | currency | `Str(16)` | `%16s` |
| `nomx2018` | Nominal exchange rate (national currency/Euro), annual average, 2018 | `Numeric(Double)` | `%10.0g` |
| `nomx2019` | Nominal exchange rate (national currency/Euro), annual average, 2019 | `Numeric(Double)` | `%10.0g` |
| `nomx2020` | Nominal exchange rate (national currency/Euro), annual average, 2020 | `Numeric(Double)` | `%10.0g` |
| `nomx2021` | Nominal exchange rate (national currency/Euro), annual average, 2021 | `Numeric(Double)` | `%10.0g` |
| `pppc2018` | Current PPP exchange rate (national currency/Euro), 2018 | `Numeric(Double)` | `%10.0g` |
| `pppc2019` | Current PPP exchange rate (national currency/Euro), 2019 | `Numeric(Double)` | `%10.0g` |
| `pppc2020` | Current PPP exchange rate (national currency/Euro), 2020 | `Numeric(Double)` | `%10.0g` |
| `pppk2018` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2018 | `Numeric(Double)` | `%10.0g` |
| `pppk2019` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2019 | `Numeric(Double)` | `%10.0g` |
| `pppk2020` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2020 | `Numeric(Double)` | `%10.0g` |

### `gv_isced` - ISCED education recodes

- Dataset: `sharew8_rel9-0-0_gv_isced.dta`
- Read with: `ps.read_share_module("gv_isced", wave=8)`
- Rows: 53,695
- Variables: 54
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `isced1997_r` | Respondent: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_sp` | Spouse/ex-spouse of respondent: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_m` | Mother of respondent: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_f` | Father of respondent: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c1` | Respondent's child 1: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c2` | Respondent's child 2: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c3` | Respondent's child 3: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c4` | Respondent's child 4: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c5` | Respondent's child 5: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c6` | Respondent's child 6: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c7` | Respondent's child 7: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c8` | Respondent's child 8: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c9` | Respondent's child 9: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c10` | Respondent's child 10: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c11` | Respondent's child 11: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c12` | Respondent's child 12: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c13` | Respondent's child 13: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c14` | Respondent's child 14: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c15` | Respondent's child 15: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c16` | Respondent's child 16: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c17` | Respondent's child 17: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c18` | Respondent's child 18: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c19` | Respondent's child 19: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c20` | Respondent's child 20: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_r` | Respondent: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_sp` | Spouse/ex-spouse of respondent: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_m` | Mother of respondent: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_f` | Father of respondent: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c1` | Respondent's child 1: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c2` | Respondent's child 2: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c3` | Respondent's child 3: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c4` | Respondent's child 4: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c5` | Respondent's child 5: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c6` | Respondent's child 6: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c7` | Respondent's child 7: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c8` | Respondent's child 8: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c9` | Respondent's child 9: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c10` | Respondent's child 10: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c11` | Respondent's child 11: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c12` | Respondent's child 12: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c13` | Respondent's child 13: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c14` | Respondent's child 14: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c15` | Respondent's child 15: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c16` | Respondent's child 16: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c17` | Respondent's child 17: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c18` | Respondent's child 18: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c19` | Respondent's child 19: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced2011_c20` | Respondent's child 20: ISCED-11 coding of education | `Numeric(Byte)` | `%15.0g` |

### `gv_networks` - Generated social network variables

- Dataset: `sharew8_rel9-0-0_gv_networks.dta`
- Read with: `ps.read_share_module("gv_networks", wave=8)`
- Rows: 53,695
- Variables: 222
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `panel_status` | In which waves was SN done? | `Numeric(Byte)` | `%20.0g` |
| `panel_change_size` | w8 SN size - w6 SN size (if both done) | `Numeric(Byte)` | `%9.0g` |
| `panel_lost` | Number of lost wave 6 SN members | `Numeric(Byte)` | `%16.0g` |
| `panel_new` | Number of new wave 8 SN members | `Numeric(Byte)` | `%16.0g` |
| `w6_panel_continued` | Count of w8 SN members that were mentioned before in w6 | `Numeric(Byte)` | `%16.0g` |
| `w4_panel_continued` | Count of w8 SN members that were mentioned before in w4 | `Numeric(Byte)` | `%16.0g` |
| `panel_changePattern_size` | Change pattern SN size between w4-w6-w8 | `Numeric(Byte)` | `%14.0g` |
| `panel_changePattern_childnet` | Change pattern of children in SN between w4-w6-w8 | `Numeric(Byte)` | `%14.0g` |
| `panel_changePattern_friendnet` | Change pattern of friends in SN between w4-w6-w8 | `Numeric(Byte)` | `%14.0g` |
| `sn_size_w4` | SN size wave 4 | `Numeric(Byte)` | `%19.0g` |
| `sn_size_w6` | SN size wave 6 | `Numeric(Byte)` | `%19.0g` |
| `sn_size_w8` | SN size wave 8 | `Numeric(Byte)` | `%19.0g` |
| `sn_satisfaction` | Social network satisfaction - Combined sn012_ & sn017_ | `Numeric(Byte)` | `%27.0g` |
| `sn_scale` | Scale of social connectedness (high=high connectedness) | `Numeric(Byte)` | `%25.0g` |
| `social_integration` | Social integration index (high=high integration) | `Numeric(Byte)` | `%9.0g` |
| `spousenet2` | Spouse/partner in SN - Dummy | `Numeric(Byte)` | `%27.0g` |
| `partner_var` | Relationship status | `Numeric(Byte)` | `%30.0g` |
| `famnet` | Family members in SN - Count | `Numeric(Byte)` | `%25.0g` |
| `childnet` | Children in SN - Count | `Numeric(Byte)` | `%19.0g` |
| `siblingnet` | Siblings in SN - Count | `Numeric(Byte)` | `%25.0g` |
| `parentnet` | Parents in SN - Count | `Numeric(Byte)` | `%25.0g` |
| `friendnet` | Friends in SN - Count | `Numeric(Byte)` | `%25.0g` |
| `formalnet` | Formal helpers in SN - Count | `Numeric(Byte)` | `%25.0g` |
| `othernet` | Others in SN - Count | `Numeric(Byte)` | `%25.0g` |
| `womennet` | Number of women in SN | `Numeric(Byte)` | `%25.0g` |
| `mennet` | Number of men in SN | `Numeric(Byte)` | `%25.0g` |
| `prx_mean` | SN proximity - Average | `Numeric(Float)` | `%25.0g` |
| `most_prx` | Proximity of closest SN member | `Numeric(Byte)` | `%25.0g` |
| `prx_5km` | Number of SN members within 5km | `Numeric(Byte)` | `%25.0g` |
| `prx_1km` | Number of SN members within 1km | `Numeric(Byte)` | `%25.0g` |
| `contact_mean` | SN contact - Average | `Numeric(Float)` | `%27.0g` |
| `most_contact` | Contact with most contacted SN member | `Numeric(Byte)` | `%27.0g` |
| `contact_daily` | Number of SN members with daily contact | `Numeric(Byte)` | `%25.0g` |
| `contact_week` | Number of SN members with weekly or more contact | `Numeric(Byte)` | `%25.0g` |
| `spouse_contact` | Average contact with spouse in SN | `Numeric(Byte)` | `%27.0g` |
| `fam_contact` | Average contact with family members in SN | `Numeric(Float)` | `%27.0g` |
| `child_contact` | Average contact with children in SN | `Numeric(Float)` | `%27.0g` |
| `sibling_contact` | Average contact with siblings in SN | `Numeric(Float)` | `%27.0g` |
| `parent_contact` | Average contact with parents in SN | `Numeric(Float)` | `%27.0g` |
| `friend_contact` | Average contact with friends in SN | `Numeric(Float)` | `%27.0g` |
| `formal_contact` | Average contact with formal helpers in SN | `Numeric(Float)` | `%27.0g` |
| `other_contact` | Average contact with others in SN | `Numeric(Float)` | `%27.0g` |
| `close_mean` | SN emotional closeness - Average | `Numeric(Float)` | `%25.0g` |
| `most_close` | Emotional closeness of closest SN member | `Numeric(Byte)` | `%25.0g` |
| `close_very` | Number of SN - Very to extrememly close | `Numeric(Byte)` | `%25.0g` |
| `year_mean` | SN year of birth - Average | `Numeric(Int)` | `%25.0f` |
| `fin_gave` | Number of persons fin. help was given to (250 or more) | `Numeric(Byte)` | `%19.0g` |
| `snfin_gave` | Number of SN members fin. help was given to (250 or more) | `Numeric(Byte)` | `%19.0g` |
| `fin_received` | Number of persons fin. help was received from (250 or more) | `Numeric(Byte)` | `%19.0g` |
| `snfin_received` | Number of SN members fin. help was received from (250 or more) | `Numeric(Byte)` | `%19.0g` |
| `gift_received` | Number of persons fin. gift was received from (5000 or more) | `Numeric(Byte)` | `%19.0g` |
| `sngift_received` | Number of SN members fin. gift was received from (5000 or more) | `Numeric(Byte)` | `%19.0g` |
| `gift_gave` | Number of persons fin. gift was given to (5000 or more) | `Numeric(Byte)` | `%19.0g` |
| `sngift_gave` | Number of SN members fin. gift was given to (5000 or more) | `Numeric(Byte)` | `%19.0g` |
| `outhh_receive_care` | Received personal/practical help from person(s) outside hh - Count | `Numeric(Byte)` | `%19.0g` |
| `outhh_snreceive_care` | Number of SN members personal/practical help was received from outside hh | `Numeric(Byte)` | `%19.0g` |
| `outhh_gave_care` | Gave personal/practical help to person(s) outside hh - Count | `Numeric(Byte)` | `%19.0g` |
| `outhh_sngave_care` | Number of SN members personal/practical help was given to outside hh | `Numeric(Byte)` | `%19.0g` |
| `hh_gave_care` | Gave personal help to person(s) inside hh - Count | `Numeric(Byte)` | `%19.0g` |
| `hh_sngave_care` | Number of SN members personal help was given to inside hh | `Numeric(Byte)` | `%19.0g` |
| `hh_receive_care` | Received personal help from person(s) inside HH - Count | `Numeric(Byte)` | `%19.0g` |
| `hh_snreceive_care` | Number of SN members personal help was received from inside hh | `Numeric(Byte)` | `%19.0g` |
| `w8_sn_mentioned_before_1` | Was w8 SN person 1 mentioned before in w6 or w4? | `Numeric(Byte)` | `%21.0g` |
| `w8_sn_mentioned_before_2` | Was w8 SN person 2 mentioned before in w6 or w4? | `Numeric(Byte)` | `%21.0g` |
| `w8_sn_mentioned_before_3` | Was w8 SN person 3 mentioned before in w6 or w4? | `Numeric(Byte)` | `%21.0g` |
| `w8_sn_mentioned_before_4` | Was w8 SN person 4 mentioned before in w6 or w4? | `Numeric(Byte)` | `%21.0g` |
| `w8_sn_mentioned_before_5` | Was w8 SN person 5 mentioned before in w6 or w4? | `Numeric(Byte)` | `%21.0g` |
| `w8_sn_mentioned_before_6` | Was w8 SN person 6 mentioned before in w6 or w4? | `Numeric(Byte)` | `%21.0g` |
| `w8_sn_mentioned_before_7` | Was w8 SN person 7 mentioned before in w6 or w4? | `Numeric(Byte)` | `%21.0g` |
| `w8_sn_w6_position_1` | The position of w8 person 1 in w6 | `Numeric(Byte)` | `%16.0g` |
| `w8_sn_w6_position_2` | The position of w8 person 2 in w6 | `Numeric(Byte)` | `%16.0g` |
| `w8_sn_w6_position_3` | The position of w8 person 3 in w6 | `Numeric(Byte)` | `%16.0g` |
| `w8_sn_w6_position_4` | The position of w8 person 4 in w6 | `Numeric(Byte)` | `%16.0g` |
| `w8_sn_w6_position_5` | The position of w8 person 5 in w6 | `Numeric(Byte)` | `%16.0g` |
| `w8_sn_w6_position_6` | The position of w8 person 6 in w6 | `Numeric(Byte)` | `%16.0g` |
| `w8_sn_w6_position_7` | The position of w8 person 7 in w6 | `Numeric(Byte)` | `%16.0g` |
| `w8_sn_w4_position_1` | The position of w8 person 1 in w4 | `Numeric(Byte)` | `%16.0g` |
| `w8_sn_w4_position_2` | The position of w8 person 2 in w4 | `Numeric(Byte)` | `%16.0g` |
| `w8_sn_w4_position_3` | The position of w8 person 3 in w4 | `Numeric(Byte)` | `%16.0g` |
| `w8_sn_w4_position_4` | The position of w8 person 4 in w4 | `Numeric(Byte)` | `%16.0g` |
| `w8_sn_w4_position_5` | The position of w8 person 5 in w4 | `Numeric(Byte)` | `%16.0g` |
| `w8_sn_w4_position_6` | The position of w8 person 6 in w4 | `Numeric(Byte)` | `%16.0g` |
| `w8_sn_w4_position_7` | The position of w8 person 7 in w4 | `Numeric(Byte)` | `%16.0g` |
| `w6_sn_mentioned_again_1` | Was w6 SN person 1 mentioned again in w8? | `Numeric(Byte)` | `%16.0g` |
| `w6_sn_mentioned_again_2` | Was w6 SN person 2 mentioned again in w8? | `Numeric(Byte)` | `%16.0g` |
| `w6_sn_mentioned_again_3` | Was w6 SN person 3 mentioned again in w8? | `Numeric(Byte)` | `%16.0g` |
| `w6_sn_mentioned_again_4` | Was w6 SN person 4 mentioned again in w8? | `Numeric(Byte)` | `%16.0g` |
| `w6_sn_mentioned_again_5` | Was w6 SN person 5 mentioned again in w8? | `Numeric(Byte)` | `%16.0g` |
| `w6_sn_mentioned_again_6` | Was w6 SN person 6 mentioned again in w8? | `Numeric(Byte)` | `%16.0g` |
| `w6_sn_mentioned_again_7` | Was w6 SN person 7 mentioned again in w8? | `Numeric(Byte)` | `%16.0g` |
| `w4_sn_mentioned_again_1` | Was w4 SN person 1 mentioned again in w8? | `Numeric(Byte)` | `%16.0g` |
| `w4_sn_mentioned_again_2` | Was w4 SN person 2 mentioned again in w8? | `Numeric(Byte)` | `%16.0g` |
| `w4_sn_mentioned_again_3` | Was w4 SN person 3 mentioned again in w8? | `Numeric(Byte)` | `%16.0g` |
| `w4_sn_mentioned_again_4` | Was w4 SN person 4 mentioned again in w8? | `Numeric(Byte)` | `%16.0g` |
| `w4_sn_mentioned_again_5` | Was w4 SN person 5 mentioned again in w8? | `Numeric(Byte)` | `%16.0g` |
| `w4_sn_mentioned_again_6` | Was w4 SN person 6 mentioned again in w8? | `Numeric(Byte)` | `%16.0g` |
| `w4_sn_mentioned_again_7` | Was w4 SN person 7 mentioned again in w8? | `Numeric(Byte)` | `%16.0g` |
| `sn_person_1` | Was there an SN person 1? | `Numeric(Byte)` | `%14.0g` |
| `sn_person_2` | Was there an SN person 2? | `Numeric(Byte)` | `%14.0g` |
| `sn_person_3` | Was there an SN person 3? | `Numeric(Byte)` | `%14.0g` |
| `sn_person_4` | Was there an SN person 4? | `Numeric(Byte)` | `%14.0g` |
| `sn_person_5` | Was there an SN person 5? | `Numeric(Byte)` | `%14.0g` |
| `sn_person_6` | Was there an SN person 6? | `Numeric(Byte)` | `%14.0g` |
| `sn_person_7` | Was there an SN person 7? | `Numeric(Byte)` | `%14.0g` |
| `rel_1` | Relation to SN member 1 | `Numeric(Byte)` | `%39.0g` |
| `rel_2` | Relation to SN member 2 | `Numeric(Byte)` | `%39.0g` |
| `rel_3` | Relation to SN member 3 | `Numeric(Byte)` | `%39.0g` |
| `rel_4` | Relation to SN member 4 | `Numeric(Byte)` | `%39.0g` |
| `rel_5` | Relation to SN member 5 | `Numeric(Byte)` | `%39.0g` |
| `rel_6` | Relation to SN member 6 | `Numeric(Byte)` | `%39.0g` |
| `rel_7` | Relation to SN member 7 | `Numeric(Byte)` | `%39.0g` |
| `gender_1` | Gender of SN member 1 | `Numeric(Byte)` | `%14.0g` |
| `gender_2` | Gender of SN member 2 | `Numeric(Byte)` | `%14.0g` |
| `gender_3` | Gender of SN member 3 | `Numeric(Byte)` | `%14.0g` |
| `gender_4` | Gender of SN member 4 | `Numeric(Byte)` | `%14.0g` |
| `gender_5` | Gender of SN member 5 | `Numeric(Byte)` | `%14.0g` |
| `gender_6` | Gender of SN member 6 | `Numeric(Byte)` | `%14.0g` |
| `gender_7` | Gender of SN member 7 | `Numeric(Byte)` | `%14.0g` |
| `prx_1` | Proximity of SN member 1 | `Numeric(Byte)` | `%35.0g` |
| `prx_2` | Proximity of SN member 2 | `Numeric(Byte)` | `%35.0g` |
| `prx_3` | Proximity of SN member 3 | `Numeric(Byte)` | `%35.0g` |
| `prx_4` | Proximity of SN member 4 | `Numeric(Byte)` | `%35.0g` |
| `prx_5` | Proximity of SN member 5 | `Numeric(Byte)` | `%35.0g` |
| `prx_6` | Proximity of SN member 6 | `Numeric(Byte)` | `%35.0g` |
| `prx_7` | Proximity of SN member 7 | `Numeric(Byte)` | `%35.0g` |
| `contact_1` | Contact to SN member 1 | `Numeric(Byte)` | `%22.0g` |
| `contact_2` | Contact to SN member 2 | `Numeric(Byte)` | `%22.0g` |
| `contact_3` | Contact to SN member 3 | `Numeric(Byte)` | `%22.0g` |
| `contact_4` | Contact to SN member 4 | `Numeric(Byte)` | `%22.0g` |
| `contact_5` | Contact to SN member 5 | `Numeric(Byte)` | `%22.0g` |
| `contact_6` | Contact to SN member 6 | `Numeric(Byte)` | `%22.0g` |
| `contact_7` | Contact to SN member 7 | `Numeric(Byte)` | `%22.0g` |
| `close_1` | Emotional closeness to SN member 1 | `Numeric(Byte)` | `%15.0g` |
| `close_2` | Emotional closeness to SN member 2 | `Numeric(Byte)` | `%15.0g` |
| `close_3` | Emotional closeness to SN member 3 | `Numeric(Byte)` | `%15.0g` |
| `close_4` | Emotional closeness to SN member 4 | `Numeric(Byte)` | `%15.0g` |
| `close_5` | Emotional closeness to SN member 5 | `Numeric(Byte)` | `%15.0g` |
| `close_6` | Emotional closeness to SN member 6 | `Numeric(Byte)` | `%15.0g` |
| `close_7` | Emotional closeness to SN member 7 | `Numeric(Byte)` | `%15.0g` |
| `year_1` | Year of birth of SN member 1 | `Numeric(Int)` | `%14.0g` |
| `year_2` | Year of birth of SN member 2 | `Numeric(Int)` | `%14.0g` |
| `year_3` | Year of birth of SN member 3 | `Numeric(Int)` | `%14.0g` |
| `year_4` | Year of birth of SN member 4 | `Numeric(Int)` | `%14.0g` |
| `year_5` | Year of birth of SN member 5 | `Numeric(Int)` | `%14.0g` |
| `year_6` | Year of birth of SN member 6 | `Numeric(Int)` | `%14.0g` |
| `year_7` | Year of birth of SN member 7 | `Numeric(Int)` | `%14.0g` |
| `fin_gave_sn_1` | Gave financial help to wave 8 SN member 1 | `Numeric(Byte)` | `%39.0g` |
| `fin_gave_sn_2` | Gave financial help to wave 8 SN member 2 | `Numeric(Byte)` | `%39.0g` |
| `fin_gave_sn_3` | Gave financial help to wave 8 SN member 3 | `Numeric(Byte)` | `%39.0g` |
| `fin_gave_sn_4` | Gave financial help to wave 8 SN member 4 | `Numeric(Byte)` | `%39.0g` |
| `fin_gave_sn_5` | Gave financial help to wave 8 SN member 5 | `Numeric(Byte)` | `%39.0g` |
| `fin_gave_sn_6` | Gave financial help to wave 8 SN member 6 | `Numeric(Byte)` | `%39.0g` |
| `fin_gave_sn_7` | Gave financial help to wave 8 SN member 7 | `Numeric(Byte)` | `%39.0g` |
| `fin_received_sn_1` | Received financial help from wave 8 SN member 1 | `Numeric(Byte)` | `%44.0g` |
| `fin_received_sn_2` | Received financial help from wave 8 SN member 2 | `Numeric(Byte)` | `%44.0g` |
| `fin_received_sn_3` | Received financial help from wave 8 SN member 3 | `Numeric(Byte)` | `%44.0g` |
| `fin_received_sn_4` | Received financial help from wave 8 SN member 4 | `Numeric(Byte)` | `%44.0g` |
| `fin_received_sn_5` | Received financial help from wave 8 SN member 5 | `Numeric(Byte)` | `%44.0g` |
| `fin_received_sn_6` | Received financial help from wave 8 SN member 6 | `Numeric(Byte)` | `%44.0g` |
| `fin_received_sn_7` | Received financial help from wave 8 SN member 7 | `Numeric(Byte)` | `%44.0g` |
| `gift_received_sn_1` | Received financial gift from wave 8 SN member 1 | `Numeric(Byte)` | `%44.0g` |
| `gift_received_sn_2` | Received financial gift from wave 8 SN member 2 | `Numeric(Byte)` | `%44.0g` |
| `gift_received_sn_3` | Received financial gift from wave 8 SN member 3 | `Numeric(Byte)` | `%44.0g` |
| `gift_received_sn_4` | Received financial gift from wave 8 SN member 4 | `Numeric(Byte)` | `%44.0g` |
| `gift_received_sn_5` | Received financial gift from wave 8 SN member 5 | `Numeric(Byte)` | `%44.0g` |
| `gift_received_sn_6` | Received financial gift from wave 8 SN member 6 | `Numeric(Byte)` | `%44.0g` |
| `gift_received_sn_7` | Received financial gift from wave 8 SN member 7 | `Numeric(Byte)` | `%44.0g` |
| `gift_gave_sn_1` | Gave financial gift to wave 8 SN member 1 | `Numeric(Byte)` | `%38.0g` |
| `gift_gave_sn_2` | Gave financial gift to wave 8 SN member 2 | `Numeric(Byte)` | `%38.0g` |
| `gift_gave_sn_3` | Gave financial gift to wave 8 SN member 3 | `Numeric(Byte)` | `%38.0g` |
| `gift_gave_sn_4` | Gave financial gift to wave 8 SN member 4 | `Numeric(Byte)` | `%38.0g` |
| `gift_gave_sn_5` | Gave financial gift to wave 8 SN member 5 | `Numeric(Byte)` | `%38.0g` |
| `gift_gave_sn_6` | Gave financial gift to wave 8 SN member 6 | `Numeric(Byte)` | `%38.0g` |
| `gift_gave_sn_7` | Gave financial gift to wave 8 SN member 7 | `Numeric(Byte)` | `%38.0g` |
| `outhh_receive_care_sn_1` | Received personal/practical help from wave 8 SN member 1 outside hh | `Numeric(Byte)` | `%53.0g` |
| `outhh_receive_care_sn_2` | Received personal/practical help from wave 8 SN member 2 outside hh | `Numeric(Byte)` | `%53.0g` |
| `outhh_receive_care_sn_3` | Received personal/practical help from wave 8 SN member 3 outside hh | `Numeric(Byte)` | `%53.0g` |
| `outhh_receive_care_sn_4` | Received personal/practical help from wave 8 SN member 4 outside hh | `Numeric(Byte)` | `%53.0g` |
| `outhh_receive_care_sn_5` | Received personal/practical help from wave 8 SN member 5 outside hh | `Numeric(Byte)` | `%53.0g` |
| `outhh_receive_care_sn_6` | Received personal/practical help from wave 8 SN member 6 outside hh | `Numeric(Byte)` | `%53.0g` |
| `outhh_receive_care_sn_7` | Received personal/practical help from wave 8 SN member 7 outside hh | `Numeric(Byte)` | `%53.0g` |
| `outhh_gave_care_sn_1` | Gave personal/practical help to wave 8 SN member 1 outside hh | `Numeric(Byte)` | `%47.0g` |
| `outhh_gave_care_sn_2` | Gave personal/practical help to wave 8 SN member 2 outside hh | `Numeric(Byte)` | `%47.0g` |
| `outhh_gave_care_sn_3` | Gave personal/practical help to wave 8 SN member 3 outside hh | `Numeric(Byte)` | `%47.0g` |
| `outhh_gave_care_sn_4` | Gave personal/practical help to wave 8 SN member 4 outside hh | `Numeric(Byte)` | `%47.0g` |
| `outhh_gave_care_sn_5` | Gave personal/practical help to wave 8 SN member 5 outside hh | `Numeric(Byte)` | `%47.0g` |
| `outhh_gave_care_sn_6` | Gave personal/practical help to wave 8 SN member 6 outside hh | `Numeric(Byte)` | `%47.0g` |
| `outhh_gave_care_sn_7` | Gave personal/practical help to wave 8 SN member 7 outside hh | `Numeric(Byte)` | `%47.0g` |
| `hh_gave_care_sn_1` | Gave personal help to wave 8 SN member 1 | `Numeric(Byte)` | `%37.0g` |
| `hh_gave_care_sn_2` | Gave personal help to wave 8 SN member 2 | `Numeric(Byte)` | `%37.0g` |
| `hh_gave_care_sn_3` | Gave personal help to wave 8 SN member 3 | `Numeric(Byte)` | `%37.0g` |
| `hh_gave_care_sn_4` | Gave personal help to wave 8 SN member 4 | `Numeric(Byte)` | `%37.0g` |
| `hh_gave_care_sn_5` | Gave personal help to wave 8 SN member 5 | `Numeric(Byte)` | `%37.0g` |
| `hh_gave_care_sn_6` | Gave personal help to wave 8 SN member 6 | `Numeric(Byte)` | `%37.0g` |
| `hh_gave_care_sn_7` | Gave personal help to wave 8 SN member 7 | `Numeric(Byte)` | `%37.0g` |
| `hh_receive_care_sn_1` | Received personal help from wave 8 SN member 1 | `Numeric(Byte)` | `%43.0g` |
| `hh_receive_care_sn_2` | Received personal help from wave 8 SN member 2 | `Numeric(Byte)` | `%43.0g` |
| `hh_receive_care_sn_3` | Received personal help from wave 8 SN member 3 | `Numeric(Byte)` | `%43.0g` |
| `hh_receive_care_sn_4` | Received personal help from wave 8 SN member 4 | `Numeric(Byte)` | `%43.0g` |
| `hh_receive_care_sn_5` | Received personal help from wave 8 SN member 5 | `Numeric(Byte)` | `%43.0g` |
| `hh_receive_care_sn_6` | Received personal help from wave 8 SN member 6 | `Numeric(Byte)` | `%43.0g` |
| `hh_receive_care_sn_7` | Received personal help from wave 8 SN member 7 | `Numeric(Byte)` | `%43.0g` |
| `sn_child_loop_1` | Child link: sn person 1 mentioned as child (loop) | `Numeric(Byte)` | `%13.0g` |
| `sn_child_loop_2` | Child link: sn person 2 mentioned as child (loop) | `Numeric(Byte)` | `%13.0g` |
| `sn_child_loop_3` | Child link: sn person 3 mentioned as child (loop) | `Numeric(Byte)` | `%13.0g` |
| `sn_child_loop_4` | Child link: sn person 4 mentioned as child (loop) | `Numeric(Byte)` | `%13.0g` |
| `sn_child_loop_5` | Child link: sn person 5 mentioned as child (loop) | `Numeric(Byte)` | `%13.0g` |
| `sn_child_loop_6` | Child link: sn person 6 mentioned as child (loop) | `Numeric(Byte)` | `%13.0g` |
| `sn_child_loop_7` | Child link: sn person 7 mentioned as child (loop) | `Numeric(Byte)` | `%13.0g` |
| `sn_childid_1` | Child link: sn person 1 child identifier (fix across modules and waves) | `Str(14)` | `%14s` |
| `sn_childid_2` | Child link: sn person 2 child identifier (fix across modules and waves) | `Str(14)` | `%14s` |
| `sn_childid_3` | Child link: sn person 3 child identifier (fix across modules and waves) | `Str(14)` | `%14s` |
| `sn_childid_4` | Child link: sn person 4 child identifier (fix across modules and waves) | `Str(14)` | `%14s` |
| `sn_childid_5` | Child link: sn person 5 child identifier (fix across modules and waves) | `Str(14)` | `%14s` |
| `sn_childid_6` | Child link: sn person 6 child identifier (fix across modules and waves) | `Str(14)` | `%14s` |
| `sn_childid_7` | Child link: sn person 7 child identifier (fix across modules and waves) | `Str(14)` | `%14s` |

### `gv_weights` - Cross-sectional weights

- Dataset: `sharew8_rel9-0-0_gv_weights.dta`
- Read with: `ps.read_share_module("gv_weights", wave=8)`
- Rows: 53,695
- Variables: 16
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid8` | Household identifier (wave 8) | `Str(11)` | `%11s` |
| `mergeidp8` | Partner identifier (wave 8) | `Str(12)` | `%12s` |
| `coupleid8` | Couple identifier (wave 8) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `dw_w8` | Design weight - wave 8 | `Numeric(Double)` | `%10.0g` |
| `cchw_w8_main` | Calibrated cross-sectional household weight - Main interview | `Numeric(Double)` | `%10.0g` |
| `cciw_w8_main` | Calibrated cross-sectional individual weight - Main interview | `Numeric(Double)` | `%10.0g` |
| `cchw_w8_main_ca` | Calibrated cross-sectional household weight - Main & CA interview | `Numeric(Double)` | `%10.0g` |
| `cciw_w8_main_ca` | Calibrated cross-sectional individual weight - Main & CA interview | `Numeric(Double)` | `%10.0g` |
| `subsample` | Indicator for country-specific subsample | `Str(6)` | `%9s` |
| `stratum1` | Indicator for primary stratum (if any) | `Str(10)` | `%10s` |
| `stratum2` | Indicator for secondary stratum (if any) | `Str(6)` | `%9s` |
| `psu` | Primary sampling unit | `Str(10)` | `%10s` |
| `ssu` | Secondary sampling unit (if any) | `Str(6)` | `%9s` |
