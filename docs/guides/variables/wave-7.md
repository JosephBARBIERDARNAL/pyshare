---
icon: lucide/list-tree
---

# Wave 7 Variable Dictionary

This page is generated from the local SHARE wave 7 release `9-0-0` Stata files.

It covers 43 datasets and 8,415 variable entries for the files currently available in `data/`.

[Back to variable dictionary](./index.md)

## Overview

| Module | Category | Meaning | Key | Variables | Rows | File |
| --- | --- | --- | --- | --- | --- | --- |
| `ac` | core | Activities | `mergeid` | 48 | 77,181 | `sharew7_rel9-0-0_ac.dta` |
| `as` | core | Assets | `mergeid` | 95 | 77,181 | `sharew7_rel9-0-0_as.dta` |
| `br` | core | Behavioural Risks | `mergeid` | 25 | 77,181 | `sharew7_rel9-0-0_br.dta` |
| `cf` | core | Cognitive Function | `mergeid` | 37 | 77,181 | `sharew7_rel9-0-0_cf.dta` |
| `ch` | core | Children | `mergeid` | 1,616 | 77,181 | `sharew7_rel9-0-0_ch.dta` |
| `co` | core | Consumption | `mergeid` | 29 | 77,181 | `sharew7_rel9-0-0_co.dta` |
| `cv_r` | core | Coverscreen on individual level | `mergeid` | 31 | 111,529 | `sharew7_rel9-0-0_cv_r.dta` |
| `dn` | core | Demographics | `mergeid` | 95 | 77,181 | `sharew7_rel9-0-0_dn.dta` |
| `ep` | core | Employment and Pensions | `mergeid` | 436 | 77,181 | `sharew7_rel9-0-0_ep.dta` |
| `ex` | core | Expectations | `mergeid` | 26 | 77,181 | `sharew7_rel9-0-0_ex.dta` |
| `ft` | core | Financial Transfers | `mergeid` | 69 | 77,181 | `sharew7_rel9-0-0_ft.dta` |
| `gs` | core | Grip Strength | `mergeid` | 23 | 77,181 | `sharew7_rel9-0-0_gs.dta` |
| `hc` | core | Health Care | `mergeid` | 71 | 77,181 | `sharew7_rel9-0-0_hc.dta` |
| `hh` | core | Household Income | `mergeid` | 24 | 77,181 | `sharew7_rel9-0-0_hh.dta` |
| `ho` | core | Housing | `mergeid` | 79 | 77,181 | `sharew7_rel9-0-0_ho.dta` |
| `it` | core | Computer Use | `mergeid` | 10 | 77,181 | `sharew7_rel9-0-0_it.dta` |
| `iv` | core | Interviewer Observations | `mergeid` | 27 | 77,181 | `sharew7_rel9-0-0_iv.dta` |
| `mh` | core | Mental Health | `mergeid` | 27 | 77,181 | `sharew7_rel9-0-0_mh.dta` |
| `ph` | core | Physical Health | `mergeid` | 196 | 77,181 | `sharew7_rel9-0-0_ph.dta` |
| `sp` | core | Social Support | `mergeid` | 161 | 77,181 | `sharew7_rel9-0-0_sp.dta` |
| `xt` | core | End-of-Life Interview | `mergeid` | 221 | 3,661 | `sharew7_rel9-0-0_xt.dta` |
| `dropoff` | special | Paper-and-pencil drop-off | `mergeid` | 809 | 24,677 | `sharew7_rel9-0-0_dropoff.dta` |
| `technical_variables` | special | Technical variables | `mergeid` | 17 | 77,181 | `sharew7_rel9-0-0_technical_variables.dta` |
| `cc` | sharelife | Childhood Circumstances | `mergeid` | 46 | 77,181 | `sharew7_rel9-0-0_cc.dta` |
| `dq` | sharelife | Disability | `mergeid` | 255 | 77,181 | `sharew7_rel9-0-0_dq.dta` |
| `fs` | sharelife | Financial Section | `mergeid` | 17 | 77,181 | `sharew7_rel9-0-0_fs.dta` |
| `gl` | sharelife | General Life and Persecution | `mergeid` | 92 | 77,181 | `sharew7_rel9-0-0_gl.dta` |
| `hs` | sharelife | Health History / Health Section | `mergeid` | 139 | 77,181 | `sharew7_rel9-0-0_hs.dta` |
| `ra` | sharelife | Retrospective Accommodation | `mergeid` | 707 | 77,181 | `sharew7_rel9-0-0_ra.dta` |
| `rc` | sharelife | Retrospective Children History | `mergeid` | 400 | 77,181 | `sharew7_rel9-0-0_rc.dta` |
| `re` | sharelife | Retrospective Employment | `mergeid` | 567 | 77,181 | `sharew7_rel9-0-0_re.dta` |
| `rh` | sharelife | Retrospective Health Care | `mergeid` | 106 | 77,181 | `sharew7_rel9-0-0_rh.dta` |
| `rp` | sharelife | Retrospective Partner History | `mergeid` | 139 | 77,181 | `sharew7_rel9-0-0_rp.dta` |
| `wq` | sharelife | Work Quality | `mergeid` | 276 | 77,181 | `sharew7_rel9-0-0_wq.dta` |
| `gv_big5` | generated | Big Five traits | `mergeid` | 11 | 77,181 | `sharew7_rel9-0-0_gv_big5.dta` |
| `gv_children` | generated | Generated child-level summaries | `mergeid` | 907 | 77,181 | `sharew7_rel9-0-0_gv_children.dta` |
| `gv_exrates` | generated | Exchange rates and PPP variables | `country` | 76 | 29 | `sharew7_rel9-0-0_gv_exrates.dta` |
| `gv_health` | generated | Generated health indicators | `mergeid` | 43 | 77,181 | `sharew7_rel9-0-0_gv_health.dta` |
| `gv_housing` | generated | Housing generated variables | `mergeid` | 10 | 77,181 | `sharew7_rel9-0-0_gv_housing.dta` |
| `gv_imputations` | generated | Multiple imputations | `mergeid` | 280 | 385,905 | `sharew7_rel9-0-0_gv_imputations.dta` |
| `gv_isced` | generated | ISCED education recodes | `mergeid` | 54 | 77,181 | `sharew7_rel9-0-0_gv_isced.dta` |
| `gv_weights` | generated | Cross-sectional weights | `mergeid` | 20 | 77,181 | `sharew7_rel9-0-0_gv_weights.dta` |
| `interviewer_survey` | auxiliary | Interviewer Survey | `intid` | 98 | 1,118 | `sharew7_rel9-0-0_interviewer_survey.dta` |

## Core Interview Modules

### `ac` - Activities

- Dataset: `sharew7_rel9-0-0_ac.dta`
- Read with: `ps.read_share_module("ac", wave=7)`
- Rows: 77,181
- Variables: 48
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ac012_` | How satisfied with life | `Numeric(Byte)` | `%10.0g` |
| `ac014_` | Age prevents from doing things | `Numeric(Byte)` | `%10.0g` |
| `ac015_` | Out of control | `Numeric(Byte)` | `%10.0g` |
| `ac016_` | Feel left out of things | `Numeric(Byte)` | `%10.0g` |
| `ac017_` | Do the things you want to do | `Numeric(Byte)` | `%10.0g` |
| `ac018_` | Family responsibilities prevent | `Numeric(Byte)` | `%10.0g` |
| `ac019_` | Shortage of money stops | `Numeric(Byte)` | `%10.0g` |
| `ac020_` | Look forward to each day | `Numeric(Byte)` | `%10.0g` |
| `ac021_` | Life has meaning | `Numeric(Byte)` | `%10.0g` |
| `ac022_` | Look back on life with happiness | `Numeric(Byte)` | `%10.0g` |
| `ac023_` | Feel full of energy | `Numeric(Byte)` | `%10.0g` |
| `ac024_` | Full of opportunities | `Numeric(Byte)` | `%10.0g` |
| `ac025_` | Future looks good | `Numeric(Byte)` | `%10.0g` |
| `ac035d1` | Activities in last year: done voluntary or charity work | `Numeric(Byte)` | `%12.0g` |
| `ac035d4` | Activities in last year: attended an educational or training course | `Numeric(Byte)` | `%12.0g` |
| `ac035d5` | Activities in last year: gone to a sport, social or other kind of club | `Numeric(Byte)` | `%12.0g` |
| `ac035d7` | Activities in last year: taken part in a political or community-related organiza | `Numeric(Byte)` | `%12.0g` |
| `ac035d8` | Activities in last year: read books, magazines or newspapers | `Numeric(Byte)` | `%12.0g` |
| `ac035d9` | Activities in last year: did word or number games (crossword puzzles/Sudoku...) | `Numeric(Byte)` | `%12.0g` |
| `ac035d10` | Activities in last year: played cards or games such as chess | `Numeric(Byte)` | `%12.0g` |
| `ac035dno` | Activities in last year: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac036_1` | How often done voluntary/charity work the last 12 months | `Numeric(Byte)` | `%18.0g` |
| `ac036_4` | How often attended an educational or training course the last 12 months | `Numeric(Byte)` | `%18.0g` |
| `ac036_5` | How often gone to a sport/social/other kind of club the last 12 months | `Numeric(Byte)` | `%18.0g` |
| `ac036_7` | How often taken part in a political/community-related organization the last 12 m | `Numeric(Byte)` | `%18.0g` |
| `ac036_8` | How often read books, magazines or newspapers the last 12 months | `Numeric(Byte)` | `%18.0g` |
| `ac036_9` | How often did word or number games the last 12 months | `Numeric(Byte)` | `%18.0g` |
| `ac036_10` | How often played cards or games such as chess the last 12 months | `Numeric(Byte)` | `%18.0g` |
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
| `ac740_` | Who answered questions in ac | `Numeric(Byte)` | `%59.0g` |

### `as` - Assets

- Dataset: `sharew7_rel9-0-0_as.dta`
- Read with: `ps.read_share_module("as", wave=7)`
- Rows: 77,181
- Variables: 95
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `as003e` | Amount bank account | `Numeric(Float)` | `%10.0g` |
| `as003ub` | Amount bank account ub | `Numeric(Byte)` | `%32.0g` |
| `as003v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `as003v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as003v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as007e` | Amount in bonds | `Numeric(Float)` | `%10.0g` |
| `as007ub` | Amount in bonds ub | `Numeric(Byte)` | `%32.0g` |
| `as007v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as007v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as007v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as011e` | Amount in stocks | `Numeric(Float)` | `%10.0g` |
| `as011ub` | Amount in stocks ub | `Numeric(Byte)` | `%32.0g` |
| `as011v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `as011v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as011v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `as017e` | Amount in mutual funds | `Numeric(Float)` | `%10.0g` |
| `as017ub` | Amount in mutual funds ub | `Numeric(Byte)` | `%32.0g` |
| `as017v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as017v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as017v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `as019_` | Mutual funds mostly stocks or bonds | `Numeric(Byte)` | `%29.0g` |
| `as020_` | Who has individual retirement accounts | `Numeric(Byte)` | `%25.0g` |
| `as021e` | Amount individual retirement accounts | `Numeric(Float)` | `%10.0g` |
| `as021ub` | Amount individual retirement accounts ub | `Numeric(Byte)` | `%32.0g` |
| `as021v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as021v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as021v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as023_` | Individual retirement accounts mostly in stocks or bonds | `Numeric(Byte)` | `%29.0g` |
| `as024e` | Partner amount individual retirement accounts | `Numeric(Float)` | `%10.0g` |
| `as024ub` | Partner amount individual retirement accounts ub | `Numeric(Byte)` | `%32.0g` |
| `as024v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as024v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as024v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as026_` | Partner individual retirement accounts mostly in stocks or bonds | `Numeric(Byte)` | `%29.0g` |
| `as027e` | Amount contractual saving for housing | `Numeric(Float)` | `%10.0g` |
| `as027ub` | Amount contractual saving for housing ub | `Numeric(Byte)` | `%32.0g` |
| `as027v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as027v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as027v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as029_` | Life insurance policies term or whole life | `Numeric(Byte)` | `%20.0g` |
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
| `as051v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
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
| `as057_` | Who answered the question in as | `Numeric(Byte)` | `%44.0g` |
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
| `as070v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `as641_` | Own firm/company/business (entirely or partial ownership) | `Numeric(Byte)` | `%10.0g` |
| `as642e` | Amount selling firm | `Numeric(Float)` | `%10.0g` |
| `as642ub` | Amount selling firm ub | `Numeric(Byte)` | `%32.0g` |
| `as642v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `as642v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as642v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as649_` | Number of cars | `Numeric(Byte)` | `%10.0g` |

### `br` - Behavioural Risks

- Dataset: `sharew7_rel9-0-0_br.dta`
- Read with: `ps.read_share_module("br", wave=7)`
- Rows: 77,181
- Variables: 25
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
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
| `br015_` | Sports or activities that are vigorous | `Numeric(Byte)` | `%28.0g` |
| `br016_` | Activities requiring a moderate level of energy | `Numeric(Byte)` | `%28.0g` |
| `br017_` | Who answered the questions in br | `Numeric(Byte)` | `%44.0g` |
| `br026_` | How often serving of dairy products | `Numeric(Byte)` | `%31.0g` |
| `br027_` | How often serving of legumes or eggs | `Numeric(Byte)` | `%31.0g` |
| `br028_` | How often serving of meat, fish or chicken | `Numeric(Byte)` | `%31.0g` |
| `br029_` | How often serving of fruits or vegetables | `Numeric(Byte)` | `%31.0g` |
| `br033_` | Not eating meat, fish or chicken more often because ... | `Numeric(Byte)` | `%70.0g` |
| `br039_` | At least one alcoholic beverage the last 7 days | `Numeric(Byte)` | `%10.0g` |
| `br040_` | Units of alcoholic beverage the last seven days | `Numeric(Int)` | `%10.0g` |
| `br623_` | How often 6 or more drinks the last 3 months | `Numeric(Byte)` | `%45.0g` |

### `cf` - Cognitive Function

- Dataset: `sharew7_rel9-0-0_cf.dta`
- Read with: `ps.read_share_module("cf", wave=7)`
- Rows: 77,181
- Variables: 37
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `cf001_` | Self-rated reading skills | `Numeric(Byte)` | `%13.0g` |
| `cf002_` | Self-rated writing skills | `Numeric(Byte)` | `%13.0g` |
| `cf003_` | Date: day of month | `Numeric(Byte)` | `%47.0g` |
| `cf004_` | Date: month | `Numeric(Byte)` | `%47.0g` |
| `cf005_` | Date: year | `Numeric(Byte)` | `%45.0g` |
| `cf006_` | Date: day of the week | `Numeric(Byte)` | `%55.0g` |
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
| `cf103_` | Memory | `Numeric(Byte)` | `%13.0g` |
| `cf104tot` | Ten words list learning first trail | `Numeric(Byte)` | `%9.0g` |
| `cf105tot` | Ten words list learning first trail | `Numeric(Byte)` | `%9.0g` |
| `cf106tot` | Ten words list learning first trail | `Numeric(Byte)` | `%9.0g` |
| `cf107tot` | Ten words list learning first trail | `Numeric(Byte)` | `%9.0g` |
| `cf108_` | Numeracy: subtraction 1 | `Numeric(Int)` | `%10.0g` |
| `cf109_` | Numeracy: subtraction 2 | `Numeric(Int)` | `%10.0g` |
| `cf110_` | Numeracy: subtraction 3 | `Numeric(Int)` | `%10.0g` |
| `cf111_` | Numeracy: subtraction 4 | `Numeric(Int)` | `%10.0g` |
| `cf112_` | Numeracy: subtraction 5 | `Numeric(Int)` | `%10.0g` |
| `cf113tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `cf114tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `cf115tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `cf116tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `cf719_` | Who answered questions in cf | `Numeric(Byte)` | `%38.0g` |

### `ch` - Children

- Dataset: `sharew7_rel9-0-0_ch.dta`
- Read with: `ps.read_share_module("ch", wave=7)`
- Rows: 77,181
- Variables: 1,616
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
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
| `childid_14` | Child identifier (fix across modules and waves): Child 14 | `Str(1)` | `%9s` |
| `childid_15` | Child identifier (fix across modules and waves): Child 15 | `Str(1)` | `%9s` |
| `childid_16` | Child identifier (fix across modules and waves): Child 16 | `Str(14)` | `%14s` |
| `childid_17` | Child identifier (fix across modules and waves): Child 17 | `Str(1)` | `%9s` |
| `childid_18` | Child identifier (fix across modules and waves): Child 18 | `Str(1)` | `%9s` |
| `childid_19` | Child identifier (fix across modules and waves): Child 19 | `Str(1)` | `%9s` |
| `childid_20` | Child identifier (fix across modules and waves): Child 20 | `Str(14)` | `%14s` |
| `ch001_` | Number of children | `Numeric(Byte)` | `%10.0g` |
| `ch005_1` | Child 1 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_2` | Child 2 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_3` | Child 3 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_4` | Child 4 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_5` | Child 5 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_6` | Child 6 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_7` | Child 7 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_8` | Child 8 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_9` | Child 9 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_10` | Child 10 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_11` | Child 11 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_12` | Child 12 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_13` | Child 13 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_14` | Child 14 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_15` | Child 15 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_16` | Child 16 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_17` | Child 17 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_18` | Child 18 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_19` | Child 19 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_20` | Child 20 gender | `Numeric(Byte)` | `%10.0g` |
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
| `ch006_14` | Child 14 year of birth | `Numeric(Byte)` | `%10.0g` |
| `ch006_15` | Child 15 year of birth | `Numeric(Byte)` | `%10.0g` |
| `ch006_16` | Child 16 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_17` | Child 17 year of birth | `Numeric(Byte)` | `%10.0g` |
| `ch006_18` | Child 18 year of birth | `Numeric(Byte)` | `%10.0g` |
| `ch006_19` | Child 19 year of birth | `Numeric(Byte)` | `%10.0g` |
| `ch006_20` | Child 20 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch007_REG_1` | Child 1 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_2` | Child 2 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_3` | Child 3 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_4` | Child 4 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_5` | Child 5 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_6` | Child 6 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_7` | Child 7 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_8` | Child 8 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_9` | Child 9 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_10` | Child 10 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_11` | Child 11 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_12` | Child 12 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_13` | Child 13 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_14` | Child 14 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_15` | Child 15 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_16` | Child 16 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_17` | Child 17 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_18` | Child 18 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_19` | Child 19 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_REG_20` | Child 20 (regular panel) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_1` | Child 1 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_2` | Child 2 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_3` | Child 3 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_4` | Child 4 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_5` | Child 5 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_6` | Child 6 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_7` | Child 7 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_8` | Child 8 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_9` | Child 9 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_10` | Child 10 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_11` | Child 11 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_12` | Child 12 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_13` | Child 13 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_14` | Child 14 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_15` | Child 15 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_16` | Child 16 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_17` | Child 17 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_18` | Child 18 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_19` | Child 19 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_adopted_child_20` | Child 20 (SHARELIFE: adopted) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_1` | Child 1 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_2` | Child 2 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_3` | Child 3 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_4` | Child 4 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_5` | Child 5 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_6` | Child 6 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_7` | Child 7 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_8` | Child 8 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_9` | Child 9 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_10` | Child 10 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_11` | Child 11 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_12` | Child 12 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_13` | Child 13 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_14` | Child 14 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_15` | Child 15 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_16` | Child 16 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_17` | Child 17 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_18` | Child 18 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_19` | Child 19 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
| `ch007_SHL_biological_child_20` | Child 20 (SHARELIFE: biological) where does child live | `Numeric(Byte)` | `%48.0g` |
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
| `ch014_REG_1` | Child 1 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_2` | Child 2 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_3` | Child 3 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_4` | Child 4 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_5` | Child 5 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_6` | Child 6 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_7` | Child 7 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_8` | Child 8 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_9` | Child 9 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_10` | Child 10 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_11` | Child 11 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_12` | Child 12 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_13` | Child 13 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_14` | Child 14 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_15` | Child 15 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_16` | Child 16 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_17` | Child 17 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_18` | Child 18 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_19` | Child 19 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_REG_20` | Child 20 (regular panel) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_1` | Child 1 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_2` | Child 2 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_3` | Child 3 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_4` | Child 4 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_5` | Child 5 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_6` | Child 6 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_7` | Child 7 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_8` | Child 8 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_9` | Child 9 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_10` | Child 10 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_11` | Child 11 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_12` | Child 12 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_13` | Child 13 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_14` | Child 14 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_15` | Child 15 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_16` | Child 16 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_17` | Child 17 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_18` | Child 18 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_19` | Child 19 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_adopted_child_20` | Child 20 (SHARELIFE: adopted) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_1` | Child 1 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_2` | Child 2 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_3` | Child 3 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_4` | Child 4 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_5` | Child 5 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_6` | Child 6 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_7` | Child 7 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_8` | Child 8 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_9` | Child 9 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_10` | Child 10 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_11` | Child 11 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_12` | Child 12 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_13` | Child 13 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_14` | Child 14 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_15` | Child 15 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_16` | Child 16 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_17` | Child 17 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_18` | Child 18 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_19` | Child 19 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch014_SHL_biological_child_20` | Child 20 (SHARELIFE: biological) contact with child | `Numeric(Byte)` | `%22.0g` |
| `ch015_1` | Child 1 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_2` | Child 2 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_3` | Child 3 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_4` | Child 4 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_5` | Child 5 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_6` | Child 6 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_7` | Child 7 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_8` | Child 8 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_9` | Child 9 year moved out | `Numeric(Int)` | `%33.0g` |
| `ch015_10` | Child 10 year moved out | `Numeric(Byte)` | `%33.0g` |
| `ch015_11` | Child 11 year moved out | `Numeric(Byte)` | `%33.0g` |
| `ch015_12` | Child 12 year moved out | `Numeric(Byte)` | `%33.0g` |
| `ch015_13` | Child 13 year moved out | `Numeric(Byte)` | `%33.0g` |
| `ch015_14` | Child 14 year moved out | `Numeric(Byte)` | `%33.0g` |
| `ch015_15` | Child 15 year moved out | `Numeric(Byte)` | `%33.0g` |
| `ch015_16` | Child 16 year moved out | `Numeric(Byte)` | `%33.0g` |
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
| `ch017_1` | Child 1 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_2` | Child 2 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_3` | Child 3 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_4` | Child 4 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_5` | Child 5 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_6` | Child 6 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_7` | Child 7 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_8` | Child 8 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_9` | Child 9 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_10` | Child 10 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_11` | Child 11 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_12` | Child 12 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_13` | Child 13 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_14` | Child 14 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_15` | Child 15 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_16` | Child 16 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_17` | Child 17 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_18` | Child 18 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_19` | Child 19 highest school degree | `Numeric(Byte)` | `%164.0g` |
| `ch017_20` | Child 20 highest school degree | `Numeric(Byte)` | `%164.0g` |
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
| `ch019_REG_1` | Child 1 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_2` | Child 2 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_3` | Child 3 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_4` | Child 4 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_5` | Child 5 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_6` | Child 6 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_7` | Child 7 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_8` | Child 8 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_9` | Child 9 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_10` | Child 10 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_11` | Child 11 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_12` | Child 12 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_13` | Child 13 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_14` | Child 14 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_15` | Child 15 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_16` | Child 16 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_17` | Child 17 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_18` | Child 18 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_19` | Child 19 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_REG_20` | Child 20 (regular panel) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_1` | Child 1 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_2` | Child 2 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_3` | Child 3 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_4` | Child 4 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_5` | Child 5 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_6` | Child 6 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_7` | Child 7 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_8` | Child 8 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_9` | Child 9 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_10` | Child 10 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_11` | Child 11 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_12` | Child 12 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_13` | Child 13 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_14` | Child 14 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_15` | Child 15 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_16` | Child 16 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_17` | Child 17 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_18` | Child 18 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_19` | Child 19 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_adopted_child_20` | Child 20 (SHARELIFE: adopted) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_1` | Child 1 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_2` | Child 2 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_3` | Child 3 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_4` | Child 4 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_5` | Child 5 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_6` | Child 6 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_7` | Child 7 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_8` | Child 8 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_9` | Child 9 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_10` | Child 10 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_11` | Child 11 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_12` | Child 12 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_13` | Child 13 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_14` | Child 14 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_15` | Child 15 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_16` | Child 16 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_17` | Child 17 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_18` | Child 18 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_19` | Child 19 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_SHL_biological_child_20` | Child 20 (SHARELIFE: biological) number of children | `Numeric(Byte)` | `%10.0g` |
| `ch020_1` | Child 1 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_2` | Child 2 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_3` | Child 3 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_4` | Child 4 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_5` | Child 5 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_6` | Child 6 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_7` | Child 7 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_8` | Child 8 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_9` | Child 9 year of birth youngest child | `Numeric(Int)` | `%10.0g` |
| `ch020_10` | Child 10 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch020_11` | Child 11 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch020_12` | Child 12 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch020_13` | Child 13 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch020_14` | Child 14 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch020_15` | Child 15 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch020_16` | Child 16 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch020_17` | Child 17 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch020_18` | Child 18 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch020_19` | Child 19 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch020_20` | Child 20 year of birth youngest child | `Numeric(Byte)` | `%10.0g` |
| `ch021_` | Number of grandchildren | `Numeric(Int)` | `%10.0g` |
| `ch022_` | Has great-grandchildren | `Numeric(Byte)` | `%10.0g` |
| `ch023_` | Who answered questions in section CH | `Numeric(Byte)` | `%44.0g` |
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
| `ch510_1` | Child 1 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_2` | Child 2 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_3` | Child 3 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_4` | Child 4 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_5` | Child 5 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_6` | Child 6 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_7` | Child 7 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_8` | Child 8 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_9` | Child 9 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_10` | Child 10 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_11` | Child 11 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_12` | Child 12 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_13` | Child 13 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_14` | Child 14 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_15` | Child 15 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_16` | Child 16 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_17` | Child 17 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_18` | Child 18 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_19` | Child 19 new educational degree | `Numeric(Byte)` | `%164.0g` |
| `ch510_20` | Child 20 new educational degree | `Numeric(Byte)` | `%164.0g` |
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
| `ch520_11` | Child 11 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_12` | Child 12 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_13` | Child 13 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_14` | Child 14 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_15` | Child 15 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_16` | Child 16 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_17` | Child 17 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_18` | Child 18 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_19` | Child 19 new youngest born | `Numeric(Byte)` | `%10.0g` |
| `ch520_20` | Child 20 new youngest born | `Numeric(Byte)` | `%10.0g` |
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

- Dataset: `sharew7_rel9-0-0_co.dta`
- Read with: `ps.read_share_module("co", wave=7)`
- Rows: 77,181
- Variables: 29
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `co002e` | Amount spent on food at home | `Numeric(Float)` | `%10.0g` |
| `co002ub` | Amount spent on food at home ub | `Numeric(Byte)` | `%32.0g` |
| `co002v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `co002v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `co002v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `co003e` | Amount spent on food outside the home | `Numeric(Float)` | `%10.0g` |
| `co003ub` | Amount spent on food outside the home ub | `Numeric(Byte)` | `%32.0g` |
| `co003v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `co003v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `co003v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `co007_` | Is household able to make ends meet | `Numeric(Byte)` | `%28.0g` |
| `co009_` | Who answered the questions in co | `Numeric(Byte)` | `%44.0g` |
| `co010_` | Consume home produced food | `Numeric(Byte)` | `%10.0g` |
| `co011e` | Value of home produced food | `Numeric(Float)` | `%10.0g` |
| `co011ub` | Value of home produced food ub | `Numeric(Byte)` | `%32.0g` |
| `co011v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `co011v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `co011v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `co020e` | Minimum amount needed per month | `Numeric(Float)` | `%10.0g` |
| `co206_` | Afford to pay an unexpected expense without borrowing money | `Numeric(Byte)` | `%10.0g` |
| `co209_` | To help keeping living costs down: put up with feeling cold | `Numeric(Byte)` | `%10.0g` |
| `co211_` | To help keeping living costs down: postponed visits to the dentist | `Numeric(Byte)` | `%10.0g` |

### `cv_r` - Coverscreen on individual level

- Dataset: `sharew7_rel9-0-0_cv_r.dta`
- Read with: `ps.read_share_module("cv_r", wave=7)`
- Rows: 111,529
- Variables: 31
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
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
| `age2017` | Age in 2017 | `Numeric(Int)` | `%14.0g` |
| `age_int` | Age of respondent at the time of interview | `Numeric(Int)` | `%14.0g` |
| `mobirthp` | Month of birth spouse/partner | `Numeric(Byte)` | `%14.0g` |
| `yrbirthp` | Year of birth spouse/partner | `Numeric(Int)` | `%14.0g` |
| `agep2017` | Age of partner in 2017 | `Numeric(Int)` | `%14.0g` |
| `partnerinhh` | Partner in household | `Numeric(Byte)` | `%14.0g` |
| `relrpers` | Relation to coverscreen respondent | `Numeric(Byte)` | `%47.0g` |
| `hhsize` | Household size | `Numeric(Byte)` | `%9.0g` |
| `hhmoved` | Household moved | `Numeric(Byte)` | `%10.0g` |
| `fam_resp` | Family respondent | `Numeric(Byte)` | `%21.0g` |
| `fin_resp` | Financial respondent | `Numeric(Byte)` | `%24.0g` |
| `hou_resp` | Household respondent | `Numeric(Byte)` | `%24.0g` |
| `ILgroup` | Population group (Israel only) | `Numeric(Byte)` | `%38.0g` |
| `interview` | Interview done in wave 7 | `Numeric(Byte)` | `%21.0g` |
| `int_year` | Interview year | `Numeric(Int)` | `%14.0g` |
| `int_month` | Interview month | `Numeric(Byte)` | `%14.0g` |

### `dn` - Demographics

- Dataset: `sharew7_rel9-0-0_dn.dta`
- Read with: `ps.read_share_module("dn", wave=7)`
- Rows: 77,181
- Variables: 95
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `dn002_` | Month of birth | `Numeric(Byte)` | `%10.0g` |
| `dn003_` | Year of birth | `Numeric(Int)` | `%10.0g` |
| `dn004_` | Born in the country of interview | `Numeric(Byte)` | `%10.0g` |
| `dn005c` | Foreign country of birth coding | `Numeric(Int)` | `%46.0g` |
| `dn006_` | Year came to live in country | `Numeric(Int)` | `%10.0g` |
| `dn007_` | Citizenship country of interview | `Numeric(Byte)` | `%10.0g` |
| `dn008c` | Other citizenship coding | `Numeric(Int)` | `%46.0g` |
| `dn009_` | Country-specific question | `Numeric(Byte)` | `%25.0g` |
| `dn010_` | Highest school degree obtained | `Numeric(Byte)` | `%164.0g` |
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
| `dn014_` | Marital status | `Numeric(Byte)` | `%56.0g` |
| `dn015_` | Year of marriage, if living together | `Numeric(Int)` | `%10.0g` |
| `dn016_` | Year of registered partnership | `Numeric(Int)` | `%10.0g` |
| `dn017_` | Year of marriage, if living separated | `Numeric(Int)` | `%10.0g` |
| `dn018_` | Since when divorced | `Numeric(Int)` | `%10.0g` |
| `dn019_` | Since when widowed | `Numeric(Int)` | `%10.0g` |
| `dn020_` | Year of birth of former partner | `Numeric(Int)` | `%10.0g` |
| `dn021_` | Highest educational degree of former partner | `Numeric(Byte)` | `%164.0g` |
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
| `dn028_2` | Age of natural parent: father | `Numeric(Int)` | `%10.0g` |
| `dn030_1` | Where does parent live: mother | `Numeric(Byte)` | `%48.0g` |
| `dn030_2` | Where does parent live: father | `Numeric(Byte)` | `%48.0g` |
| `dn032_1` | Personal contact with parent during past 12 months: mother | `Numeric(Byte)` | `%27.0g` |
| `dn032_2` | Personal contact with parent during past 12 months: father | `Numeric(Byte)` | `%27.0g` |
| `dn033_1` | Health of parent: mother | `Numeric(Byte)` | `%13.0g` |
| `dn033_2` | Health of parent: father | `Numeric(Byte)` | `%13.0g` |
| `dn034_` | Ever had any siblings | `Numeric(Byte)` | `%10.0g` |
| `dn036_` | How many brothers alive | `Numeric(Byte)` | `%10.0g` |
| `dn037_` | How many sisters alive | `Numeric(Byte)` | `%10.0g` |
| `dn038_` | Who answered the questions in dn | `Numeric(Byte)` | `%44.0g` |
| `dn040_` | Partner outside household | `Numeric(Byte)` | `%10.0g` |
| `dn041_` | Years education | `Numeric(Int)` | `%35.0g` |
| `dn042_` | Male or female | `Numeric(Byte)` | `%10.0g` |
| `dn043_` | Confirm month/year birth | `Numeric(Byte)` | `%10.0g` |
| `dn044_` | Marital status changed | `Numeric(Byte)` | `%49.0g` |
| `dn127_1` | Year of death of parent: mother | `Numeric(Int)` | `%10.0g` |
| `dn127_2` | Year of death of parent: father | `Numeric(Int)` | `%10.0g` |
| `dn502_` | Year of becoming citizen of country of interview | `Numeric(Int)` | `%10.0g` |
| `dn503_` | Born a citizen of country of interview | `Numeric(Byte)` | `%10.0g` |
| `dn504c` | Country of birth coded: mother | `Numeric(Int)` | `%46.0g` |
| `dn505c` | Country of birth coded: father | `Numeric(Int)` | `%46.0g` |
| `dn756_` | Who answers questionnaire | `Numeric(Byte)` | `%44.0g` |

### `ep` - Employment and Pensions

- Dataset: `sharew7_rel9-0-0_ep.dta`
- Read with: `ps.read_share_module("ep", wave=7)`
- Rows: 77,181
- Variables: 436
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `ep002_` | Did nevertheless any paid work last four weeks | `Numeric(Byte)` | `%10.0g` |
| `ep005_` | Current job situation | `Numeric(Byte)` | `%65.0g` |
| `ep006_` | Ever done paid work | `Numeric(Byte)` | `%10.0g` |
| `ep007_` | Currently more than one job | `Numeric(Byte)` | `%10.0g` |
| `ep009_` | Employee or self-employed | `Numeric(Byte)` | `%60.0g` |
| `ep010_` | Start of current job (year) | `Numeric(Int)` | `%10.0g` |
| `ep011_` | Term of job | `Numeric(Byte)` | `%27.0g` |
| `ep013_` | Total hours usually working per week | `Numeric(Int)` | `%10.0g` |
| `ep018_` | Kind of industry working in | `Numeric(Byte)` | `%117.0g` |
| `ep020_` | Number of people employed at firm | `Numeric(Byte)` | `%13.0g` |
| `ep021_` | Responsibility for supervising other employees | `Numeric(Byte)` | `%10.0g` |
| `ep022_` | Number of people responsible for | `Numeric(Byte)` | `%13.0g` |
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
| `ep036_` | Look for early retirement in (main) job | `Numeric(Byte)` | `%10.0g` |
| `ep037_` | Afraid health limits ability to work before regular retirement in (main) job | `Numeric(Byte)` | `%10.0g` |
| `ep050_` | Year last job ended | `Numeric(Int)` | `%10.0g` |
| `ep051_` | Employee or a self employed in last job | `Numeric(Byte)` | `%61.0g` |
| `ep054_` | Kind of industry working in last job | `Numeric(Byte)` | `%117.0g` |
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
| `ep069d1` | Reason stopped working: health problems | `Numeric(Byte)` | `%12.0g` |
| `ep069d2` | Reason stopped working: too tiring | `Numeric(Byte)` | `%12.0g` |
| `ep069d3` | Reason stopped working: too expensive to hire someone to look after home/family | `Numeric(Byte)` | `%12.0g` |
| `ep069d4` | Reason stopped working: wanted to take care of (grand)children | `Numeric(Byte)` | `%12.0g` |
| `ep069d5` | Reason stopped working: laid off, or workplace/office closed | `Numeric(Byte)` | `%12.0g` |
| `ep069d6` | Reason stopped working: family income sufficient | `Numeric(Byte)` | `%12.0g` |
| `ep069d7` | Reason stopped working: to care for old/sick family member | `Numeric(Byte)` | `%12.0g` |
| `ep069dot` | Reason stopped working: other | `Numeric(Byte)` | `%12.0g` |
| `ep074_1` | Period of income source c1 (ep671d1) | `Numeric(Byte)` | `%29.0g` |
| `ep074_2` | Period of income source c2 (ep671d2) | `Numeric(Byte)` | `%29.0g` |
| `ep074_3` | Period of income source c3 (ep671d3) | `Numeric(Byte)` | `%29.0g` |
| `ep074_4` | Period of income source c4 (ep671d4) | `Numeric(Byte)` | `%29.0g` |
| `ep074_5` | Period of income source c5 (ep671d5) | `Numeric(Byte)` | `%29.0g` |
| `ep074_6` | Period of income source c6 (ep671d6) | `Numeric(Byte)` | `%29.0g` |
| `ep074_7` | Period of income source c7 (ep671d7) | `Numeric(Byte)` | `%29.0g` |
| `ep074_8` | Period of income source c8 (ep671d8) | `Numeric(Byte)` | `%29.0g` |
| `ep074_9` | Period of income source c9 (ep671d9) | `Numeric(Byte)` | `%29.0g` |
| `ep074_10` | Period of income source c10 (ep671d10) | `Numeric(Byte)` | `%29.0g` |
| `ep074_11` | Period of income source c11 (ep671d11) | `Numeric(Byte)` | `%29.0g` |
| `ep074_12` | Period of income source c12 (ep671d12) | `Numeric(Byte)` | `%29.0g` |
| `ep074_13` | Period of income source c13 (ep671d13) | `Numeric(Byte)` | `%29.0g` |
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
| `ep082e_8` | Total amount of lump sum payment income source c8 last year (ep671d8) | `Numeric(Int)` | `%10.0g` |
| `ep082e_9` | Total amount of lump sum payment income source c9 last year (ep671d9) | `Numeric(Float)` | `%10.0g` |
| `ep082e_10` | Total amount of lump sum payment income source c10 last year (ep671d10) | `Numeric(Int)` | `%10.0g` |
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
| `ep090_1` | Period received payment c1 | `Numeric(Byte)` | `%29.0g` |
| `ep090_2` | Period received payment c2 | `Numeric(Byte)` | `%29.0g` |
| `ep090_3` | Period received payment c3 | `Numeric(Byte)` | `%29.0g` |
| `ep090_4` | Period received payment c4 | `Numeric(Byte)` | `%29.0g` |
| `ep090_5` | Period received payment c5 | `Numeric(Byte)` | `%29.0g` |
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
| `ep102_1` | Compulsory or voluntary participation in pension c1 | `Numeric(Byte)` | `%13.0g` |
| `ep102_2` | Compulsory or voluntary participation in pension c2 | `Numeric(Byte)` | `%13.0g` |
| `ep102_3` | Compulsory or voluntary participation in pension c3 | `Numeric(Byte)` | `%13.0g` |
| `ep102_4` | Compulsory or voluntary participation in pension c4 | `Numeric(Byte)` | `%13.0g` |
| `ep102_5` | Compulsory or voluntary participation in pension c5 | `Numeric(Byte)` | `%13.0g` |
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
| `ep123_` | Receive severance year | `Numeric(Byte)` | `%17.0g` |
| `ep125_` | Continuously working | `Numeric(Byte)` | `%10.0g` |
| `ep127_1` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_2` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_3` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_4` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_5` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_6` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_7` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_8` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_9` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_10` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_11` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_12` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_13` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_21` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_22` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_23` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_24` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_25` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_26` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_27` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_28` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_29` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_30` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_31` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_32` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep128_1` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_2` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_3` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_4` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_5` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_6` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_7` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_8` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_9` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_10` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_11` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_12` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_13` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_21` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_22` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_23` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_24` | Period from year (unemployed) | `Numeric(Int)` | `%17.0g` |
| `ep128_25` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_26` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_27` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_28` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_29` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_30` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_31` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_32` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep129_1` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_2` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_3` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_4` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_5` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_6` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_7` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_8` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_9` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_10` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_11` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_12` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_13` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_21` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_22` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_23` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_24` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_25` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_26` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_27` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_28` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_29` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_30` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_31` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_32` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep130_1` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_2` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_3` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_4` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_5` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_6` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_7` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_8` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_9` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_10` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_11` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_12` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_13` | Period to year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep130_21` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_22` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_23` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_24` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_25` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_26` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_27` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_28` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_29` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_30` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_31` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep130_32` | Period to year (unemployed) | `Numeric(Byte)` | `%17.0g` |
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
| `ep133_21` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_22` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_23` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_24` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_25` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_26` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_27` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_28` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_29` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_30` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_31` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_32` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
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
| `ep207v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
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
| `ep209e_5` | Additional payments c5 after taxes | `Numeric(Byte)` | `%10.0g` |
| `ep209ub_1` | Additional payments c1 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209ub_2` | Additional payments c2 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209ub_3` | Additional payments c3 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209ub_4` | Additional payments c4 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209ub_5` | Additional payments c5 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209v1` | Bracket value 1 | `Numeric(Float)` | `%9.0g` |
| `ep209v2` | Bracket value 2 | `Numeric(Float)` | `%9.0g` |
| `ep209v3` | Bracket value 3 | `Numeric(Float)` | `%9.0g` |
| `ep210_` | Who answered section ep | `Numeric(Byte)` | `%44.0g` |
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
| `ep321_` | Total hours worked per week second job | `Numeric(Byte)` | `%10.0g` |
| `ep322_` | Months per year worked in second job (number) | `Numeric(Byte)` | `%10.0g` |
| `ep325_` | Unemployed since last interview | `Numeric(Byte)` | `%10.0g` |
| `ep326_` | Received severance payment since last interview | `Numeric(Byte)` | `%10.0g` |
| `ep328_` | Retirement month | `Numeric(Byte)` | `%10.0g` |
| `ep329_` | Retirement year | `Numeric(Int)` | `%10.0g` |
| `ep337_` | Currently looking for job | `Numeric(Byte)` | `%10.0g` |
| `ep609e_1` | Amount of first monthly benefit from pension 1 (ep098d1) | `Numeric(Float)` | `%10.0g` |
| `ep609e_2` | Amount of first monthly benefit from pension 2 (ep098d2) | `Numeric(Float)` | `%10.0g` |
| `ep609e_3` | Amount of first monthly benefit from pension 3 (ep098d3) | `Numeric(Float)` | `%10.0g` |
| `ep609e_4` | Amount of first monthly benefit from pension 4 (ep098d4) | `Numeric(Float)` | `%10.0g` |
| `ep609e_5` | Amount of first monthly benefit from pension 5 (ep098d5) | `Numeric(Float)` | `%10.0g` |
| `ep612_1` | First received income source c1 before last interview (ep671d1) | `Numeric(Byte)` | `%32.0g` |
| `ep612_2` | First received income source c2 before last interview (ep671d2) | `Numeric(Byte)` | `%32.0g` |
| `ep612_3` | First received income source c3 before last interview (ep671d3) | `Numeric(Byte)` | `%32.0g` |
| `ep612_4` | First received income source c4 before last interview (ep671d4) | `Numeric(Byte)` | `%32.0g` |
| `ep612_5` | First received income source c5 before last interview (ep671d5) | `Numeric(Byte)` | `%32.0g` |
| `ep612_6` | First received income source c6 before last interview (ep671d6) | `Numeric(Byte)` | `%32.0g` |
| `ep612_7` | First received income source c7 before last interview (ep671d7) | `Numeric(Byte)` | `%32.0g` |
| `ep612_8` | First received income source c8 before last interview (ep671d8) | `Numeric(Byte)` | `%32.0g` |
| `ep612_9` | First received income source c9 before last interview (ep671d9) | `Numeric(Byte)` | `%32.0g` |
| `ep612_10` | First received income source c10 before last interview (ep671d10) | `Numeric(Byte)` | `%32.0g` |
| `ep612_11` | First received income source c11 before last interview (ep671d11) | `Numeric(Byte)` | `%32.0g` |
| `ep612_12` | First received income source c12 before last interview (ep671d12) | `Numeric(Byte)` | `%32.0g` |
| `ep612_13` | First received income source c13 before last interview (ep671d13) | `Numeric(Byte)` | `%32.0g` |
| `ep613_` | Year started collecting first occupational pension | `Numeric(Int)` | `%10.0g` |
| `ep616isco` | ISCO code-08: respondent's current main job | `Numeric(Int)` | `%13.0g` |
| `ep621_` | Started collecting first occupational pension before last interview | `Numeric(Byte)` | `%32.0g` |
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
| `ep678v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ep678v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ep678v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `ep681_` | Received additional/extra/lump-sum payment from occupational pension last year | `Numeric(Byte)` | `%10.0g` |
| `ep682e` | Amount received as additional/extra/lump-sum payment | `Numeric(Float)` | `%10.0g` |
| `ep682ub` | Amount received as additional/extra/lump-sum payment ub | `Numeric(Byte)` | `%32.0g` |
| `ep682v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ep682v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ep682v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ep738_` | Who answered questions in ep | `Numeric(Byte)` | `%59.0g` |

### `ex` - Expectations

- Dataset: `sharew7_rel9-0-0_ex.dta`
- Read with: `ps.read_share_module("ex", wave=7)`
- Rows: 77,181
- Variables: 26
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ex001_` | Introduction and example | `Numeric(Byte)` | `%10.0g` |
| `ex007_` | Chance government reduces pension | `Numeric(Byte)` | `%10.0g` |
| `ex008_` | Chance government raises retirement age | `Numeric(Byte)` | `%10.0g` |
| `ex009_` | Life expectancy | `Numeric(Byte)` | `%10.0g` |
| `ex009age` | Life expectancy target age | `Numeric(Int)` | `%10.0g` |
| `ex023_` | End non proxy | `Numeric(Byte)` | `%59.0g` |
| `ex025_` | Chance to work after age of 63 | `Numeric(Byte)` | `%10.0g` |
| `ex026_` | Trust in other people | `Numeric(Byte)` | `%10.0g` |
| `ex028_` | Left or right in politics | `Numeric(Byte)` | `%10.0g` |
| `ex029_` | Frequency of praying | `Numeric(Byte)` | `%31.0g` |
| `ex104_` | Partner ever done paid work | `Numeric(Byte)` | `%10.0g` |
| `ex105_` | Partner employee or a self-employed | `Numeric(Byte)` | `%61.0g` |
| `ex110_` | Risk aversion | `Numeric(Byte)` | `%118.0g` |
| `ex111_` | Planning horizon of saving and spending | `Numeric(Byte)` | `%24.0g` |
| `ex123_` | Consent to recontact | `Numeric(Byte)` | `%45.0g` |
| `ex600_` | Partner available/willing to be (proxy) interviewed | `Numeric(Byte)` | `%91.0g` |
| `ex602_` | Amount of years spouse/partner been in school | `Numeric(Int)` | `%10.0g` |
| `ex603_` | Partner current job situation | `Numeric(Byte)` | `%62.0g` |
| `ex613isco` | ISCO-08 code: Most recent job of spouse/partner | `Numeric(Int)` | `%13.0g` |
| `ex709_` | Life expectancy | `Numeric(Byte)` | `%10.0g` |

### `ft` - Financial Transfers

- Dataset: `sharew7_rel9-0-0_ft.dta`
- Read with: `ps.read_share_module("ft", wave=7)`
- Rows: 77,181
- Variables: 69
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ft002_` | Given financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft003_1` | To whom given gift, person 1 | `Numeric(Byte)` | `%56.0g` |
| `ft003_2` | To whom given gift, person 2 | `Numeric(Byte)` | `%56.0g` |
| `ft003_3` | To whom given gift, person 3 | `Numeric(Byte)` | `%56.0g` |
| `ft007_1` | Other persons given financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft007_2` | Other persons given financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft007_3` | Other persons given financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft009_` | Received financial gift of 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft010_1` | From whom recieved gift, person 1 | `Numeric(Byte)` | `%56.0g` |
| `ft010_2` | From whom recieved gift, person 2 | `Numeric(Byte)` | `%56.0g` |
| `ft010_3` | From whom recieved gift, person 3 | `Numeric(Byte)` | `%56.0g` |
| `ft014_1` | From other persons received financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft014_2` | From other persons received financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft014_3` | From other persons received financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft015_` | Ever received gift or inheritance (worth 5000 euros or more) | `Numeric(Byte)` | `%10.0g` |
| `ft016_1` | Year, inheritance or large gift 1 received | `Numeric(Int)` | `%10.0g` |
| `ft016_2` | Year, inheritance or large gift 2 received | `Numeric(Int)` | `%10.0g` |
| `ft016_3` | Year, inheritance or large gift 3 received | `Numeric(Int)` | `%10.0g` |
| `ft016_4` | Year, inheritance or large gift 4 received | `Numeric(Int)` | `%10.0g` |
| `ft016_5` | Year, inheritance or large gift 5 received | `Numeric(Int)` | `%10.0g` |
| `ft017_1` | From whom inheritance or large gift 1 | `Numeric(Byte)` | `%56.0g` |
| `ft017_2` | From whom inheritance or large gift 2 | `Numeric(Byte)` | `%56.0g` |
| `ft017_3` | From whom inheritance or large gift 3 | `Numeric(Byte)` | `%56.0g` |
| `ft017_4` | From whom inheritance or large gift 4 | `Numeric(Byte)` | `%56.0g` |
| `ft017_5` | From whom inheritance or large gift 5 | `Numeric(Byte)` | `%56.0g` |
| `ft020_1` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft020_2` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft020_3` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft020_4` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft020_5` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft021_` | Who answered the questions in ft | `Numeric(Byte)` | `%44.0g` |
| `ft025_` | Ever given gift 5000 or more | `Numeric(Byte)` | `%10.0g` |
| `ft026_1` | In which year given gift | `Numeric(Int)` | `%10.0g` |
| `ft026_2` | In which year given gift | `Numeric(Int)` | `%10.0g` |
| `ft026_3` | In which year given gift | `Numeric(Int)` | `%10.0g` |
| `ft026_4` | In which year given gift | `Numeric(Int)` | `%10.0g` |
| `ft026_5` | In which year given gift | `Numeric(Int)` | `%10.0g` |
| `ft027_1` | To whom given 5000 or more | `Numeric(Byte)` | `%56.0g` |
| `ft027_2` | To whom given 5000 or more | `Numeric(Byte)` | `%56.0g` |
| `ft027_3` | To whom given 5000 or more | `Numeric(Byte)` | `%56.0g` |
| `ft027_4` | To whom given 5000 or more | `Numeric(Byte)` | `%56.0g` |
| `ft027_5` | To whom given 5000 or more | `Numeric(Byte)` | `%56.0g` |
| `ft031_1` | Any further gift | `Numeric(Byte)` | `%10.0g` |
| `ft031_2` | Any further gift | `Numeric(Byte)` | `%10.0g` |
| `ft031_3` | Any further gift | `Numeric(Byte)` | `%10.0g` |
| `ft031_4` | Any further gift | `Numeric(Byte)` | `%10.0g` |
| `ft031_5` | Any further gift | `Numeric(Byte)` | `%10.0g` |
| `ft032_1` | To which child given financial gift | `Numeric(Byte)` | `%14.0g` |
| `ft032_2` | To which child given financial gift | `Numeric(Byte)` | `%14.0g` |
| `ft032_3` | To which child given financial gift | `Numeric(Byte)` | `%14.0g` |
| `ft034_1` | From which child received financial gift | `Numeric(Byte)` | `%14.0g` |
| `ft034_2` | From which child received financial gift | `Numeric(Byte)` | `%14.0g` |
| `ft034_3` | From which child received financial gift | `Numeric(Byte)` | `%14.0g` |
| `ft036_1` | From which child inheritance or large gift | `Numeric(Byte)` | `%14.0g` |
| `ft036_2` | From which child inheritance or large gift | `Numeric(Byte)` | `%14.0g` |
| `ft036_3` | From which child inheritance or large gift | `Numeric(Byte)` | `%14.0g` |
| `ft036_4` | From which child inheritance or large gift | `Numeric(Byte)` | `%14.0g` |
| `ft036_5` | From which child inheritance or large gift | `Numeric(Byte)` | `%14.0g` |
| `ft038_1` | To which child given 5000 or more | `Numeric(Byte)` | `%14.0g` |
| `ft038_2` | To which child given 5000 or more | `Numeric(Byte)` | `%14.0g` |
| `ft038_3` | To which child given 5000 or more | `Numeric(Byte)` | `%14.0g` |
| `ft038_4` | To which child given 5000 or more | `Numeric(Byte)` | `%14.0g` |
| `ft038_5` | To which child given 5000 or more | `Numeric(Byte)` | `%14.0g` |

### `gs` - Grip Strength

- Dataset: `sharew7_rel9-0-0_gs.dta`
- Read with: `ps.read_share_module("gs", wave=7)`
- Rows: 77,181
- Variables: 23
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `gs002_` | Record respondent status | `Numeric(Byte)` | `%51.0g` |
| `gs004_` | Dominant hand | `Numeric(Byte)` | `%13.0g` |
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
| `gs012_` | How much effort gave r | `Numeric(Byte)` | `%121.0g` |
| `gs013_` | The position of r for this test | `Numeric(Byte)` | `%10.0g` |
| `gs014_` | R rested his/her arms on a support | `Numeric(Byte)` | `%10.0g` |
| `gs701_` | Willing to have handgrip measured | `Numeric(Byte)` | `%58.0g` |

### `hc` - Health Care

- Dataset: `sharew7_rel9-0-0_hc.dta`
- Read with: `ps.read_share_module("hc", wave=7)`
- Rows: 77,181
- Variables: 71
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `hc010_` | Seen a dentist/dental hygienist in the last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc012_` | Stayed over night in hospital last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc013_` | Times being patient in hospital | `Numeric(Byte)` | `%10.0g` |
| `hc014_` | Total nights stayed in hospital | `Numeric(Int)` | `%10.0g` |
| `hc029_` | In a nursing home during last 12 months | `Numeric(Byte)` | `%18.0g` |
| `hc031_` | Weeks stayed in a nursing home or residential care facility | `Numeric(Byte)` | `%10.0g` |
| `hc033_` | Weeks received professional nursing care | `Numeric(Byte)` | `%10.0g` |
| `hc034_` | Hours received professional nursing care | `Numeric(Int)` | `%10.0g` |
| `hc035_` | Weeks received paid domestic help | `Numeric(Byte)` | `%10.0g` |
| `hc036_` | Hours received paid domestic help | `Numeric(Int)` | `%10.0g` |
| `hc037_` | Weeks received meals-on-wheels | `Numeric(Byte)` | `%10.0g` |
| `hc064_` | In other institutions last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc066_` | Total nights stayed in other institutions | `Numeric(Int)` | `%10.0g` |
| `hc097e` | Amount payed for stay in nursing home/residential care facility last 12 months | `Numeric(Float)` | `%10.0g` |
| `hc097ub` | Amount payed for stay in nursing home/residential care facility last 12 months u | `Numeric(Byte)` | `%21.0g` |
| `hc097v` | Bracket value | `Numeric(Double)` | `%8.0g` |
| `hc113_` | Has supplementary health insurance | `Numeric(Byte)` | `%10.0g` |
| `hc114_` | Could not see a doctor because of cost | `Numeric(Byte)` | `%10.0g` |
| `hc115_` | Could not see a doctor because of long waiting times | `Numeric(Byte)` | `%10.0g` |
| `hc116d1` | Long-term care insurances: public (country deviations!) | `Numeric(Byte)` | `%12.0g` |
| `hc116d2` | Long-term care insurances: private mandatory (country deviations!) | `Numeric(Byte)` | `%12.0g` |
| `hc116d3` | Long-term care insurances: private voluntary/supplementary (country deviations!) | `Numeric(Byte)` | `%12.0g` |
| `hc116dno` | Long-term care insurances: none of these (country deviations!) | `Numeric(Byte)` | `%12.0g` |
| `hc125_` | Satisfaction with own coverage in basic health insurance/national health system | `Numeric(Byte)` | `%21.0g` |
| `hc127d1` | Received professional services: help with personal care in own home | `Numeric(Byte)` | `%12.0g` |
| `hc127d2` | Received professional services: help with domestic tasks in own home | `Numeric(Byte)` | `%12.0g` |
| `hc127d3` | Received professional services: meals-on-wheels | `Numeric(Byte)` | `%12.0g` |
| `hc127d4` | Received professional services: help with other activies | `Numeric(Byte)` | `%12.0g` |
| `hc127dno` | Received professional services: none of these | `Numeric(Byte)` | `%12.0g` |
| `hc140d1` | Payed anything yourself for aids/appliances last 12 months | `Numeric(Byte)` | `%12.0g` |
| `hc140d2` | Payed anything yourself for ambulatory therapies last 12 months | `Numeric(Byte)` | `%12.0g` |
| `hc140dno` | Payed anything yourself: none of these | `Numeric(Byte)` | `%12.0g` |
| `hc142e` | Amount payed yourself for aids/appliances last 12 months | `Numeric(Float)` | `%10.0g` |
| `hc142ub` | Amount payed yourself for aids/appliances last 12 months ub | `Numeric(Byte)` | `%21.0g` |
| `hc142v` | Bracket value | `Numeric(Float)` | `%8.0g` |
| `hc143e` | Amount payed yourself for ambulatory therapies last 12 months | `Numeric(Float)` | `%10.0g` |
| `hc143ub` | Amount payed yourself for ambulatory therapies last 12 months ub | `Numeric(Byte)` | `%21.0g` |
| `hc143v` | Bracket value | `Numeric(Float)` | `%8.0g` |
| `hc144e` | Amount payed yourself for homecare in a typical month | `Numeric(Float)` | `%10.0g` |
| `hc144ub` | Amount payed yourself for homecare in a typical month ub | `Numeric(Byte)` | `%21.0g` |
| `hc144v` | Bracket value | `Numeric(Float)` | `%8.0g` |
| `hc602_` | Times talked to medical doctor/nurse about your health last 12 months | `Numeric(Int)` | `%10.0g` |
| `hc628_` | Payed anything yourself for homecare last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc629e` | Amount payed yourself for homecare last 12 months | `Numeric(Float)` | `%10.0g` |
| `hc630e` | Amount payed yourself for medication in a typical month | `Numeric(Float)` | `%10.0g` |
| `hc630ub` | Amount payed yourself for medication in a typical month ub | `Numeric(Byte)` | `%21.0g` |
| `hc630v` | Bracket value | `Numeric(Float)` | `%8.0g` |
| `hc682_` | Payed anything yourself for doctor visits last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc683e` | Amount payed yourself for doctor visits last 12 months | `Numeric(Float)` | `%10.0g` |
| `hc683ub` | Amount payed yourself for doctor visits last 12 months ub | `Numeric(Byte)` | `%21.0g` |
| `hc683v` | Bracket value | `Numeric(Float)` | `%8.0g` |
| `hc688_` | Payed anything yourself for medication last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc689e` | Amount payed yourself for medication last 12 months | `Numeric(Float)` | `%10.0g` |
| `hc692_` | Payed anything yourself for dental care last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc693e` | Amount payed yourself for dental care last 12 months | `Numeric(Float)` | `%10.0g` |
| `hc693ub` | Amount payed yourself for dental care last 12 months ub | `Numeric(Byte)` | `%21.0g` |
| `hc693v` | Bracket value | `Numeric(Float)` | `%8.0g` |
| `hc694_` | Payed anything yourself for stays in hospitals 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc695e` | Amount payed yourself for stays in hospitals last 12 months | `Numeric(Float)` | `%10.0g` |
| `hc695ub` | Amount payed yourself for stays in hospitals last 12 months ub | `Numeric(Byte)` | `%21.0g` |
| `hc695v` | Bracket value | `Numeric(Float)` | `%8.0g` |
| `hc696_` | Payed anything yourself:stay in nursing home/residential care facility last 12 m | `Numeric(Byte)` | `%10.0g` |
| `hc751_` | Certified nurse | `Numeric(Byte)` | `%10.0g` |
| `hc760_` | Needed medication but could not afford last 12 months | `Numeric(Byte)` | `%10.0g` |

### `hh` - Household Income

- Dataset: `sharew7_rel9-0-0_hh.dta`
- Read with: `ps.read_share_module("hh", wave=7)`
- Rows: 77,181
- Variables: 24
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `hh001_` | Other contributor to household income | `Numeric(Byte)` | `%10.0g` |
| `hh010_` | Income from other sources | `Numeric(Byte)` | `%10.0g` |
| `hh011e` | Additional income received by all hh-members last year | `Numeric(Float)` | `%10.0g` |
| `hh011ub` | Additional income received by all hh-members last year ub | `Numeric(Byte)` | `%32.0g` |
| `hh011v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `hh011v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `hh011v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `hh014_` | Who answered the question in hh | `Numeric(Byte)` | `%44.0g` |
| `hh017e` | Total income received by all hh members an average month last year | `Numeric(Float)` | `%10.0g` |
| `hh017ub` | Total income received by all hh-members an average month last year ub | `Numeric(Byte)` | `%32.0g` |
| `hh017v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `hh017v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `hh017v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `hh022_` | Feeling part of this area | `Numeric(Byte)` | `%26.0g` |
| `hh023_` | Vandalism/Crime is a big problem in this area | `Numeric(Byte)` | `%26.0g` |
| `hh024_` | Area is kept very clean | `Numeric(Byte)` | `%26.0g` |
| `hh025_` | If I were in trouble, there are people in this area who would help me | `Numeric(Byte)` | `%26.0g` |

### `ho` - Housing

- Dataset: `sharew7_rel9-0-0_ho.dta`
- Read with: `ps.read_share_module("ho", wave=7)`
- Rows: 77,181
- Variables: 79
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `ho001_` | Interview in house of respondent | `Numeric(Byte)` | `%10.0g` |
| `ho002_` | Owner, tenant or rent free | `Numeric(Byte)` | `%23.0g` |
| `ho003_` | Rent payment period | `Numeric(Byte)` | `%22.0g` |
| `ho007_` | Last rent payment included all charges and services | `Numeric(Byte)` | `%10.0g` |
| `ho008e` | Amount charges and services | `Numeric(Float)` | `%10.0g` |
| `ho010_` | More than two months behind with rent | `Numeric(Byte)` | `%10.0g` |
| `ho012_` | Year acquired property | `Numeric(Int)` | `%10.0g` |
| `ho013_` | Mortgages or loans on property | `Numeric(Byte)` | `%10.0g` |
| `ho014_` | Years left of mortgage or loan | `Numeric(Byte)` | `%10.0g` |
| `ho015e` | Amount still to pay on mortgage or loan | `Numeric(Float)` | `%10.0g` |
| `ho017_` | Regularly repay mortgage or loans | `Numeric(Byte)` | `%10.0g` |
| `ho022_` | Behind with regular repay mortgage or loan | `Numeric(Byte)` | `%10.0g` |
| `ho023_` | Sublet or let parts of accommodation | `Numeric(Byte)` | `%10.0g` |
| `ho024e` | Value of property | `Numeric(Float)` | `%10.0g` |
| `ho026_` | Own other real estate | `Numeric(Byte)` | `%10.0g` |
| `ho027e` | Value of other real estate | `Numeric(Float)` | `%10.0g` |
| `ho029_` | Received income or rent of other real estate | `Numeric(Byte)` | `%10.0g` |
| `ho030e` | Amount income or rent of other real estate last year | `Numeric(Float)` | `%10.0g` |
| `ho032_` | Number of rooms in accommodation | `Numeric(Byte)` | `%10.0g` |
| `ho034_` | Years in accommodation | `Numeric(Int)` | `%10.0g` |
| `ho037_` | Area where respondent lives | `Numeric(Byte)` | `%38.0g` |
| `ho041_` | Who answered the questions in ho | `Numeric(Byte)` | `%44.0g` |
| `ho043_` | Number of steps to entrance | `Numeric(Byte)` | `%12.0g` |
| `ho054_` | Elevator | `Numeric(Byte)` | `%10.0g` |
| `ho060_` | Partner years in accomodation | `Numeric(Byte)` | `%10.0g` |
| `ho061_` | Years in accommodation | `Numeric(Byte)` | `%10.0g` |
| `ho067e` | Amount similar dwelling todays market | `Numeric(Float)` | `%10.0g` |
| `ho070_` | Percentage of house owned | `Numeric(Byte)` | `%10.0g` |
| `ho074e` | Income from sublet of accomodation | `Numeric(Float)` | `%10.0g` |
| `ho075_` | Own other real estate/houses | `Numeric(Byte)` | `%10.0g` |
| `ho076e` | Worth of properties if now sold | `Numeric(Float)` | `%10.0g` |
| `ho077_` | Receive rent or income from properties | `Numeric(Byte)` | `%10.0g` |
| `ho078e` | Amount of income from properties | `Numeric(Float)` | `%10.0g` |
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
| `ho611d1` | How property acquired: own means | `Numeric(Byte)` | `%12.0g` |
| `ho611d2` | How property acquired: loan/mortgage | `Numeric(Byte)` | `%12.0g` |
| `ho611d3` | How property acquired: help from family | `Numeric(Byte)` | `%12.0g` |
| `ho611d4` | How property acquired: bequest | `Numeric(Byte)` | `%12.0g` |
| `ho611d5` | How property acquired: gift | `Numeric(Byte)` | `%12.0g` |
| `ho611d6` | How property acquired: other means | `Numeric(Byte)` | `%12.0g` |
| `ho620e` | Amount payed for mortgages/loans on property last 12 months | `Numeric(Float)` | `%10.0g` |
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
| `ho636_` | Type of building | `Numeric(Byte)` | `%94.0g` |
| `ho662_` | Has to pay out-of-pocket for nursing home accommodation | `Numeric(Byte)` | `%10.0g` |
| `ho665e` | Amount paying out-of-pocket for nursing home a typical month | `Numeric(Float)` | `%10.0g` |
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

- Dataset: `sharew7_rel9-0-0_it.dta`
- Read with: `ps.read_share_module("it", wave=7)`
- Rows: 77,181
- Variables: 10
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `it001_` | Current job requires using a computer | `Numeric(Byte)` | `%10.0g` |
| `it002_` | Last job before retiring required using a computer | `Numeric(Byte)` | `%10.0g` |
| `it003_` | Computer skills | `Numeric(Byte)` | `%51.0g` |
| `it004_` | Use of internet in past 7 days | `Numeric(Byte)` | `%10.0g` |

### `iv` - Interviewer Observations

- Dataset: `sharew7_rel9-0-0_iv.dta`
- Read with: `ps.read_share_module("iv", wave=7)`
- Rows: 77,181
- Variables: 27
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
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
| `iv012_` | Number of steps to entrance | `Numeric(Byte)` | `%12.0g` |
| `iv018_` | Help needed reading showcards | `Numeric(Byte)` | `%30.0g` |
| `iv020_` | Relationship proxy | `Numeric(Byte)` | `%37.0g` |
| `iv610_` | Type of building hh lives in | `Numeric(Byte)` | `%94.0g` |
| `iv621_` | Certified nurse | `Numeric(Byte)` | `%10.0g` |

### `mh` - Mental Health

- Dataset: `sharew7_rel9-0-0_mh.dta`
- Read with: `ps.read_share_module("mh", wave=7)`
- Rows: 77,181
- Variables: 27
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `mh002_` | Sad or depressed last month | `Numeric(Byte)` | `%10.0g` |
| `mh003_` | Hopes for the future | `Numeric(Byte)` | `%31.0g` |
| `mh004_` | Suicidal feelings or wish to be dead | `Numeric(Byte)` | `%61.0g` |
| `mh005_` | Feels guilty | `Numeric(Byte)` | `%128.0g` |
| `mh006_` | Blame for what | `Numeric(Byte)` | `%186.0g` |
| `mh007_` | Trouble sleeping | `Numeric(Byte)` | `%73.0g` |
| `mh008_` | Less or same interest in things | `Numeric(Byte)` | `%46.0g` |
| `mh009_` | Keeps up interest | `Numeric(Byte)` | `%10.0g` |
| `mh010_` | Irritability | `Numeric(Byte)` | `%10.0g` |
| `mh011_` | Appetite | `Numeric(Byte)` | `%46.0g` |
| `mh012_` | Eating more or less | `Numeric(Byte)` | `%21.0g` |
| `mh013_` | Fatigue | `Numeric(Byte)` | `%10.0g` |
| `mh014_` | Concentration on entertainment | `Numeric(Byte)` | `%74.0g` |
| `mh015_` | Concentration on reading | `Numeric(Byte)` | `%48.0g` |
| `mh016_` | Enjoyment | `Numeric(Byte)` | `%71.0g` |
| `mh017_` | Tearfulness | `Numeric(Byte)` | `%10.0g` |
| `mh032_` | End non proxy | `Numeric(Byte)` | `%59.0g` |
| `mh034_` | Feels lack of companionship | `Numeric(Byte)` | `%20.0g` |
| `mh035_` | Feels left out | `Numeric(Byte)` | `%20.0g` |
| `mh036_` | Feels isolated from others | `Numeric(Byte)` | `%20.0g` |
| `mh037_` | Feels lonely | `Numeric(Byte)` | `%20.0g` |

### `ph` - Physical Health

- Dataset: `sharew7_rel9-0-0_ph.dta`
- Read with: `ps.read_share_module("ph", wave=7)`
- Rows: 77,181
- Variables: 196
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ph003_` | Health in general question 2 | `Numeric(Byte)` | `%13.0g` |
| `ph004_` | Long-term illness | `Numeric(Byte)` | `%10.0g` |
| `ph005_` | Limited in activities because of health | `Numeric(Byte)` | `%32.0g` |
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
| `ph043_` | Eyesight distance | `Numeric(Byte)` | `%13.0g` |
| `ph044_` | Eyesight reading | `Numeric(Byte)` | `%13.0g` |
| `ph045_` | Use hearing aid | `Numeric(Byte)` | `%10.0g` |
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
| `ph049d14` | Difficulties: leaving the house independently/accessing transportation | `Numeric(Byte)` | `%12.0g` |
| `ph049d15` | Difficulties: doing personal laundry | `Numeric(Byte)` | `%12.0g` |
| `ph049dno` | Difficulties: none of these | `Numeric(Byte)` | `%12.0g` |
| `ph050_` | Help activities | `Numeric(Byte)` | `%10.0g` |
| `ph051_` | Help meets needs | `Numeric(Byte)` | `%12.0g` |
| `ph054_` | Who answered the questions in ph | `Numeric(Byte)` | `%44.0g` |
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
| `ph066_` | Reason lost weight | `Numeric(Byte)` | `%51.0g` |
| `ph071_1` | How many heart attacks since last interview | `Numeric(Byte)` | `%11.0g` |
| `ph071_2` | How many strokes/diagnosed cerebral vascular disease since last interview | `Numeric(Byte)` | `%11.0g` |
| `ph071_3` | How often diagnosed with cancer since last interview | `Numeric(Byte)` | `%11.0g` |
| `ph071_4` | How often suffered a hip fracture since last interview | `Numeric(Byte)` | `%11.0g` |
| `ph072_1` | Had a heart attack since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph072_2` | Had a stroke/diagnosed with cerebral vascular disease since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph072_3` | Been diagnosed with cancer since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph072_4` | Suffered a hip fracture since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph076_1` | Year most recent condition: heart atttack | `Numeric(Byte)` | `%10.0g` |
| `ph076_2` | Year most recent condition: stroke/cerebral vascular disease | `Numeric(Byte)` | `%10.0g` |
| `ph076_3` | Year most recent condition: cancer | `Numeric(Byte)` | `%10.0g` |
| `ph076_4` | Year most recent condition: hip fracture | `Numeric(Byte)` | `%10.0g` |
| `ph077_1` | Month most recent condition: heart atttack | `Numeric(Byte)` | `%10.0g` |
| `ph077_2` | Month most recent condition: stroke/cerebral vascular disease | `Numeric(Byte)` | `%10.0g` |
| `ph077_3` | Month most recent condition: cancer | `Numeric(Byte)` | `%10.0g` |
| `ph077_4` | Month most recent condition: hip fracture | `Numeric(Byte)` | `%10.0g` |
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
| `ph085_` | Level of pain | `Numeric(Byte)` | `%13.0g` |
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

### `sp` - Social Support

- Dataset: `sharew7_rel9-0-0_sp.dta`
- Read with: `ps.read_share_module("sp", wave=7)`
- Rows: 77,181
- Variables: 161
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sp002_` | Received help from others (outside hh) | `Numeric(Byte)` | `%10.0g` |
| `sp003_1` | Who gave help: person 1 | `Numeric(Byte)` | `%56.0g` |
| `sp003_2` | Who gave help: person 2 | `Numeric(Byte)` | `%56.0g` |
| `sp003_3` | Who gave help: person 3 | `Numeric(Byte)` | `%56.0g` |
| `sp004d1_1` | Help provided from person 1: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp004d1_2` | Help provided from person 2: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp004d1_3` | Help provided from person 3: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp004d2_1` | Help provided from person 1: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp004d2_2` | Help provided from person 2: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp004d2_3` | Help provided from person 3: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp004d3_1` | Help provided from person 1: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp004d3_2` | Help provided from person 2: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp004d3_3` | Help provided from person 3: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp005_1` | How often received help: from person 1 | `Numeric(Byte)` | `%22.0g` |
| `sp005_2` | How often received help: from person 2 | `Numeric(Byte)` | `%22.0g` |
| `sp005_3` | How often received help: from person 3 | `Numeric(Byte)` | `%22.0g` |
| `sp007_1` | Any other helper from outside the household | `Numeric(Byte)` | `%10.0g` |
| `sp007_2` | Any other helper from outside the household | `Numeric(Byte)` | `%10.0g` |
| `sp007_3` | Any other helper from outside the household | `Numeric(Byte)` | `%10.0g` |
| `sp008_` | Given help last twelve months | `Numeric(Byte)` | `%10.0g` |
| `sp009_1` | To whom did you give help: person 1 | `Numeric(Byte)` | `%56.0g` |
| `sp009_2` | To whom did you give help: person 2 | `Numeric(Byte)` | `%56.0g` |
| `sp009_3` | To whom did you give help: person 3 | `Numeric(Byte)` | `%56.0g` |
| `sp010d1_1` | Help given person 1: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp010d1_2` | Help given person 2: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp010d1_3` | Help given person 3: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp010d2_1` | Help given person 1: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp010d2_2` | Help given person 2: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp010d2_3` | Help given person 3: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp010d3_1` | Help given person 1: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp010d3_2` | Help given person 2: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp010d3_3` | Help given person 3: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp011_1` | How often given help to person 1 | `Numeric(Byte)` | `%22.0g` |
| `sp011_2` | How often given help to person 2 | `Numeric(Byte)` | `%22.0g` |
| `sp011_3` | How often given help to person 3 | `Numeric(Byte)` | `%22.0g` |
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
| `sp016_1` | How often did you look after child of child 1 | `Numeric(Byte)` | `%22.0g` |
| `sp016_2` | How often did you look after child of child 2 | `Numeric(Byte)` | `%22.0g` |
| `sp016_3` | How often did you look after child of child 3 | `Numeric(Byte)` | `%22.0g` |
| `sp016_4` | How often did you look after child of child 4 | `Numeric(Byte)` | `%22.0g` |
| `sp016_5` | How often did you look after child of child 5 | `Numeric(Byte)` | `%22.0g` |
| `sp016_6` | How often did you look after child of child 6 | `Numeric(Byte)` | `%22.0g` |
| `sp016_7` | How often did you look after child of child 7 | `Numeric(Byte)` | `%22.0g` |
| `sp016_8` | How often did you look after child of child 8 | `Numeric(Byte)` | `%22.0g` |
| `sp016_9` | How often did you look after child of child 9 | `Numeric(Byte)` | `%22.0g` |
| `sp016_10` | How often did you look after child of child 10 | `Numeric(Byte)` | `%22.0g` |
| `sp016_11` | How often did you look after child of child 11 | `Numeric(Byte)` | `%22.0g` |
| `sp016_12` | How often did you look after child of child 12 | `Numeric(Byte)` | `%22.0g` |
| `sp016_13` | How often did you look after child of child 13 | `Numeric(Byte)` | `%22.0g` |
| `sp016_14` | How often did you look after child of child 14 | `Numeric(Byte)` | `%22.0g` |
| `sp016_15` | How often do you look after child of child 15 | `Numeric(Byte)` | `%22.0g` |
| `sp016_16` | How often do you look after child of child 16 | `Numeric(Byte)` | `%22.0g` |
| `sp016_17` | How often do you look after child of child 17 | `Numeric(Byte)` | `%22.0g` |
| `sp016_18` | How often do you look after child of child 18 | `Numeric(Byte)` | `%22.0g` |
| `sp016_19` | How often do you look after child of child 19 | `Numeric(Byte)` | `%22.0g` |
| `sp016_20` | How often do you look after child of child 20 | `Numeric(Byte)` | `%22.0g` |
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
| `sp022_` | Who answered the questions in sp | `Numeric(Byte)` | `%44.0g` |
| `sp027_1` | From which child R received help | `Numeric(Byte)` | `%14.0g` |
| `sp027_2` | From which child R received help | `Numeric(Byte)` | `%14.0g` |
| `sp027_3` | From which child R received help | `Numeric(Byte)` | `%14.0g` |
| `sp029_1` | To which child R gave help | `Numeric(Byte)` | `%14.0g` |
| `sp029_2` | To which child R gave help | `Numeric(Byte)` | `%14.0g` |
| `sp029_3` | To which child R gave help | `Numeric(Byte)` | `%14.0g` |
| `sp031_1` | To which child in household R gave help with personal care | `Numeric(Byte)` | `%14.0g` |
| `sp031_2` | To which child in household R gave help with personal care | `Numeric(Byte)` | `%14.0g` |
| `sp031_3` | To which child in household R gave help with personal care | `Numeric(Byte)` | `%14.0g` |
| `sp033_1` | From which child in household R received help with personal care | `Numeric(Byte)` | `%14.0g` |
| `sp033_2` | From which child in household R received help with personal care | `Numeric(Byte)` | `%14.0g` |
| `sp033_3` | From which child in household R received help with personal care | `Numeric(Byte)` | `%14.0g` |
| `sp033_4` | From which child in household R received help with personal care | `Numeric(Byte)` | `%14.0g` |
| `sp033_5` | From which child in household R received help with personal care | `Numeric(Byte)` | `%14.0g` |
| `sp033_6` | From which child in household R received help with personal care | `Numeric(Byte)` | `%14.0g` |
| `sp033_7` | From which child in household R received help with personal care | `Numeric(Byte)` | `%14.0g` |

### `xt` - End-of-Life Interview

- Dataset: `sharew7_rel9-0-0_xt.dta`
- Read with: `ps.read_share_module("xt", wave=7)`
- Rows: 3,661
- Variables: 221
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language_xt` | Language: End of life interview | `Numeric(Byte)` | `%44.0g` |
| `gender_xt` | Gender of the deceased | `Numeric(Byte)` | `%10.0g` |
| `yrbirth_xt` | Year of birth of the deceased | `Numeric(Int)` | `%10.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `xt002_` | Relationship to the deceased | `Numeric(Byte)` | `%50.0g` |
| `xt005_` | How often contact last twelve month | `Numeric(Byte)` | `%27.0g` |
| `xt006_` | Proxy respondent's sex | `Numeric(Byte)` | `%10.0g` |
| `xt007_` | Year of birth proxy | `Numeric(Int)` | `%10.0g` |
| `xt008_` | Month of decease | `Numeric(Byte)` | `%10.0g` |
| `xt009_` | Year of decease | `Numeric(Int)` | `%10.0g` |
| `xt010_` | Age at the moment of decease | `Numeric(Int)` | `%10.0g` |
| `xt011_` | Main cause of death | `Numeric(Byte)` | `%103.0g` |
| `xt012c` | Main cause of death: xt012 coded | `Numeric(Byte)` | `%60.0g` |
| `xt013_` | How long been ill before decease | `Numeric(Byte)` | `%51.0g` |
| `xt014_` | Place of dying | `Numeric(Byte)` | `%56.0g` |
| `xt016_` | Total time in hospital last year before dying | `Numeric(Byte)` | `%53.0g` |
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
| `xt024_` | Time the deceased received help | `Numeric(Byte)` | `%51.0g` |
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
| `xt039_` | Number of children (still alive) deceased had at the end | `Numeric(Int)` | `%10.0g` |
| `xt040a_` | Estate divided among children | `Numeric(Byte)` | `%67.0g` |
| `xt040b_` | Some children received more to make up for previous gifts | `Numeric(Byte)` | `%10.0g` |
| `xt040c_` | Some children received more to give them financial support | `Numeric(Byte)` | `%10.0g` |
| `xt040d_` | Some children received more because they helped/cared for deceased | `Numeric(Byte)` | `%10.0g` |
| `xt040e_` | Some children received more because of other reasons | `Numeric(Byte)` | `%10.0g` |
| `xt041_` | Funeral was accompanied by a religious ceremony | `Numeric(Byte)` | `%10.0g` |
| `xt043_` | Interview mode | `Numeric(Byte)` | `%23.0g` |
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
| `xt119v1_1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt119v1_2` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt119v1_3` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt119v1_4` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `xt119v1_5` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `xt119v1_6` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt119v1_7` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt119v1_8` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt119v1_9` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt119v2_1` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt119v2_2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt119v2_3` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt119v2_4` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `xt119v2_5` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `xt119v2_6` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt119v2_7` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt119v2_8` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt119v2_9` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt119v3_1` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt119v3_2` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt119v3_3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt119v3_4` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `xt119v3_5` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `xt119v3_6` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt119v3_7` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
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
| `xt622_` | Anyone helped with ADLII | `Numeric(Byte)` | `%10.0g` |
| `xt623d1` | Who has helped with ADLII: yourself (proxy respondent) | `Numeric(Byte)` | `%12.0g` |
| `xt623d2` | Who has helped with ADLII: spouse/partner of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt623d3` | Who has helped with ADLII: mother/father of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt623d4` | Who has helped with ADLII: son of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt623d5` | Who has helped with ADLII: son-in-law of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt623d6` | Who has helped with ADLII: daughter of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt623d7` | Who has helped with ADLII: daughter-in-law of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt623d8` | Who has helped with ADLII: grandson of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt623d9` | Who has helped with ADLII: granddaughter of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt623d10` | Who has helped with ADLII: sister of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt623d11` | Who has helped with ADLII: brother of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt623d12` | Who has helped with ADLII: other relative | `Numeric(Byte)` | `%12.0g` |
| `xt623d13` | Who has helped with ADLII: unpaid volunteer | `Numeric(Byte)` | `%12.0g` |
| `xt623d14` | Who has helped with ADLII: professional helper | `Numeric(Byte)` | `%12.0g` |
| `xt623d15` | Who has helped with ADLII: friend/neighbor of deceased | `Numeric(Byte)` | `%12.0g` |
| `xt623dot` | Who has helped with ADLII: other person | `Numeric(Byte)` | `%12.0g` |
| `xt624_` | Time the deceased received help with ADLII | `Numeric(Byte)` | `%51.0g` |
| `xt625_` | Hours of help with ADLII necessary during typical day | `Numeric(Byte)` | `%10.0g` |
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
| `xt638v1_1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt638v1_2` | Bracket value 1 | `Numeric(Double)` | `%12.0g` |
| `xt638v1_3` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt638v1_4` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt638v1_5` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `xt638v2_1` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt638v2_2` | Bracket value 2 | `Numeric(Double)` | `%12.0g` |
| `xt638v2_3` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt638v2_4` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt638v2_5` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `xt638v3_1` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt638v3_2` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `xt638v3_3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt638v3_4` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt638v3_5` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `xt750_` | Intensive care unit | `Numeric(Byte)` | `%10.0g` |
| `xt751_` | Palliative care or inpatient hospice unit | `Numeric(Byte)` | `%10.0g` |
| `xt752_` | Inpatient hospice unit | `Numeric(Byte)` | `%10.0g` |
| `xt753_` | Residential provided by hospice | `Numeric(Byte)` | `%10.0g` |
| `xt754_` | Reason no hospice or palliative care | `Numeric(Byte)` | `%57.0g` |
| `xt757_` | Hospice or palliative care | `Numeric(Byte)` | `%10.0g` |
| `xt758_` | Take medicine for pain | `Numeric(Byte)` | `%10.0g` |
| `xt759_` | Medication amount | `Numeric(Byte)` | `%13.0g` |
| `xt760_` | Trouble breathing | `Numeric(Byte)` | `%10.0g` |
| `xt761_` | How much help breathing | `Numeric(Byte)` | `%12.0g` |
| `xt762_` | Feelings of anxiety or sadness | `Numeric(Byte)` | `%10.0g` |
| `xt763_` | How much help with anxiety or sadness | `Numeric(Byte)` | `%12.0g` |
| `xt764_` | How often personal care needs met | `Numeric(Byte)` | `%70.0g` |
| `xt765_` | How often was staff caring and respectful | `Numeric(Byte)` | `%52.0g` |
| `xt766_` | Rate care | `Numeric(Byte)` | `%13.0g` |
| `xt767_` | Certified nurse | `Numeric(Byte)` | `%10.0g` |


## Special Modules

### `dropoff` - Paper-and-pencil drop-off

- Dataset: `sharew7_rel9-0-0_dropoff.dta`
- Read with: `ps.read_share_module("dropoff", wave=7)`
- Rows: 24,677
- Variables: 809
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `yrbirth_do` | Year of birth | `Numeric(Int)` | `%11.0g` |
| `gender_do` | Gender | `Numeric(Byte)` | `%27.0g` |
| `at_f1x1` | Motivating factor to work - social status | `Numeric(Byte)` | `%21.0g` |
| `at_f1x2` | Motivating factor to work - implement my abilities | `Numeric(Byte)` | `%21.0g` |
| `at_f1x3` | Motivating factor to work - community | `Numeric(Byte)` | `%21.0g` |
| `at_f1x4` | Motivating factor to work - creative freedom | `Numeric(Byte)` | `%21.0g` |
| `at_f1x5` | Motivating factor to work - independence | `Numeric(Byte)` | `%21.0g` |
| `at_f1x6` | Motivating factor to work - ensure basic means for living | `Numeric(Byte)` | `%21.0g` |
| `at_f1x7` | Motivating factor to work - big money | `Numeric(Byte)` | `%21.0g` |
| `at_f2` | Got desired profession? | `Numeric(Byte)` | `%27.0g` |
| `at_f3` | Satisfaction with main job | `Numeric(Byte)` | `%27.0g` |
| `at_f4` | Obtained desired education | `Numeric(Byte)` | `%11.0g` |
| `at_f5` | Satisfaction with training & education | `Numeric(Byte)` | `%19.0g` |
| `at_f6` | Other education/training - professional life more successful? | `Numeric(Byte)` | `%28.0g` |
| `at_f7` | Which other education/training | `Numeric(Byte)` | `%45.0g` |
| `at_f8` | Receives public pension | `Numeric(Byte)` | `%10.0g` |
| `at_f9` | Retrospectively chosen retirement age | `Numeric(Byte)` | `%41.0g` |
| `at_f10x1` | Postponed retirement by reducing working hours - No | `Numeric(Byte)` | `%12.0g` |
| `at_f10x2` | Postponed retirement by reducing working hours - Yes, reduce unpaid extra hours | `Numeric(Byte)` | `%12.0g` |
| `at_f10x3` | Postponed retirement by reducing working hours - Yes, reduce paid extra hours | `Numeric(Byte)` | `%12.0g` |
| `at_f10x4` | Postponed retirement by reducing working hours - Yes, part-time | `Numeric(Byte)` | `%12.0g` |
| `at_f10x5` | Postponed retirement by reducing working hours - Yes, part-time with income comp | `Numeric(Byte)` | `%12.0g` |
| `at_f10x6` | Postponed retirement by reducing working hours - Don't know | `Numeric(Byte)` | `%12.0g` |
| `at_f10x7` | Postponed retirement by reducing working hours - No answer | `Numeric(Byte)` | `%12.0g` |
| `at_f11` | Postponed retirement for higher payments | `Numeric(Byte)` | `%10.0g` |
| `at_f12` | Increase in pension payment to postpone pension by one year | `Numeric(Int)` | `%16.0g` |
| `at_f13` | Retired and work for payment | `Numeric(Byte)` | `%10.0g` |
| `at_f14x1` | Reason to work in retirement - pension not sufficient | `Numeric(Byte)` | `%21.0g` |
| `at_f14x2` | Reason to work in retirement - financially support related persons | `Numeric(Byte)` | `%21.0g` |
| `at_f14x3` | Reason to work in retirement - temporary financial problems | `Numeric(Byte)` | `%21.0g` |
| `at_f14x4` | Reason to work in retirement - hobby | `Numeric(Byte)` | `%21.0g` |
| `at_f14x5` | Reason to work in retirement - extra money | `Numeric(Byte)` | `%21.0g` |
| `at_f14x6` | Reason to work in retirement - communication | `Numeric(Byte)` | `%21.0g` |
| `at_f14x7` | Reason to work in retirement - fun | `Numeric(Byte)` | `%21.0g` |
| `at_f15` | Work even need to change profession? | `Numeric(Byte)` | `%44.0g` |
| `at_f16` | Work OR retire? | `Numeric(Byte)` | `%26.0g` |
| `at_f17` | Currently employed? | `Numeric(Byte)` | `%10.0g` |
| `at_f18` | Planned retirement | `Numeric(Byte)` | `%39.0g` |
| `at_f19x1` | Postpone retirement by reducing working hours - No | `Numeric(Byte)` | `%12.0g` |
| `at_f19x2` | Postpone retirement by reducing working hours - Yes, reduce unpaid extra hours | `Numeric(Byte)` | `%12.0g` |
| `at_f19x3` | Postpone retirement by reducing working hours - Yes, reduce paid extra hours | `Numeric(Byte)` | `%12.0g` |
| `at_f19x4` | Postpone retirement by reducing working hours - Yes, part-time | `Numeric(Byte)` | `%12.0g` |
| `at_f19x5` | Postpone retirement by reducing working hours - Yes, part-time with income compe | `Numeric(Byte)` | `%12.0g` |
| `at_f19x6` | Postpone retirement by reducing working hours - Don't know | `Numeric(Byte)` | `%12.0g` |
| `at_f19x7` | Postpone retirement by reducing working hours - No answer | `Numeric(Byte)` | `%12.0g` |
| `at_f20` | Postpone retirement for higher pension payment? | `Numeric(Byte)` | `%10.0g` |
| `at_f21` | Increase in pension payment to postpone pension by one year | `Numeric(Int)` | `%16.0g` |
| `at_f22` | Tired of work | `Numeric(Byte)` | `%14.0g` |
| `at_f23` | Work even need to change profession? | `Numeric(Byte)` | `%10.0g` |
| `at_f24` | Place of living in 5 years | `Numeric(Byte)` | `%21.0g` |
| `at_f25` | Kind of place of living in 5 years | `Numeric(Byte)` | `%17.0g` |
| `at_f26` | Size of place of living in 5 years | `Numeric(Byte)` | `%19.0g` |
| `ch_q1` | would like to live until age | `Numeric(Int)` | `%27.0g` |
| `ch_q1a` | would like to live until age (don't know) | `Numeric(Byte)` | `%27.0g` |
| `ch_q2a` | important today: standard of living | `Numeric(Byte)` | `%27.0g` |
| `ch_q2b` | important today: personal safety | `Numeric(Byte)` | `%27.0g` |
| `ch_q2c` | important today: health & healthy lifestyle | `Numeric(Byte)` | `%27.0g` |
| `ch_q2d` | important today: partnership and family | `Numeric(Byte)` | `%27.0g` |
| `ch_q2e` | important today: friends and social relationships | `Numeric(Byte)` | `%27.0g` |
| `ch_q2f` | important today: community participation | `Numeric(Byte)` | `%27.0g` |
| `ch_q2g` | important today: free time | `Numeric(Byte)` | `%27.0g` |
| `ch_q2h` | important today: religious beliefs | `Numeric(Byte)` | `%27.0g` |
| `ch_q2i` | important today: professional career and achievement (current or past job) | `Numeric(Byte)` | `%27.0g` |
| `ch_q2j` | important today: personal development and growth (having new experiences ...) | `Numeric(Byte)` | `%27.0g` |
| `ch_q2k` | important today: making a difference | `Numeric(Byte)` | `%27.0g` |
| `ch_q2l` | important today: enjoying myself in everyday life | `Numeric(Byte)` | `%27.0g` |
| `ch_q3a` | important when 25: standard of living | `Numeric(Byte)` | `%27.0g` |
| `ch_q3b` | important when 25: personal safety | `Numeric(Byte)` | `%27.0g` |
| `ch_q3c` | important when 25: health & healthy lifestyle | `Numeric(Byte)` | `%27.0g` |
| `ch_q3d` | important when 25: partnership and family | `Numeric(Byte)` | `%27.0g` |
| `ch_q3e` | important when 25: friends and social relationships | `Numeric(Byte)` | `%27.0g` |
| `ch_q3f` | important when 25: community participation | `Numeric(Byte)` | `%27.0g` |
| `ch_q3g` | important when 25: free time | `Numeric(Byte)` | `%27.0g` |
| `ch_q3h` | important when 25: religious beliefs | `Numeric(Byte)` | `%27.0g` |
| `ch_q3i` | important when 25: professional career and achievement (current or past job) | `Numeric(Byte)` | `%27.0g` |
| `ch_q3j` | important when 25: personal development and growth (having new experiences ...) | `Numeric(Byte)` | `%27.0g` |
| `ch_q3k` | important when 25: making a difference | `Numeric(Byte)` | `%27.0g` |
| `ch_q3l` | important when 25: enjoying myself in everyday life | `Numeric(Byte)` | `%27.0g` |
| `ch_q4a` | regret: way handled personal finances | `Numeric(Byte)` | `%27.0g` |
| `ch_q4b` | regret: decisions about education | `Numeric(Byte)` | `%27.0g` |
| `ch_q4c` | regret: decisions about career | `Numeric(Byte)` | `%27.0g` |
| `ch_q4d` | regret: decisions affect family | `Numeric(Byte)` | `%27.0g` |
| `ch_q4e` | regret: way handled friendships & personal relationships | `Numeric(Byte)` | `%27.0g` |
| `ch_q4f` | regret: decisions affect health | `Numeric(Byte)` | `%27.0g` |
| `ch_q4g` | regret: way pursued leisure | `Numeric(Byte)` | `%27.0g` |
| `ch_q4h` | regret: not being more ... | `Numeric(Byte)` | `%27.0g` |
| `ch_q4i` | regret: did not focus enough on joys of everyday | `Numeric(Byte)` | `%27.0g` |
| `ch_q4j` | regret: wrong decisions in life in general | `Numeric(Byte)` | `%27.0g` |
| `ch_q5a` | satisfied with current life: life as a whole | `Numeric(Byte)` | `%27.0g` |
| `ch_q5b` | satisfied with current life: standard of living | `Numeric(Byte)` | `%27.0g` |
| `ch_q5c` | satisfied with current life: personal safety | `Numeric(Byte)` | `%27.0g` |
| `ch_q5d` | satisfied with current life: health | `Numeric(Byte)` | `%27.0g` |
| `ch_q5e` | satisfied with current life: family relationships | `Numeric(Byte)` | `%27.0g` |
| `ch_q5f` | satisfied with current life: friends and social relationships | `Numeric(Byte)` | `%27.0g` |
| `ch_q5g` | satisfied with current life: home/residence | `Numeric(Byte)` | `%27.0g` |
| `ch_q5h` | satisfied with current life: neighborhood/local environment | `Numeric(Byte)` | `%27.0g` |
| `ch_q5i` | satisfied with current life: amount of free time | `Numeric(Byte)` | `%27.0g` |
| `ch_q5j` | satisfied with current life: overall achievements in life | `Numeric(Byte)` | `%27.0g` |
| `ch_q6` | yesterday: which day of week? | `Numeric(Byte)` | `%27.0g` |
| `ch_q7a` | feelings yesterday: enjoyment | `Numeric(Byte)` | `%27.0g` |
| `ch_q7b` | feelings yesterday: calm/relaxed | `Numeric(Byte)` | `%27.0g` |
| `ch_q7c` | feelings yesterday: worry | `Numeric(Byte)` | `%27.0g` |
| `ch_q7d` | feelings yesterday: sadness | `Numeric(Byte)` | `%27.0g` |
| `ch_q7e` | feelings yesterday: happiness | `Numeric(Byte)` | `%27.0g` |
| `ch_q7f` | feelings yesterday: anger | `Numeric(Byte)` | `%27.0g` |
| `ch_q7g` | feelings yesterday: stress/rush | `Numeric(Byte)` | `%27.0g` |
| `ch_q7h` | feelings yesterday: tiredness | `Numeric(Byte)` | `%27.0g` |
| `ch_q7i` | feelings yesterday: hope | `Numeric(Byte)` | `%27.0g` |
| `ch_q7j` | feelings yesterday: gratitude | `Numeric(Byte)` | `%27.0g` |
| `ch_q7k` | feelings yesterday: shame | `Numeric(Byte)` | `%27.0g` |
| `ch_q7l` | feelings yesterday: love | `Numeric(Byte)` | `%27.0g` |
| `ch_q7m` | feelings yesterday: boredom | `Numeric(Byte)` | `%27.0g` |
| `ch_q7n` | feelings yesterday: pain | `Numeric(Byte)` | `%27.0g` |
| `ch_q7o` | feelings yesterday: irritability | `Numeric(Byte)` | `%27.0g` |
| `ch_q7p` | feelings yesterday: content | `Numeric(Byte)` | `%27.0g` |
| `ch_q7q` | feelings yesterday: frustration | `Numeric(Byte)` | `%27.0g` |
| `ch_q7r` | feelings yesterday: motivation | `Numeric(Byte)` | `%27.0g` |
| `ch_q7s` | feelings yesterday: resignation | `Numeric(Byte)` | `%27.0g` |
| `ch_q7t` | feelings yesterday: hostility | `Numeric(Byte)` | `%27.0g` |
| `ch_q7u` | feelings yesterday: nervousness | `Numeric(Byte)` | `%27.0g` |
| `ch_q7v` | feelings yesterday: loneliness | `Numeric(Byte)` | `%27.0g` |
| `ch_q7w` | feelings yesterday: reward | `Numeric(Byte)` | `%27.0g` |
| `ch_q7x` | feelings yesterday: purpose | `Numeric(Byte)` | `%27.0g` |
| `ch_q8am` | time use yesterday (m): doing housework or yardwork | `Numeric(Byte)` | `%27.0g` |
| `ch_q8as` | time use yesterday (h): doing housework or yardwork | `Numeric(Byte)` | `%27.0g` |
| `ch_q8bm` | time use yesterday (m): working for pay | `Numeric(Byte)` | `%27.0g` |
| `ch_q8bs` | time use yesterday (h): working for pay | `Numeric(Byte)` | `%27.0g` |
| `ch_q8cm` | time use yesterday (m): caring for sick/disabled/frail person | `Numeric(Byte)` | `%27.0g` |
| `ch_q8cs` | time use yesterday (h): caring for sick/disabled/frail person | `Numeric(Byte)` | `%27.0g` |
| `ch_q8dm` | time use yesterday (m): volunteering | `Numeric(Byte)` | `%27.0g` |
| `ch_q8ds` | time use yesterday (h): volunteering | `Numeric(Byte)` | `%27.0g` |
| `ch_q8em` | time use yesterday (m): walk or exercising | `Numeric(Byte)` | `%27.0g` |
| `ch_q8es` | time use yesterday (h): walk or exercising | `Numeric(Byte)` | `%27.0g` |
| `ch_q8fm` | time use yesterday (m): healthcare and self-care | `Numeric(Byte)` | `%27.0g` |
| `ch_q8fs` | time use yesterday (h): healthcare and self-care | `Numeric(Byte)` | `%27.0g` |
| `ch_q8gm` | time use yesterday (m): traveling or commuting | `Numeric(Byte)` | `%27.0g` |
| `ch_q8gs` | time use yesterday (h): traveling or commuting | `Numeric(Byte)` | `%27.0g` |
| `ch_q8hm` | time use yesterday (m): watching tv | `Numeric(Byte)` | `%27.0g` |
| `ch_q8hs` | time use yesterday (h): watching tv | `Numeric(Byte)` | `%27.0g` |
| `ch_q8im` | time use yesterday (m): listening to radio | `Numeric(Byte)` | `%27.0g` |
| `ch_q8is` | time use yesterday (h): listening to radio | `Numeric(Byte)` | `%27.0g` |
| `ch_q8jm` | time use yesterday (m): reading books, newspaper, magazines | `Numeric(Byte)` | `%27.0g` |
| `ch_q8js` | time use yesterday (h): reading books, newspaper, magazines | `Numeric(Byte)` | `%27.0g` |
| `ch_q8km` | time use yesterday (m): using computer or the Internet | `Numeric(Byte)` | `%27.0g` |
| `ch_q8ks` | time use yesterday (h): using computer or the Internet | `Numeric(Byte)` | `%27.0g` |
| `ch_q8lm` | time use yesterday (m): spending time with/calling family | `Numeric(Byte)` | `%27.0g` |
| `ch_q8ls` | time use yesterday (h): spending time with/calling family | `Numeric(Byte)` | `%27.0g` |
| `ch_q8mm` | time use yesterday (m): spending time with/calling friends | `Numeric(Byte)` | `%27.0g` |
| `ch_q8ms` | time use yesterday (h): spending time with/calling friends | `Numeric(Byte)` | `%27.0g` |
| `ch_q8nm` | time use yesterday (m): staying home alone | `Numeric(Byte)` | `%27.0g` |
| `ch_q8ns` | time use yesterday (h): staying home alone | `Numeric(Byte)` | `%27.0g` |
| `ch_q9` | yesterday: normal or unusual? | `Numeric(Byte)` | `%44.0g` |
| `ch_q10a` | how often in-depth conversation with: spouse or partner | `Numeric(Byte)` | `%27.0g` |
| `ch_q10b` | how often in-depth conversation with: children | `Numeric(Byte)` | `%27.0g` |
| `ch_q10c` | how often in-depth conversation with: grandchildren | `Numeric(Byte)` | `%27.0g` |
| `ch_q10d` | how often in-depth conversation with: other family | `Numeric(Byte)` | `%27.0g` |
| `ch_q10e` | how often in-depth conversation with: friends and acquaintances | `Numeric(Byte)` | `%27.0g` |
| `ch_q11a_myself` | allergies (myself): hayfever, pollen, grass | `Numeric(Byte)` | `%27.0g` |
| `ch_q11a_noone` | allergies (no one in hh): hayfever, pollen, grass | `Numeric(Byte)` | `%27.0g` |
| `ch_q11a_others` | allergies (others in hh): hayfever, pollen, grass | `Numeric(Byte)` | `%27.0g` |
| `ch_q11b_myself` | allergies (myself): dust | `Numeric(Byte)` | `%27.0g` |
| `ch_q11b_noone` | allergies (no one in hh): dust | `Numeric(Byte)` | `%27.0g` |
| `ch_q11b_others` | allergies (others in hh): dust | `Numeric(Byte)` | `%27.0g` |
| `ch_q11c_myself` | allergies (myself): animal hear | `Numeric(Byte)` | `%27.0g` |
| `ch_q11c_noone` | allergies (no one in hh): animal hear | `Numeric(Byte)` | `%27.0g` |
| `ch_q11c_others` | allergies (others in hh): animal hear | `Numeric(Byte)` | `%27.0g` |
| `ch_q11d_myself` | allergies (myself): mold | `Numeric(Byte)` | `%27.0g` |
| `ch_q11d_noone` | allergies (no one in hh): mold | `Numeric(Byte)` | `%27.0g` |
| `ch_q11d_others` | allergies (others in hh): mold | `Numeric(Byte)` | `%27.0g` |
| `ch_q11e_myself` | allergies (myself): foods | `Numeric(Byte)` | `%27.0g` |
| `ch_q11e_noone` | allergies (no one in hh): foods | `Numeric(Byte)` | `%27.0g` |
| `ch_q11e_others` | allergies (others in hh): foods | `Numeric(Byte)` | `%27.0g` |
| `ch_q11f_myself` | allergies (myself): medicine/drugs | `Numeric(Byte)` | `%27.0g` |
| `ch_q11f_noone` | allergies (no one in hh): medicine/drugs | `Numeric(Byte)` | `%27.0g` |
| `ch_q11f_others` | allergies (others in hh): medicine/drugs | `Numeric(Byte)` | `%27.0g` |
| `ch_q12a` | currently have pet(s): dog | `Numeric(Byte)` | `%27.0g` |
| `ch_q12b` | currently have pet(s): cat | `Numeric(Byte)` | `%27.0g` |
| `ch_q12c` | currently have pet(s): bird | `Numeric(Byte)` | `%27.0g` |
| `ch_q12d` | currently have pet(s): fish | `Numeric(Byte)` | `%27.0g` |
| `ch_q12e` | currently have pet(s): other | `Numeric(Byte)` | `%27.0g` |
| `ch_q12e1` | currently have pet(s): other: rodent (hamster, degu, guinea pig, rabbit) | `Numeric(Byte)` | `%27.0g` |
| `ch_q12e2` | currently have pet(s): other: poultry (chicken, hens, cock, duck, quail, goose) | `Numeric(Byte)` | `%27.0g` |
| `ch_q12e3` | currently have pet(s): other: field animal (deer, sheep, goat) | `Numeric(Byte)` | `%27.0g` |
| `ch_q12e4` | currently have pet(s): other: equidae (horse, ponie, donkey) | `Numeric(Byte)` | `%27.0g` |
| `ch_q12e5` | currently have pet(s): other: aquarium and terrarium animal (turtle, snake) | `Numeric(Byte)` | `%27.0g` |
| `ch_q12e6` | currently have pet(s): other: cow | `Numeric(Byte)` | `%27.0g` |
| `ch_q12f` | currently have pet(s): none | `Numeric(Byte)` | `%27.0g` |
| `ch_q13` | whose decision to get the pet(s) | `Numeric(Byte)` | `%29.0g` |
| `ch_q14` | who is mainly responsible for taking care of pet(s) | `Numeric(Byte)` | `%27.0g` |
| `ch_q15a` | relationship to pet(s): enjoy having pet(s) around | `Numeric(Byte)` | `%27.0g` |
| `ch_q15b` | relationship to pet(s): love pet(s) | `Numeric(Byte)` | `%27.0g` |
| `ch_q15c` | relationship to pet(s): pet(s) give me companionship | `Numeric(Byte)` | `%27.0g` |
| `ch_q15d` | relationship to pet(s): very expensive to take care of pet(s) | `Numeric(Byte)` | `%27.0g` |
| `ch_q15e` | relationship to pet(s): love to take care of pet(s) | `Numeric(Byte)` | `%27.0g` |
| `ch_q15f` | relationship to pet(s): pet(s) is/are my friend(s) | `Numeric(Byte)` | `%27.0g` |
| `ch_q15g` | relationship to pet(s): talk to pet(s) | `Numeric(Byte)` | `%27.0g` |
| `ch_q15h` | relationship to pet(s): pet(s) add to happiness | `Numeric(Byte)` | `%27.0g` |
| `ch_q15i` | relationship to pet(s): often play with pet(s) | `Numeric(Byte)` | `%27.0g` |
| `ch_q15j` | relationship to pet(s): talk about pet(s) | `Numeric(Byte)` | `%27.0g` |
| `ch_q15k` | relationship to pet(s): pet(s) makes me go outside | `Numeric(Byte)` | `%27.0g` |
| `ch_q15l` | relationship to pet(s): pet(s) help me to engage with other people | `Numeric(Byte)` | `%27.0g` |
| `ch_q15m` | relationship to pet(s): pet knows how I feel about things | `Numeric(Byte)` | `%27.0g` |
| `ch_q15n` | relationship to pet(s): pet(s) go(es) on my nerves | `Numeric(Byte)` | `%27.0g` |
| `ch_q15o` | relationship to pet(s): hard work to care of pet(s) | `Numeric(Byte)` | `%27.0g` |
| `cz_version` | Version (A = retired, B = not retired) | `Numeric(Byte)` | `%15.0g` |
| `cz_a1` | What do you generally think of credit and loans? | `Numeric(Byte)` | `%37.0g` |
| `cz_a2_a` | Borrow for Holidays | `Numeric(Byte)` | `%13.0g` |
| `cz_a2_b` | Borrow for Living expenses | `Numeric(Byte)` | `%13.0g` |
| `cz_a2_c` | Borrow for Buying a luxury fur coat or jewellery | `Numeric(Byte)` | `%13.0g` |
| `cz_a2_d` | Borrow for Buying a car | `Numeric(Byte)` | `%13.0g` |
| `cz_a2_e` | Borrow for Educational courses | `Numeric(Byte)` | `%13.0g` |
| `cz_a2_f` | Borrow for Gifts to loved ones | `Numeric(Byte)` | `%13.0g` |
| `cz_a3` | Do you personally have any credit or debit cards? | `Numeric(Byte)` | `%10.0g` |
| `cz_a4` | If you sold all your property and paid all debts - money left? | `Numeric(Byte)` | `%10.0g` |
| `cz_b1_1` | I follow the municipal newsletter | `Numeric(Byte)` | `%10.0g` |
| `cz_b1_2` | I follow information in the daily press | `Numeric(Byte)` | `%10.0g` |
| `cz_b1_3` | I follow municipal notice boards | `Numeric(Byte)` | `%10.0g` |
| `cz_b1_4` | I follow information on the Internet | `Numeric(Byte)` | `%10.0g` |
| `cz_b1_5` | I have discussions with neighbours | `Numeric(Byte)` | `%10.0g` |
| `cz_b1_6` | I take part in the local council meetings | `Numeric(Byte)` | `%10.0g` |
| `cz_b1_7` | I do not follow, I am not interested | `Numeric(Byte)` | `%10.0g` |
| `cz_b1_8` | I follow in a different manner | `Numeric(Byte)` | `%10.0g` |
| `cz_b2` | Did you vote in the last local elections of 2014? | `Numeric(Byte)` | `%10.0g` |
| `cz_b3` | If there were local elections tomorrow, would you go and vote? | `Numeric(Byte)` | `%11.0g` |
| `cz_b4` | Have you ever stood as a candidate in any local elections? | `Numeric(Byte)` | `%10.0g` |
| `cz_b5_a` | Do you agree: What people like me think makes little difference | `Numeric(Byte)` | `%10.0g` |
| `cz_b5_b` | Do you agree: People like me feel left out of local affairs | `Numeric(Byte)` | `%10.0g` |
| `cz_b5_c` | Do you agree: While people can vote, they have little influence | `Numeric(Byte)` | `%10.0g` |
| `cz_b6` | Do you think your village or town is thriving or declining | `Numeric(Byte)` | `%20.0g` |
| `cz_c1_a` | Sleep: difficult to get to sleep | `Numeric(Byte)` | `%10.0g` |
| `cz_c1_b` | Sleep: wake up several times a night | `Numeric(Byte)` | `%10.0g` |
| `cz_c1_c` | Sleep: wake up too early | `Numeric(Byte)` | `%10.0g` |
| `cz_c1_d` | Sleep: wake up tired and exhausted | `Numeric(Byte)` | `%10.0g` |
| `cz_c1_e` | Sleep: take sleeping pills | `Numeric(Byte)` | `%10.0g` |
| `cz_c2` | How many hours per night do you usually sleep on weekdays? | `Numeric(Byte)` | `%10.0g` |
| `cz_d1` | How often in the last 5 years - holiday outside your home or holiday home | `Numeric(Byte)` | `%11.0g` |
| `cz_d2` | How many times in the last five years - holiday abroad? | `Numeric(Byte)` | `%11.0g` |
| `cz_d3` | How often in the last 5 years - travel by plane (excluding business trips) | `Numeric(Byte)` | `%11.0g` |
| `cz_e1_a` | Do you agree: opposition holds government back from making important decisions | `Numeric(Byte)` | `%10.0g` |
| `cz_e1_b` | Do you agree: state should provide people with security/right to work for all | `Numeric(Byte)` | `%10.0g` |
| `cz_e1_c` | Do you agree: individual should be able to express his/her views freely | `Numeric(Byte)` | `%10.0g` |
| `cz_e1_d` | Do you agree: government should adopt measures to reduce income inequalities | `Numeric(Byte)` | `%10.0g` |
| `cz_e1_e` | Do you agree: By voting in elections I can influence the course of our country | `Numeric(Byte)` | `%10.0g` |
| `cz_e1_f` | Do you agree: For me it makes no difference whether or not living in democracy | `Numeric(Byte)` | `%10.0g` |
| `cz_e1_g` | Do you agree: The market is harmful, it brings out the worst in people | `Numeric(Byte)` | `%10.0g` |
| `cz_e2_a` | Do you agree: The Czech Republic should leave the European Union | `Numeric(Byte)` | `%10.0g` |
| `cz_e2_b` | Do you agree: The Czech Republic should leave NATO | `Numeric(Byte)` | `%10.0g` |
| `cz_e2_c` | Do you agree: The break-up of the Soviet Union was a mistake | `Numeric(Byte)` | `%10.0g` |
| `cz_e2_d` | Do you agree: Germany represents a security threat for the Czech | `Numeric(Byte)` | `%10.0g` |
| `cz_e2_e` | Do you agree: European Union will break up in the next 10 years | `Numeric(Byte)` | `%10.0g` |
| `cz_e2_f` | Do you agree: Economic migrants take jobs away from Czech workers | `Numeric(Byte)` | `%10.0g` |
| `cz_e2_g` | Do you agree: Czech Republic should adopt Euro as its currency | `Numeric(Byte)` | `%10.0g` |
| `cz_e2_h` | Do you agree: Czech Republic contributes to EU more than it gets back | `Numeric(Byte)` | `%10.0g` |
| `cz_e2_i` | Do you agree: The Schengen free movement area should be abolished | `Numeric(Byte)` | `%10.0g` |
| `cz_e2_j` | Do you agree: Thanks to EU membership we are better off | `Numeric(Byte)` | `%10.0g` |
| `cz_f1` | Do you use the Internet? | `Numeric(Byte)` | `%10.0g` |
| `cz_f2_a` | Did you do the following activities: I wrote blogs | `Numeric(Byte)` | `%10.0g` |
| `cz_f2_b` | Did you do the following activities: I wrote discussion comment(s) on articles | `Numeric(Byte)` | `%10.0g` |
| `cz_f2_c` | Did you do the following activities: I was active on social networks | `Numeric(Byte)` | `%10.0g` |
| `cz_f2_d` | Did you do the following activities: I used the Internet for activities | `Numeric(Byte)` | `%10.0g` |
| `cz_f2_e` | Did you do the following activities: I downloaded films videos, music | `Numeric(Byte)` | `%10.0g` |
| `cz_f2_f` | Did you do the following activities: I followed news | `Numeric(Byte)` | `%10.0g` |
| `cz_f2_g` | Did you do the following activities: I played games | `Numeric(Byte)` | `%10.0g` |
| `cz_f3_a` | Do you agree: I have someone online to consult for important decisions | `Numeric(Byte)` | `%10.0g` |
| `cz_f3_b` | Do you agree: When I feel lonely, there are a few people online for talking | `Numeric(Byte)` | `%10.0g` |
| `cz_f3_c` | Do you agree: Socializing online gives me a chance to talk to unknown people | `Numeric(Byte)` | `%10.0g` |
| `cz_f3_d` | Do you agree: Socializing online - take interest in what happens outside my home | `Numeric(Byte)` | `%10.0g` |
| `cz_g1_a` | How often: Visiting a museum | `Numeric(Byte)` | `%21.0g` |
| `cz_g1_b` | How often: Going to see a theatre play | `Numeric(Byte)` | `%21.0g` |
| `cz_g1_c` | How often: Attending a sports match | `Numeric(Byte)` | `%21.0g` |
| `cz_g1_d` | How often: Going to a concert of classical music, opera or ballet | `Numeric(Byte)` | `%21.0g` |
| `cz_g1_e` | How often: Going to a concert of other than classical music | `Numeric(Byte)` | `%21.0g` |
| `cz_g1_f` | How often: Visiting historical monuments, castles and chateaux | `Numeric(Byte)` | `%21.0g` |
| `cz_g1_g` | How often: Borrowing books in public library | `Numeric(Byte)` | `%21.0g` |
| `cz_g2_a` | How well do you know the following language: English | `Numeric(Byte)` | `%10.0g` |
| `cz_g2_b` | How well do you know the following language: German | `Numeric(Byte)` | `%10.0g` |
| `cz_g2_c` | How well do you know the following language: Russian | `Numeric(Byte)` | `%10.0g` |
| `cz_g2_d` | How well do you know the following language: Another language | `Numeric(Byte)` | `%10.0g` |
| `cz_g3` | How many fiction books did you read in the last 12 months? | `Numeric(Int)` | `%10.0g` |
| `cz_g3_coding` | Do not know or missing - cz_g3 | `Numeric(Byte)` | `%11.0g` |
| `cz_g4` | How many books do you approximately have at home? | `Numeric(Int)` | `%10.0g` |
| `cz_g4_coding` | Do not know or missing - cz_g4 | `Numeric(Byte)` | `%11.0g` |
| `cz_h1_a` | Do you have rugs on the floor of your home? | `Numeric(Byte)` | `%35.0g` |
| `cz_h1_b` | Do you use an anti-slip bathroom mat when taking a bath/shower? | `Numeric(Byte)` | `%35.0g` |
| `cz_h1_c` | Is your bath/shower fitted with grab bars? | `Numeric(Byte)` | `%35.0g` |
| `cz_h1_d` | Do you go swimming to places unsupervised by a lifeguard? | `Numeric(Byte)` | `%35.0g` |
| `cz_h1_e` | Do you self-administer your medication? | `Numeric(Byte)` | `%35.0g` |
| `cz_h1_f` | Have you ever been hurt by your pet in such a way | `Numeric(Byte)` | `%35.0g` |
| `cz_h1_g` | When crossing the street, do you use marked pedestrian crossings only? | `Numeric(Byte)` | `%35.0g` |
| `cz_h1_h` | Do you carry or use reflexive elements | `Numeric(Byte)` | `%35.0g` |
| `cz_h1_i` | Do you use a helmet whenever cycling? | `Numeric(Byte)` | `%35.0g` |
| `cz_h1_j` | Do you use a pill box for your medication? | `Numeric(Byte)` | `%35.0g` |
| `cz_h1_k` | Do you keep your medication stored in a locked cupboard or drawer? | `Numeric(Byte)` | `%35.0g` |
| `cz_h1_l` | Do you have some medication stored freely in the fridge? | `Numeric(Byte)` | `%35.0g` |
| `cz_h2_1` | In which room do you keep your medication: In the kitchen | `Numeric(Byte)` | `%10.0g` |
| `cz_h2_2` | In which room do you keep your medication: In the bedroom | `Numeric(Byte)` | `%10.0g` |
| `cz_h2_3` | In which room do you keep your medication: In the bathroom | `Numeric(Byte)` | `%10.0g` |
| `cz_h2_4` | In which room do you keep your medication: Elsewhere | `Numeric(Byte)` | `%10.0g` |
| `cz_h2_noanswer` | No answer - cz_h2 | `Numeric(Byte)` | `%10.0g` |
| `cz_i1_a` | Percent pension decrease if retire before legal retirement age | `Numeric(Byte)` | `%10.0g` |
| `cz_i2_a` | Percent pension increase if retire after legal retirement age | `Numeric(Int)` | `%10.0g` |
| `cz_i3_a_a` | Would it be more profitable if you choose early retirement? | `Numeric(Byte)` | `%35.0g` |
| `cz_i3_b_a` | Would it be more profitable if you start receiving old age pension | `Numeric(Byte)` | `%35.0g` |
| `cz_i3_c_a` | Would it be more profitable if you postpone retirement for later | `Numeric(Byte)` | `%35.0g` |
| `cz_i3_d_a` | Would it be more profitable if you at the legal retirement age | `Numeric(Byte)` | `%35.0g` |
| `cz_i4_a` | Situation: Retirement and/or work | `Numeric(Byte)` | `%56.0g` |
| `cz_i4_b` | When do you plan to retire? | `Numeric(Byte)` | `%71.0g` |
| `cz_j1` | Over the last 12 months, how often did you have sex | `Numeric(Byte)` | `%32.0g` |
| `cz_k1` | How many years in total did you live with one parent only? | `Numeric(Byte)` | `%39.0g` |
| `cz_k1_b_mother` | Number of years with mother only | `Numeric(Byte)` | `%10.0g` |
| `cz_k1_c_father` | Number of years with father only | `Numeric(Byte)` | `%10.0g` |
| `cz_k2` | Did your family move to the territory of the former Sudetenland | `Numeric(Byte)` | `%10.0g` |
| `cz_k2a_year` | Year of move to Sudetenland | `Numeric(Int)` | `%10.0g` |
| `cz_k2b_year` | If yes, until which year did you live on the territory | `Numeric(Int)` | `%10.0g` |
| `ee_language` | Drop-Off language: Estonia | `Numeric(Byte)` | `%10.0g` |
| `ee_k12` | How well do you know the Estonian language? Can you ... | `Numeric(Byte)` | `%33.0g` |
| `ee_k16` | Can you use public transportationâ€¦ | `Numeric(Byte)` | `%22.0g` |
| `ee_k17` | Can you visit a food and convenience storeâ€¦ | `Numeric(Byte)` | `%22.0g` |
| `ee_k18` | When necessary, can you visit the nearest pharmacyâ€¦ | `Numeric(Byte)` | `%22.0g` |
| `ee_k19` | When necessary, can you visit your family doctor or nurseâ€¦ | `Numeric(Byte)` | `%22.0g` |
| `ee_k20` | When necessary, can you visit the city or rural municipality governmentâ€¦ | `Numeric(Byte)` | `%22.0g` |
| `ee_k21` | When you need cash, can you get it from the nearest ATM, bank, post office or st | `Numeric(Byte)` | `%22.0g` |
| `ee_k22` | When you wish, can you get to a cultural event, sports practice or training cour | `Numeric(Byte)` | `%22.0g` |
| `ee_k23_1` | Access: Food and convenience store | `Numeric(Byte)` | `%56.0g` |
| `ee_k23_2` | Access: Pharmacy | `Numeric(Byte)` | `%56.0g` |
| `ee_k23_3` | Access: Family doctor or nurse | `Numeric(Byte)` | `%56.0g` |
| `ee_k23_4` | Access: City or rural municipality government | `Numeric(Byte)` | `%56.0g` |
| `ee_k23_5` | Access: ATM, bank, post office (store) | `Numeric(Byte)` | `%56.0g` |
| `ee_k23_6` | Access: Cultural building, theatre, sports hall, village centre, etc. | `Numeric(Byte)` | `%56.0g` |
| `ee_k24` | Has a social worker evaluated your need for a subsistence benefit or personal as | `Numeric(Byte)` | `%10.0g` |
| `ee_k25` | Has a care plan been prepared fo you? | `Numeric(Byte)` | `%10.0g` |
| `ee_k26` | Have you been assigned a caregiver by the local government? | `Numeric(Byte)` | `%10.0g` |
| `ee_k27` | Do you receive compensation from the local government to pay for care service? | `Numeric(Byte)` | `%10.0g` |
| `ee_k28` | Do you receive home services organised by the local government? | `Numeric(Byte)` | `%10.0g` |
| `fi_language` | Drop-Off language: Finland | `Numeric(Byte)` | `%10.0g` |
| `fi_g01_1` | work status | `Numeric(Byte)` | `%47.0g` |
| `fi_g01_2` | work status again if two ticks in q1 (if nows year of both full and part time re | `Numeric(Byte)` | `%47.0g` |
| `fi_g01_3` | year of part time retirement | `Numeric(Int)` | `%10.0g` |
| `fi_g01_4` | year of retirement | `Numeric(Int)` | `%10.0g` |
| `fi_g02` | Assuming that the best working capacity you have ever had would score 10 on a sc | `Numeric(Double)` | `%10.0g` |
| `fi_g03` | If possible, would you like to do more or less wage work than you currently do? | `Numeric(Byte)` | `%42.0g` |
| `fi_g04` | If possible, would you like to do more or less voluntary work than you currently | `Numeric(Double)` | `%47.0g` |
| `fi_g05_1` | I belong to group of friends | `Numeric(Byte)` | `%10.0g` |
| `fi_g05_2` | I am no longer close to anybody | `Numeric(Double)` | `%10.0g` |
| `fi_g05_3` | I can find company if I want to | `Numeric(Byte)` | `%10.0g` |
| `fi_g05_4` | There are people, who really understand me | `Numeric(Byte)` | `%10.0g` |
| `fi_g06` | Do you have regular responsibility for the care of a dependent household member? | `Numeric(Byte)` | `%10.0g` |
| `fi_g07` | How many such close friends would you say you have at the moment, with whom you | `Numeric(Double)` | `%10.0g` |
| `fi_g08` | How often do you meet your these close friends face-to-face? | `Numeric(Double)` | `%22.0g` |
| `fi_g09` | How many such relatives do you have at the moment, with whom you feel at ease an | `Numeric(Double)` | `%10.0g` |
| `fi_g10` | How often do you meet these close relatives face-to-face? | `Numeric(Double)` | `%34.0g` |
| `fi_g11_1` | The level of social services and benefits is too high in Finland | `Numeric(Double)` | `%26.0g` |
| `fi_g11_2` | Social benefits in Finland often go to persons who do not need them | `Numeric(Byte)` | `%26.0g` |
| `fi_g11_3` | It is common that people cheat in order to receive social benefits in Finland | `Numeric(Byte)` | `%26.0g` |
| `fi_g12` | How often do you meet your grandchild(ren) face-to-face? | `Numeric(Double)` | `%19.0g` |
| `fi_g13` | How often do you look after your grandchild/your grandchildren without the prese | `Numeric(Double)` | `%19.0g` |
| `fi_g14_1` | I am satisfied with how we express things and feelings to each other | `Numeric(Byte)` | `%17.0g` |
| `fi_g14_2` | I feel that my partner understands me | `Numeric(Byte)` | `%17.0g` |
| `fi_g14_3` | I am satisfied with the amount of physical closeness between us | `Numeric(Double)` | `%17.0g` |
| `fi_g14_4` | I feel that my partner respects me | `Numeric(Byte)` | `%17.0g` |
| `fi_g14_5` | I feel that we love each other | `Numeric(Byte)` | `%17.0g` |
| `fi_g14_6` | I feel that we belong together | `Numeric(Double)` | `%17.0g` |
| `fi_g14_7` | My partner fully supports me in life | `Numeric(Byte)` | `%17.0g` |
| `fi_g14_8` | I have recently considered divorce or ending the relationship | `Numeric(Byte)` | `%17.0g` |
| `fi_g14_9` | I am satisfied with how we decide about money and economic issues | `Numeric(Byte)` | `%17.0g` |
| `fi_g14_10` | I am satisfied with the way we spend time together | `Numeric(Byte)` | `%17.0g` |
| `fi_g15_1` | The division of house work | `Numeric(Double)` | `%28.0g` |
| `fi_g15_2` | Money | `Numeric(Byte)` | `%28.0g` |
| `fi_g15_3` | Spending leisure time | `Numeric(Byte)` | `%28.0g` |
| `fi_g15_4` | Sexual life | `Numeric(Byte)` | `%28.0g` |
| `fi_g15_5` | Infidelity or jealousy | `Numeric(Byte)` | `%28.0g` |
| `fi_g15_6` | Friends and relations with friends | `Numeric(Byte)` | `%28.0g` |
| `fi_g15_7` | Relations to our shared children or grandchildren | `Numeric(Byte)` | `%28.0g` |
| `fi_g15_8` | Relations to my own kin (e.g. my own parents, children or siblings) | `Numeric(Byte)` | `%28.0g` |
| `fi_g15_9` | Relations to my partnerâ€™s kin | `Numeric(Double)` | `%28.0g` |
| `fi_g15_10` | Issues and situations related to divorce or blended (â€™newâ€™) families | `Numeric(Byte)` | `%28.0g` |
| `fi_g15_11` | Alcohol or drug use | `Numeric(Byte)` | `%28.0g` |
| `fi_g15_12` | My own wage work | `Numeric(Byte)` | `%28.0g` |
| `fi_g15_13` | My partnerâ€™s wage work | `Numeric(Byte)` | `%28.0g` |
| `fi_g15_14` | My own retirement | `Numeric(Byte)` | `%28.0g` |
| `fi_g15_15` | My partnerâ€™s retirement | `Numeric(Byte)` | `%28.0g` |
| `il_q1_a` | Alzheimer's Disease is a form of insanity | `Numeric(Byte)` | `%10.0g` |
| `il_q1_b` | Trouble with memory and confused thinking | `Numeric(Byte)` | `%10.0g` |
| `il_q1_c` | There is currently no cure for AD | `Numeric(Byte)` | `%10.0g` |
| `il_q1_d` | AD could be contagious | `Numeric(Byte)` | `%10.0g` |
| `il_q1_e` | Genes can only partially account for the development of AD | `Numeric(Byte)` | `%10.0g` |
| `il_q1_f` | Confusion with time and place is a symptom of AD | `Numeric(Byte)` | `%10.0g` |
| `il_q1_g` | AD can be diagnosed with a blood test | `Numeric(Byte)` | `%10.0g` |
| `il_q1_h` | At present, the cause of AD is unclear | `Numeric(Byte)` | `%10.0g` |
| `il_q1_i` | Symptoms of severe depression can be mistaken for symptoms of AD | `Numeric(Byte)` | `%10.0g` |
| `il_q1_j` | The majority of people that suffer from AD live in institutions | `Numeric(Byte)` | `%10.0g` |
| `il_q2_a` | Important factor for developing AD: Old age | `Numeric(Byte)` | `%30.0g` |
| `il_q2_b` | Important factor for developing AD: Genetics | `Numeric(Byte)` | `%30.0g` |
| `il_q2_c` | Important factor for developing AD: Physical inactivity | `Numeric(Byte)` | `%30.0g` |
| `il_q2_d` | Important factor for developing AD: Stress | `Numeric(Byte)` | `%30.0g` |
| `il_q2_e` | Important factor for developing AD: Loneliness | `Numeric(Byte)` | `%30.0g` |
| `il_q2_f` | Important factor for developing AD: Poor nutrition | `Numeric(Byte)` | `%30.0g` |
| `il_q3_a` | I feel comfortable being around people with AD | `Numeric(Byte)` | `%17.0g` |
| `il_q3_b` | I find it hard to talk to someone with AD. | `Numeric(Byte)` | `%17.0g` |
| `il_q3_c` | Someone with AD can still enjoy life | `Numeric(Byte)` | `%17.0g` |
| `il_q3_d` | High risk of developing AD, I consider life not worth living | `Numeric(Byte)` | `%17.0g` |
| `il_q3_e` | I would like to know if I am at higher risk for developing AD | `Numeric(Byte)` | `%17.0g` |
| `il_q3_f` | Early detection of AD increases the chance to treat the disease | `Numeric(Byte)` | `%17.0g` |
| `il_q4_a` | Did Physical exercise or activity, at least twice a week | `Numeric(Byte)` | `%56.0g` |
| `il_q4_b` | Consumed foods with high saturated fat and cholesterol | `Numeric(Byte)` | `%53.0g` |
| `il_q4_c` | Consumed, on a daily basis, at least 3 portions | `Numeric(Byte)` | `%31.0g` |
| `il_q4_d` | Attempted to limit your total daily caloric intake | `Numeric(Byte)` | `%33.0g` |
| `il_q4_e` | Tried to reduce your stress level | `Numeric(Byte)` | `%58.0g` |
| `il_q4_f` | Communicated with family or friends, at least twice a week | `Numeric(Byte)` | `%55.0g` |
| `il_q4_g` | Participated in social activities, at least once a week | `Numeric(Byte)` | `%60.0g` |
| `il_q4_h` | Did word or number games such as crossword puzzles or sudoku | `Numeric(Byte)` | `%85.0g` |
| `il_q4_i` | Took nutritional supplements on a daily basis | `Numeric(Byte)` | `%85.0g` |
| `il_q5_a` | Do you know someone with AD: Partner | `Numeric(Byte)` | `%10.0g` |
| `il_q5_b` | Do you know someone with AD: Parent | `Numeric(Byte)` | `%10.0g` |
| `il_q5_c` | Do you know someone with AD: Other relative | `Numeric(Byte)` | `%14.0g` |
| `il_q5_d` | Do you know someone with AD: A friend | `Numeric(Byte)` | `%10.0g` |
| `il_q5_e` | Do you know someone with AD: My job involves/involved working AD patients | `Numeric(Byte)` | `%68.0g` |
| `il_q5_f` | Do you know someone with AD: Other | `Numeric(Byte)` | `%10.0g` |
| `il_q5_g` | Do you know someone with AD: I don't know anyone with AD | `Numeric(Byte)` | `%55.0g` |
| `il_q6_a` | Provide(d) care for someone with AD: On regular basis | `Numeric(Byte)` | `%18.0g` |
| `il_q6_b` | Provide(d) care for someone with AD: On infrequent basis | `Numeric(Byte)` | `%22.0g` |
| `il_q6_c` | Provide(d) care for someone with AD: None of these | `Numeric(Byte)` | `%14.0g` |
| `il_q7_a` | Warning symptom of AD - seek help: Partner | `Numeric(Byte)` | `%10.0g` |
| `il_q7_b` | Warning symptom of AD - seek help: Parent | `Numeric(Byte)` | `%10.0g` |
| `il_q7_c` | Warning symptom of AD - seek help: Other relative | `Numeric(Byte)` | `%14.0g` |
| `il_q7_d` | Warning symptom of AD - seek help: A friend | `Numeric(Byte)` | `%10.0g` |
| `il_q7_e` | Warning symptom of AD - seek help: General Practitioner (MD) | `Numeric(Byte)` | `%25.0g` |
| `il_q7_f` | Warning symptom of AD - seek help: Geriatrician | `Numeric(Byte)` | `%12.0g` |
| `il_q7_g` | Warning symptom of AD - seek help: Neurologist | `Numeric(Byte)` | `%11.0g` |
| `il_q7_h` | Warning symptom of AD - seek help: Psychologist or Psychiatrist | `Numeric(Byte)` | `%28.0g` |
| `il_q7_i` | Warning symptom of AD - seek help: Nurse | `Numeric(Byte)` | `%10.0g` |
| `il_q7_j` | Warning symptom of AD - seek help: Social worker | `Numeric(Byte)` | `%13.0g` |
| `il_q7_k` | Warning symptom of AD - seek help: Clergy (Rabbi, Sheikh or Priest) | `Numeric(Byte)` | `%32.0g` |
| `il_q7_l` | Warning symptom of AD - seek help: Other spiritual care provider | `Numeric(Byte)` | `%29.0g` |
| `il_q7_m` | Warning symptom of AD - seek help: The internet | `Numeric(Byte)` | `%12.0g` |
| `il_q7_n` | Warning symptom of AD - seek help: An organization that deals with AD | `Numeric(Byte)` | `%34.0g` |
| `pl_version` | Version (A = not retired, B = retired) | `Numeric(Byte)` | `%15.0g` |
| `pl_q1d1_empcontract_self` | Current/last main employment contract: self-employed | `Numeric(Byte)` | `%12.0g` |
| `pl_q1d2_empcontract_open` | Current/last main employment contract: open ended | `Numeric(Byte)` | `%12.0g` |
| `pl_q1d3_empcontract_fixed` | Current/last main employment contract: fixed contract | `Numeric(Byte)` | `%12.0g` |
| `pl_q1d4_empcontract_delegated` | Current/last main employment contract: temporary delegated | `Numeric(Byte)` | `%12.0g` |
| `pl_q1d5_empcontract_task` | Current/last main employment contract: temporary task | `Numeric(Byte)` | `%12.0g` |
| `pl_q1d6_empcontract_management` | Current/last main employment contract: management | `Numeric(Byte)` | `%12.0g` |
| `pl_q1d7_empcontract_oth` | Current/last main employment contract: other | `Numeric(Byte)` | `%12.0g` |
| `pl_q1d8_empcontract_none` | Current/last main employment contract: no contract | `Numeric(Byte)` | `%12.0g` |
| `pl_q2_a_involve_positions` | Main job involves/involved: tiring/painful positions | `Numeric(Byte)` | `%10.0g` |
| `pl_q2_b_involve_lifting` | Main job involves/involved: lifting/moving people | `Numeric(Byte)` | `%10.0g` |
| `pl_q2_c_involve_carrying` | Main job involves/involved: carrying heavy loads | `Numeric(Byte)` | `%10.0g` |
| `pl_q2_d_involve_sitting` | Main job involves/involved: sitting | `Numeric(Byte)` | `%10.0g` |
| `pl_q2_e_involve_standing` | Main job involves/involved: standing | `Numeric(Byte)` | `%10.0g` |
| `pl_q2_f_involve_repetitive` | Main job involves/involved: repetitive movements | `Numeric(Byte)` | `%10.0g` |
| `pl_q2_g_involve_customers` | Main job involves/involved: dealing with customers | `Numeric(Byte)` | `%10.0g` |
| `pl_q2_h_involve_lighting` | Main job involves/involved: insufficient lighting | `Numeric(Byte)` | `%10.0g` |
| `pl_q2_i_involve_computers` | Main job involves/involved: working with computers etc. | `Numeric(Byte)` | `%10.0g` |
| `pl_q3_a_exposed_vibr` | Main job exposure to: vibrations | `Numeric(Byte)` | `%10.0g` |
| `pl_q3_b_exposed_noise` | Main job exposure to: noise | `Numeric(Byte)` | `%10.0g` |
| `pl_q3_c_exposed_htemp` | Main job exposure to: high temperature | `Numeric(Byte)` | `%10.0g` |
| `pl_q3_d_exposed_ltemp` | Main job exposure to: low temperature | `Numeric(Byte)` | `%10.0g` |
| `pl_q3_e_exposed_fumes` | Main job exposure to: fumes | `Numeric(Byte)` | `%10.0g` |
| `pl_q3_f_exposed_vapours` | Main job exposure to: vapours | `Numeric(Byte)` | `%10.0g` |
| `pl_q3_g_exposed_chemicals` | Main job exposure to: chemicals | `Numeric(Byte)` | `%10.0g` |
| `pl_q3_h_exposed_smoke` | Main job exposure to: tobacco smoke | `Numeric(Byte)` | `%10.0g` |
| `pl_q3_i_exposed_infectious` | Main job exposure to: infectious material | `Numeric(Byte)` | `%10.0g` |
| `pl_q3_j_exposed_tools` | Main job exposure to: dangerous tools | `Numeric(Byte)` | `%10.0g` |
| `pl_q4_ever_exposed_noise` | Ever had a job with exposure to noise for 4 or more hours several days | `Numeric(Byte)` | `%10.0g` |
| `pl_q5_a_laidoff_12m` | In the next year how likely is it that: you will lose your job | `Numeric(Byte)` | `%10.0g` |
| `pl_q5_a_permcontract_12m` | In the next year how likely: employed with permanent contract | `Numeric(Byte)` | `%10.0g` |
| `pl_q5_b_retire_12m` | In the next year how likely is it that: you will retire | `Numeric(Byte)` | `%10.0g` |
| `pl_q5_b_tempcontract_12m` | In the next year how likely: employed with temporary contract | `Numeric(Byte)` | `%10.0g` |
| `pl_q5_c_laidoff_24m` | In the next two years how likely is it that: you will lose your job | `Numeric(Byte)` | `%10.0g` |
| `pl_q5_c_permcontract_24m` | In the next two years how likely: employed with permanent contract | `Numeric(Byte)` | `%10.0g` |
| `pl_q5_d_retire_24m` | In the next two years how likely is it that: you will retire | `Numeric(Byte)` | `%10.0g` |
| `pl_q5_d_tempcontract_24m` | In the next two years how likely: employed with temporary contract | `Numeric(Byte)` | `%10.0g` |
| `pl_q6d1_factors_age` | Most influence on occupational situation: age | `Numeric(Byte)` | `%12.0g` |
| `pl_q6d2_factors_health` | Most influence on occupational situation: health | `Numeric(Byte)` | `%12.0g` |
| `pl_q6d3_factors_skills` | Most influence on occupational situation: skills | `Numeric(Byte)` | `%12.0g` |
| `pl_q6d4_factors_family` | Most influence on occupational situation: family | `Numeric(Byte)` | `%12.0g` |
| `pl_q6d5_factors_emot_burden` | Most influence on occupational situation: emotional burden | `Numeric(Byte)` | `%12.0g` |
| `pl_q6d5_factors_finsit` | Most influence on occupational situation: financial situation | `Numeric(Byte)` | `%12.0g` |
| `pl_q6d6_factors_loc_jobmarket` | Most influence on occupational situation: local job market | `Numeric(Byte)` | `%12.0g` |
| `pl_q6d6_factors_phys_burden` | Most influence on occupational situation: physical burden | `Numeric(Byte)` | `%12.0g` |
| `pl_q6d7_factors_employer` | Most influence on occupational situation: employer | `Numeric(Byte)` | `%12.0g` |
| `pl_q6d7_factors_help` | Most influence on occupational situation: help | `Numeric(Byte)` | `%12.0g` |
| `pl_q6d8_factors_commuting` | Most influence on occupational situation: commuting | `Numeric(Byte)` | `%12.0g` |
| `pl_q7_glasses` | Do you usually wear glasses or contact lenses? | `Numeric(Byte)` | `%10.0g` |
| `pl_q8_eyesight_distance` | How good is your eyesight for seeing things at a distance | `Numeric(Byte)` | `%10.0g` |
| `pl_q9_eyesight_close` | How good is your eyesight for seeing things up close | `Numeric(Byte)` | `%10.0g` |
| `pl_q10_have_hearing_aid` | Do you have a hearing aid? | `Numeric(Byte)` | `%10.0g` |
| `pl_q11_wear_hearing_aid` | Do you usually wear a hearing aid? | `Numeric(Byte)` | `%10.0g` |
| `pl_q12_hearing` | Self-rated hearing ability | `Numeric(Byte)` | `%10.0g` |
| `pl_q13_hearing_problem_noise` | How often difficulties hearing with background noise | `Numeric(Byte)` | `%10.0g` |
| `pl_q14_hearing_problem_frust` | How often hearing cause of frustration talking to family/friends | `Numeric(Byte)` | `%10.0g` |
| `pl_q15_hearing_problem_job` | How often hearing source of misunderstanding in your job | `Numeric(Byte)` | `%10.0g` |
| `pl_q16_a_hearing_whisper` | Without hearing aid: understand whisper | `Numeric(Byte)` | `%10.0g` |
| `pl_q16_b_hearing_normalvoice` | Without hearing aid: understand normal voice | `Numeric(Byte)` | `%10.0g` |
| `pl_q16_c_hearing_shout` | Without hearing aid: understand shouting | `Numeric(Byte)` | `%10.0g` |
| `pl_q17_hearing_tested` | When was the last time you had your hearing tested | `Numeric(Byte)` | `%20.0g` |
| `pl_q18d1_hearingaid_noproblem` | Why donâ€™t you use a hearing aid?: no problem | `Numeric(Byte)` | `%12.0g` |
| `pl_q18d2_hearingaid_doctor` | Why donâ€™t you use a hearing aid?: doctor | `Numeric(Byte)` | `%12.0g` |
| `pl_q18d3_hearingaid_expensive` | Why donâ€™t you use a hearing aid?: expensive | `Numeric(Byte)` | `%12.0g` |
| `pl_q18d4_hearingaid_uncomfortab` | Why donâ€™t you use a hearing aid?: uncomfortable | `Numeric(Byte)` | `%12.0g` |
| `pl_q18d5_hearingaid_notworking` | Why donâ€™t you use a hearing aid?: not working | `Numeric(Byte)` | `%12.0g` |
| `pl_q18d6_hearingaid_unaesthetic` | Why donâ€™t you use a hearing aid?: unaesthetic | `Numeric(Byte)` | `%12.0g` |
| `pl_q18d7_hearingaid_ashamed` | Why donâ€™t you use a hearing aid?: ashamed | `Numeric(Byte)` | `%12.0g` |
| `pl_q18d8_hearingaid_dunno` | Why donâ€™t you use a hearing aid?: don't know | `Numeric(Byte)` | `%12.0g` |
| `pl_q18d9_hearingaid_none` | Why donâ€™t you use a hearing aid?: none | `Numeric(Byte)` | `%12.0g` |
| `pl_q19_periodic_exam` | Last periodic medical examination at current/last main job | `Numeric(Byte)` | `%20.0g` |
| `pl_q20_a_test_blood` | Which health test: blood analysis | `Numeric(Byte)` | `%10.0g` |
| `pl_q20_b_test_urin` | Which health test: urinalyis | `Numeric(Byte)` | `%10.0g` |
| `pl_q20_c_test_vision` | Which health test: vision test | `Numeric(Byte)` | `%10.0g` |
| `pl_q20_d_test_audio` | Which health test: audiometric test | `Numeric(Byte)` | `%10.0g` |
| `pl_q20_e_test_pressure` | Which health test: blood pressure measurement | `Numeric(Byte)` | `%10.0g` |
| `pl_q20_f_test_ecg` | Which health test: electrocardiography (ecg) | `Numeric(Byte)` | `%10.0g` |
| `pl_q20_g_test_xray` | Which health test: chest x-ray | `Numeric(Byte)` | `%10.0g` |
| `pl_q20_h_test_neurological` | Which health test: neurological examination | `Numeric(Byte)` | `%10.0g` |
| `pl_q21_templeave_ownhealth` | Last 12 months how many days taken a temporary leave: own health | `Numeric(Byte)` | `%17.0g` |
| `pl_q22_templeave_care` | Last 12 months how many days taken a temporary leave: care for others | `Numeric(Byte)` | `%17.0g` |
| `pl_q23_protected_period` | Labour Law: How long employment protection? | `Numeric(Byte)` | `%12.0g` |
| `si_h0_10` | Activity in hour 0 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h0_20` | Activity in hour 0 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h0_30` | Activity in hour 0 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h0_40` | Activity in hour 0 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h0_50` | Activity in hour 0 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h0_60` | Activity in hour 0 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h1_10` | Activity in hour 1 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h1_20` | Activity in hour 1 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h1_30` | Activity in hour 1 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h1_40` | Activity in hour 1 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h1_50` | Activity in hour 1 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h1_60` | Activity in hour 1 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h2_10` | Activity in hour 2 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h2_20` | Activity in hour 2 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h2_30` | Activity in hour 2 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h2_40` | Activity in hour 2 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h2_50` | Activity in hour 2 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h2_60` | Activity in hour 2 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h3_10` | Activity in hour 3 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h3_20` | Activity in hour 3 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h3_30` | Activity in hour 3 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h3_40` | Activity in hour 3 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h3_50` | Activity in hour 3 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h3_60` | Activity in hour 3 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h4_10` | Activity in hour 4 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h4_20` | Activity in hour 4 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h4_30` | Activity in hour 4 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h4_40` | Activity in hour 4 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h4_50` | Activity in hour 4 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h4_60` | Activity in hour 4 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h5_10` | Activity in hour 5 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h5_20` | Activity in hour 5 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h5_30` | Activity in hour 5 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h5_40` | Activity in hour 5 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h5_50` | Activity in hour 5 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h5_60` | Activity in hour 5 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h6_10` | Activity in hour 6 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h6_20` | Activity in hour 6 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h6_30` | Activity in hour 6 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h6_40` | Activity in hour 6 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h6_50` | Activity in hour 6 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h6_60` | Activity in hour 6 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h7_10` | Activity in hour 7 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h7_20` | Activity in hour 7 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h7_30` | Activity in hour 7 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h7_40` | Activity in hour 7 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h7_50` | Activity in hour 7 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h7_60` | Activity in hour 7 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h8_10` | Activity in hour 8 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h8_20` | Activity in hour 8 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h8_30` | Activity in hour 8 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h8_40` | Activity in hour 8 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h8_50` | Activity in hour 8 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h8_60` | Activity in hour 8 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h9_10` | Activity in hour 9 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h9_20` | Activity in hour 9 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h9_30` | Activity in hour 9 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h9_40` | Activity in hour 9 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h9_50` | Activity in hour 9 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h9_60` | Activity in hour 9 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h10_10` | Activity in hour 10 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h10_20` | Activity in hour 10 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h10_30` | Activity in hour 10 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h10_40` | Activity in hour 10 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h10_50` | Activity in hour 10 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h10_60` | Activity in hour 10 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h11_10` | Activity in hour 11 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h11_20` | Activity in hour 11 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h11_30` | Activity in hour 11 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h11_40` | Activity in hour 11 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h11_50` | Activity in hour 11 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h11_60` | Activity in hour 11 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h12_10` | Activity in hour 12 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h12_20` | Activity in hour 12 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h12_30` | Activity in hour 12 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h12_40` | Activity in hour 12 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h12_50` | Activity in hour 12 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h12_60` | Activity in hour 12 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h13_10` | Activity in hour 13 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h13_20` | Activity in hour 13 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h13_30` | Activity in hour 13 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h13_40` | Activity in hour 13 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h13_50` | Activity in hour 13 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h13_60` | Activity in hour 13 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h14_10` | Activity in hour 14 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h14_20` | Activity in hour 14 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h14_30` | Activity in hour 14 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h14_40` | Activity in hour 14 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h14_50` | Activity in hour 14 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h14_60` | Activity in hour 14 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h15_10` | Activity in hour 15 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h15_20` | Activity in hour 15 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h15_30` | Activity in hour 15 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h15_40` | Activity in hour 15 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h15_50` | Activity in hour 15 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h15_60` | Activity in hour 15 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h16_10` | Activity in hour 16 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h16_20` | Activity in hour 16 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h16_30` | Activity in hour 16 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h16_40` | Activity in hour 16 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h16_50` | Activity in hour 16 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h16_60` | Activity in hour 16 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h17_10` | Activity in hour 17 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h17_20` | Activity in hour 17 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h17_30` | Activity in hour 17 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h17_40` | Activity in hour 17 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h17_50` | Activity in hour 17 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h17_60` | Activity in hour 17 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h18_10` | Activity in hour 18 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h18_20` | Activity in hour 18 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h18_30` | Activity in hour 18 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h18_40` | Activity in hour 18 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h18_50` | Activity in hour 18 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h18_60` | Activity in hour 18 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h19_10` | Activity in hour 19 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h19_20` | Activity in hour 19 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h19_30` | Activity in hour 19 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h19_40` | Activity in hour 19 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h19_50` | Activity in hour 19 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h19_60` | Activity in hour 19 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h20_10` | Activity in hour 20 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h20_20` | Activity in hour 20 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h20_30` | Activity in hour 20 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h20_40` | Activity in hour 20 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h20_50` | Activity in hour 20 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h20_60` | Activity in hour 20 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h21_10` | Activity in hour 21 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h21_20` | Activity in hour 21 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h21_30` | Activity in hour 21 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h21_40` | Activity in hour 21 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h21_50` | Activity in hour 21 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h21_60` | Activity in hour 21 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h22_10` | Activity in hour 22 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h22_20` | Activity in hour 22 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h22_30` | Activity in hour 22 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h22_40` | Activity in hour 22 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h22_50` | Activity in hour 22 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h22_60` | Activity in hour 22 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_h23_10` | Activity in hour 23 from minute 1 to 10 | `Numeric(Int)` | `%77.0g` |
| `si_h23_20` | Activity in hour 23 from minute 11 to 20 | `Numeric(Int)` | `%77.0g` |
| `si_h23_30` | Activity in hour 23 from minute 21 to 30 | `Numeric(Int)` | `%77.0g` |
| `si_h23_40` | Activity in hour 23 from minute 31 to 40 | `Numeric(Int)` | `%77.0g` |
| `si_h23_50` | Activity in hour 23 from minute 41 to 50 | `Numeric(Int)` | `%77.0g` |
| `si_h23_60` | Activity in hour 23 from minute 51 to 60 | `Numeric(Int)` | `%77.0g` |
| `si_q1` | Did you take care of children/(great-)grandchildren yesterday? | `Numeric(Byte)` | `%10.0g` |
| `si_q1_nchild` | Number of children/(great-)grandchildren yoou took care of yesterday? | `Numeric(Byte)` | `%9.0g` |
| `si_q1_age1` | Age of child/(great-)grandchild 1 | `Numeric(Double)` | `%12.0g` |
| `si_q1_age2` | Age of child/(great-)grandchild 2 | `Numeric(Byte)` | `%12.0g` |
| `si_q1_age3` | Age of child/(great-)grandchild 3 | `Numeric(Double)` | `%12.0g` |
| `si_q1_age4` | Age of child/(great-)grandchild 4 | `Numeric(Byte)` | `%12.0g` |
| `si_q1_age5` | Age of child/(great-)grandchild 5 | `Numeric(Byte)` | `%12.0g` |
| `si_q1_age6` | Age of child/(great-)grandchild 6 | `Numeric(Byte)` | `%12.0g` |
| `si_q1_age7` | Age of child/(great-)grandchild 7 | `Numeric(Byte)` | `%12.0g` |
| `si_q1_gen1` | Gender of child/(great-)grandchild 1 | `Numeric(Byte)` | `%27.0g` |
| `si_q1_gen2` | Gender of child/(great-)grandchild 2 | `Numeric(Byte)` | `%27.0g` |
| `si_q1_gen3` | Gender of child/(great-)grandchild 3 | `Numeric(Byte)` | `%27.0g` |
| `si_q1_gen4` | Gender of child/(great-)grandchild 4 | `Numeric(Byte)` | `%27.0g` |
| `si_q1_gen5` | Gender of child/(great-)grandchild 5 | `Numeric(Byte)` | `%27.0g` |
| `si_q1_gen6` | Gender of child/(great-)grandchild 6 | `Numeric(Byte)` | `%27.0g` |
| `si_q1_gen7` | Gender of child/(great-)grandchild 7 | `Numeric(Byte)` | `%27.0g` |
| `si_q1_hh1` | Is child/(great-)grandchild 1 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q1_hh2` | Is child/(great-)grandchild 2 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q1_hh3` | Is child/(great-)grandchild 3 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q1_hh4` | Is child/(great-)grandchild 4 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q1_hh5` | Is child/(great-)grandchild 5 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q1_hh6` | Is child/(great-)grandchild 6 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q1_hh7` | Is child/(great-)grandchild 7 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q1_time1` | Time spend taking care of child/(great-)grandchild 1 | `Numeric(Float)` | `%tcHH:MM` |
| `si_q1_time2` | Time spend taking care of child/(great-)grandchild 2 | `Numeric(Float)` | `%tcHH:MM` |
| `si_q1_time3` | Time spend taking care of child/(great-)grandchild 3 | `Numeric(Double)` | `%tcHH:MM` |
| `si_q1_time4` | Time spend taking care of child/(great-)grandchild 4 | `Numeric(Double)` | `%tcHH:MM` |
| `si_q1_time5` | Time spend taking care of child/(great-)grandchild 5 | `Numeric(Double)` | `%tcHH:MM` |
| `si_q1_time6` | Time spend taking care of child/(great-)grandchild 6 | `Numeric(Double)` | `%tcHH:MM` |
| `si_q1_time7` | Time spend taking care of child/(great-)grandchild 7 | `Numeric(Byte)` | `%tcHH:MM` |
| `si_q2` | Did you help another adult person (18+) perform ADL yesterday? | `Numeric(Byte)` | `%10.0g` |
| `si_q2_1` | I helped person 1 perform ADL | `Numeric(Byte)` | `%53.0g` |
| `si_q2_2` | I helped person 2 perform ADL | `Numeric(Byte)` | `%53.0g` |
| `si_q2_3` | I helped person 3 perform ADL | `Numeric(Byte)` | `%53.0g` |
| `si_q2_4` | I helped person 4 perform ADL | `Numeric(Byte)` | `%53.0g` |
| `si_q2_5` | I helped person 5 perform ADL | `Numeric(Byte)` | `%53.0g` |
| `si_q2_age1` | Age of person 1 | `Numeric(Int)` | `%12.0g` |
| `si_q2_age2` | Age of person 2 | `Numeric(Byte)` | `%12.0g` |
| `si_q2_age3` | Age of person 3 | `Numeric(Byte)` | `%12.0g` |
| `si_q2_age4` | Age of person 4 | `Numeric(Byte)` | `%12.0g` |
| `si_q2_age5` | Age of person 5 | `Numeric(Byte)` | `%12.0g` |
| `si_q2_gen1` | Gender of person 1 | `Numeric(Byte)` | `%27.0g` |
| `si_q2_gen2` | Gender of person 2 | `Numeric(Byte)` | `%27.0g` |
| `si_q2_gen3` | Gender of person 3 | `Numeric(Byte)` | `%27.0g` |
| `si_q2_gen4` | Gender of person 4 | `Numeric(Byte)` | `%27.0g` |
| `si_q2_gen5` | Gender of person 5 | `Numeric(Byte)` | `%27.0g` |
| `si_q2_hh1` | Is person 1 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q2_hh2` | Is person 2 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q2_hh3` | Is person 3 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q2_hh4` | Is person 4 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q2_hh5` | Is person 5 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q2_time1` | Time spend helping person 1 | `Numeric(Float)` | `%tcHH:MM` |
| `si_q2_time2` | Time spend helping person 2 | `Numeric(Double)` | `%tcHH:MM` |
| `si_q2_time3` | Time spend helping person 3 | `Numeric(Byte)` | `%tcHH:MM` |
| `si_q2_time4` | Time spend helping person 4 | `Numeric(Byte)` | `%tcHH:MM` |
| `si_q2_time5` | Time spend helping person 5 | `Numeric(Byte)` | `%tcHH:MM` |
| `si_q3` | Did you help another adult person (18+) perform IADL yesterday? | `Numeric(Byte)` | `%10.0g` |
| `si_q3_1` | I helped person 1 perform IADL | `Numeric(Byte)` | `%53.0g` |
| `si_q3_2` | I helped person 2 perform IADL | `Numeric(Byte)` | `%53.0g` |
| `si_q3_3` | I helped person 3 perform IADL | `Numeric(Byte)` | `%53.0g` |
| `si_q3_4` | I helped person 4 perform IADL | `Numeric(Byte)` | `%53.0g` |
| `si_q3_5` | I helped person 5 perform IADL | `Numeric(Byte)` | `%53.0g` |
| `si_q3_age1` | Age of person 1 | `Numeric(Int)` | `%12.0g` |
| `si_q3_age2` | Age of person 2 | `Numeric(Byte)` | `%12.0g` |
| `si_q3_age3` | Age of person 3 | `Numeric(Byte)` | `%12.0g` |
| `si_q3_age4` | Age of person 4 | `Numeric(Byte)` | `%12.0g` |
| `si_q3_age5` | Age of person 5 | `Numeric(Byte)` | `%12.0g` |
| `si_q3_gen1` | Gender of person 1 | `Numeric(Byte)` | `%27.0g` |
| `si_q3_gen2` | Gender of person 2 | `Numeric(Byte)` | `%27.0g` |
| `si_q3_gen3` | Gender of person 3 | `Numeric(Byte)` | `%27.0g` |
| `si_q3_gen4` | Gender of person 4 | `Numeric(Byte)` | `%27.0g` |
| `si_q3_gen5` | Gender of person 5 | `Numeric(Byte)` | `%27.0g` |
| `si_q3_hh1` | Is person 1 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q3_hh2` | Is person 2 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q3_hh3` | Is person 3 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q3_hh4` | Is person 4 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q3_hh5` | Is person 5 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q3_time1` | Time spend helping person 1 | `Numeric(Float)` | `%tcHH:MM` |
| `si_q3_time2` | Time spend helping person 2 | `Numeric(Double)` | `%tcHH:MM` |
| `si_q3_time3` | Time spend helping person 3 | `Numeric(Double)` | `%tcHH:MM` |
| `si_q3_time4` | Time spend helping person 4 | `Numeric(Double)` | `%tcHH:MM` |
| `si_q3_time5` | Time spend helping person 5 | `Numeric(Byte)` | `%tcHH:MM` |
| `si_q4` | Did you receive help from other people in performing ADL yesterday? | `Numeric(Byte)` | `%10.0g` |
| `si_q4_1` | I received help in performing ADL from person 1 | `Numeric(Byte)` | `%53.0g` |
| `si_q4_2` | I received help in performing ADL from person 2 | `Numeric(Byte)` | `%53.0g` |
| `si_q4_3` | I received help in performing ADL from person 3 | `Numeric(Byte)` | `%53.0g` |
| `si_q4_4` | I received help in performing ADL from person 4 | `Numeric(Byte)` | `%53.0g` |
| `si_q4_5` | I received help in performing ADL from person 5 | `Numeric(Byte)` | `%53.0g` |
| `si_q4_age1` | Age of person 1 | `Numeric(Byte)` | `%12.0g` |
| `si_q4_age2` | Age of person 2 | `Numeric(Byte)` | `%12.0g` |
| `si_q4_age3` | Age of person 3 | `Numeric(Byte)` | `%12.0g` |
| `si_q4_age4` | Age of person 4 | `Numeric(Byte)` | `%12.0g` |
| `si_q4_age5` | Age of person 5 | `Numeric(Byte)` | `%12.0g` |
| `si_q4_gen1` | Gender of person 1 | `Numeric(Byte)` | `%27.0g` |
| `si_q4_gen2` | Gender of person 2 | `Numeric(Byte)` | `%27.0g` |
| `si_q4_gen3` | Gender of person 3 | `Numeric(Byte)` | `%27.0g` |
| `si_q4_gen4` | Gender of person 4 | `Numeric(Byte)` | `%27.0g` |
| `si_q4_gen5` | Gender of person 5 | `Numeric(Byte)` | `%27.0g` |
| `si_q4_hh1` | Is person 1 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q4_hh2` | Is person 2 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q4_hh3` | Is person 3 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q4_hh4` | Is person 4 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q4_hh5` | Is person 5 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q4_time1` | How much time did you receive help from person 1? | `Numeric(Float)` | `%tcHH:MM` |
| `si_q4_time2` | How much time did you receive help from person 2? | `Numeric(Float)` | `%tcHH:MM` |
| `si_q4_time3` | How much time did you receive help from person 3? | `Numeric(Double)` | `%tcHH:MM` |
| `si_q4_time4` | How much time did you receive help from person 4? | `Numeric(Double)` | `%tcHH:MM` |
| `si_q4_time5` | How much time did you receive help from person 5? | `Numeric(Byte)` | `%tcHH:MM` |
| `si_q5` | Did you receive help from other people in performing IADL yesterday? | `Numeric(Byte)` | `%10.0g` |
| `si_q5_1` | I received help in performing IADL from person 1 | `Numeric(Byte)` | `%53.0g` |
| `si_q5_2` | I received help in performing IADL from person 2 | `Numeric(Byte)` | `%53.0g` |
| `si_q5_3` | I received help in performing IADL from person 3 | `Numeric(Byte)` | `%53.0g` |
| `si_q5_4` | I received help in performing IADL from person 4 | `Numeric(Byte)` | `%53.0g` |
| `si_q5_5` | I received help in performing IADL from person 5 | `Numeric(Byte)` | `%53.0g` |
| `si_q5_age1` | Age of person 1 | `Numeric(Byte)` | `%12.0g` |
| `si_q5_age2` | Age of person 2 | `Numeric(Byte)` | `%12.0g` |
| `si_q5_age3` | Age of person 3 | `Numeric(Byte)` | `%12.0g` |
| `si_q5_age4` | Age of person 4 | `Numeric(Byte)` | `%12.0g` |
| `si_q5_age5` | Age of person 5 | `Numeric(Byte)` | `%12.0g` |
| `si_q5_gen1` | Gender of person 1 | `Numeric(Byte)` | `%27.0g` |
| `si_q5_gen2` | Gender of person 2 | `Numeric(Byte)` | `%27.0g` |
| `si_q5_gen3` | Gender of person 3 | `Numeric(Byte)` | `%27.0g` |
| `si_q5_gen4` | Gender of person 4 | `Numeric(Byte)` | `%27.0g` |
| `si_q5_gen5` | Gender of person 5 | `Numeric(Byte)` | `%27.0g` |
| `si_q5_hh1` | Is person 1 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q5_hh2` | Is person 2 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q5_hh3` | Is person 3 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q5_hh4` | Is person 4 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q5_hh5` | Is person 5 living in the same household? | `Numeric(Byte)` | `%10.0g` |
| `si_q5_time1` | How much time did you receive help from person 1? | `Numeric(Float)` | `%tcHH:MM` |
| `si_q5_time2` | How much time did you receive help from person 2? | `Numeric(Float)` | `%tcHH:MM` |
| `si_q5_time3` | How much time did you receive help from person 3? | `Numeric(Byte)` | `%tcHH:MM` |
| `si_q5_time4` | How much time did you receive help from person 4? | `Numeric(Byte)` | `%tcHH:MM` |
| `si_q5_time5` | How much time did you receive help from person 5? | `Numeric(Byte)` | `%tcHH:MM` |
| `si_q6a` | Days spent on holidays in the past 12 months | `Numeric(Int)` | `%10.0g` |
| `si_q6b` | Did you take care of a child/(great-)grandchild in the past 12 months? | `Numeric(Byte)` | `%10.0g` |
| `si_q6b_days` | How many days in the past 12 months? | `Numeric(Int)` | `%12.0g` |
| `si_q6b_hours` | How many hours per day in the past 12 months? | `Numeric(Double)` | `%10.0g` |
| `si_q6c` | Did you take care of an elderly parent in the past 12 months? | `Numeric(Byte)` | `%10.0g` |
| `si_q6c_days` | How many days in the past 12 months? | `Numeric(Int)` | `%12.0g` |
| `si_q6c_hours` | How many hours per day in the past 12 months? | `Numeric(Double)` | `%10.0g` |

### `technical_variables` - Technical variables

- Dataset: `sharew7_rel9-0-0_technical_variables.dta`
- Read with: `ps.read_share_module("technical_variables", wave=7)`
- Rows: 77,181
- Variables: 17
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `fam_resp` | Family respondent | `Numeric(Byte)` | `%21.0g` |
| `fin_resp` | Financial respondent | `Numeric(Byte)` | `%24.0g` |
| `hou_resp` | Household respondent | `Numeric(Byte)` | `%24.0g` |
| `mn005_` | Single or couple interview | `Numeric(Byte)` | `%37.0g` |
| `mn024_` | Nursing home interview | `Numeric(Byte)` | `%17.0g` |
| `mn026_` | First respondent from couple or single | `Numeric(Byte)` | `%10.0g` |
| `mn029_` | Eligible for linkage | `Numeric(Byte)` | `%16.0g` |
| `mn032_` | Eligible for social exclusion items | `Numeric(Byte)` | `%10.0g` |
| `mn101_` | Questionnaire version | `Numeric(Byte)` | `%26.0g` |
| `mn103_` | SHARELIFE life history interview | `Numeric(Byte)` | `%10.0g` |
| `mn104_` | Household moved | `Numeric(Byte)` | `%10.0g` |


## SHARELIFE Modules

### `cc` - Childhood Circumstances

- Dataset: `sharew7_rel9-0-0_cc.dta`
- Read with: `ps.read_share_module("cc", wave=7)`
- Rows: 77,181
- Variables: 46
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `cc002_` | Rooms when ten years old | `Numeric(Byte)` | `%10.0g` |
| `cc003_` | Number of people living in household when ten | `Numeric(Byte)` | `%10.0g` |
| `cc008_` | Number of books when ten | `Numeric(Byte)` | `%58.0g` |
| `cc733_` | Family was pretty well off financially, about average, or poor | `Numeric(Byte)` | `%49.0g` |
| `cc734_` | Financial difficulties cause family to move | `Numeric(Byte)` | `%10.0g` |
| `cc735_` | Received help from relatives because of financial difficulties | `Numeric(Byte)` | `%10.0g` |
| `cc736_` | Father had no job | `Numeric(Byte)` | `%98.0g` |
| `cc010_` | Relative position to others when ten: mathematically | `Numeric(Byte)` | `%43.0g` |
| `cc010a_` | Relative position to others when ten: language | `Numeric(Byte)` | `%36.0g` |
| `cc721_1` | How much did your mother understand your problems and worries | `Numeric(Byte)` | `%16.0g` |
| `cc722_1` | How would you rate the relationship with your mother | `Numeric(Byte)` | `%13.0g` |
| `cc721_2` | How much did your father understand your problems and worries | `Numeric(Byte)` | `%16.0g` |
| `cc722_2` | How would you rate the relationship with your father | `Numeric(Byte)` | `%13.0g` |
| `cc725_1` | Mother physical harm | `Numeric(Byte)` | `%10.0g` |
| `cc725_2` | Father physical harm | `Numeric(Byte)` | `%10.0g` |
| `cc727_` | Anybody else physical harm | `Numeric(Byte)` | `%10.0g` |
| `cc728_` | Importance of religion at home when growing up | `Numeric(Byte)` | `%24.0g` |
| `cc729_` | Lonely for friends in childhood | `Numeric(Byte)` | `%10.0g` |
| `cc730_` | Group of friends felt comfortable spending time with | `Numeric(Byte)` | `%10.0g` |
| `cc731_` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `cc012_` | Proxy check | `Numeric(Byte)` | `%44.0g` |
| `cc004d1` | Lived in hh when ten: biological mother | `Numeric(Byte)` | `%12.0g` |
| `cc004d2` | Lived in hh when ten: biological father | `Numeric(Byte)` | `%12.0g` |
| `cc004d3` | Lived in hh when ten: adoptive/step/foster mother | `Numeric(Byte)` | `%12.0g` |
| `cc004d4` | Lived in hh when ten: adoptive/step/foster father | `Numeric(Byte)` | `%12.0g` |
| `cc004d5` | Lived in hh when ten: biological sibling(s) | `Numeric(Byte)` | `%12.0g` |
| `cc004d6` | Lived in hh when ten: adoptive/step/foster/half sibling(s) | `Numeric(Byte)` | `%12.0g` |
| `cc004d7` | Lived in hh when ten: grandparent(s) | `Numeric(Byte)` | `%12.0g` |
| `cc004d8` | Lived in hh when ten: other relative(s) | `Numeric(Byte)` | `%12.0g` |
| `cc004d9` | Lived in hh when ten: other non-relative(s) | `Numeric(Byte)` | `%12.0g` |
| `cc007d1` | Features of accommodation when ten: fixed bath | `Numeric(Byte)` | `%12.0g` |
| `cc007d2` | Features of accommodation when ten: cold running water supply | `Numeric(Byte)` | `%12.0g` |
| `cc007d3` | Features of accommodation when ten: hot running water supply | `Numeric(Byte)` | `%12.0g` |
| `cc007d4` | Features of accommodation when ten: inside toilet | `Numeric(Byte)` | `%12.0g` |
| `cc007d5` | Features of accommodation when ten: central heating | `Numeric(Byte)` | `%12.0g` |
| `cc007dno` | Features of accommodation when ten: none of these | `Numeric(Byte)` | `%12.0g` |
| `cc720d1` | Intro: Relationship parents/person that raised you | `Numeric(Byte)` | `%12.0g` |
| `cc720d8` | SPONTANEOUS ONLY: didn't live with mother or had no female caregiver | `Numeric(Byte)` | `%12.0g` |
| `cc720d9` | SPONTANEOUS ONLY: didn't live with father or had no male caregiver | `Numeric(Byte)` | `%12.0g` |
| `cc009isco` | ISCO code: Occupation of main breadwinner when ten | `Numeric(Int)` | `%13.0g` |

### `dq` - Disability

- Dataset: `sharew7_rel9-0-0_dq.dta`
- Read with: `ps.read_share_module("dq", wave=7)`
- Rows: 77,181
- Variables: 255
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `dq001_` | Ever left job because of disability | `Numeric(Byte)` | `%10.0g` |
| `dq003_1` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_1` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_2` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_2` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_3` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_3` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_4` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_4` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_5` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_5` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_6` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_6` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_7` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_7` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_8` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_8` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_9` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_9` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_10` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_10` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_11` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_11` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_12` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_12` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_13` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_13` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_14` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_14` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_15` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq005_15` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `dq003_16` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq003_17` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq003_19` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq003_20` | Extent of limitation | `Numeric(Byte)` | `%45.0g` |
| `dq007_` | Took temporary leave of absence for disability | `Numeric(Byte)` | `%10.0g` |
| `dq008_1` | Temp leave which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq009_1` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `dq010_1` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `dq012_1` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `dq008_2` | Temp leave which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq009_2` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `dq010_2` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `dq012_2` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `dq008_3` | Temp leave which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq009_3` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `dq010_3` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `dq012_3` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `dq008_4` | Temp leave which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq009_4` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `dq010_4` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `dq012_4` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `dq008_5` | Temp leave which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq009_5` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `dq010_5` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `dq012_5` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `dq008_6` | Temp leave which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq009_6` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `dq010_6` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `dq012_6` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `dq008_7` | Temp leave which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq009_7` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `dq010_7` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `dq012_7` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `dq008_8` | Temp leave which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq009_8` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `dq010_8` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `dq012_8` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `dq008_9` | Temp leave which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq009_9` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `dq010_9` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `dq012_9` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `dq008_10` | Temp leave which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq009_10` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `dq010_10` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `dq012_10` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `dq008_11` | Temp leave which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq009_11` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `dq010_11` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `dq012_11` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `dq008_12` | Temp leave which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq009_12` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `dq010_12` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `dq012_12` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `dq013_` | Ever limited hours because of disability | `Numeric(Byte)` | `%10.0g` |
| `dq014_1` | Left which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq015_1` | Reduction extent of hours | `Numeric(Byte)` | `%10.0g` |
| `dq016_1` | Other jobs reduce hours for disability | `Numeric(Byte)` | `%10.0g` |
| `dq014_2` | Left which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq015_2` | Reduction extent of hours | `Numeric(Byte)` | `%10.0g` |
| `dq016_2` | Other jobs reduce hours for disability | `Numeric(Byte)` | `%10.0g` |
| `dq014_3` | Left which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq015_3` | Reduction extent of hours | `Numeric(Byte)` | `%10.0g` |
| `dq016_3` | Other jobs reduce hours for disability | `Numeric(Byte)` | `%10.0g` |
| `dq014_4` | Left which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq015_4` | Reduction extent of hours | `Numeric(Byte)` | `%10.0g` |
| `dq016_4` | Other jobs reduce hours for disability | `Numeric(Byte)` | `%10.0g` |
| `dq014_5` | Left which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq015_5` | Reduction extent of hours | `Numeric(Byte)` | `%10.0g` |
| `dq016_5` | Other jobs reduce hours for disability | `Numeric(Byte)` | `%10.0g` |
| `dq014_6` | Left which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq015_6` | Reduction extent of hours | `Numeric(Byte)` | `%10.0g` |
| `dq016_6` | Other jobs reduce hours for disability | `Numeric(Byte)` | `%10.0g` |
| `dq014_7` | Left which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq015_7` | Reduction extent of hours | `Numeric(Byte)` | `%10.0g` |
| `dq016_7` | Other jobs reduce hours for disability | `Numeric(Byte)` | `%10.0g` |
| `dq014_8` | Left which job because of disability | `Numeric(Byte)` | `%14.0g` |
| `dq015_8` | Reduction extent of hours | `Numeric(Byte)` | `%10.0g` |
| `dq016_8` | Other jobs reduce hours for disability | `Numeric(Byte)` | `%10.0g` |
| `dq017_` | Ever applied for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `dq018_1` | When apply for public disability pension | `Numeric(Int)` | `%10.0g` |
| `dq019_1` | Was public disability pension granted | `Numeric(Byte)` | `%19.0g` |
| `dq020_1` | Ever again apply for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `dq018_2` | When apply for public disability pension | `Numeric(Int)` | `%10.0g` |
| `dq019_2` | Was public disability pension granted | `Numeric(Byte)` | `%19.0g` |
| `dq020_2` | Ever again apply for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `dq018_3` | When apply for public disability pension | `Numeric(Int)` | `%10.0g` |
| `dq019_3` | Was public disability pension granted | `Numeric(Byte)` | `%19.0g` |
| `dq020_3` | Ever again apply for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `dq018_4` | When apply for public disability pension | `Numeric(Int)` | `%10.0g` |
| `dq019_4` | Was public disability pension granted | `Numeric(Byte)` | `%19.0g` |
| `dq020_4` | Ever again apply for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `dq018_5` | When apply for public disability pension | `Numeric(Int)` | `%10.0g` |
| `dq019_5` | Was public disability pension granted | `Numeric(Byte)` | `%19.0g` |
| `dq020_5` | Ever again apply for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `dq018_6` | When apply for public disability pension | `Numeric(Int)` | `%10.0g` |
| `dq019_6` | Was public disability pension granted | `Numeric(Byte)` | `%19.0g` |
| `dq020_6` | Ever again apply for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `dq018_7` | When apply for public disability pension | `Numeric(Int)` | `%10.0g` |
| `dq019_7` | Was public disability pension granted | `Numeric(Byte)` | `%19.0g` |
| `dq020_7` | Ever again apply for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `dq021a_` | Ever purchased private disability insurance | `Numeric(Byte)` | `%10.0g` |
| `dq021_` | Ever applied for private disability insurance | `Numeric(Byte)` | `%10.0g` |
| `dq022_1` | When apply for private disability insurance | `Numeric(Int)` | `%10.0g` |
| `dq023_1` | Was private disability insurance granted | `Numeric(Byte)` | `%19.0g` |
| `dq024_1` | Ever again apply for private disability insurance | `Numeric(Byte)` | `%10.0g` |
| `dq022_2` | When apply for private disability insurance | `Numeric(Int)` | `%10.0g` |
| `dq023_2` | Was private disability insurance granted | `Numeric(Byte)` | `%19.0g` |
| `dq024_2` | Ever again apply for private disability insurance | `Numeric(Byte)` | `%10.0g` |
| `dq022_3` | When apply for private disability insurance | `Numeric(Int)` | `%10.0g` |
| `dq023_3` | Was private disability insurance granted | `Numeric(Byte)` | `%19.0g` |
| `dq024_3` | Ever again apply for private disability insurance | `Numeric(Byte)` | `%10.0g` |
| `dq022_4` | When apply for private disability insurance | `Numeric(Int)` | `%10.0g` |
| `dq023_4` | Was private disability insurance granted | `Numeric(Byte)` | `%19.0g` |
| `dq024_4` | Ever again apply for private disability insurance | `Numeric(Byte)` | `%10.0g` |
| `dq002d1` | Left which job because of disability: job 1 | `Numeric(Byte)` | `%12.0g` |
| `dq002d2` | Left which job because of disability: job 2 | `Numeric(Byte)` | `%12.0g` |
| `dq002d3` | Left which job because of disability: job 3 | `Numeric(Byte)` | `%12.0g` |
| `dq002d4` | Left which job because of disability: job 4 | `Numeric(Byte)` | `%12.0g` |
| `dq002d5` | Left which job because of disability: job 5 | `Numeric(Byte)` | `%12.0g` |
| `dq002d6` | Left which job because of disability: job 6 | `Numeric(Byte)` | `%12.0g` |
| `dq002d7` | Left which job because of disability: job 7 | `Numeric(Byte)` | `%12.0g` |
| `dq002d8` | Left which job because of disability: job 8 | `Numeric(Byte)` | `%12.0g` |
| `dq002d9` | Left which job because of disability: job 9 | `Numeric(Byte)` | `%12.0g` |
| `dq002d10` | Left which job because of disability: job 10 | `Numeric(Byte)` | `%12.0g` |
| `dq002d11` | Left which job because of disability: job 11 | `Numeric(Byte)` | `%12.0g` |
| `dq002d12` | Left which job because of disability: job 12 | `Numeric(Byte)` | `%12.0g` |
| `dq002d13` | Left which job because of disability: job 13 | `Numeric(Byte)` | `%12.0g` |
| `dq002d14` | Left which job because of disability: job 14 | `Numeric(Byte)` | `%12.0g` |
| `dq002d15` | Left which job because of disability: job 15 | `Numeric(Byte)` | `%12.0g` |
| `dq002d16` | Left which job because of disability: job 16 | `Numeric(Byte)` | `%12.0g` |
| `dq002d17` | Left which job because of disability: job 17 | `Numeric(Byte)` | `%12.0g` |
| `dq002d18` | Left which job because of disability: job 18 | `Numeric(Byte)` | `%12.0g` |
| `dq002d19` | Left which job because of disability: job 19 | `Numeric(Byte)` | `%12.0g` |
| `dq002d20` | Left which job because of disability: job 20 | `Numeric(Byte)` | `%12.0g` |
| `dq011d1_1` | Income during gap after leaving job 1: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `dq011d2_1` | Income during gap after leaving job 1: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `dq011d3_1` | Income during gap after leaving job 1: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `dq011d4_1` | Income during gap after leaving job 1: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `dq011d5_1` | Income during gap after leaving job 1: sold property | `Numeric(Byte)` | `%12.0g` |
| `dq011d6_1` | Income during gap after leaving job 1: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `dq011dot_1` | Income during gap after leaving job 1: other | `Numeric(Byte)` | `%12.0g` |
| `dq011d1_2` | Income during gap after leaving job 2: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `dq011d2_2` | Income during gap after leaving job 2: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `dq011d3_2` | Income during gap after leaving job 2: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `dq011d4_2` | Income during gap after leaving job 2: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `dq011d5_2` | Income during gap after leaving job 2: sold property | `Numeric(Byte)` | `%12.0g` |
| `dq011d6_2` | Income during gap after leaving job 2: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `dq011dot_2` | Income during gap after leaving job 2: other | `Numeric(Byte)` | `%12.0g` |
| `dq011d1_3` | Income during gap after leaving job 3: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `dq011d2_3` | Income during gap after leaving job 3: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `dq011d3_3` | Income during gap after leaving job 3: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `dq011d4_3` | Income during gap after leaving job 3: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `dq011d5_3` | Income during gap after leaving job 3: sold property | `Numeric(Byte)` | `%12.0g` |
| `dq011d6_3` | Income during gap after leaving job 3: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `dq011dot_3` | Income during gap after leaving job 3: other | `Numeric(Byte)` | `%12.0g` |
| `dq011d1_4` | Income during gap after leaving job 4: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `dq011d2_4` | Income during gap after leaving job 4: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `dq011d3_4` | Income during gap after leaving job 4: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `dq011d4_4` | Income during gap after leaving job 4: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `dq011d5_4` | Income during gap after leaving job 4: sold property | `Numeric(Byte)` | `%12.0g` |
| `dq011d6_4` | Income during gap after leaving job 4: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `dq011dot_4` | Income during gap after leaving job 4: other | `Numeric(Byte)` | `%12.0g` |
| `dq011d1_5` | Income during gap after leaving job 5: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `dq011d2_5` | Income during gap after leaving job 5: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `dq011d3_5` | Income during gap after leaving job 5: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `dq011d4_5` | Income during gap after leaving job 5: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `dq011d5_5` | Income during gap after leaving job 5: sold property | `Numeric(Byte)` | `%12.0g` |
| `dq011d6_5` | Income during gap after leaving job 5: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `dq011dot_5` | Income during gap after leaving job 5: other | `Numeric(Byte)` | `%12.0g` |
| `dq011d1_6` | Income during gap after leaving job 6: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `dq011d2_6` | Income during gap after leaving job 6: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `dq011d3_6` | Income during gap after leaving job 6: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `dq011d4_6` | Income during gap after leaving job 6: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `dq011d5_6` | Income during gap after leaving job 6: sold property | `Numeric(Byte)` | `%12.0g` |
| `dq011d6_6` | Income during gap after leaving job 6: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `dq011dot_6` | Income during gap after leaving job 6: other | `Numeric(Byte)` | `%12.0g` |
| `dq011d1_7` | Income during gap after leaving job 7: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `dq011d2_7` | Income during gap after leaving job 7: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `dq011d3_7` | Income during gap after leaving job 7: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `dq011d4_7` | Income during gap after leaving job 7: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `dq011d5_7` | Income during gap after leaving job 7: sold property | `Numeric(Byte)` | `%12.0g` |
| `dq011d6_7` | Income during gap after leaving job 7: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `dq011dot_7` | Income during gap after leaving job 7: other | `Numeric(Byte)` | `%12.0g` |
| `dq011d1_8` | Income during gap after leaving job 8: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `dq011d2_8` | Income during gap after leaving job 8: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `dq011d3_8` | Income during gap after leaving job 8: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `dq011d4_8` | Income during gap after leaving job 8: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `dq011d5_8` | Income during gap after leaving job 8: sold property | `Numeric(Byte)` | `%12.0g` |
| `dq011d6_8` | Income during gap after leaving job 8: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `dq011dot_8` | Income during gap after leaving job 8: other | `Numeric(Byte)` | `%12.0g` |
| `dq011d1_9` | Income during gap after leaving job 9: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `dq011d2_9` | Income during gap after leaving job 9: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `dq011d3_9` | Income during gap after leaving job 9: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `dq011d4_9` | Income during gap after leaving job 9: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `dq011d5_9` | Income during gap after leaving job 9: sold property | `Numeric(Byte)` | `%12.0g` |
| `dq011d6_9` | Income during gap after leaving job 9: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `dq011dot_9` | Income during gap after leaving job 9: other | `Numeric(Byte)` | `%12.0g` |
| `dq011d1_10` | Income during gap after leaving job 10: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `dq011d2_10` | Income during gap after leaving job 10: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `dq011d3_10` | Income during gap after leaving job 10: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `dq011d4_10` | Income during gap after leaving job 10: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `dq011d5_10` | Income during gap after leaving job 10: sold property | `Numeric(Byte)` | `%12.0g` |
| `dq011d6_10` | Income during gap after leaving job 10: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `dq011dot_10` | Income during gap after leaving job 10: other | `Numeric(Byte)` | `%12.0g` |
| `dq011d1_11` | Income during gap after leaving job 11: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `dq011d2_11` | Income during gap after leaving job 11: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `dq011d3_11` | Income during gap after leaving job 11: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `dq011d4_11` | Income during gap after leaving job 11: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `dq011d5_11` | Income during gap after leaving job 11: sold property | `Numeric(Byte)` | `%12.0g` |
| `dq011d6_11` | Income during gap after leaving job 11: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `dq011dot_11` | Income during gap after leaving job 11: other | `Numeric(Byte)` | `%12.0g` |
| `dq011d1_12` | Income during gap after leaving job 12: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `dq011d2_12` | Income during gap after leaving job 12: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `dq011d3_12` | Income during gap after leaving job 12: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `dq011d4_12` | Income during gap after leaving job 12: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `dq011d5_12` | Income during gap after leaving job 12: sold property | `Numeric(Byte)` | `%12.0g` |
| `dq011d6_12` | Income during gap after leaving job 12: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `dq011dot_12` | Income during gap after leaving job 12: other | `Numeric(Byte)` | `%12.0g` |

### `fs` - Financial Section

- Dataset: `sharew7_rel9-0-0_fs.dta`
- Read with: `ps.read_share_module("fs", wave=7)`
- Rows: 77,181
- Variables: 17
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `fs002_` | Ever had any stocks or shares | `Numeric(Byte)` | `%10.0g` |
| `fs003_` | When invested in stocks first | `Numeric(Int)` | `%10.0g` |
| `fs004_` | Ever had any mutual funds | `Numeric(Byte)` | `%10.0g` |
| `fs005_` | When invested in mutual funds first | `Numeric(Int)` | `%10.0g` |
| `fs006_` | Ever had retirement account | `Numeric(Byte)` | `%10.0g` |
| `fs007_` | When subscribed to retirement account first | `Numeric(Int)` | `%10.0g` |
| `fs008_` | Ever taken out a life insurance policy | `Numeric(Byte)` | `%10.0g` |
| `fs009_` | When taken out a life insurance policy first | `Numeric(Int)` | `%10.0g` |
| `fs010_` | Ever owned business | `Numeric(Byte)` | `%10.0g` |
| `fs011_` | When first owned business | `Numeric(Int)` | `%10.0g` |
| `fs013_` | Proxy check | `Numeric(Byte)` | `%44.0g` |

### `gl` - General Life and Persecution

- Dataset: `sharew7_rel9-0-0_gl.dta`
- Read with: `ps.read_share_module("gl", wave=7)`
- Rows: 77,181
- Variables: 92
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `gl002_` | Period of happiness | `Numeric(Byte)` | `%10.0g` |
| `gl003_` | When happiness period started | `Numeric(Int)` | `%10.0g` |
| `gl004_` | When happiness period stopped | `Numeric(Int)` | `%21.0g` |
| `gl005_` | Period of stress | `Numeric(Byte)` | `%10.0g` |
| `gl006_` | When stress period started | `Numeric(Int)` | `%10.0g` |
| `gl007_` | When stress period stopped | `Numeric(Int)` | `%21.0g` |
| `gl011_` | Period of financial hardship | `Numeric(Byte)` | `%10.0g` |
| `gl012_` | When financial hardship period started | `Numeric(Int)` | `%10.0g` |
| `gl013_` | When financial hardship period stopped | `Numeric(Int)` | `%21.0g` |
| `gl014_` | Period of hunger | `Numeric(Byte)` | `%10.0g` |
| `gl015_` | When hunger period started | `Numeric(Int)` | `%10.0g` |
| `gl016_` | When hunger period stopped | `Numeric(Int)` | `%21.0g` |
| `gl022_` | Discriminated against | `Numeric(Byte)` | `%10.0g` |
| `gl023_` | Main reason of persecution | `Numeric(Byte)` | `%63.0g` |
| `gl024_` | Forced to stop working | `Numeric(Byte)` | `%10.0g` |
| `gl028_` | Difficulties finding a job because of reason for persecution | `Numeric(Byte)` | `%10.0g` |
| `gl029_` | First experience difficulties finding a job | `Numeric(Int)` | `%10.0g` |
| `gl031_` | Dispossessed because of reason for persecution | `Numeric(Byte)` | `%10.0g` |
| `gl030_1` | In prison because of reason for persecution | `Numeric(Byte)` | `%10.0g` |
| `gl030_2` | In prisoner of war camp because of reason for persecution | `Numeric(Byte)` | `%10.0g` |
| `gl030_3` | In labour camp because of reason for persecution | `Numeric(Byte)` | `%10.0g` |
| `gl030_4` | In concentration camp because of reason for persecution | `Numeric(Byte)` | `%10.0g` |
| `gl030_6` | Were exiled or banished because of reason for persecution | `Numeric(Byte)` | `%10.0g` |
| `gl033_1` | When property taken away | `Numeric(Int)` | `%10.0g` |
| `gl034_1` | Compensated | `Numeric(Byte)` | `%16.0g` |
| `gl035_1` | Another time dispossessed of any property | `Numeric(Byte)` | `%10.0g` |
| `gl033_2` | When property taken away | `Numeric(Int)` | `%10.0g` |
| `gl034_2` | Compensated | `Numeric(Byte)` | `%16.0g` |
| `gl035_2` | Another time dispossessed of any property | `Numeric(Byte)` | `%10.0g` |
| `gl033_3` | When property taken away | `Numeric(Int)` | `%10.0g` |
| `gl034_3` | Compensated | `Numeric(Byte)` | `%16.0g` |
| `gl035_3` | Another time dispossessed of any property | `Numeric(Byte)` | `%10.0g` |
| `gl033_4` | When property taken away | `Numeric(Int)` | `%10.0g` |
| `gl034_4` | Compensated | `Numeric(Byte)` | `%16.0g` |
| `gl035_4` | Another time dispossessed of any property | `Numeric(Byte)` | `%10.0g` |
| `gl033_5` | When property taken away | `Numeric(Int)` | `%10.0g` |
| `gl034_5` | Compensated | `Numeric(Byte)` | `%16.0g` |
| `gl035_5` | Another time dispossessed of any property | `Numeric(Byte)` | `%10.0g` |
| `gl036_` | Proxy check | `Numeric(Byte)` | `%44.0g` |
| `gl026d1` | Experiences in job: denied promotions | `Numeric(Byte)` | `%12.0g` |
| `gl026d2` | Experiences in job: assignment to a task with fewer responsibilities | `Numeric(Byte)` | `%12.0g` |
| `gl026d3` | Experiences in job: working on tasks below your qualifications | `Numeric(Byte)` | `%12.0g` |
| `gl026d4` | Experiences in job: harassment by your boss or colleagues | `Numeric(Byte)` | `%12.0g` |
| `gl026d5` | Experiences in job: pay cuts | `Numeric(Byte)` | `%12.0g` |
| `gl026dno` | Experiences in job: none of these | `Numeric(Byte)` | `%12.0g` |
| `gl032d1_1` | Type of property: businesses or companies | `Numeric(Byte)` | `%12.0g` |
| `gl032d2_1` | Type of property: houses or buildings | `Numeric(Byte)` | `%12.0g` |
| `gl032d3_1` | Type of property: farmland or other land | `Numeric(Byte)` | `%12.0g` |
| `gl032d4_1` | Type of property: flat or apartment | `Numeric(Byte)` | `%12.0g` |
| `gl032d5_1` | Type of property: money or assets | `Numeric(Byte)` | `%12.0g` |
| `gl032d1_2` | Type of property: businesses or companies | `Numeric(Byte)` | `%12.0g` |
| `gl032d2_2` | Type of property: houses or buildings | `Numeric(Byte)` | `%12.0g` |
| `gl032d3_2` | Type of property: farmland or other land | `Numeric(Byte)` | `%12.0g` |
| `gl032d4_2` | Type of property: flat or apartment | `Numeric(Byte)` | `%12.0g` |
| `gl032d5_2` | Type of property: money or assets | `Numeric(Byte)` | `%12.0g` |
| `gl032d1_3` | Type of property: businesses or companies | `Numeric(Byte)` | `%12.0g` |
| `gl032d2_3` | Type of property: houses or buildings | `Numeric(Byte)` | `%12.0g` |
| `gl032d3_3` | Type of property: farmland or other land | `Numeric(Byte)` | `%12.0g` |
| `gl032d4_3` | Type of property: flat or apartment | `Numeric(Byte)` | `%12.0g` |
| `gl032d5_3` | Type of property: money or assets | `Numeric(Byte)` | `%12.0g` |
| `gl032d1_4` | Type of property: businesses or companies | `Numeric(Byte)` | `%12.0g` |
| `gl032d2_4` | Type of property: houses or buildings | `Numeric(Byte)` | `%12.0g` |
| `gl032d3_4` | Type of property: farmland or other land | `Numeric(Byte)` | `%12.0g` |
| `gl032d4_4` | Type of property: flat or apartment | `Numeric(Byte)` | `%12.0g` |
| `gl032d5_4` | Type of property: money or assets | `Numeric(Byte)` | `%12.0g` |
| `gl032d1_5` | Type of property: businesses or companies | `Numeric(Byte)` | `%12.0g` |
| `gl032d2_5` | Type of property: houses or buildings | `Numeric(Byte)` | `%12.0g` |
| `gl032d3_5` | Type of property: farmland or other land | `Numeric(Byte)` | `%12.0g` |
| `gl032d4_5` | Type of property: flat or apartment | `Numeric(Byte)` | `%12.0g` |
| `gl032d5_5` | Type of property: money or assets | `Numeric(Byte)` | `%12.0g` |
| `gl738d1` | Discriminated against mother: imprisonment | `Numeric(Byte)` | `%12.0g` |
| `gl738d2` | Discriminated against mother: labour camp | `Numeric(Byte)` | `%12.0g` |
| `gl738d3` | Discriminated against mother: concentration camp | `Numeric(Byte)` | `%12.0g` |
| `gl738d4` | Discriminated against mother: deportation, forced displacement or flight | `Numeric(Byte)` | `%12.0g` |
| `gl738d5` | Discriminated against mother: engaged in combat operations/fighting | `Numeric(Byte)` | `%12.0g` |
| `gl738d6` | Discriminated against mother: serious damage to health or injury | `Numeric(Byte)` | `%12.0g` |
| `gl738d7` | Discriminated against mother: death | `Numeric(Byte)` | `%12.0g` |
| `gl738dno` | Discriminated against mother: none of these | `Numeric(Byte)` | `%12.0g` |
| `gl740d1` | Discriminated against father: imprisonment | `Numeric(Byte)` | `%12.0g` |
| `gl740d2` | Discriminated against father: labour camp | `Numeric(Byte)` | `%12.0g` |
| `gl740d3` | Discriminated against father: concentration camp | `Numeric(Byte)` | `%12.0g` |
| `gl740d4` | Discriminated against father: deportation, forced displacement or flight | `Numeric(Byte)` | `%12.0g` |
| `gl740d5` | Discriminated against father: engaged in combat operations/fighting | `Numeric(Byte)` | `%12.0g` |
| `gl740d6` | Discriminated against father: serious damage to health or injury | `Numeric(Byte)` | `%12.0g` |
| `gl740d7` | Discriminated against father: death | `Numeric(Byte)` | `%12.0g` |
| `gl740dno` | Discriminated against father: none of these | `Numeric(Byte)` | `%12.0g` |

### `hs` - Health History / Health Section

- Dataset: `sharew7_rel9-0-0_hs.dta`
- Read with: `ps.read_share_module("hs", wave=7)`
- Rows: 77,181
- Variables: 139
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `hs003_` | Childhood health status | `Numeric(Byte)` | `%52.0g` |
| `hs004_` | Childhood health: missed school for 1 month or longer | `Numeric(Byte)` | `%10.0g` |
| `hs005_` | Childhood health: confined to bed or home for 1 month or longer | `Numeric(Byte)` | `%10.0g` |
| `hs006_` | Childhood health: in hospital for 1 month or longer | `Numeric(Byte)` | `%10.0g` |
| `hs052_` | Ever had physical injury to disability | `Numeric(Byte)` | `%10.0g` |
| `hs053_` | When received this injury | `Numeric(Int)` | `%10.0g` |
| `hs054_` | Number periods of ill health | `Numeric(Byte)` | `%83.0g` |
| `hs059_1` | When did illness period 1 start | `Numeric(Int)` | `%10.0g` |
| `hs060_1` | When did illness period 1 stop | `Numeric(Int)` | `%21.0g` |
| `hs061_1` | Did family and friends help (illness period 1) | `Numeric(Byte)` | `%22.0g` |
| `hs059_2` | When did illness period 2 start | `Numeric(Int)` | `%10.0g` |
| `hs060_2` | When did illness period 2 stop | `Numeric(Int)` | `%21.0g` |
| `hs061_2` | Did family and friends help (illness period 2) | `Numeric(Byte)` | `%22.0g` |
| `hs059_3` | When did illness period 3 start | `Numeric(Int)` | `%10.0g` |
| `hs060_3` | When did illness period 3 stop | `Numeric(Int)` | `%21.0g` |
| `hs061_3` | Did family and friends help (illness period 3) | `Numeric(Byte)` | `%22.0g` |
| `hs066_` | Proxy check | `Numeric(Byte)` | `%44.0g` |
| `hs008d1` | Childhood illness 1: infectious disease | `Numeric(Byte)` | `%12.0g` |
| `hs008d2` | Childhood illness 1: polio | `Numeric(Byte)` | `%12.0g` |
| `hs008d3` | Childhood illness 1: asthma | `Numeric(Byte)` | `%12.0g` |
| `hs008d4` | Childhood illness 1: respiratory problems other than asthma | `Numeric(Byte)` | `%12.0g` |
| `hs008d5` | Childhood illness 1: allergies (other than asthma) | `Numeric(Byte)` | `%12.0g` |
| `hs008d6` | Childhood illness 1: severe diarrhoea | `Numeric(Byte)` | `%12.0g` |
| `hs008d7` | Childhood illness 1: meningitis/encephalitis | `Numeric(Byte)` | `%12.0g` |
| `hs008d8` | Childhood illness 1: chronic ear problems | `Numeric(Byte)` | `%12.0g` |
| `hs008d9` | Childhood illness 1: speech impairment | `Numeric(Byte)` | `%12.0g` |
| `hs008d10` | Childhood illness 1: difficulty seeing even with eyeglasses | `Numeric(Byte)` | `%12.0g` |
| `hs008dno` | Childhood illness 1: none of these | `Numeric(Byte)` | `%12.0g` |
| `hs009d1` | Childhood illness 2: severe headaches or migraines | `Numeric(Byte)` | `%12.0g` |
| `hs009d2` | Childhood illness 2: epilepsy, fits or seizures | `Numeric(Byte)` | `%12.0g` |
| `hs009d3` | Childhood illness 2: emotional, nervous, or psychiatric problem | `Numeric(Byte)` | `%12.0g` |
| `hs009d4` | Childhood illness 2: broken bones, fractures | `Numeric(Byte)` | `%12.0g` |
| `hs009d5` | Childhood illness 2: appendicitis | `Numeric(Byte)` | `%12.0g` |
| `hs009d6` | Childhood illness 2: childhood diabetes or high blood sugar | `Numeric(Byte)` | `%12.0g` |
| `hs009d7` | Childhood illness 2: heart trouble | `Numeric(Byte)` | `%12.0g` |
| `hs009d8` | Childhood illness 2: leukaemia or lymphoma | `Numeric(Byte)` | `%12.0g` |
| `hs009d9` | Childhood illness 2: cancer or malignant tumour (excluding minor skin cancers) | `Numeric(Byte)` | `%12.0g` |
| `hs009d10` | Childhood illness 2: rickets, osteomalacia, rachitis | `Numeric(Byte)` | `%12.0g` |
| `hs009dno` | Childhood illness 2: none of these | `Numeric(Byte)` | `%12.0g` |
| `hs009dot` | Childhood illness 2: other serious health condition | `Numeric(Byte)` | `%12.0g` |
| `hs055d1_1` | Type 1 illness period 1: back pain | `Numeric(Byte)` | `%12.0g` |
| `hs055d2_1` | Type 1 illness period 1: arthritis, including osteoarthritis and rheumatism | `Numeric(Byte)` | `%12.0g` |
| `hs055d3_1` | Type 1 illness period 1: osteoporosis | `Numeric(Byte)` | `%12.0g` |
| `hs055d4_1` | Type 1 illness period 1: angina or heart attack | `Numeric(Byte)` | `%12.0g` |
| `hs055d5_1` | Type 1 illness period 1: other heart disease | `Numeric(Byte)` | `%12.0g` |
| `hs055d6_1` | Type 1 illness period 1: diabetes or high blood sugar | `Numeric(Byte)` | `%12.0g` |
| `hs055d7_1` | Type 1 illness period 1: stroke | `Numeric(Byte)` | `%12.0g` |
| `hs055d8_1` | Type 1 illness period 1: asthma | `Numeric(Byte)` | `%12.0g` |
| `hs055d9_1` | Type 1 illness period 1: respiratory problems other than asthma | `Numeric(Byte)` | `%12.0g` |
| `hs055d10_1` | Type 1 illness period 1: tuberculosis | `Numeric(Byte)` | `%12.0g` |
| `hs055d11_1` | Type 1 illness period 1: severe headaches or migraines | `Numeric(Byte)` | `%12.0g` |
| `hs055dno_1` | Type 1 illness period 1: none of these | `Numeric(Byte)` | `%12.0g` |
| `hs055d1_2` | Type 1 illness period 2: back pain | `Numeric(Byte)` | `%12.0g` |
| `hs055d2_2` | Type 1 illness period 2: arthritis, including osteoarthritis and rheumatism | `Numeric(Byte)` | `%12.0g` |
| `hs055d3_2` | Type 1 illness period 2: osteoporosis | `Numeric(Byte)` | `%12.0g` |
| `hs055d4_2` | Type 1 illness period 2: angina or heart attack | `Numeric(Byte)` | `%12.0g` |
| `hs055d5_2` | Type 1 illness period 2: other heart disease | `Numeric(Byte)` | `%12.0g` |
| `hs055d6_2` | Type 1 illness period 2: diabetes or high blood sugar | `Numeric(Byte)` | `%12.0g` |
| `hs055d7_2` | Type 1 illness period 2: stroke | `Numeric(Byte)` | `%12.0g` |
| `hs055d8_2` | Type 1 illness period 2: asthma | `Numeric(Byte)` | `%12.0g` |
| `hs055d9_2` | Type 1 illness period 2: respiratory problems other than asthma | `Numeric(Byte)` | `%12.0g` |
| `hs055d10_2` | Type 1 illness period 2: tuberculosis | `Numeric(Byte)` | `%12.0g` |
| `hs055d11_2` | Type 1 illness period 2: severe headaches or migraines | `Numeric(Byte)` | `%12.0g` |
| `hs055dno_2` | Type 1 illness period 2: none of these | `Numeric(Byte)` | `%12.0g` |
| `hs055d1_3` | Type 1 illness period 3: back pain | `Numeric(Byte)` | `%12.0g` |
| `hs055d2_3` | Type 1 illness period 3: arthritis, including osteoarthritis and rheumatism | `Numeric(Byte)` | `%12.0g` |
| `hs055d3_3` | Type 1 illness period 3: osteoporosis | `Numeric(Byte)` | `%12.0g` |
| `hs055d4_3` | Type 1 illness period 3: angina or heart attack | `Numeric(Byte)` | `%12.0g` |
| `hs055d5_3` | Type 1 illness period 3: other heart disease | `Numeric(Byte)` | `%12.0g` |
| `hs055d6_3` | Type 1 illness period 3: diabetes or high blood sugar | `Numeric(Byte)` | `%12.0g` |
| `hs055d7_3` | Type 1 illness period 3: stroke | `Numeric(Byte)` | `%12.0g` |
| `hs055d8_3` | Type 1 illness period 3: asthma | `Numeric(Byte)` | `%12.0g` |
| `hs055d9_3` | Type 1 illness period 3: respiratory problems other than asthma | `Numeric(Byte)` | `%12.0g` |
| `hs055d10_3` | Type 1 illness period 3: tuberculosis | `Numeric(Byte)` | `%12.0g` |
| `hs055d11_3` | Type 1 illness period 3: severe headaches or migraines | `Numeric(Byte)` | `%12.0g` |
| `hs055dno_3` | Type 1 illness period 3: none of these | `Numeric(Byte)` | `%12.0g` |
| `hs056d1_1` | Type 2 illness period 1: leukaemia or lymphoma | `Numeric(Byte)` | `%12.0g` |
| `hs056d2_1` | Type 2 illness period 1: cancer or malignant tumour | `Numeric(Byte)` | `%12.0g` |
| `hs056d3_1` | Type 2 illness period 1: emotional, nervous, or psychiatric problem | `Numeric(Byte)` | `%12.0g` |
| `hs056d4_1` | Type 2 illness period 1: fatigue, e.g. with ME, MS | `Numeric(Byte)` | `%12.0g` |
| `hs056d5_1` | Type 2 illness period 1: gynaecological (women's) problem | `Numeric(Byte)` | `%12.0g` |
| `hs056d6_1` | Type 2 illness period 1: eyesight problems | `Numeric(Byte)` | `%12.0g` |
| `hs056d7_1` | Type 2 illness period 1: infectious disease (e.g. shingles, mumps, TB, HIV) | `Numeric(Byte)` | `%12.0g` |
| `hs056d8_1` | Type 2 illness period 1: allergies (other than asthma) | `Numeric(Byte)` | `%12.0g` |
| `hs056dno_1` | Type 2 illness period 1: none of these | `Numeric(Byte)` | `%12.0g` |
| `hs056dot_1` | Type 2 illness period 1: other | `Numeric(Byte)` | `%12.0g` |
| `hs056d1_2` | Type 2 illness period 2: leukaemia or lymphoma | `Numeric(Byte)` | `%12.0g` |
| `hs056d2_2` | Type 2 illness period 2: cancer or malignant tumour | `Numeric(Byte)` | `%12.0g` |
| `hs056d3_2` | Type 2 illness period 2: emotional, nervous, or psychiatric problem | `Numeric(Byte)` | `%12.0g` |
| `hs056d4_2` | Type 2 illness period 2: fatigue, e.g. with ME, MS | `Numeric(Byte)` | `%12.0g` |
| `hs056d5_2` | Type 2 illness period 2: gynaecological (women's) problem | `Numeric(Byte)` | `%12.0g` |
| `hs056d6_2` | Type 2 illness period 2: eyesight problems | `Numeric(Byte)` | `%12.0g` |
| `hs056d7_2` | Type 2 illness period 2: infectious disease (e.g. shingles, mumps, TB, HIV) | `Numeric(Byte)` | `%12.0g` |
| `hs056d8_2` | Type 2 illness period 2: allergies (other than asthma) | `Numeric(Byte)` | `%12.0g` |
| `hs056dno_2` | Type 2 illness period 2: none of these | `Numeric(Byte)` | `%12.0g` |
| `hs056dot_2` | Type 2 illness period 2: other | `Numeric(Byte)` | `%12.0g` |
| `hs056d1_3` | Type 2 illness period 3: leukaemia or lymphoma | `Numeric(Byte)` | `%12.0g` |
| `hs056d2_3` | Type 2 illness period 3: cancer or malignant tumour | `Numeric(Byte)` | `%12.0g` |
| `hs056d3_3` | Type 2 illness period 3: emotional, nervous, or psychiatric problem | `Numeric(Byte)` | `%12.0g` |
| `hs056d4_3` | Type 2 illness period 3: fatigue, e.g. with ME, MS | `Numeric(Byte)` | `%12.0g` |
| `hs056d5_3` | Type 2 illness period 3: gynaecological (women's) problem | `Numeric(Byte)` | `%12.0g` |
| `hs056d6_3` | Type 2 illness period 3: eyesight problems | `Numeric(Byte)` | `%12.0g` |
| `hs056d7_3` | Type 2 illness period 3: infectious disease (e.g. shingles, mumps, TB, HIV) | `Numeric(Byte)` | `%12.0g` |
| `hs056d8_3` | Type 2 illness period 3: allergies (other than asthma) | `Numeric(Byte)` | `%12.0g` |
| `hs056dno_3` | Type 2 illness period 3: none of these | `Numeric(Byte)` | `%12.0g` |
| `hs056dot_3` | Type 2 illness period 3: other | `Numeric(Byte)` | `%12.0g` |
| `hs062d1_1` | Experiences at work (illness period 1): denied promotions | `Numeric(Byte)` | `%12.0g` |
| `hs062d2_1` | Experiences at work (illness period 1): fewer responsibilities | `Numeric(Byte)` | `%12.0g` |
| `hs062d3_1` | Experiences at work (illness period 1): tasks below qualifications | `Numeric(Byte)` | `%12.0g` |
| `hs062d4_1` | Experiences at work (illness period 1): harassment by boss/colleagues | `Numeric(Byte)` | `%12.0g` |
| `hs062d5_1` | Experiences at work (illness period 1): pay cuts | `Numeric(Byte)` | `%12.0g` |
| `hs062dno_1` | Experiences at work (illness period 1): none of these | `Numeric(Byte)` | `%12.0g` |
| `hs062d1_2` | Experiences at work (illness period 2): denied promotions | `Numeric(Byte)` | `%12.0g` |
| `hs062d2_2` | Experiences at work (illness period 2): fewer responsibilities | `Numeric(Byte)` | `%12.0g` |
| `hs062d3_2` | Experiences at work (illness period 2): tasks below qualifications | `Numeric(Byte)` | `%12.0g` |
| `hs062d4_2` | Experiences at work (illness period 2): harassment by boss/colleagues | `Numeric(Byte)` | `%12.0g` |
| `hs062d5_2` | Experiences at work (illness period 2): pay cuts | `Numeric(Byte)` | `%12.0g` |
| `hs062dno_2` | Experiences at work (illness period 2): none of these | `Numeric(Byte)` | `%12.0g` |
| `hs062d1_3` | Experiences at work (illness period 3): denied promotions | `Numeric(Byte)` | `%12.0g` |
| `hs062d2_3` | Experiences at work (illness period 3): fewer responsibilities | `Numeric(Byte)` | `%12.0g` |
| `hs062d3_3` | Experiences at work (illness period 3): tasks below qualifications | `Numeric(Byte)` | `%12.0g` |
| `hs062d4_3` | Experiences at work (illness period 3): harassment by boss/colleagues | `Numeric(Byte)` | `%12.0g` |
| `hs062d5_3` | Experiences at work (illness period 3): pay cuts | `Numeric(Byte)` | `%12.0g` |
| `hs062dno_3` | Experiences at work (illness period 3): none of these | `Numeric(Byte)` | `%12.0g` |
| `hs063d1` | Consequences of illness period: limited opportunities for paid work | `Numeric(Byte)` | `%12.0g` |
| `hs063d2` | Consequences of illness period: negative effect on family life | `Numeric(Byte)` | `%12.0g` |
| `hs063d3` | Consequences of illness period: positive effect on family life | `Numeric(Byte)` | `%12.0g` |
| `hs063d4` | Consequences of illness period: made social life more difficult | `Numeric(Byte)` | `%12.0g` |
| `hs063d5` | Consequences of illness period: limited leisure activities | `Numeric(Byte)` | `%12.0g` |
| `hs063d6` | Consequences of illness period: made determined to get the best out of life | `Numeric(Byte)` | `%12.0g` |
| `hs063d7` | Consequences of illness period: opened up new opportunities | `Numeric(Byte)` | `%12.0g` |
| `hs063dno` | Consequences of illness period: none of these | `Numeric(Byte)` | `%12.0g` |
| `hs063dot` | Consequences of illness period: other | `Numeric(Byte)` | `%12.0g` |

### `ra` - Retrospective Accommodation

- Dataset: `sharew7_rel9-0-0_ra.dta`
- Read with: `ps.read_share_module("ra", wave=7)`
- Rows: 77,181
- Variables: 707
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ra003_` | When established home | `Numeric(Int)` | `%24.0g` |
| `ra004_` | When born lived in same residence more than 1 year | `Numeric(Byte)` | `%10.0g` |
| `ra006_1` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_1` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_1` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_1` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra709_1` | Typ of rental: social/public housing accomodation | `Numeric(Byte)` | `%10.0g` |
| `ra011_1` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_1` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_1` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_1` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_1` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_1` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_1` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_1` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_1` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_2` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_2` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_2` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_2` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_2` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra709_2` | Typ of rental: social/public housing accomodation | `Numeric(Byte)` | `%10.0g` |
| `ra011_2` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_2` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_2` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_2` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_2` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_2` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_2` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_2` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_2` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_3` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_3` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_3` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_3` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_3` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra709_3` | Typ of rental: social/public housing accomodation | `Numeric(Byte)` | `%10.0g` |
| `ra011_3` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_3` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_3` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_3` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_3` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_3` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_3` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_3` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_3` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_4` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_4` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_4` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_4` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_4` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra709_4` | Typ of rental: social/public housing accomodation | `Numeric(Byte)` | `%10.0g` |
| `ra011_4` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_4` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_4` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_4` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_4` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_4` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_4` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_4` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_4` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_5` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_5` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_5` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_5` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_5` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra709_5` | Typ of rental: social/public housing accomodation | `Numeric(Byte)` | `%10.0g` |
| `ra011_5` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_5` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_5` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_5` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_5` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_5` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_5` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_5` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_5` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_6` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_6` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_6` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_6` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_6` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra709_6` | Typ of rental: social/public housing accomodation | `Numeric(Byte)` | `%10.0g` |
| `ra011_6` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_6` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_6` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_6` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_6` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_6` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_6` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_6` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_6` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_7` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_7` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_7` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_7` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_7` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra709_7` | Typ of rental: social/public housing accomodation | `Numeric(Byte)` | `%10.0g` |
| `ra011_7` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_7` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_7` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_7` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_7` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_7` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_7` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_7` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_7` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_8` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_8` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_8` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_8` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_8` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra709_8` | Typ of rental: social/public housing accomodation | `Numeric(Byte)` | `%10.0g` |
| `ra011_8` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_8` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_8` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_8` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_8` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_8` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_8` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_8` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_8` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_9` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_9` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_9` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_9` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_9` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra709_9` | Typ of rental: social/public housing accomodation | `Numeric(Byte)` | `%10.0g` |
| `ra011_9` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_9` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_9` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_9` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_9` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_9` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_9` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_9` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_9` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_10` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_10` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_10` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_10` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_10` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra011_10` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_10` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_10` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_10` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_10` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_10` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_10` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_10` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_10` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_11` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_11` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_11` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_11` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_11` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra011_11` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_11` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_11` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_11` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_11` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_11` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_11` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_11` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_11` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_12` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_12` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_12` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_12` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_12` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra011_12` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_12` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_12` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_12` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_12` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_12` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_12` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_12` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_12` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_13` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_13` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_13` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_13` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_13` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra011_13` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_13` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_13` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_13` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_13` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_13` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_13` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_13` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra005_14` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_14` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_14` | Estimated start year of accommodation | `Numeric(Byte)` | `%10.0g` |
| `ra008_14` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_14` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra011_14` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_14` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_14` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_14` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_14` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_14` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_14` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_14` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_14` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_15` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_15` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_15` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_15` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_15` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra011_15` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_15` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_15` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_15` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_15` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_15` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_15` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra005_16` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_16` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_16` | Estimated start year of accommodation | `Numeric(Byte)` | `%10.0g` |
| `ra008_16` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_16` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra011_16` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_16` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_16` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_16` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_16` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_16` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra005_17` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_17` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_17` | Estimated start year of accommodation | `Numeric(Byte)` | `%10.0g` |
| `ra008_17` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_17` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra011_17` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_17` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_17` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_17` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_17` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_17` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_17` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra005_18` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_18` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_18` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `ra008_18` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_18` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra013_18` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_18` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_18` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_18` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_18` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_18` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_18` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_18` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_19` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_19` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_19` | Estimated start year of accommodation | `Numeric(Byte)` | `%10.0g` |
| `ra008_19` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_19` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra011_19` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_19` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_19` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_19` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_19` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_19` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_19` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra022b_19` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `ra022c_19` | When sell property | `Numeric(Int)` | `%10.0g` |
| `ra005_20` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_20` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_20` | Estimated start year of accommodation | `Numeric(Byte)` | `%10.0g` |
| `ra008_20` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_20` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra011_20` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_20` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_20` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_20` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_20` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_20` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra005_21` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_21` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_21` | Estimated start year of accommodation | `Numeric(Byte)` | `%10.0g` |
| `ra008_21` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_21` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra013_21` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_21` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_21` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_21` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_21` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra005_22` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_22` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_22` | Estimated start year of accommodation | `Numeric(Byte)` | `%10.0g` |
| `ra008_22` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_22` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra013_22` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_22` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_22` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_22` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_22` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra005_23` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_23` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra008_23` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_23` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra013_23` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_23` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_23` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_23` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_23` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_23` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra005_24` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_24` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra008_24` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_24` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra011_24` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `ra013_24` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_24` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_24` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_24` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra005_25` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_25` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra008_25` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_25` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra013_25` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_25` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_25` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_25` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra005_26` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_26` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra008_26` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_26` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra013_26` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_26` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_26` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_26` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra005_27` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_27` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra008_27` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_27` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra013_27` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_27` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_27` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_27` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra005_28` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_28` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra008_28` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_28` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra013_28` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_28` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_28` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_28` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra005_29` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_29` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `ra007_29` | Estimated start year of accommodation | `Numeric(Byte)` | `%10.0g` |
| `ra008_29` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_29` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra013_29` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_29` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_29` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_29` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra022_29` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `ra022a_29` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `ra005_30` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `ra006_30` | Start living at residence | `Numeric(Byte)` | `%10.0g` |
| `ra007_30` | Estimated start year of accommodation | `Numeric(Byte)` | `%10.0g` |
| `ra008_30` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `ra009_30` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `ra013_30` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `ra015_30` | Region of residence (not current) | `Numeric(Byte)` | `%28.0g` |
| `ra017_30` | Area of residence | `Numeric(Byte)` | `%43.0g` |
| `ra021_30` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `ra027_` | Proxy check | `Numeric(Byte)` | `%44.0g` |
| `ra733_1` | Start year living first time: Mother | `Numeric(Int)` | `%10.0g` |
| `ra734_1` | Stop year living first time: Mother | `Numeric(Int)` | `%26.0g` |
| `ra735_1` | Living again later: Mother | `Numeric(Byte)` | `%10.0g` |
| `ra736_1` | Start year living last time: Mother | `Numeric(Int)` | `%10.0g` |
| `ra737_1` | Stop year living last time: Mother | `Numeric(Int)` | `%26.0g` |
| `ra738_1` | First help coresident out or vice versa: Mother | `Numeric(Byte)` | `%33.0g` |
| `ra739_1` | Last help coresident out or vice versa: Mother | `Numeric(Byte)` | `%33.0g` |
| `ra740_1` | Current help coresident out or vice versa: Mother | `Numeric(Byte)` | `%33.0g` |
| `ra733_2` | Start year living first time: Father | `Numeric(Int)` | `%10.0g` |
| `ra734_2` | Stop year living first time: Father | `Numeric(Int)` | `%26.0g` |
| `ra735_2` | Living again later: Father | `Numeric(Byte)` | `%10.0g` |
| `ra736_2` | Start year living last time: Father | `Numeric(Int)` | `%10.0g` |
| `ra737_2` | Stop year living last time: Father | `Numeric(Int)` | `%26.0g` |
| `ra738_2` | First help coresident out or vice versa: Father | `Numeric(Byte)` | `%33.0g` |
| `ra739_2` | Last help coresident out or vice versa: Father | `Numeric(Byte)` | `%33.0g` |
| `ra740_2` | Current help coresident out or vice versa: Father | `Numeric(Byte)` | `%33.0g` |
| `ra733_3` | Start year living first time: Mother-in-law | `Numeric(Int)` | `%10.0g` |
| `ra734_3` | Stop year living first time: Mother-in-law | `Numeric(Int)` | `%26.0g` |
| `ra735_3` | Living again later: Mother-in-law | `Numeric(Byte)` | `%10.0g` |
| `ra736_3` | Start year living last time: Mother-in-law | `Numeric(Int)` | `%10.0g` |
| `ra737_3` | Stop year living last time: Mother-in-law | `Numeric(Int)` | `%26.0g` |
| `ra738_3` | First help coresident out or vice versa: Mother-in-law | `Numeric(Byte)` | `%33.0g` |
| `ra739_3` | Last help coresident out or vice versa: Mother-in-law | `Numeric(Byte)` | `%33.0g` |
| `ra740_3` | Current help coresident out or vice versa: Mother-in-law | `Numeric(Byte)` | `%33.0g` |
| `ra733_4` | Start year living first time: Father-in-law | `Numeric(Int)` | `%10.0g` |
| `ra734_4` | Stop year living first time: Father-in-law | `Numeric(Int)` | `%26.0g` |
| `ra735_4` | Living again later: Father-in-law | `Numeric(Byte)` | `%10.0g` |
| `ra736_4` | Start year living last time: Father-in-law | `Numeric(Int)` | `%10.0g` |
| `ra737_4` | Stop year living last time: Father-in-law | `Numeric(Int)` | `%26.0g` |
| `ra738_4` | First help coresident out or vice versa: Father-in-law | `Numeric(Byte)` | `%33.0g` |
| `ra739_4` | Last help coresident out or vice versa: Father-in-law | `Numeric(Byte)` | `%33.0g` |
| `ra740_4` | Current help coresident out or vice versa: Father-in-law | `Numeric(Byte)` | `%33.0g` |
| `ra742_1` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_1` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_2` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_2` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_3` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_3` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_4` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_4` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_5` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_5` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_6` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_6` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_7` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_7` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_8` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_8` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_9` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_9` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_10` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_10` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_11` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_11` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_12` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_12` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_13` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_13` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_15` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_15` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_21` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_21` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_22` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_22` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_23` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_23` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra742_24` | Help coresident child out or vice versa | `Numeric(Byte)` | `%33.0g` |
| `ra743_24` | When child left home | `Numeric(Int)` | `%27.0g` |
| `ra010c_1` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_2` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_3` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_4` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_5` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_6` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_7` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_8` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_9` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_10` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_11` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_12` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_13` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_14` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_15` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_16` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra010c_20` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `ra002d1` | Events in accomodation: lived in children's home | `Numeric(Byte)` | `%12.0g` |
| `ra002d2` | Events in accomodation: fostered with another family | `Numeric(Byte)` | `%12.0g` |
| `ra002d3` | Events in accomodation: evacuated/relocated during war | `Numeric(Byte)` | `%12.0g` |
| `ra002d4` | Events in accomodation: lived in prisoner of war camp | `Numeric(Byte)` | `%12.0g` |
| `ra002d5` | Events in accomodation: lived in prison | `Numeric(Byte)` | `%12.0g` |
| `ra002d6` | Events in accomodation: lived in labor camp | `Numeric(Byte)` | `%12.0g` |
| `ra002d7` | Events in accomodation: lived in concentration camp | `Numeric(Byte)` | `%12.0g` |
| `ra002d8` | Events in accomodation: inpatient in tb institution | `Numeric(Byte)` | `%12.0g` |
| `ra002d9` | Events in accomodation: stayed in psychiatric hospital | `Numeric(Byte)` | `%12.0g` |
| `ra002d10` | Events in accomodation: homeless for 1 month + | `Numeric(Byte)` | `%12.0g` |
| `ra002dno` | Events in accomodation: none of these | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_1` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_1` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_1` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_1` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_1` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_1` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_2` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_2` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_2` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_2` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_2` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_2` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_3` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_3` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_3` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_3` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_3` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_3` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_4` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_4` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_4` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_4` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_4` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_4` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_5` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_5` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_5` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_5` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_5` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_5` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_6` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_6` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_6` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_6` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_6` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_6` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_7` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_7` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_7` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_7` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_7` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_7` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_8` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_8` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_8` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_8` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_8` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_8` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_9` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_9` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_9` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_9` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_9` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_9` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_10` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_10` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_10` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_10` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_10` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_10` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_11` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_11` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_11` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_11` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_11` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_11` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_12` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_12` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_12` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_12` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_12` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_12` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_13` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_13` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_13` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_13` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_13` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_13` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_14` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_14` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_14` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_14` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_14` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_14` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_15` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_15` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_15` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_15` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_15` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_15` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_16` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_16` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_16` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_16` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_16` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_16` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_17` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_17` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_17` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_17` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_17` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_17` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_18` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_18` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_18` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_18` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_18` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_18` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_19` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_19` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_19` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_19` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_19` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_19` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_20` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_20` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_20` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_20` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_20` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_20` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_21` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_21` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_21` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_21` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_21` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_21` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_22` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_22` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_22` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_22` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_22` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_22` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_23` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_23` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_23` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_23` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_23` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_23` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_24` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_24` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_24` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_24` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_24` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_24` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_27` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_27` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_27` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_27` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_27` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_27` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_29` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_29` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_29` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_29` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_29` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_29` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra018d1_30` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `ra018d2_30` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `ra018d3_30` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `ra018d4_30` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `ra018d5_30` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `ra018d6_30` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `ra732d1` | Who lived in household: Mother | `Numeric(Byte)` | `%12.0g` |
| `ra732d2` | Who lived in household: Father | `Numeric(Byte)` | `%12.0g` |
| `ra732d3` | Who lived in household: Mother-in-law | `Numeric(Byte)` | `%12.0g` |
| `ra732d4` | Who lived in household: Father-in-law | `Numeric(Byte)` | `%12.0g` |
| `ra732dno` | Who lived in household: None of these | `Numeric(Byte)` | `%12.0g` |
| `ra741_1` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_2` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_3` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_4` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_5` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_6` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_7` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_8` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_9` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_10` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_11` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_12` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_13` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_15` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_21` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_22` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_23` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra741_24` | Start year living with child | `Numeric(Int)` | `%45.0g` |
| `ra014c_1` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_2` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_3` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_4` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_5` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_6` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_7` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_8` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_9` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_10` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_11` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_12` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_13` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_14` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_15` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_16` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_17` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_18` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_19` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra014c_20` | Country of residence (not current) - coded | `Numeric(Int)` | `%46.0g` |
| `ra015c_1` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_2` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_3` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_4` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_5` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_6` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_7` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_8` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_9` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_10` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_11` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_12` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_13` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_14` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_15` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_16` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_17` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_18` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_19` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_20` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_21` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_22` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_23` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_24` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_25` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_26` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_27` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_28` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_29` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `ra015c_30` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |

### `rc` - Retrospective Children History

- Dataset: `sharew7_rel9-0-0_rc.dta`
- Read with: `ps.read_share_module("rc", wave=7)`
- Rows: 77,181
- Variables: 400
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sl_childid_biological_1` | Child identifier (fix across modules and waves): Child 1 (SHARELIFE: biological) | `Str(14)` | `%14s` |
| `sl_childid_biological_2` | Child identifier (fix across modules and waves): Child 2 (SHARELIFE: biological) | `Str(14)` | `%14s` |
| `sl_childid_biological_3` | Child identifier (fix across modules and waves): Child 3 (SHARELIFE: biological) | `Str(14)` | `%14s` |
| `sl_childid_biological_4` | Child identifier (fix across modules and waves): Child 4 (SHARELIFE: biological) | `Str(14)` | `%14s` |
| `sl_childid_biological_5` | Child identifier (fix across modules and waves): Child 5 (SHARELIFE: biological) | `Str(14)` | `%14s` |
| `sl_childid_biological_6` | Child identifier (fix across modules and waves): Child 6 (SHARELIFE: biological) | `Str(14)` | `%14s` |
| `sl_childid_biological_7` | Child identifier (fix across modules and waves): Child 7 (SHARELIFE: biological) | `Str(14)` | `%14s` |
| `sl_childid_biological_8` | Child identifier (fix across modules and waves): Child 8 (SHARELIFE: biological) | `Str(14)` | `%14s` |
| `sl_childid_biological_9` | Child identifier (fix across modules and waves): Child 9 (SHARELIFE: biological) | `Str(14)` | `%14s` |
| `sl_childid_biological_10` | Child identifier (fix across modules and waves): Child 10 (SHARELIFE: biological | `Str(14)` | `%14s` |
| `sl_childid_biological_11` | Child identifier (fix across modules and waves): Child 11 (SHARELIFE: biological | `Str(14)` | `%14s` |
| `sl_childid_biological_12` | Child identifier (fix across modules and waves): Child 12 (SHARELIFE: biological | `Str(14)` | `%14s` |
| `sl_childid_biological_13` | Child identifier (fix across modules and waves): Child 13 (SHARELIFE: biological | `Str(14)` | `%14s` |
| `sl_childid_biological_14` | Child identifier (fix across modules and waves): Child 14 (SHARELIFE: biological | `Str(14)` | `%14s` |
| `sl_childid_biological_15` | Child identifier (fix across modules and waves): Child 15 (SHARELIFE: biological | `Str(14)` | `%14s` |
| `sl_childid_biological_16` | Child identifier (fix across modules and waves): Child 16 (SHARELIFE: biological | `Str(14)` | `%14s` |
| `sl_childid_adopted_1` | Child identifier (fix across modules and waves): Child 1 (SHARELIFE: adopted) | `Str(14)` | `%14s` |
| `sl_childid_adopted_2` | Child identifier (fix across modules and waves): Child 2 (SHARELIFE: adopted) | `Str(14)` | `%14s` |
| `sl_childid_adopted_3` | Child identifier (fix across modules and waves): Child 3 (SHARELIFE: adopted) | `Str(14)` | `%14s` |
| `sl_childid_adopted_4` | Child identifier (fix across modules and waves): Child 4 (SHARELIFE: adopted) | `Str(14)` | `%14s` |
| `sl_childid_adopted_5` | Child identifier (fix across modules and waves): Child 5 (SHARELIFE: adopted) | `Str(14)` | `%14s` |
| `sl_childid_adopted_6` | Child identifier (fix across modules and waves): Child 6 (SHARELIFE: adopted) | `Str(14)` | `%14s` |
| `sl_childid_adopted_7` | Child identifier (fix across modules and waves): Child 7 (SHARELIFE: adopted) | `Str(14)` | `%14s` |
| `sl_childid_adopted_8` | Child identifier (fix across modules and waves): Child 8 (SHARELIFE: adopted) | `Str(14)` | `%14s` |
| `rc022_` | Ever had other non_mentioned children | `Numeric(Byte)` | `%10.0g` |
| `rc023_` | Number of other children | `Numeric(Byte)` | `%10.0g` |
| `rc024_1` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_2` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_3` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_4` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_5` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_6` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_7` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_8` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_9` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_10` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_11` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_12` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_13` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_14` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_15` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc024_16` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `rc026_1` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_2` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_3` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_4` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_5` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_6` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_7` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_8` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_9` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_10` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_11` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_12` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_13` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_14` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_15` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc026_16` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `rc027_1` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_2` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_3` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_4` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_5` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_6` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_7` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_8` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_9` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_10` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_11` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_12` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_13` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_14` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_15` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc027_16` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc028_1` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `rc028_2` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `rc028_3` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `rc028_4` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `rc028_5` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `rc028_6` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `rc028_7` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `rc028_8` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `rc028_9` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `rc028_10` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `rc028_11` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `rc028_12` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `rc028_13` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `rc028_15` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `rc029_1` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_2` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_3` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_4` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_5` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_6` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_7` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_8` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_9` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_10` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_11` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_12` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_13` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_14` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_15` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc029_16` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc030_1` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_2` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_3` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_4` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_5` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_6` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_7` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_8` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_9` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_10` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_11` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_12` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_13` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_14` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_15` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030_16` | How long was maternity interruption | `Numeric(Byte)` | `%50.0g` |
| `rc030a_1` | When started working again | `Numeric(Int)` | `%10.0g` |
| `rc030a_2` | When started working again | `Numeric(Int)` | `%10.0g` |
| `rc030a_3` | When started working again | `Numeric(Int)` | `%10.0g` |
| `rc030a_4` | When started working again | `Numeric(Int)` | `%10.0g` |
| `rc030a_5` | When started working again | `Numeric(Int)` | `%10.0g` |
| `rc030a_6` | When started working again | `Numeric(Int)` | `%10.0g` |
| `rc030a_7` | When started working again | `Numeric(Int)` | `%10.0g` |
| `rc030a_8` | When started working again | `Numeric(Int)` | `%10.0g` |
| `rc030a_9` | When started working again | `Numeric(Int)` | `%10.0g` |
| `rc030a_10` | When started working again | `Numeric(Int)` | `%10.0g` |
| `rc031d1_1` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_1` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_1` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_1` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_1` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_1` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_1` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_2` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_2` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_2` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_2` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_2` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_2` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_2` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_3` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_3` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_3` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_3` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_3` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_3` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_3` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_4` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_4` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_4` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_4` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_4` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_4` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_4` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_5` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_5` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_5` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_5` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_5` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_5` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_5` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_6` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_6` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_6` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_6` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_6` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_6` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_6` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_7` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_7` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_7` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_7` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_7` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_7` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_7` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_8` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_8` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_8` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_8` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_8` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_8` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_8` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_9` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_9` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_9` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_9` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_9` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_9` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_9` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_10` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_10` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_10` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_10` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_10` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_10` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_10` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_11` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_11` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_11` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_11` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_11` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_11` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_11` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_12` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_12` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_12` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_12` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_12` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_12` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_12` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_13` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_13` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_13` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_13` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_13` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_13` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_13` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_14` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_14` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_14` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_14` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_14` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_14` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_14` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_15` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_15` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_15` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_15` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_15` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_15` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_15` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc031d1_16` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc031d2_16` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc031d3_16` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d4_16` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc031d5_16` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc031d6_16` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc031dot_16` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc032_1` | Maternity benefit amount | `Numeric(Long)` | `%12.0g` |
| `rc032_2` | Maternity benefit amount | `Numeric(Double)` | `%10.0g` |
| `rc032_3` | Maternity benefit amount | `Numeric(Long)` | `%12.0g` |
| `rc032_4` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `rc032_5` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `rc032_6` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `rc032_7` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `rc032_8` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `rc032_9` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `rc032_10` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `rc032_11` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `rc032_12` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `rc032_13` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `rc033_1` | Currency maternity benefit | `Numeric(Byte)` | `%30.0g` |
| `rc033_2` | Currency maternity benefit | `Numeric(Byte)` | `%30.0g` |
| `rc033_3` | Currency maternity benefit | `Numeric(Byte)` | `%30.0g` |
| `rc033_4` | Currency maternity benefit | `Numeric(Byte)` | `%30.0g` |
| `rc033_5` | Currency maternity benefit | `Numeric(Byte)` | `%30.0g` |
| `rc033_6` | Currency maternity benefit | `Numeric(Byte)` | `%30.0g` |
| `rc033_7` | Currency maternity benefit | `Numeric(Byte)` | `%30.0g` |
| `rc033_8` | Currency maternity benefit | `Numeric(Byte)` | `%30.0g` |
| `rc033_9` | Currency maternity benefit | `Numeric(Byte)` | `%30.0g` |
| `rc033_10` | Currency maternity benefit | `Numeric(Byte)` | `%30.0g` |
| `rc033_11` | Currency maternity benefit | `Numeric(Byte)` | `%30.0g` |
| `rc033c_1` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `rc033c_2` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `rc033c_3` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `rc033c_4` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `rc033c_5` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `rc033c_6` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `rc033c_7` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `rc033c_8` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `rc033c_9` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `rc033c_10` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `rc033c_11` | Currency maternity benefit - coded | `Numeric(Byte)` | `%63.0g` |
| `rc038_` | Other adopted children | `Numeric(Byte)` | `%10.0g` |
| `rc039_` | Number of other adopted children | `Numeric(Byte)` | `%10.0g` |
| `rc041_1` | Other child year of adoption | `Numeric(Int)` | `%10.0g` |
| `rc041_2` | Other child year of adoption | `Numeric(Int)` | `%10.0g` |
| `rc041_3` | Other child year of adoption | `Numeric(Int)` | `%10.0g` |
| `rc041_4` | Other child year of adoption | `Numeric(Int)` | `%10.0g` |
| `rc041_5` | Other child year of adoption | `Numeric(Int)` | `%10.0g` |
| `rc041_6` | Other child year of adoption | `Numeric(Int)` | `%10.0g` |
| `rc041_7` | Other child year of adoption | `Numeric(Int)` | `%10.0g` |
| `rc041_8` | Other child year of adoption | `Numeric(Byte)` | `%10.0g` |
| `rc042_1` | Other adopted child gender | `Numeric(Byte)` | `%10.0g` |
| `rc042_2` | Other adopted child gender | `Numeric(Byte)` | `%10.0g` |
| `rc042_3` | Other adopted child gender | `Numeric(Byte)` | `%10.0g` |
| `rc042_4` | Other adopted child gender | `Numeric(Byte)` | `%10.0g` |
| `rc042_5` | Other adopted child gender | `Numeric(Byte)` | `%10.0g` |
| `rc042_6` | Other adopted child gender | `Numeric(Byte)` | `%10.0g` |
| `rc042_7` | Other adopted child gender | `Numeric(Byte)` | `%10.0g` |
| `rc042_8` | Other adopted child gender | `Numeric(Byte)` | `%10.0g` |
| `rc043_1` | Other adopted child year of birth | `Numeric(Int)` | `%10.0g` |
| `rc043_2` | Other adopted child year of birth | `Numeric(Int)` | `%10.0g` |
| `rc043_3` | Other adopted child year of birth | `Numeric(Int)` | `%10.0g` |
| `rc043_4` | Other adopted child year of birth | `Numeric(Int)` | `%10.0g` |
| `rc043_5` | Other adopted child year of birth | `Numeric(Int)` | `%10.0g` |
| `rc043_6` | Other adopted child year of birth | `Numeric(Int)` | `%10.0g` |
| `rc043_7` | Other adopted child year of birth | `Numeric(Int)` | `%10.0g` |
| `rc043_8` | Other adopted child year of birth | `Numeric(Byte)` | `%10.0g` |
| `rc044_1` | Other adopted child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc044_2` | Other adopted child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc044_3` | Other adopted child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc044_4` | Other adopted child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc044_5` | Other adopted child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc044_6` | Other adopted child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc044_7` | Other adopted child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc044_8` | Other adopted child still alive | `Numeric(Byte)` | `%10.0g` |
| `rc045_1` | Other adopted child year of death | `Numeric(Int)` | `%10.0g` |
| `rc045_2` | Other adopted child year of death | `Numeric(Int)` | `%10.0g` |
| `rc045_3` | Other adopted child year of death | `Numeric(Int)` | `%10.0g` |
| `rc045_4` | Other adopted child year of death | `Numeric(Int)` | `%10.0g` |
| `rc045_5` | Other adopted child year of death | `Numeric(Int)` | `%10.0g` |
| `rc046_1` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc046_2` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc046_3` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc046_4` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc046_5` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc046_6` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc046_7` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc046_8` | Left job because of child | `Numeric(Byte)` | `%50.0g` |
| `rc047_1` | How long was maternity interuption | `Numeric(Byte)` | `%50.0g` |
| `rc047_2` | How long was maternity interuption | `Numeric(Byte)` | `%50.0g` |
| `rc047_3` | How long was maternity interuption | `Numeric(Byte)` | `%50.0g` |
| `rc047a_1` | When started working again | `Numeric(Int)` | `%10.0g` |
| `rc047a_2` | When started working again | `Numeric(Int)` | `%10.0g` |
| `rc047a_3` | When started working again | `Numeric(Int)` | `%10.0g` |
| `rc048d1_1` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc048d2_1` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc048d3_1` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d4_1` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d5_1` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc048d6_1` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc048dot_1` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc048d1_2` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc048d2_2` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc048d3_2` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d4_2` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d5_2` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc048d6_2` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc048dot_2` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc048d1_3` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc048d2_3` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc048d3_3` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d4_3` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d5_3` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc048d6_3` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc048dot_3` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc048d1_4` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc048d2_4` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc048d3_4` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d4_4` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d5_4` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc048d6_4` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc048dot_4` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc048d1_5` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc048d2_5` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc048d3_5` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d4_5` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d5_5` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc048d6_5` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc048dot_5` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc048d1_6` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc048d2_6` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc048d3_6` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d4_6` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d5_6` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc048d6_6` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc048dot_6` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc048d1_7` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc048d2_7` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc048d3_7` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d4_7` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d5_7` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc048d6_7` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc048dot_7` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc048d1_8` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `rc048d2_8` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `rc048d3_8` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d4_8` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `rc048d5_8` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `rc048d6_8` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `rc048dot_8` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `rc049_1` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `rc049_2` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `rc049_3` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `rc050_1` | Currency maternity benefit | `Numeric(Byte)` | `%30.0g` |
| `rc050_2` | Currency maternity benefit | `Numeric(Byte)` | `%30.0g` |
| `rc050c_1` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `rc050c_2` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `rc061_` | Proxy check | `Numeric(Byte)` | `%44.0g` |

### `re` - Retrospective Employment

- Dataset: `sharew7_rel9-0-0_re.dta`
- Read with: `ps.read_share_module("re", wave=7)`
- Rows: 77,181
- Variables: 567
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `re002_` | Year finished fulltime education | `Numeric(Int)` | `%20.0g` |
| `re003_` | Situation at age 15 if no education | `Numeric(Byte)` | `%81.0g` |
| `re005_` | Ever done paid work | `Numeric(Byte)` | `%10.0g` |
| `re006_` | Start first paid job | `Numeric(Byte)` | `%83.0g` |
| `re007_` | Situation in gap after education | `Numeric(Byte)` | `%81.0g` |
| `re008_1` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `re009_1` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `re010_1` | Situation changed to | `Numeric(Byte)` | `%81.0g` |
| `re008_2` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `re009_2` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `re010_2` | Situation changed to | `Numeric(Byte)` | `%81.0g` |
| `re008_3` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `re009_3` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `re010_3` | Situation changed to | `Numeric(Byte)` | `%81.0g` |
| `re008_4` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `re009_4` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `re010_4` | Situation changed to | `Numeric(Byte)` | `%81.0g` |
| `re008_5` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `re009_5` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `re010_5` | Situation changed to | `Numeric(Byte)` | `%81.0g` |
| `re008_6` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `re009_6` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `re010_6` | Situation changed to | `Numeric(Byte)` | `%81.0g` |
| `re008_7` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `re009_7` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `re010_7` | Situation changed to | `Numeric(Byte)` | `%81.0g` |
| `re008_8` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `re009_8` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `re010_8` | Situation changed to | `Numeric(Byte)` | `%81.0g` |
| `re008_9` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `re009_9` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `re010_9` | Situation changed to | `Numeric(Byte)` | `%81.0g` |
| `re008_10` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `re009_10` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `re010_10` | Situation changed to | `Numeric(Byte)` | `%81.0g` |
| `re008_11` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `re011_1` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_1` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_1` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_1` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_1` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_1` | First monthly wage in job | `Numeric(Long)` | `%12.0g` |
| `re022_1` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_1` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re023_1` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `re024_1` | Currency of work income | `Numeric(Byte)` | `%30.0g` |
| `re024c_1` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `re025d1_1` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_1` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_1` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_1` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_1` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_1` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `re028_1` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_1` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `re029_1` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `re030_1` | Currency of current work income | `Numeric(Byte)` | `%30.0g` |
| `re030c_1` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `re031_1` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_1` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_1` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_2` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_2` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_2` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_2` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_2` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_2` | First monthly wage in job | `Numeric(Long)` | `%12.0g` |
| `re022_2` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_2` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re023_2` | First monthly work income in self-employment | `Numeric(Long)` | `%12.0g` |
| `re024_2` | Currency of work income | `Numeric(Byte)` | `%30.0g` |
| `re024c_2` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `re025d1_2` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_2` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_2` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_2` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_2` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_2` | Current wage if still employed | `Numeric(Long)` | `%12.0g` |
| `re028_2` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_2` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `re029_2` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `re030_2` | Currency of current work income | `Numeric(Byte)` | `%30.0g` |
| `re030c_2` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `re031_2` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_2` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_2` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_3` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_3` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_3` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_3` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_3` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_3` | First monthly wage in job | `Numeric(Long)` | `%12.0g` |
| `re022_3` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_3` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re023_3` | First monthly work income in self-employment | `Numeric(Long)` | `%12.0g` |
| `re024_3` | Currency of work income | `Numeric(Byte)` | `%30.0g` |
| `re024c_3` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `re025d1_3` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_3` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_3` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_3` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_3` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_3` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `re028_3` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_3` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `re029_3` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `re030_3` | Currency of current work income | `Numeric(Byte)` | `%30.0g` |
| `re030c_3` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `re031_3` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_3` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_3` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_4` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_4` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_4` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_4` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_4` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_4` | First monthly wage in job | `Numeric(Long)` | `%12.0g` |
| `re022_4` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_4` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re023_4` | First monthly work income in self-employment | `Numeric(Long)` | `%12.0g` |
| `re024_4` | Currency of work income | `Numeric(Byte)` | `%30.0g` |
| `re024c_4` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `re025d1_4` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_4` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_4` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_4` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_4` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_4` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `re028_4` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_4` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `re029_4` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `re030_4` | Currency of current work income | `Numeric(Byte)` | `%30.0g` |
| `re030c_4` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `re031_4` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_4` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_4` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_5` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_5` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_5` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_5` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_5` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_5` | First monthly wage in job | `Numeric(Long)` | `%12.0g` |
| `re022_5` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_5` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re023_5` | First monthly work income in self-employment | `Numeric(Long)` | `%12.0g` |
| `re024_5` | Currency of work income | `Numeric(Byte)` | `%30.0g` |
| `re024c_5` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `re025d1_5` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_5` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_5` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_5` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_5` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_5` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `re028_5` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_5` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `re029_5` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `re030_5` | Currency of current work income | `Numeric(Byte)` | `%30.0g` |
| `re030c_5` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `re031_5` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_5` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_5` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_6` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_6` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_6` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_6` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_6` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_6` | First monthly wage in job | `Numeric(Long)` | `%12.0g` |
| `re022_6` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_6` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re023_6` | First monthly work income in self-employment | `Numeric(Double)` | `%10.0g` |
| `re024_6` | Currency of work income | `Numeric(Byte)` | `%30.0g` |
| `re024c_6` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `re025d1_6` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_6` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_6` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_6` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_6` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_6` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `re028_6` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_6` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `re029_6` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `re030_6` | Currency of current work income | `Numeric(Byte)` | `%30.0g` |
| `re030c_6` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `re031_6` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_6` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_6` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_7` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_7` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_7` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_7` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_7` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_7` | First monthly wage in job | `Numeric(Long)` | `%12.0g` |
| `re022_7` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_7` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re023_7` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `re024_7` | Currency of work income | `Numeric(Byte)` | `%30.0g` |
| `re024c_7` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `re025d1_7` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_7` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_7` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_7` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_7` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_7` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `re028_7` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_7` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `re029_7` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `re030_7` | Currency of current work income | `Numeric(Byte)` | `%30.0g` |
| `re030c_7` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `re031_7` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_7` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_7` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_8` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_8` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_8` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_8` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_8` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_8` | First monthly wage in job | `Numeric(Long)` | `%12.0g` |
| `re022_8` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_8` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re023_8` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `re024_8` | Currency of work income | `Numeric(Byte)` | `%30.0g` |
| `re024c_8` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `re025d1_8` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_8` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_8` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_8` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_8` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_8` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `re028_8` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_8` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `re029_8` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `re030_8` | Currency of current work income | `Numeric(Byte)` | `%30.0g` |
| `re030c_8` | Currency of current work income - coded | `Numeric(Byte)` | `%63.0g` |
| `re031_8` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_8` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_8` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_9` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_9` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_9` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_9` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_9` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_9` | First monthly wage in job | `Numeric(Long)` | `%12.0g` |
| `re022_9` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_9` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re023_9` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `re024_9` | Currency of work income | `Numeric(Byte)` | `%30.0g` |
| `re024c_9` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `re025d1_9` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_9` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_9` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_9` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_9` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_9` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `re028_9` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_9` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `re029_9` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `re030_9` | Currency of current work income | `Numeric(Byte)` | `%30.0g` |
| `re030c_9` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `re031_9` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_9` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_9` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_10` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_10` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_10` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_10` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_10` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_10` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `re022_10` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_10` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re023_10` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `re024_10` | Currency of work income | `Numeric(Byte)` | `%30.0g` |
| `re024c_10` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `re025d1_10` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_10` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_10` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_10` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_10` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_10` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `re028_10` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_10` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `re029_10` | Current work income if still self-employed | `Numeric(Int)` | `%10.0g` |
| `re030_10` | Currency of current work income | `Numeric(Byte)` | `%30.0g` |
| `re030c_10` | Currency of current work income - coded | `Numeric(Byte)` | `%63.0g` |
| `re031_10` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_10` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_10` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_11` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_11` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_11` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_11` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_11` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_11` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `re022_11` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_11` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re023_11` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `re024_11` | Currency of work income | `Numeric(Byte)` | `%30.0g` |
| `re024c_11` | Currency of work income - coded | `Numeric(Byte)` | `%63.0g` |
| `re025d1_11` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_11` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_11` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_11` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_11` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_11` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `re028_11` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_11` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `re029_11` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `re030_11` | Currency of current work income | `Numeric(Byte)` | `%30.0g` |
| `re030c_11` | Currency of current work income - coded | `Numeric(Byte)` | `%63.0g` |
| `re031_11` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_11` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_11` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_12` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_12` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_12` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_12` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_12` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_12` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `re022_12` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_12` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re023_12` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `re025d1_12` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_12` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_12` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_12` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_12` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_12` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `re028_12` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_12` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `re031_12` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_12` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_12` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_13` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_13` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_13` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_13` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_13` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_13` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `re022_13` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_13` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re023_13` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `re024_13` | Currency of work income | `Numeric(Byte)` | `%30.0g` |
| `re024c_13` | Currency of work income - coded | `Numeric(Byte)` | `%63.0g` |
| `re025d1_13` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_13` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_13` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_13` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_13` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_13` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `re028_13` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_13` | Currency of current wage - coded | `Numeric(Byte)` | `%63.0g` |
| `re031_13` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_13` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_13` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_14` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_14` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_14` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_14` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_14` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_14` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `re022_14` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_14` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re023_14` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `re024_14` | Currency of work income | `Numeric(Byte)` | `%30.0g` |
| `re024c_14` | Currency of work income - coded | `Numeric(Byte)` | `%63.0g` |
| `re025d1_14` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_14` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_14` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_14` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_14` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_14` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `re028_14` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_14` | Currency of current wage - coded | `Numeric(Byte)` | `%63.0g` |
| `re029_14` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `re030_14` | Currency of current work income | `Numeric(Byte)` | `%30.0g` |
| `re030c_14` | Currency of current work income - coded | `Numeric(Byte)` | `%63.0g` |
| `re031_14` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_14` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_14` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_15` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_15` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_15` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_15` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_15` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_15` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `re022_15` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_15` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re025d1_15` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_15` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_15` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_15` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_15` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_15` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `re028_15` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_15` | Currency of current wage - coded | `Numeric(Byte)` | `%63.0g` |
| `re031_15` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_15` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_15` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_16` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_16` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_16` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_16` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_16` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_16` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `re022_16` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_16` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `re025d1_16` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_16` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_16` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_16` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_16` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_16` | Current wage if still employed | `Numeric(Int)` | `%10.0g` |
| `re028_16` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_16` | Currency of current wage - coded | `Numeric(Byte)` | `%63.0g` |
| `re031_16` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_16` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_16` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_17` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_17` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_17` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_17` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_17` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_17` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `re022_17` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_17` | Currency of wage - coded | `Numeric(Byte)` | `%63.0g` |
| `re025d1_17` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_17` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_17` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_17` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_17` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re031_17` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_17` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re011_18` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_18` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_18` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_18` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_18` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_18` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `re022_18` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_18` | Currency of wage - coded | `Numeric(Byte)` | `%63.0g` |
| `re025d1_18` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_18` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_18` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_18` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_18` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re027_18` | Current wage if still employed | `Numeric(Int)` | `%10.0g` |
| `re028_18` | Currency of current wage | `Numeric(Byte)` | `%30.0g` |
| `re028c_18` | Currency of current wage - coded | `Numeric(Byte)` | `%63.0g` |
| `re031_18` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_18` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_18` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re011_19` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_19` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_19` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_19` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_19` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_19` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `re022_19` | Currency of wage | `Numeric(Byte)` | `%30.0g` |
| `re022c_19` | Currency of wage - coded | `Numeric(Byte)` | `%63.0g` |
| `re025d1_19` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_19` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_19` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_19` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_19` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re031_19` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_19` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re011_20` | Year started job | `Numeric(Int)` | `%10.0g` |
| `re012isco_20` | ISCO-08 code: Title of job | `Numeric(Int)` | `%13.0g` |
| `re014_20` | Job industry | `Numeric(Byte)` | `%117.0g` |
| `re015_20` | Was employee civil servant or self | `Numeric(Byte)` | `%60.0g` |
| `re016_20` | Job was part or full time | `Numeric(Byte)` | `%42.0g` |
| `re021_20` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `re025d1_20` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d2_20` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `re025d3_20` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `re025d4_20` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `re026_20` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `re031_20` | Reasons left job | `Numeric(Byte)` | `%55.0g` |
| `re032_20` | Gap after leaving this job | `Numeric(Byte)` | `%118.0g` |
| `re033_20` | Done in gap after leaving this job | `Numeric(Byte)` | `%81.0g` |
| `re035_1` | Situation in after last job | `Numeric(Byte)` | `%81.0g` |
| `re035a_1` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `re036_1` | Pension benefit when retired | `Numeric(Long)` | `%12.0g` |
| `re037_1` | Currency of pension benefit | `Numeric(Byte)` | `%30.0g` |
| `re037c_1` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `re038_1` | Paid job after retirement | `Numeric(Byte)` | `%10.0g` |
| `re039_1` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `re039a_1` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `re035_2` | Situation in after last job | `Numeric(Byte)` | `%81.0g` |
| `re035a_2` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `re036_2` | Pension benefit when retired | `Numeric(Long)` | `%10.0g` |
| `re037_2` | Currency of pension benefit | `Numeric(Byte)` | `%30.0g` |
| `re037c_2` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `re039_2` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `re039a_2` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `re035_3` | Situation in after last job | `Numeric(Byte)` | `%81.0g` |
| `re035a_3` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `re036_3` | Pension benefit when retired | `Numeric(Long)` | `%10.0g` |
| `re037_3` | Currency of pension benefit | `Numeric(Byte)` | `%30.0g` |
| `re037c_3` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `re039_3` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `re039a_3` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `re035_4` | Situation in after last job | `Numeric(Byte)` | `%81.0g` |
| `re035a_4` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `re036_4` | Pension benefit when retired | `Numeric(Long)` | `%10.0g` |
| `re037_4` | Currency of pension benefit | `Numeric(Byte)` | `%30.0g` |
| `re037c_4` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `re039_4` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `re039a_4` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `re035_5` | Situation in after last job | `Numeric(Byte)` | `%81.0g` |
| `re035a_5` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `re036_5` | Pension benefit when retired | `Numeric(Long)` | `%10.0g` |
| `re037_5` | Currency of pension benefit | `Numeric(Byte)` | `%30.0g` |
| `re037c_5` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `re039_5` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `re039a_5` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `re035_6` | Situation in after last job | `Numeric(Byte)` | `%81.0g` |
| `re035a_6` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `re036_6` | Pension benefit when retired | `Numeric(Long)` | `%10.0g` |
| `re037_6` | Currency of pension benefit | `Numeric(Byte)` | `%30.0g` |
| `re037c_6` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `re039_6` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `re039a_6` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `re035_7` | Situation in after last job | `Numeric(Byte)` | `%81.0g` |
| `re035a_7` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `re036_7` | Pension benefit when retired | `Numeric(Long)` | `%10.0g` |
| `re037_7` | Currency of pension benefit | `Numeric(Byte)` | `%30.0g` |
| `re037c_7` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `re039_7` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `re039a_7` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `re035_8` | Situation in after last job | `Numeric(Byte)` | `%81.0g` |
| `re035a_8` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `re036_8` | Pension benefit when retired | `Numeric(Long)` | `%10.0g` |
| `re037_8` | Currency of pension benefit | `Numeric(Byte)` | `%30.0g` |
| `re037c_8` | Currency of pension benefit - coded | `Numeric(Byte)` | `%63.0g` |
| `re039_8` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `re039a_8` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `re035_9` | Situation in after last job | `Numeric(Byte)` | `%81.0g` |
| `re035a_9` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `re036_9` | Pension benefit when retired | `Numeric(Int)` | `%10.0g` |
| `re037_9` | Currency of pension benefit | `Numeric(Byte)` | `%30.0g` |
| `re037c_9` | Currency of pension benefit - coded | `Numeric(Byte)` | `%63.0g` |
| `re039_9` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `re039a_9` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `re035_10` | Situation in after last job | `Numeric(Byte)` | `%81.0g` |
| `re035a_10` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `re036_10` | Pension benefit when retired | `Numeric(Long)` | `%10.0g` |
| `re037_10` | Currency of pension benefit | `Numeric(Byte)` | `%30.0g` |
| `re037c_10` | Currency of pension benefit - coded | `Numeric(Byte)` | `%63.0g` |
| `re039_10` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `re039a_10` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `re040_` | Which was main job in career | `Numeric(Byte)` | `%14.0g` |
| `re041_` | Wage at end of main job | `Numeric(Long)` | `%12.0g` |
| `re042_` | Currency of wage at end of main job | `Numeric(Byte)` | `%30.0g` |
| `re042c` | Currency of wage at end of main job - coded | `Numeric(Int)` | `%63.0g` |
| `re043_` | Work income at end of main job | `Numeric(Long)` | `%12.0g` |
| `re044_` | Currency of work income at end of main job | `Numeric(Byte)` | `%30.0g` |
| `re044c` | Currency of work income at end of main job - coded | `Numeric(Int)` | `%63.0g` |
| `re048_` | Proxy check | `Numeric(Byte)` | `%44.0g` |
| `re701_` | Ever used computer at work | `Numeric(Byte)` | `%10.0g` |
| `re702_` | First time computer at work | `Numeric(Int)` | `%10.0g` |
| `re704_` | Computer training for job | `Numeric(Byte)` | `%10.0g` |

### `rh` - Retrospective Health Care

- Dataset: `sharew7_rel9-0-0_rh.dta`
- Read with: `ps.read_share_module("rh", wave=7)`
- Rows: 77,181
- Variables: 106
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `rh002_` | Vaccinations during childhood | `Numeric(Byte)` | `%10.0g` |
| `rh015_` | Ever regular dentist | `Numeric(Byte)` | `%10.0g` |
| `rh016_` | Childhood regular dentist | `Numeric(Byte)` | `%10.0g` |
| `rh017_` | Year regular dentist visits started | `Numeric(Int)` | `%10.0g` |
| `rh018_` | Continuity regular dentist | `Numeric(Byte)` | `%10.0g` |
| `rh025_` | Frequency regular dentist | `Numeric(Byte)` | `%49.0g` |
| `rh040_` | Regular blood pressure checks | `Numeric(Byte)` | `%10.0g` |
| `rh041_` | Year regular blood pressure checks started | `Numeric(Int)` | `%10.0g` |
| `rh049_` | Frequency regular blood pressure | `Numeric(Byte)` | `%49.0g` |
| `rh042_` | Continuity regular blood pressure | `Numeric(Byte)` | `%10.0g` |
| `rh780_` | Needed doctor but could not afford it | `Numeric(Byte)` | `%10.0g` |
| `rh781_` | Number of periods could not afford doctor | `Numeric(Int)` | `%10.0g` |
| `rh784_` | Needed doctor but waited too long for appointment | `Numeric(Byte)` | `%10.0g` |
| `rh785_` | Number of periods wait for appointment | `Numeric(Int)` | `%10.0g` |
| `rh788_` | Postponed dentist visit | `Numeric(Byte)` | `%10.0g` |
| `rh789_` | Number of periods postponed dentist visit | `Numeric(Int)` | `%10.0g` |
| `rh792_` | Postponed taking medication because of cost | `Numeric(Byte)` | `%10.0g` |
| `rh793_` | Number of periods postponed taking medication | `Numeric(Int)` | `%10.0g` |
| `rh098_` | Proxy check | `Numeric(Byte)` | `%44.0g` |
| `rh782_1` | Years could not afford doctor 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh782_2` | Years could not afford doctor 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh782_3` | Years could not afford doctor 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh782_4` | Years could not afford doctor 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh782_5` | Years could not afford doctor 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh783_1` | Years could not afford doctor over 5 | `Numeric(Int)` | `%10.0g` |
| `rh783_2` | Years could not afford doctor over 5 | `Numeric(Int)` | `%10.0g` |
| `rh783_3` | Years could not afford doctor over 5 | `Numeric(Int)` | `%10.0g` |
| `rh783_4` | Years could not afford doctor over 5 | `Numeric(Int)` | `%10.0g` |
| `rh783_5` | Years could not afford doctor over 5 | `Numeric(Int)` | `%10.0g` |
| `rh786_1` | Years wait for appointment 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh786_2` | Years wait for appointment 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh786_3` | Years wait for appointment 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh786_4` | Years wait for appointment 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh786_5` | Years wait for appointment 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh787_1` | Years wait for appointment over 5 | `Numeric(Int)` | `%10.0g` |
| `rh787_2` | Years wait for appointment over 5 | `Numeric(Int)` | `%10.0g` |
| `rh787_3` | Years wait for appointment over 5 | `Numeric(Int)` | `%10.0g` |
| `rh787_4` | Years wait for appointment over 5 | `Numeric(Int)` | `%10.0g` |
| `rh787_5` | Years wait for appointment over 5 | `Numeric(Int)` | `%10.0g` |
| `rh790_1` | Years postponed dentist visit 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh790_2` | Years postponed dentist visit 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh790_3` | Years postponed dentist visit 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh790_4` | Years postponed dentist visit 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh790_5` | Years postponed dentist visit 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh791_1` | Years postponed dentist visit over 5 | `Numeric(Int)` | `%10.0g` |
| `rh791_2` | Years postponed dentist visit over 5 | `Numeric(Int)` | `%10.0g` |
| `rh791_3` | Years postponed dentist visit over 5 | `Numeric(Int)` | `%10.0g` |
| `rh791_4` | Years postponed dentist visit over 5 | `Numeric(Int)` | `%10.0g` |
| `rh791_5` | Years postponed dentist visit over 5 | `Numeric(Int)` | `%10.0g` |
| `rh794_1` | Years postponed taking medication 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh794_2` | Years postponed taking medication 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh794_3` | Years postponed taking medication 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh794_4` | Years postponed taking medication 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh794_5` | Years postponed taking medication 1 to 5 | `Numeric(Int)` | `%10.0g` |
| `rh795_1` | Years postponed taking medication over 5 | `Numeric(Int)` | `%10.0g` |
| `rh795_2` | Years postponed taking medication over 5 | `Numeric(Int)` | `%10.0g` |
| `rh795_3` | Years postponed taking medication over 5 | `Numeric(Int)` | `%10.0g` |
| `rh795_4` | Years postponed taking medication over 5 | `Numeric(Int)` | `%10.0g` |
| `rh795_5` | Years postponed taking medication over 5 | `Numeric(Int)` | `%10.0g` |
| `rh003d1` | Why no childhood vaccinations: not affordable | `Numeric(Byte)` | `%12.0g` |
| `rh003d2` | Why no childhood vaccinations: not covered by health insurance | `Numeric(Byte)` | `%12.0g` |
| `rh003d3` | Why no childhood vaccinations: did not have health insurance | `Numeric(Byte)` | `%12.0g` |
| `rh003d4` | Why no childhood vaccinations: time constraints | `Numeric(Byte)` | `%12.0g` |
| `rh003d5` | Why no childhood vaccinations: not enough information about it | `Numeric(Byte)` | `%12.0g` |
| `rh003d6` | Why no childhood vaccinations: not usual to get it | `Numeric(Byte)` | `%12.0g` |
| `rh003d7` | Why no childhood vaccinations: no place to receive it close to home | `Numeric(Byte)` | `%12.0g` |
| `rh003d8` | Why no childhood vaccinations: not considered to be necessary | `Numeric(Byte)` | `%12.0g` |
| `rh003dot` | Why no childhood vaccinations: other reasons | `Numeric(Byte)` | `%12.0g` |
| `rh018ad1` | No dental care: when between 0-15 years old | `Numeric(Byte)` | `%12.0g` |
| `rh018ad2` | No dental care: when between 16-25 years old | `Numeric(Byte)` | `%12.0g` |
| `rh018ad3` | No dental care: when between 26-40 years old | `Numeric(Byte)` | `%12.0g` |
| `rh018ad4` | No dental care: when between 41-55 years old | `Numeric(Byte)` | `%12.0g` |
| `rh018ad5` | No dental care: when between 56-65 years old | `Numeric(Byte)` | `%12.0g` |
| `rh018ad6` | No dental care: when between 66-75 years old | `Numeric(Byte)` | `%12.0g` |
| `rh018ad7` | No dental care: when older than 75 years | `Numeric(Byte)` | `%12.0g` |
| `rh026d1` | Why no regular dental care: not affordable | `Numeric(Byte)` | `%12.0g` |
| `rh026d2` | Why no regular dental care: not covered by health insurance | `Numeric(Byte)` | `%12.0g` |
| `rh026d3` | Why no regular dental care: did not have health insurance | `Numeric(Byte)` | `%12.0g` |
| `rh026d4` | Why no regular dental care: time constraints | `Numeric(Byte)` | `%12.0g` |
| `rh026d5` | Why no regular dental care: not enough information about it | `Numeric(Byte)` | `%12.0g` |
| `rh026d6` | Why no regular dental care: not usual to get it | `Numeric(Byte)` | `%12.0g` |
| `rh026d7` | Why no regular dental care: no place to receive it close to home | `Numeric(Byte)` | `%12.0g` |
| `rh026d8` | Why no regular dental care: not considered to be necessary | `Numeric(Byte)` | `%12.0g` |
| `rh026dot` | Why no regular dental care: other reasons | `Numeric(Byte)` | `%12.0g` |
| `rh042ad1` | No blood pressure checks: when between 0-15 years old | `Numeric(Byte)` | `%12.0g` |
| `rh042ad2` | No blood pressure checks: when between 16-25 years old | `Numeric(Byte)` | `%12.0g` |
| `rh042ad3` | No blood pressure checks: when between 26-40 years old | `Numeric(Byte)` | `%12.0g` |
| `rh042ad4` | No blood pressure checks: when between 41-55 years old | `Numeric(Byte)` | `%12.0g` |
| `rh042ad5` | No blood pressure checks: when between 56-65 years old | `Numeric(Byte)` | `%12.0g` |
| `rh042ad6` | No blood pressure checks: when between 66-75 years old | `Numeric(Byte)` | `%12.0g` |
| `rh042ad7` | No blood pressure checks: when older than 75 years | `Numeric(Byte)` | `%12.0g` |
| `rh050d1` | Why no regular blood pressure checks: not affordable | `Numeric(Byte)` | `%12.0g` |
| `rh050d2` | Why no regular blood pressure checks: not covered by health insurance | `Numeric(Byte)` | `%12.0g` |
| `rh050d3` | Why no regular blood pressure checks: did not have health insurance | `Numeric(Byte)` | `%12.0g` |
| `rh050d4` | Why no regular blood pressure checks: time constraints | `Numeric(Byte)` | `%12.0g` |
| `rh050d5` | Why no regular blood pressure checks: not enough information about it | `Numeric(Byte)` | `%12.0g` |
| `rh050d6` | Why no regular blood pressure checks: not usual to get it | `Numeric(Byte)` | `%12.0g` |
| `rh050d7` | Why no regular blood pressure checks: no place to receive it close to home | `Numeric(Byte)` | `%12.0g` |
| `rh050d8` | Why no regular blood pressure checks: not considered to be necessary | `Numeric(Byte)` | `%12.0g` |
| `rh050dot` | Why no regular blood pressure checks: other reasons | `Numeric(Byte)` | `%12.0g` |

### `rp` - Retrospective Partner History

- Dataset: `sharew7_rel9-0-0_rp.dta`
- Read with: `ps.read_share_module("rp", wave=7)`
- Rows: 77,181
- Variables: 139
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `rp002_` | Ever been married | `Numeric(Byte)` | `%10.0g` |
| `rp002d_` | Ever had unmarried partner | `Numeric(Byte)` | `%10.0g` |
| `rp002e_` | How often married | `Numeric(Byte)` | `%10.0g` |
| `rp004c_1` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `rp008_1` | Year married | `Numeric(Int)` | `%10.0g` |
| `rp004b_1` | Year started living with married partner | `Numeric(Int)` | `%20.0g` |
| `rp009_1` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `rp010_1` | Reasons for not living with partner | `Numeric(Byte)` | `%45.0g` |
| `rp011_1` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `rp012_1` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `rp013_1` | Divorced partner | `Numeric(Byte)` | `%10.0g` |
| `rp014_1` | Year of divorce | `Numeric(Int)` | `%10.0g` |
| `rp004c_2` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `rp008_2` | Year married | `Numeric(Int)` | `%10.0g` |
| `rp004b_2` | Year started living with married partner | `Numeric(Int)` | `%20.0g` |
| `rp009_2` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `rp010_2` | Reasons for not living with partner | `Numeric(Byte)` | `%45.0g` |
| `rp011_2` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `rp012_2` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `rp013_2` | Divorced partner | `Numeric(Byte)` | `%10.0g` |
| `rp014_2` | Year of divorce | `Numeric(Int)` | `%10.0g` |
| `rp004c_3` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `rp008_3` | Year married | `Numeric(Int)` | `%10.0g` |
| `rp004b_3` | Year started living with married partner | `Numeric(Int)` | `%20.0g` |
| `rp009_3` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `rp010_3` | Reasons for not living with partner | `Numeric(Byte)` | `%45.0g` |
| `rp011_3` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `rp012_3` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `rp013_3` | Divorced partner | `Numeric(Byte)` | `%10.0g` |
| `rp014_3` | Year of divorce | `Numeric(Int)` | `%10.0g` |
| `rp004c_4` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `rp008_4` | Year married | `Numeric(Int)` | `%10.0g` |
| `rp004b_4` | Year started living with married partner | `Numeric(Int)` | `%20.0g` |
| `rp009_4` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `rp010_4` | Reasons for not living with partner | `Numeric(Byte)` | `%45.0g` |
| `rp011_4` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `rp012_4` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `rp013_4` | Divorced partner | `Numeric(Byte)` | `%10.0g` |
| `rp014_4` | Year of divorce | `Numeric(Int)` | `%10.0g` |
| `rp004c_5` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `rp008_5` | Year married | `Numeric(Int)` | `%10.0g` |
| `rp004b_5` | Year started living with married partner | `Numeric(Int)` | `%20.0g` |
| `rp009_5` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `rp004c_11` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `rp003_11` | Year started living with partner | `Numeric(Int)` | `%10.0g` |
| `rp009_11` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `rp010_11` | Reasons for not living with partner | `Numeric(Byte)` | `%45.0g` |
| `rp011_11` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `rp012_11` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `rp015a_11` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp004c_12` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `rp003_12` | Year started living with partner | `Numeric(Int)` | `%10.0g` |
| `rp009_12` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `rp010_12` | Reasons for not living with partner | `Numeric(Byte)` | `%45.0g` |
| `rp011_12` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `rp012_12` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `rp015a_12` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp004c_13` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `rp003_13` | Year started living with partner | `Numeric(Int)` | `%10.0g` |
| `rp009_13` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `rp010_13` | Reasons for not living with partner | `Numeric(Byte)` | `%45.0g` |
| `rp011_13` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `rp012_13` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `rp015a_13` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp004c_14` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `rp003_14` | Year started living with partner | `Numeric(Int)` | `%10.0g` |
| `rp009_14` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `rp010_14` | Reasons for not living with partner | `Numeric(Byte)` | `%45.0g` |
| `rp011_14` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `rp012_14` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `rp015a_14` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp004c_15` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `rp003_15` | Year started living with partner | `Numeric(Int)` | `%10.0g` |
| `rp009_15` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `rp010_15` | Reasons for not living with partner | `Numeric(Byte)` | `%45.0g` |
| `rp011_15` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `rp012_15` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `rp015a_15` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp004c_16` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `rp003_16` | Year started living with partner | `Numeric(Int)` | `%10.0g` |
| `rp009_16` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `rp010_16` | Reasons for not living with partner | `Numeric(Byte)` | `%45.0g` |
| `rp011_16` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `rp012_16` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `rp015a_16` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp004c_17` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `rp003_17` | Year started living with partner | `Numeric(Int)` | `%10.0g` |
| `rp009_17` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `rp010_17` | Reasons for not living with partner | `Numeric(Byte)` | `%45.0g` |
| `rp012_17` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `rp015a_17` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp016_` | Non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp017_1` | Start non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `rp019_1` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `rp020_1` | End non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `rp021_1` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp017_2` | Start non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `rp019_2` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `rp020_2` | End non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `rp021_2` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp017_3` | Start non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `rp019_3` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `rp020_3` | End non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `rp021_3` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp017_4` | Start non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `rp019_4` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `rp020_4` | End non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `rp021_4` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp017_5` | Start non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `rp019_5` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `rp020_5` | End non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `rp021_5` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp017_6` | Start non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `rp019_6` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `rp020_6` | End non-cohabitating partnership | `Numeric(Byte)` | `%10.0g` |
| `rp021_6` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp017_7` | Start non-cohabitating partnership | `Numeric(Byte)` | `%10.0g` |
| `rp019_7` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `rp020_7` | End non-cohabitating partnership | `Numeric(Byte)` | `%10.0g` |
| `rp021_7` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp017_8` | Start non-cohabitating partnership | `Numeric(Byte)` | `%10.0g` |
| `rp019_8` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `rp020_8` | End non-cohabitating partnership | `Numeric(Byte)` | `%10.0g` |
| `rp021_8` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp017_9` | Start non-cohabitating partnership | `Numeric(Byte)` | `%10.0g` |
| `rp019_9` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `rp020_9` | End non-cohabitating partnership | `Numeric(Byte)` | `%10.0g` |
| `rp021_9` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp017_10` | Start non-cohabitating partnership | `Numeric(Byte)` | `%10.0g` |
| `rp019_10` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `rp020_10` | End non-cohabitating partnership | `Numeric(Byte)` | `%10.0g` |
| `rp021_10` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `rp023_` | Proxy check | `Numeric(Byte)` | `%44.0g` |

### `wq` - Work Quality

- Dataset: `sharew7_rel9-0-0_wq.dta`
- Read with: `ps.read_share_module("wq", wave=7)`
- Rows: 77,181
- Variables: 276
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `wq726_1` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_1` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_1` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_1` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_1` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_1` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_1` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_1` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_1` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_1` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_1` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_1` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_1` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_1` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_1` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_2` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_2` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_2` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_2` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_2` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_2` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_2` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_2` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_2` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_2` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_2` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_2` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_2` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_2` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_2` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_3` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_3` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_3` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_3` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_3` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_3` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_3` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_3` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_3` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_3` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_3` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_3` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_3` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_3` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_3` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_4` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_4` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_4` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_4` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_4` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_4` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_4` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_4` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_4` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_4` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_4` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_4` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_4` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_4` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_4` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_5` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_5` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_5` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_5` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_5` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_5` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_5` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_5` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_5` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_5` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_5` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_5` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_5` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_5` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_5` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_6` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_6` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_6` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_6` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_6` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_6` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_6` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_6` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_6` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_6` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_6` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_6` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_6` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_6` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_6` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_7` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_7` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_7` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_7` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_7` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_7` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_7` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_7` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_7` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_7` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_7` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_7` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_7` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_7` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_7` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_8` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_8` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_8` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_8` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_8` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_8` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_8` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_8` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_8` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_8` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_8` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_8` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_8` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_8` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_8` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_9` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_9` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_9` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_9` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_9` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_9` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_9` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_9` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_9` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_9` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_9` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_9` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_9` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_9` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_9` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_10` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_10` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_10` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_10` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_10` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_10` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_10` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_10` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_10` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_10` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_10` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_10` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_10` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_10` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_10` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_11` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_11` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_11` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_11` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_11` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_11` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_11` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_11` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_11` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_11` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_11` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_11` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_11` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_11` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_11` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_12` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_12` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_12` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_12` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_12` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_12` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_12` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_12` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_12` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_12` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_12` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_12` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_12` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_12` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_12` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_13` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_13` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_13` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_13` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_13` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_13` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_13` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_13` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_13` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_13` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_13` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_13` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_13` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_13` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_13` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_14` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_14` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_14` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_14` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_14` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_14` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_14` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_14` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_14` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_14` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_14` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_14` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_14` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_14` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_14` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_15` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_15` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_15` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_15` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_15` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_15` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_15` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_15` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_15` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_15` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_15` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_15` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_15` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_15` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_15` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_16` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_16` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_16` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_16` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_16` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_16` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_16` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_16` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_16` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_16` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_16` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_16` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_16` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_16` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_16` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq726_18` | Satisfied with current job | `Numeric(Byte)` | `%26.0g` |
| `wq016_18` | Work is physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq017_18` | Work is uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq018_18` | Work has heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq019_18` | Work is emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq020_18` | Work involves conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq021_18` | Work has little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq022_18` | Work allows development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq023_18` | Work gives recognition | `Numeric(Byte)` | `%26.0g` |
| `wq024_18` | Work has adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq025_18` | Work has adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq026_18` | Current work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq027_18` | Work employees are treated fairly | `Numeric(Byte)` | `%26.0g` |
| `wq028_18` | Current work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq729_18` | Proxy check | `Numeric(Byte)` | `%59.0g` |
| `wq727_` | Satisfaction with job | `Numeric(Byte)` | `%26.0g` |
| `wq002_` | Work was physically demanding | `Numeric(Byte)` | `%26.0g` |
| `wq003_` | Work was uncomfortable | `Numeric(Byte)` | `%26.0g` |
| `wq004_` | Work had heavy time pressure | `Numeric(Byte)` | `%26.0g` |
| `wq005_` | Work was emotionally demanding | `Numeric(Byte)` | `%26.0g` |
| `wq006_` | Work involved conflicts | `Numeric(Byte)` | `%26.0g` |
| `wq007_` | Work had little freedom to decide | `Numeric(Byte)` | `%26.0g` |
| `wq008_` | Work allowed development of skills | `Numeric(Byte)` | `%26.0g` |
| `wq009_` | Work gave recognition | `Numeric(Byte)` | `%26.0g` |
| `wq010_` | Work had adequate salary | `Numeric(Byte)` | `%26.0g` |
| `wq011_` | Work had adequate support | `Numeric(Byte)` | `%26.0g` |
| `wq012_` | Work atmosphere | `Numeric(Byte)` | `%26.0g` |
| `wq013_` | Work employees treated fair | `Numeric(Byte)` | `%26.0g` |
| `wq014_` | Work health risk reduced | `Numeric(Byte)` | `%26.0g` |
| `wq715_` | Proxy check | `Numeric(Byte)` | `%59.0g` |


## Generated Modules

### `gv_big5` - Big Five traits

- Dataset: `sharew7_rel9-0-0_gv_big5.dta`
- Read with: `ps.read_share_module("gv_big5", wave=7)`
- Rows: 77,181
- Variables: 11
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `bfi10_extra` | Extraversion (Big Five personality inventory) | `Numeric(Float)` | `%9.0g` |
| `bfi10_agree` | Agreeableness (Big Five personality inventory) | `Numeric(Float)` | `%9.0g` |
| `bfi10_consc` | Conscientiousness (Big Five personality inventory) | `Numeric(Float)` | `%9.0g` |
| `bfi10_neuro` | Neuroticism (Big Five personality inventory) | `Numeric(Float)` | `%9.0g` |
| `bfi10_open` | Openness (Big Five personality inventory) | `Numeric(Float)` | `%9.0g` |

### `gv_children` - Generated child-level summaries

- Dataset: `sharew7_rel9-0-0_gv_children.dta`
- Read with: `ps.read_share_module("gv_children", wave=7)`
- Rows: 77,181
- Variables: 907
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
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
| `childid_14` | Child identifier (fix across modules and waves): Child 14 | `Str(1)` | `%9s` |
| `childid_15` | Child identifier (fix across modules and waves): Child 15 | `Str(1)` | `%9s` |
| `childid_16` | Child identifier (fix across modules and waves): Child 16 | `Str(14)` | `%14s` |
| `childid_17` | Child identifier (fix across modules and waves): Child 17 | `Str(1)` | `%9s` |
| `childid_18` | Child identifier (fix across modules and waves): Child 18 | `Str(1)` | `%9s` |
| `childid_19` | Child identifier (fix across modules and waves): Child 19 | `Str(1)` | `%9s` |
| `childid_20` | Child identifier (fix across modules and waves): Child 20 | `Str(14)` | `%14s` |
| `ch001_` | Number of children | `Numeric(Byte)` | `%10.0g` |
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
| `ch_yrbirth_14` | Child year of birth, based on ch006_14 | `Numeric(Byte)` | `%10.0g` |
| `ch_yrbirth_15` | Child year of birth, based on ch006_15 | `Numeric(Byte)` | `%10.0g` |
| `ch_yrbirth_16` | Child year of birth, based on ch006_16 | `Numeric(Int)` | `%10.0g` |
| `ch_yrbirth_17` | Child year of birth, based on ch006_17 | `Numeric(Byte)` | `%10.0g` |
| `ch_yrbirth_18` | Child year of birth, based on ch006_18 | `Numeric(Byte)` | `%10.0g` |
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
| `ch_contact_1` | Contact to child 1, based on ch014_1 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_2` | Contact to child 2, based on ch014_2 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_3` | Contact to child 3, based on ch014_3 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_4` | Contact to child 4, based on ch014_4 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_5` | Contact to child 5, based on ch014_5 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_6` | Contact to child 6, based on ch014_6 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_7` | Contact to child 7, based on ch014_7 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_8` | Contact to child 8, based on ch014_8 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_9` | Contact to child 9, based on ch014_9 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_10` | Contact to child 10, based on ch014_10 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_11` | Contact to child 11, based on ch014_11 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_12` | Contact to child 12, based on ch014_12 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_13` | Contact to child 13, based on ch014_13 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_14` | Contact to child 14, based on ch014_14 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_15` | Contact to child 15, based on ch014_15 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_16` | Contact to child 16, based on ch014_16 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_17` | Contact to child 17, based on ch014_17 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_18` | Contact to child 18, based on ch014_18 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_19` | Contact to child 19, based on ch014_19 | `Numeric(Byte)` | `%27.0g` |
| `ch_contact_20` | Contact to child 20, based on ch014_20 | `Numeric(Byte)` | `%27.0g` |
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
| `ch_move_out_year_10` | Year when child 10 moved out, based on ch015_10 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_11` | Year when child 11 moved out, based on ch015_11 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_12` | Year when child 12 moved out, based on ch015_12 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_13` | Year when child 13 moved out, based on ch015_13 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_14` | Year when child 14 moved out, based on ch015_14 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_15` | Year when child 15 moved out, based on ch015_15 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_16` | Year when child 16 moved out, based on ch015_16 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_17` | Year when child 17 moved out, based on ch015_17 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_18` | Year when child 18 moved out, based on ch015_18 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_19` | Year when child 19 moved out, based on ch015_19 | `Numeric(Byte)` | `%33.0g` |
| `ch_move_out_year_20` | Year when child 20 moved out, based on ch015_20 | `Numeric(Byte)` | `%33.0g` |
| `ch_marital_status_1` | Marital status of child 1, based on ch012_1 & ch516_1 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_2` | Marital status of child 2, based on ch012_2 & ch516_2 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_3` | Marital status of child 3, based on ch012_3 & ch516_3 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_4` | Marital status of child 4, based on ch012_4 & ch516_4 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_5` | Marital status of child 5, based on ch012_5 & ch516_5 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_6` | Marital status of child 6, based on ch012_6 & ch516_6 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_7` | Marital status of child 7, based on ch012_7 & ch516_7 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_8` | Marital status of child 8, based on ch012_8 & ch516_8 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_9` | Marital status of child 9, based on ch012_9 & ch516_9 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_10` | Marital status of child 10, based on ch012_10 & ch516_10 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_11` | Marital status of child 11, based on ch012_11 & ch516_11 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_12` | Marital status of child 12, based on ch012_12 & ch516_12 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_13` | Marital status of child 13, based on ch012_13 & ch516_13 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_14` | Marital status of child 14, based on ch012_14 & ch516_14 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_15` | Marital status of child 15, based on ch012_15 & ch516_15 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_16` | Marital status of child 16, based on ch012_16 & ch516_16 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_17` | Marital status of child 17, based on ch012_17 & ch516_17 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_18` | Marital status of child 18, based on ch012_18 & ch516_18 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_19` | Marital status of child 19, based on ch012_19 & ch516_19 | `Numeric(Byte)` | `%56.0g` |
| `ch_marital_status_20` | Marital status of child 20, based on ch012_20 & ch516_20 | `Numeric(Byte)` | `%56.0g` |
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
| `ch_occupation_1` | Occupational status of child 1, based on ch016_1 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_2` | Occupational status of child 2, based on ch016_2 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_3` | Occupational status of child 3, based on ch016_3 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_4` | Occupational status of child 4, based on ch016_4 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_5` | Occupational status of child 5, based on ch016_5 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_6` | Occupational status of child 6, based on ch016_6 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_7` | Occupational status of child 7, based on ch016_7 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_8` | Occupational status of child 8, based on ch016_8 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_9` | Occupational status of child 9, based on ch016_9 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_10` | Occupational status of child 10, based on ch016_10 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_11` | Occupational status of child 11, based on ch016_11 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_12` | Occupational status of child 12, based on ch016_12 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_13` | Occupational status of child 13, based on ch016_13 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_14` | Occupational status of child 14, based on ch016_14 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_15` | Occupational status of child 15, based on ch016_15 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_16` | Occupational status of child 16, based on ch016_16 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_17` | Occupational status of child 17, based on ch016_17 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_18` | Occupational status of child 18, based on ch016_18 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_19` | Occupational status of child 19, based on ch016_19 | `Numeric(Byte)` | `%58.0g` |
| `ch_occupation_20` | Occupational status of child 20, based on ch016_20 | `Numeric(Byte)` | `%58.0g` |
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
| `ch_yrbirth_youngest_child_11` | Yrbirth youngest child of child 11, based on ch020_11 & ch520_11 | `Numeric(Byte)` | `%15.0g` |
| `ch_yrbirth_youngest_child_12` | Yrbirth youngest child of child 12, based on ch020_12 & ch520_12 | `Numeric(Byte)` | `%15.0g` |
| `ch_yrbirth_youngest_child_13` | Yrbirth youngest child of child 13, based on ch020_13 & ch520_13 | `Numeric(Byte)` | `%15.0g` |
| `ch_yrbirth_youngest_child_14` | Yrbirth youngest child of child 14, based on ch020_14 & ch520_14 | `Numeric(Byte)` | `%15.0g` |
| `ch_yrbirth_youngest_child_15` | Yrbirth youngest child of child 15, based on ch020_15 & ch520_15 | `Numeric(Byte)` | `%15.0g` |
| `ch_yrbirth_youngest_child_16` | Yrbirth youngest child of child 16, based on ch020_16 & ch520_16 | `Numeric(Byte)` | `%15.0g` |
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
| `ch_school_education_1` | School degree of child 1, based on ch017_1 & ch510_1 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_2` | School degree of child 2, based on ch017_2 & ch510_2 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_3` | School degree of child 3, based on ch017_3 & ch510_3 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_4` | School degree of child 4, based on ch017_4 & ch510_4 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_5` | School degree of child 5, based on ch017_5 & ch510_5 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_6` | School degree of child 6, based on ch017_6 & ch510_6 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_7` | School degree of child 7, based on ch017_7 & ch510_7 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_8` | School degree of child 8, based on ch017_8 & ch510_8 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_9` | School degree of child 9, based on ch017_9 & ch510_9 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_10` | School degree of child 10, based on ch017_10 & ch510_10 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_11` | School degree of child 11, based on ch017_11 & ch510_11 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_12` | School degree of child 12, based on ch017_12 & ch510_12 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_13` | School degree of child 13, based on ch017_13 & ch510_13 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_14` | School degree of child 14, based on ch017_14 & ch510_14 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_15` | School degree of child 15, based on ch017_15 & ch510_15 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_16` | School degree of child 16, based on ch017_16 & ch510_16 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_17` | School degree of child 17, based on ch017_17 & ch510_17 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_18` | School degree of child 18, based on ch017_18 & ch510_18 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_19` | School degree of child 19, based on ch017_19 & ch510_19 | `Numeric(Byte)` | `%164.0g` |
| `ch_school_education_20` | School degree of child 20, based on ch017_20 & ch510_20 | `Numeric(Byte)` | `%164.0g` |
| `ch_further_education_1_1` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_2` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_3` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_4` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_5` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_6` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_7` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_8` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_9` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_10` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_11` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_12` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_13` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_14` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_15` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_16` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_17` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_18` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_19` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_20` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_21` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_1_22` | Further education of child 1, based on ch018_1_* & ch513_1_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_1` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_2` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_3` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_4` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_5` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_6` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_7` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_8` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_9` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_10` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_11` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_12` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_13` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_14` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_15` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_16` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_17` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_18` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_19` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_20` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_21` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_2_22` | Further education of child 2, based on ch018_2_* & ch513_2_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_1` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_2` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_3` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_4` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_5` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_6` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_7` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_8` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_9` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_10` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_11` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_12` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_13` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_14` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_15` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_16` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_17` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_18` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_19` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_20` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_21` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_3_22` | Further education of child 3, based on ch018_3_* & ch513_3_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_1` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_2` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_3` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_4` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_5` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_6` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_7` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_8` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_9` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_10` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_11` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_12` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_13` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_14` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_15` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_16` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_17` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_18` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_19` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_20` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_21` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_4_22` | Further education of child 4, based on ch018_4_* & ch513_4_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_1` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_2` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_3` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_4` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_5` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_6` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_7` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_8` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_9` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_10` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_11` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_12` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_13` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_14` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_15` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_16` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_17` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_18` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_19` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_20` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_21` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_5_22` | Further education of child 5, based on ch018_5_* & ch513_5_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_1` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_2` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_3` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_4` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_5` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_6` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_7` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_8` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_9` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_10` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_11` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_12` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_13` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_14` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_15` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_16` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_17` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_18` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_19` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_20` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_21` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_6_22` | Further education of child 6, based on ch018_6_* & ch513_6_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_1` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_2` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_3` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_4` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_5` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_6` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_7` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_8` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_9` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_10` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_11` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_12` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_13` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_14` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_15` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_16` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_17` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_18` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_19` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_20` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_21` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_7_22` | Further education of child 7, based on ch018_7_* & ch513_7_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_1` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_2` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_3` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_4` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_5` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_6` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_7` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_8` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_9` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_10` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_11` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_12` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_13` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_14` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_15` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_16` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_17` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_18` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_19` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_20` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_21` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_8_22` | Further education of child 8, based on ch018_8_* & ch513_8_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_1` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_2` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_3` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_4` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_5` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_6` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_7` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_8` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_9` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_10` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_11` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_12` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_13` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_14` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_15` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_16` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_17` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_18` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_19` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_20` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_21` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_9_22` | Further education of child 9, based on ch018_9_* & ch513_9_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_1` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_2` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_3` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_4` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_5` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_6` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_7` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_8` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_9` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_10` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_11` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_12` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_13` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_14` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_15` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_16` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_17` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_18` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_19` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_20` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_21` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_10_22` | Further education of child 10, based on ch018_10_* & ch513_10_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_1` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_2` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_3` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_4` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_5` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_6` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_7` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_8` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_9` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_10` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_11` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_12` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_13` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_14` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_15` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_16` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_17` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_18` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_19` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_20` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_21` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_11_22` | Further education of child 11, based on ch018_11_* & ch513_11_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_1` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_2` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_3` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_4` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_5` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_6` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_7` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_8` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_9` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_10` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_11` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_12` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_13` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_14` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_15` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_16` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_17` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_18` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_19` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_20` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_21` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_12_22` | Further education of child 12, based on ch018_12_* & ch513_12_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_1` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_2` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_3` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_4` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_5` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_6` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_7` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_8` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_9` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_10` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_11` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_12` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_13` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_14` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_15` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_16` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_17` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_18` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_19` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_20` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_21` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_13_22` | Further education of child 13, based on ch018_13_* & ch513_13_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_1` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_2` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_3` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_4` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_5` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_6` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_7` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_8` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_9` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_10` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_11` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_12` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_13` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_14` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_15` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_16` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_17` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_18` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_19` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_20` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_21` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_14_22` | Further education of child 14, based on ch018_14_* & ch513_14_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_1` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_2` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_3` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_4` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_5` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_6` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_7` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_8` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_9` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_10` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_11` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_12` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_13` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_14` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_15` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_16` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_17` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_18` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_19` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_20` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_21` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_15_22` | Further education of child 15, based on ch018_15_* & ch513_15_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_1` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_2` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_3` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_4` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_5` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_6` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_7` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_8` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_9` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_10` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_11` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_12` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_13` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_14` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_15` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_16` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_17` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_18` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_19` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_20` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_21` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_16_22` | Further education of child 16, based on ch018_16_* & ch513_16_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_1` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_2` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_3` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_4` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_5` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_6` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_7` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_8` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_9` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_10` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_11` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_12` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_13` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_14` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_15` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_16` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_17` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_18` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_19` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_20` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_21` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_17_22` | Further education of child 17, based on ch018_17_* & ch513_17_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_1` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_2` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_3` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_4` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_5` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_6` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_7` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_8` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_9` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_10` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_11` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_12` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_13` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_14` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_15` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_16` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_17` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_18` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_19` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_20` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_21` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_18_22` | Further education of child 18, based on ch018_18_* & ch513_18_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_1` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_2` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_3` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_4` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_5` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_6` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_7` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_8` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_9` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_10` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_11` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_12` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_13` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_14` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_15` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_16` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_17` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_18` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_19` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_20` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_21` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_19_22` | Further education of child 19, based on ch018_19_* & ch513_19_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_1` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_2` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_3` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_4` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_5` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_6` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_7` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_8` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_9` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_10` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_11` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_12` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_13` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_14` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_15` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_16` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_17` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_18` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_19` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_20` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_21` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
| `ch_further_education_20_22` | Further education of child 20, based on ch018_20_* & ch513_20_* | `Numeric(Byte)` | `%108.0g` |
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

- Dataset: `sharew7_rel9-0-0_gv_exrates.dta`
- Read with: `ps.read_share_module("gv_exrates", wave=7)`
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

- Dataset: `sharew7_rel9-0-0_gv_health.dta`
- Read with: `ps.read_share_module("gv_health", wave=7)`
- Rows: 77,181
- Variables: 43
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `adl` | Number of limitations with activities of daily living (adl) | `Numeric(Byte)` | `%10.0g` |
| `adl2` | 1+ adl limitations | `Numeric(Byte)` | `%18.0g` |
| `bmi` | Body mass index | `Numeric(Float)` | `%28.0g` |
| `bmi2` | Bmi categories | `Numeric(Byte)` | `%27.0g` |
| `casp` | CASP index for quality of life and well-being | `Numeric(Byte)` | `%10.0g` |
| `cf008tot` | Ten words list learning first trial total | `Numeric(Byte)` | `%9.0g` |
| `cf016tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `chronic2w7` | 2+ chronic diseases (w7 version) | `Numeric(Byte)` | `%20.0g` |
| `chronicw7` | Number of chronic diseases (w7 version) | `Numeric(Byte)` | `%10.0g` |
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

- Dataset: `sharew7_rel9-0-0_gv_housing.dta`
- Read with: `ps.read_share_module("gv_housing", wave=7)`
- Rows: 77,181
- Variables: 10
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `areabldgi` | Area of building | `Numeric(Byte)` | `%38.0g` |
| `typebldgi6` | Type of building (since w6) | `Numeric(Byte)` | `%57.0g` |
| `nstepsi` | Number of steps to entrance | `Numeric(Byte)` | `%12.0g` |
| `nuts1_2013` | NUTS 2013 level 1: nomenclature of territorial units for statistics | `Str(44)` | `%44s` |

### `gv_imputations` - Multiple imputations

- Dataset: `sharew7_rel9-0-0_gv_imputations.dta`
- Read with: `ps.read_share_module("gv_imputations", wave=7)`
- Rows: 385,905
- Variables: 280
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `implicat` | Implicat number | `Numeric(Byte)` | `%9.0g` |
| `htype` | Household type | `Numeric(Byte)` | `%16.0g` |
| `SHARELIFE` | Individual indicator of SHARELIFE interview | `Numeric(Byte)` | `%14.0g` |
| `H_SHARELIFE` | Household indicator of SHARELIFE interview | `Numeric(Byte)` | `%14.0g` |
| `Sample_SH1` | First imputation sample for SHARELIFE interviews: single | `Numeric(Byte)` | `%14.0g` |
| `Sample_SH2` | Second imputation sample for SHARELIFE interviews: all couples | `Numeric(Byte)` | `%14.0g` |
| `Sample_RE1` | First imputation sample for regular interviews: single and C2R | `Numeric(Byte)` | `%14.0g` |
| `Sample_RE2` | Second imputation sample for regular interviews: all couples | `Numeric(Byte)` | `%14.0g` |
| `fam_resp` | Family respondent | `Numeric(Byte)` | `%14.0g` |
| `fin_resp` | Financial respondent | `Numeric(Byte)` | `%14.0g` |
| `hou_resp` | Household respondent | `Numeric(Byte)` | `%14.0g` |
| `exrate` | Exchange rate | `Numeric(Float)` | `%9.0g` |
| `couple` | Couple | `Numeric(Byte)` | `%14.0g` |
| `nursinghome` | Living in nursing home | `Numeric(Byte)` | `%14.0g` |
| `perho` | Percentage of house owned | `Numeric(Byte)` | `%14.0g` |
| `otrf` | Owner, tenant or rent free | `Numeric(Byte)` | `%24.0g` |
| `single` | Single | `Numeric(Byte)` | `%14.0g` |
| `partner` | Partner in the couple | `Numeric(Byte)` | `%14.0g` |
| `p_nrp` | Partner of nonresponding partner | `Numeric(Byte)` | `%14.0g` |
| `inpat7` | Paid out-of-pocket for inpatient care | `Numeric(Double)` | `%9.0g` |
| `outpa7` | Paid out-of-pocket for outpatient care | `Numeric(Double)` | `%9.0g` |
| `drugs7` | Paid out-of-pocket for prescribed drugs | `Numeric(Double)` | `%9.0g` |
| `nurs7` | Paid out-of-pocket for nursing home/home care | `Numeric(Double)` | `%9.0g` |
| `aapt7` | Paid out-of-pocket for aids, appliances, physical therapy | `Numeric(Double)` | `%9.0g` |
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
| `ylsp4` | LS payments from unemployment benefits/insurances | `Numeric(Float)` | `%9.0g` |
| `ylsp5` | LS payments from social assistance | `Numeric(Double)` | `%9.0g` |
| `ylsp6` | LS payments from sickness benefits | `Numeric(Double)` | `%9.0g` |
| `yreg1` | Regular private payments | `Numeric(Double)` | `%9.0g` |
| `yreg2` | Other regular private transfers | `Numeric(Double)` | `%9.0g` |
| `ylsr1` | LS from private payments | `Numeric(Double)` | `%9.0g` |
| `ylsr2` | LS from other private transfers | `Numeric(Float)` | `%9.0g` |
| `home` | Value of main residence | `Numeric(Double)` | `%9.0g` |
| `mort` | Mortgage on main residence | `Numeric(Double)` | `%9.0g` |
| `rhre` | Rent and home-related expenditures | `Numeric(Double)` | `%9.0g` |
| `ores` | Value of real estate - Amount | `Numeric(Double)` | `%9.0g` |
| `ysrent` | Income from rent/sublet | `Numeric(Double)` | `%9.0g` |
| `yaohm` | Income from other household members | `Numeric(Double)` | `%9.0g` |
| `fahc` | Amount spent on food at home | `Numeric(Double)` | `%9.0g` |
| `fohc` | Amount spent on food outside home | `Numeric(Double)` | `%9.0g` |
| `hprf` | Value of home produced food | `Numeric(Double)` | `%9.0g` |
| `hmem` | Minimum amount needed per month to make ends meet | `Numeric(Double)` | `%9.0g` |
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
| `yedu` | Years of education | `Numeric(Float)` | `%22.0g` |
| `yedu_p` | Years of education of partner | `Numeric(Float)` | `%22.0g` |
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
| `doctor` | Seen/Talked to medical doctor | `Numeric(Byte)` | `%14.0g` |
| `hospital` | In hospital last 12 months | `Numeric(Byte)` | `%14.0g` |
| `thospital` | Times being patient in hospital | `Numeric(Byte)` | `%10.0g` |
| `nhospital` | Total nights stayed in hospital | `Numeric(Int)` | `%14.0g` |
| `cjs` | Current job situation | `Numeric(Byte)` | `%90.0g` |
| `pwork` | Did any paid work | `Numeric(Byte)` | `%14.0g` |
| `empstat` | Employee or self-employed | `Numeric(Byte)` | `%35.0g` |
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
| `politics` | Left or right in politics | `Numeric(Byte)` | `%14.0g` |
| `bfi10_extra` | Extraversion (Big Five personality inventory) | `Numeric(Float)` | `%14.0g` |
| `bfi10_agree` | Agreeableness (Big Five personality inventory) | `Numeric(Float)` | `%14.0g` |
| `bfi10_consc` | Conscientiousness (Big Five personality inventory) | `Numeric(Float)` | `%14.0g` |
| `bfi10_neuro` | Neuroticism (Big Five personality inventory) | `Numeric(Float)` | `%14.0g` |
| `bfi10_open` | Openness (Big Five personality inventory) | `Numeric(Float)` | `%14.0g` |
| `tppdi` | Third persons present during the interview | `Numeric(Byte)` | `%14.0g` |
| `willans` | Willingness to answer | `Numeric(Byte)` | `%21.0g` |
| `clarif` | Respondent asked for clarifications | `Numeric(Byte)` | `%14.0g` |
| `undersq` | Respondent understood questions | `Numeric(Byte)` | `%14.0g` |
| `hnrsc` | Help needed to read showcards | `Numeric(Byte)` | `%19.0g` |
| `inpat7_f` | Paid out-of-pocket for inpatient care - Flag | `Numeric(Byte)` | `%21.0g` |
| `outpa7_f` | Paid out-of-pocket for outpatient care - Flag | `Numeric(Byte)` | `%21.0g` |
| `drugs7_f` | Paid out-of-pocket for prescribed drugs - Flag | `Numeric(Byte)` | `%21.0g` |
| `nurs7_f` | Paid out-of-pocket for nursing home/home care - Flag | `Numeric(Byte)` | `%21.0g` |
| `aapt7_f` | Paid out-of-pocket for aids, appliances, physical therapy - Flag | `Numeric(Byte)` | `%21.0g` |
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
| `hmem_f` | Minimum amount needed per month to make ends meet - Flag | `Numeric(Byte)` | `%21.0g` |
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
| `politics_f` | Left or right in politics - Flag | `Numeric(Byte)` | `%20.0g` |
| `bfi10_extra_f` | Extraversion (Big Five personality inventory) - Flag | `Numeric(Byte)` | `%20.0g` |
| `bfi10_agree_f` | Agreeableness (Big Five personality inventory) - Flag | `Numeric(Byte)` | `%20.0g` |
| `bfi10_consc_f` | Conscientiousness (Big Five personality inventory) - Flag | `Numeric(Byte)` | `%20.0g` |
| `bfi10_neuro_f` | Neuroticism (Big Five personality inventory) - Flag | `Numeric(Byte)` | `%20.0g` |
| `bfi10_open_f` | Openness (Big Five personality inventory) - Flag | `Numeric(Byte)` | `%20.0g` |
| `tppdi_f` | Third persons present during the interview - Flag | `Numeric(Byte)` | `%20.0g` |
| `willans_f` | Willingness to answer - Flag | `Numeric(Byte)` | `%20.0g` |
| `clarif_f` | Respondent asked for clarifications - Flag | `Numeric(Byte)` | `%20.0g` |
| `undersq_f` | Respondent understood questions - Flag | `Numeric(Byte)` | `%20.0g` |
| `hnrsc_f` | Help needed to read showcards â€“ Flag | `Numeric(Byte)` | `%20.0g` |
| `currency` | currency | `Str(16)` | `%16s` |
| `nomx2016` | Nominal exchange rate (national currency/Euro), annual average, 2016 | `Numeric(Double)` | `%10.0g` |
| `nomx2017` | Nominal exchange rate (national currency/Euro), annual average, 2017 | `Numeric(Double)` | `%10.0g` |
| `pppc2016` | Current PPP exchange rate (national currency/Euro), 2016 | `Numeric(Double)` | `%10.0g` |
| `pppc2017` | Current PPP exchange rate (national currency/Euro), 2017 | `Numeric(Double)` | `%10.0g` |
| `pppk2016` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2016 | `Numeric(Double)` | `%10.0g` |
| `pppk2017` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2017 | `Numeric(Double)` | `%10.0g` |

### `gv_isced` - ISCED education recodes

- Dataset: `sharew7_rel9-0-0_gv_isced.dta`
- Read with: `ps.read_share_module("gv_isced", wave=7)`
- Rows: 77,181
- Variables: 54
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
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

### `gv_weights` - Cross-sectional weights

- Dataset: `sharew7_rel9-0-0_gv_weights.dta`
- Read with: `ps.read_share_module("gv_weights", wave=7)`
- Rows: 77,181
- Variables: 20
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid7` | Household identifier (wave 7) | `Str(11)` | `%11s` |
| `mergeidp7` | Partner identifier (wave 7) | `Str(12)` | `%12s` |
| `coupleid7` | Couple identifier (wave 7) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `SHARELIFE` | Dummy for respondent's SHARELIFE interview | `Numeric(Byte)` | `%9.0g` |
| `H_SHARELIFE` | Indicator for household SHARELIFE interview | `Numeric(Byte)` | `%14.0g` |
| `dw_w7` | Design weight - wave 7 | `Numeric(Double)` | `%10.0g` |
| `cchw_w7` | Calibrated cross-sectional household weight - wave 7 | `Numeric(Double)` | `%10.0g` |
| `cciw_w7` | Calibrated cross-sectional individual weight - wave 7 | `Numeric(Double)` | `%10.0g` |
| `cchw_w7_SHL` | Calibrated (cross-sectional) household weight - SHARELIFE interview only | `Numeric(Double)` | `%10.0g` |
| `cciw_w7_SHL` | Calibrated (cross-sectional) individual weight - SHARELIFE interview only | `Numeric(Double)` | `%10.0g` |
| `cchw_w7_REG` | Calibrated (cross-sectional) household weight - regular interview only | `Numeric(Double)` | `%10.0g` |
| `cciw_w7_REG` | Calibrated (cross-sectional) individual weight - regular interview only | `Numeric(Double)` | `%10.0g` |
| `subsample` | Indicator for country-specific subsample | `Str(6)` | `%9s` |
| `stratum1` | Indicator for primary stratum (if any) | `Str(10)` | `%10s` |
| `stratum2` | Indicator for secondary stratum (if any) | `Str(6)` | `%9s` |
| `psu` | Primary sampling unit | `Str(11)` | `%11s` |
| `ssu` | Secondary sampling unit (if any) | `Str(13)` | `%13s` |


## Auxiliary Datasets

### `interviewer_survey` - Interviewer Survey

- Dataset: `sharew7_rel9-0-0_interviewer_survey.dta`
- Read with: `ps.read_share_module("interviewer_survey", wave=7)`
- Rows: 1,118
- Variables: 98
- Key hint: `intid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `intid` | Interviewer ID (wave specific) | `Str(10)` | `%10s` |
| `intidwX` | Interviewer ID (fix across waves) | `Str(11)` | `%11s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `v1` | Start working as an interviewer | `Numeric(Int)` | `%10.0g` |
| `v4` | No. of waves working for SHARE | `Numeric(Byte)` | `%10.0g` |
| `v5` | Working hours per week | `Numeric(Byte)` | `%10.0g` |
| `v40` | Interviewing radius in km | `Numeric(Byte)` | `%13.0g` |
| `v6_1` | Payment | `Numeric(Byte)` | `%23.0g` |
| `v6_2` | Interesting work | `Numeric(Byte)` | `%23.0g` |
| `v6_3` | Opportunity to interact with people | `Numeric(Byte)` | `%23.0g` |
| `v6_4` | Gaining insight into other people's social circumstances | `Numeric(Byte)` | `%23.0g` |
| `v6_5` | Involvement in scientific research | `Numeric(Byte)` | `%23.0g` |
| `v6_6` | Involvement in research that serves society | `Numeric(Byte)` | `%23.0g` |
| `v6_7` | Flexible working hours | `Numeric(Byte)` | `%23.0g` |
| `v6a` | Other reasons | `Numeric(Byte)` | `%10.0g` |
| `v7_1` | Contributing to research | `Numeric(Byte)` | `%20.0g` |
| `v7_2` | Taking part in order to serve society | `Numeric(Byte)` | `%20.0g` |
| `v7_3` | Opportunity to interact with someone | `Numeric(Byte)` | `%20.0g` |
| `v7_4` | Expressing their opinions | `Numeric(Byte)` | `%20.0g` |
| `v7_5` | Inability to say no to the interviewer | `Numeric(Byte)` | `%20.0g` |
| `v7_6` | Receiving incentives/gifts | `Numeric(Byte)` | `%20.0g` |
| `v7a` | Other reasons | `Numeric(Byte)` | `%10.0g` |
| `v8_1` | Explain question | `Numeric(Byte)` | `%13.0g` |
| `v8_2` | Reread question | `Numeric(Byte)` | `%13.0g` |
| `v8_3` | Shorten long question | `Numeric(Byte)` | `%13.0g` |
| `v8_4` | Speak slowly | `Numeric(Byte)` | `%13.0g` |
| `v8_5` | Speak faster | `Numeric(Byte)` | `%13.0g` |
| `v8_6` | Known from interview - Complete answers | `Numeric(Byte)` | `%13.0g` |
| `v8_7` | Remember -  Complete answers | `Numeric(Byte)` | `%13.0g` |
| `v8_8` | Speak in regional dialect | `Numeric(Byte)` | `%13.0g` |
| `v8_9` | Stick to interviewer instructions | `Numeric(Byte)` | `%13.0g` |
| `v9_1` | Persuade to participate | `Numeric(Byte)` | `%20.0g` |
| `v9_2` | Enough effort | `Numeric(Byte)` | `%20.0g` |
| `v9_3` | Respect privacy | `Numeric(Byte)` | `%20.0g` |
| `v9_4` | Accept refusal | `Numeric(Byte)` | `%20.0g` |
| `v9_5` | Emphasize voluntary nature | `Numeric(Byte)` | `%20.0g` |
| `v9_6` | Not contact repeatedly | `Numeric(Byte)` | `%20.0g` |
| `v9_7` | Right time | `Numeric(Byte)` | `%20.0g` |
| `v9_8` | No reliable answers | `Numeric(Byte)` | `%20.0g` |
| `v41_1` | Too busy | `Numeric(Byte)` | `%14.0g` |
| `v41_2` | Not interested | `Numeric(Byte)` | `%14.0g` |
| `v41_3` | Privacy concerns | `Numeric(Byte)` | `%14.0g` |
| `v41_4` | Fear | `Numeric(Byte)` | `%14.0g` |
| `v41_5` | Too complex | `Numeric(Byte)` | `%14.0g` |
| `v10` | Trust people | `Numeric(Byte)` | `%30.0g` |
| `v11_1` | First impression right | `Numeric(Byte)` | `%13.0g` |
| `v11_2` | Not confident of judgements | `Numeric(Byte)` | `%13.0g` |
| `v11_3` | Know why like things | `Numeric(Byte)` | `%13.0g` |
| `v11_4` | Received too much change | `Numeric(Byte)` | `%13.0g` |
| `v11_5` | Honest to other people | `Numeric(Byte)` | `%13.0g` |
| `v11_6` | Taken advantage | `Numeric(Byte)` | `%13.0g` |
| `v14` | Safety of personal data | `Numeric(Byte)` | `%23.0g` |
| `v42` | Intimacy of survey | `Numeric(Byte)` | `%20.0g` |
| `v16_1` | Income tax assessment | `Numeric(Byte)` | `%17.0g` |
| `v16_2` | Debts and loans | `Numeric(Byte)` | `%17.0g` |
| `v16_3` | Employment history | `Numeric(Byte)` | `%17.0g` |
| `v16_4` | Medical data | `Numeric(Byte)` | `%17.0g` |
| `v16_5` | Health insurance | `Numeric(Byte)` | `%17.0g` |
| `v16_6` | Social security benefits | `Numeric(Byte)` | `%17.0g` |
| `v16_7` | School files | `Numeric(Byte)` | `%17.0g` |
| `v17` | Percentage consent to linkage request | `Numeric(Byte)` | `%10.0g` |
| `v18` | Own consent to linkage | `Numeric(Byte)` | `%10.0g` |
| `v19` | Linkage asked before | `Numeric(Byte)` | `%10.0g` |
| `v20` | Percentage information about income | `Numeric(Byte)` | `%10.0g` |
| `v21` | Gender | `Numeric(Byte)` | `%10.0g` |
| `v22` | Year of birth | `Numeric(Int)` | `%10.0g` |
| `v23` | Social networks | `Numeric(Byte)` | `%10.0g` |
| `v43_1` | Difficult situations | `Numeric(Byte)` | `%17.0g` |
| `v43_2` | Most problems | `Numeric(Byte)` | `%17.0g` |
| `v43_3` | Challenging and complex tasks | `Numeric(Byte)` | `%17.0g` |
| `v25_1` | Voluntary or charity work | `Numeric(Byte)` | `%21.0g` |
| `v25_2` | Political or community-related organization | `Numeric(Byte)` | `%21.0g` |
| `v25_3` | Sport, social or other kind of club | `Numeric(Byte)` | `%21.0g` |
| `v26` | Political inclination | `Numeric(Byte)` | `%10.0g` |
| `v27` | Health | `Numeric(Byte)` | `%12.0g` |
| `v36_1` | Being Reserved | `Numeric(Byte)` | `%17.0g` |
| `v36_2` | Trusting | `Numeric(Byte)` | `%17.0g` |
| `v36_3` | Being Lazy | `Numeric(Byte)` | `%17.0g` |
| `v36_4` | Handling stress well | `Numeric(Byte)` | `%17.0g` |
| `v36_5` | Having few artistic interests | `Numeric(Byte)` | `%17.0g` |
| `v36_6` | Being sociable | `Numeric(Byte)` | `%17.0g` |
| `v36_7` | Finding fault with others | `Numeric(Byte)` | `%17.0g` |
| `v36_8` | Doing a thorough job | `Numeric(Byte)` | `%17.0g` |
| `v36_9` | Getting nervous easily | `Numeric(Byte)` | `%17.0g` |
| `v36_10` | Having an active imagination | `Numeric(Byte)` | `%17.0g` |
| `v36_11` | Being kind to almost everyone | `Numeric(Byte)` | `%17.0g` |
| `v30` | East/West germany | `Numeric(Byte)` | `%10.0g` |
| `v31_1` | Interviewer is only job | `Numeric(Byte)` | `%12.0g` |
| `v31_2` | Full-time employed | `Numeric(Byte)` | `%12.0g` |
| `v31_3` | Part-time employed or other mini job | `Numeric(Byte)` | `%12.0g` |
| `v31_4` | Vocational training or occupational re-training | `Numeric(Byte)` | `%12.0g` |
| `v31_5` | Unemployed | `Numeric(Byte)` | `%12.0g` |
| `v31_6` | Retired | `Numeric(Byte)` | `%12.0g` |
| `v31_7` | Other | `Numeric(Byte)` | `%12.0g` |
| `v32` | Level of education | `Numeric(Byte)` | `%32.0g` |
| `v33` | Household size | `Numeric(Byte)` | `%10.0g` |
| `v34` | Household income in national currency | `Numeric(Long)` | `%10.0g` |
| `v44` | Living area | `Numeric(Byte)` | `%38.0g` |
