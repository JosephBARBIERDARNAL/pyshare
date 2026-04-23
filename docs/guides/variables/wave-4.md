---
icon: lucide/list-tree
---

# Wave 4 Variable Dictionary

This page is generated from the local SHARE wave 4 release `9-0-0` Stata files.

It covers 33 datasets and 4,811 variable entries for the files currently available in `data/`.

[Back to variable dictionary](./index.md)

## Overview

| Module | Category | Meaning | Key | Variables | Rows | File |
| --- | --- | --- | --- | --- | --- | --- |
| `ac` | core | Activities | `mergeid` | 38 | 57,982 | `sharew4_rel9-0-0_ac.dta` |
| `as` | core | Assets | `mergeid` | 96 | 57,982 | `sharew4_rel9-0-0_as.dta` |
| `br` | core | Behavioural Risks | `mergeid` | 27 | 57,982 | `sharew4_rel9-0-0_br.dta` |
| `cf` | core | Cognitive Function | `mergeid` | 36 | 57,982 | `sharew4_rel9-0-0_cf.dta` |
| `ch` | core | Children | `mergeid` | 915 | 57,982 | `sharew4_rel9-0-0_ch.dta` |
| `co` | core | Consumption | `mergeid` | 25 | 57,982 | `sharew4_rel9-0-0_co.dta` |
| `cv_r` | core | Coverscreen on individual level | `mergeid` | 30 | 82,927 | `sharew4_rel9-0-0_cv_r.dta` |
| `dn` | core | Demographics | `mergeid` | 76 | 57,982 | `sharew4_rel9-0-0_dn.dta` |
| `ep` | core | Employment and Pensions | `mergeid` | 548 | 57,982 | `sharew4_rel9-0-0_ep.dta` |
| `ex` | core | Expectations | `mergeid` | 25 | 57,982 | `sharew4_rel9-0-0_ex.dta` |
| `ft` | core | Financial Transfers | `mergeid` | 53 | 57,982 | `sharew4_rel9-0-0_ft.dta` |
| `gs` | core | Grip Strength | `mergeid` | 23 | 57,982 | `sharew4_rel9-0-0_gs.dta` |
| `hc` | core | Health Care | `mergeid` | 29 | 57,982 | `sharew4_rel9-0-0_hc.dta` |
| `hh` | core | Household Income | `mergeid` | 25 | 57,982 | `sharew4_rel9-0-0_hh.dta` |
| `ho` | core | Housing | `mergeid` | 88 | 57,982 | `sharew4_rel9-0-0_ho.dta` |
| `iv` | core | Interviewer Observations | `mergeid` | 27 | 57,982 | `sharew4_rel9-0-0_iv.dta` |
| `mh` | core | Mental Health | `mergeid` | 35 | 57,982 | `sharew4_rel9-0-0_mh.dta` |
| `pf` | core | Peak Flow | `mergeid` | 17 | 57,982 | `sharew4_rel9-0-0_pf.dta` |
| `ph` | core | Physical Health | `mergeid` | 185 | 57,982 | `sharew4_rel9-0-0_ph.dta` |
| `sn` | core | Social Networks | `mergeid` | 56 | 57,982 | `sharew4_rel9-0-0_sn.dta` |
| `sp` | core | Social Support | `mergeid` | 140 | 57,982 | `sharew4_rel9-0-0_sp.dta` |
| `xt` | core | End-of-Life Interview | `mergeid` | 172 | 1,174 | `sharew4_rel9-0-0_xt.dta` |
| `dropoff` | special | Paper-and-pencil drop-off | `mergeid` | 1,261 | 46,684 | `sharew4_rel9-0-0_dropoff.dta` |
| `technical_variables` | special | Technical variables | `mergeid` | 17 | 57,982 | `sharew4_rel9-0-0_technical_variables.dta` |
| `gv_children` | generated | Generated child-level summaries | `mergeid` | 347 | 57,982 | `sharew4_rel9-0-0_gv_children.dta` |
| `gv_exrates` | generated | Exchange rates and PPP variables | `country` | 76 | 29 | `sharew4_rel9-0-0_gv_exrates.dta` |
| `gv_health` | generated | Generated health indicators | `mergeid` | 45 | 57,982 | `sharew4_rel9-0-0_gv_health.dta` |
| `gv_housing` | generated | Housing generated variables | `mergeid` | 11 | 57,982 | `sharew4_rel9-0-0_gv_housing.dta` |
| `gv_imputations` | generated | Multiple imputations | `mergeid` | 236 | 289,910 | `sharew4_rel9-0-0_gv_imputations.dta` |
| `gv_isced` | generated | ISCED education recodes | `mergeid` | 28 | 57,982 | `sharew4_rel9-0-0_gv_isced.dta` |
| `gv_networks` | generated | Generated social network variables | `mergeid` | 102 | 57,982 | `sharew4_rel9-0-0_gv_networks.dta` |
| `gv_ssw` | generated | Social security wealth | `mergeid` | 8 | 57,982 | `sharew4_rel9-0-0_gv_ssw.dta` |
| `gv_weights` | generated | Cross-sectional weights | `mergeid` | 14 | 57,982 | `sharew4_rel9-0-0_gv_weights.dta` |

## Core Interview Modules

### `ac` - Activities

- Dataset: `sharew4_rel9-0-0_ac.dta`
- Read with: `ps.read_share_module("ac", wave=4)`
- Rows: 57,982
- Variables: 38
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ac012_` | How satisfied with life | `Numeric(Byte)` | `%11.0g` |
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
| `ac035d6` | Activities in last year: taken part in activities of a religious organization | `Numeric(Byte)` | `%12.0g` |
| `ac035d7` | Activities in last year: taken part in a political or community-related organiza | `Numeric(Byte)` | `%12.0g` |
| `ac035d8` | Activities in last year: read books, magazines or newspapers | `Numeric(Byte)` | `%12.0g` |
| `ac035d9` | Activities in last year: did word or number games (crossword puzzles/Sudoku...) | `Numeric(Byte)` | `%12.0g` |
| `ac035d10` | Activities in last year: played cards or games such as chess | `Numeric(Byte)` | `%12.0g` |
| `ac035dno` | Activities in last year: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac036_1` | How often done voluntary/charity work the last 12 months | `Numeric(Byte)` | `%18.0g` |
| `ac036_4` | How often attended an educational or training course the last 12 months | `Numeric(Byte)` | `%18.0g` |
| `ac036_5` | How often gone to a sport/social/other kind of club the last 12 months | `Numeric(Byte)` | `%18.0g` |
| `ac036_6` | How often taken part in activities of a religious organization the last 12 month | `Numeric(Byte)` | `%18.0g` |
| `ac036_7` | How often taken part in a political/community-related organization the last 12 m | `Numeric(Byte)` | `%18.0g` |
| `ac036_8` | How often read books, magazines or newspapers the last 12 months | `Numeric(Byte)` | `%18.0g` |
| `ac036_9` | How often did word or number games the last 12 months | `Numeric(Byte)` | `%18.0g` |
| `ac036_10` | How often played cards or games such as chess the last 12 months | `Numeric(Byte)` | `%18.0g` |
| `ac037_` | Satisfied with activities | `Numeric(Byte)` | `%11.0g` |
| `ac038_` | Satisfied with no activities | `Numeric(Byte)` | `%11.0g` |

### `as` - Assets

- Dataset: `sharew4_rel9-0-0_as.dta`
- Read with: `ps.read_share_module("as", wave=4)`
- Rows: 57,982
- Variables: 96
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `as003e` | Amount bank account | `Numeric(Double)` | `%11.0g` |
| `as003ub` | Amount bank account ub | `Numeric(Byte)` | `%32.0g` |
| `as003v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `as003v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `as003v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `as007e` | Amount in bonds | `Numeric(Double)` | `%11.0g` |
| `as007ub` | Amount in bonds ub | `Numeric(Byte)` | `%32.0g` |
| `as007v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `as007v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `as007v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `as011e` | Amount in stocks | `Numeric(Double)` | `%11.0g` |
| `as011ub` | Amount in stocks ub | `Numeric(Byte)` | `%32.0g` |
| `as011v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `as011v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `as011v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `as017e` | Amount in mutual funds | `Numeric(Double)` | `%11.0g` |
| `as017ub` | Amount in mutual funds ub | `Numeric(Byte)` | `%32.0g` |
| `as017v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `as017v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `as017v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `as019_` | Mutual funds mostly stocks or bonds | `Numeric(Byte)` | `%26.0g` |
| `as020_` | Who has individual retirement accounts | `Numeric(Byte)` | `%25.0g` |
| `as021e` | Amount individual retirement accounts | `Numeric(Double)` | `%11.0g` |
| `as021ub` | Amount individual retirement accounts ub | `Numeric(Byte)` | `%32.0g` |
| `as021v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `as021v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `as021v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `as023_` | Individual retirement accounts mostly in stocks or bonds | `Numeric(Byte)` | `%29.0g` |
| `as024e` | Partner amount individual retirement accounts | `Numeric(Double)` | `%11.0g` |
| `as024ub` | Partner amount individual retirement accounts ub | `Numeric(Byte)` | `%32.0g` |
| `as024v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `as024v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `as024v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `as026_` | Partner individual retirement accounts mostly in stocks or bonds | `Numeric(Byte)` | `%32.0g` |
| `as027e` | Amount contractual saving for housing | `Numeric(Double)` | `%11.0g` |
| `as027ub` | Amount contractual saving for housing ub | `Numeric(Byte)` | `%32.0g` |
| `as027v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `as027v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `as027v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `as029_` | Life insurance policies term or whole life | `Numeric(Byte)` | `%20.0g` |
| `as030e` | Face value of whole life policies | `Numeric(Double)` | `%11.0g` |
| `as030ub` | Face value of whole life policies ub | `Numeric(Byte)` | `%32.0g` |
| `as030v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `as030v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `as030v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `as041_` | Own firm company business | `Numeric(Byte)` | `%11.0g` |
| `as042e` | Amount selling firm | `Numeric(Double)` | `%11.0g` |
| `as042ub` | Amount selling firm ub | `Numeric(Byte)` | `%32.0g` |
| `as042v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `as042v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `as042v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `as044_` | Percentage share firm owned | `Numeric(Byte)` | `%11.0g` |
| `as044ub` | Percentage share firm owned ub | `Numeric(Byte)` | `%32.0g` |
| `as044v1` | Bracket value 1 | `Numeric(Byte)` | `%11.0g` |
| `as044v2` | Bracket value 2 | `Numeric(Byte)` | `%11.0g` |
| `as044v3` | Bracket value 3 | `Numeric(Byte)` | `%11.0g` |
| `as049_` | Number of cars | `Numeric(Byte)` | `%11.0g` |
| `as051e` | Amount selling cars | `Numeric(Double)` | `%11.0g` |
| `as051ub` | Amount selling cars ub | `Numeric(Byte)` | `%32.0g` |
| `as051v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `as051v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `as051v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `as054d1` | Owe money: debt on cars and other vehicles (vans/motorcycles/boats, etc.) | `Numeric(Byte)` | `%12.0g` |
| `as054d2` | Owe money: debt on credit cards/store cards | `Numeric(Byte)` | `%12.0g` |
| `as054d3` | Owe money: loans (from bank, building society, other financial institution) | `Numeric(Byte)` | `%12.0g` |
| `as054d4` | Owe money: debts to relatives or friends | `Numeric(Byte)` | `%12.0g` |
| `as054d5` | Owe money: student loans | `Numeric(Byte)` | `%12.0g` |
| `as054d6` | Owe money: overdue bills (phone, electricity, heating, rent) | `Numeric(Byte)` | `%12.0g` |
| `as054dno` | Owe money: none of these | `Numeric(Byte)` | `%12.0g` |
| `as054dot` | Owe money: other | `Numeric(Byte)` | `%12.0g` |
| `as055e` | Amount owing money in total | `Numeric(Double)` | `%11.0g` |
| `as055ub` | Amount owing money in total ub | `Numeric(Byte)` | `%32.0g` |
| `as055v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `as055v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `as055v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `as057_` | Who answered the question in as | `Numeric(Byte)` | `%44.0g` |
| `as060_` | Has bank account | `Numeric(Byte)` | `%11.0g` |
| `as061_` | Reason for not having a bank account | `Numeric(Byte)` | `%80.0g` |
| `as062_` | Has bonds | `Numeric(Byte)` | `%11.0g` |
| `as063_` | Has stocks | `Numeric(Byte)` | `%11.0g` |
| `as064_` | Has mutual funds | `Numeric(Byte)` | `%11.0g` |
| `as065_` | Has individual retirement accounts | `Numeric(Byte)` | `%11.0g` |
| `as066_` | Has contractual saving | `Numeric(Byte)` | `%11.0g` |
| `as067_` | Has life insurance | `Numeric(Byte)` | `%11.0g` |
| `as070e` | Interest or dividend income | `Numeric(Double)` | `%11.0g` |
| `as070ub` | Interest or dividend income ub | `Numeric(Byte)` | `%32.0g` |
| `as070v1` | Bracket value 1 | `Numeric(Float)` | `%11.0g` |
| `as070v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `as070v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |

### `br` - Behavioural Risks

- Dataset: `sharew4_rel9-0-0_br.dta`
- Read with: `ps.read_share_module("br", wave=4)`
- Rows: 57,982
- Variables: 27
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `br001_` | Ever smoked daily | `Numeric(Byte)` | `%11.0g` |
| `br002_` | Smoke at the present time | `Numeric(Byte)` | `%11.0g` |
| `br003_` | How many years smoked | `Numeric(Byte)` | `%11.0g` |
| `br010_` | Days a week consumed alcohol last 3 months | `Numeric(Byte)` | `%38.0g` |
| `br015_` | Sports or activities that are vigorous | `Numeric(Byte)` | `%26.0g` |
| `br016_` | Activities requiring a moderate level of energy | `Numeric(Byte)` | `%26.0g` |
| `br017_` | Who answered the questions in br | `Numeric(Byte)` | `%44.0g` |
| `br019_` | How many drinks in a day | `Numeric(Float)` | `%11.0g` |
| `br021_` | Ever drunk alcoholic beverages | `Numeric(Byte)` | `%11.0g` |
| `br022_` | Stopped smoking | `Numeric(Byte)` | `%60.0g` |
| `br023_` | How often six or more drinks last 3 months | `Numeric(Byte)` | `%38.0g` |
| `br024_` | Drinking problem | `Numeric(Byte)` | `%11.0g` |
| `br025_` | How many meals a day | `Numeric(Byte)` | `%11.0g` |
| `br025a_` | Three meals every day | `Numeric(Byte)` | `%11.0g` |
| `br026_` | How often serving of dairy products | `Numeric(Byte)` | `%31.0g` |
| `br027_` | How often serving of legumes or eggs | `Numeric(Byte)` | `%31.0g` |
| `br028_` | How often serving of meat, fish or chicken | `Numeric(Byte)` | `%31.0g` |
| `br029_` | How often serving of fruits or vegetables | `Numeric(Byte)` | `%31.0g` |
| `br030_` | How many cups a day drinks of tea, coffee, water, milk, fruit, soft drinks | `Numeric(Byte)` | `%19.0g` |
| `br031_` | Year stopped smoking for the last time | `Numeric(Byte)` | `%11.0g` |
| `br032_` | Month stopped smoking for the last time | `Numeric(Byte)` | `%11.0g` |

### `cf` - Cognitive Function

- Dataset: `sharew4_rel9-0-0_cf.dta`
- Read with: `ps.read_share_module("cf", wave=4)`
- Rows: 57,982
- Variables: 36
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `cf001_` | Self-rated reading skills | `Numeric(Byte)` | `%13.0g` |
| `cf002_` | Self-rated writing skills | `Numeric(Byte)` | `%13.0g` |
| `cf003_` | Date: day of month | `Numeric(Byte)` | `%47.0g` |
| `cf004_` | Date: month | `Numeric(Byte)` | `%47.0g` |
| `cf005_` | Date: year | `Numeric(Byte)` | `%45.0g` |
| `cf006_` | Date: day of the week | `Numeric(Byte)` | `%55.0g` |
| `cf010_` | Verbal fluency score: number of animals | `Numeric(Byte)` | `%11.0g` |
| `cf012_` | Numeracy: chance disease 10% of 1000 | `Numeric(Byte)` | `%19.0g` |
| `cf013_` | Numeracy: half price | `Numeric(Byte)` | `%19.0g` |
| `cf014_` | Numeracy: 6000 is two-thirds what is total price | `Numeric(Byte)` | `%23.0g` |
| `cf015_` | Numeracy: amount in the savings account | `Numeric(Byte)` | `%22.0g` |
| `cf017_` | Contextual factors during the cognitive function test | `Numeric(Byte)` | `%11.0g` |
| `cf018d1` | Who present during cf: respondent alone | `Numeric(Byte)` | `%12.0g` |
| `cf018d2` | Who present during cf: partner present | `Numeric(Byte)` | `%12.0g` |
| `cf018d3` | Who present during cf: child(ren) present | `Numeric(Byte)` | `%12.0g` |
| `cf018d4` | Who present during cf: other(s) | `Numeric(Byte)` | `%12.0g` |
| `cf103_` | Memory | `Numeric(Byte)` | `%13.0g` |
| `cf104tot` | Ten words list learning first trail | `Numeric(Byte)` | `%9.0g` |
| `cf105tot` | Ten words list learning first trail | `Numeric(Byte)` | `%9.0g` |
| `cf106tot` | Ten words list learning first trail | `Numeric(Byte)` | `%9.0g` |
| `cf107tot` | Ten words list learning first trail | `Numeric(Byte)` | `%9.0g` |
| `cf108_` | Numeracy: subtraction 1 | `Numeric(Long)` | `%11.0g` |
| `cf109_` | Numeracy: subtraction 2 | `Numeric(Long)` | `%11.0g` |
| `cf110_` | Numeracy: subtraction 3 | `Numeric(Long)` | `%11.0g` |
| `cf111_` | Numeracy: subtraction 4 | `Numeric(Long)` | `%11.0g` |
| `cf112_` | Numeracy: subtraction 5 | `Numeric(Long)` | `%11.0g` |
| `cf113tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `cf114tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `cf115tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `cf116tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |

### `ch` - Children

- Dataset: `sharew4_rel9-0-0_ch.dta`
- Read with: `ps.read_share_module("ch", wave=4)`
- Rows: 57,982
- Variables: 915
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
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
| `childid_15` | Child identifier (fix across modules and waves): Child 15 | `Str(1)` | `%9s` |
| `childid_16` | Child identifier (fix across modules and waves): Child 16 | `Str(14)` | `%14s` |
| `childid_17` | Child identifier (fix across modules and waves): Child 17 | `Str(1)` | `%9s` |
| `childid_18` | Child identifier (fix across modules and waves): Child 18 | `Str(1)` | `%9s` |
| `childid_19` | Child identifier (fix across modules and waves): Child 19 | `Str(1)` | `%9s` |
| `childid_20` | Child identifier (fix across modules and waves): Child 20 | `Str(1)` | `%9s` |
| `ch001_` | Number of children | `Numeric(Byte)` | `%11.0g` |
| `ch002_1` | Child 1 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_2` | Child 2 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_3` | Child 3 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_4` | Child 4 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_5` | Child 5 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_6` | Child 6 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_7` | Child 7 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_8` | Child 8 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_9` | Child 9 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_10` | Child 10 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_11` | Child 11 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_12` | Child 12 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_13` | Child 13 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_14` | Child 14 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_15` | Child 15 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_16` | Child 16 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_17` | Child 17 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_18` | Child 18 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_19` | Child 19 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch002_20` | Child 20 is natural child | `Numeric(Byte)` | `%11.0g` |
| `ch005_1` | Child 1 gender | `Numeric(Long)` | `%11.0g` |
| `ch005_2` | Child 2 gender | `Numeric(Long)` | `%11.0g` |
| `ch005_3` | Child 3 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_4` | Child 4 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_5` | Child 5 gender | `Numeric(Long)` | `%11.0g` |
| `ch005_6` | Child 6 gender | `Numeric(Long)` | `%11.0g` |
| `ch005_7` | Child 7 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_8` | Child 8 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_9` | Child 9 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_10` | Child 10 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_11` | Child 11 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_12` | Child 12 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_13` | Child 13 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_14` | Child 14 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_15` | Child 15 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_16` | Child 16 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_17` | Child 17 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_18` | Child 18 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_19` | Child 19 gender | `Numeric(Byte)` | `%11.0g` |
| `ch005_20` | Child 20 gender | `Numeric(Byte)` | `%11.0g` |
| `ch006_1` | Child 1 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_2` | Child 2 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_3` | Child 3 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_4` | Child 4 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_5` | Child 5 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_6` | Child 6 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_7` | Child 7 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_8` | Child 8 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_9` | Child 9 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_10` | Child 10 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_11` | Child 11 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_12` | Child 12 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_13` | Child 13 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_14` | Child 14 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_15` | Child 15 year of birth | `Numeric(Byte)` | `%11.0g` |
| `ch006_16` | Child 16 year of birth | `Numeric(Int)` | `%11.0g` |
| `ch006_17` | Child 17 year of birth | `Numeric(Byte)` | `%11.0g` |
| `ch006_18` | Child 18 year of birth | `Numeric(Byte)` | `%11.0g` |
| `ch006_19` | Child 19 year of birth | `Numeric(Byte)` | `%11.0g` |
| `ch006_20` | Child 20 year of birth | `Numeric(Byte)` | `%11.0g` |
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
| `ch010_1` | Child 1 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_2` | Child 2 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_3` | Child 3 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_4` | Child 4 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_5` | Child 5 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_6` | Child 6 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_7` | Child 7 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_8` | Child 8 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_9` | Child 9 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_10` | Child 10 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_11` | Child 11 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_12` | Child 12 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_13` | Child 13 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_14` | Child 14 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_15` | Child 15 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_16` | Child 16 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_17` | Child 17 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_18` | Child 18 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_19` | Child 19 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_20` | Child 20 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch011_1` | Child 1 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_2` | Child 2 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_3` | Child 3 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_4` | Child 4 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_5` | Child 5 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_6` | Child 6 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_7` | Child 7 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_8` | Child 8 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_9` | Child 9 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_10` | Child 10 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_11` | Child 11 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_12` | Child 12 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_13` | Child 13 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_14` | Child 14 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_15` | Child 15 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_16` | Child 16 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_17` | Child 17 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_18` | Child 18 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_19` | Child 19 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_20` | Child 20 own child | `Numeric(Byte)` | `%61.0g` |
| `ch012_1` | Child 1 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_2` | Child 2 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_3` | Child 3 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_4` | Child 4 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_5` | Child 5 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_6` | Child 6 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_7` | Child 7 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_8` | Child 8 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_9` | Child 9 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_10` | Child 10 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_11` | Child 11 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_12` | Child 12 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_13` | Child 13 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_14` | Child 14 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_15` | Child 15 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_16` | Child 16 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_17` | Child 17 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_18` | Child 18 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_19` | Child 19 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch012_20` | Child 20 marital status | `Numeric(Byte)` | `%56.0g` |
| `ch013_1` | Child 1 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_2` | Child 2 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_3` | Child 3 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_4` | Child 4 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_5` | Child 5 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_6` | Child 6 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_7` | Child 7 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_8` | Child 8 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_9` | Child 9 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_10` | Child 10 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_11` | Child 11 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_12` | Child 12 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_13` | Child 13 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_14` | Child 14 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_15` | Child 15 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_16` | Child 16 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_17` | Child 17 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_18` | Child 18 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_19` | Child 19 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch013_20` | Child 20 has partner | `Numeric(Byte)` | `%11.0g` |
| `ch014_1` | Child 1 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_2` | Child 2 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_3` | Child 3 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_4` | Child 4 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_5` | Child 5 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_6` | Child 6 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_7` | Child 7 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_8` | Child 8 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_9` | Child 9 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_10` | Child 10 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_11` | Child 11 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_12` | Child 12 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_13` | Child 13 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_14` | Child 14 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_15` | Child 15 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_16` | Child 16 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_17` | Child 17 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_18` | Child 18 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_19` | Child 19 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_20` | Child 20 contact with child | `Numeric(Byte)` | `%27.0g` |
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
| `ch015_15` | Child 15 year moved out | `Numeric(Byte)` | `%33.0g` |
| `ch015_16` | Child 16 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_17` | Child 17 year moved out | `Numeric(Byte)` | `%33.0g` |
| `ch015_18` | Child 18 year moved out | `Numeric(Byte)` | `%33.0g` |
| `ch015_19` | Child 19 year moved out | `Numeric(Byte)` | `%33.0g` |
| `ch015_20` | Child 20 year moved out | `Numeric(Byte)` | `%33.0g` |
| `ch016_1` | Child 1 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_2` | Child 2 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_3` | Child 3 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_4` | Child 4 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_5` | Child 5 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_6` | Child 6 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_7` | Child 7 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_8` | Child 8 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_9` | Child 9 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_10` | Child 10 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_11` | Child 11 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_12` | Child 12 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_13` | Child 13 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_14` | Child 14 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_15` | Child 15 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_16` | Child 16 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_17` | Child 17 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_18` | Child 18 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_19` | Child 19 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_20` | Child 20 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch017_1` | Child 1 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_2` | Child 2 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_3` | Child 3 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_4` | Child 4 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_5` | Child 5 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_6` | Child 6 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_7` | Child 7 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_8` | Child 8 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_9` | Child 9 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_10` | Child 10 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_11` | Child 11 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_12` | Child 12 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_13` | Child 13 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_14` | Child 14 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_15` | Child 15 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_16` | Child 16 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_17` | Child 17 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_18` | Child 18 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_19` | Child 19 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_20` | Child 20 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch018d1_1` | Child 1 further education country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_2` | Child 2 further education country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_3` | Child 3 further education country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_4` | Child 4 further education country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_5` | Child 5 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_6` | Child 6 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_7` | Child 7 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_8` | Child 8 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_9` | Child 9 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_10` | Child 10 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_11` | Child 11 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_12` | Child 12 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_13` | Child 13 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_14` | Child 14 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_15` | Child 15 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_16` | Child 16 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_17` | Child 17 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_18` | Child 18 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_19` | Child 19 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_20` | Child 20 further education: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_1` | Child 1 further education country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_2` | Child 2 further education country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_3` | Child 3 further education country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_4` | Child 4 further education country specific category 2 | `Numeric(Byte)` | `%12.0g` |
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
| `ch018d3_1` | Child 1 further education country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_2` | Child 2 further education country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_3` | Child 3 further education country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_4` | Child 4 further education country specific category 3 | `Numeric(Byte)` | `%12.0g` |
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
| `ch018d4_1` | Child 1 further education country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_2` | Child 2 further education country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_3` | Child 3 further education country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_4` | Child 4 further education country specific category 4 | `Numeric(Byte)` | `%12.0g` |
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
| `ch018d5_1` | Child 1 further education country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_2` | Child 2 further education country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_3` | Child 3 further education country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_4` | Child 4 further education country specific category 5 | `Numeric(Byte)` | `%12.0g` |
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
| `ch018d6_1` | Child 1 further education country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_2` | Child 2 further education country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_3` | Child 3 further education country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_4` | Child 4 further education country specific category 6 | `Numeric(Byte)` | `%12.0g` |
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
| `ch018d7_1` | Child 1 further education country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_2` | Child 2 further education country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_3` | Child 3 further education country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_4` | Child 4 further education country specific category 7 | `Numeric(Byte)` | `%12.0g` |
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
| `ch018d8_1` | Child 1 further education country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_2` | Child 2 further education country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_3` | Child 3 further education country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_4` | Child 4 further education country specific category 8 | `Numeric(Byte)` | `%12.0g` |
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
| `ch018d9_1` | Child 1 further education country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_2` | Child 2 further education country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_3` | Child 3 further education country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_4` | Child 4 further education country specific category 9 | `Numeric(Byte)` | `%12.0g` |
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
| `ch018d10_1` | Child 1 further education country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_2` | Child 2 further education country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_3` | Child 3 further education country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_4` | Child 4 further education country specific category 10 | `Numeric(Byte)` | `%12.0g` |
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
| `ch018d11_1` | Child 1 further education country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_2` | Child 2 further education country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_3` | Child 3 further education country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_4` | Child 4 further education country specific category 11 | `Numeric(Byte)` | `%12.0g` |
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
| `ch018d12_1` | Child 1 further education country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_2` | Child 2 further education country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_3` | Child 3 further education country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_4` | Child 4 further education country specific category 12 | `Numeric(Byte)` | `%12.0g` |
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
| `ch018d13_1` | Child 1 further education country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_2` | Child 2 further education country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_3` | Child 3 further education country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_4` | Child 4 further education country specific category 13 | `Numeric(Byte)` | `%12.0g` |
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
| `ch018d95_1` | Child 1 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_2` | Child 2 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_3` | Child 3 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_4` | Child 4 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_5` | Child 5 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_6` | Child 6 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_7` | Child 7 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_8` | Child 8 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_9` | Child 9 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_10` | Child 10 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_11` | Child 11 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_12` | Child 12 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_13` | Child 13 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_14` | Child 14 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_15` | Child 15 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_16` | Child 16 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_17` | Child 17 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_18` | Child 18 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_19` | Child 19 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_20` | Child 20 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_1` | Child 1 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_2` | Child 2 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_3` | Child 3 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_4` | Child 4 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_5` | Child 5 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_6` | Child 6 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_7` | Child 7 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_8` | Child 8 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_9` | Child 9 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_10` | Child 10 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_11` | Child 11 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_12` | Child 12 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_13` | Child 13 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_14` | Child 14 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_15` | Child 15 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_16` | Child 16 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_17` | Child 17 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_18` | Child 18 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_19` | Child 19 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_20` | Child 20 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_1` | Child 1 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_2` | Child 2 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_3` | Child 3 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_4` | Child 4 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_5` | Child 5 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_6` | Child 6 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_7` | Child 7 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_8` | Child 8 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_9` | Child 9 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_10` | Child 10 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_11` | Child 11 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_12` | Child 12 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_13` | Child 13 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_14` | Child 14 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_15` | Child 15 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_16` | Child 16 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_17` | Child 17 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_18` | Child 18 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_19` | Child 19 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_20` | Child 20 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch019_1` | Child 1 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_2` | Child 2 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_3` | Child 3 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_4` | Child 4 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_5` | Child 5 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_6` | Child 6 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_7` | Child 7 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_8` | Child 8 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_9` | Child 9 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_10` | Child 10 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_11` | Child 11 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_12` | Child 12 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_13` | Child 13 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_14` | Child 14 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_15` | Child 15 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_16` | Child 16 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_17` | Child 17 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_18` | Child 18 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_19` | Child 19 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch019_20` | Child 20 number of children | `Numeric(Byte)` | `%11.0g` |
| `ch020_1` | Child 1 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_2` | Child 2 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_3` | Child 3 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_4` | Child 4 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_5` | Child 5 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_6` | Child 6 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_7` | Child 7 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_8` | Child 8 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_9` | Child 9 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_10` | Child 10 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_11` | Child 11 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_12` | Child 12 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_13` | Child 13 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_14` | Child 14 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_15` | Child 15 year of birth youngest child | `Numeric(Byte)` | `%11.0g` |
| `ch020_16` | Child 16 year of birth youngest child | `Numeric(Int)` | `%11.0g` |
| `ch020_17` | Child 17 year of birth youngest child | `Numeric(Byte)` | `%11.0g` |
| `ch020_18` | Child 18 year of birth youngest child | `Numeric(Byte)` | `%11.0g` |
| `ch020_19` | Child 19 year of birth youngest child | `Numeric(Byte)` | `%11.0g` |
| `ch020_20` | Child 20 year of birth youngest child | `Numeric(Byte)` | `%11.0g` |
| `ch021_` | Number of grandchildren | `Numeric(Byte)` | `%11.0g` |
| `ch022_` | Has great-grandchildren | `Numeric(Byte)` | `%11.0g` |
| `ch023_` | Who answered questions in section CH | `Numeric(Byte)` | `%44.0g` |
| `ch504_1` | Child 1 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_2` | Child 2 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_3` | Child 3 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_4` | Child 4 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_5` | Child 5 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_6` | Child 6 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_7` | Child 7 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_8` | Child 8 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_9` | Child 9 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_10` | Child 10 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_11` | Child 11 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_12` | Child 12 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_13` | Child 13 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_14` | Child 14 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_15` | Child 15 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_16` | Child 16 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_17` | Child 17 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_18` | Child 18 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_19` | Child 19 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch504_20` | Child 20 why removed | `Numeric(Byte)` | `%60.0g` |
| `ch505_1` | Child 1 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_2` | Child 2 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_3` | Child 3 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_4` | Child 4 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_5` | Child 5 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_6` | Child 6 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_7` | Child 7 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_8` | Child 8 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_9` | Child 9 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_10` | Child 10 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_11` | Child 11 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_12` | Child 12 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_13` | Child 13 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_14` | Child 14 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_15` | Child 15 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_16` | Child 16 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_17` | Child 17 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_18` | Child 18 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_19` | Child 19 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch505_20` | Child 20 equal to which child | `Numeric(Byte)` | `%12.0g` |
| `ch508_` | Check children education changed | `Numeric(Byte)` | `%11.0g` |
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
| `ch510_1` | Child 1 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_2` | Child 2 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_3` | Child 3 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_4` | Child 4 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_5` | Child 5 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_6` | Child 6 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_7` | Child 7 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_8` | Child 8 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_9` | Child 9 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_10` | Child 10 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_11` | Child 11 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_12` | Child 12 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_13` | Child 13 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_14` | Child 14 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_15` | Child 15 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_16` | Child 16 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_17` | Child 17 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_18` | Child 18 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_19` | Child 19 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch510_20` | Child 20 new educational degree | `Numeric(Byte)` | `%47.0g` |
| `ch511_` | Check children further education changed | `Numeric(Byte)` | `%11.0g` |
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
| `ch513_1` | Child 1 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_2` | Child 2 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_3` | Child 3 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_4` | Child 4 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_5` | Child 5 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_6` | Child 6 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_7` | Child 7 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_8` | Child 8 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_9` | Child 9 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_10` | Child 10 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_11` | Child 11 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_12` | Child 12 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_13` | Child 13 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_14` | Child 14 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_15` | Child 15 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_16` | Child 16 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_17` | Child 17 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_18` | Child 18 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_19` | Child 19 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch513_20` | Child 20 degree obtained | `Numeric(Byte)` | `%61.0g` |
| `ch514_` | Check children marital status changed | `Numeric(Byte)` | `%11.0g` |
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
| `ch516_1` | Child 1 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_2` | Child 2 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_3` | Child 3 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_4` | Child 4 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_5` | Child 5 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_6` | Child 6 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_7` | Child 7 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_8` | Child 8 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_9` | Child 9 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_10` | Child 10 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_11` | Child 11 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_12` | Child 12 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_13` | Child 13 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_14` | Child 14 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_15` | Child 15 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_16` | Child 16 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_17` | Child 17 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_18` | Child 18 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_19` | Child 19 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch516_20` | Child 20 new marital status | `Numeric(Byte)` | `%56.0g` |
| `ch517_` | Check children parenthood changed | `Numeric(Byte)` | `%11.0g` |
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
| `ch519_1` | Child 1 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_2` | Child 2 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_3` | Child 3 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_4` | Child 4 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_5` | Child 5 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_6` | Child 6 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_7` | Child 7 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_8` | Child 8 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_9` | Child 9 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_10` | Child 10 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_11` | Child 11 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_12` | Child 12 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_13` | Child 13 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_14` | Child 14 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_15` | Child 15 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_16` | Child 16 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_17` | Child 17 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_18` | Child 18 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_19` | Child 19 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch519_20` | Child 20 new number of children | `Numeric(Byte)` | `%11.0g` |
| `ch520_1` | Child 1 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_2` | Child 2 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_3` | Child 3 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_4` | Child 4 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_5` | Child 5 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_6` | Child 6 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_7` | Child 7 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_8` | Child 8 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_9` | Child 9 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_10` | Child 10 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_11` | Child 11 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_12` | Child 12 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_13` | Child 13 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_14` | Child 14 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_15` | Child 15 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_16` | Child 16 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_17` | Child 17 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_18` | Child 18 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_19` | Child 19 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch520_20` | Child 20 new youngest born | `Numeric(Byte)` | `%17.0g` |
| `ch524_` | Check location of children changed | `Numeric(Byte)` | `%11.0g` |
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
| `ch526_1` | Child 1 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_2` | Child 2 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_3` | Child 3 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_4` | Child 4 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_5` | Child 5 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_6` | Child 6 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_7` | Child 7 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_8` | Child 8 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_9` | Child 9 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_10` | Child 10 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_11` | Child 11 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_12` | Child 12 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_13` | Child 13 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_14` | Child 14 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_15` | Child 15 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_16` | Child 16 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_17` | Child 17 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_18` | Child 18 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_19` | Child 19 where does child live | `Numeric(Byte)` | `%39.0g` |
| `ch526_20` | Child 20 where does child live | `Numeric(Byte)` | `%39.0g` |
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

- Dataset: `sharew4_rel9-0-0_co.dta`
- Read with: `ps.read_share_module("co", wave=4)`
- Rows: 57,982
- Variables: 25
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `co002e` | Amount spent on food at home | `Numeric(Double)` | `%11.0g` |
| `co002ub` | Amount spent on food at home ub | `Numeric(Byte)` | `%32.0g` |
| `co002v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `co002v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `co002v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `co003e` | Amount spent on food outside the home | `Numeric(Double)` | `%11.0g` |
| `co003ub` | Amount spent on food outside the home ub | `Numeric(Byte)` | `%32.0g` |
| `co003v1` | Bracket value 1 | `Numeric(Float)` | `%11.0g` |
| `co003v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `co003v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `co007_` | Is household able to make ends meet | `Numeric(Byte)` | `%28.0g` |
| `co009_` | Who answered the questions in co | `Numeric(Byte)` | `%44.0g` |
| `co010_` | Consume home produced food | `Numeric(Byte)` | `%11.0g` |
| `co011e` | Value of home produced food | `Numeric(Double)` | `%11.0g` |
| `co011ub` | Value of home produced food ub | `Numeric(Byte)` | `%32.0g` |
| `co011v1` | Bracket value 1 | `Numeric(Float)` | `%11.0g` |
| `co011v2` | Bracket value 2 | `Numeric(Float)` | `%11.0g` |
| `co011v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |

### `cv_r` - Coverscreen on individual level

- Dataset: `sharew4_rel9-0-0_cv_r.dta`
- Read with: `ps.read_share_module("cv_r", wave=4)`
- Rows: 82,927
- Variables: 30
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `waveid` | Identifier of original wave (person) | `Numeric(Int)` | `%9.0g` |
| `waveid_hh` | Identifier of original wave (household) | `Numeric(Int)` | `%10.0g` |
| `firstwave` | First appearance of person in SHARE | `Numeric(Byte)` | `%9.0g` |
| `firstwave_hh` | Wave household was sampled/first participated | `Numeric(Byte)` | `%9.0g` |
| `cvresp` | Coverscreen respondent | `Numeric(Byte)` | `%10.0g` |
| `deceased` | Deceased | `Numeric(Byte)` | `%10.0g` |
| `gender` | Male or female | `Numeric(Byte)` | `%10.0g` |
| `mobirth` | Month of birth | `Numeric(Byte)` | `%10.0g` |
| `yrbirth` | Year of birth | `Numeric(Int)` | `%10.0g` |
| `age2011` | Age in 2011 | `Numeric(Int)` | `%14.0g` |
| `age_int` | Age of respondent at the time of interview | `Numeric(Int)` | `%14.0g` |
| `mobirthp` | Month of birth spouse/partner | `Numeric(Byte)` | `%14.0g` |
| `yrbirthp` | Year of birth spouse/partner | `Numeric(Int)` | `%14.0g` |
| `agep2011` | Age of partner in 2011 | `Numeric(Byte)` | `%14.0g` |
| `partnerinhh` | Partner in household | `Numeric(Byte)` | `%14.0g` |
| `relrpers` | Relation to coverscreen respondent | `Numeric(Byte)` | `%47.0g` |
| `hhsize` | Household size | `Numeric(Byte)` | `%9.0g` |
| `fam_resp` | Family respondent | `Numeric(Byte)` | `%21.0g` |
| `fin_resp` | Financial respondent | `Numeric(Byte)` | `%24.0g` |
| `hou_resp` | Household respondent | `Numeric(Byte)` | `%24.0g` |
| `interview` | Interview done in wave 4 | `Numeric(Byte)` | `%21.0g` |
| `int_year` | Interview year | `Numeric(Int)` | `%14.0g` |
| `int_month` | Interview month | `Numeric(Byte)` | `%14.0g` |
| `PTsample` | Portugal only: sample indication | `Numeric(Byte)` | `%14.0g` |

### `dn` - Demographics

- Dataset: `sharew4_rel9-0-0_dn.dta`
- Read with: `ps.read_share_module("dn", wave=4)`
- Rows: 57,982
- Variables: 76
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `dn002_` | Month of birth | `Numeric(Byte)` | `%11.0g` |
| `dn003_` | Year of birth | `Numeric(Int)` | `%11.0g` |
| `dn004_` | Born in the country of interview | `Numeric(Byte)` | `%11.0g` |
| `dn005c` | Foreign country of birth coding | `Numeric(Int)` | `%46.0g` |
| `dn006_` | Year came to live in country | `Numeric(Int)` | `%11.0g` |
| `dn007_` | Citizenship country of interview | `Numeric(Byte)` | `%11.0g` |
| `dn008c` | Other citizenship coding | `Numeric(Int)` | `%46.0g` |
| `dn009_` | Country-specific question | `Numeric(Byte)` | `%25.0g` |
| `dn010_` | Highest school degree obtained | `Numeric(Byte)` | `%47.0g` |
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
| `dn012d95` | Further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `dn012dno` | Further education: none | `Numeric(Byte)` | `%12.0g` |
| `dn012dot` | Further education: other | `Numeric(Byte)` | `%12.0g` |
| `dn014_` | Marital status | `Numeric(Byte)` | `%56.0g` |
| `dn015_` | Year of marriage, if living together | `Numeric(Int)` | `%11.0g` |
| `dn016_` | Year of registered partnership | `Numeric(Int)` | `%11.0g` |
| `dn017_` | Year of marriage, if living separated | `Numeric(Int)` | `%11.0g` |
| `dn018_` | Since when divorced | `Numeric(Int)` | `%11.0g` |
| `dn019_` | Since when widowed | `Numeric(Int)` | `%11.0g` |
| `dn020_` | Year of birth of former partner | `Numeric(Int)` | `%11.0g` |
| `dn021_` | Highest educational degree of former partner | `Numeric(Byte)` | `%47.0g` |
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
| `dn023d95` | Further education former partner: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `dn023dno` | Further education former partner: none | `Numeric(Byte)` | `%12.0g` |
| `dn023dot` | Further education former partner: other | `Numeric(Byte)` | `%12.0g` |
| `dn026_1` | Is natural parent still alive: mother | `Numeric(Byte)` | `%11.0g` |
| `dn026_2` | Is natural parent still alive: father | `Numeric(Byte)` | `%11.0g` |
| `dn027_1` | Age of death of parent: mother | `Numeric(Int)` | `%11.0g` |
| `dn027_2` | Age of death of parent: father | `Numeric(Int)` | `%11.0g` |
| `dn028_1` | Age of natural parent: mother | `Numeric(Int)` | `%11.0g` |
| `dn028_2` | Age of natural parent: father | `Numeric(Int)` | `%11.0g` |
| `dn030_1` | Where does parent live: mother | `Numeric(Byte)` | `%48.0g` |
| `dn030_2` | Where does parent live: father | `Numeric(Byte)` | `%48.0g` |
| `dn032_1` | Personal contact with parent during past 12 months: mother | `Numeric(Byte)` | `%27.0g` |
| `dn032_2` | Personal contact with parent during past 12 months: father | `Numeric(Byte)` | `%27.0g` |
| `dn033_1` | Health of parent: mother | `Numeric(Byte)` | `%13.0g` |
| `dn033_2` | Health of parent: father | `Numeric(Byte)` | `%13.0g` |
| `dn034_` | Ever had any siblings | `Numeric(Byte)` | `%11.0g` |
| `dn035_` | Oldest or youngest child | `Numeric(Byte)` | `%12.0g` |
| `dn036_` | How many brothers alive | `Numeric(Byte)` | `%11.0g` |
| `dn037_` | How many sisters alive | `Numeric(Byte)` | `%11.0g` |
| `dn040_` | Partner outside household | `Numeric(Byte)` | `%11.0g` |
| `dn041_` | Years education | `Numeric(Byte)` | `%35.0g` |
| `dn042_` | Male or female | `Numeric(Byte)` | `%11.0g` |
| `dn043_` | Confirm month/year birth | `Numeric(Byte)` | `%11.0g` |
| `dn044_` | Marital status changed | `Numeric(Byte)` | `%49.0g` |

### `ep` - Employment and Pensions

- Dataset: `sharew4_rel9-0-0_ep.dta`
- Read with: `ps.read_share_module("ep", wave=4)`
- Rows: 57,982
- Variables: 548
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `ep002_` | Did nevertheless any paid work last four weeks | `Numeric(Byte)` | `%11.0g` |
| `ep005_` | Current job situation | `Numeric(Byte)` | `%65.0g` |
| `ep006_` | Ever done paid work | `Numeric(Byte)` | `%11.0g` |
| `ep007_` | Currently more than one job | `Numeric(Byte)` | `%11.0g` |
| `ep009_` | Employee or self-employed | `Numeric(Byte)` | `%47.0g` |
| `ep010_` | Start of current job (year) | `Numeric(Int)` | `%11.0g` |
| `ep011_` | Term of job | `Numeric(Byte)` | `%27.0g` |
| `ep012_` | Total contracted hours per week in this job | `Numeric(Double)` | `%11.0g` |
| `ep013_` | Total hours usually working per week | `Numeric(Double)` | `%11.0g` |
| `ep014_` | Months per year working in the job (number) | `Numeric(Byte)` | `%11.0g` |
| `ep016_` | Name or title of job | `Numeric(Byte)` | `%63.0g` |
| `ep018_` | Kind of industry working in | `Numeric(Byte)` | `%98.0g` |
| `ep019_` | Firm belongs to the public sector | `Numeric(Byte)` | `%11.0g` |
| `ep024_` | Number of employees | `Numeric(Byte)` | `%13.0g` |
| `ep026_` | Satisfied with (main) job | `Numeric(Byte)` | `%26.0g` |
| `ep027_` | (Main) job physically demanding | `Numeric(Byte)` | `%26.0g` |
| `ep028_` | Time pressure due to a heavy workload in (main) job | `Numeric(Byte)` | `%26.0g` |
| `ep029_` | Little freedom to decide how I do my work in (main) job | `Numeric(Byte)` | `%26.0g` |
| `ep030_` | Opportunity to develop new skills in (main) job | `Numeric(Byte)` | `%26.0g` |
| `ep031_` | Receive support in difficult situations in (main) job | `Numeric(Byte)` | `%26.0g` |
| `ep032_` | Receive recognition for work in (main) job | `Numeric(Byte)` | `%26.0g` |
| `ep033_` | Salary or earnings are adequate in (main) job | `Numeric(Byte)` | `%26.0g` |
| `ep034_` | Poor prospects for (main) job advancement | `Numeric(Byte)` | `%26.0g` |
| `ep035_` | Poor (main) job security | `Numeric(Byte)` | `%26.0g` |
| `ep036_` | Look for early retirement in (main) job | `Numeric(Byte)` | `%11.0g` |
| `ep037_` | Afraid health limits ability to work before regular retirement in (main) job | `Numeric(Byte)` | `%11.0g` |
| `ep049_` | Years working in last job | `Numeric(Float)` | `%11.0g` |
| `ep050_` | Year last job ended | `Numeric(Int)` | `%11.0g` |
| `ep051_` | Employee or a self employed in last job | `Numeric(Byte)` | `%36.0g` |
| `ep052_` | Name or title of last job | `Numeric(Byte)` | `%63.0g` |
| `ep054_` | Kind of industry working in last job | `Numeric(Byte)` | `%98.0g` |
| `ep055_` | Employed in the public sector, last job | `Numeric(Byte)` | `%11.0g` |
| `ep061_` | Number of employees, last job | `Numeric(Byte)` | `%13.0g` |
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
| `ep067_` | How became unemployed | `Numeric(Byte)` | `%55.0g` |
| `ep068_` | Disability caused by work | `Numeric(Byte)` | `%11.0g` |
| `ep069d1` | Reason stopped working: health problems | `Numeric(Byte)` | `%12.0g` |
| `ep069d2` | Reason stopped working: too tiring | `Numeric(Byte)` | `%12.0g` |
| `ep069d3` | Reason stopped working: too expensive to hire someone to look after home/family | `Numeric(Byte)` | `%12.0g` |
| `ep069d4` | Reason stopped working: wanted to take care of (grand)children | `Numeric(Byte)` | `%12.0g` |
| `ep069d5` | Reason stopped working: laid off, or workplace/office closed | `Numeric(Byte)` | `%12.0g` |
| `ep069d6` | Reason stopped working: family income sufficient | `Numeric(Byte)` | `%12.0g` |
| `ep069dot` | Reason stopped working: other | `Numeric(Byte)` | `%12.0g` |
| `ep071d1` | Income sources: country-specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ep071d2` | Income sources: country-specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ep071d3` | Income sources: country-specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ep071d4` | Income sources: country-specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ep071d5` | Income sources: country-specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ep071d6` | Income sources: country-specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ep071d7` | Income sources: country-specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ep071d8` | Income sources: country-specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ep071d9` | Income sources: country-specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ep071d10` | Income sources: country-specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ep071d11` | Income sources: country-specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ep071d12` | Income sources: country-specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ep071d13` | Income sources: country-specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ep071d14` | Income sources: country-specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ep071d15` | Income sources: country-specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `ep071dno` | Income sources: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep074_1` | Period of income source c1 (ep071d1) | `Numeric(Byte)` | `%29.0g` |
| `ep074_2` | Period of income source c2 (ep071d2) | `Numeric(Byte)` | `%29.0g` |
| `ep074_3` | Period of income source c3 (ep071d3) | `Numeric(Byte)` | `%29.0g` |
| `ep074_4` | Period of income source c4 (ep071d4) | `Numeric(Byte)` | `%29.0g` |
| `ep074_5` | Period of income source c5 (ep071d5) | `Numeric(Byte)` | `%29.0g` |
| `ep074_6` | Period of income source c6 (ep071d6) | `Numeric(Byte)` | `%29.0g` |
| `ep074_7` | Period of income source c7 (ep071d7) | `Numeric(Byte)` | `%29.0g` |
| `ep074_8` | Period of income source c8 (ep071d8) | `Numeric(Byte)` | `%29.0g` |
| `ep074_9` | Period of income source c9 (ep071d9) | `Numeric(Byte)` | `%29.0g` |
| `ep074_10` | Period of income source c10 (ep071d10) | `Numeric(Byte)` | `%29.0g` |
| `ep074_11` | Period of income source c11 (ep324d1) | `Numeric(Byte)` | `%29.0g` |
| `ep074_12` | Period of income source c12 (ep324d2) | `Numeric(Byte)` | `%29.0g` |
| `ep074_13` | Period of income source c13 (ep324d3) | `Numeric(Byte)` | `%29.0g` |
| `ep074_14` | Period of income source c14 (ep324d4) | `Numeric(Byte)` | `%29.0g` |
| `ep074_15` | Period of income source c15 (ep324d5) | `Numeric(Byte)` | `%29.0g` |
| `ep074_16` | Period of income source c16 (ep324d6) | `Numeric(Byte)` | `%29.0g` |
| `ep078e_1` | Typical payment of pension in c1 last year (ep071d1) | `Numeric(Double)` | `%11.0g` |
| `ep078e_2` | Typical payment of pension in c2 last year (ep071d2) | `Numeric(Double)` | `%11.0g` |
| `ep078e_3` | Typical payment of pension in c3 last year (ep071d3) | `Numeric(Double)` | `%11.0g` |
| `ep078e_4` | Typical payment of pension in c4 last year (ep071d4) | `Numeric(Double)` | `%11.0g` |
| `ep078e_5` | Typical payment of pension in c5 last year (ep071d5) | `Numeric(Double)` | `%11.0g` |
| `ep078e_6` | Typical payment of pension in c6 last year (ep071d6) | `Numeric(Double)` | `%11.0g` |
| `ep078e_7` | Typical payment of pension in c7 last year (ep071d7) | `Numeric(Double)` | `%11.0g` |
| `ep078e_8` | Typical payment of pension in c8 last year (ep071d8) | `Numeric(Double)` | `%11.0g` |
| `ep078e_9` | Typical payment of pension in c9 last year (ep071d9) | `Numeric(Double)` | `%11.0g` |
| `ep078e_10` | Typical payment of pension in c10 last year (ep071d10) | `Numeric(Double)` | `%11.0g` |
| `ep078e_11` | Typical payment of pension in c11 last year (ep324d1) | `Numeric(Double)` | `%11.0g` |
| `ep078e_12` | Typical payment of pension in c12 last year (ep324d2) | `Numeric(Double)` | `%11.0g` |
| `ep078e_13` | Typical payment of pension in c13 last year (ep324d3) | `Numeric(Double)` | `%11.0g` |
| `ep078e_14` | Typical payment of pension in c14 last year (ep324d4) | `Numeric(Double)` | `%11.0g` |
| `ep078e_15` | Typical payment of pension in c15 last year (ep324d5) | `Numeric(Double)` | `%11.0g` |
| `ep078e_16` | Typical payment of pension in c16 last year (ep324d6) | `Numeric(Double)` | `%11.0g` |
| `ep078ub_1` | Typical payment of pension in c1 last year ub (ep071d1) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_2` | Typical payment of pension in c2 last year ub (ep071d2) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_3` | Typical payment of pension in c3 last year ub (ep071d3) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_4` | Typical payment of pension in c4 last year ub (ep071d4) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_5` | Typical payment of pension in c5 last year ub (ep071d5) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_6` | Typical payment of pension in c6 last year ub (ep071d6) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_7` | Typical payment of pension in c7 last year ub (ep071d7) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_8` | Typical payment of pension in c8 last year ub (ep071d8) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_9` | Typical payment of pension in c9 last year ub (ep071d9) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_10` | Typical payment of pension in c10 last year ub (ep071d10) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_11` | Typical payment of pension in c11 last year ub (ep324d1) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_12` | Typical payment of pension in c12 last year ub (ep324d2) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_13` | Typical payment of pension in c13 last year ub (ep324d3) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_14` | Typical payment of pension in c14 last year ub (ep324d4) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_15` | Typical payment of pension in c15 last year ub (ep324d5) | `Numeric(Byte)` | `%32.0g` |
| `ep078ub_16` | Typical payment of pension in c16 last year ub (ep324d6) | `Numeric(Byte)` | `%32.0g` |
| `ep078v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `ep078v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `ep078v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `ep081_1` | Lump sum payment income source c1 (ep071d1) | `Numeric(Byte)` | `%11.0g` |
| `ep081_2` | Lump sum payment income source c2 (ep071d2) | `Numeric(Byte)` | `%11.0g` |
| `ep081_3` | Lump sum payment income source c3 (ep071d3) | `Numeric(Byte)` | `%11.0g` |
| `ep081_4` | Lump sum payment income source c4 (ep071d4) | `Numeric(Byte)` | `%11.0g` |
| `ep081_5` | Lump sum payment income source c5 (ep071d5) | `Numeric(Byte)` | `%11.0g` |
| `ep081_6` | Lump sum payment income source c6 (ep071d6) | `Numeric(Byte)` | `%11.0g` |
| `ep081_7` | Lump sum payment income source c7 (ep071d7) | `Numeric(Byte)` | `%11.0g` |
| `ep081_8` | Lump sum payment income source c8 (ep071d8) | `Numeric(Byte)` | `%11.0g` |
| `ep081_9` | Lump sum payment income source c9 (ep071d9) | `Numeric(Byte)` | `%11.0g` |
| `ep081_10` | Lump sum payment income source c10 (ep071d10) | `Numeric(Byte)` | `%11.0g` |
| `ep081_11` | Lump sum payment income source c11 (ep324d1) | `Numeric(Byte)` | `%11.0g` |
| `ep081_12` | Lump sum payment income source c12 (ep324d2) | `Numeric(Byte)` | `%11.0g` |
| `ep081_13` | Lump sum payment income source c13 (ep324d3) | `Numeric(Byte)` | `%11.0g` |
| `ep081_14` | Lump sum payment income source c14 (ep324d4) | `Numeric(Byte)` | `%11.0g` |
| `ep081_15` | Lump sum payment income source c15 (ep324d5) | `Numeric(Byte)` | `%11.0g` |
| `ep081_16` | Lump sum payment income source c16 (ep324d6) | `Numeric(Byte)` | `%11.0g` |
| `ep082e_1` | Total amount of lump sum payment income source c1 last year (ep071d1) | `Numeric(Double)` | `%11.0g` |
| `ep082e_2` | Total amount of lump sum payment income source c2 last year (ep071d2) | `Numeric(Double)` | `%11.0g` |
| `ep082e_3` | Total amount of lump sum payment income source c3 last year (ep071d3) | `Numeric(Double)` | `%11.0g` |
| `ep082e_4` | Total amount of lump sum payment income source c4 last year (ep071d4) | `Numeric(Double)` | `%11.0g` |
| `ep082e_5` | Total amount of lump sum payment income source c5 last year (ep071d5) | `Numeric(Double)` | `%11.0g` |
| `ep082e_6` | Total amount of lump sum payment income source c6 last year (ep071d6) | `Numeric(Double)` | `%11.0g` |
| `ep082e_7` | Total amount of lump sum payment income source c7 last year (ep071d7) | `Numeric(Double)` | `%11.0g` |
| `ep082e_8` | Total amount of lump sum payment income source c8 last year (ep071d8) | `Numeric(Double)` | `%11.0g` |
| `ep082e_9` | Total amount of lump sum payment income source c9 last year (ep071d9) | `Numeric(Double)` | `%11.0g` |
| `ep082e_10` | Total amount of lump sum payment income source c10 last year (ep071d10) | `Numeric(Double)` | `%11.0g` |
| `ep082e_11` | Total amount of lump sum payment income source c11 last year (ep324d1) | `Numeric(Double)` | `%11.0g` |
| `ep082e_12` | Total amount of lump sum payment income source c12 last year (ep324d2) | `Numeric(Double)` | `%11.0g` |
| `ep082e_13` | Total amount of lump sum payment income source c13 last year (ep324d3) | `Numeric(Double)` | `%11.0g` |
| `ep082e_14` | Total amount of lump sum payment income source c14 last year (ep324d4) | `Numeric(Double)` | `%11.0g` |
| `ep082e_15` | Total amount of lump sum payment income source c15 last year (ep324d5) | `Numeric(Double)` | `%11.0g` |
| `ep082e_16` | Total amount of lump sum payment income source c16 last year (ep324d6) | `Numeric(Double)` | `%11.0g` |
| `ep082ub_1` | Total amount of lump sum payment income source c1 ub  last year (ep071d1) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_2` | Total amount of lump sum payment income source c2 ub  last year (ep071d2) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_3` | Total amount of lump sum payment income source c3 ub  last year (ep071d3) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_4` | Total amount of lump sum payment income source c4 ub  last year (ep071d4) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_5` | Total amount of lump sum payment income source c5 ub  last year (ep071d5) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_6` | Total amount of lump sum payment income source c6 ub  last year (ep071d6) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_7` | Total amount of lump sum payment income source c7 ub  last year (ep071d7) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_8` | Total amount of lump sum payment income source c8 ub  last year (ep071d8) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_9` | Total amount of lump sum payment income source c9 ub  last year (ep071d9) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_10` | Total amount of lump sum payment income source c10 ub  last year (ep071d10) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_11` | Total amount of lump sum payment income source c11 last year ub (ep324d1) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_12` | Total amount of lump sum payment income source c12 last year ub (ep324d2) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_13` | Total amount of lump sum payment income source c13 last year ub (ep324d3) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_14` | Total amount of lump sum payment income source c14 last year ub (ep324d4) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_15` | Total amount of lump sum payment income source c15 last year ub (ep324d5) | `Numeric(Byte)` | `%32.0g` |
| `ep082ub_16` | Total amount of lump sum payment income source c16 last year ub (ep324d6) | `Numeric(Byte)` | `%32.0g` |
| `ep082v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `ep082v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `ep082v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `ep089d1` | Regular payments received: life insurance | `Numeric(Byte)` | `%12.0g` |
| `ep089d2` | Regular payments received: private annuity/private personal pension | `Numeric(Byte)` | `%12.0g` |
| `ep089d3` | Regular payments received: alimony | `Numeric(Byte)` | `%12.0g` |
| `ep089d4` | Regular payments received: from charities | `Numeric(Byte)` | `%12.0g` |
| `ep089d5` | Regular payments received: long-term care private insurance | `Numeric(Byte)` | `%12.0g` |
| `ep089dno` | Regular payments received: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep090_1` | Period received payment c1 | `Numeric(Byte)` | `%29.0g` |
| `ep090_2` | Period received payment c2 | `Numeric(Byte)` | `%29.0g` |
| `ep090_3` | Period received payment c3 | `Numeric(Byte)` | `%29.0g` |
| `ep090_4` | Period received payment c4 | `Numeric(Byte)` | `%29.0g` |
| `ep090_5` | Period received payment c5 | `Numeric(Byte)` | `%29.0g` |
| `ep092_1` | Additional payments for this benefit in last year, payment c1 | `Numeric(Byte)` | `%11.0g` |
| `ep092_2` | Additional payments for this benefit in last year, payment c2 | `Numeric(Byte)` | `%11.0g` |
| `ep092_3` | Additional payments for this benefit in last year, payment c3 | `Numeric(Byte)` | `%11.0g` |
| `ep092_4` | Additional payments for this benefit in last year, payment c4 | `Numeric(Byte)` | `%11.0g` |
| `ep092_5` | Additional payments for this benefit in last year, payment c5 | `Numeric(Byte)` | `%11.0g` |
| `ep094e_1` | Total amount payment c1 last year | `Numeric(Double)` | `%11.0g` |
| `ep094e_2` | Total amount payment c2 last year | `Numeric(Double)` | `%11.0g` |
| `ep094e_3` | Total amount payment c3 last year | `Numeric(Double)` | `%11.0g` |
| `ep094e_4` | Total amount payment c4 last year | `Numeric(Double)` | `%11.0g` |
| `ep094e_5` | Total amount payment c5 last year | `Numeric(Double)` | `%11.0g` |
| `ep094ub_1` | Total amount payment c1 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094ub_2` | Total amount payment c2 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094ub_3` | Total amount payment c3 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094ub_4` | Total amount payment c4 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094ub_5` | Total amount payment c5 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `ep094v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `ep094v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `ep096_1` | Months received payment c1 | `Numeric(Byte)` | `%11.0g` |
| `ep096_2` | Months received payment c2 | `Numeric(Byte)` | `%11.0g` |
| `ep096_3` | Months received payment c3 | `Numeric(Byte)` | `%11.0g` |
| `ep096_4` | Months received payment c4 | `Numeric(Byte)` | `%11.0g` |
| `ep096_5` | Months received payment c5 | `Numeric(Byte)` | `%11.0g` |
| `ep097_` | Pension claims | `Numeric(Byte)` | `%11.0g` |
| `ep098d1` | Type of pension entitled to: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ep098d2` | Type of pension entitled to: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ep098d3` | Type of pension entitled to: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ep098d4` | Type of pension entitled to: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ep098d5` | Type of pension entitled to: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ep098dno` | Type of pension entitled to: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep102_1` | Compulsory or voluntary participation in pension c1 | `Numeric(Byte)` | `%13.0g` |
| `ep102_2` | Compulsory or voluntary participation in pension c2 | `Numeric(Byte)` | `%13.0g` |
| `ep102_3` | Compulsory or voluntary participation in pension c3 | `Numeric(Byte)` | `%13.0g` |
| `ep102_4` | Compulsory or voluntary participation in pension c4 | `Numeric(Byte)` | `%13.0g` |
| `ep102_5` | Compulsory or voluntary participation in pension c5 | `Numeric(Byte)` | `%13.0g` |
| `ep103_1` | Years contributing to plan, pension c1 | `Numeric(Byte)` | `%11.0g` |
| `ep103_2` | Years contributing to plan, pension c2 | `Numeric(Byte)` | `%11.0g` |
| `ep103_3` | Years contributing to plan, pension c3 | `Numeric(Byte)` | `%11.0g` |
| `ep103_4` | Years contributing to plan, pension c4 | `Numeric(Int)` | `%11.0g` |
| `ep103_5` | Years contributing to plan, pension c5 | `Numeric(Byte)` | `%11.0g` |
| `ep106_1` | Expected age to collect pension c1 | `Numeric(Byte)` | `%11.0g` |
| `ep106_2` | Expected age to collect pension c2 | `Numeric(Byte)` | `%11.0g` |
| `ep106_3` | Expected age to collect pension c3 | `Numeric(Byte)` | `%11.0g` |
| `ep106_4` | Expected age to collect pension c4 | `Numeric(Byte)` | `%11.0g` |
| `ep106_5` | Expected age to collect pension c5 | `Numeric(Byte)` | `%11.0g` |
| `ep109_1` | Percentage of salary received as pension c1 | `Numeric(Int)` | `%11.0g` |
| `ep109_2` | Percentage of salary received as pension c2 | `Numeric(Int)` | `%11.0g` |
| `ep109_3` | Percentage of salary received as pension c3 | `Numeric(Int)` | `%11.0g` |
| `ep109_4` | Percentage of salary received as pension c4 | `Numeric(Int)` | `%11.0g` |
| `ep109_5` | Percentage of salary received as pension c5 | `Numeric(Byte)` | `%11.0g` |
| `ep110d1` | Received public benefits: old age pension | `Numeric(Byte)` | `%12.0g` |
| `ep110d2` | Received public benefits: early retirement pension | `Numeric(Byte)` | `%12.0g` |
| `ep110d3` | Received public benefits: unemployment benefits | `Numeric(Byte)` | `%12.0g` |
| `ep110d4` | Received public benefits: sickness benefits | `Numeric(Byte)` | `%12.0g` |
| `ep110d5` | Received public benefits: disability insurance | `Numeric(Byte)` | `%12.0g` |
| `ep110d6` | Received public benefits: social assistance | `Numeric(Byte)` | `%12.0g` |
| `ep110dno` | received public benefits: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep111_1_1` | Receive old age pension period 1 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_1_2` | Receive old age pension period 2 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_1_3` | Receive old age pension period 3 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_1_4` | Receive old age pension period 4 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_1_5` | Receive old age pension period 5 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_1_6` | Receive old age pension period 6 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_1_7` | Receive old age pension period 7 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_1_8` | Receive old age pension period 8 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_1_9` | Receive old age pension period 9 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_2_1` | Receive early retirement pension period 1 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_2_2` | Receive early retirement pension period 2 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_2_3` | Receive early retirement pension period 3 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_2_4` | Receive early retirement pension period 4 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_3_1` | Receive unemployment benefits period 1 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_3_2` | Receive unemployment benefits period 2 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_3_3` | Receive unemployment benefits period 3 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_3_4` | Receive unemployment benefits period 4 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_3_5` | Receive unemployment benefits period 5 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_4_1` | Receive sickness benefits period 1 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_4_2` | Receive sickness benefits period 2 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_4_3` | Receive sickness benefits period 3 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_4_4` | Receive sickness benefits period 4 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_4_5` | Receive sickness benefits period 5 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_4_6` | Receive sickness benefits period 6 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_1` | Receive disability insurance period 1 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_2` | Receive disability insurance period 2 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_3` | Receive disability insurance period 3 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_6_1` | Receive social assistance period 1 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_6_2` | Receive social assistance period 2 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_6_3` | Receive social assistance period 3 from month | `Numeric(Byte)` | `%10.0g` |
| `ep112_1_1` | Receive old age pension period 1 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_1_2` | Receive old age pension period 2 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_1_3` | Receive old age pension period 3 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_1_4` | Receive old age pension period 4 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_1_5` | Receive old age pension period 5 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_1_6` | Receive old age pension period 6 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_1_7` | Receive old age pension period 7 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_1_8` | Receive old age pension period 7 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_1_9` | Receive old age pension period 7 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_2_1` | Receive early retirement pension period 1 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_2_2` | Receive early retirement pension period 2 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_2_3` | Receive early retirement pension period 3 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_2_4` | Receive early retirement pension period 4 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_3_1` | Receive unemployment benefits period 1 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_3_2` | Receive unemployment benefits period 2 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_3_3` | Receive unemployment benefits period 3 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_3_4` | Receive unemployment benefits period 4 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_3_5` | Receive unemployment benefits period 5 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_4_1` | Receive sickness benefits period 1 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_4_2` | Receive sickness benefits period 2 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_4_3` | Receive sickness benefits period 3 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_4_4` | Receive sickness benefits period 4 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_4_5` | Receive sickness benefits period 5 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_4_6` | Receive sickness benefits period 6 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_1` | Receive disability insurance period 1 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_2` | Receive disability insurance period 2 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_3` | Receive disability insurance period 3 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_6_1` | Receive social assistance period 1 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_6_2` | Receive social assistance period 2 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_6_3` | Receive social assistance period 2 from year | `Numeric(Byte)` | `%15.0g` |
| `ep113_1_1` | Receive old age pension period 1 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_1_2` | Receive old age pension period 2 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_1_3` | Receive old age pension period 3 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_1_4` | Receive old age pension period 4 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_1_5` | Receive old age pension period 5 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_1_6` | Receive old age pension period 6 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_1_7` | Receive old age pension period 7 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_1_8` | Receive old age pension period 8 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_1_9` | Receive old age pension period 9 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_2_1` | Receive early retirement pension period 1 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_2_2` | Receive early retirement pension period 2 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_2_3` | Receive early retirement pension period 3 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_2_4` | Receive early retirement pension period 4 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_3_1` | Receive unemployment benefits period 1 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_3_2` | Receive unemployment benefits period 2 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_3_3` | Receive unemployment benefits period 3 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_3_4` | Receive unemployment benefits period 4 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_3_5` | Receive unemployment benefits period 5 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_4_1` | Receive sickness benefits period 1 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_4_2` | Receive sickness benefits period 2 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_4_3` | Receive sickness benefits period 3 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_4_4` | Receive sickness benefits period 4 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_4_5` | Receive sickness benefits period 5 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_4_6` | Receive sickness benefits period 6 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_1` | Receive disability insurance period 1 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_2` | Receive disability insurance period 2 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_3` | Receive disability insurance period 3 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_6_1` | Receive social assistance period 1 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_6_2` | Receive social assistance period 2 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_6_3` | Receive social assistance period 3 to month | `Numeric(Byte)` | `%10.0g` |
| `ep114_1_1` | Receive old age pension period 1 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_1_2` | Receive old age pension period 2 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_1_3` | Receive old age pension period 3 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_1_4` | Receive old age pension period 4 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_1_5` | Receive old age pension period 5 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_1_6` | Receive old age pension period 6 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_1_7` | Receive old age pension period 7 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_1_8` | Receive old age pension period 8 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_1_9` | Receive old age pension period 9 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_2_1` | Receive early retirement pension period 1 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_2_2` | Receive early retirement pension period 2 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_2_3` | Receive early retirement pension period 3 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_2_4` | Receive early retirement pension period 4 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_3_1` | Receive unemployment benefits period 1 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_3_2` | Receive unemployment benefits period 2 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_3_3` | Receive unemployment benefits period 3 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_3_4` | Receive unemployment benefits period 4 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_3_5` | Receive unemployment benefits period 5 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_4_1` | Receive sickness benefits period 1 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_4_2` | Receive sickness benefits period 2 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_4_3` | Receive sickness benefits period 3 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_4_4` | Receive sickness benefits period 4 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_4_5` | Receive sickness benefits period 5 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_4_6` | Receive sickness benefits period 6 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_5_1` | Receive disability insurance period 1 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_5_2` | Receive disability insurance period 2 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_5_3` | Receive disability insurance period 3 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_6_1` | Receive social assistance period 1 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_6_2` | Receive social assistance period 2 to year | `Numeric(Byte)` | `%15.0g` |
| `ep114_6_3` | Receive social assistance period 3 to year | `Numeric(Byte)` | `%15.0g` |
| `ep116_1_1` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_2` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_3` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_4` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_5` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_6` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_7` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_8` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_9` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_2_1` | Receive early retirement pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_2_2` | Receive early retirement pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_2_3` | Receive early retirement pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_2_4` | Receive early retirement pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_3_1` | Receive unemployment benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_3_2` | Receive unemployment benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_3_3` | Receive unemployment benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_3_4` | Receive unemployment benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_3_5` | Receive unemployment benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_4_1` | Receive sickness benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_4_2` | Receive sickness benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_4_3` | Receive sickness benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_4_4` | Receive sickness benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_4_5` | Receive sickness benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_4_6` | Receive sickness benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_1` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_2` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_3` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_6_1` | Receive social assistance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_6_2` | Receive social assistance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_6_3` | Receive social assistance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep122_` | Receive severance month | `Numeric(Byte)` | `%11.0g` |
| `ep123_` | Receive severance year | `Numeric(Byte)` | `%17.0g` |
| `ep125_` | Continuously working | `Numeric(Byte)` | `%11.0g` |
| `ep127_1` | Period from month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep127_2` | Period from month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep127_3` | Period from month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep127_4` | Period from month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep127_5` | Period from month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep127_6` | Period from month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep127_7` | Period from month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep127_8` | Period from month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep127_21` | Period from month (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep127_22` | Period from month (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep127_23` | Period from month (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep127_24` | Period from month (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep127_25` | Period from month (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep127_26` | Period from month (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep128_1` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_2` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_3` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_4` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_5` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_6` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_7` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_8` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_21` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_22` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_23` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_24` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_25` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_26` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep129_1` | Period to month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep129_2` | Period to month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep129_3` | Period to month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep129_4` | Period to month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep129_5` | Period to month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep129_6` | Period to month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep129_7` | Period to month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep129_8` | Period to month (working) | `Numeric(Byte)` | `%11.0g` |
| `ep129_21` | Period to month (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep129_22` | Period to month (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep129_23` | Period to month (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep129_24` | Period to month (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep129_25` | Period to month (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep129_26` | Period to month (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep130_1` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_2` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_3` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_4` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_5` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_6` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_7` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_8` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_21` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_22` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_23` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_24` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_25` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_26` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep133_1` | Other periods (working) | `Numeric(Byte)` | `%11.0g` |
| `ep133_2` | Other periods (working) | `Numeric(Byte)` | `%11.0g` |
| `ep133_3` | Other periods (working) | `Numeric(Byte)` | `%11.0g` |
| `ep133_4` | Other periods (working) | `Numeric(Byte)` | `%11.0g` |
| `ep133_5` | Other periods (working) | `Numeric(Byte)` | `%11.0g` |
| `ep133_6` | Other periods (working) | `Numeric(Byte)` | `%11.0g` |
| `ep133_7` | Other periods (working) | `Numeric(Byte)` | `%11.0g` |
| `ep133_8` | Other periods (working) | `Numeric(Byte)` | `%11.0g` |
| `ep133_21` | Other periods (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep133_22` | Other periods (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep133_23` | Other periods (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep133_24` | Other periods (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep133_25` | Other periods (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep133_26` | Other periods (unemployed) | `Numeric(Byte)` | `%11.0g` |
| `ep141d1` | Change in job: type of employment | `Numeric(Byte)` | `%12.0g` |
| `ep141d2` | Change in job: employer | `Numeric(Byte)` | `%12.0g` |
| `ep141d3` | Change in job: promotion | `Numeric(Byte)` | `%12.0g` |
| `ep141d4` | Change in job: job location | `Numeric(Byte)` | `%12.0g` |
| `ep141d5` | Change in job: contract length | `Numeric(Byte)` | `%12.0g` |
| `ep141dno` | Change in job: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep204_` | Any earnings from employment previous year | `Numeric(Byte)` | `%11.0g` |
| `ep205e` | Earnings employment per year after taxes | `Numeric(Double)` | `%11.0g` |
| `ep205ub` | Earnings employment per year after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep205v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `ep205v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `ep205v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `ep206_` | Income from self-employment previous year | `Numeric(Byte)` | `%11.0g` |
| `ep207e` | Earnings self-employment per year after taxes | `Numeric(Double)` | `%11.0g` |
| `ep207ub` | Earnings self-employment per year after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep207v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `ep207v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `ep207v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `ep208_1` | How many months received income source c1 (ep071d1) | `Numeric(Byte)` | `%11.0g` |
| `ep208_2` | How many months received income source c2 (ep071d2) | `Numeric(Byte)` | `%11.0g` |
| `ep208_3` | How many months received income source c3 (ep071d3) | `Numeric(Byte)` | `%11.0g` |
| `ep208_4` | How many months received income source c4 (ep071d4) | `Numeric(Byte)` | `%11.0g` |
| `ep208_5` | How many months received income source c5 (ep071d5) | `Numeric(Byte)` | `%11.0g` |
| `ep208_6` | How many months received income source c6 (ep071d6) | `Numeric(Byte)` | `%11.0g` |
| `ep208_7` | How many months received income source c7 (ep071d7) | `Numeric(Byte)` | `%11.0g` |
| `ep208_8` | How many months received income source c8 (ep071d8) | `Numeric(Byte)` | `%11.0g` |
| `ep208_9` | How many months received income source c9 (ep071d9) | `Numeric(Byte)` | `%11.0g` |
| `ep208_10` | How many months received income source c10 (ep071d10) | `Numeric(Byte)` | `%11.0g` |
| `ep208_11` | How many months received income source c11 (ep324d1) | `Numeric(Byte)` | `%11.0g` |
| `ep208_12` | How many months received income source c12 (ep324d2) | `Numeric(Byte)` | `%11.0g` |
| `ep208_13` | How many months received income source c13 (ep324d3) | `Numeric(Byte)` | `%11.0g` |
| `ep208_14` | How many months received income source c14 (ep324d4) | `Numeric(Byte)` | `%11.0g` |
| `ep208_15` | How many months received income source c15 (ep324d5) | `Numeric(Byte)` | `%11.0g` |
| `ep208_16` | How many months received income source c16 (ep324d6) | `Numeric(Byte)` | `%11.0g` |
| `ep209e_1` | Additional payments c1 after taxes | `Numeric(Double)` | `%11.0g` |
| `ep209e_2` | Additional payments c2 after taxes | `Numeric(Double)` | `%11.0g` |
| `ep209e_3` | Additional payments c3 after taxes | `Numeric(Double)` | `%11.0g` |
| `ep209e_4` | Additional payments c4 after taxes | `Numeric(Double)` | `%11.0g` |
| `ep209e_5` | Additional payments c5 after taxes | `Numeric(Int)` | `%11.0g` |
| `ep209ub_1` | Additional payments c1 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209ub_2` | Additional payments c2 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209ub_3` | Additional payments c3 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209ub_4` | Additional payments c4 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209ub_5` | Additional payments c5 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209v1` | Bracket value 1 | `Numeric(Float)` | `%11.0g` |
| `ep209v2` | Bracket value 2 | `Numeric(Float)` | `%11.0g` |
| `ep209v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `ep210_` | Who answered section ep | `Numeric(Byte)` | `%44.0g` |
| `ep213_1` | First year received income source c1 (ep071d1) | `Numeric(Int)` | `%11.0g` |
| `ep213_2` | First year received income source c2 (ep071d2) | `Numeric(Int)` | `%11.0g` |
| `ep213_3` | First year received income source c3 (ep071d3) | `Numeric(Int)` | `%11.0g` |
| `ep213_4` | First year received income source c4 (ep071d4) | `Numeric(Int)` | `%11.0g` |
| `ep213_5` | First year received income source c5 (ep071d5) | `Numeric(Int)` | `%11.0g` |
| `ep213_6` | First year received income source c6 (ep071d6) | `Numeric(Int)` | `%11.0g` |
| `ep213_7` | First year received income source c7 (ep071d7) | `Numeric(Int)` | `%11.0g` |
| `ep213_8` | First year received income source c8 (ep071d8) | `Numeric(Int)` | `%11.0g` |
| `ep213_9` | First year received income source c9 (ep071d9) | `Numeric(Int)` | `%11.0g` |
| `ep213_10` | First year received income source c10 (ep071d10) | `Numeric(Int)` | `%11.0g` |
| `ep213_11` | First year received income source c11 (ep324d1) | `Numeric(Int)` | `%11.0g` |
| `ep213_12` | First year received income source c12 (ep324d2) | `Numeric(Int)` | `%11.0g` |
| `ep213_13` | First year received income source c13 (ep324d3) | `Numeric(Int)` | `%11.0g` |
| `ep213_14` | First year received income source c14 (ep324d4) | `Numeric(Int)` | `%11.0g` |
| `ep213_15` | First year received income source c15 (ep324d5) | `Numeric(Int)` | `%11.0g` |
| `ep213_16` | First year received income source c16 (ep324d6) | `Numeric(Int)` | `%11.0g` |
| `ep301_` | Missed days from work the last 12 months | `Numeric(Byte)` | `%11.0g` |
| `ep302_` | How many days missed from work | `Numeric(Int)` | `%11.0g` |
| `ep321_` | Total hours worked per week second job | `Numeric(Double)` | `%11.0g` |
| `ep322_` | Months per year worked in second job (number) | `Numeric(Byte)` | `%11.0g` |
| `ep324d1` | Occupational pension income: old age pension last job | `Numeric(Byte)` | `%12.0g` |
| `ep324d2` | Occupational pension income: old age pension second job | `Numeric(Byte)` | `%12.0g` |
| `ep324d3` | Occupational pension income: old age pension third job | `Numeric(Byte)` | `%12.0g` |
| `ep324d4` | Occupational pension income: early retirement | `Numeric(Byte)` | `%12.0g` |
| `ep324d5` | Occupational pension income: disability/invalidity insurance | `Numeric(Byte)` | `%12.0g` |
| `ep324d6` | Occupational pension income: survivor pension from spouse/partner's job | `Numeric(Byte)` | `%12.0g` |
| `ep324dno` | Occupational pension income: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep325_` | Unemployed since last interview | `Numeric(Byte)` | `%11.0g` |
| `ep326_` | Received severance payment since last interview | `Numeric(Byte)` | `%11.0g` |
| `ep328_` | Retirement month | `Numeric(Byte)` | `%11.0g` |
| `ep329_` | Retirement year | `Numeric(Int)` | `%11.0g` |
| `ep337_` | Currently looking for job | `Numeric(Byte)` | `%11.0g` |

### `ex` - Expectations

- Dataset: `sharew4_rel9-0-0_ex.dta`
- Read with: `ps.read_share_module("ex", wave=4)`
- Rows: 57,982
- Variables: 25
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ex001_` | Introduction and example | `Numeric(Byte)` | `%11.0g` |
| `ex002_` | Chance of receiving inheritance | `Numeric(Byte)` | `%11.0g` |
| `ex003_` | Chance inheritance more than 50000 | `Numeric(Byte)` | `%11.0g` |
| `ex007_` | Chance government reduces pension | `Numeric(Byte)` | `%11.0g` |
| `ex025_` | Chance to work after age of 63 | `Numeric(Byte)` | `%11.0g` |
| `ex008_` | Chance government raises retirement age | `Numeric(Byte)` | `%11.0g` |
| `ex009_` | Life expectancy | `Numeric(Byte)` | `%11.0g` |
| `ex009age` | Life expectancy target age | `Numeric(Int)` | `%10.0g` |
| `ex026_` | Trust in other people | `Numeric(Byte)` | `%11.0g` |
| `ex110_` | Risk aversion | `Numeric(Byte)` | `%74.0g` |
| `ex028_` | Left or right in politics | `Numeric(Byte)` | `%11.0g` |
| `ex029_` | Frequency of praying | `Numeric(Byte)` | `%31.0g` |
| `ex109_` | Use world wide web | `Numeric(Byte)` | `%11.0g` |
| `ex023_` | End non proxy | `Numeric(Byte)` | `%47.0g` |
| `ex100_` | Partner available and willing to participate | `Numeric(Byte)` | `%62.0g` |
| `ex102_` | Partner years of education | `Numeric(Byte)` | `%11.0g` |
| `ex103_` | Partner current job situation | `Numeric(Byte)` | `%65.0g` |
| `ex104_` | Partner ever done paid work | `Numeric(Byte)` | `%11.0g` |
| `ex105_` | Partner employee or a self-employed | `Numeric(Byte)` | `%36.0g` |

### `ft` - Financial Transfers

- Dataset: `sharew4_rel9-0-0_ft.dta`
- Read with: `ps.read_share_module("ft", wave=4)`
- Rows: 57,982
- Variables: 53
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ft002_` | Given financial gift 250 or more | `Numeric(Byte)` | `%11.0g` |
| `ft003_1ft` | To whom given gift, person 1 | `Numeric(Int)` | `%39.0g` |
| `ft003_2ft` | To whom given gift, person 2 | `Numeric(Int)` | `%39.0g` |
| `ft003_3ft` | To whom given gift, person 3 | `Numeric(Int)` | `%39.0g` |
| `ft007_1` | Other persons given financial gift 250 or more | `Numeric(Byte)` | `%11.0g` |
| `ft007_2` | Other persons given financial gift 250 or more | `Numeric(Byte)` | `%11.0g` |
| `ft007_3` | Other persons given financial gift 250 or more | `Numeric(Byte)` | `%11.0g` |
| `ft009_` | Received financial gift of 250 or more | `Numeric(Byte)` | `%11.0g` |
| `ft010_1ft` | From whom recieved gift, person 1 | `Numeric(Int)` | `%39.0g` |
| `ft010_2ft` | From whom recieved gift, person 2 | `Numeric(Int)` | `%39.0g` |
| `ft010_3ft` | From whom recieved gift, person 3 | `Numeric(Int)` | `%39.0g` |
| `ft014_1` | From other persons received financial gift 250 or more | `Numeric(Byte)` | `%11.0g` |
| `ft014_2` | From other persons received financial gift 250 or more | `Numeric(Byte)` | `%11.0g` |
| `ft014_3` | From other persons received financial gift 250 or more | `Numeric(Byte)` | `%11.0g` |
| `ft015_` | Ever received gift or inheritance (worth 5000 euros or more) | `Numeric(Byte)` | `%11.0g` |
| `ft016_1` | Year, inheritance or large gift 1 received | `Numeric(Int)` | `%11.0g` |
| `ft016_2` | Year, inheritance or large gift 2 received | `Numeric(Int)` | `%11.0g` |
| `ft016_3` | Year, inheritance or large gift 3 received | `Numeric(Int)` | `%11.0g` |
| `ft016_4` | Year, inheritance or large gift 4 received | `Numeric(Int)` | `%11.0g` |
| `ft016_5` | Year, inheritance or large gift 5 received | `Numeric(Int)` | `%11.0g` |
| `ft017_1ft` | From whom inheritance or large gift 1 | `Numeric(Int)` | `%39.0g` |
| `ft017_2ft` | From whom inheritance or large gift 2 | `Numeric(Int)` | `%39.0g` |
| `ft017_3ft` | From whom inheritance or large gift 3 | `Numeric(Int)` | `%39.0g` |
| `ft017_4ft` | From whom inheritance or large gift 4 | `Numeric(Int)` | `%39.0g` |
| `ft017_5ft` | From whom inheritance or large gift 5 | `Numeric(Int)` | `%39.0g` |
| `ft020_1` | Any further gift or inheritance | `Numeric(Byte)` | `%11.0g` |
| `ft020_2` | Any further gift or inheritance | `Numeric(Byte)` | `%11.0g` |
| `ft020_3` | Any further gift or inheritance | `Numeric(Byte)` | `%11.0g` |
| `ft020_4` | Any further gift or inheritance | `Numeric(Byte)` | `%11.0g` |
| `ft020_5` | Any further gift or inheritance | `Numeric(Byte)` | `%11.0g` |
| `ft021_` | Who answered the questions in ft | `Numeric(Byte)` | `%44.0g` |
| `ft025_` | Ever given gift 5000 or more | `Numeric(Byte)` | `%11.0g` |
| `ft026_1` | In which year given gift | `Numeric(Int)` | `%11.0g` |
| `ft026_2` | In which year given gift | `Numeric(Int)` | `%11.0g` |
| `ft026_3` | In which year given gift | `Numeric(Int)` | `%11.0g` |
| `ft026_4` | In which year given gift | `Numeric(Int)` | `%11.0g` |
| `ft026_5` | In which year given gift | `Numeric(Int)` | `%11.0g` |
| `ft027_1ft` | To whom given 5000 or more | `Numeric(Int)` | `%39.0g` |
| `ft027_2ft` | To whom given 5000 or more | `Numeric(Int)` | `%39.0g` |
| `ft027_3ft` | To whom given 5000 or more | `Numeric(Int)` | `%39.0g` |
| `ft027_4ft` | To whom given 5000 or more | `Numeric(Int)` | `%39.0g` |
| `ft027_5ft` | To whom given 5000 or more | `Numeric(Int)` | `%39.0g` |
| `ft031_1` | Any further gift | `Numeric(Byte)` | `%11.0g` |
| `ft031_2` | Any further gift | `Numeric(Byte)` | `%11.0g` |
| `ft031_3` | Any further gift | `Numeric(Byte)` | `%11.0g` |
| `ft031_4` | Any further gift | `Numeric(Byte)` | `%11.0g` |
| `ft031_5` | Any further gift | `Numeric(Byte)` | `%11.0g` |

### `gs` - Grip Strength

- Dataset: `sharew4_rel9-0-0_gs.dta`
- Read with: `ps.read_share_module("gs", wave=4)`
- Rows: 57,982
- Variables: 23
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `gs001_` | Willing to have handgrip measured | `Numeric(Byte)` | `%58.0g` |
| `gs002_` | Record respondent status | `Numeric(Byte)` | `%51.0g` |
| `gs004_` | Dominant hand | `Numeric(Byte)` | `%13.0g` |
| `gs006_` | 1st measurement: left hand | `Numeric(Byte)` | `%11.0g` |
| `gs007_` | 2nd measurement: left hand | `Numeric(Byte)` | `%11.0g` |
| `gs008_` | 1st measurement: right hand | `Numeric(Byte)` | `%11.0g` |
| `gs009_` | 2nd measurement: right hand | `Numeric(Byte)` | `%11.0g` |
| `gs010d1` | Why not completed gs test: r felt it would not be safe | `Numeric(Byte)` | `%12.0g` |
| `gs010d2` | Why not completed gs test: iwer felt it would not be safe | `Numeric(Byte)` | `%12.0g` |
| `gs010d3` | Why not completed gs test: r refused, no reason given | `Numeric(Byte)` | `%12.0g` |
| `gs010d4` | Why not completed gs test: r tried but was unable to complete test | `Numeric(Byte)` | `%12.0g` |
| `gs010d5` | Why not completed gs test: r did not understand the instructions | `Numeric(Byte)` | `%12.0g` |
| `gs010d6` | Why not completed gs test: r had surgery, injury, swelling, etc. | `Numeric(Byte)` | `%12.0g` |
| `gs010dot` | Why not completed gs test: others | `Numeric(Byte)` | `%12.0g` |
| `gs012_` | How much effort gave r | `Numeric(Byte)` | `%90.0g` |
| `gs013_` | The position of r for this test | `Numeric(Byte)` | `%11.0g` |
| `gs014_` | R rested his/her arms on a support | `Numeric(Byte)` | `%11.0g` |

### `hc` - Health Care

- Dataset: `sharew4_rel9-0-0_hc.dta`
- Read with: `ps.read_share_module("hc", wave=4)`
- Rows: 57,982
- Variables: 29
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `hc002_` | How often seen or talked to medical doctor last 12 months | `Numeric(Byte)` | `%11.0g` |
| `hc003_` | How many of these contacts with general practitioner | `Numeric(Byte)` | `%11.0g` |
| `hc004_` | Contacts with specialists | `Numeric(Byte)` | `%11.0g` |
| `hc005d1` | Consultation: specialist for heart disease, pulmonary, gastroenterology, diabete | `Numeric(Byte)` | `%12.0g` |
| `hc005d2` | Consultation: dermatologist | `Numeric(Byte)` | `%12.0g` |
| `hc005d3` | Consultation: neurologist | `Numeric(Byte)` | `%12.0g` |
| `hc005d4` | Consultation: opthalmologist | `Numeric(Byte)` | `%12.0g` |
| `hc005d5` | Consultation: ear, nose and throat specialist | `Numeric(Byte)` | `%12.0g` |
| `hc005d6` | Consultation: rheumatologist or physiatrist | `Numeric(Byte)` | `%12.0g` |
| `hc005d7` | Consultation: orthopaedist | `Numeric(Byte)` | `%12.0g` |
| `hc005d8` | Consultation: surgeon | `Numeric(Byte)` | `%12.0g` |
| `hc005d9` | Consultation: psychiatrist | `Numeric(Byte)` | `%12.0g` |
| `hc005d10` | Consultation: gynaecologist | `Numeric(Byte)` | `%12.0g` |
| `hc005d11` | Consultation: urologist | `Numeric(Byte)` | `%12.0g` |
| `hc005d12` | Consultation: oncologist | `Numeric(Byte)` | `%12.0g` |
| `hc005d13` | Consultation: geriatrician | `Numeric(Byte)` | `%12.0g` |
| `hc005dot` | Consultation: other | `Numeric(Byte)` | `%12.0g` |
| `hc012_` | Stayed over night in hospital last 12 months | `Numeric(Byte)` | `%11.0g` |
| `hc013_` | Times being patient in hospital | `Numeric(Byte)` | `%11.0g` |
| `hc014_` | Total nights stayed in hospital | `Numeric(Int)` | `%11.0g` |
| `hc029_` | In a nursing home during last 12 months | `Numeric(Byte)` | `%16.0g` |
| `hc030_` | Times stayed in a nursing home overnight | `Numeric(Int)` | `%11.0g` |
| `hc031_` | Weeks stayed in a nursing home | `Numeric(Byte)` | `%11.0g` |

### `hh` - Household Income

- Dataset: `sharew4_rel9-0-0_hh.dta`
- Read with: `ps.read_share_module("hh", wave=4)`
- Rows: 57,982
- Variables: 25
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `hh001_` | Other contributor to household income | `Numeric(Byte)` | `%11.0g` |
| `hh002e` | Total income (other) household members last year | `Numeric(Double)` | `%11.0g` |
| `hh002ub` | Total income (other) household members last year ub | `Numeric(Byte)` | `%32.0g` |
| `hh002v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `hh002v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `hh002v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `hh010_` | Income from other sources | `Numeric(Byte)` | `%11.0g` |
| `hh011e` | Additional income received by all hh-members last year | `Numeric(Double)` | `%11.0g` |
| `hh011ub` | Additional income received by all hh-members last year ub | `Numeric(Byte)` | `%32.0g` |
| `hh011v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `hh011v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `hh011v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `hh014_` | Who answered the question in hh | `Numeric(Byte)` | `%44.0g` |
| `hh017e` | Total income received by all hh members an average month last year | `Numeric(Double)` | `%11.0g` |
| `hh017ub` | Total income received by all hh-members an average month last year ub | `Numeric(Byte)` | `%32.0g` |
| `hh017v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `hh017v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `hh017v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |

### `ho` - Housing

- Dataset: `sharew4_rel9-0-0_ho.dta`
- Read with: `ps.read_share_module("ho", wave=4)`
- Rows: 57,982
- Variables: 88
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `ho001_` | Interview in house of respondent | `Numeric(Byte)` | `%11.0g` |
| `ho002_` | Owner, tenant or rent free | `Numeric(Byte)` | `%36.0g` |
| `ho003_` | Rent payment period | `Numeric(Byte)` | `%22.0g` |
| `ho005e` | Amount last rent payment | `Numeric(Double)` | `%11.0g` |
| `ho005ub` | Amount last rent payment ub | `Numeric(Byte)` | `%32.0g` |
| `ho005v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `ho005v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `ho005v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `ho007_` | Last rent payment included all charges and services | `Numeric(Byte)` | `%11.0g` |
| `ho008e` | Amount charges and services | `Numeric(Double)` | `%11.0g` |
| `ho008ub` | Amount charges and services ub | `Numeric(Byte)` | `%32.0g` |
| `ho008v1` | Bracket value 1 | `Numeric(Float)` | `%11.0g` |
| `ho008v2` | Bracket value 2 | `Numeric(Float)` | `%11.0g` |
| `ho008v3` | Bracket value 3 | `Numeric(Float)` | `%11.0g` |
| `ho010_` | More than two months behind with rent | `Numeric(Byte)` | `%11.0g` |
| `ho011_` | How property acquired | `Numeric(Byte)` | `%55.0g` |
| `ho012_` | Year acquired property | `Numeric(Int)` | `%11.0g` |
| `ho013_` | Mortgages or loans on property | `Numeric(Byte)` | `%11.0g` |
| `ho014_` | Years left of mortgage or loan | `Numeric(Byte)` | `%11.0g` |
| `ho015e` | Amount still to pay on mortgage or loan | `Numeric(Double)` | `%11.0g` |
| `ho015ub` | Amount still to pay on mortgage or loan ub | `Numeric(Byte)` | `%32.0g` |
| `ho015v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `ho015v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `ho015v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `ho017_` | Regularly repay mortgage or loans | `Numeric(Byte)` | `%11.0g` |
| `ho020e` | Amount regular repayments on mortgage or loan | `Numeric(Double)` | `%11.0g` |
| `ho020ub` | Amount regular repayments on mortgage or loan ub | `Numeric(Byte)` | `%32.0g` |
| `ho020v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `ho020v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `ho020v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `ho022_` | Behind with regular repay mortgage or loan | `Numeric(Byte)` | `%11.0g` |
| `ho023_` | Sublet or let parts of accommodation | `Numeric(Byte)` | `%11.0g` |
| `ho024e` | Value of property | `Numeric(Double)` | `%11.0g` |
| `ho024ub` | Value of property ub | `Numeric(Byte)` | `%32.0g` |
| `ho024v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `ho024v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `ho024v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `ho026_` | Own other real estate | `Numeric(Byte)` | `%11.0g` |
| `ho027e` | Value of other real estate | `Numeric(Double)` | `%11.0g` |
| `ho027ub` | Value of other real estate ub | `Numeric(Byte)` | `%32.0g` |
| `ho027v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `ho027v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `ho027v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `ho029_` | Received income or rent of other real estate | `Numeric(Byte)` | `%11.0g` |
| `ho030e` | Amount income or rent of other real estate last year | `Numeric(Double)` | `%11.0g` |
| `ho030ub` | Amount income or rent of other real estate last year ub | `Numeric(Byte)` | `%32.0g` |
| `ho030v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `ho030v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `ho030v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `ho032_` | Number of rooms in accommodation | `Numeric(Byte)` | `%11.0g` |
| `ho033_` | Special features in accommodation | `Numeric(Byte)` | `%11.0g` |
| `ho034_` | Years in accommodation | `Numeric(Int)` | `%11.0g` |
| `ho036_` | Type of building | `Numeric(Byte)` | `%61.0g` |
| `ho041_` | Who answered the questions in ho | `Numeric(Byte)` | `%44.0g` |
| `ho042_` | Number of floors of building | `Numeric(Byte)` | `%11.0g` |
| `ho043_` | Number of steps to entrance | `Numeric(Byte)` | `%12.0g` |
| `ho044_` | Changed place of residence | `Numeric(Byte)` | `%11.0g` |
| `ho045_` | Main reason move | `Numeric(Byte)` | `%62.0g` |
| `ho054_` | Elevator | `Numeric(Byte)` | `%11.0g` |
| `ho060_` | Partner years in accomodation | `Numeric(Int)` | `%11.0g` |
| `ho061_` | Years in accommodation | `Numeric(Byte)` | `%11.0g` |
| `ho062_` | Out of pocket for nursing home | `Numeric(Byte)` | `%11.0g` |
| `ho063_` | Rent payment period | `Numeric(Byte)` | `%22.0g` |
| `ho065e` | Amount last payment | `Numeric(Double)` | `%11.0g` |
| `ho066d1` | Payment covering nursing home: lodging (room) | `Numeric(Byte)` | `%12.0g` |
| `ho066d2` | Payment covering nursing home: meals | `Numeric(Byte)` | `%12.0g` |
| `ho066d3` | Payment covering nursing home: nursing and care services | `Numeric(Byte)` | `%12.0g` |
| `ho066d4` | Payment covering nursing home: rehabilitation and other health services | `Numeric(Byte)` | `%12.0g` |
| `ho067e` | Amount similar dwelling todays market | `Numeric(Double)` | `%11.0g` |
| `ho067ub` | Amount similar dwelling todays market ub | `Numeric(Byte)` | `%32.0g` |
| `ho067v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `ho067v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `ho067v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `ho068_` | Amount rent at market price | `Numeric(Byte)` | `%29.0g` |
| `ho069e` | Payment similar dwelling | `Numeric(Double)` | `%11.0g` |
| `ho069ub` | Payment similar dwelling ub | `Numeric(Byte)` | `%32.0g` |
| `ho069v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `ho069v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `ho069v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `ho070_` | Percentage of house owned | `Numeric(Byte)` | `%11.0g` |
| `ho074e` | Income from sublet of accomodation | `Numeric(Double)` | `%11.0g` |

### `iv` - Interviewer Observations

- Dataset: `sharew4_rel9-0-0_iv.dta`
- Read with: `ps.read_share_module("iv", wave=4)`
- Rows: 57,982
- Variables: 27
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
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
| `iv004_` | Willingness to answer | `Numeric(Byte)` | `%58.0g` |
| `iv005d1` | Why willingness worse: respondent was losing interest | `Numeric(Byte)` | `%12.0g` |
| `iv005d2` | Why willingness worse: respondent was losing concentration | `Numeric(Byte)` | `%12.0g` |
| `iv005d3` | Why willingness worse: other | `Numeric(Byte)` | `%12.0g` |
| `iv007_` | Respondent asked for clarification | `Numeric(Byte)` | `%12.0g` |
| `iv008_` | Respondent understood questions | `Numeric(Byte)` | `%12.0g` |
| `iv009_` | Which area building located | `Numeric(Byte)` | `%38.0g` |
| `iv010_` | Type of building | `Numeric(Byte)` | `%61.0g` |
| `iv011_` | Number of floors of building | `Numeric(Byte)` | `%11.0g` |
| `iv012_` | Number of steps to entrance | `Numeric(Byte)` | `%12.0g` |
| `iv018_` | Help needed reading showcards | `Numeric(Byte)` | `%30.0g` |
| `iv020_` | Relationship proxy | `Numeric(Byte)` | `%37.0g` |

### `mh` - Mental Health

- Dataset: `sharew4_rel9-0-0_mh.dta`
- Read with: `ps.read_share_module("mh", wave=4)`
- Rows: 57,982
- Variables: 35
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `mh002_` | Sad or depressed last month | `Numeric(Byte)` | `%11.0g` |
| `mh003_` | Hopes for the future | `Numeric(Byte)` | `%27.0g` |
| `mh004_` | Suicidal feelings or wish to be dead | `Numeric(Byte)` | `%61.0g` |
| `mh005_` | Feels guilty | `Numeric(Byte)` | `%64.0g` |
| `mh006_` | Blame for what | `Numeric(Byte)` | `%62.0g` |
| `mh007_` | Trouble sleeping | `Numeric(Byte)` | `%62.0g` |
| `mh008_` | Less or same interest in things | `Numeric(Byte)` | `%46.0g` |
| `mh009_` | Keeps up interest | `Numeric(Byte)` | `%11.0g` |
| `mh010_` | Irritability | `Numeric(Byte)` | `%11.0g` |
| `mh011_` | Appetite | `Numeric(Byte)` | `%46.0g` |
| `mh012_` | Eating more or less | `Numeric(Byte)` | `%21.0g` |
| `mh013_` | Fatigue | `Numeric(Byte)` | `%11.0g` |
| `mh014_` | Concentration on entertainment | `Numeric(Byte)` | `%60.0g` |
| `mh015_` | Concentration on reading | `Numeric(Byte)` | `%48.0g` |
| `mh016_` | Enjoyment | `Numeric(Byte)` | `%62.0g` |
| `mh017_` | Tearfulness | `Numeric(Byte)` | `%11.0g` |
| `mh018_` | Depression ever | `Numeric(Byte)` | `%11.0g` |
| `mh019_` | Age depression symptoms first time | `Numeric(Byte)` | `%11.0g` |
| `mh020_` | Ever treated for depression by doctor or psychiatrist | `Numeric(Byte)` | `%11.0g` |
| `mh021_` | Ever admitted to mental hospital or psychiatric ward | `Numeric(Byte)` | `%11.0g` |
| `mh022_` | Ever told affective or emotional disorders | `Numeric(Byte)` | `%11.0g` |
| `mh023_` | Fear of the worst happening | `Numeric(Byte)` | `%16.0g` |
| `mh024_` | Nervous | `Numeric(Byte)` | `%16.0g` |
| `mh025_` | Hands trembling | `Numeric(Byte)` | `%16.0g` |
| `mh026_` | Fear of dying | `Numeric(Byte)` | `%16.0g` |
| `mh027_` | Felt faint | `Numeric(Byte)` | `%16.0g` |
| `mh030_` | Year depression for the last time | `Numeric(Byte)` | `%11.0g` |
| `mh031_` | Month depression for the last time | `Numeric(Byte)` | `%11.0g` |
| `mh032_` | End non proxy | `Numeric(Byte)` | `%59.0g` |

### `pf` - Peak Flow

- Dataset: `sharew4_rel9-0-0_pf.dta`
- Read with: `ps.read_share_module("pf", wave=4)`
- Rows: 57,982
- Variables: 17
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `pf002_` | Feels safe to do the test | `Numeric(Byte)` | `%11.0g` |
| `pf003_` | Value first measurement | `Numeric(Int)` | `%11.0g` |
| `pf004_` | Value second measurement | `Numeric(Int)` | `%11.0g` |
| `pf005_` | Effort R gave to this measurement | `Numeric(Byte)` | `%60.0g` |
| `pf006_` | Position of R for this test | `Numeric(Byte)` | `%11.0g` |
| `pf007d1` | Why pf not completed: R felt it would not be safe | `Numeric(Byte)` | `%12.0g` |
| `pf007d2` | Why pf not completed: IWER felt it would not be safe | `Numeric(Byte)` | `%12.0g` |
| `pf007d3` | Why pf not completed: R refused or was not willing to complete | `Numeric(Byte)` | `%12.0g` |
| `pf007d4` | Why pf not completed: R tried but was unable to complete | `Numeric(Byte)` | `%12.0g` |
| `pf007d5` | Why pf not completed: R did not understand the instructions | `Numeric(Byte)` | `%12.0g` |
| `pf007dot` | Why pf not completed: Other | `Numeric(Byte)` | `%12.0g` |

### `ph` - Physical Health

- Dataset: `sharew4_rel9-0-0_ph.dta`
- Read with: `ps.read_share_module("ph", wave=4)`
- Rows: 57,982
- Variables: 185
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ph003_` | Health in general question 2 | `Numeric(Byte)` | `%13.0g` |
| `ph004_` | Long-term illness | `Numeric(Byte)` | `%11.0g` |
| `ph005_` | Limited in activities because of health | `Numeric(Byte)` | `%32.0g` |
| `ph006d1` | Heart attack: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d2` | High blood pressure or hypertension: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d3` | High blood cholesterol: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d4` | Stroke: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d5` | Diabetes or high blood sugar: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d6` | Chronic lung disease: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d7` | Asthma: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d8` | Arthritis: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d9` | Osteoporosis: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d10` | Cancer: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d11` | Stomach or duodenal ulcer, peptic ulcer: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d12` | Parkinson disease: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d13` | Cataracts: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d14` | Hip fracture or femoral fracture: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d15` | Other fractures: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d16` | Alzheimer's disease, dementia, senility: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
| `ph006d17` | Benign tumor: ever diagnosed/currently having | `Numeric(Byte)` | `%12.0g` |
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
| `ph009_1` | Age heart attack or other heart problems | `Numeric(Int)` | `%11.0g` |
| `ph009_2` | Age high blood pressure | `Numeric(Int)` | `%11.0g` |
| `ph009_3` | Age high blood cholesterol | `Numeric(Byte)` | `%11.0g` |
| `ph009_4` | Age stroke or cerebral vascular disease | `Numeric(Byte)` | `%11.0g` |
| `ph009_5` | Age diabetes | `Numeric(Byte)` | `%11.0g` |
| `ph009_6` | Age chronic lung disease | `Numeric(Byte)` | `%11.0g` |
| `ph009_7` | Age asthma | `Numeric(Byte)` | `%11.0g` |
| `ph009_8` | Age arthritis or rheumatism | `Numeric(Byte)` | `%11.0g` |
| `ph009_9` | Age osteoporosis | `Numeric(Byte)` | `%11.0g` |
| `ph009_10` | Age cancer or malignant tumour | `Numeric(Byte)` | `%11.0g` |
| `ph009_11` | Age stomach, duodenal or peptic ulcer | `Numeric(Byte)` | `%11.0g` |
| `ph009_12` | Age parkinson disease | `Numeric(Byte)` | `%11.0g` |
| `ph009_13` | Age cataracts | `Numeric(Byte)` | `%11.0g` |
| `ph009_14` | Age hip or femoral fracture | `Numeric(Byte)` | `%11.0g` |
| `ph009_15` | Age other fractures | `Numeric(Byte)` | `%11.0g` |
| `ph009_16` | Age alzheimer's disease | `Numeric(Byte)` | `%11.0g` |
| `ph009_17` | Age benign tumor | `Numeric(Byte)` | `%11.0g` |
| `ph010d1` | Bothered by: pain in back, knees, hips or other joint | `Numeric(Byte)` | `%12.0g` |
| `ph010d2` | Bothered by: heart trouble | `Numeric(Byte)` | `%12.0g` |
| `ph010d3` | Bothered by: breathlessness | `Numeric(Byte)` | `%12.0g` |
| `ph010d4` | Bothered by: persistent cough | `Numeric(Byte)` | `%12.0g` |
| `ph010d5` | Bothered by: swollen legs | `Numeric(Byte)` | `%12.0g` |
| `ph010d6` | Bothered by: sleeping problems | `Numeric(Byte)` | `%12.0g` |
| `ph010d7` | Bothered by: falling down | `Numeric(Byte)` | `%12.0g` |
| `ph010d8` | Bothered by: fear of falling down | `Numeric(Byte)` | `%12.0g` |
| `ph010d9` | Bothered by: dizziness, faints or blackouts | `Numeric(Byte)` | `%12.0g` |
| `ph010d10` | Bothered by: stomach or intestine problems | `Numeric(Byte)` | `%12.0g` |
| `ph010d11` | Bothered by: incontinence | `Numeric(Byte)` | `%12.0g` |
| `ph010d12` | Bothered by: fatigue | `Numeric(Byte)` | `%12.0g` |
| `ph010dno` | Bothered by: no symptoms | `Numeric(Byte)` | `%12.0g` |
| `ph010dot` | Bothered by: other symptoms | `Numeric(Byte)` | `%12.0g` |
| `ph011d1` | Drugs for: high blood cholesterol | `Numeric(Byte)` | `%12.0g` |
| `ph011d2` | Drugs for: high blood pressure | `Numeric(Byte)` | `%12.0g` |
| `ph011d3` | Drugs for: coronary diseases | `Numeric(Byte)` | `%12.0g` |
| `ph011d4` | Drugs for: other heart diseases | `Numeric(Byte)` | `%12.0g` |
| `ph011d5` | Drugs for: asthma | `Numeric(Byte)` | `%12.0g` |
| `ph011d6` | Drugs for: diabetes | `Numeric(Byte)` | `%12.0g` |
| `ph011d7` | Drugs for: joint pain | `Numeric(Byte)` | `%12.0g` |
| `ph011d8` | Drugs for: other pain | `Numeric(Byte)` | `%12.0g` |
| `ph011d9` | Drugs for: sleep problems | `Numeric(Byte)` | `%12.0g` |
| `ph011d10` | Drugs for: anxiety or depression | `Numeric(Byte)` | `%12.0g` |
| `ph011d11` | Drugs for: osteoporosis (hormonal) | `Numeric(Byte)` | `%12.0g` |
| `ph011d12` | Drugs for: osteoporosis (other) | `Numeric(Byte)` | `%12.0g` |
| `ph011d13` | Drugs for: stomach burns | `Numeric(Byte)` | `%12.0g` |
| `ph011d14` | Drugs for: chronic bronchitis | `Numeric(Byte)` | `%12.0g` |
| `ph011dno` | Drugs for: none | `Numeric(Byte)` | `%12.0g` |
| `ph011dot` | Drugs for: other | `Numeric(Byte)` | `%12.0g` |
| `ph012_` | Weight of respondent | `Numeric(Double)` | `%11.0g` |
| `ph013_` | How tall are you? | `Numeric(Double)` | `%11.0g` |
| `ph041_` | Wears glasses/contact lenses | `Numeric(Byte)` | `%11.0g` |
| `ph043_` | Eyesight distance | `Numeric(Byte)` | `%13.0g` |
| `ph044_` | Eyesight reading | `Numeric(Byte)` | `%13.0g` |
| `ph045_` | Use hearing aid | `Numeric(Byte)` | `%11.0g` |
| `ph046_` | Hearing | `Numeric(Byte)` | `%13.0g` |
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
| `ph049dno` | Difficulties: none of these | `Numeric(Byte)` | `%12.0g` |
| `ph054_` | Who answered the questions in ph | `Numeric(Byte)` | `%44.0g` |
| `ph061_` | Health problem that limits paid work | `Numeric(Byte)` | `%11.0g` |
| `ph065_` | Check: lost weight | `Numeric(Byte)` | `%54.0g` |
| `ph066_` | Reason lost weight | `Numeric(Byte)` | `%58.0g` |
| `ph071_1` | How many heart attacks since last interview | `Numeric(Byte)` | `%11.0g` |
| `ph071_2` | How many strokes/diagnosed cerebral vascular disease since last interview | `Numeric(Byte)` | `%11.0g` |
| `ph071_3` | How often diagnosed with cancer since last interview | `Numeric(Byte)` | `%11.0g` |
| `ph071_4` | How often suffered a hip fracture since last interview | `Numeric(Byte)` | `%11.0g` |
| `ph072_1` | Had a heart attack since last interview | `Numeric(Byte)` | `%11.0g` |
| `ph072_2` | Had a stroke/diagnosed with cerebral vascular disease since last interview | `Numeric(Byte)` | `%11.0g` |
| `ph072_3` | Been diagnosed with cancer since last interview | `Numeric(Byte)` | `%11.0g` |
| `ph072_4` | Suffered a hip fracture since last interview | `Numeric(Byte)` | `%11.0g` |
| `ph073_1` | Check: had a heart attack before last interview | `Numeric(Byte)` | `%11.0g` |
| `ph073_2` | Check: had a stroke/diagnosed with cerebral vascular disease before last intervi | `Numeric(Byte)` | `%11.0g` |
| `ph073_3` | Check: been diagnosed with cancer before last interview | `Numeric(Byte)` | `%11.0g` |
| `ph073_4` | Check: suffered a hip fracture before last interview | `Numeric(Byte)` | `%11.0g` |
| `ph074_1` | Reason disputes had condition: heart attack | `Numeric(Byte)` | `%45.0g` |
| `ph074_2` | Reason disputes had condition: stroke/diagnosed with cerebral vascular disease | `Numeric(Byte)` | `%45.0g` |
| `ph074_3` | Reason disputes had condition: diagnosed with cancer | `Numeric(Byte)` | `%45.0g` |
| `ph074_4` | Reason disputes had condition: suffered a hip fracture | `Numeric(Byte)` | `%45.0g` |
| `ph075_1` | Had ANOTHER heart attack since last interview | `Numeric(Byte)` | `%33.0g` |
| `ph075_2` | Had ANOTHER stroke/diagnosed with cerebral vascular disease AGAIN since last int | `Numeric(Byte)` | `%33.0g` |
| `ph075_3` | Been diagnosed with cancer AGAIN since last interview | `Numeric(Byte)` | `%33.0g` |
| `ph075_4` | Suffered ANOTHER hip fracture since last interview | `Numeric(Byte)` | `%33.0g` |
| `ph076_1` | Year most recent condition: heart atttack | `Numeric(Byte)` | `%11.0g` |
| `ph076_2` | Year most recent condition: stroke/cerebral vascular disease | `Numeric(Byte)` | `%11.0g` |
| `ph076_3` | Year most recent condition: cancer | `Numeric(Byte)` | `%11.0g` |
| `ph076_4` | Year most recent condition: hip fracture | `Numeric(Byte)` | `%11.0g` |
| `ph077_1` | Month most recent condition: heart atttack | `Numeric(Byte)` | `%11.0g` |
| `ph077_2` | Month most recent condition: stroke/cerebral vascular disease | `Numeric(Byte)` | `%11.0g` |
| `ph077_3` | Month most recent condition: cancer | `Numeric(Byte)` | `%11.0g` |
| `ph077_4` | Month most recent condition: hip fracture | `Numeric(Byte)` | `%11.0g` |
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

### `sn` - Social Networks

- Dataset: `sharew4_rel9-0-0_sn.dta`
- Read with: `ps.read_share_module("sn", wave=4)`
- Rows: 57,982
- Variables: 56
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sn002a_1` | Any more persons with whom you often discuss: sn person 1 | `Numeric(Byte)` | `%11.0g` |
| `sn002a_2` | Any more persons with whom you often discuss: sn person 2 | `Numeric(Byte)` | `%11.0g` |
| `sn002a_3` | Any more persons with whom you often discuss: sn person 3 | `Numeric(Byte)` | `%11.0g` |
| `sn002a_4` | Any more persons with whom you often discuss: sn person 4 | `Numeric(Byte)` | `%11.0g` |
| `sn002a_5` | Any more persons with whom you often discuss: sn person 5 | `Numeric(Byte)` | `%11.0g` |
| `sn002a_6` | Any more persons with whom you often discuss: sn person 6 | `Numeric(Byte)` | `%11.0g` |
| `sn003a_` | Anyone else very important | `Numeric(Byte)` | `%11.0g` |
| `sn005_1` | Network relationship: sn person 1 | `Numeric(Byte)` | `%56.0g` |
| `sn005_2` | Network relationship: sn person 2 | `Numeric(Byte)` | `%56.0g` |
| `sn005_3` | Network relationship: sn person 3 | `Numeric(Byte)` | `%56.0g` |
| `sn005_4` | Network relationship: sn person 4 | `Numeric(Byte)` | `%56.0g` |
| `sn005_5` | Network relationship: sn person 5 | `Numeric(Byte)` | `%56.0g` |
| `sn005_6` | Network relationship: sn person 6 | `Numeric(Byte)` | `%56.0g` |
| `sn005_7` | Network relationship: sn person 7 | `Numeric(Byte)` | `%56.0g` |
| `sn005a_1` | Network person gender: sn person 1 | `Numeric(Byte)` | `%11.0g` |
| `sn005a_2` | Network person gender: sn person 2 | `Numeric(Byte)` | `%11.0g` |
| `sn005a_3` | Network person gender: sn person 3 | `Numeric(Byte)` | `%11.0g` |
| `sn005a_4` | Network person gender: sn person 4 | `Numeric(Byte)` | `%11.0g` |
| `sn005a_5` | Network person gender: sn person 5 | `Numeric(Byte)` | `%11.0g` |
| `sn005a_6` | Network person gender: sn person 6 | `Numeric(Byte)` | `%11.0g` |
| `sn005a_7` | Network person gender: sn person 7 | `Numeric(Byte)` | `%11.0g` |
| `sn006_1` | Network proximity: sn person 1 | `Numeric(Byte)` | `%39.0g` |
| `sn006_2` | Network proximity: sn person 2 | `Numeric(Byte)` | `%39.0g` |
| `sn006_3` | Network proximity: sn person 3 | `Numeric(Byte)` | `%39.0g` |
| `sn006_4` | Network proximity: sn person 4 | `Numeric(Byte)` | `%39.0g` |
| `sn006_5` | Network proximity: sn person 5 | `Numeric(Byte)` | `%39.0g` |
| `sn006_6` | Network proximity: sn person 6 | `Numeric(Byte)` | `%39.0g` |
| `sn006_7` | Network proximity: sn person 7 | `Numeric(Byte)` | `%39.0g` |
| `sn007_1` | Network contact: sn person 1 | `Numeric(Byte)` | `%27.0g` |
| `sn007_2` | Network contact: sn person 2 | `Numeric(Byte)` | `%27.0g` |
| `sn007_3` | Network contact: sn person 3 | `Numeric(Byte)` | `%27.0g` |
| `sn007_4` | Network contact: sn person 4 | `Numeric(Byte)` | `%27.0g` |
| `sn007_5` | Network contact: sn person 5 | `Numeric(Byte)` | `%27.0g` |
| `sn007_6` | Network contact: sn person 6 | `Numeric(Byte)` | `%27.0g` |
| `sn007_7` | Network contact: sn person 7 | `Numeric(Byte)` | `%27.0g` |
| `sn009_1` | Network closeness: sn person 1 | `Numeric(Byte)` | `%15.0g` |
| `sn009_2` | Network closeness: sn person 2 | `Numeric(Byte)` | `%15.0g` |
| `sn009_3` | Network closeness: sn person 3 | `Numeric(Byte)` | `%15.0g` |
| `sn009_4` | Network closeness: sn person 4 | `Numeric(Byte)` | `%15.0g` |
| `sn009_5` | Network closeness: sn person 5 | `Numeric(Byte)` | `%15.0g` |
| `sn009_6` | Network closeness: sn person 6 | `Numeric(Byte)` | `%15.0g` |
| `sn009_7` | Network closeness: sn person 7 | `Numeric(Byte)` | `%15.0g` |
| `sn012_` | Network satisfaction | `Numeric(Byte)` | `%11.0g` |
| `sn013_` | Non proxy | `Numeric(Byte)` | `%59.0g` |
| `sn014_` | Privacy SN | `Numeric(Byte)` | `%62.0g` |
| `sn015d1` | Who was present: respondent alone | `Numeric(Byte)` | `%12.0g` |
| `sn015d2` | Who was present: partner present | `Numeric(Byte)` | `%12.0g` |
| `sn015d3` | Who was present: child(ren) present | `Numeric(Byte)` | `%12.0g` |
| `sn015dot` | Who was present: other(s) | `Numeric(Byte)` | `%12.0g` |
| `sn017_` | Empty network satisfaction | `Numeric(Byte)` | `%11.0g` |

### `sp` - Social Support

- Dataset: `sharew4_rel9-0-0_sp.dta`
- Read with: `ps.read_share_module("sp", wave=4)`
- Rows: 57,982
- Variables: 140
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sp002_` | Received help from others (outside hh) | `Numeric(Byte)` | `%11.0g` |
| `sp003_1sp` | Who gave you help: person 1 | `Numeric(Int)` | `%39.0g` |
| `sp003_2sp` | Who gave you help: person 2 | `Numeric(Int)` | `%39.0g` |
| `sp003_3sp` | Who gave you help: person 3 | `Numeric(Int)` | `%39.0g` |
| `sp005_1` | How often received help: from person 1 | `Numeric(Byte)` | `%18.0g` |
| `sp005_2` | How often received help: from person 2 | `Numeric(Byte)` | `%18.0g` |
| `sp005_3` | How often received help: from person 3 | `Numeric(Byte)` | `%18.0g` |
| `sp007_1` | Any other helper from outside the household | `Numeric(Byte)` | `%11.0g` |
| `sp007_2` | Any other helper from outside the household | `Numeric(Byte)` | `%11.0g` |
| `sp007_3` | Any other helper from outside the household | `Numeric(Byte)` | `%11.0g` |
| `sp008_` | Given help last twelve months | `Numeric(Byte)` | `%11.0g` |
| `sp009_1sp` | To whom did you give help: person 1 | `Numeric(Int)` | `%39.0g` |
| `sp009_2sp` | To whom did you give help: person 2 | `Numeric(Int)` | `%39.0g` |
| `sp009_3sp` | To whom did you give help: person 3 | `Numeric(Int)` | `%39.0g` |
| `sp011_1` | How often given help to person 1 | `Numeric(Byte)` | `%18.0g` |
| `sp011_2` | How often given help to person 2 | `Numeric(Byte)` | `%18.0g` |
| `sp011_3` | How often given help to person 3 | `Numeric(Byte)` | `%18.0g` |
| `sp013_1` | Have you given help to others | `Numeric(Byte)` | `%11.0g` |
| `sp013_2` | Have you given help to others | `Numeric(Byte)` | `%11.0g` |
| `sp013_3` | Have you given help to others | `Numeric(Byte)` | `%11.0g` |
| `sp014_` | Looked after grandchildren | `Numeric(Byte)` | `%11.0g` |
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
| `sp016_1` | How often did you look after child of child 1 | `Numeric(Byte)` | `%18.0g` |
| `sp016_2` | How often did you look after child of child 2 | `Numeric(Byte)` | `%18.0g` |
| `sp016_3` | How often did you look after child of child 3 | `Numeric(Byte)` | `%18.0g` |
| `sp016_4` | How often did you look after child of child 4 | `Numeric(Byte)` | `%18.0g` |
| `sp016_5` | How often did you look after child of child 5 | `Numeric(Byte)` | `%18.0g` |
| `sp016_6` | How often did you look after child of child 6 | `Numeric(Byte)` | `%18.0g` |
| `sp016_7` | How often did you look after child of child 7 | `Numeric(Byte)` | `%18.0g` |
| `sp016_8` | How often did you look after child of child 8 | `Numeric(Byte)` | `%18.0g` |
| `sp016_9` | How often did you look after child of child 9 | `Numeric(Byte)` | `%18.0g` |
| `sp016_10` | How often did you look after child of child 10 | `Numeric(Byte)` | `%18.0g` |
| `sp016_11` | How often did you look after child of child 11 | `Numeric(Byte)` | `%18.0g` |
| `sp016_12` | How often did you look after child of child 12 | `Numeric(Byte)` | `%18.0g` |
| `sp016_13` | How often did you look after child of child 13 | `Numeric(Byte)` | `%18.0g` |
| `sp016_14` | How often did you look after child of child 14 | `Numeric(Byte)` | `%18.0g` |
| `sp016_15` | How often do you look after child of child 15 | `Numeric(Byte)` | `%18.0g` |
| `sp016_16` | How often do you look after child of child 16 | `Numeric(Byte)` | `%18.0g` |
| `sp016_17` | How often do you look after child of child 17 | `Numeric(Byte)` | `%18.0g` |
| `sp016_18` | How often do you look after child of child 18 | `Numeric(Byte)` | `%18.0g` |
| `sp016_19` | How often do you look after child of child 19 | `Numeric(Byte)` | `%18.0g` |
| `sp016_20` | How often do you look after child of child 20 | `Numeric(Byte)` | `%18.0g` |
| `sp018_` | Given help to someone with personal care in the household | `Numeric(Byte)` | `%11.0g` |
| `sp019d1sn` | R provided help with personal care to: social network person 1 | `Numeric(Byte)` | `%12.0g` |
| `sp019d2sn` | R provided help with personal care to: social network person 2 | `Numeric(Byte)` | `%12.0g` |
| `sp019d3sn` | R provided help with personal care to: social network person 3 | `Numeric(Byte)` | `%12.0g` |
| `sp019d4sn` | R provided help with personal care to: social network person 4 | `Numeric(Byte)` | `%12.0g` |
| `sp019d5sn` | R provided help with personal care to: social network person 5 | `Numeric(Byte)` | `%12.0g` |
| `sp019d6sn` | R provided help with personal care to: social network person 6 | `Numeric(Byte)` | `%12.0g` |
| `sp019d7sn` | R provided help with personal care to: social network person 7 | `Numeric(Byte)` | `%12.0g` |
| `sp019d1sp` | R provided help with personal care to: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sp019d2sp` | R provided help with personal care to: mother | `Numeric(Byte)` | `%12.0g` |
| `sp019d3sp` | R provided help with personal care to: father | `Numeric(Byte)` | `%12.0g` |
| `sp019d4sp` | R provided help with personal care to: mother-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp019d5sp` | R provided help with personal care to: father-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp019d6sp` | R provided help with personal care to: stepmother | `Numeric(Byte)` | `%12.0g` |
| `sp019d7sp` | R provided help with personal care to: stepfather | `Numeric(Byte)` | `%12.0g` |
| `sp019d8sp` | R provided help with personal care to: brother | `Numeric(Byte)` | `%12.0g` |
| `sp019d9sp` | R provided help with personal care to: sister | `Numeric(Byte)` | `%12.0g` |
| `sp019d19sp` | R provided help with personal care to: child | `Numeric(Byte)` | `%12.0g` |
| `sp019d20sp` | R provided help with personal care to: son-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp019d21sp` | R provided help with personal care to: daughter-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp019d22sp` | R provided help with personal care to: grandchild | `Numeric(Byte)` | `%12.0g` |
| `sp019d23sp` | R provided help with personal care to: grandparent | `Numeric(Byte)` | `%12.0g` |
| `sp019d24sp` | R provided help with personal care to: aunt | `Numeric(Byte)` | `%12.0g` |
| `sp019d25sp` | R provided help with personal care to: uncle | `Numeric(Byte)` | `%12.0g` |
| `sp019d26sp` | R provided help with personal care to: niece | `Numeric(Byte)` | `%12.0g` |
| `sp019d27sp` | R provided help with personal care to: nephew | `Numeric(Byte)` | `%12.0g` |
| `sp019d28sp` | R provided help with personal care to: other relative | `Numeric(Byte)` | `%12.0g` |
| `sp019d29sp` | R provided help with personal care to: friend | `Numeric(Byte)` | `%12.0g` |
| `sp019d30sp` | R provided help with personal care to: ex-colleague | `Numeric(Byte)` | `%12.0g` |
| `sp019d31sp` | R provided help with personal care to: neighbour | `Numeric(Byte)` | `%12.0g` |
| `sp019d32sp` | R provided help with personal care to: ex-spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sp019d34sp` | R provided help with personal care to: step-child/current partner's child | `Numeric(Byte)` | `%12.0g` |
| `sp019d35sp` | R provided help with personal care to: minister, priest, or other clergy | `Numeric(Byte)` | `%12.0g` |
| `sp019d36sp` | R provided help with personal care to: therapist or other professional helper | `Numeric(Byte)` | `%12.0g` |
| `sp019d37sp` | R provided help with personal care to: housekeeper/home health care provider | `Numeric(Byte)` | `%12.0g` |
| `sp019dno` | R provided help with personal care to: NONE OF THESE | `Numeric(Byte)` | `%12.0g` |
| `sp020_` | Someone in this household helped you regularly with personal care | `Numeric(Byte)` | `%11.0g` |
| `sp021d1sn` | R received help with personal care from: social network person 1 | `Numeric(Byte)` | `%12.0g` |
| `sp021d2sn` | R received help with personal care from: social network person 2 | `Numeric(Byte)` | `%12.0g` |
| `sp021d3sn` | R received help with personal care from: social network person 3 | `Numeric(Byte)` | `%12.0g` |
| `sp021d4sn` | R received help with personal care from: social network person 4 | `Numeric(Byte)` | `%12.0g` |
| `sp021d5sn` | R received help with personal care from: social network person 5 | `Numeric(Byte)` | `%12.0g` |
| `sp021d6sn` | R received help with personal care from: social network person 6 | `Numeric(Byte)` | `%12.0g` |
| `sp021d7sn` | R received help with personal care from: social network person 7 | `Numeric(Byte)` | `%12.0g` |
| `sp021d1sp` | R received help with personal care from: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sp021d2sp` | R received help with personal care from: mother | `Numeric(Byte)` | `%12.0g` |
| `sp021d3sp` | R received help with personal care from: father | `Numeric(Byte)` | `%12.0g` |
| `sp021d4sp` | R received help with personal care from: mother-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp021d5sp` | R received help with personal care from: father-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp021d6sp` | R received help with personal care from: stepmother | `Numeric(Byte)` | `%12.0g` |
| `sp021d7sp` | R received help with personal care from: stepfather | `Numeric(Byte)` | `%12.0g` |
| `sp021d8sp` | R received help with personal care from: brother | `Numeric(Byte)` | `%12.0g` |
| `sp021d9sp` | R received help with personal care from: sister | `Numeric(Byte)` | `%12.0g` |
| `sp021d19sp` | R received help with personal care from: child | `Numeric(Byte)` | `%12.0g` |
| `sp021d20sp` | R received help with personal care from: son-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp021d21sp` | R received help with personal care from: daughter-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp021d22sp` | R received help with personal care from: grandchild | `Numeric(Byte)` | `%12.0g` |
| `sp021d23sp` | R received help with personal care from: grandparent | `Numeric(Byte)` | `%12.0g` |
| `sp021d24sp` | R received help with personal care from: aunt | `Numeric(Byte)` | `%12.0g` |
| `sp021d25sp` | R received help with personal care from: uncle | `Numeric(Byte)` | `%12.0g` |
| `sp021d26sp` | R received help with personal care from: niece | `Numeric(Byte)` | `%12.0g` |
| `sp021d27sp` | R received help with personal care from: nephew | `Numeric(Byte)` | `%12.0g` |
| `sp021d28sp` | R received help with personal care from: other relative | `Numeric(Byte)` | `%12.0g` |
| `sp021d29sp` | R received help with personal care from: friend | `Numeric(Byte)` | `%12.0g` |
| `sp021d30sp` | R received help with personal care from: ex-colleague | `Numeric(Byte)` | `%12.0g` |
| `sp021d31sp` | R received help with personal care from: neighbour | `Numeric(Byte)` | `%12.0g` |
| `sp021d32sp` | R received help with personal care from: ex-spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sp021d34sp` | R received help with personal care from: step-child/current partner's child | `Numeric(Byte)` | `%12.0g` |
| `sp021d35sp` | R received help with personal care from: minister, priest, or other clergy | `Numeric(Byte)` | `%12.0g` |
| `sp021d36sp` | R received help with personal care from: therapist or other professional helper | `Numeric(Byte)` | `%12.0g` |
| `sp021d37sp` | R received help with personal care from: housekeeper/home health care provider | `Numeric(Byte)` | `%12.0g` |
| `sp022_` | Who answered the questions in sp | `Numeric(Byte)` | `%44.0g` |

### `xt` - End-of-Life Interview

- Dataset: `sharew4_rel9-0-0_xt.dta`
- Read with: `ps.read_share_module("xt", wave=4)`
- Rows: 1,174
- Variables: 172
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language_xt` | Language: End of life interview | `Numeric(Byte)` | `%44.0g` |
| `gender_xt` | Gender of the deceased | `Numeric(Byte)` | `%10.0g` |
| `yrbirth_xt` | Year of birth of the deceased | `Numeric(Int)` | `%10.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `xt002_` | Relationship to the deceased | `Numeric(Byte)` | `%50.0g` |
| `xt005_` | How often contact last twelve month | `Numeric(Byte)` | `%27.0g` |
| `xt006_` | Proxy respondent's sex | `Numeric(Byte)` | `%11.0g` |
| `xt007_` | Year of birth proxy | `Numeric(Int)` | `%11.0g` |
| `xt008_` | Month of decease | `Numeric(Byte)` | `%11.0g` |
| `xt009_` | Year of decease | `Numeric(Int)` | `%11.0g` |
| `xt010_` | Age at the moment of decease | `Numeric(Int)` | `%11.0g` |
| `xt011_` | Main cause of death | `Numeric(Byte)` | `%62.0g` |
| `xt012c` | Main cause of death: xt012 coded | `Numeric(Byte)` | `%60.0g` |
| `xt013_` | How long been ill before decease | `Numeric(Byte)` | `%51.0g` |
| `xt014_` | Place of dying | `Numeric(Byte)` | `%56.0g` |
| `xt015_` | Times in hospital last year before dying | `Numeric(Byte)` | `%18.0g` |
| `xt016_` | Total time in hospital last year before dying | `Numeric(Byte)` | `%53.0g` |
| `xt018_1` | Type of medical care in last 12 months: care from a general practitioner | `Numeric(Byte)` | `%11.0g` |
| `xt018_2` | Type of medical care in last 12 months: care from specialist physicians | `Numeric(Byte)` | `%11.0g` |
| `xt018_3` | Type of medical care in last 12 months: hospital stays | `Numeric(Byte)` | `%11.0g` |
| `xt018_4` | Type of medical care in last 12 months: care in a nursing home | `Numeric(Byte)` | `%11.0g` |
| `xt018_5` | Type of medical care in last 12 months: hospice stays | `Numeric(Byte)` | `%11.0g` |
| `xt018_6` | Type of medical care in last 12 months: medication | `Numeric(Byte)` | `%11.0g` |
| `xt018_7` | Type of medical care in last 12 months: aids and appliances | `Numeric(Byte)` | `%11.0g` |
| `xt018_8` | Type of medical care in last 12 months: home care or help due to disability | `Numeric(Byte)` | `%11.0g` |
| `xt019e_1` | Costs: care from a general practitioner | `Numeric(Double)` | `%11.0g` |
| `xt019e_2` | Costs: care from specialist physicians | `Numeric(Double)` | `%11.0g` |
| `xt019e_3` | Costs: hospital stays | `Numeric(Double)` | `%11.0g` |
| `xt019e_4` | Costs: care in a nursing home | `Numeric(Double)` | `%11.0g` |
| `xt019e_5` | Costs: hospice stays | `Numeric(Double)` | `%11.0g` |
| `xt019e_6` | Costs: medication | `Numeric(Double)` | `%11.0g` |
| `xt019e_7` | Costs: aids and appliances | `Numeric(Double)` | `%11.0g` |
| `xt019e_8` | Costs: home care or help due to disability | `Numeric(Double)` | `%11.0g` |
| `xt019ub_1` | Costs: care from a general practitioner ub | `Numeric(Byte)` | `%32.0g` |
| `xt019ub_2` | Costs: care from specialist physicians ub | `Numeric(Byte)` | `%32.0g` |
| `xt019ub_3` | Costs: hospital stays ub | `Numeric(Byte)` | `%32.0g` |
| `xt019ub_4` | Costs: care in a nursing home ub | `Numeric(Byte)` | `%32.0g` |
| `xt019ub_5` | Costs: hospice stays ub | `Numeric(Byte)` | `%32.0g` |
| `xt019ub_6` | Costs: medication ub | `Numeric(Byte)` | `%32.0g` |
| `xt019ub_7` | Costs: aids and appliances ub | `Numeric(Byte)` | `%32.0g` |
| `xt019ub_8` | Costs: home care or help due to disability ub | `Numeric(Byte)` | `%32.0g` |
| `xt019v1_1` | Bracket value 1: care from a general practicioner | `Numeric(Float)` | `%11.0g` |
| `xt019v1_2` | Bracket value 1: care from specialist physicians | `Numeric(Float)` | `%11.0g` |
| `xt019v1_3` | Bracket value 1: hospital stays | `Numeric(Float)` | `%11.0g` |
| `xt019v1_4` | Bracket value 1: care in a nursing home | `Numeric(Float)` | `%11.0g` |
| `xt019v1_5` | Bracket value 1: hospice stays | `Numeric(Float)` | `%11.0g` |
| `xt019v1_6` | Bracket value 1: medication | `Numeric(Float)` | `%11.0g` |
| `xt019v1_7` | Bracket value 1: aids and appliances | `Numeric(Float)` | `%11.0g` |
| `xt019v1_8` | Bracket value 1: home care or help due to disability | `Numeric(Float)` | `%11.0g` |
| `xt019v2_1` | Bracket value 2: care from a general practicioner | `Numeric(Float)` | `%11.0g` |
| `xt019v2_2` | Bracket value 2: care from specialist physicians | `Numeric(Float)` | `%11.0g` |
| `xt019v2_3` | Bracket value 2: hospital stays | `Numeric(Float)` | `%11.0g` |
| `xt019v2_4` | Bracket value 2: care in a nursing home | `Numeric(Double)` | `%11.0g` |
| `xt019v2_5` | Bracket value 2: hospice stays | `Numeric(Float)` | `%11.0g` |
| `xt019v2_6` | Bracket value 2: medication | `Numeric(Float)` | `%11.0g` |
| `xt019v2_7` | Bracket value 2: aids and appliances | `Numeric(Float)` | `%11.0g` |
| `xt019v2_8` | Bracket value 2: home care or help due to disability | `Numeric(Float)` | `%11.0g` |
| `xt019v3_1` | Bracket value 3: care from a general practicioner | `Numeric(Float)` | `%11.0g` |
| `xt019v3_2` | Bracket value 3: care from specialist physicians | `Numeric(Float)` | `%11.0g` |
| `xt019v3_3` | Bracket value 3: hospital stays | `Numeric(Float)` | `%11.0g` |
| `xt019v3_4` | Bracket value 3: care in a nursing home | `Numeric(Double)` | `%11.0g` |
| `xt019v3_5` | Bracket value 3: hospice stays | `Numeric(Float)` | `%11.0g` |
| `xt019v3_6` | Bracket value 3: medication | `Numeric(Float)` | `%11.0g` |
| `xt019v3_7` | Bracket value 3: aids and appliances | `Numeric(Float)` | `%11.0g` |
| `xt019v3_8` | Bracket value 3: home care or help due to disability | `Numeric(Float)` | `%11.0g` |
| `xt020d1` | Difficulties doing activities: dressing, including putting on shoes and socks | `Numeric(Byte)` | `%12.0g` |
| `xt020d2` | Difficulties doing activities: walking across a room | `Numeric(Byte)` | `%12.0g` |
| `xt020d3` | Difficulties doing activities: bathing or showering | `Numeric(Byte)` | `%12.0g` |
| `xt020d4` | Difficulties doing activities: eating, such as cutting up your food | `Numeric(Byte)` | `%12.0g` |
| `xt020d5` | Difficulties doing activities: getting in or out of bed | `Numeric(Byte)` | `%12.0g` |
| `xt020d6` | Difficulties doing activities: using the toilet, including getting up or down | `Numeric(Byte)` | `%12.0g` |
| `xt020d7` | Difficulties doing activities: preparing a hot meal | `Numeric(Byte)` | `%12.0g` |
| `xt020d8` | Difficulties doing activities: shopping for groceries | `Numeric(Byte)` | `%12.0g` |
| `xt020d9` | Difficulties doing activities: making telephone calls | `Numeric(Byte)` | `%12.0g` |
| `xt020d10` | Difficulties doing activities: taking medication | `Numeric(Byte)` | `%12.0g` |
| `xt020dno` | Difficulties doing activities: none of these | `Numeric(Byte)` | `%12.0g` |
| `xt022_` | Anyone helped with ADL | `Numeric(Byte)` | `%11.0g` |
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
| `xt024_` | Time the deceased received help | `Numeric(Byte)` | `%49.0g` |
| `xt025_` | Hours of help necessary during typical day | `Numeric(Byte)` | `%11.0g` |
| `xt026_` | The deceased had a will | `Numeric(Byte)` | `%11.0g` |
| `xt027d1` | Beneficiaries of the estate: yourself (proxy) | `Numeric(Byte)` | `%12.0g` |
| `xt027d2` | Beneficiaries of the estate: spouse/partner of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt027d3` | Beneficiaries of the estate: children of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt027d4` | Beneficiaries of the estate: grandchildren of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt027d5` | Beneficiaries of the estate: siblings of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt027d6` | Beneficiaries of the estate: other relatives of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt027d7` | Beneficiaries of the estate: other non-relatives | `Numeric(Byte)` | `%12.0g` |
| `xt027d8` | Beneficiaries of the estate: church, foundation or charitable organization | `Numeric(Byte)` | `%12.0g` |
| `xt027d9` | Beneficiaries of the estate: deceased did not leave anything at all (SPONTANEOUS | `Numeric(Byte)` | `%12.0g` |
| `xt030_` | The deceased owned home | `Numeric(Byte)` | `%11.0g` |
| `xt031e` | Value of home after mortgages | `Numeric(Double)` | `%11.0g` |
| `xt031ub` | Values home after mortgages ub | `Numeric(Byte)` | `%32.0g` |
| `xt031v1` | Bracket value 1 | `Numeric(Double)` | `%11.0g` |
| `xt031v2` | Bracket value 2 | `Numeric(Double)` | `%11.0g` |
| `xt031v3` | Bracket value 3 | `Numeric(Double)` | `%11.0g` |
| `xt032d1` | Who inherited the home of the deceased: yourself (proxy) | `Numeric(Byte)` | `%12.0g` |
| `xt032d2` | Who inherited the home of the deceased: spouse/partner of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt032d3` | Who inherited the home of the deceased: sons/daughters | `Numeric(Byte)` | `%12.0g` |
| `xt032d4` | Who inherited the home of the deceased: grandchildren of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt032d5` | Who inherited the home of the deceased: siblings of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt032d6` | Who inherited the home of the deceased: other relatives | `Numeric(Byte)` | `%12.0g` |
| `xt032d7` | Who inherited the home of the deceased: other non-relatives | `Numeric(Byte)` | `%12.0g` |
| `xt033_` | Deceased owned any life insurance policies | `Numeric(Byte)` | `%11.0g` |
| `xt034e` | Value of all life insurance policies | `Numeric(Double)` | `%11.0g` |
| `xt035d1` | Beneficiaries of the life insurance policies: yourself (proxy) | `Numeric(Byte)` | `%12.0g` |
| `xt035d2` | Beneficiaries of the life insurance policies: spouse/partner of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt035d3` | Beneficiaries of the life insurance policies: sons/daughters | `Numeric(Byte)` | `%12.0g` |
| `xt035d4` | Beneficiaries of the life insurance policies: grandchildren of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt035d5` | Beneficiaries of the life insurance policies: siblings of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt035d6` | Beneficiaries of the life insurance policies: other relatives | `Numeric(Byte)` | `%12.0g` |
| `xt035d7` | Beneficiaries of the life insurance policies: other non-relatives | `Numeric(Byte)` | `%12.0g` |
| `xt037_1` | Deceased owned assets: business, including land or permises | `Numeric(Byte)` | `%11.0g` |
| `xt037_2` | Deceased owned assets: other real estate | `Numeric(Byte)` | `%11.0g` |
| `xt037_3` | Deceased owned assets: cars | `Numeric(Byte)` | `%11.0g` |
| `xt037_4` | Deceased owned assets: financial assets, e.g. cash/bonds/stocks | `Numeric(Byte)` | `%11.0g` |
| `xt037_5` | Deceased owned assets: jewelry or antiquities | `Numeric(Byte)` | `%11.0g` |
| `xt038e_1` | Value of assets: business, including land or permises | `Numeric(Double)` | `%11.0g` |
| `xt038e_2` | Value of assets: other real estate | `Numeric(Double)` | `%11.0g` |
| `xt038e_3` | Value of assets: cars | `Numeric(Double)` | `%11.0g` |
| `xt038e_4` | Value of assets: financial assets, e.g. cash, bonds or stocks | `Numeric(Double)` | `%11.0g` |
| `xt038e_5` | Value of assets: jewelry or antiquities | `Numeric(Double)` | `%11.0g` |
| `xt038ub_1` | Value of assets: business, including land or permises ub | `Numeric(Byte)` | `%32.0g` |
| `xt038ub_2` | Value of assets: other real estate ub | `Numeric(Byte)` | `%32.0g` |
| `xt038ub_3` | Value of assets: cars ub | `Numeric(Byte)` | `%32.0g` |
| `xt038ub_4` | Value of assets: financial assets, e.g. cash, bonds or stocks ub | `Numeric(Byte)` | `%32.0g` |
| `xt038ub_5` | Value of assets: jewelry or antiquities ub | `Numeric(Byte)` | `%32.0g` |
| `xt038v1_1` | Bracket value 1: business, including land or permises | `Numeric(Float)` | `%11.0g` |
| `xt038v1_2` | Bracket value 1: other real estate | `Numeric(Float)` | `%11.0g` |
| `xt038v1_3` | Bracket value 1: cars | `Numeric(Float)` | `%11.0g` |
| `xt038v1_4` | Bracket value 1: financial assets, e.g. cash/bonds/stocks | `Numeric(Float)` | `%11.0g` |
| `xt038v1_5` | Bracket value 1: jewelry or antiquities | `Numeric(Float)` | `%11.0g` |
| `xt038v2_1` | Bracket value 2: business, including land or permises | `Numeric(Float)` | `%11.0g` |
| `xt038v2_2` | Bracket value 2: other real estate | `Numeric(Float)` | `%11.0g` |
| `xt038v2_3` | Bracket value 2: cars | `Numeric(Float)` | `%11.0g` |
| `xt038v2_4` | Bracket value 2: financial assets, e.g. cash/bonds/stocks | `Numeric(Float)` | `%11.0g` |
| `xt038v2_5` | Bracket value 2: jewelry or antiquities | `Numeric(Float)` | `%11.0g` |
| `xt038v3_1` | Bracket value 3: business, including land or permises | `Numeric(Double)` | `%11.0g` |
| `xt038v3_2` | Bracket value 3: other real estate | `Numeric(Float)` | `%11.0g` |
| `xt038v3_3` | Bracket value 3: cars | `Numeric(Double)` | `%11.0g` |
| `xt038v3_4` | Bracket value 3: financial assets, e.g. cash/bonds/stocks | `Numeric(Float)` | `%11.0g` |
| `xt038v3_5` | Bracket value 3: jewelry or antiquities | `Numeric(Double)` | `%11.0g` |
| `xt039_` | Number of children (still alive) deceased had at the end | `Numeric(Byte)` | `%11.0g` |
| `xt040a_` | Estate divided among children | `Numeric(Byte)` | `%62.0g` |
| `xt040b_` | Some children received more to make up for previous gifts | `Numeric(Byte)` | `%11.0g` |
| `xt040c_` | Some children received more to give them financial support | `Numeric(Byte)` | `%11.0g` |
| `xt040d_` | Some children received more because they helped/cared for deceased | `Numeric(Byte)` | `%11.0g` |
| `xt040e_` | Some children received more because of other reasons | `Numeric(Byte)` | `%11.0g` |
| `xt041_` | Funeral was accompanied by a religious ceremony | `Numeric(Byte)` | `%11.0g` |
| `xt043_` | Interview mode | `Numeric(Byte)` | `%23.0g` |
| `xt105_` | Difficulties remembering where he/she was | `Numeric(Byte)` | `%11.0g` |
| `xt106_` | Difficulties remembering the year | `Numeric(Byte)` | `%11.0g` |
| `xt107_` | Difficulties recognizing | `Numeric(Byte)` | `%11.0g` |
| `xt109_` | Deceased married at time of death | `Numeric(Byte)` | `%11.0g` |


## Special Modules

### `dropoff` - Paper-and-pencil drop-off

- Dataset: `sharew4_rel9-0-0_dropoff.dta`
- Read with: `ps.read_share_module("dropoff", wave=4)`
- Rows: 46,684
- Variables: 1,261
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `gender_do` | Gender | `Numeric(Byte)` | `%12.0g` |
| `yrbirth_do` | Year of birth | `Numeric(Int)` | `%12.0g` |
| `q1a` | Health: to walk about | `Numeric(Byte)` | `%21.0g` |
| `q1b` | Health: self-care | `Numeric(Byte)` | `%33.0g` |
| `q1c` | Health: usual activities | `Numeric(Byte)` | `%35.0g` |
| `q1d` | Health: pain/discomfort | `Numeric(Byte)` | `%27.0g` |
| `q1e` | Health: depressed | `Numeric(Byte)` | `%31.0g` |
| `q2` | Health thermometer | `Numeric(Double)` | `%34.0g` |
| `q3a` | Who pays: medical visit to gp | `Numeric(Byte)` | `%28.0g` |
| `q3b` | Who pays: medical visit to specialist | `Numeric(Byte)` | `%28.0g` |
| `q3c` | Who pays: medical visit to specialist not prescribed by gp | `Numeric(Byte)` | `%28.0g` |
| `q3d` | Who pays: medical visit to any doctor of choice | `Numeric(Byte)` | `%28.0g` |
| `q3e` | Who pays: dental care | `Numeric(Byte)` | `%28.0g` |
| `q3f` | Q3a: Who pays: prescribed drugs | `Numeric(Byte)` | `%28.0g` |
| `q3g` | Q3b: Who pays: hospitalisations in public hospitals | `Numeric(Byte)` | `%28.0g` |
| `q3h` | Q3c: Who pays: hospitalisations in private hospitals | `Numeric(Byte)` | `%28.0g` |
| `q3i` | Q3d: Who pays: stays in nursing home/care in cas of chronic cond. | `Numeric(Byte)` | `%28.0g` |
| `q4a` | Out of pocket expenses: hospital inpatient care | `Numeric(Double)` | `%12.0g` |
| `q4b` | Out of pocket expenses: outpatient care | `Numeric(Double)` | `%12.0g` |
| `q4c` | Out of pocket expenses: prescribed drugs | `Numeric(Double)` | `%12.0g` |
| `q4d` | Out of pocket expenses: care in nursing home, day-care | `Numeric(Double)` | `%12.0g` |
| `q4e` | Out of pocket expenses: home care services | `Numeric(Double)` | `%12.0g` |
| `q5a` | How much of time: feel you lack companionship | `Numeric(Byte)` | `%20.0g` |
| `q5b` | How much of time: feel left out | `Numeric(Byte)` | `%20.0g` |
| `q5c` | How much of time: feel isolated from others | `Numeric(Byte)` | `%20.0g` |
| `q5d` | How much of time: feel lonely | `Numeric(Byte)` | `%20.0g` |
| `at_q1f` | Highest education father | `Numeric(Byte)` | `%44.0g` |
| `at_q1m` | Highest education mother | `Numeric(Byte)` | `%44.0g` |
| `at_q2` | You as well as you're father and mother born in Austria (todays territory) | `Numeric(Byte)` | `%12.0g` |
| `at_q3a_c` | Country of birth | `Numeric(Int)` | `%16.0g` |
| `at_q3b_c` | Country of birth mother | `Numeric(Int)` | `%16.0g` |
| `at_q3c_c` | Country of birth father | `Numeric(Int)` | `%16.0g` |
| `at_q4_2f` | Year since when father lived in Austria | `Numeric(Int)` | `%12.0g` |
| `at_q4_2m` | Year since when mother lived in Austria | `Numeric(Int)` | `%12.0g` |
| `at_q4_3a_f` | Father lived in Austria for specific time: from | `Numeric(Int)` | `%12.0g` |
| `at_q4_3a_m` | Mother lived in Austria for specific time: from | `Numeric(Int)` | `%12.0g` |
| `at_q4_3b_f` | Father lived in Austria for specific time: to | `Numeric(Int)` | `%12.0g` |
| `at_q4_3b_m` | Mother lived in Austria for specific time: to | `Numeric(Int)` | `%12.0g` |
| `at_q4f` | Father lived in Austria since birth | `Numeric(Byte)` | `%21.0g` |
| `at_q4m` | Mother lived in Austria since birth | `Numeric(Byte)` | `%21.0g` |
| `at_q5a` | Difficulties linked to integration: language | `Numeric(Byte)` | `%17.0g` |
| `at_q5b` | Difficulties linked to integration: dealing with authorities/bureaucracy | `Numeric(Byte)` | `%17.0g` |
| `at_q5c` | Difficulties linked to integration: work/occupation | `Numeric(Byte)` | `%17.0g` |
| `at_q5d` | Difficulties linked to integration: finances/creditworthiness | `Numeric(Byte)` | `%17.0g` |
| `at_q5e` | Difficulties linked to integration: apartment/accomodation | `Numeric(Byte)` | `%17.0g` |
| `at_q5f` | Difficulties linked to integration: school/education for children | `Numeric(Byte)` | `%17.0g` |
| `at_q5g` | Difficulties linked to integration: others | `Numeric(Byte)` | `%17.0g` |
| `at_q6a` | Help during integration/move: family members already living in Austria | `Numeric(Byte)` | `%15.0g` |
| `at_q6b` | Help during integration/move: others from origin country already living in Austr | `Numeric(Byte)` | `%15.0g` |
| `at_q6c` | Help during integration/move: local population | `Numeric(Byte)` | `%15.0g` |
| `at_q6d` | Help during integration/move: social organization | `Numeric(Byte)` | `%15.0g` |
| `at_q6e` | Help during integration/move: local authorities/government | `Numeric(Byte)` | `%15.0g` |
| `at_q6f` | Help during integration/move: others | `Numeric(Byte)` | `%15.0g` |
| `at_q9` | Have you/a member of your family ever been persecuted due to political/armed con | `Numeric(Byte)` | `%12.0g` |
| `at_q10_1` | Persecuted in which incident (1st answer) | `Numeric(Byte)` | `%51.0g` |
| `at_q10_2` | Persecuted in which incident (2nd answer) | `Numeric(Byte)` | `%51.0g` |
| `at_q10_3` | Persecuted in which incident (3rd answer) | `Numeric(Byte)` | `%51.0g` |
| `at_q11c` | Year of persecution | `Numeric(Int)` | `%12.0g` |
| `at_q12a1` | Own political views as reason for persecution of yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q12a2` | Own political views as reason for persecution of spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q12a3` | Own political views as reason for persecution of father | `Numeric(Byte)` | `%12.0g` |
| `at_q12a4` | Own political views as reason for persecution of mother | `Numeric(Byte)` | `%12.0g` |
| `at_q12a5` | Own political views as reason for persecution of siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q12a6` | Own political views as reason for persecution of your children | `Numeric(Byte)` | `%12.0g` |
| `at_q12b1` | Religion as reason for persecution of yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q12b2` | Religion as reason for persecution of spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q12b3` | Religion as reason for persecution of father | `Numeric(Byte)` | `%12.0g` |
| `at_q12b4` | Religion as reason for persecution of mother | `Numeric(Byte)` | `%12.0g` |
| `at_q12b5` | Religion as reason for persecution of siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q12b6` | Religion as reason for persecution of your children | `Numeric(Byte)` | `%12.0g` |
| `at_q12c1` | Nationality as reason for persecution of yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q12c2` | Nationality as reason for persecution of spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q12c3` | Nationality as reason for persecution of father | `Numeric(Byte)` | `%12.0g` |
| `at_q12c4` | Nationality as reason for persecution of mother | `Numeric(Byte)` | `%12.0g` |
| `at_q12c5` | Nationality as reason for persecution of siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q12c6` | Nationality as reason for persecution of your children | `Numeric(Byte)` | `%12.0g` |
| `at_q12d1` | Origin as reason for persecution of yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q12d2` | Origin as reason for persecution of spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q12d3` | Origin as reason for persecution of father | `Numeric(Byte)` | `%12.0g` |
| `at_q12d4` | Origin as reason for persecution of mother | `Numeric(Byte)` | `%12.0g` |
| `at_q12d5` | Origin as reason for persecution of siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q12d6` | Origin as reason for persecution of your children | `Numeric(Byte)` | `%12.0g` |
| `at_q12e1` | Political view/religion/origin of other family member as reason: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q12e2` | Political view/religion/origin of other family member as reason: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q12e3` | Political view/religion/origin of other family member as reason: father | `Numeric(Byte)` | `%12.0g` |
| `at_q12e4` | Political view/religion/origin of other family member as reason: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q12e5` | Political view/religion/origin of other family member as reason: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q12e6` | Political view/religion/origin of other family member as reason: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q12f1` | Membership in a political movement as reason for persecution of yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q12f2` | Membership in a political movement as reason for persecution of spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q12f3` | Membership in a political movement as reason for persecution of father | `Numeric(Byte)` | `%12.0g` |
| `at_q12f4` | Membership in a political movement as reason for persecution of mother | `Numeric(Byte)` | `%12.0g` |
| `at_q12f5` | Membership in a political movement as reason for persecution of siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q12f6` | Membership in a political movement as reason for persecution of your children | `Numeric(Byte)` | `%12.0g` |
| `at_q12g1` | Belonging to a special social group as reason for persecution of yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q12g2` | Belonging to a special social group as reason for persecution of spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q12g3` | Belonging to a special social group as reason for persecution of father | `Numeric(Byte)` | `%12.0g` |
| `at_q12g4` | Belonging to a special social group as reason for persecution of mother | `Numeric(Byte)` | `%12.0g` |
| `at_q12g5` | Belonging to a special social group as reason for persecution of siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q12g6` | Belonging to a special social group as reason for persecution of your children | `Numeric(Byte)` | `%12.0g` |
| `at_q12h1` | Other reason for persecution of yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q12h2` | Other reason for persecution of spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q12h3` | Other reason for persecution of father | `Numeric(Byte)` | `%12.0g` |
| `at_q12h4` | Other reason for persecution of mother | `Numeric(Byte)` | `%12.0g` |
| `at_q12h5` | Other reason for persecution of siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q12h6` | Other reason for persecution of your children | `Numeric(Byte)` | `%12.0g` |
| `at_q13a2` | Death as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q13a3` | Death as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q13a4` | Death as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q13a5` | Death as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q13a6` | Death as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q13b1` | Concentration camp as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q13b2` | Concentration camp as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q13b3` | Concentration camp as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q13b4` | Concentration camp as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q13b5` | Concentration camp as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q13b6` | Concentration camp as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q13c1` | Imprisonment as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q13c2` | Imprisonment as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q13c3` | Imprisonment as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q13c4` | Imprisonment as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q13c5` | Imprisonment as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q13c6` | Imprisonment as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q13d1` | Resettlement as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q13d2` | Resettlement as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q13d3` | Resettlement as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q13d4` | Resettlement as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q13d5` | Resettlement as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q13d6` | Resettlement as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q13e1` | Emigration as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q13e2` | Emigration as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q13e3` | Emigration as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q13e4` | Emigration as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q13e5` | Emigration as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q13e6` | Emigration as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q13f1` | Loss of work as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q13f2` | Loss of work as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q13f3` | Loss of work as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q13f4` | Loss of work as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q13f5` | Loss of work as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q13f6` | Loss of work as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q13g1` | Loss of property/assets/firm as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q13g2` | Loss of property/assets/firm as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q13g3` | Loss of property/assets/firm as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q13g4` | Loss of property/assets/firm as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q13g5` | Loss of property/assets/firm as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q13g6` | Loss of property/assets/firm as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q13h1` | Education not possible as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q13h2` | Education not possible as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q13h3` | Education not possible as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q13h4` | Education not possible as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q13h5` | Education not possible as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q13h6` | Education not possible as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q13i1` | Conscription as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q13i2` | Conscription as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q13i3` | Conscription as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q13i4` | Conscription as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q13i5` | Conscription as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q13i6` | Conscription as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q13k1` | Coersive psychiatry as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q13k2` | Coersive psychiatry as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q13k3` | Coersive psychiatry as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q13k4` | Coersive psychiatry as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q13k5` | Coersive psychiatry as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q13k6` | Coersive psychiatry as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q13l1` | Torture as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q13l2` | Torture as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q13l3` | Torture as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q13l4` | Torture as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q13l5` | Torture as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q13l6` | Torture as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q13m1` | No consequences of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q13m2` | No consequences of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q13m3` | No consequences of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q13m4` | No consequences of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q13m5` | No consequences of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q13m6` | No consequences of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q13n1` | Other consequences of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q13n2` | Other consequences of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q13n3` | Other consequences of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q13n4` | Other consequences of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q13n5` | Other consequences of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q13n6` | Other consequences of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q14a1` | Physical health problems as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q14a2` | Physical health problems as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q14a3` | Physical health problems as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q14a4` | Physical health problems as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q14a5` | Physical health problems as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q14a6` | Physical health problems as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q14b1` | Mental health problems as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q14b2` | Mental health problems as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q14b3` | Mental health problems as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q14b4` | Mental health problems as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q14b5` | Mental health problems as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q14b6` | Mental health problems as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q14c1` | Family problems as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q14c2` | Family problems as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q14c3` | Family problems as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q14c4` | Family problems as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q14c5` | Family problems as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q14c6` | Family problems as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q14d1` | Financial problems as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q14d2` | Financial problems as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q14d3` | Financial problems as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q14d4` | Financial problems as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q14d5` | Financial problems as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q14d6` | Financial problems as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q14e1` | Other problems as consequence of persecution: yourself | `Numeric(Byte)` | `%12.0g` |
| `at_q14e2` | Other problems as consequence of persecution: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `at_q14e3` | Other problems as consequence of persecution: father | `Numeric(Byte)` | `%12.0g` |
| `at_q14e4` | Other problems as consequence of persecution: mother | `Numeric(Byte)` | `%12.0g` |
| `at_q14e5` | Other problems as consequence of persecution: siblings | `Numeric(Byte)` | `%12.0g` |
| `at_q14e6` | Other problems as consequence of persecution: your children | `Numeric(Byte)` | `%12.0g` |
| `at_q15` | Duration of problems | `Numeric(Byte)` | `%45.0g` |
| `at_q21` | Amount of drugs regularily taken (prescribed by your doctor) | `Numeric(Byte)` | `%12.0g` |
| `at_q22` | Amount of drugs regularily taken (NOT prescribed) | `Numeric(Byte)` | `%12.0g` |
| `at_q24a` | Shopping done by yourself | `Numeric(Byte)` | `%17.0g` |
| `at_q24b` | Measuring weight done by yourself | `Numeric(Byte)` | `%17.0g` |
| `at_q24c` | I fell down | `Numeric(Byte)` | `%17.0g` |
| `at_q25` | How often achieved help from home nursing | `Numeric(Byte)` | `%57.0g` |
| `be_fr_q5` | Category of national health insurance | `Numeric(Byte)` | `%59.0g` |
| `be_nl_q12` | How old do you feel? | `Numeric(Double)` | `%12.0g` |
| `be_nl_q16` | Category of national health insurance system | `Numeric(Byte)` | `%39.0g` |
| `be_nl_q21a` | How often visited by: daughers(-in-law) | `Numeric(Byte)` | `%25.0g` |
| `be_nl_q21b` | How often visited by: sons(-in-law) | `Numeric(Byte)` | `%25.0g` |
| `be_nl_q21c` | How often visited by: grandchildren | `Numeric(Byte)` | `%25.0g` |
| `be_nl_q21d` | How often visited by: parents(-in-law) | `Numeric(Byte)` | `%25.0g` |
| `be_nl_q21e` | How often visited by: siblings(-in-law) | `Numeric(Byte)` | `%25.0g` |
| `be_nl_q21f` | How often visited by: other relatives | `Numeric(Byte)` | `%25.0g` |
| `be_nl_q21g` | How often visited by: neighbours | `Numeric(Byte)` | `%25.0g` |
| `be_nl_q21h` | How often visited by: friends/acquaintances | `Numeric(Byte)` | `%25.0g` |
| `be_nl_q21i` | How often visited by: others | `Numeric(Byte)` | `%25.0g` |
| `be_nl_q31a` | How satisfied with: life as whole | `Numeric(Byte)` | `%23.0g` |
| `be_nl_q31b` | How satisfied with: standard of living | `Numeric(Byte)` | `%23.0g` |
| `be_nl_q31c` | How satisfied with: health | `Numeric(Byte)` | `%23.0g` |
| `be_nl_q31d` | How satisfied with: what achieved in life | `Numeric(Byte)` | `%23.0g` |
| `be_nl_q31e` | How satisfied with: personal relationships | `Numeric(Byte)` | `%23.0g` |
| `be_nl_q31f` | How satisfied with: how safe feeling | `Numeric(Byte)` | `%23.0g` |
| `be_nl_q31g` | How satisfied with: feeling part of your comunity | `Numeric(Byte)` | `%23.0g` |
| `be_nl_q31h` | How satisfied with: future security | `Numeric(Byte)` | `%23.0g` |
| `be_nl_q31i` | How satisfied with: spirituality or religion | `Numeric(Byte)` | `%23.0g` |
| `be_nl_q41a` | Does accommodation have: separate bath/shower | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q41b` | Does accommodation have: indoor flushing toilet | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q41c` | Does accommodation have: central heating | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q41d` | Does accommodation have: hot tap water | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q41e` | Does accommodation have: place to sit outside | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q42a` | Problems of accomodation: too small | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q42b` | Problems of accomodation: not enough light | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q42c` | Problems of accomodation: leaky roof, damp walls or floors,... | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q42d` | Problems of accomodation: insufficient means to heat | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q51a` | Items to make life easier: cell-phone | `Numeric(Byte)` | `%22.0g` |
| `be_nl_q51b` | Items to make life easier: telephone (fixed line) | `Numeric(Byte)` | `%22.0g` |
| `be_nl_q51c` | Items to make life easier: colour tv | `Numeric(Byte)` | `%22.0g` |
| `be_nl_q51d` | Items to make life easier: personal computer | `Numeric(Byte)` | `%22.0g` |
| `be_nl_q51e` | Items to make life easier: internet connection | `Numeric(Byte)` | `%22.0g` |
| `be_nl_q51f` | Items to make life easier: washing machine | `Numeric(Byte)` | `%22.0g` |
| `be_nl_q51g` | Items to make life easier: dish washer | `Numeric(Byte)` | `%22.0g` |
| `be_nl_q51h` | Items to make life easier: car | `Numeric(Byte)` | `%22.0g` |
| `be_nl_q52a` | Reads the newspaper every day | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q52b` | Has a hobby | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q52c` | Went on vacation in Belgium (last 12 months) | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q52d` | Went on vacation abroad (last 12 months) | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q52e` | Went on a day trip (last 12 months) | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q61` | Aware of a service that provides family care and additional home care | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q62` | Aware of a service that provides logistical help | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q63` | Aware of a service that provides nursing at home | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q64` | Aware of a service that provides meals-on-wheels | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q71f` | Highest school degree: Father | `Numeric(Byte)` | `%23.0g` |
| `be_nl_q71m` | Highest school degree: Mother | `Numeric(Byte)` | `%23.0g` |
| `be_nl_q611` | Rely on service that provides family care (now or last year) | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q621` | Rely on service that provides logistical help (now or last year) | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q631` | Rely on service that provides nursing at home (now or last year) | `Numeric(Byte)` | `%12.0g` |
| `be_nl_q641` | Rely on service that provides meals-on-wheels (now or last year) | `Numeric(Byte)` | `%12.0g` |
| `ch_q6` | Insurance model contracted | `Numeric(Byte)` | `%27.0g` |
| `ch_q7` | Changed insurance model during last 12 months | `Numeric(Byte)` | `%12.0g` |
| `ch_q8` | Changed health insurance company during last 12 months (of basic insurance) | `Numeric(Byte)` | `%12.0g` |
| `ch_q9` | Main reason switched health insurance company | `Numeric(Byte)` | `%61.0g` |
| `ch_q10` | Main reason NOT switched health insurance company | `Numeric(Byte)` | `%66.0g` |
| `ch_q11` | Amount of yearly deductible | `Numeric(Byte)` | `%12.0g` |
| `ch_q12` | Changed amount of deductible during last 12 months | `Numeric(Byte)` | `%21.0g` |
| `ch_q13` | Main reason for this change | `Numeric(Byte)` | `%42.0g` |
| `ch_q14` | Receives subsidies from canton/municipality | `Numeric(Byte)` | `%12.0g` |
| `ch_q15` | Has a complementary insurance | `Numeric(Byte)` | `%12.0g` |
| `ch_q16a` | Complementary insurance covers: hospitalization | `Numeric(Byte)` | `%12.0g` |
| `ch_q16b` | Complementary insurance covers: ambulatory care | `Numeric(Byte)` | `%12.0g` |
| `ch_q16c` | Complementary insurance covers: home care | `Numeric(Byte)` | `%12.0g` |
| `ch_q16d` | Complementary insurance covers: daily allowance, income loss | `Numeric(Byte)` | `%12.0g` |
| `ch_q16e` | Complementary insurance covers: other | `Numeric(Byte)` | `%12.0g` |
| `ch_q17` | Contracted complementary insurance with same fund as basic | `Numeric(Byte)` | `%12.0g` |
| `cz_qcz1a_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz1a_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz1b_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz1b_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz1c_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz1c_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz1d_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz1d_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz1e_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz1e_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz1f_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz1f_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4a_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4a_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4a_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4a_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4a_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4a_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4a_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4a_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4b_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4b_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4b_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4b_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4b_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4b_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4b_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4b_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4c_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4c_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4c_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4c_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4c_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4c_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4c_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4c_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4d_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4d_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4d_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4d_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4d_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4d_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4d_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4d_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4e_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4e_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4e_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4e_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4e_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4e_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4e_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4e_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4f_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4f_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4f_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4f_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4f_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4f_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4f_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4f_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4g_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4g_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4g_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4g_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4g_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4g_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4g_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4g_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4h_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4h_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4h_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4h_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4h_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4h_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4h_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4h_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4i_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4i_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4i_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4i_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4i_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4i_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4i_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz4i_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5a_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5a_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5a_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5a_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5a_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5a_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5a_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5a_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5b_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5b_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5b_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5b_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5b_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5b_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5b_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5b_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5c_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5c_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5c_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5c_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5c_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5c_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5c_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5c_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5d_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5d_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5d_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5d_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5d_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5d_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5d_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5d_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5e_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5e_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5e_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5e_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5e_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5e_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5e_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5e_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5f_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5f_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5f_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5f_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5f_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5f_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5f_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz5f_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6a_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6a_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6a_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6a_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6a_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6a_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6a_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6a_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6b_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6b_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6b_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6b_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6b_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6b_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6b_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6b_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6c_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6c_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6c_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6c_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6c_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6c_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6c_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6c_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6d_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6d_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6d_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6d_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6d_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6d_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6d_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz6d_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz7a` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz7a_codes` | CZ only | `Numeric(Int)` | `%10.0g` |
| `cz_qcz8a_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8a_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8a_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8a_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8a_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8a_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8a_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8a_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8b_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8b_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8b_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8b_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8b_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8b_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8b_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8b_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8c_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8c_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8c_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8c_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8c_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8c_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8c_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8c_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8d_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8d_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8d_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8d_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8d_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8d_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8d_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8d_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8e_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8e_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8e_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8e_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8e_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8e_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8e_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8e_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8f_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8f_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8f_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8f_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8f_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8f_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8f_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8f_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8g_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8g_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8g_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8g_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8g_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8g_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8g_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8g_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8h_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8h_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8h_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8h_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8h_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8h_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8h_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8h_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8i_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8i_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8i_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8i_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8i_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8i_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8i_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8i_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8j_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8j_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8j_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8j_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8j_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8j_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8j_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8j_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8k_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8k_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8k_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8k_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8k_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8k_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8k_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz8k_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9a_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9a_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9a_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9a_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9a_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9a_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9a_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9a_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9b_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9b_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9b_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9b_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9b_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9b_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9b_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9b_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9c_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9c_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9c_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9c_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9c_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9c_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9c_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9c_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9d_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9d_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9d_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9d_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9d_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9d_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9d_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9d_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9e_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9e_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9e_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9e_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9e_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9e_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9e_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9e_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9f_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9f_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9f_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9f_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9f_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9f_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9f_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz9f_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10a_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10a_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10a_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10a_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10a_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10a_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10a_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10a_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10b_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10b_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10b_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10b_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10b_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10b_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10b_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10b_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10c_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10c_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10c_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10c_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10c_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10c_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10c_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10c_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10d_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10d_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10d_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10d_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10d_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10d_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10d_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz10d_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11a_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11a_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11a_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11a_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11a_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11a_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11a_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11a_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11b_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11b_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11b_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11b_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11b_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11b_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11b_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11b_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11c_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11c_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11c_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11c_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11c_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11c_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11c_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11c_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11d_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11d_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11d_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11d_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11d_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11d_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11d_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11d_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11e_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11e_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11e_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11e_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11e_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11e_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11e_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11e_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11f_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11f_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11f_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11f_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11f_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11f_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11f_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11f_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11g_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11g_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11g_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11g_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11g_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11g_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11g_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11g_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11h_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11h_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11h_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11h_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11h_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11h_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11h_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11h_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11i_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11i_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11i_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11i_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11i_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11i_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11i_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11i_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11j_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11j_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11j_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11j_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11j_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11j_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11j_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11j_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11k_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11k_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11k_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11k_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11k_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11k_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11k_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz11k_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12a_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12a_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12a_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12a_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12a_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12a_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12a_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12a_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12b_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12b_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12b_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12b_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12b_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12b_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12b_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12b_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12c_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12c_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12c_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12c_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12c_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12c_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12c_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12c_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12d_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12d_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12d_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12d_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12d_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12d_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12d_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12d_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12e_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12e_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12e_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12e_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12e_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12e_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12e_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12e_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12f_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12f_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12f_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12f_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12f_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12f_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12f_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz12f_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13a_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13a_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13a_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13a_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13a_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13a_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13a_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13a_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13b_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13b_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13b_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13b_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13b_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13b_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13b_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13b_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13c_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13c_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13c_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13c_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13c_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13c_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13c_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13c_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13d_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13d_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13d_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13d_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13d_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13d_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13d_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz13d_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14a_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14a_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14a_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14a_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14a_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14a_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14a_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14a_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14b_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14b_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14b_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14b_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14b_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14b_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14b_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz14b_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15a_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15a_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15a_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15a_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15a_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15a_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15a_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15a_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15b_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15b_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15b_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15b_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15b_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15b_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15b_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15b_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15c_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15c_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15c_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15c_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15c_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15c_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15c_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15c_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15d_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15d_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15d_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15d_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15d_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15d_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15d_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15d_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15e_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15e_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15e_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15e_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15e_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15e_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15e_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15e_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15f_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15f_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15f_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15f_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15f_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15f_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15f_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz15f_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16a_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16a_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16a_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16a_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16a_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16a_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16a_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16a_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16b_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16b_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16b_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16b_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16b_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16b_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16b_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16b_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16c_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16c_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16c_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16c_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16c_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16c_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16c_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16c_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16d_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16d_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16d_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16d_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16d_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16d_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16d_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz16d_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17a_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17a_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17a_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17a_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17a_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17a_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17a_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17a_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17b_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17b_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17b_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17b_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17b_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17b_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17b_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17b_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17c_1` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17c_2` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17c_3` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17c_4` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17c_5` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17c_6` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17c_7` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `cz_qcz17c_8` | CZ only | `Numeric(Byte)` | `%10.0g` |
| `de_q7` | Claim to contribution or medical care for members of civil service | `Numeric(Byte)` | `%13.0f` |
| `de_q8` | Changed health insurance company after the 31. of Dec 2007 | `Numeric(Byte)` | `%13.0f` |
| `de_q9` | Type of health insurance | `Numeric(Byte)` | `%41.0f` |
| `de_q10` | Company of health insurance | `Numeric(Byte)` | `%26.0f` |
| `de_q11` | Personally you are in this health insurance: | `Numeric(Byte)` | `%83.0f` |
| `de_q12` | Type of tariff | `Numeric(Byte)` | `%21.0f` |
| `de_q12_wahl` | Type of optional tariff | `Numeric(Byte)` | `%38.0f` |
| `de_q13` | Policy holder | `Numeric(Byte)` | `%24.0f` |
| `de_q14` | Amount of monthly contribution | `Numeric(Int)` | `%13.0f` |
| `de_q15` | More persons insured with that health insurance | `Numeric(Byte)` | `%13.0f` |
| `de_q16` | Health insurance with deductible | `Numeric(Byte)` | `%12.0f` |
| `de_q17a` | Amount of deductible in per cent | `Numeric(Byte)` | `%12.0f` |
| `de_q17b` | Amount of deductible in euro | `Numeric(Int)` | `%12.0f` |
| `dk_q6` | Public health insurance group | `Numeric(Byte)` | `%24.0g` |
| `dk_q7` | Member of health insurance association ”Danmark” | `Numeric(Byte)` | `%32.0g` |
| `dk_q8a` | Covered by private supplementary health insurance: yes, health ins. assoc. ”Danm | `Numeric(Byte)` | `%12.0g` |
| `dk_q8b` | Covered by private supplementary health insurance: yes, other private | `Numeric(Byte)` | `%12.0g` |
| `dk_q8c` | Covered by private supplementary health insurance: yes, extended | `Numeric(Byte)` | `%12.0g` |
| `dk_q8d` | Covered by private supplementary health insurance: yes, fixed disbursement | `Numeric(Byte)` | `%12.0g` |
| `dk_q8e` | Covered by private supplementary health insurance: yes, does not know which type | `Numeric(Byte)` | `%12.0g` |
| `dk_q8f` | Covered by private supplementary health insurance: no | `Numeric(Byte)` | `%12.0g` |
| `dk_q8g` | Covered by private supplementary health insurance: don't know | `Numeric(Byte)` | `%12.0g` |
| `dk_q9` | Who pays for private supplementary health insurance? | `Numeric(Byte)` | `%27.0g` |
| `dk_q10` | Days of moderate/harder physical activity per week (at least 30min a day) | `Numeric(Byte)` | `%13.0g` |
| `dk_q11` | Leisure time activity last 12 months | `Numeric(Byte)` | `%45.0g` |
| `dk_q12` | Influence you think you have on municipality to take up issues of your interest | `Numeric(Byte)` | `%19.0g` |
| `dk_q13a` | Usual hh expenditures (typical month): food to eat at home | `Numeric(Long)` | `%12.0g` |
| `dk_q13b` | Usual hh expenditures (typical month): eating outside the hh | `Numeric(Long)` | `%12.0g` |
| `dk_q13c` | Usual hh expenditures (typical month): telephone | `Numeric(Long)` | `%12.0g` |
| `dk_q13d` | Usual hh expenditures (typical month): all goods and services | `Numeric(Long)` | `%12.0g` |
| `dk_q13e` | Usual hh expenditures (typical month): gifts to (grand-)children | `Numeric(Long)` | `%12.0g` |
| `dk_q14a` | Times went on vacation in Denmark (last 12 months) | `Numeric(Byte)` | `%8.0g` |
| `dk_q14b` | Times went on vacation abroad (last 12 months) | `Numeric(Byte)` | `%8.0g` |
| `dk_q14c` | Money hh used on vacation abroad (last 12 months) | `Numeric(Long)` | `%12.0g` |
| `dk_q15` | Received a disbursement of “SP-money” during the years 2009-10 | `Numeric(Byte)` | `%12.0g` |
| `dk_q16` | Amount received as lump sum of “SP-money” | `Numeric(Long)` | `%12.0g` |
| `dk_q17a` | Use of “SP-money”: holidays | `Numeric(Byte)` | `%12.0g` |
| `dk_q17b` | Use of “SP-money”: lasting improvement of residence | `Numeric(Byte)` | `%12.0g` |
| `dk_q17c` | Use of “SP-money”: other private consumption | `Numeric(Byte)` | `%12.0g` |
| `dk_q17d` | Use of “SP-money”: investment in securities/pension | `Numeric(Byte)` | `%12.0g` |
| `dk_q17e` | Use of “SP-money”: repayment of loan | `Numeric(Byte)` | `%12.0g` |
| `dk_q18` | Member of religious community | `Numeric(Byte)` | `%39.0g` |
| `dk_q19` | How often goes to church | `Numeric(Byte)` | `%22.0g` |
| `dk_q20` | How often prays to God (apart from services) | `Numeric(Byte)` | `%21.0g` |
| `dk_q21` | Importance of role of God in life today | `Numeric(Byte)` | `%19.0g` |
| `es_q6a` | Received: professional/paid nursing/personal care in own home | `Numeric(Byte)` | `%12.0g` |
| `es_q6b` | Received: professional/paid home help for domestic tasks due to health problems | `Numeric(Byte)` | `%12.0g` |
| `es_q6c` | Received: teleassistance | `Numeric(Byte)` | `%12.0g` |
| `es_q6d` | Received: paid help from non-professional caregiver in own home | `Numeric(Byte)` | `%12.0g` |
| `es_q6e` | Received: stays in day/night-care centers | `Numeric(Byte)` | `%12.0g` |
| `es_q6f` | Received: Stays in a nursing home | `Numeric(Byte)` | `%12.0g` |
| `es_q7a` | Who provided services: public national long-term care system | `Numeric(Byte)` | `%12.0g` |
| `es_q7b` | Who provided services: other health care and social programs | `Numeric(Byte)` | `%12.0g` |
| `es_q7c` | Who provided services: hired and paid by yourself | `Numeric(Byte)` | `%12.0g` |
| `es_q8a_d2` | During Civil War and the 40s: spouse/partner lost life | `Numeric(Byte)` | `%12.0g` |
| `es_q8a_d3` | During Civil War and the 40s: father lost life | `Numeric(Byte)` | `%12.0g` |
| `es_q8a_d4` | During Civil War and the 40s: mother lost life | `Numeric(Byte)` | `%12.0g` |
| `es_q8a_d5` | During Civil War and the 40s: child lost life | `Numeric(Byte)` | `%12.0g` |
| `es_q8a_d6` | During Civil War and the 40s: sibling lost life | `Numeric(Byte)` | `%12.0g` |
| `es_q8b_d1` | During Civil War and the 40s: respondent in concentration camp | `Numeric(Byte)` | `%12.0g` |
| `es_q8b_d2` | During Civil War and the 40s: spouse/partner in concentration camp | `Numeric(Byte)` | `%12.0g` |
| `es_q8b_d3` | During Civil War and the 40s: father in concentration camp | `Numeric(Byte)` | `%12.0g` |
| `es_q8b_d4` | During Civil War and the 40s: mother in concentration camp | `Numeric(Byte)` | `%12.0g` |
| `es_q8b_d5` | During Civil War and the 40s: child in concentration camp | `Numeric(Byte)` | `%12.0g` |
| `es_q8b_d6` | During Civil War and the 40s: sibling in concentration camp | `Numeric(Byte)` | `%12.0g` |
| `es_q8c_d1` | During Civil War and the 40s: respondent in prison | `Numeric(Byte)` | `%12.0g` |
| `es_q8c_d2` | During Civil War and the 40s: spouse/partner in prison | `Numeric(Byte)` | `%12.0g` |
| `es_q8c_d3` | During Civil War and the 40s: father in prison | `Numeric(Byte)` | `%12.0g` |
| `es_q8c_d4` | During Civil War and the 40s: mother in prison | `Numeric(Byte)` | `%12.0g` |
| `es_q8c_d5` | During Civil War and the 40s: child in prison | `Numeric(Byte)` | `%12.0g` |
| `es_q8c_d6` | During Civil War and the 40s: sibling in prison | `Numeric(Byte)` | `%12.0g` |
| `es_q8d_d1` | During Civil War and the 40s: respondent in labor camp | `Numeric(Byte)` | `%12.0g` |
| `es_q8d_d2` | During Civil War and the 40s: spouse/partner in labor camp | `Numeric(Byte)` | `%12.0g` |
| `es_q8d_d3` | During Civil War and the 40s: father in labor camp | `Numeric(Byte)` | `%12.0g` |
| `es_q8d_d4` | During Civil War and the 40s: mother in labor camp | `Numeric(Byte)` | `%12.0g` |
| `es_q8d_d5` | During Civil War and the 40s: child in labor camp | `Numeric(Byte)` | `%12.0g` |
| `es_q8d_d6` | During Civil War and the 40s: sibling in labor camp | `Numeric(Byte)` | `%12.0g` |
| `es_q8f_d1` | During Civil War and the 40s: respondent exile/emigration | `Numeric(Byte)` | `%12.0g` |
| `es_q8f_d2` | During Civil War and the 40s: spouse/partner exile/emigration | `Numeric(Byte)` | `%12.0g` |
| `es_q8f_d3` | During Civil War and the 40s: father exile/emigration | `Numeric(Byte)` | `%12.0g` |
| `es_q8f_d4` | During Civil War and the 40s: mother exile/emigration | `Numeric(Byte)` | `%12.0g` |
| `es_q8f_d5` | During Civil War and the 40s: child exile/emigration | `Numeric(Byte)` | `%12.0g` |
| `es_q8f_d6` | During Civil War and the 40s: sibling exile/emigration | `Numeric(Byte)` | `%12.0g` |
| `es_q8g_d1` | During Civil War and the 40s: respondent lost career/job | `Numeric(Byte)` | `%12.0g` |
| `es_q8g_d2` | During Civil War and the 40s: spouse/partner lost career/job | `Numeric(Byte)` | `%12.0g` |
| `es_q8g_d3` | During Civil War and the 40s: father lost career/job | `Numeric(Byte)` | `%12.0g` |
| `es_q8g_d4` | During Civil War and the 40s: mother lost career/job | `Numeric(Byte)` | `%12.0g` |
| `es_q8g_d5` | During Civil War and the 40s: child lost career/job | `Numeric(Byte)` | `%12.0g` |
| `es_q8g_d6` | During Civil War and the 40s: sibling lost career/job | `Numeric(Byte)` | `%12.0g` |
| `es_q8h_d1` | During Civil War and the 40s: respondent lost major property/assets/business | `Numeric(Byte)` | `%12.0g` |
| `es_q8h_d2` | During Civil War and the 40s: spouse/partner lost major property/assets/business | `Numeric(Byte)` | `%12.0g` |
| `es_q8h_d3` | During Civil War and the 40s: father lost major property/assets/business | `Numeric(Byte)` | `%12.0g` |
| `es_q8h_d4` | During Civil War and the 40s: mother lost major property/assets/business | `Numeric(Byte)` | `%12.0g` |
| `es_q8h_d5` | During Civil War and the 40s: child lost major property/assets/business | `Numeric(Byte)` | `%12.0g` |
| `es_q8h_d6` | During Civil War and the 40s: sibling lost major property/assets/business | `Numeric(Byte)` | `%12.0g` |
| `es_q8i_d1` | During Civil War and the 40s: respondent had other sufferings | `Numeric(Byte)` | `%12.0g` |
| `es_q8i_d2` | During Civil War and the 40s: spouse/partner had other sufferings | `Numeric(Byte)` | `%12.0g` |
| `es_q8i_d3` | During Civil War and the 40s: father had other sufferings | `Numeric(Byte)` | `%12.0g` |
| `es_q8i_d4` | During Civil War and the 40s: mother had other sufferings | `Numeric(Byte)` | `%12.0g` |
| `es_q8i_d5` | During Civil War and the 40s: child had other sufferings | `Numeric(Byte)` | `%12.0g` |
| `es_q8i_d6` | During Civil War and the 40s: sibling had other sufferings | `Numeric(Byte)` | `%12.0g` |
| `es_q9a_d1` | Main consequences of Civil War/40s: respondent had physical/mental health proble | `Numeric(Byte)` | `%12.0g` |
| `es_q9a_d2` | Main consequences of Civil War/40s: spouse/partner had physical/mental health pr | `Numeric(Byte)` | `%12.0g` |
| `es_q9a_d3` | Main consequences of Civil War/40s: father had physical/mental health problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9a_d4` | Main consequences of Civil War/40s: mother had physical/mental health problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9a_d5` | Main consequences of Civil War/40s: child had physical/mental health problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9a_d6` | Main consequences of Civil War/40s: sibling had physical/mental health problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9b_d1` | Main consequences of Civil War/40s: respondent had family problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9b_d2` | Main consequences of Civil War/40s: spouse/partner had family problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9b_d3` | Main consequences of Civil War/40s: father had family problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9b_d4` | Main consequences of Civil War/40s: mother had family problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9b_d5` | Main consequences of Civil War/40s: child had family problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9b_d6` | Main consequences of Civil War/40s: sibling had family problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9c_d1` | Main consequences of Civil War/40s: respondent had financial problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9c_d2` | Main consequences of Civil War/40s: spouse/partner had financial problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9c_d3` | Main consequences of Civil War/40s: father had financial problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9c_d4` | Main consequences of Civil War/40s: mother had financial problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9c_d5` | Main consequences of Civil War/40s: child had financial problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9c_d6` | Main consequences of Civil War/40s: sibling had financial problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9d_d1` | Main consequences of Civil War/40s: respondent had job problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9d_d2` | Main consequences of Civil War/40s: spouse/partner had job problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9d_d3` | Main consequences of Civil War/40s: father had job problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9d_d4` | Main consequences of Civil War/40s: mother had job problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9d_d5` | Main consequences of Civil War/40s: child had job problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9d_d6` | Main consequences of Civil War/40s: sibling had job problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9e_d1` | Main consequences of Civil War/40s: respondent had access to education | `Numeric(Byte)` | `%12.0g` |
| `es_q9e_d2` | Main consequences of Civil War/40s: spouse/partner had access to education | `Numeric(Byte)` | `%12.0g` |
| `es_q9e_d3` | Main consequences of Civil War/40s: father had access to education | `Numeric(Byte)` | `%12.0g` |
| `es_q9e_d4` | Main consequences of Civil War/40s: mother had access to education | `Numeric(Byte)` | `%12.0g` |
| `es_q9e_d5` | Main consequences of Civil War/40s: child had access to education | `Numeric(Byte)` | `%12.0g` |
| `es_q9e_d6` | Main consequences of Civil War/40s: sibling had access to education | `Numeric(Byte)` | `%12.0g` |
| `es_q9f_d1` | Main consequences of Civil War/40s: respondent had other problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9f_d2` | Main consequences of Civil War/40s: spouse/partner had other problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9f_d3` | Main consequences of Civil War/40s: father had other problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9f_d4` | Main consequences of Civil War/40s: mother had other problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9f_d5` | Main consequences of Civil War/40s: child had other problems | `Numeric(Byte)` | `%12.0g` |
| `es_q9f_d6` | Main consequences of Civil War/40s: sibling had other problems | `Numeric(Byte)` | `%12.0g` |
| `fr_q6` | Has any supplementary long-term care insurance (excluding gov. prog.) | `Numeric(Byte)` | `%12.0g` |
| `fr_q7` | Lives in a nursing home | `Numeric(Byte)` | `%12.0g` |
| `fr_q8a` | Received: professional/paid nursing/personal care in own home | `Numeric(Byte)` | `%12.0g` |
| `fr_q8b` | Received: professional/paid home help for domestic tasks due to health problems | `Numeric(Byte)` | `%12.0g` |
| `fr_q8c` | Received: meals-on-wheels | `Numeric(Byte)` | `%12.0g` |
| `hu_q6` | Has any supplementary long-term care insurance (excluding gov. prog.) | `Numeric(Byte)` | `%12.0g` |
| `hu_q7a` | Received: professional/paid nursing/personal care in own home | `Numeric(Byte)` | `%12.0g` |
| `hu_q7b` | Received: professional/paid home help for domestic tasks due to health problems | `Numeric(Byte)` | `%12.0g` |
| `hu_q7c` | Received: meals-on-wheels | `Numeric(Byte)` | `%12.0g` |
| `pl_q6a` | Activities at home: watching news in TV | `Numeric(Byte)` | `%21.0g` |
| `pl_q6b` | Activities at home: reading daily newspapers | `Numeric(Byte)` | `%21.0g` |
| `pl_q6c` | Activities at home: reading magazines | `Numeric(Byte)` | `%21.0g` |
| `pl_q6d` | Activities at home: reading books | `Numeric(Byte)` | `%21.0g` |
| `pl_q6e` | Activities at home: listening to serialized novels on radio | `Numeric(Byte)` | `%21.0g` |
| `pl_q6f` | Activities at home: listening to scientific/historical/... programs on radio | `Numeric(Byte)` | `%21.0g` |
| `pl_q6g` | Activities at home: watching films in TV | `Numeric(Byte)` | `%21.0g` |
| `pl_q6h` | Activities at home: watching theatrical plays in TV | `Numeric(Byte)` | `%21.0g` |
| `pl_q6i` | Activities at home: listening to concert transmission on radio/in TV | `Numeric(Byte)` | `%21.0g` |
| `pl_q6j` | Activities at home: listening to audiobooks | `Numeric(Byte)` | `%21.0g` |
| `pl_q6k` | Activities at home: using a computer | `Numeric(Byte)` | `%21.0g` |
| `pl_q6l` | Activities at home: using the internet | `Numeric(Byte)` | `%21.0g` |
| `pl_q6m` | Activities at home: reading in foreign language | `Numeric(Byte)` | `%21.0g` |
| `pl_q7a` | Activities out of home: going out to watch a film | `Numeric(Byte)` | `%27.0g` |
| `pl_q7b` | Activities out of home: going out to a concert | `Numeric(Byte)` | `%27.0g` |
| `pl_q7c` | Activities out of home: going out to see a theatrical play | `Numeric(Byte)` | `%27.0g` |
| `pl_q7d` | Activities out of home: going out to opera or ballet | `Numeric(Byte)` | `%27.0g` |
| `pl_q7e` | Activities out of home: going out to see an exhibition in museum | `Numeric(Byte)` | `%27.0g` |
| `pl_q7f` | Activities out of home: going out to listen to a lecture | `Numeric(Byte)` | `%27.0g` |
| `pl_q7g` | Activities out of home: field trip or excursion within Poland | `Numeric(Byte)` | `%27.0g` |
| `pl_q7h` | Activities out of home: field trip or excursion abroad | `Numeric(Byte)` | `%27.0g` |
| `pl_q7i` | Activities out of home: pilgrimage | `Numeric(Byte)` | `%27.0g` |
| `pl_q7j` | Activities out of home: local picnic | `Numeric(Byte)` | `%27.0g` |
| `pl_q7k` | Activities out of home: opening of an exhibition/poetry reading | `Numeric(Byte)` | `%27.0g` |
| `pl_q7l` | Activities out of home: attending other cultural event | `Numeric(Byte)` | `%27.0g` |
| `pl_q8a` | Meeting with friends at my home | `Numeric(Byte)` | `%27.0g` |
| `pl_q8b` | Meeting with freinds outside home | `Numeric(Byte)` | `%27.0g` |
| `pl_q8c` | Meeting with family members at my home | `Numeric(Byte)` | `%27.0g` |
| `pl_q8d` | Meeting with familiy members outside home | `Numeric(Byte)` | `%27.0g` |
| `pl_q9` | Attending meetings of Third Age University (TAU) | `Numeric(Byte)` | `%12.0g` |
| `pl_q10a` | Reasons for attending TAU: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `pl_q10b` | Reasons for attending TAU: to develop interest | `Numeric(Byte)` | `%12.0g` |
| `pl_q10c` | Reasons for attending TAU: to spend time interentingly | `Numeric(Byte)` | `%12.0g` |
| `pl_q10d` | Reasons for attending TAU: to stop routine of daily life | `Numeric(Byte)` | `%12.0g` |
| `pl_q10e` | Reasons for attending TAU: to improve career perspectives | `Numeric(Byte)` | `%12.0g` |
| `pl_q10f` | Reasons for attending TAU: to maintain activity | `Numeric(Byte)` | `%12.0g` |
| `pl_q10g` | Reasons for attending TAU: to improve relations with generation of (grand-)child | `Numeric(Byte)` | `%12.0g` |
| `pl_q10h` | Reasons for attending TAU: to cope better with own problems | `Numeric(Byte)` | `%12.0g` |
| `pl_q10i` | Reasons for attending TAU: other | `Numeric(Byte)` | `%12.0g` |
| `pl_q11a` | Reasons for NOT attending TAU: not heard about | `Numeric(Byte)` | `%12.0g` |
| `pl_q11b` | Reasons for NOT attending TAU: un-/hardly available | `Numeric(Byte)` | `%12.0g` |
| `pl_q11c` | Reasons for NOT attending TAU: no time due to professional duties | `Numeric(Byte)` | `%12.0g` |
| `pl_q11d` | Reasons for NOT attending TAU: no time due to family duties | `Numeric(Byte)` | `%12.0g` |
| `pl_q11e` | Reasons for NOT attending TAU: not interested | `Numeric(Byte)` | `%12.0g` |
| `pl_q11f` | Reasons for NOT attending TAU: health does not allow attending | `Numeric(Byte)` | `%12.0g` |
| `pl_q11g` | Reasons for NOT attending TAU: too old | `Numeric(Byte)` | `%12.0g` |
| `pl_q11h` | Reasons for NOT attending TAU: other | `Numeric(Byte)` | `%12.0g` |
| `pl_q12a` | Regulary goes to: library | `Numeric(Byte)` | `%12.0g` |
| `pl_q12b` | Regulary goes to: church | `Numeric(Byte)` | `%12.0g` |
| `pl_q12c` | Regulary goes to: choir meetings | `Numeric(Byte)` | `%12.0g` |
| `pl_q12d` | Regulary goes to: discussion club | `Numeric(Byte)` | `%12.0g` |
| `pl_q12e` | Regulary goes to: senior club | `Numeric(Byte)` | `%12.0g` |
| `pl_q12f` | Regulary goes to: local cultural centre | `Numeric(Byte)` | `%12.0g` |
| `pl_q12g` | Regulary goes to: other organized meetings | `Numeric(Byte)` | `%12.0g` |
| `pl_q13` | Participated in language course the last five years | `Numeric(Byte)` | `%12.0g` |
| `pl_q14a` | Year participated in language course: 2011 | `Numeric(Byte)` | `%22.0g` |
| `pl_q14b` | Year participated in language course: 2010 | `Numeric(Byte)` | `%22.0g` |
| `pl_q14c` | Year participated in language course: 2009 | `Numeric(Byte)` | `%22.0g` |
| `pl_q14d` | Year participated in language course: 2008 | `Numeric(Byte)` | `%22.0g` |
| `pl_q14e` | Year participated in language course: 2007 | `Numeric(Byte)` | `%22.0g` |
| `pl_q15a` | Reason participated in language course: supervisor instruction | `Numeric(Byte)` | `%12.0g` |
| `pl_q15b` | Reason participated in language course: desire to improve qualifications | `Numeric(Byte)` | `%12.0g` |
| `pl_q15c` | Reason participated in language course: desire to be promoted | `Numeric(Byte)` | `%12.0g` |
| `pl_q15d` | Reason participated in language course: desire to change job | `Numeric(Byte)` | `%12.0g` |
| `pl_q15e` | Reason participated in language course: desire to find job | `Numeric(Byte)` | `%12.0g` |
| `pl_q15f` | Reason participated in language course: for own pleasure | `Numeric(Byte)` | `%12.0g` |
| `pl_q15g` | Reason participated in language course: other | `Numeric(Byte)` | `%12.0g` |
| `pl_q16a` | Organizer of language course: labour office | `Numeric(Byte)` | `%12.0g` |
| `pl_q16b` | Organizer of language course: employer | `Numeric(Byte)` | `%12.0g` |
| `pl_q16c` | Organizer of language course: centre of culture | `Numeric(Byte)` | `%12.0g` |
| `pl_q16d` | Organizer of language course: training company | `Numeric(Byte)` | `%12.0g` |
| `pl_q16e` | Organizer of language course: Third Age University | `Numeric(Byte)` | `%12.0g` |
| `pl_q16f` | Organizer of language course: language school | `Numeric(Byte)` | `%12.0g` |
| `pl_q16g` | Organizer of language course: other | `Numeric(Byte)` | `%12.0g` |
| `pl_q17a` | Satisfied with language course | `Numeric(Byte)` | `%17.0g` |
| `pl_q17b` | Language course was helpful in work | `Numeric(Byte)` | `%17.0g` |
| `pl_q17c` | Promotion thanks to language course | `Numeric(Byte)` | `%17.0g` |
| `pl_q17d` | Found job thanks to language course | `Numeric(Byte)` | `%17.0g` |
| `pl_q17e` | Changed job thanks to language course | `Numeric(Byte)` | `%17.0g` |
| `pl_q17f` | Achieved new competencies thanks to language course | `Numeric(Byte)` | `%17.0g` |
| `pl_q17g` | Language course was waste of time | `Numeric(Byte)` | `%17.0g` |
| `pl_q17h` | Got signigicant business contacts thanks to language course | `Numeric(Byte)` | `%17.0g` |
| `pl_q17i` | Met new people thanks to language course | `Numeric(Byte)` | `%17.0g` |
| `pl_q18` | Paritcipated in developing competencies training the last five years | `Numeric(Byte)` | `%12.0g` |
| `pl_q19a` | Year paritcipated in developing competencies training: 2011 | `Numeric(Byte)` | `%22.0g` |
| `pl_q19b` | Year paritcipated in developing competencies training: 2010 | `Numeric(Byte)` | `%22.0g` |
| `pl_q19c` | Year paritcipated in developing competencies training: 2009 | `Numeric(Byte)` | `%22.0g` |
| `pl_q19d` | Year paritcipated in developing competencies training: 2008 | `Numeric(Byte)` | `%22.0g` |
| `pl_q19e` | Year paritcipated in developing competencies training: 2007 | `Numeric(Byte)` | `%22.0g` |
| `pl_q20a` | Reason participated in this training: supervisor instruction | `Numeric(Byte)` | `%12.0g` |
| `pl_q20b` | Reason participated in this training: desire to improve qualifications | `Numeric(Byte)` | `%12.0g` |
| `pl_q20c` | Reason participated in this training: desire to be promoted | `Numeric(Byte)` | `%12.0g` |
| `pl_q20d` | Reason participated in this training: desire to change job | `Numeric(Byte)` | `%12.0g` |
| `pl_q20e` | Reason participated in this training: desire to find job | `Numeric(Byte)` | `%12.0g` |
| `pl_q20f` | Reason participated in this training: for own pleasure | `Numeric(Byte)` | `%12.0g` |
| `pl_q20g` | Reason participated in this training: other | `Numeric(Byte)` | `%12.0g` |
| `pl_q21a` | Organizer of this training: labour office | `Numeric(Byte)` | `%12.0g` |
| `pl_q21b` | Organizer of this training: employer | `Numeric(Byte)` | `%12.0g` |
| `pl_q21c` | Organizer of this training: centre of culture | `Numeric(Byte)` | `%12.0g` |
| `pl_q21d` | Organizer of this training: training company | `Numeric(Byte)` | `%12.0g` |
| `pl_q21e` | Organizer of this training: Third Age University | `Numeric(Byte)` | `%12.0g` |
| `pl_q21f` | Organizer of this training: other | `Numeric(Byte)` | `%12.0g` |
| `pl_q22a` | Satisfied with developing competencies training | `Numeric(Byte)` | `%17.0g` |
| `pl_q22b` | Developing competencies training was helpful in work | `Numeric(Byte)` | `%17.0g` |
| `pl_q22c` | Promotion thanks to developing competencies training | `Numeric(Byte)` | `%17.0g` |
| `pl_q22d` | Found job thanks to developing competencies training | `Numeric(Byte)` | `%17.0g` |
| `pl_q22e` | Changed job thanks to developing competencies training | `Numeric(Byte)` | `%17.0g` |
| `pl_q22f` | Achieved new competencies thanks to this training | `Numeric(Byte)` | `%17.0g` |
| `pl_q22g` | Developing competencies training was waste of time | `Numeric(Byte)` | `%17.0g` |
| `pl_q22h` | Got signigicant business contacts thanks to this training | `Numeric(Byte)` | `%17.0g` |
| `pl_q22i` | Met new people thanks to developing competencies training | `Numeric(Byte)` | `%17.0g` |
| `pl_q23a` | Reason for NOT participating in trainings: lack of any trainings | `Numeric(Byte)` | `%12.0g` |
| `pl_q23b` | Reason for NOT participating in trainings: lack of interesting trainings | `Numeric(Byte)` | `%12.0g` |
| `pl_q23c` | Reason for NOT participating in trainings: lack of funding | `Numeric(Byte)` | `%12.0g` |
| `pl_q23d` | Reason for NOT participating in trainings: long commuting time | `Numeric(Byte)` | `%12.0g` |
| `pl_q23e` | Reason for NOT participating in trainings: inconvenient date | `Numeric(Byte)` | `%12.0g` |
| `pl_q23f` | Reason for NOT participating in trainings: lack of time | `Numeric(Byte)` | `%12.0g` |
| `pl_q23g` | Reason for NOT participating in trainings: too expensive | `Numeric(Byte)` | `%12.0g` |
| `pl_q23h` | Reason for NOT participating in trainings: no need | `Numeric(Byte)` | `%12.0g` |
| `pl_q23i` | Reason for NOT participating in trainings: other | `Numeric(Byte)` | `%12.0g` |
| `pl_q24a` | Time for learning is when you're young, then use achieved knowledge in work/life | `Numeric(Byte)` | `%17.0g` |
| `pl_q24b` | After school we learn mainly in work | `Numeric(Byte)` | `%17.0g` |
| `pl_q24c` | Necessary to continue education throughout life, to achieve new competencies | `Numeric(Byte)` | `%17.0g` |
| `pl_q25a` | Highest education level: not completed primary school | `Numeric(Byte)` | `%12.0g` |
| `pl_q25b` | Highest education level: completed 4-class primary school before war | `Numeric(Byte)` | `%12.0g` |
| `pl_q25c` | Highest education level: completed 7 or 8-class primary school | `Numeric(Byte)` | `%12.0g` |
| `pl_q25d` | Highest education level: completed gymnasium | `Numeric(Byte)` | `%12.0g` |
| `pl_q25e` | Highest education level: completed basic vocational school | `Numeric(Byte)` | `%12.0g` |
| `pl_q25f` | Highest education level: completed high school without certificate | `Numeric(Byte)` | `%12.0g` |
| `pl_q25g` | Highest education level: completed high school with certificate | `Numeric(Byte)` | `%12.0g` |
| `pl_q25h` | Highest education level: completed secondary vocational school without certifica | `Numeric(Byte)` | `%12.0g` |
| `pl_q25i` | Highest education level: completed secondary vocational school with certificate | `Numeric(Byte)` | `%12.0g` |
| `pl_q25j` | Highest education level: diploma of graduation from secondary school | `Numeric(Byte)` | `%12.0g` |
| `pl_q25k` | Highest education level: diploma of graduation from teacher training college/stu | `Numeric(Byte)` | `%12.0g` |
| `pl_q25l` | Highest education level: diploma of bachelor/engineer | `Numeric(Byte)` | `%12.0g` |
| `pl_q25m` | Highest education level: master degree/diploma of medicine doctor | `Numeric(Byte)` | `%12.0g` |
| `pl_q25n` | Highest education level: scientific degree of doctor and higher | `Numeric(Byte)` | `%12.0g` |
| `pl_q25o` | Highest education level: other | `Numeric(Byte)` | `%12.0g` |
| `pl_q26af` | Highest education father: not completed primary school | `Numeric(Byte)` | `%12.0g` |
| `pl_q26am` | Highest education mother: not completed primary school | `Numeric(Byte)` | `%12.0g` |
| `pl_q26bf` | Highest education father: completed 4-class primary school before war | `Numeric(Byte)` | `%12.0g` |
| `pl_q26bm` | Highest education mother: completed 4-class primary school before war | `Numeric(Byte)` | `%12.0g` |
| `pl_q26cf` | Highest education father: completed 7 or 8-class primary school | `Numeric(Byte)` | `%12.0g` |
| `pl_q26cm` | Highest education mother: completed 7 or 8-class primary school | `Numeric(Byte)` | `%12.0g` |
| `pl_q26df` | Highest education father: completed gymnasium | `Numeric(Byte)` | `%12.0g` |
| `pl_q26dm` | Highest education mother: completed gymnasium | `Numeric(Byte)` | `%12.0g` |
| `pl_q26ef` | Highest education father: completed basic vocational school | `Numeric(Byte)` | `%12.0g` |
| `pl_q26em` | Highest education mother: completed basic vocational school | `Numeric(Byte)` | `%12.0g` |
| `pl_q26ff` | Highest education father: completed high school without certificate | `Numeric(Byte)` | `%12.0g` |
| `pl_q26fm` | Highest education mother: completed high school without certificate | `Numeric(Byte)` | `%12.0g` |
| `pl_q26gf` | Highest education father: completed high school with certificate | `Numeric(Byte)` | `%12.0g` |
| `pl_q26gm` | Highest education mother: completed high school with certificate | `Numeric(Byte)` | `%12.0g` |
| `pl_q26hf` | Highest education father: completed secondary vocational school without certific | `Numeric(Byte)` | `%12.0g` |
| `pl_q26hm` | Highest education mother: completed secondary vocational school without certific | `Numeric(Byte)` | `%12.0g` |
| `pl_q26if` | Highest education father: completed secondary vocational school with certificate | `Numeric(Byte)` | `%12.0g` |
| `pl_q26im` | Highest education mother: completed secondary vocational school with certificate | `Numeric(Byte)` | `%12.0g` |
| `pl_q26jf` | Highest education father: diploma of graduation from secondary school | `Numeric(Byte)` | `%12.0g` |
| `pl_q26jm` | Highest education mother: diploma of graduation from secondary school | `Numeric(Byte)` | `%12.0g` |
| `pl_q26kf` | Highest education father: diploma of graduation from teacher training college/st | `Numeric(Byte)` | `%12.0g` |
| `pl_q26km` | Highest education mother: diploma of graduation from teacher training college/st | `Numeric(Byte)` | `%12.0g` |
| `pl_q26lf` | Highest education father: diploma of bachelor/engineer | `Numeric(Byte)` | `%12.0g` |
| `pl_q26lm` | Highest education mother: diploma of bachelor/engineer | `Numeric(Byte)` | `%12.0g` |
| `pl_q26mf` | Highest education father: master degree/diploma of medicine doctor | `Numeric(Byte)` | `%12.0g` |
| `pl_q26mm` | Highest education mother: master degree/diploma of medicine doctor | `Numeric(Byte)` | `%12.0g` |
| `pl_q26nf` | Highest education father: scientific degree of doctor and higher | `Numeric(Byte)` | `%12.0g` |
| `pl_q26nm` | Highest education mother: scientific degree of doctor and higher | `Numeric(Byte)` | `%12.0g` |
| `pl_q26of` | Highest education father: other | `Numeric(Byte)` | `%12.0g` |
| `pl_q26om` | Highest education mother: other | `Numeric(Byte)` | `%12.0g` |
| `pt_q6` | Number of medical exams past 6months | `Numeric(Byte)` | `%12.0g` |
| `pt_q7a` | Reason for doing medical exams: you asked | `Numeric(Byte)` | `%12.0g` |
| `pt_q7b` | Reason for doing medical exams: practitioner prescribed it | `Numeric(Byte)` | `%12.0g` |
| `pt_q7c` | Reason for doing medical exams: other reason | `Numeric(Byte)` | `%12.0g` |
| `pt_q8a` | Last month emotional problems affected your regular daily activites/work | `Numeric(Byte)` | `%20.0g` |
| `pt_q8b` | Last month emotional problems affected the way you relate to relatives/friends | `Numeric(Byte)` | `%20.0g` |
| `pt_q9` | How many friends/relatives helped you with your emotional problems | `Numeric(Byte)` | `%12.0g` |
| `pt_q10a` | Pets in hh: dogs | `Numeric(Byte)` | `%12.0g` |
| `pt_q10b` | Pets in hh: cats | `Numeric(Byte)` | `%12.0g` |
| `pt_q10c` | Pets in hh: others | `Numeric(Byte)` | `%12.0g` |
| `pt_q11` | Who decided to have pets | `Numeric(Byte)` | `%28.0g` |
| `pt_q12a` | Reason for adopting a pet: for companion | `Numeric(Byte)` | `%12.0g` |
| `pt_q12b` | Reason for adopting a pet: for protection | `Numeric(Byte)` | `%12.0g` |
| `pt_q12c` | Reason for adopting a pet: other reason | `Numeric(Byte)` | `%12.0g` |
| `pt_q13` | Hours spent with pet on a regular day | `Numeric(Byte)` | `%12.0g` |
| `pt_q14` | Hours walking pet outside in a regular week | `Numeric(Byte)` | `%12.0g` |
| `pt_q15a` | I feel closer to my pet(s) than to many of my friends | `Numeric(Byte)` | `%17.0g` |
| `pt_q15b` | My pet makes me feel loved | `Numeric(Byte)` | `%17.0g` |
| `pt_q15c` | My pet gives me something to talk about with others | `Numeric(Byte)` | `%17.0g` |
| `pt_q15d` | I feel closer to my pet(s) than to other family members | `Numeric(Byte)` | `%17.0g` |
| `pt_q15e` | My pet keeps me from being lonely | `Numeric(Byte)` | `%17.0g` |
| `pt_q15f` | When I am with my pet I feel calmer | `Numeric(Byte)` | `%17.0g` |
| `pt_q15g` | When I am sad my pet helps me feeling better | `Numeric(Byte)` | `%17.0g` |
| `pt_q15h` | There are times when my pet is my closest companion | `Numeric(Byte)` | `%17.0g` |
| `pt_q15i` | Because of my pet I’ve had conflicts/discussions with others | `Numeric(Byte)` | `%17.0g` |
| `pt_q16a` | Reason for not having a pet: has not housing conditions | `Numeric(Byte)` | `%12.0g` |
| `pt_q16b` | Reason for not having a pet: has not financial conditions | `Numeric(Byte)` | `%12.0g` |
| `pt_q16c` | Reason for not having a pet: has not health conditions | `Numeric(Byte)` | `%12.0g` |
| `pt_q16d` | Reason for not having a pet: doesn't like animals | `Numeric(Byte)` | `%12.0g` |
| `pt_q16e` | Reason for not having a pet: other reasons | `Numeric(Byte)` | `%12.0g` |

### `technical_variables` - Technical variables

- Dataset: `sharew4_rel9-0-0_technical_variables.dta`
- Read with: `ps.read_share_module("technical_variables", wave=4)`
- Rows: 57,982
- Variables: 17
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `fam_resp` | Family respondent | `Numeric(Byte)` | `%21.0g` |
| `fin_resp` | Financial respondent | `Numeric(Byte)` | `%24.0g` |
| `hou_resp` | Household respondent | `Numeric(Byte)` | `%24.0g` |
| `mn005_` | Single or couple interview | `Numeric(Byte)` | `%37.0g` |
| `mn016_` | Mother in household | `Numeric(Byte)` | `%11.0g` |
| `mn017_` | Father in household | `Numeric(Byte)` | `%11.0g` |
| `mn018_` | Mother-in-law in household | `Numeric(Byte)` | `%11.0g` |
| `mn019_` | Father-in-law in household | `Numeric(Byte)` | `%11.0g` |
| `mn024_` | Nursing home interview | `Numeric(Byte)` | `%17.0g` |
| `mn026_` | First respondent from couple or single | `Numeric(Byte)` | `%11.0g` |
| `mn101_` | Questionnaire version | `Numeric(Byte)` | `%26.0g` |


## Generated Modules

### `gv_children` - Generated child-level summaries

- Dataset: `sharew4_rel9-0-0_gv_children.dta`
- Read with: `ps.read_share_module("gv_children", wave=4)`
- Rows: 57,982
- Variables: 347
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
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
| `childid_15` | Child identifier (fix across modules and waves): Child 15 | `Str(1)` | `%9s` |
| `childid_16` | Child identifier (fix across modules and waves): Child 16 | `Str(14)` | `%14s` |
| `childid_17` | Child identifier (fix across modules and waves): Child 17 | `Str(1)` | `%9s` |
| `childid_18` | Child identifier (fix across modules and waves): Child 18 | `Str(1)` | `%9s` |
| `childid_19` | Child identifier (fix across modules and waves): Child 19 | `Str(1)` | `%9s` |
| `childid_20` | Child identifier (fix across modules and waves): Child 20 | `Str(1)` | `%9s` |
| `ch001_` | Number of children | `Numeric(Byte)` | `%11.0g` |
| `ch_gender_1` | Child gender, based on ch005_1 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_2` | Child gender, based on ch005_2 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_3` | Child gender, based on ch005_3 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_4` | Child gender, based on ch005_4 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_5` | Child gender, based on ch005_5 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_6` | Child gender, based on ch005_6 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_7` | Child gender, based on ch005_7 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_8` | Child gender, based on ch005_8 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_9` | Child gender, based on ch005_9 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_10` | Child gender, based on ch005_10 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_11` | Child gender, based on ch005_11 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_12` | Child gender, based on ch005_12 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_13` | Child gender, based on ch005_13 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_14` | Child gender, based on ch005_14 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_15` | Child gender, based on ch005_15 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_16` | Child gender, based on ch005_16 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_17` | Child gender, based on ch005_17 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_18` | Child gender, based on ch005_18 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_19` | Child gender, based on ch005_19 | `Numeric(Byte)` | `%10.0g` |
| `ch_gender_20` | Child gender, based on ch005_20 | `Numeric(Byte)` | `%10.0g` |
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
| `ch_yrbirth_15` | Child year of birth, based on ch006_15 | `Numeric(Byte)` | `%10.0g` |
| `ch_yrbirth_16` | Child year of birth, based on ch006_16 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_17` | Child year of birth, based on ch006_17 | `Numeric(Byte)` | `%10.0g` |
| `ch_yrbirth_18` | Child year of birth, based on ch006_18 | `Numeric(Byte)` | `%10.0g` |
| `ch_yrbirth_19` | Child year of birth, based on ch006_19 | `Numeric(Byte)` | `%10.0g` |
| `ch_yrbirth_20` | Child year of birth, based on ch006_20 | `Numeric(Byte)` | `%10.0g` |
| `ch_relation_1` | Relation to child 1, based on ch002_1, ch010_1, ch011_1 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_2` | Relation to child 2, based on ch002_2, ch010_2, ch011_2 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_3` | Relation to child 3, based on ch002_3, ch010_3, ch011_3 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_4` | Relation to child 4, based on ch002_4, ch010_4, ch011_4 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_5` | Relation to child 5, based on ch002_5, ch010_5, ch011_5 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_6` | Relation to child 6, based on ch002_6, ch010_6, ch011_6 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_7` | Relation to child 7, based on ch002_7, ch010_7, ch011_7 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_8` | Relation to child 8, based on ch002_8, ch010_8, ch011_8 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_9` | Relation to child 9, based on ch002_9, ch010_9, ch011_9 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_10` | Relation to child 10, based on ch002_10, ch010_10, ch011_10 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_11` | Relation to child 11, based on ch002_11, ch010_11, ch011_11 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_12` | Relation to child 12, based on ch002_12, ch010_12, ch011_12 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_13` | Relation to child 13, based on ch002_13, ch010_13, ch011_13 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_14` | Relation to child 14, based on ch002_14, ch010_14, ch011_14 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_15` | Relation to child 15, based on ch002_15, ch010_15, ch011_15 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_16` | Relation to child 16, based on ch002_16, ch010_16, ch011_16 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_17` | Relation to child 17, based on ch002_17, ch010_17, ch011_17 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_18` | Relation to child 18, based on ch002_18, ch010_18, ch011_18 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_19` | Relation to child 19, based on ch002_19, ch010_19, ch011_19 | `Numeric(Byte)` | `%43.0g` |
| `ch_relation_20` | Relation to child 20, based on ch002_20, ch010_20, ch011_20 | `Numeric(Byte)` | `%43.0g` |
| `ch_contact_1` | Contact to child 1, based on ch014_1 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_2` | Contact to child 2, based on ch014_2 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_3` | Contact to child 3, based on ch014_3 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_4` | Contact to child 4, based on ch014_4 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_5` | Contact to child 5, based on ch014_5 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_6` | Contact to child 6, based on ch014_6 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_7` | Contact to child 7, based on ch014_7 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_8` | Contact to child 8, based on ch014_8 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_9` | Contact to child 9, based on ch014_9 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_10` | Contact to child 10, based on ch014_10 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_11` | Contact to child 11, based on ch014_11 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_12` | Contact to child 12, based on ch014_12 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_13` | Contact to child 13, based on ch014_13 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_14` | Contact to child 14, based on ch014_14 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_15` | Contact to child 15, based on ch014_15 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_16` | Contact to child 16, based on ch014_16 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_17` | Contact to child 17, based on ch014_17 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_18` | Contact to child 18, based on ch014_18 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_19` | Contact to child 19, based on ch014_19 | `Numeric(Byte)` | `%22.0g` |
| `ch_contact_20` | Contact to child 20, based on ch014_20 | `Numeric(Byte)` | `%22.0g` |
| `ch_proximity_1` | Proximity to child 1, based on ch007_1, ch526_1 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_2` | Proximity to child 2, based on ch007_2, ch526_2 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_3` | Proximity to child 3, based on ch007_3, ch526_3 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_4` | Proximity to child 4, based on ch007_4, ch526_4 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_5` | Proximity to child 5, based on ch007_5, ch526_5 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_6` | Proximity to child 6, based on ch007_6, ch526_6 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_7` | Proximity to child 7, based on ch007_7, ch526_7 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_8` | Proximity to child 8, based on ch007_8, ch526_8 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_9` | Proximity to child 9, based on ch007_9, ch526_9 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_10` | Proximity to child 10, based on ch007_10, ch526_10 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_11` | Proximity to child 11, based on ch007_11, ch526_11 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_12` | Proximity to child 12, based on ch007_12, ch526_12 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_13` | Proximity to child 13, based on ch007_13, ch526_13 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_14` | Proximity to child 14, based on ch007_14, ch526_14 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_15` | Proximity to child 15, based on ch007_15, ch526_15 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_16` | Proximity to child 16, based on ch007_16, ch526_16 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_17` | Proximity to child 17, based on ch007_17, ch526_17 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_18` | Proximity to child 18, based on ch007_18, ch526_18 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_19` | Proximity to child 19, based on ch007_19, ch526_19 | `Numeric(Byte)` | `%48.0g` |
| `ch_proximity_20` | Proximity to child 20, based on ch007_20, ch526_20 | `Numeric(Byte)` | `%48.0g` |
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
| `ch_move_out_year_15` | Year when child 15 moved out, based on ch015_15 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_16` | Year when child 16 moved out, based on ch015_16 | `Numeric(Int)` | `%33.0g` |
| `ch_move_out_year_17` | Year when child 17 moved out, based on ch015_17 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_18` | Year when child 18 moved out, based on ch015_18 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_19` | Year when child 19 moved out, based on ch015_19 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_20` | Year when child 20 moved out, based on ch015_20 | `Numeric(Byte)` | `%33.0g` |
| `ch_marital_status_1` | Marital status of child 1, based on ch012_1 & ch516_1 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_2` | Marital status of child 2, based on ch012_2 & ch516_2 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_3` | Marital status of child 3, based on ch012_3 & ch516_3 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_4` | Marital status of child 4, based on ch012_4 & ch516_4 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_5` | Marital status of child 5, based on ch012_5 & ch516_5 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_6` | Marital status of child 6, based on ch012_6 & ch516_6 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_7` | Marital status of child 7, based on ch012_7 & ch516_7 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_8` | Marital status of child 8, based on ch012_8 & ch516_8 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_9` | Marital status of child 9, based on ch012_9 & ch516_9 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_10` | Marital status of child 10, based on ch012_10 & ch516_10 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_11` | Marital status of child 11, based on ch012_11 & ch516_11 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_12` | Marital status of child 12, based on ch012_12 & ch516_12 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_13` | Marital status of child 13, based on ch012_13 & ch516_13 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_14` | Marital status of child 14, based on ch012_14 & ch516_14 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_15` | Marital status of child 15, based on ch012_15 & ch516_15 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_16` | Marital status of child 16, based on ch012_16 & ch516_16 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_17` | Marital status of child 17, based on ch012_17 & ch516_17 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_18` | Marital status of child 18, based on ch012_18 & ch516_18 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_19` | Marital status of child 19, based on ch012_19 & ch516_19 | `Numeric(Byte)` | `%39.0g` |
| `ch_marital_status_20` | Marital status of child 20, based on ch012_20 & ch516_20 | `Numeric(Byte)` | `%39.0g` |
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
| `ch_occupation_1` | Occupational status of child 1, based on ch016_1 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_2` | Occupational status of child 2, based on ch016_2 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_3` | Occupational status of child 3, based on ch016_3 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_4` | Occupational status of child 4, based on ch016_4 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_5` | Occupational status of child 5, based on ch016_5 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_6` | Occupational status of child 6, based on ch016_6 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_7` | Occupational status of child 7, based on ch016_7 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_8` | Occupational status of child 8, based on ch016_8 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_9` | Occupational status of child 9, based on ch016_9 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_10` | Occupational status of child 10, based on ch016_10 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_11` | Occupational status of child 11, based on ch016_11 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_12` | Occupational status of child 12, based on ch016_12 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_13` | Occupational status of child 13, based on ch016_13 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_14` | Occupational status of child 14, based on ch016_14 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_15` | Occupational status of child 15, based on ch016_15 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_16` | Occupational status of child 16, based on ch016_16 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_17` | Occupational status of child 17, based on ch016_17 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_18` | Occupational status of child 18, based on ch016_18 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_19` | Occupational status of child 19, based on ch016_19 | `Numeric(Byte)` | `%43.0g` |
| `ch_occupation_20` | Occupational status of child 20, based on ch016_20 | `Numeric(Byte)` | `%43.0g` |
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
| `ch_yrbirth_youngest_child_15` | Yrbirth youngest child of child 15, based on ch020_15 & ch520_15 | `Numeric(Byte)` | `%15.0g` |
| `ch_yrbirth_youngest_child_16` | Yrbirth youngest child of child 16, based on ch020_16 & ch520_16 | `Numeric(Int)` | `%15.0g` |
| `ch_yrbirth_youngest_child_17` | Yrbirth youngest child of child 17, based on ch020_17 & ch520_17 | `Numeric(Byte)` | `%15.0g` |
| `ch_yrbirth_youngest_child_18` | Yrbirth youngest child of child 18, based on ch020_18 & ch520_18 | `Numeric(Byte)` | `%15.0g` |
| `ch_yrbirth_youngest_child_19` | Yrbirth youngest child of child 19, based on ch020_19 & ch520_19 | `Numeric(Byte)` | `%15.0g` |
| `ch_yrbirth_youngest_child_20` | Yrbirth youngest child of child 20, based on ch020_20 & ch520_20 | `Numeric(Byte)` | `%15.0g` |
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
| `ch_school_education_1` | School degree of child 1, based on ch017_1 & ch510_1 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_2` | School degree of child 2, based on ch017_2 & ch510_2 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_3` | School degree of child 3, based on ch017_3 & ch510_3 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_4` | School degree of child 4, based on ch017_4 & ch510_4 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_5` | School degree of child 5, based on ch017_5 & ch510_5 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_6` | School degree of child 6, based on ch017_6 & ch510_6 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_7` | School degree of child 7, based on ch017_7 & ch510_7 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_8` | School degree of child 8, based on ch017_8 & ch510_8 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_9` | School degree of child 9, based on ch017_9 & ch510_9 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_10` | School degree of child 10, based on ch017_10 & ch510_10 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_11` | School degree of child 11, based on ch017_11 & ch510_11 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_12` | School degree of child 12, based on ch017_12 & ch510_12 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_13` | School degree of child 13, based on ch017_13 & ch510_13 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_14` | School degree of child 14, based on ch017_14 & ch510_14 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_15` | School degree of child 15, based on ch017_15 & ch510_15 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_16` | School degree of child 16, based on ch017_16 & ch510_16 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_17` | School degree of child 17, based on ch017_17 & ch510_17 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_18` | School degree of child 18, based on ch017_18 & ch510_18 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_19` | School degree of child 19, based on ch017_19 & ch510_19 | `Numeric(Byte)` | `%38.0g` |
| `ch_school_education_20` | School degree of child 20, based on ch017_20 & ch510_20 | `Numeric(Byte)` | `%38.0g` |
| `ch_further_education_1` | Further education of child 1, based on ch018_1_* & ch513_1 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_2` | Further education of child 2, based on ch018_2_* & ch513_2 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_3` | Further education of child 3, based on ch018_3_* & ch513_3 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_4` | Further education of child 4, based on ch018_4_* & ch513_4 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_5` | Further education of child 5, based on ch018_5_* & ch513_5 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_6` | Further education of child 6, based on ch018_6_* & ch513_6 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_7` | Further education of child 7, based on ch018_7_* & ch513_7 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_8` | Further education of child 8, based on ch018_8_* & ch513_8 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_9` | Further education of child 9, based on ch018_9_* & ch513_9 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_10` | Further education of child 10, based on ch018_10_* & ch513_10 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_11` | Further education of child 11, based on ch018_11_* & ch513_11 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_12` | Further education of child 12, based on ch018_12_* & ch513_12 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_13` | Further education of child 13, based on ch018_13_* & ch513_13 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_14` | Further education of child 14, based on ch018_14_* & ch513_14 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_15` | Further education of child 15, based on ch018_15_* & ch513_15 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_16` | Further education of child 16, based on ch018_16_* & ch513_16 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_17` | Further education of child 17, based on ch018_17_* & ch513_17 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_18` | Further education of child 18, based on ch018_18_* & ch513_18 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_19` | Further education of child 19, based on ch018_19_* & ch513_19 | `Numeric(Byte)` | `%100.0g` |
| `ch_further_education_20` | Further education of child 20, based on ch018_20_* & ch513_20 | `Numeric(Byte)` | `%100.0g` |
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

- Dataset: `sharew4_rel9-0-0_gv_exrates.dta`
- Read with: `ps.read_share_module("gv_exrates", wave=4)`
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

- Dataset: `sharew4_rel9-0-0_gv_health.dta`
- Read with: `ps.read_share_module("gv_health", wave=4)`
- Rows: 57,982
- Variables: 45
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `adl` | Number of limitations with activities of daily living (adl) | `Numeric(Byte)` | `%10.0g` |
| `adl2` | 1+ adl limitations | `Numeric(Byte)` | `%18.0g` |
| `bmi` | Body mass index | `Numeric(Float)` | `%28.0g` |
| `bmi2` | Bmi categories | `Numeric(Byte)` | `%27.0g` |
| `casp` | CASP index for quality of life and well-being | `Numeric(Byte)` | `%10.0g` |
| `cf008tot` | Ten words list learning first trial total | `Numeric(Byte)` | `%9.0g` |
| `cf016tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `chronic2w4` | 2+ chronic diseases (w4 version) | `Numeric(Byte)` | `%20.0g` |
| `chronicw4` | Number of chronic diseases (w4 version) | `Numeric(Byte)` | `%10.0g` |
| `cusmoke` | Current smoking | `Numeric(Byte)` | `%40.0g` |
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
| `symptoms2w4` | 2+ symptoms (w4 version) | `Numeric(Byte)` | `%20.0g` |
| `symptomsw4` | Number of symptoms (w4 version) | `Numeric(Byte)` | `%10.0g` |

### `gv_housing` - Housing generated variables

- Dataset: `sharew4_rel9-0-0_gv_housing.dta`
- Read with: `ps.read_share_module("gv_housing", wave=4)`
- Rows: 57,982
- Variables: 11
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `areabldgi` | Area of building | `Numeric(Byte)` | `%38.0g` |
| `typebldgi` | Type of building | `Numeric(Byte)` | `%57.0g` |
| `floorsbli` | Number of floors of building | `Numeric(Byte)` | `%10.0g` |
| `nstepsi` | Number of steps to entrance | `Numeric(Byte)` | `%12.0g` |
| `nuts1_2010` | NUTS 2010 level 1: nomenclature of territorial units for statistics | `Str(30)` | `%30s` |

### `gv_imputations` - Multiple imputations

- Dataset: `sharew4_rel9-0-0_gv_imputations.dta`
- Read with: `ps.read_share_module("gv_imputations", wave=4)`
- Rows: 289,910
- Variables: 236
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
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
| `otrf` | Owner, tenant or rent free | `Numeric(Byte)` | `%32.0g` |
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
| `ypen36` | Disability/sickness pensions/benefits | `Numeric(Double)` | `%9.0g` |
| `ypen4` | Unemployment benefits/insurances | `Numeric(Double)` | `%9.0g` |
| `ypen5` | Social assistance | `Numeric(Double)` | `%9.0g` |
| `ylsp1` | LS payments from old age, early retirement, and survivor pensions | `Numeric(Double)` | `%9.0g` |
| `ylsp2` | LS payments from private and occupational pensions | `Numeric(Double)` | `%9.0g` |
| `ylsp36` | LS payments from disability/sickness pensions/benefits | `Numeric(Double)` | `%9.0g` |
| `ylsp4` | LS payments from unemployment benefits/insurances | `Numeric(Double)` | `%9.0g` |
| `ylsp5` | LS payments from social assistance | `Numeric(Float)` | `%9.0g` |
| `yreg1` | Regular private payments | `Numeric(Double)` | `%9.0g` |
| `yreg2` | Other regular private transfers | `Numeric(Double)` | `%9.0g` |
| `ylsr1` | LS from private payments | `Numeric(Double)` | `%9.0g` |
| `ylsr2` | LS from other private transfers | `Numeric(Double)` | `%9.0g` |
| `home` | Value of main residence | `Numeric(Double)` | `%9.0g` |
| `mort` | Mortgage on main residence | `Numeric(Double)` | `%9.0g` |
| `rhre` | Rent and home-related expenditures | `Numeric(Double)` | `%9.0g` |
| `ores` | Value of other real estate | `Numeric(Double)` | `%9.0g` |
| `ysrent` | Income from rent/sublet | `Numeric(Double)` | `%9.0g` |
| `yaohm` | Income from other household members | `Numeric(Double)` | `%9.0g` |
| `fahc` | Amount spent on food at home | `Numeric(Double)` | `%9.0g` |
| `fohc` | Amount spent on food outside home | `Numeric(Double)` | `%9.0g` |
| `hprf` | Value of home produced food | `Numeric(Double)` | `%9.0g` |
| `bacc` | Bank accounts | `Numeric(Double)` | `%9.0g` |
| `bsmf` | Bond, stock and mutual funds | `Numeric(Double)` | `%9.0g` |
| `slti` | Savings for long-term investments | `Numeric(Double)` | `%9.0g` |
| `vbus` | Value of own business | `Numeric(Double)` | `%9.0g` |
| `sbus` | Share of own business | `Numeric(Float)` | `%9.0g` |
| `car` | Value of cars | `Numeric(Double)` | `%9.0g` |
| `liab` | Financial liabilities | `Numeric(Double)` | `%9.0g` |
| `thinc2` | Total household income - Version B | `Numeric(Double)` | `%9.0g` |
| `thinc` | Total household income - Version A | `Numeric(Double)` | `%9.0g` |
| `thexp` | Total household expenditure | `Numeric(Double)` | `%9.0g` |
| `hnetw` | Household net worth | `Numeric(Double)` | `%9.0g` |
| `ybabsmf` | Interest/dividend from financial assett | `Numeric(Double)` | `%9.0g` |
| `yincnrp` | Income from nonresponding partner | `Numeric(Double)` | `%9.0g` |
| `hrass` | Household real assets | `Numeric(Double)` | `%9.0g` |
| `hgfass` | Household gross financial assets | `Numeric(Double)` | `%9.0g` |
| `hnfass` | Household net financial assets | `Numeric(Double)` | `%9.0g` |
| `gender` | Gender | `Numeric(Byte)` | `%14.0g` |
| `age` | Age | `Numeric(Int)` | `%14.0g` |
| `age_p` | Age of partner | `Numeric(Byte)` | `%14.0g` |
| `yedu` | Years of education | `Numeric(Float)` | `%14.0g` |
| `yedu_p` | Years of education of partner | `Numeric(Float)` | `%14.0g` |
| `isced` | ISCED 1997 coding of education | `Numeric(Byte)` | `%15.0g` |
| `sphus` | Self-perceived health - US scale | `Numeric(Byte)` | `%14.0g` |
| `mstat` | Marital status | `Numeric(Byte)` | `%31.0g` |
| `nchild` | Number of children | `Numeric(Byte)` | `%14.0g` |
| `ngrchild` | Number of grandchildren | `Numeric(Byte)` | `%14.0g` |
| `gali` | Limitation with activities | `Numeric(Byte)` | `%14.0g` |
| `chronic` | Number of chronic deseases | `Numeric(Byte)` | `%14.0g` |
| `symptoms` | Number of symptoms | `Numeric(Byte)` | `%14.0g` |
| `eyesightr` | Eyesight reading | `Numeric(Byte)` | `%14.0g` |
| `hearing` | Hearing | `Numeric(Byte)` | `%14.0g` |
| `bmi` | Body mass index | `Numeric(Double)` | `%14.0g` |
| `weight` | Weight | `Numeric(Double)` | `%14.0g` |
| `height` | Height | `Numeric(Double)` | `%14.0g` |
| `mobility` | Mobility limitations | `Numeric(Byte)` | `%14.0g` |
| `adl` | Limitations with activities of daily living | `Numeric(Byte)` | `%14.0g` |
| `iadl` | Limitations with instrumental activities of daily living | `Numeric(Byte)` | `%14.0g` |
| `esmoked` | Ever smoked daily | `Numeric(Byte)` | `%14.0g` |
| `drinking` | More than 2 glasses of alcohol almost everyday | `Numeric(Byte)` | `%14.0g` |
| `phinact` | Physical inactivity | `Numeric(Byte)` | `%14.0g` |
| `reading` | Self-rated reading skills | `Numeric(Byte)` | `%14.0g` |
| `writing` | Self-rated writing skills | `Numeric(Byte)` | `%14.0g` |
| `orienti` | Score of orientation in time test | `Numeric(Byte)` | `%9.0g` |
| `wllft` | Score of words list learning test - trial 1 | `Numeric(Byte)` | `%14.0g` |
| `wllst` | Score of words list learning test - trial 2 | `Numeric(Byte)` | `%14.0g` |
| `fluency` | Score of verbal fluency test | `Numeric(Byte)` | `%14.0g` |
| `numeracy` | Score of first numeracy test | `Numeric(Byte)` | `%9.0g` |
| `numeracy2` | Score of second numeracy test | `Numeric(Byte)` | `%9.0g` |
| `memory` | Score of memory test | `Numeric(Byte)` | `%9.0g` |
| `maxgrip` | Maximum of grip strength measures | `Numeric(Byte)` | `%14.0g` |
| `eurod` | EURO depression scale | `Numeric(Byte)` | `%14.0g` |
| `doctor` | Seen/Talked to medical doctor | `Numeric(Byte)` | `%10.0g` |
| `hospital` | In hospital last 12 months | `Numeric(Byte)` | `%14.0g` |
| `thospital` | Times being patient in hospital | `Numeric(Byte)` | `%10.0g` |
| `nhospital` | Total nights stayed in hospital | `Numeric(Int)` | `%14.0g` |
| `cjs` | Current job situation | `Numeric(Byte)` | `%62.0g` |
| `pwork` | Did any paid work | `Numeric(Byte)` | `%14.0g` |
| `empstat` | Employee or self-employed | `Numeric(Byte)` | `%17.0g` |
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
| `tppdi` | Third persons present during the interview | `Numeric(Byte)` | `%14.0g` |
| `willans` | Willingness to answer | `Numeric(Byte)` | `%21.0g` |
| `clarif` | Respondent asked for clarifications | `Numeric(Byte)` | `%14.0g` |
| `undersq` | Respondent understood questions | `Numeric(Byte)` | `%14.0g` |
| `hnrsc` | Help needed to read showcards | `Numeric(Byte)` | `%19.0g` |
| `ydip_f` | Earnings from employment - Flag | `Numeric(Byte)` | `%21.0g` |
| `yind_f` | Earnings from self-employment - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen1_f` | Old age, early retirement, and survivor pensions - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen2_f` | Private and occupational pensions - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen36_f` | Disability/sickness pensions/benefits - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen4_f` | Unemployment benefits/insurances - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen5_f` | Social assistance - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsp1_f` | LS payments from old age, early retirement, and survivor pensions - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsp2_f` | LS payments from private and occupational pensions - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsp36_f` | LS payments from disability/sickness pensions/benefits - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsp4_f` | LS payments from unemployment benefits/insurances - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsp5_f` | LS payments from social assistance - Flag | `Numeric(Byte)` | `%21.0g` |
| `yreg1_f` | Regular private payments - Flag | `Numeric(Byte)` | `%21.0g` |
| `yreg2_f` | Other regular private transfers - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsr1_f` | LS from private payments - Flag | `Numeric(Byte)` | `%21.0g` |
| `ylsr2_f` | LS from other private transfers - Flag | `Numeric(Byte)` | `%21.0g` |
| `home_f` | Value of main residence - Flag | `Numeric(Byte)` | `%21.0g` |
| `mort_f` | Mortgage on main residence - Flag | `Numeric(Byte)` | `%21.0g` |
| `rhre_f` | Rent and home-related expenditures - Flag | `Numeric(Byte)` | `%21.0g` |
| `ores_f` | Value of other real estate - Flag | `Numeric(Byte)` | `%21.0g` |
| `ysrent_f` | Income from rent/sublet - Flag | `Numeric(Byte)` | `%21.0g` |
| `yaohm_f` | Income from other household members - Flag | `Numeric(Byte)` | `%21.0g` |
| `fahc_f` | Amount spent on food at home - Flag | `Numeric(Byte)` | `%21.0g` |
| `fohc_f` | Amount spent on food outside home - Flag | `Numeric(Byte)` | `%21.0g` |
| `hprf_f` | Value of home produced food - Flag | `Numeric(Byte)` | `%21.0g` |
| `bacc_f` | Bank accounts - Flag | `Numeric(Byte)` | `%21.0g` |
| `bsmf_f` | Bond, stock and mutual funds - Flag | `Numeric(Byte)` | `%21.0g` |
| `slti_f` | Savings for long-term investments - Flag | `Numeric(Byte)` | `%21.0g` |
| `vbus_f` | Value of own business - Flag | `Numeric(Byte)` | `%21.0g` |
| `sbus_f` | Share of own business - Flag | `Numeric(Byte)` | `%21.0g` |
| `car_f` | Value of cars - Flag | `Numeric(Byte)` | `%21.0g` |
| `liab_f` | Financial liabilities - Flag | `Numeric(Byte)` | `%21.0g` |
| `thinc2_f` | Total household income - Version B - Flag | `Numeric(Byte)` | `%21.0g` |
| `ybabsmf_f` | Interest/dividend from financial assett - Flag | `Numeric(Byte)` | `%20.0g` |
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
| `symptoms_f` | Number of symptoms - Flag | `Numeric(Byte)` | `%20.0g` |
| `eyesightr_f` | Eyesight reading - Flag | `Numeric(Byte)` | `%20.0g` |
| `hearing_f` | Hearing - Flag | `Numeric(Byte)` | `%20.0g` |
| `bmi_f` | Body mass index - Flag | `Numeric(Byte)` | `%20.0g` |
| `weight_f` | Weight - Flag | `Numeric(Byte)` | `%20.0g` |
| `height_f` | Height - Flag | `Numeric(Byte)` | `%20.0g` |
| `mobility_f` | Mobility limitations - Flag | `Numeric(Byte)` | `%20.0g` |
| `adl_f` | Limitations with activities of daily living - Flag | `Numeric(Byte)` | `%20.0g` |
| `iadl_f` | Limitations with instrumental activities of daily living - Flag | `Numeric(Byte)` | `%20.0g` |
| `esmoked_f` | Ever smoked daily - Flag | `Numeric(Byte)` | `%20.0g` |
| `drinking_f` | More than 2 glasses of alcohol almost everyday - Flag | `Numeric(Byte)` | `%20.0g` |
| `phinact_f` | Physical inactivity - Flag | `Numeric(Byte)` | `%20.0g` |
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
| `tppdi_f` | Third persons present during the interview - Flag | `Numeric(Byte)` | `%20.0g` |
| `willans_f` | Willingness to answer - Flag | `Numeric(Byte)` | `%20.0g` |
| `clarif_f` | Respondent asked for clarifications - Flag | `Numeric(Byte)` | `%20.0g` |
| `undersq_f` | Respondent understood questions - Flag | `Numeric(Byte)` | `%20.0g` |
| `hnrsc_f` | Help needed to read showcards â€“ Flag | `Numeric(Byte)` | `%20.0g` |
| `currency` | currency | `Str(16)` | `%16s` |
| `nomx2010` | Nominal exchange rate (national currency/Euro), annual average, 2010 | `Numeric(Double)` | `%10.0g` |
| `nomx2011` | Nominal exchange rate (national currency/Euro), annual average, 2011 | `Numeric(Double)` | `%10.0g` |
| `nomx2012` | Nominal exchange rate (national currency/Euro), annual average, 2012 | `Numeric(Double)` | `%10.0g` |
| `pppc2010` | Current PPP exchange rate (national currency/Euro), 2010 | `Numeric(Double)` | `%10.0g` |
| `pppc2011` | Current PPP exchange rate (national currency/Euro), 2011 | `Numeric(Double)` | `%10.0g` |
| `pppc2012` | Current PPP exchange rate (national currency/Euro), 2012 | `Numeric(Double)` | `%10.0g` |
| `pppk2010` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2010 | `Numeric(Double)` | `%10.0g` |
| `pppk2011` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2011 | `Numeric(Double)` | `%10.0g` |
| `pppk2012` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2012 | `Numeric(Double)` | `%10.0g` |

### `gv_isced` - ISCED education recodes

- Dataset: `sharew4_rel9-0-0_gv_isced.dta`
- Read with: `ps.read_share_module("gv_isced", wave=4)`
- Rows: 57,982
- Variables: 28
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `isced1997_r` | Respondent: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_sp` | Spouse/ex-spouse of respondent: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
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

### `gv_networks` - Generated social network variables

- Dataset: `sharew4_rel9-0-0_gv_networks.dta`
- Read with: `ps.read_share_module("gv_networks", wave=4)`
- Rows: 57,982
- Variables: 102
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `famnet` | Family members in SN - Count | `Numeric(Byte)` | `%14.0g` |
| `famnet2` | Family members in SN - Dummy | `Numeric(Byte)` | `%23.0g` |
| `famnet3` | Family members in SN - Percentage of SN | `Numeric(Float)` | `%14.0g` |
| `womennet` | Number of women in SN | `Numeric(Byte)` | `%14.0g` |
| `womennet2` | Women in SN - Dummy | `Numeric(Byte)` | `%14.0g` |
| `womennet3` | Women in SN - Percentage of SN | `Numeric(Float)` | `%14.0g` |
| `mennet` | Number of men in SN | `Numeric(Byte)` | `%14.0g` |
| `mennet2` | Men in SN - Dummy | `Numeric(Byte)` | `%14.0g` |
| `mennet3` | Men in SN - Percentage of SN | `Numeric(Float)` | `%14.0g` |
| `childnet` | Children in SN - Count | `Numeric(Byte)` | `%14.0g` |
| `childnet2` | Children in SN - Dummy | `Numeric(Byte)` | `%17.0g` |
| `childnet3` | Children in SN - Percentage of SN | `Numeric(Float)` | `%14.0g` |
| `gchildnet` | Grandchildren in SN - Count | `Numeric(Byte)` | `%14.0g` |
| `gchildnet2` | Grandchildren in SN - Dummy | `Numeric(Byte)` | `%22.0g` |
| `gchildnet3` | Grandchildren in SN - Percentage of SN | `Numeric(Float)` | `%14.0g` |
| `spousenet2` | Spouse/partner in SN - Dummy | `Numeric(Byte)` | `%23.0g` |
| `spousenet3` | Spouse/partner in SN - Percentage of SN | `Numeric(Float)` | `%14.0g` |
| `partner` | Relationship status, info from waves 1,2,4 | `Numeric(Byte)` | `%37.0g` |
| `siblingnet` | Siblings in SN - Count | `Numeric(Byte)` | `%14.0g` |
| `siblingnet2` | Sibling in SN - Dummy | `Numeric(Byte)` | `%16.0g` |
| `siblingnet3` | Sibling in SN - Percentage of SN | `Numeric(Float)` | `%14.0g` |
| `parentnet` | Parents in SN - Count | `Numeric(Byte)` | `%14.0g` |
| `parentnet2` | Parent in SN - Dummy | `Numeric(Byte)` | `%15.0g` |
| `parentnet3` | Parent in SN - Percentage of SN | `Numeric(Float)` | `%14.0g` |
| `friendnet` | Friends in SN - Count | `Numeric(Byte)` | `%14.0g` |
| `friendnet2` | Friends in SN - Dummy | `Numeric(Byte)` | `%16.0g` |
| `friendnet3` | Friends in SN - Percentage of SN | `Numeric(Float)` | `%14.0g` |
| `formalnet` | Formal helpers in SN - Count | `Numeric(Byte)` | `%14.0g` |
| `formalnet2` | Formal helpers in SN - Dummy | `Numeric(Byte)` | `%23.0g` |
| `formalnet3` | Formal helpers in SN - Percentage of SN | `Numeric(Float)` | `%14.0g` |
| `othernet` | Others in SN - Count | `Numeric(Byte)` | `%14.0g` |
| `othernet2` | Others in SN - Dummy | `Numeric(Byte)` | `%15.0g` |
| `othernet3` | Others in SN - Percentage of SN | `Numeric(Float)` | `%14.0g` |
| `prx_mean` | SN proximity - Average | `Numeric(Float)` | `%14.0g` |
| `most_prx` | Proximity of closest SN member | `Numeric(Byte)` | `%14.0g` |
| `prx_5km` | Number of SN members within 5km | `Numeric(Byte)` | `%14.0g` |
| `prx_5km3` | Percentage of SN - 5km or less proximity | `Numeric(Float)` | `%14.0g` |
| `prx_1km` | Number of SN members within 1km | `Numeric(Byte)` | `%14.0g` |
| `prx_1km3` | Percentage of SN - 1km or less proximity | `Numeric(Float)` | `%14.0g` |
| `contact_mean` | SN contact - Average | `Numeric(Float)` | `%22.0g` |
| `most_contact` | Contact with most contacted SN member | `Numeric(Byte)` | `%22.0g` |
| `daily_contact` | Number of SN members with daily contact | `Numeric(Byte)` | `%14.0g` |
| `daily_contact3` | Percentage of SN with daily contact | `Numeric(Float)` | `%14.0g` |
| `week_contact` | Number of SN members with weekly or more contact | `Numeric(Byte)` | `%14.0g` |
| `week_contact3` | Percentage of SN with weekly or more contact | `Numeric(Float)` | `%14.0g` |
| `month_contact` | Number of SN members with monthly or less contact | `Numeric(Byte)` | `%14.0g` |
| `month_contact3` | Percentage of SN with monthly or less contact | `Numeric(Float)` | `%14.0g` |
| `fam_contact` | Average contact with family members in SN | `Numeric(Float)` | `%22.0g` |
| `child_contact` | Average contact with children in SN | `Numeric(Float)` | `%22.0g` |
| `gchild_contact` | Average contact with grandchildren in SN | `Numeric(Float)` | `%22.0g` |
| `spouse_contact` | Average contact with spouse in SN | `Numeric(Byte)` | `%22.0g` |
| `sibling_contact` | Average contact with siblings in SN | `Numeric(Float)` | `%22.0g` |
| `parent_contact` | Average contact with parents in SN | `Numeric(Float)` | `%22.0g` |
| `friend_contact` | Average contact with friends in SN | `Numeric(Float)` | `%22.0g` |
| `formal_contact` | Average contact with formal helpders in SN | `Numeric(Float)` | `%22.0g` |
| `other_contact` | Average contact with others in SN | `Numeric(Float)` | `%22.0g` |
| `close_mean` | SN emotional closeness - Average | `Numeric(Float)` | `%15.0g` |
| `most_close` | Emotional closeness of closest SN member | `Numeric(Byte)` | `%15.0g` |
| `very_close` | Number of SN - Very to extrememly close | `Numeric(Byte)` | `%14.0g` |
| `very_close3` | Percentage of SN - Very to extremely close | `Numeric(Float)` | `%14.0g` |
| `not_close` | Number of SN - Somewhat close or less | `Numeric(Byte)` | `%14.0g` |
| `not_close3` | Percentage of SN - Somewhat close or less | `Numeric(Float)` | `%14.0g` |
| `fin_gave` | Number of persons fin. help was given to (250 or more) | `Numeric(Byte)` | `%14.0g` |
| `fin_gave2` | Gave financial help - Dummy | `Numeric(Byte)` | `%14.0g` |
| `snfin_gave` | Number of SN members fin. help was given to (250 or more) | `Numeric(Byte)` | `%14.0g` |
| `snfin_gave2` | Gave financial help to SN member(s) - Dummy | `Numeric(Byte)` | `%27.0g` |
| `fin_received` | Number of persons fin. help was received from (250 or more) | `Numeric(Byte)` | `%14.0g` |
| `fin_received2` | Received financial help - Dummy | `Numeric(Byte)` | `%16.0g` |
| `snfin_received` | Number of SN members fin. help was received from (250 or more) | `Numeric(Byte)` | `%14.0g` |
| `snfin_received2` | Received financial help from SN member(s) - Dummy | `Numeric(Byte)` | `%32.0g` |
| `gift_received` | Number of persons fin. gift was received from (5000 or more) | `Numeric(Byte)` | `%14.0g` |
| `gift_received2` | Received financial gift - Dummy | `Numeric(Byte)` | `%16.0g` |
| `sngift_received` | Number of SN members fin. gift was received from (5000 or more) | `Numeric(Byte)` | `%14.0g` |
| `sngift_received2` | Received financial gift from SN member(s) - Dummy | `Numeric(Byte)` | `%42.0g` |
| `gift_gave` | Number of persons fin. gift was given to (5000 or more) | `Numeric(Byte)` | `%14.0g` |
| `gift_gave2` | Gave financial gift - Dummy | `Numeric(Byte)` | `%14.0g` |
| `sngift_gave` | Number of SN members fin. gift was given to (5000 or more) | `Numeric(Byte)` | `%14.0g` |
| `sngift_gave2` | Gave financial gift to SN member(s) - Dummy | `Numeric(Byte)` | `%37.0g` |
| `outhh_receive_care` | Received personal/practical help from person(s) outside hh - Count | `Numeric(Byte)` | `%14.0g` |
| `outhh_receive_care2` | Received personal/practical help from person(s) outside hh - Dummy | `Numeric(Byte)` | `%16.0g` |
| `outhh_snreceive_care` | Received personal/practical help from sn member(s) outside hh - Count | `Numeric(Byte)` | `%14.0g` |
| `outhh_snreceive_care2` | Received personal/practical help from sn member(s) outhh - Dummy | `Numeric(Byte)` | `%32.0g` |
| `outhh_gave_care` | Gave personal/practical help to person(s) outside hh - Count | `Numeric(Byte)` | `%14.0g` |
| `outhh_gave_care2` | Gave Personal/Practical Help to person outside hh - Dummy | `Numeric(Byte)` | `%14.0g` |
| `outhh_sngave_care` | Gave personal/practical help to SN member(s) outhh - Count | `Numeric(Byte)` | `%14.0g` |
| `outhh_sngave_care2` | Gave personal/practical help to SN member(s) outside hh - Dummy | `Numeric(Byte)` | `%27.0g` |
| `hh_gave_care` | Gave personal help to person(s) inside hh - Count | `Numeric(Byte)` | `%14.0g` |
| `hh_gave_care2` | Gave personal help person inside HH - Dummy | `Numeric(Byte)` | `%14.0g` |
| `hh_sngave_care` | Gave personal help to SN member(s) inside HH - Count | `Numeric(Byte)` | `%14.0g` |
| `hh_sngave_care2` | Gave personal help to SN member(s) inside HH - Dummy | `Numeric(Byte)` | `%27.0g` |
| `hh_receive_care` | Received personal help person inside HH - Count | `Numeric(Byte)` | `%14.0g` |
| `hh_receive_care2` | Received personal help person inside HH - Dummy | `Numeric(Byte)` | `%16.0g` |
| `hh_snreceive_care` | Received personal help from SN member(s) inside HH - Count | `Numeric(Byte)` | `%14.0g` |
| `hh_snreceive_care2` | Received personal help from SN member(s) inside HH - Dummy | `Numeric(Byte)` | `%32.0g` |
| `sizeofsocialnetwork` | Sec_SN. Size of social network | `Numeric(Byte)` | `%11.0g` |
| `sn_satisfaction` | Social network satisfaction - Combined sn012_ & sn017_ | `Numeric(Byte)` | `%23.0g` |

### `gv_ssw` - Social security wealth

- Dataset: `sharew4_rel9-0-0_gv_ssw.dta`
- Read with: `ps.read_share_module("gv_ssw", wave=4)`
- Rows: 57,982
- Variables: 8
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `SSW_gw` | Social security wealth (based on approx. gross wage) | `Numeric(Float)` | `%9.0g` |
| `SSW_nw` | Social security wealth (based on net wage) | `Numeric(Float)` | `%9.0g` |

### `gv_weights` - Cross-sectional weights

- Dataset: `sharew4_rel9-0-0_gv_weights.dta`
- Read with: `ps.read_share_module("gv_weights", wave=4)`
- Rows: 57,982
- Variables: 14
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid4` | Household identifier (wave 4) | `Str(11)` | `%11s` |
| `mergeidp4` | Partner identifier (wave 4) | `Str(12)` | `%12s` |
| `coupleid4` | Couple identifier (wave 4) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `dw_w4` | Design weight - wave 4 | `Numeric(Double)` | `%10.0g` |
| `cchw_w4` | Calibrated cross-sectional household weight - wave 4 | `Numeric(Double)` | `%10.0g` |
| `cciw_w4` | Calibrated cross-sectional individual weight - wave 4 | `Numeric(Double)` | `%10.0g` |
| `subsample` | Indicator for country-specific subsample | `Str(6)` | `%9s` |
| `stratum1` | Indicator for primary stratum (if any) | `Str(9)` | `%9s` |
| `stratum2` | Indicator for secondary stratum (if any) | `Str(6)` | `%9s` |
| `psu` | Primary sampling unit | `Str(11)` | `%11s` |
| `ssu` | Secondary sampling unit (if any) | `Str(13)` | `%13s` |
