---
icon: lucide/list-tree
---

# Wave 1 Variable Dictionary

This page is generated from the local SHARE wave 1 release `9-0-0` Stata files.

It covers 32 datasets and 2,447 variable entries for the files currently available in `data/`.

[Back to variable dictionary](./index.md)

## Overview

| Module | Category | Meaning | Key | Variables | Rows | File |
| --- | --- | --- | --- | --- | --- | --- |
| `ac` | core | Activities | `mergeid` | 90 | 30,416 | `sharew1_rel9-0-0_ac.dta` |
| `as` | core | Assets | `mergeid` | 127 | 30,416 | `sharew1_rel9-0-0_as.dta` |
| `br` | core | Behavioural Risks | `mergeid` | 23 | 30,416 | `sharew1_rel9-0-0_br.dta` |
| `cf` | core | Cognitive Function | `mergeid` | 24 | 30,416 | `sharew1_rel9-0-0_cf.dta` |
| `ch` | core | Children | `mergeid` | 223 | 30,416 | `sharew1_rel9-0-0_ch.dta` |
| `co` | core | Consumption | `mergeid` | 14 | 30,416 | `sharew1_rel9-0-0_co.dta` |
| `cv_r` | core | Coverscreen on individual level | `mergeid` | 30 | 43,961 | `sharew1_rel9-0-0_cv_r.dta` |
| `dn` | core | Demographics | `mergeid` | 75 | 30,416 | `sharew1_rel9-0-0_dn.dta` |
| `ep` | core | Employment and Pensions | `mergeid` | 360 | 30,416 | `sharew1_rel9-0-0_ep.dta` |
| `ex` | core | Expectations | `mergeid` | 34 | 30,416 | `sharew1_rel9-0-0_ex.dta` |
| `ft` | core | Financial Transfers | `mergeid` | 64 | 30,416 | `sharew1_rel9-0-0_ft.dta` |
| `gs` | core | Grip Strength | `mergeid` | 13 | 30,416 | `sharew1_rel9-0-0_gs.dta` |
| `hc` | core | Health Care | `mergeid` | 157 | 30,416 | `sharew1_rel9-0-0_hc.dta` |
| `hh` | core | Household Income | `mergeid` | 20 | 30,416 | `sharew1_rel9-0-0_hh.dta` |
| `ho` | core | Housing | `mergeid` | 68 | 30,416 | `sharew1_rel9-0-0_ho.dta` |
| `iv` | core | Interviewer Observations | `mergeid` | 42 | 30,416 | `sharew1_rel9-0-0_iv.dta` |
| `mh` | core | Mental Health | `mergeid` | 26 | 30,416 | `sharew1_rel9-0-0_mh.dta` |
| `ph` | core | Physical Health | `mergeid` | 137 | 30,416 | `sharew1_rel9-0-0_ph.dta` |
| `sp` | core | Social Support | `mergeid` | 169 | 30,416 | `sharew1_rel9-0-0_sp.dta` |
| `ws` | core | Walking Speed | `mergeid` | 19 | 30,416 | `sharew1_rel9-0-0_ws.dta` |
| `dropoff` | special | Paper-and-pencil drop-off | `mergeid` | 216 | 20,190 | `sharew1_rel9-0-0_dropoff.dta` |
| `technical_variables` | special | Technical variables | `mergeid` | 14 | 30,416 | `sharew1_rel9-0-0_technical_variables.dta` |
| `vignettes` | special | Vignettes | `mergeid` | 41 | 4,512 | `sharew1_rel9-0-0_vignettes.dta` |
| `gv_exrates` | generated | Exchange rates and PPP variables | `country` | 76 | 29 | `sharew1_rel9-0-0_gv_exrates.dta` |
| `gv_grossnet` | generated | Net income derived from gross income | `mergeid` | 20 | 30,416 | `sharew1_rel9-0-0_gv_grossnet.dta` |
| `gv_health` | generated | Generated health indicators | `mergeid` | 47 | 30,416 | `sharew1_rel9-0-0_gv_health.dta` |
| `gv_housing` | generated | Housing generated variables | `mergeid` | 11 | 30,416 | `sharew1_rel9-0-0_gv_housing.dta` |
| `gv_imputations` | generated | Multiple imputations | `mergeid` | 224 | 152,080 | `sharew1_rel9-0-0_gv_imputations.dta` |
| `gv_isced` | generated | ISCED education recodes | `mergeid` | 20 | 30,416 | `sharew1_rel9-0-0_gv_isced.dta` |
| `gv_isco` | generated | Occupation and industry coding | `mergeid` | 24 | 30,416 | `sharew1_rel9-0-0_gv_isco.dta` |
| `gv_weights` | generated | Cross-sectional weights | `mergeid` | 14 | 30,416 | `sharew1_rel9-0-0_gv_weights.dta` |
| `ep_ilextra` | auxiliary | Israel EP add-on | `mergeid` | 25 | 575 | `sharew1_rel9-0-0_ep_ilextra.dta` |

## Core Interview Modules

### `ac` - Activities

- Dataset: `sharew1_rel9-0-0_ac.dta`
- Read with: `ps.read_share_module("ac", wave=1)`
- Rows: 30,416
- Variables: 90
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ac002d1` | Activities last month: voluntary or charity work | `Numeric(Byte)` | `%12.0g` |
| `ac002d2` | Activities last month: cared for a sick or disabled adult | `Numeric(Byte)` | `%12.0g` |
| `ac002d3` | Activities last month: provided help to family, friends or neighbors | `Numeric(Byte)` | `%12.0g` |
| `ac002d4` | Activities last month: attended educational or training course | `Numeric(Byte)` | `%12.0g` |
| `ac002d5` | Activities last month: gone to sport, social or other kind of club | `Numeric(Byte)` | `%12.0g` |
| `ac002d6` | Activities last month: taken part in religious organization | `Numeric(Byte)` | `%12.0g` |
| `ac002d7` | Activities last month: taken part in political or community organization | `Numeric(Byte)` | `%12.0g` |
| `ac002dno` | Activities last month: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac003_1` | How often in last 4 weeks: voluntary/charity work | `Numeric(Byte)` | `%17.0f` |
| `ac003_2` | How often in last 4 weeks: cared for sick/disabled adult | `Numeric(Byte)` | `%17.0f` |
| `ac003_3` | How often in last 4 weeks: provided help to family/friends/neighbors | `Numeric(Byte)` | `%17.0f` |
| `ac003_4` | How often in last 4 weeks: attended educational/training course | `Numeric(Byte)` | `%17.0f` |
| `ac003_5` | How often in last 4 weeks: sport/social/other club | `Numeric(Byte)` | `%17.0f` |
| `ac003_6` | How often in last 4 weeks: taken part religious organization | `Numeric(Byte)` | `%17.0f` |
| `ac003_7` | How often in last 4 weeks: taken part political/community-rel. org. | `Numeric(Byte)` | `%17.0f` |
| `ac004d1_1` | Voluntary or charity work: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `ac004d1_2` | Cared for sick or disabled adult: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `ac004d1_3` | Help to family, friends or neighbors: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `ac004d1_4` | Educational or training course: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `ac004d1_5` | Sport, social or other club: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `ac004d1_6` | Religious org.: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `ac004d1_7` | Political or community org.: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `ac004d2_1` | Voluntary or charity work: to contribute something useful | `Numeric(Byte)` | `%12.0g` |
| `ac004d2_2` | Cared for sick or disabled adult: to contribute something useful | `Numeric(Byte)` | `%12.0g` |
| `ac004d2_3` | Help to family, friends or neighbors: to contribute something useful | `Numeric(Byte)` | `%12.0g` |
| `ac004d2_4` | Educational or training course: to contribute something useful | `Numeric(Byte)` | `%12.0g` |
| `ac004d2_5` | Sport, social or other club: to contribute something useful | `Numeric(Byte)` | `%12.0g` |
| `ac004d2_6` | Religious org.: to contribute something useful | `Numeric(Byte)` | `%12.0g` |
| `ac004d2_7` | Political or community org.: to contribute something useful | `Numeric(Byte)` | `%12.0g` |
| `ac004d3_1` | Voluntary or charity work: for personal achievement | `Numeric(Byte)` | `%12.0g` |
| `ac004d3_2` | Cared for sick or disabled adult: for personal achievement | `Numeric(Byte)` | `%12.0g` |
| `ac004d3_3` | Help to family, friends or neighbors: for personal achievement | `Numeric(Byte)` | `%12.0g` |
| `ac004d3_4` | Educational or training course: for personal achievement | `Numeric(Byte)` | `%12.0g` |
| `ac004d3_5` | Sport, social or other club: for personal achievement | `Numeric(Byte)` | `%12.0g` |
| `ac004d3_6` | Religious org.: for personal achievement | `Numeric(Byte)` | `%12.0g` |
| `ac004d3_7` | Political or community org.: for personal achievement | `Numeric(Byte)` | `%12.0g` |
| `ac004d4_1` | Voluntary or charity work: because I am needed | `Numeric(Byte)` | `%12.0g` |
| `ac004d4_2` | Cared for sick or disabled adult: because I am needed | `Numeric(Byte)` | `%12.0g` |
| `ac004d4_3` | Help to family, friends or neighbors: because I am needed | `Numeric(Byte)` | `%12.0g` |
| `ac004d4_4` | Educational or training course: because I am needed | `Numeric(Byte)` | `%12.0g` |
| `ac004d4_5` | Sport, social or other club: because I am needed | `Numeric(Byte)` | `%12.0g` |
| `ac004d4_6` | Religious org.: because I am needed | `Numeric(Byte)` | `%12.0g` |
| `ac004d4_7` | Political or community org.: because I am needed | `Numeric(Byte)` | `%12.0g` |
| `ac004d5_1` | Voluntary or charity work: to earn money | `Numeric(Byte)` | `%12.0g` |
| `ac004d5_2` | Cared for sick or disabled adult: to earn money | `Numeric(Byte)` | `%12.0g` |
| `ac004d5_3` | Help to family, friends or neighbors: to earn money | `Numeric(Byte)` | `%12.0g` |
| `ac004d5_4` | Educational or training course: to earn money | `Numeric(Byte)` | `%12.0g` |
| `ac004d5_5` | Sport, social or other club: to earn money | `Numeric(Byte)` | `%12.0g` |
| `ac004d5_6` | Religious org.: to earn money | `Numeric(Byte)` | `%12.0g` |
| `ac004d5_7` | Political or community org.: to earn money | `Numeric(Byte)` | `%12.0g` |
| `ac004d6_1` | Voluntary or charity work: because I enjoy it | `Numeric(Byte)` | `%12.0g` |
| `ac004d6_2` | Cared for sick or disabled adult: because I enjoy it | `Numeric(Byte)` | `%12.0g` |
| `ac004d6_3` | Help to family, friends or neighbors: because I enjoy it | `Numeric(Byte)` | `%12.0g` |
| `ac004d6_4` | Educational or training course: because I enjoy it | `Numeric(Byte)` | `%12.0g` |
| `ac004d6_5` | Sport, social or other club: because I enjoy it | `Numeric(Byte)` | `%12.0g` |
| `ac004d6_6` | Religious org.: because I enjoy it | `Numeric(Byte)` | `%12.0g` |
| `ac004d6_7` | Political or community org.: because I enjoy it | `Numeric(Byte)` | `%12.0g` |
| `ac004d7_1` | Voluntary or charity work: to use skills or to keep fit | `Numeric(Byte)` | `%12.0g` |
| `ac004d7_2` | Cared for sick or disabled adult: to use skills or to keep fit | `Numeric(Byte)` | `%12.0g` |
| `ac004d7_3` | Help to family, friends or neighbors: to use skills or to keep fit | `Numeric(Byte)` | `%12.0g` |
| `ac004d7_4` | Educational or training course: to use skills or to keep fit | `Numeric(Byte)` | `%12.0g` |
| `ac004d7_5` | Sport, social or other club: to use skills or to keep fit | `Numeric(Byte)` | `%12.0g` |
| `ac004d7_6` | Religious org.: to use skills or to keep fit | `Numeric(Byte)` | `%12.0g` |
| `ac004d7_7` | Political or community org.: to use skills or to keep fit | `Numeric(Byte)` | `%12.0g` |
| `ac004d8_1` | Voluntary or charity work: feel obligated to do it | `Numeric(Byte)` | `%12.0g` |
| `ac004d8_2` | Cared for sick or disabled adult: feel obligated to do it | `Numeric(Byte)` | `%12.0g` |
| `ac004d8_3` | Help to family, friends or neighbors: feel obligated to do it | `Numeric(Byte)` | `%12.0g` |
| `ac004d8_4` | Educational or training course: feel obligated to do it | `Numeric(Byte)` | `%12.0g` |
| `ac004d8_5` | Sport, social or other club: feel obligated to do it | `Numeric(Byte)` | `%12.0g` |
| `ac004d8_6` | Religious org.: feel obligated to do it | `Numeric(Byte)` | `%12.0g` |
| `ac004d8_7` | Political or community org.: feel obligated to do it | `Numeric(Byte)` | `%12.0g` |
| `ac004dno_1` | Voluntary or charity work: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac004dno_2` | Cared for sick or disabled adult: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac004dno_3` | Help to family, friends or neighbors: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac004dno_4` | Educational or training course: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac004dno_5` | Sport, social or other club: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac004dno_6` | Religious org.: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac004dno_7` | Political or community org.: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac006_1` | Fully satisfied with what achieved so far | `Numeric(Byte)` | `%26.0f` |
| `ac006_2` | Fully satisfied with what achieved so far | `Numeric(Byte)` | `%26.0f` |
| `ac006_3` | Fully satisfied with what achieved so far | `Numeric(Byte)` | `%26.0f` |
| `ac007_1` | Received adequate appreciation from others | `Numeric(Byte)` | `%26.0f` |
| `ac007_2` | Received adequate appreciation from others | `Numeric(Byte)` | `%26.0f` |
| `ac007_3` | Received adequate appreciation from others | `Numeric(Byte)` | `%26.0f` |

### `as` - Assets

- Dataset: `sharew1_rel9-0-0_as.dta`
- Read with: `ps.read_share_module("as", wave=1)`
- Rows: 30,416
- Variables: 127
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `as002d1` | Saving/investments: bank accounts, transaction accounts or saving accounts | `Numeric(Byte)` | `%12.0g` |
| `as002d2` | Saving/investments: government or corporate bonds | `Numeric(Byte)` | `%12.0g` |
| `as002d3` | Saving/investments: stock or shares | `Numeric(Byte)` | `%12.0g` |
| `as002d4` | Saving/investments: mutual funds or managed investment accounts | `Numeric(Byte)` | `%12.0g` |
| `as002d5` | Saving/investments: individual retirements accounts | `Numeric(Byte)` | `%12.0g` |
| `as002d6` | Saving/investments: contractual saving for house | `Numeric(Byte)` | `%12.0g` |
| `as002d7` | Saving/investments: life insurance | `Numeric(Byte)` | `%12.0g` |
| `as002d8` | Saving/investments: private pension precaution, state-run supported (ATonly) | `Numeric(Byte)` | `%12.0g` |
| `as002dno` | Saving/investments: none of these | `Numeric(Byte)` | `%12.0g` |
| `as003e` | Amount bank account | `Numeric(Double)` | `%222.0g` |
| `as003ub` | Amount bank account ub | `Numeric(Byte)` | `%32.0f` |
| `as003v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `as003v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `as003v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `as005e` | Interest from bank account | `Numeric(Double)` | `%222.0g` |
| `as005ub` | Interest from bank account ub | `Numeric(Byte)` | `%32.0f` |
| `as005v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `as005v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `as005v3` | Bracket value 3 | `Numeric(Float)` | `%19.0f` |
| `as007e` | Amount in bonds | `Numeric(Double)` | `%222.0g` |
| `as007ub` | Amount in bonds ub | `Numeric(Byte)` | `%32.0f` |
| `as007v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `as007v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `as007v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `as009e` | Interest from bonds | `Numeric(Double)` | `%222.0g` |
| `as009ub` | Interest from bonds ub | `Numeric(Byte)` | `%32.0f` |
| `as009v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `as009v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `as009v3` | Bracket value 3 | `Numeric(Float)` | `%19.0f` |
| `as011e` | Amount in stocks | `Numeric(Double)` | `%222.0g` |
| `as011ub` | Amount in stocks ub | `Numeric(Byte)` | `%32.0f` |
| `as011v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `as011v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `as011v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `as015e` | Dividend from stocks | `Numeric(Double)` | `%222.0g` |
| `as015ub` | Dividend from stocks ub | `Numeric(Byte)` | `%32.0f` |
| `as015v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `as015v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `as015v3` | Bracket value 3 | `Numeric(Float)` | `%19.0f` |
| `as017e` | Amount in mutual funds | `Numeric(Double)` | `%222.0g` |
| `as017ub` | Amount in mutual funds ub | `Numeric(Byte)` | `%32.0f` |
| `as017v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `as017v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `as017v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `as019_` | Mutual funds mostly stocks or bonds | `Numeric(Byte)` | `%29.0f` |
| `as020_` | Who has individual retirement accounts | `Numeric(Byte)` | `%25.0f` |
| `as021e` | Amount individual retirement accounts | `Numeric(Double)` | `%222.0g` |
| `as021ub` | Amount individual retirement accounts ub | `Numeric(Byte)` | `%32.0f` |
| `as021v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `as021v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `as021v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `as023_` | Individual retirement accounts mostly in stocks or bonds | `Numeric(Byte)` | `%48.0f` |
| `as024e` | Partner amount individual retirement accounts | `Numeric(Double)` | `%222.0g` |
| `as024ub` | Partner amount individual retirement accounts ub | `Numeric(Byte)` | `%32.0f` |
| `as024v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `as024v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `as024v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `as026_` | Partner individual retirement accounts mostly in stocks or bonds | `Numeric(Byte)` | `%54.0f` |
| `as027e` | Amount contractual saving for housing | `Numeric(Double)` | `%222.0g` |
| `as027ub` | Amount contractual saving for housing ub | `Numeric(Byte)` | `%32.0f` |
| `as027v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `as027v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `as027v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `as029_` | Life insurance policies term or whole life | `Numeric(Byte)` | `%19.0f` |
| `as030e` | Face value of whole life policies | `Numeric(Double)` | `%222.0g` |
| `as030ub` | Face value of whole life policies ub | `Numeric(Byte)` | `%32.0f` |
| `as030v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `as030v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `as030v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `as032e_1` | Amount dependents get from life insurace policies | `Numeric(Double)` | `%222.0g` |
| `as032ub_1` | Amount dependents get from life insurace policies ub | `Numeric(Byte)` | `%32.0f` |
| `as032e_2` | Amount dependents get from term policies | `Numeric(Double)` | `%222.0g` |
| `as032ub_2` | Amount dependents get from term policies ub | `Numeric(Byte)` | `%32.0f` |
| `as032v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `as032v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `as032v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `as034e_1` | Paid on life insurance policies | `Numeric(Double)` | `%222.0g` |
| `as034ub_1` | Paid on life insurance policies ub | `Numeric(Byte)` | `%32.0f` |
| `as034e_2` | Paid on term policies | `Numeric(Double)` | `%222.0g` |
| `as034ub_2` | Paid on term policies ub | `Numeric(Byte)` | `%32.0f` |
| `as034v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `as034v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `as034v3` | Bracket value 3 | `Numeric(Float)` | `%19.0f` |
| `as040_` | How often spent time on managing savings | `Numeric(Byte)` | `%34.0f` |
| `as041_` | Own firm company business | `Numeric(Byte)` | `%10.0f` |
| `as042e` | Amount selling firm | `Numeric(Double)` | `%222.0g` |
| `as042ub` | Amount selling firm ub | `Numeric(Byte)` | `%32.0f` |
| `as042v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `as042v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `as042v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `as044_` | Percentage share firm owned | `Numeric(Double)` | `%18.2f` |
| `as044ub` | Percentage share firm owned ub | `Numeric(Byte)` | `%32.0f` |
| `as044v1` | Bracket value 1 | `Numeric(Byte)` | `%19.0f` |
| `as044v2` | Bracket value 2 | `Numeric(Byte)` | `%19.0f` |
| `as044v3` | Bracket value 3 | `Numeric(Byte)` | `%19.0f` |
| `as049_` | Number of cars | `Numeric(Byte)` | `%10.0f` |
| `as051e` | Amount selling cars | `Numeric(Double)` | `%222.0g` |
| `as051ub` | Amount selling cars ub | `Numeric(Byte)` | `%32.0f` |
| `as051v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `as051v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `as051v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `as054d1` | Owe money: debt on cars and other vehicles (vans/motorcycles/boats, etc.) | `Numeric(Byte)` | `%12.0g` |
| `as054d2` | Owe money: overdue bills (phone, electricity, heating, rent) | `Numeric(Byte)` | `%12.0g` |
| `as054d3` | Owe money: debt on credit cards/store cards | `Numeric(Byte)` | `%12.0g` |
| `as054d4` | Owe money: loans (from bank, building society or other financial institution) | `Numeric(Byte)` | `%12.0g` |
| `as054d5` | Owe money: debts to relatives or friends | `Numeric(Byte)` | `%12.0g` |
| `as054d6` | Owe money: student loans | `Numeric(Byte)` | `%12.0g` |
| `as054dno` | Owe money: none of these | `Numeric(Byte)` | `%12.0g` |
| `as054dot` | Owe money: other | `Numeric(Byte)` | `%12.0g` |
| `as055e` | Amount owing money in total | `Numeric(Double)` | `%222.0g` |
| `as055ub` | Amount owing money in total ub | `Numeric(Byte)` | `%32.0f` |
| `as055v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `as055v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `as055v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `as057_` | Who answered the question in as | `Numeric(Byte)` | `%20.0f` |
| `as058e` | Interest or dividend on mutual funds | `Numeric(Double)` | `%222.0g` |
| `as058ub` | Interest or dividend on mutual funds ub | `Numeric(Byte)` | `%32.0f` |
| `as058v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `as058v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `as058v3` | Bracket value 3 | `Numeric(Float)` | `%19.0f` |

### `br` - Behavioural Risks

- Dataset: `sharew1_rel9-0-0_br.dta`
- Read with: `ps.read_share_module("br", wave=1)`
- Rows: 30,416
- Variables: 23
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `br001_` | Ever smoked daily | `Numeric(Byte)` | `%10.0f` |
| `br002_` | Smoke at the present time | `Numeric(Byte)` | `%25.0f` |
| `br003_` | How many years smoked | `Numeric(Byte)` | `%10.0f` |
| `br004_` | Age stopped smoking | `Numeric(Byte)` | `%10.0f` |
| `br005d1` | Do or did smoke: cigarettes | `Numeric(Byte)` | `%12.0g` |
| `br005d2` | Do or did smoke: pipe | `Numeric(Byte)` | `%12.0g` |
| `br005d3` | Do or did smoke: cigars or cigarillos | `Numeric(Byte)` | `%12.0g` |
| `br006_` | Average amount of cigarettes per day | `Numeric(Int)` | `%10.0f` |
| `br007_` | Average amount of pipes per day | `Numeric(Byte)` | `%10.0f` |
| `br008_` | Average amount of cigars per day | `Numeric(Byte)` | `%10.0f` |
| `br010_` | Days a week consumed alcohol last 6 months | `Numeric(Byte)` | `%42.0f` |
| `br011_` | Freq more than 2 glasses beer in a day | `Numeric(Byte)` | `%42.0f` |
| `br012_` | Freq more than 2 glasses wine in a day | `Numeric(Byte)` | `%42.0f` |
| `br013_` | Freq more than 2 hard liquor in a day | `Numeric(Byte)` | `%42.0f` |
| `br015_` | Sports or activities that are vigorous | `Numeric(Byte)` | `%26.0f` |
| `br016_` | Activities requiring a moderate level of energy | `Numeric(Byte)` | `%26.0f` |
| `br017_` | Who answered the questions in br | `Numeric(Byte)` | `%20.0f` |

### `cf` - Cognitive Function

- Dataset: `sharew1_rel9-0-0_cf.dta`
- Read with: `ps.read_share_module("cf", wave=1)`
- Rows: 30,416
- Variables: 24
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `cf001_` | Self-rated reading skills | `Numeric(Byte)` | `%13.0f` |
| `cf002_` | Self-rated writing skills | `Numeric(Byte)` | `%13.0f` |
| `cf003_` | Date: day of month | `Numeric(Byte)` | `%47.0f` |
| `cf004_` | Date: month | `Numeric(Byte)` | `%47.0f` |
| `cf005_` | Date: year | `Numeric(Byte)` | `%45.0f` |
| `cf006_` | Date: day of the week | `Numeric(Byte)` | `%55.0f` |
| `cf008tot` | Ten words list learning first trial total | `Numeric(Byte)` | `%9.0g` |
| `cf010_` | Verbal fluency score: number of animals | `Numeric(Byte)` | `%10.0f` |
| `cf012_` | Numeracy: chance disease 10% of 1000 | `Numeric(Byte)` | `%19.0f` |
| `cf013_` | Numeracy: half price | `Numeric(Byte)` | `%19.0f` |
| `cf014_` | Numeracy: 6000 is two-thirds what is total price | `Numeric(Byte)` | `%21.0f` |
| `cf015_` | Numeracy: amount in the savings account | `Numeric(Byte)` | `%20.0f` |
| `cf016tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `cf017_` | Contextual factors during the cognitive function test | `Numeric(Byte)` | `%10.0f` |
| `cf018d1` | Who present during cf: respondent alone | `Numeric(Byte)` | `%12.0g` |
| `cf018d2` | Who present during cf: partner present | `Numeric(Byte)` | `%12.0g` |
| `cf018d3` | Who present during cf: child(ren) present | `Numeric(Byte)` | `%12.0g` |
| `cf018d4` | Who present during cf: other(s) | `Numeric(Byte)` | `%12.0g` |

### `ch` - Children

- Dataset: `sharew1_rel9-0-0_ch.dta`
- Read with: `ps.read_share_module("ch", wave=1)`
- Rows: 30,416
- Variables: 223
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
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
| `childid_18` | Child identifier (fix across modules and waves): Child 18 | `Str(1)` | `%9s` |
| `childid_19` | Child identifier (fix across modules and waves): Child 19 | `Str(1)` | `%9s` |
| `childid_20` | Child identifier (fix across modules and waves): Child 20 | `Str(1)` | `%9s` |
| `ch001_` | Number of children | `Numeric(Byte)` | `%10.0f` |
| `ch002_` | Natural child(ren) | `Numeric(Byte)` | `%10.0f` |
| `ch005_1` | Child 1 gender | `Numeric(Long)` | `%10.0f` |
| `ch005_2` | Child 2 gender | `Numeric(Long)` | `%10.0f` |
| `ch005_3` | Child 3 gender | `Numeric(Long)` | `%10.0f` |
| `ch005_4` | Child 4 gender | `Numeric(Long)` | `%10.0f` |
| `ch005_5` | Child 5 gender | `Numeric(Long)` | `%10.0f` |
| `ch005_6` | Child 6 gender | `Numeric(Long)` | `%10.0f` |
| `ch005_7` | Child 7 gender | `Numeric(Long)` | `%10.0f` |
| `ch005_8` | Child 8 gender | `Numeric(Long)` | `%10.0f` |
| `ch005_9` | Child 9 gender | `Numeric(Long)` | `%10.0f` |
| `ch005_10` | Child 10 gender | `Numeric(Byte)` | `%10.0f` |
| `ch005_11` | Child 11 gender | `Numeric(Byte)` | `%10.0f` |
| `ch005_12` | Child 12 gender | `Numeric(Byte)` | `%10.0f` |
| `ch005_13` | Child 13 gender | `Numeric(Byte)` | `%10.0f` |
| `ch005_14` | Child 14 gender | `Numeric(Byte)` | `%10.0f` |
| `ch005_15` | Child 15 gender | `Numeric(Byte)` | `%10.0f` |
| `ch005_16` | Child 16 gender | `Numeric(Byte)` | `%10.0f` |
| `ch005_17` | Child 17 gender | `Numeric(Byte)` | `%10.0f` |
| `ch005_18` | Child 18 gender | `Numeric(Byte)` | `%10.0f` |
| `ch005_19` | Child 19 gender | `Numeric(Byte)` | `%10.0f` |
| `ch005_20` | Child 20 gender | `Numeric(Byte)` | `%10.0f` |
| `ch006_1` | Child 1 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_2` | Child 2 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_3` | Child 3 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_4` | Child 4 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_5` | Child 5 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_6` | Child 6 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_7` | Child 7 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_8` | Child 8 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_9` | Child 9 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_10` | Child 10 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_11` | Child 11 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_12` | Child 12 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_13` | Child 13 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_14` | Child 14 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_15` | Child 15 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_16` | Child 16 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_17` | Child 17 year of birth | `Numeric(Int)` | `%10.0f` |
| `ch006_18` | Child 18 year of birth | `Numeric(Byte)` | `%10.0f` |
| `ch006_19` | Child 19 year of birth | `Numeric(Byte)` | `%10.0f` |
| `ch006_20` | Child 20 year of birth | `Numeric(Byte)` | `%10.0f` |
| `ch007_1` | Child 1 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_2` | Child 2 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_3` | Child 3 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_4` | Child 4 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_5` | Child 5 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_6` | Child 6 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_7` | Child 7 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_8` | Child 8 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_9` | Child 9 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_10` | Child 10 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_11` | Child 11 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_12` | Child 12 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_13` | Child 13 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_14` | Child 14 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_15` | Child 15 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_16` | Child 16 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_17` | Child 17 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_18` | Child 18 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_19` | Child 19 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch007_20` | Child 20 where does child live | `Numeric(Byte)` | `%48.0f` |
| `ch008c_1` | Child 1 which country - coded | `Numeric(Int)` | `%46.0g` |
| `ch008c_2` | Child 2 which country - coded | `Numeric(Int)` | `%46.0g` |
| `ch008c_3` | Child 3 which country - coded | `Numeric(Int)` | `%46.0g` |
| `ch008c_4` | Child 4 which country - coded | `Numeric(Int)` | `%46.0g` |
| `ch008c_5` | Child 5 which country - coded | `Numeric(Int)` | `%46.0g` |
| `ch008c_6` | Child 6 which country - coded | `Numeric(Int)` | `%46.0g` |
| `ch008c_7` | Child 7 which country - coded | `Numeric(Int)` | `%46.0g` |
| `ch008c_8` | Child 8 which country - coded | `Numeric(Int)` | `%46.0g` |
| `ch008c_9` | Child 9 which country - coded | `Numeric(Int)` | `%46.0g` |
| `ch008c_10` | Child 10 which country - coded | `Numeric(Int)` | `%46.0g` |
| `ch008c_11` | Child 11 which country - coded | `Numeric(Int)` | `%46.0g` |
| `ch008c_12` | Child 12 which country - coded | `Numeric(Int)` | `%46.0g` |
| `ch008c_13` | Child 13 which country - coded | `Numeric(Int)` | `%46.0g` |
| `ch008c_14` | Child 14 which country - coded | `Numeric(Byte)` | `%46.0g` |
| `ch008c_15` | Child 15 which country - coded | `Numeric(Byte)` | `%46.0g` |
| `ch008c_16` | Child 16 which country - coded | `Numeric(Byte)` | `%46.0g` |
| `ch008c_17` | Child 17 which country - coded | `Numeric(Byte)` | `%46.0g` |
| `ch008c_18` | Child 18 which country - coded | `Numeric(Byte)` | `%46.0g` |
| `ch008c_19` | Child 19 which country - coded | `Numeric(Byte)` | `%46.0g` |
| `ch008c_20` | Child 20 which country - coded | `Numeric(Byte)` | `%46.0g` |
| `chselch1` | Child number 1 selected child | `Numeric(Byte)` | `%10.0f` |
| `chselch2` | Child number 2 selected child | `Numeric(Byte)` | `%10.0f` |
| `chselch3` | Child number 3 selected child | `Numeric(Byte)` | `%10.0f` |
| `chselch4` | Child number 4 selected child | `Numeric(Byte)` | `%10.0f` |
| `ch010_1` | Child 1 step adoptive or foster child | `Numeric(Byte)` | `%19.0f` |
| `ch010_2` | Child 2 step adoptive or foster child | `Numeric(Byte)` | `%19.0f` |
| `ch010_3` | Child 3 step adoptive or foster child | `Numeric(Byte)` | `%19.0f` |
| `ch010_4` | Child 4 step adoptive or foster child | `Numeric(Byte)` | `%19.0f` |
| `ch011_1` | Child 1 own child | `Numeric(Byte)` | `%61.0f` |
| `ch011_2` | Child 2 own child | `Numeric(Byte)` | `%61.0f` |
| `ch011_3` | Child 3 own child | `Numeric(Byte)` | `%61.0f` |
| `ch011_4` | Child 4 own child | `Numeric(Byte)` | `%61.0f` |
| `ch012_1` | Child 1 marital status | `Numeric(Byte)` | `%39.0f` |
| `ch012_2` | Child 2 marital status | `Numeric(Byte)` | `%39.0f` |
| `ch012_3` | Child 3 marital status | `Numeric(Byte)` | `%39.0f` |
| `ch012_4` | Child 4 marital status | `Numeric(Byte)` | `%39.0f` |
| `ch013_1` | Child 1 has partner | `Numeric(Byte)` | `%10.0f` |
| `ch013_2` | Child 2 has partner | `Numeric(Byte)` | `%10.0f` |
| `ch013_3` | Child 3 has partner | `Numeric(Byte)` | `%10.0f` |
| `ch013_4` | Child 4 has partner | `Numeric(Byte)` | `%10.0f` |
| `ch014_1` | Child 1 contact with child | `Numeric(Byte)` | `%27.0f` |
| `ch014_2` | Child 2 contact with child | `Numeric(Byte)` | `%27.0f` |
| `ch014_3` | Child 3 contact with child | `Numeric(Byte)` | `%27.0f` |
| `ch014_4` | Child 4 contact with child | `Numeric(Byte)` | `%27.0f` |
| `ch015_1` | Child 1 year moved out | `Numeric(Int)` | `%10.0f` |
| `ch015_2` | Child 2 year moved out | `Numeric(Int)` | `%10.0f` |
| `ch015_3` | Child 3 year moved out | `Numeric(Int)` | `%10.0f` |
| `ch015_4` | Child 4 year moved out | `Numeric(Int)` | `%10.0f` |
| `ch016_1` | Child 1 employment status | `Numeric(Byte)` | `%48.0f` |
| `ch016_2` | Child 2 employment status | `Numeric(Byte)` | `%48.0f` |
| `ch016_3` | Child 3 employment status | `Numeric(Byte)` | `%48.0f` |
| `ch016_4` | Child 4 employment status | `Numeric(Byte)` | `%48.0f` |
| `ch017_1` | Child 1 highest school degree | `Numeric(Byte)` | `%47.0f` |
| `ch017_2` | Child 2 highest school degree | `Numeric(Byte)` | `%47.0f` |
| `ch017_3` | Child 3 highest school degree | `Numeric(Byte)` | `%47.0f` |
| `ch017_4` | Child 4 highest school degree | `Numeric(Byte)` | `%47.0f` |
| `ch018d1_1` | Child 1 further education country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_2` | Child 2 further education country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_3` | Child 3 further education country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d1_4` | Child 4 further education country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_1` | Child 1 further education country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_2` | Child 2 further education country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_3` | Child 3 further education country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d2_4` | Child 4 further education country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_1` | Child 1 further education country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_2` | Child 2 further education country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_3` | Child 3 further education country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d3_4` | Child 4 further education country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_1` | Child 1 further education country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_2` | Child 2 further education country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_3` | Child 3 further education country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d4_4` | Child 4 further education country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_1` | Child 1 further education country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_2` | Child 2 further education country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_3` | Child 3 further education country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d5_4` | Child 4 further education country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_1` | Child 1 further education country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_2` | Child 2 further education country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_3` | Child 3 further education country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d6_4` | Child 4 further education country specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_1` | Child 1 further education country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_2` | Child 2 further education country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_3` | Child 3 further education country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d7_4` | Child 4 further education country specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_1` | Child 1 further education country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_2` | Child 2 further education country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_3` | Child 3 further education country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d8_4` | Child 4 further education country specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_1` | Child 1 further education country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_2` | Child 2 further education country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_3` | Child 3 further education country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d9_4` | Child 4 further education country specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_1` | Child 1 further education country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_2` | Child 2 further education country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_3` | Child 3 further education country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d10_4` | Child 4 further education country specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_1` | Child 1 further education country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_2` | Child 2 further education country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_3` | Child 3 further education country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d11_4` | Child 4 further education country specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_1` | Child 1 further education country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_2` | Child 2 further education country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_3` | Child 3 further education country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d12_4` | Child 4 further education country specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_1` | Child 1 further education country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_2` | Child 2 further education country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_3` | Child 3 further education country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d13_4` | Child 4 further education country specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_1` | Child 1 further education country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_2` | Child 2 further education country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_3` | Child 3 further education country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d14_4` | Child 4 further education country specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_1` | Child 1 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_2` | Child 2 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_3` | Child 3 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018d95_4` | Child 4 further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_1` | Child 1 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_2` | Child 2 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_3` | Child 3 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dno_4` | Child 4 further education: none | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_1` | Child 1 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_2` | Child 2 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_3` | Child 3 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch018dot_4` | Child 4 further education: other | `Numeric(Byte)` | `%12.0g` |
| `ch019_1` | Child 1 number of children | `Numeric(Byte)` | `%10.0f` |
| `ch019_2` | Child 2 number of children | `Numeric(Byte)` | `%10.0f` |
| `ch019_3` | Child 3 number of children | `Numeric(Byte)` | `%10.0f` |
| `ch019_4` | Child 4 number of children | `Numeric(Byte)` | `%10.0f` |
| `ch020_1` | Child 1 year of birth youngest child | `Numeric(Int)` | `%10.0f` |
| `ch020_2` | Child 2 year of birth youngest child | `Numeric(Int)` | `%10.0f` |
| `ch020_3` | Child 3 year of birth youngest child | `Numeric(Int)` | `%10.0f` |
| `ch020_4` | Child 4 year of birth youngest child | `Numeric(Int)` | `%10.0f` |
| `ch021_` | Number of grandchildren | `Numeric(Byte)` | `%10.0f` |
| `ch022_` | Has great-grandchildren | `Numeric(Byte)` | `%10.0f` |
| `ch023_` | Who answered questions in section CH | `Numeric(Byte)` | `%20.0f` |

### `co` - Consumption

- Dataset: `sharew1_rel9-0-0_co.dta`
- Read with: `ps.read_share_module("co", wave=1)`
- Rows: 30,416
- Variables: 14
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `co002e` | Amount spent on food at home | `Numeric(Double)` | `%222.0g` |
| `co003e` | Amount spent on food outside the home | `Numeric(Double)` | `%222.0g` |
| `co004e` | Amount spent on telephones in last month | `Numeric(Double)` | `%222.0g` |
| `co005e` | Amount spent on all goods and services in last month | `Numeric(Double)` | `%222.0g` |
| `co007_` | Is household able to make ends meet | `Numeric(Byte)` | `%28.0f` |
| `co008_` | Situation improvement thinking back one year | `Numeric(Byte)` | `%21.0f` |
| `co009_` | Who answered the questions in co | `Numeric(Byte)` | `%20.0f` |

### `cv_r` - Coverscreen on individual level

- Dataset: `sharew1_rel9-0-0_cv_r.dta`
- Read with: `ps.read_share_module("cv_r", wave=1)`
- Rows: 43,961
- Variables: 30
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `waveid` | Identifier of original wave (person) | `Numeric(Byte)` | `%9.0g` |
| `waveid_hh` | Identifier of original wave (household) | `Numeric(Byte)` | `%9.0g` |
| `firstwave` | First appearance of person in SHARE | `Numeric(Byte)` | `%9.0g` |
| `firstwave_hh` | Wave household was sampled/first participated | `Numeric(Byte)` | `%9.0g` |
| `cvresp` | Coverscreen respondent | `Numeric(Byte)` | `%10.0g` |
| `gender` | Male or female | `Numeric(Byte)` | `%10.0f` |
| `mobirth` | Month of birth | `Numeric(Byte)` | `%10.0f` |
| `yrbirth` | Year of birth | `Numeric(Int)` | `%10.0f` |
| `age2004` | Age in 2004 | `Numeric(Int)` | `%14.0g` |
| `age_int` | Age of respondent at the time of interview | `Numeric(Int)` | `%14.0g` |
| `mobirthp` | Month of birth spouse/partner | `Numeric(Byte)` | `%14.0g` |
| `yrbirthp` | Year of birth spouse/partner | `Numeric(Int)` | `%14.0g` |
| `agep2004` | Age of partner in 2004 | `Numeric(Byte)` | `%14.0g` |
| `partnerinhh` | Partner in household | `Numeric(Byte)` | `%14.0g` |
| `relrpers` | Relation to coverscreen respondent | `Numeric(Byte)` | `%47.0f` |
| `hhsize` | Household size | `Numeric(Byte)` | `%9.0g` |
| `fam_resp` | Family respondent | `Numeric(Byte)` | `%21.0g` |
| `fin_resp` | Financial respondent | `Numeric(Byte)` | `%24.0g` |
| `finsep` | Finances totally separate | `Numeric(Byte)` | `%14.0g` |
| `hou_resp` | Household respondent | `Numeric(Byte)` | `%24.0g` |
| `ILgroup` | Population group (Israel only) | `Numeric(Byte)` | `%38.0g` |
| `interview` | Interview done in wave 1 | `Numeric(Byte)` | `%21.0g` |
| `int_year` | Interview year | `Numeric(Int)` | `%14.0g` |
| `int_month` | Interview month | `Numeric(Byte)` | `%14.0g` |

### `dn` - Demographics

- Dataset: `sharew1_rel9-0-0_dn.dta`
- Read with: `ps.read_share_module("dn", wave=1)`
- Rows: 30,416
- Variables: 75
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `dn002_` | Month of birth | `Numeric(Byte)` | `%10.0f` |
| `dn003_` | Year of birth | `Numeric(Int)` | `%10.0f` |
| `dn004_` | Born in the country of interview | `Numeric(Byte)` | `%10.0f` |
| `dn005c` | Foreign country of birth coding | `Numeric(Int)` | `%46.0g` |
| `dn006_` | Year came to live in country | `Numeric(Int)` | `%10.0f` |
| `dn007_` | Citizenship country of interview | `Numeric(Byte)` | `%10.0f` |
| `dn008c` | Other citizenship coding | `Numeric(Int)` | `%46.0g` |
| `dn009_` | Country-specific question | `Numeric(Byte)` | `%25.0f` |
| `dn010_` | Highest school degree obtained | `Numeric(Byte)` | `%47.0f` |
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
| `dn012d95` | Further education: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `dn012dno` | Further education: none | `Numeric(Byte)` | `%12.0g` |
| `dn012dot` | Further education: other | `Numeric(Byte)` | `%12.0g` |
| `dn014_` | Marital status | `Numeric(Byte)` | `%39.0f` |
| `dn015_` | Year of marriage, if living together | `Numeric(Int)` | `%10.0f` |
| `dn016_` | Year of registered partnership | `Numeric(Int)` | `%10.0f` |
| `dn017_` | Year of marriage, if living separated | `Numeric(Int)` | `%10.0f` |
| `dn018_` | Since when divorced | `Numeric(Int)` | `%10.0f` |
| `dn019_` | Since when widowed | `Numeric(Int)` | `%10.0f` |
| `dn020_` | Year of birth of former partner | `Numeric(Int)` | `%10.0f` |
| `dn021_` | Highest educational degree of former partner | `Numeric(Byte)` | `%47.0f` |
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
| `dn023d14` | Further education partner: country-specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `dn023d95` | Further education former partner: still in education or training | `Numeric(Byte)` | `%12.0g` |
| `dn023dno` | Further education former partner: none | `Numeric(Byte)` | `%12.0g` |
| `dn023dot` | Further education former partner: other | `Numeric(Byte)` | `%12.0g` |
| `dn026_1` | Is natural parent still alive: mother | `Numeric(Byte)` | `%10.0f` |
| `dn026_2` | Is natural parent still alive: father | `Numeric(Byte)` | `%10.0f` |
| `dn027_1` | Age of death of parent: mother | `Numeric(Int)` | `%10.0f` |
| `dn027_2` | Age of death of parent: father | `Numeric(Int)` | `%10.0f` |
| `dn028_1` | Age of natural parent: mother | `Numeric(Int)` | `%10.0f` |
| `dn028_2` | Age of natural parent: father | `Numeric(Int)` | `%10.0f` |
| `dn030_1` | Where does parent live: mother | `Numeric(Byte)` | `%48.0f` |
| `dn030_2` | Where does parent live: father | `Numeric(Byte)` | `%48.0f` |
| `dn032_1` | Personal contact with parent during past 12 months: mother | `Numeric(Byte)` | `%27.0f` |
| `dn032_2` | Personal contact with parent during past 12 months: father | `Numeric(Byte)` | `%27.0f` |
| `dn033_1` | Health of parent: mother | `Numeric(Byte)` | `%13.0f` |
| `dn033_2` | Health of parent: father | `Numeric(Byte)` | `%13.0f` |
| `dn034_` | Ever had any siblings | `Numeric(Byte)` | `%10.0f` |
| `dn035_` | Oldest or youngest child | `Numeric(Byte)` | `%12.0f` |
| `dn036_` | How many brothers alive | `Numeric(Byte)` | `%10.0f` |
| `dn037_` | How many sisters alive | `Numeric(Byte)` | `%10.0f` |
| `dn038_` | Who answered the questions in dn | `Numeric(Byte)` | `%20.0f` |
| `dn042_` | Male or female | `Numeric(Byte)` | `%10.0g` |

### `ep` - Employment and Pensions

- Dataset: `sharew1_rel9-0-0_ep.dta`
- Read with: `ps.read_share_module("ep", wave=1)`
- Rows: 30,416
- Variables: 360
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `ep002_` | Did nevertheless any paid work last four weeks | `Numeric(Byte)` | `%10.0f` |
| `ep003_` | Temporarily away from work | `Numeric(Byte)` | `%10.0f` |
| `ep005_` | Current job situation | `Numeric(Byte)` | `%65.0g` |
| `ep005raw` | Current job situation (original response) | `Numeric(Byte)` | `%27.0g` |
| `ep006_` | Ever done paid work | `Numeric(Byte)` | `%10.0f` |
| `ep007_` | Currently more than one job | `Numeric(Byte)` | `%10.0f` |
| `ep009_1` | Employee or a self-employed in (main) job | `Numeric(Byte)` | `%30.0f` |
| `ep009_2` | Employee or a self-employed in secondary job | `Numeric(Byte)` | `%30.0f` |
| `ep010_1` | Start of current (main) job (year) | `Numeric(Int)` | `%10.0f` |
| `ep010_2` | Start of current secondary job (year) | `Numeric(Int)` | `%10.0f` |
| `ep011_1` | Term of (main) job | `Numeric(Byte)` | `%10.0f` |
| `ep011_2` | Term of secondary job | `Numeric(Byte)` | `%10.0f` |
| `ep012_1` | Total contracted hours per week (main) job | `Numeric(Double)` | `%10.1f` |
| `ep012_2` | Total contracted hours per week secondary job | `Numeric(Double)` | `%10.1f` |
| `ep013_1` | Total hours worked per week (main) job | `Numeric(Double)` | `%10.1f` |
| `ep013_2` | Total hours worked per week secondary job | `Numeric(Double)` | `%10.1f` |
| `ep014_1` | Months worked in (main) job (number) | `Numeric(Byte)` | `%10.0f` |
| `ep014_2` | Months worked in secondary job (number) | `Numeric(Byte)` | `%10.0f` |
| `ep019_1` | Employed in the public sector, (main) job | `Numeric(Byte)` | `%10.0f` |
| `ep019_2` | Employed in the public sector, secondary job | `Numeric(Byte)` | `%10.0f` |
| `ep020_1` | Number of people employed at firm, (main) job | `Numeric(Byte)` | `%11.0f` |
| `ep020_2` | Number of people employed at firm, secondary job | `Numeric(Byte)` | `%11.0f` |
| `ep021_1` | Responsibility for supervising other employees, (main) job | `Numeric(Byte)` | `%10.0f` |
| `ep021_2` | Responsibility for supervising other employees, secondary job | `Numeric(Byte)` | `%10.0f` |
| `ep022_1` | Number of people responsible for in (main) job | `Numeric(Byte)` | `%11.0f` |
| `ep022_2` | Number of people responsible for in secondary job | `Numeric(Byte)` | `%11.0f` |
| `ep024_1` | Number of employees in (main) job | `Numeric(Byte)` | `%11.0f` |
| `ep024_2` | Number of employees in secondary job | `Numeric(Byte)` | `%11.0f` |
| `ep026_` | Satisfied with (main) job | `Numeric(Byte)` | `%26.0f` |
| `ep027_` | (Main) job physically demanding | `Numeric(Byte)` | `%26.0f` |
| `ep028_` | Time pressure due to a heavy workload in (main) job | `Numeric(Byte)` | `%26.0f` |
| `ep029_` | Little freedom to decide how I do my work in (main) job | `Numeric(Byte)` | `%26.0f` |
| `ep030_` | Opportunity to develop new skills in (main) job | `Numeric(Byte)` | `%26.0f` |
| `ep031_` | Receive support in difficult situations in (main) job | `Numeric(Byte)` | `%26.0f` |
| `ep032_` | Receive recognition for work in (main) job | `Numeric(Byte)` | `%26.0f` |
| `ep033_` | Salary or earnings are adequate in (main) job | `Numeric(Byte)` | `%26.0f` |
| `ep034_` | Poor prospects for (main) job advancement | `Numeric(Byte)` | `%26.0f` |
| `ep035_` | Poor (main) job security | `Numeric(Byte)` | `%26.0f` |
| `ep036_` | Look for early retirement in (main) job | `Numeric(Byte)` | `%10.0f` |
| `ep037_` | Afraid health limits ability to work before regular retirement in (main) job | `Numeric(Byte)` | `%10.0f` |
| `ep038_1` | Frequency of payment in (main) job | `Numeric(Byte)` | `%29.0f` |
| `ep038_2` | Frequency of payment in secondary job | `Numeric(Byte)` | `%29.0f` |
| `ep041e_1` | Taken home from work before tax, (main) job | `Numeric(Double)` | `%222.0g` |
| `ep041ub_1` | Taken home from work before tax, (main) job ub | `Numeric(Byte)` | `%222.0g` |
| `ep041e_2` | Taken home from work before tax, secondary job | `Numeric(Double)` | `%222.0g` |
| `ep041ub_2` | Taken home from work before tax, secondary job ub | `Numeric(Byte)` | `%222.0g` |
| `ep041v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `ep041v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `ep041v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `ep045e_1` | Total amount of profits at the end of the year, (main) job | `Numeric(Double)` | `%222.0g` |
| `ep045ub_1` | Total amount of profits at the end of the year, (main) job ub | `Numeric(Byte)` | `%222.0g` |
| `ep045e_2` | Total amount of profits at the end of the year, secondary job | `Numeric(Double)` | `%222.0g` |
| `ep045ub_2` | Total amount of profits at the end of the year, secondary job ub | `Numeric(Byte)` | `%222.0g` |
| `ep045v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `ep045v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `ep045v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `ep049_` | Years working in last job | `Numeric(Byte)` | `%10.0f` |
| `ep050_` | Year last job ended | `Numeric(Int)` | `%10.0f` |
| `ep051_` | Employee or a self employed in last job | `Numeric(Byte)` | `%30.0f` |
| `ep055_` | Employed in the public sector, last job | `Numeric(Byte)` | `%10.0f` |
| `ep056_` | Number of people employed at firm, last job | `Numeric(Byte)` | `%11.0f` |
| `ep057_` | Responsibility for supervising others, last job | `Numeric(Byte)` | `%10.0f` |
| `ep058_` | Number of people responsible for, last job | `Numeric(Byte)` | `%11.0f` |
| `ep059_` | Opportunities to work after the official retirement age | `Numeric(Byte)` | `%10.0f` |
| `ep061_` | Number of employees, last job | `Numeric(Byte)` | `%11.0f` |
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
| `ep064dot` | Reason retirement: other | `Numeric(Byte)` | `%12.0g` |
| `ep065_` | Retirement been a relief or a concern | `Numeric(Byte)` | `%30.0f` |
| `ep067_` | How became unemployed | `Numeric(Byte)` | `%55.0f` |
| `ep068_` | Disability caused by work | `Numeric(Byte)` | `%10.0f` |
| `ep069d1` | Reason stopped working: health problems | `Numeric(Byte)` | `%12.0g` |
| `ep069d2` | Reason stopped working: too tiring | `Numeric(Byte)` | `%12.0g` |
| `ep069d3` | Reason stopped working: too expensive to hire someone to look after home/family | `Numeric(Byte)` | `%12.0g` |
| `ep069d4` | Reason stopped working: wanted to take care of (grand)children | `Numeric(Byte)` | `%12.0g` |
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
| `ep071dot` | Income sources: country-specific category 50 | `Numeric(Byte)` | `%12.0g` |
| `ep071dno` | Income sources: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep074_1` | Period of income source c1 | `Numeric(Byte)` | `%29.0f` |
| `ep074_2` | Period of income source c2 | `Numeric(Byte)` | `%29.0f` |
| `ep074_3` | Period of income source c3 | `Numeric(Byte)` | `%29.0f` |
| `ep074_4` | Period of income source c4 | `Numeric(Byte)` | `%29.0f` |
| `ep074_5` | Period of income source c5 | `Numeric(Byte)` | `%29.0f` |
| `ep074_6` | Period of income source c6 | `Numeric(Byte)` | `%29.0f` |
| `ep074_7` | Period of income source c7 | `Numeric(Byte)` | `%29.0f` |
| `ep074_8` | Period of income source c8 | `Numeric(Byte)` | `%29.0f` |
| `ep074_9` | Period of income source c9 | `Numeric(Byte)` | `%29.0f` |
| `ep074_10` | Period of income source c10 | `Numeric(Byte)` | `%29.0f` |
| `ep074_11` | Period of income source c11 | `Numeric(Byte)` | `%29.0f` |
| `ep078e_1` | Average payment income source c1 last year | `Numeric(Double)` | `%222.0g` |
| `ep078ub_1` | Average payment income source c1 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep078e_2` | Average payment income source c2 last year | `Numeric(Double)` | `%222.0g` |
| `ep078ub_2` | Average payment income source c2 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep078e_3` | Average payment income source c3 last year | `Numeric(Double)` | `%222.0g` |
| `ep078ub_3` | Average payment income source c3 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep078e_4` | Average payment income source c4 last year | `Numeric(Double)` | `%222.0g` |
| `ep078ub_4` | Average payment income source c4 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep078e_5` | Average payment income source c5 last year | `Numeric(Double)` | `%222.0g` |
| `ep078ub_5` | Average payment income source c5 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep078e_6` | Average payment income source c6 last year | `Numeric(Double)` | `%222.0g` |
| `ep078ub_6` | Average payment income source c6 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep078e_7` | Average payment income source c7 last year | `Numeric(Double)` | `%222.0g` |
| `ep078ub_7` | Average payment income source c7 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep078e_8` | Average payment income source c8 last year | `Numeric(Double)` | `%222.0g` |
| `ep078ub_8` | Average payment income source c8 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep078e_9` | Average payment income source c9 last year | `Numeric(Double)` | `%222.0g` |
| `ep078ub_9` | Average payment income source c9 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep078e_10` | Average payment income source c10 last year | `Numeric(Double)` | `%222.0g` |
| `ep078ub_10` | Average payment income source c10 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep078e_11` | Average payment income source c11 last year | `Numeric(Double)` | `%222.0g` |
| `ep078ub_11` | Average payment income source c11 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep078v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `ep078v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `ep078v3` | Bracket value 3 | `Numeric(Float)` | `%19.0f` |
| `ep081_1` | Lump sum payment income source c1 | `Numeric(Byte)` | `%10.0f` |
| `ep081_2` | Lump sum payment income source c2 | `Numeric(Byte)` | `%10.0f` |
| `ep081_3` | Lump sum payment income source c3 | `Numeric(Byte)` | `%10.0f` |
| `ep081_4` | Lump sum payment income source c4 | `Numeric(Byte)` | `%10.0f` |
| `ep081_5` | Lump sum payment income source c5 | `Numeric(Byte)` | `%10.0f` |
| `ep081_6` | Lump sum payment income source c6 | `Numeric(Byte)` | `%10.0f` |
| `ep081_7` | Lump sum payment income source c7 | `Numeric(Byte)` | `%10.0f` |
| `ep081_8` | Lump sum payment income source c8 | `Numeric(Byte)` | `%10.0f` |
| `ep081_9` | Lump sum payment income source c9 | `Numeric(Byte)` | `%10.0f` |
| `ep081_10` | Lump sum payment income source c10 | `Numeric(Byte)` | `%10.0f` |
| `ep081_11` | Lump sum payment income source c11 | `Numeric(Byte)` | `%10.0f` |
| `ep082e_1` | Total amount of lump sum payment income source c1 | `Numeric(Double)` | `%222.0g` |
| `ep082ub_1` | Total amount of lump sum payment income source c1 ub | `Numeric(Byte)` | `%222.0g` |
| `ep082e_2` | Total amount of lump sum payment income source c2 | `Numeric(Double)` | `%222.0g` |
| `ep082ub_2` | Total amount of lump sum payment income source c2 ub | `Numeric(Byte)` | `%222.0g` |
| `ep082e_3` | Total amount of lump sum payment income source c3 | `Numeric(Double)` | `%222.0g` |
| `ep082ub_3` | Total amount of lump sum payment income source c3 ub | `Numeric(Byte)` | `%222.0g` |
| `ep082e_4` | Total amount of lump sum payment income source c4 | `Numeric(Double)` | `%222.0g` |
| `ep082ub_4` | Total amount of lump sum payment income source c4 ub | `Numeric(Byte)` | `%222.0g` |
| `ep082e_5` | Total amount of lump sum payment income source c5 | `Numeric(Double)` | `%222.0g` |
| `ep082ub_5` | Total amount of lump sum payment income source c5 ub | `Numeric(Byte)` | `%222.0g` |
| `ep082e_6` | Total amount of lump sum payment income source c6 | `Numeric(Double)` | `%222.0g` |
| `ep082ub_6` | Total amount of lump sum payment income source c6 ub | `Numeric(Byte)` | `%222.0g` |
| `ep082e_7` | Total amount of lump sum payment income source c7 | `Numeric(Double)` | `%222.0g` |
| `ep082ub_7` | Total amount of lump sum payment income source c7 ub | `Numeric(Byte)` | `%222.0g` |
| `ep082e_8` | Total amount of lump sum payment income source c8 | `Numeric(Double)` | `%222.0g` |
| `ep082ub_8` | Total amount of lump sum payment income source c8 ub | `Numeric(Byte)` | `%222.0g` |
| `ep082e_9` | Total amount of lump sum payment income source c9 | `Numeric(Double)` | `%222.0g` |
| `ep082ub_9` | Total amount of lump sum payment income source c9 ub | `Numeric(Byte)` | `%222.0g` |
| `ep082e_10` | Total amount of lump sum payment income source c10 | `Numeric(Double)` | `%222.0g` |
| `ep082ub_10` | Total amount of lump sum payment income source c10 ub | `Numeric(Byte)` | `%222.0g` |
| `ep082e_11` | Total amount of lump sum payment income source c11 | `Numeric(Double)` | `%222.0g` |
| `ep082ub_11` | Total amount of lump sum payment income source c11 ub | `Numeric(Byte)` | `%222.0g` |
| `ep082v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `ep082v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `ep082v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `ep085_` | Receive care insurance payments | `Numeric(Byte)` | `%10.0f` |
| `ep086e` | Amount of care insurance | `Numeric(Double)` | `%222.0g` |
| `ep087_` | Apply for care insurance | `Numeric(Byte)` | `%10.0f` |
| `ep088_` | Application rejected or pending | `Numeric(Byte)` | `%10.0f` |
| `ep089d1` | Regular payments received: life insurance | `Numeric(Byte)` | `%12.0g` |
| `ep089d2` | Regular payments received: private annuity/private personal pension | `Numeric(Byte)` | `%12.0g` |
| `ep089d3` | Regular payments received: private health insurance | `Numeric(Byte)` | `%12.0g` |
| `ep089d4` | Regular payments received: alimony | `Numeric(Byte)` | `%12.0g` |
| `ep089d5` | Regular payments received: from charities | `Numeric(Byte)` | `%12.0g` |
| `ep089dno` | Regular payments received: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep090_1` | Period received payment c1 | `Numeric(Byte)` | `%28.0f` |
| `ep090_2` | Period received payment c2 | `Numeric(Byte)` | `%28.0f` |
| `ep090_3` | Period received payment c3 | `Numeric(Byte)` | `%28.0f` |
| `ep090_4` | Period received payment c4 | `Numeric(Byte)` | `%28.0f` |
| `ep090_5` | Period received payment c5 | `Numeric(Byte)` | `%28.0f` |
| `ep092_1` | Additional payments for this benefit in last year, payment c1 | `Numeric(Byte)` | `%10.0f` |
| `ep092_2` | Additional payments for this benefit in last year, payment c2 | `Numeric(Byte)` | `%10.0f` |
| `ep092_3` | Additional payments for this benefit in last year, payment c3 | `Numeric(Byte)` | `%10.0f` |
| `ep092_4` | Additional payments for this benefit in last year, payment c4 | `Numeric(Byte)` | `%10.0f` |
| `ep092_5` | Additional payments for this benefit in last year, payment c5 | `Numeric(Byte)` | `%10.0f` |
| `ep094e_1` | Total amount payment c1 last year | `Numeric(Double)` | `%222.0g` |
| `ep094ub_1` | Total amount payment c1 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep094e_2` | Total amount payment c2 last year | `Numeric(Double)` | `%222.0g` |
| `ep094ub_2` | Total amount payment c2 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep094e_3` | Total amount payment c3 last year | `Numeric(Double)` | `%222.0g` |
| `ep094ub_3` | Total amount payment c3 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep094e_4` | Total amount payment c4 last year | `Numeric(Double)` | `%222.0g` |
| `ep094ub_4` | Total amount payment c4 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep094e_5` | Total amount payment c5 last year | `Numeric(Double)` | `%222.0g` |
| `ep094ub_5` | Total amount payment c5 last year ub | `Numeric(Byte)` | `%222.0g` |
| `ep094v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `ep094v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `ep094v3` | Bracket value 3 | `Numeric(Float)` | `%19.0f` |
| `ep096_1` | Months received payment c1 | `Numeric(Byte)` | `%10.0f` |
| `ep096_2` | Months received payment c2 | `Numeric(Byte)` | `%10.0f` |
| `ep096_3` | Months received payment c3 | `Numeric(Byte)` | `%10.0f` |
| `ep096_4` | Months received payment c4 | `Numeric(Byte)` | `%10.0f` |
| `ep096_5` | Months received payment c5 | `Numeric(Byte)` | `%10.0f` |
| `ep097_` | Pension claims | `Numeric(Byte)` | `%10.0f` |
| `ep098d1` | Type of pension entitled to: country specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `ep098d2` | Type of pension entitled to: country specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `ep098d3` | Type of pension entitled to: country specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `ep098d4` | Type of pension entitled to: country specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `ep098d5` | Type of pension entitled to: country specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `ep098d6` | Type of pension entitled to: country-specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `ep098d7` | Type of pension entitled to: country-specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `ep098dno` | Type of pension entitled to: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep099_1` | Pension c1 with/without health insurance | `Numeric(Byte)` | `%28.0f` |
| `ep099_2` | Pension c2 with/without health insurance | `Numeric(Byte)` | `%28.0f` |
| `ep099_3` | Pension c3 with/without health insurance | `Numeric(Byte)` | `%28.0f` |
| `ep099_4` | Pension c4 with/without health insurance | `Numeric(Byte)` | `%28.0f` |
| `ep099_5` | Pension c5 with/without health insurance | `Numeric(Byte)` | `%28.0f` |
| `ep099_6` | Pension c6 with/without health insurance | `Numeric(Byte)` | `%28.0f` |
| `ep099_7` | Pension c7 with/without health insurance | `Numeric(Byte)` | `%28.0f` |
| `ep100_1` | Percentage of salary to pension c1 | `Numeric(Double)` | `%10.2f` |
| `ep100_2` | Percentage of salary to pension c2 | `Numeric(Double)` | `%10.2f` |
| `ep100_3` | Percentage of salary to pension c3 | `Numeric(Double)` | `%10.2f` |
| `ep100_4` | Percentage of salary to pension c4 | `Numeric(Double)` | `%10.2f` |
| `ep100_5` | Percentage of salary to pension c5 | `Numeric(Double)` | `%10.2f` |
| `ep100_6` | Percentage of salary to pension c6 | `Numeric(Double)` | `%10.2f` |
| `ep100_7` | Percentage of salary to pension c7 | `Numeric(Byte)` | `%10.2f` |
| `ep102_1` | Compulsory or voluntary participation in pension c1 | `Numeric(Byte)` | `%10.0f` |
| `ep102_2` | Compulsory or voluntary participation in pension c2 | `Numeric(Byte)` | `%10.0f` |
| `ep102_3` | Compulsory or voluntary participation in pension c3 | `Numeric(Byte)` | `%10.0f` |
| `ep102_4` | Compulsory or voluntary participation in pension c4 | `Numeric(Byte)` | `%10.0f` |
| `ep102_5` | Compulsory or voluntary participation in pension c5 | `Numeric(Byte)` | `%10.0f` |
| `ep102_6` | Compulsory or voluntary plan or fund, pension c6 | `Numeric(Byte)` | `%10.0f` |
| `ep102_7` | Compulsory or voluntary plan or fund, pension c7 | `Numeric(Byte)` | `%10.0f` |
| `ep103_1` | Years contributing to plan, pension c1 | `Numeric(Int)` | `%10.0f` |
| `ep103_2` | Years contributing to plan, pension c2 | `Numeric(Byte)` | `%10.0f` |
| `ep103_3` | Years contributing to plan, pension c3 | `Numeric(Int)` | `%10.0f` |
| `ep103_4` | Years contributing to plan, pension c4 | `Numeric(Byte)` | `%10.0f` |
| `ep103_5` | Years contributing to plan, pension c5 | `Numeric(Int)` | `%10.0f` |
| `ep103_6` | Years contributing to plan, pension c6 | `Numeric(Byte)` | `%10.0f` |
| `ep103_7` | Years contributing to plan, pension c7 | `Numeric(Int)` | `%10.0f` |
| `ep104_1` | Retirement age in pension c1 | `Numeric(Byte)` | `%10.0f` |
| `ep104_2` | Retirement age in pension c2 | `Numeric(Byte)` | `%10.0f` |
| `ep104_3` | Retirement age in pension c3 | `Numeric(Byte)` | `%10.0f` |
| `ep104_4` | Retirement age in pension c4 | `Numeric(Byte)` | `%10.0f` |
| `ep104_5` | Retirement age in pension c5 | `Numeric(Byte)` | `%10.0f` |
| `ep104_6` | Retirement age in pension c6 | `Numeric(Byte)` | `%10.0f` |
| `ep104_7` | Retirement age in pension c7 | `Numeric(Byte)` | `%10.0f` |
| `ep105_1` | Early retirement possibility, pension c1 | `Numeric(Byte)` | `%10.0f` |
| `ep105_2` | Early retirement possibility, pension c2 | `Numeric(Byte)` | `%10.0f` |
| `ep105_3` | Early retirement possibility, pension c3 | `Numeric(Byte)` | `%10.0f` |
| `ep105_4` | Early retirement possibility, pension c4 | `Numeric(Byte)` | `%10.0f` |
| `ep105_5` | Early retirement possibility, pension c5 | `Numeric(Byte)` | `%10.0f` |
| `ep105_6` | Early retirement possibility, pension c6 | `Numeric(Byte)` | `%10.0f` |
| `ep105_7` | Early retirement possibility, pension c7 | `Numeric(Byte)` | `%10.0f` |
| `ep106_1` | Expected age to collect pension c1 | `Numeric(Int)` | `%10.0f` |
| `ep106_2` | Expected age to collect pension c2 | `Numeric(Byte)` | `%10.0f` |
| `ep106_3` | Expected age to collect pension c3 | `Numeric(Int)` | `%10.0f` |
| `ep106_4` | Expected age to collect pension c4 | `Numeric(Byte)` | `%10.0f` |
| `ep106_5` | Expected age to collect pension c5 | `Numeric(Byte)` | `%10.0f` |
| `ep106_6` | Expected age to collect pension c6 | `Numeric(Byte)` | `%10.0f` |
| `ep106_7` | Expected age to collect pension c7 | `Numeric(Byte)` | `%10.0f` |
| `ep107_1` | Expect lump sum payment with pension c1 | `Numeric(Byte)` | `%10.0f` |
| `ep107_2` | Expect lump sum payment with pension c2 | `Numeric(Byte)` | `%10.0f` |
| `ep107_3` | Expect lump sum payment with pension c3 | `Numeric(Byte)` | `%10.0f` |
| `ep107_4` | Expect lump sum payment with pension c4 | `Numeric(Byte)` | `%10.0f` |
| `ep107_5` | Expect lump sum payment with pension c5 | `Numeric(Byte)` | `%10.0f` |
| `ep107_6` | Expect lump sum payment with pension c6 | `Numeric(Byte)` | `%10.0f` |
| `ep107_7` | Expect lump sum payment with pension c7 | `Numeric(Byte)` | `%10.0f` |
| `ep108e_1` | Amount lump sum payment at retirement, pension c1 | `Numeric(Double)` | `%222.0g` |
| `ep108ub_1` | Amount lump sum payment at retirement, pension c1 ub | `Numeric(Byte)` | `%222.0g` |
| `ep108e_2` | Amount lump sum payment at retirement, pension c2 | `Numeric(Double)` | `%222.0g` |
| `ep108ub_2` | Amount lump sum payment at retirement, pension c2 ub | `Numeric(Byte)` | `%222.0g` |
| `ep108e_3` | Amount lump sum payment at retirement, pension c3 | `Numeric(Double)` | `%222.0g` |
| `ep108ub_3` | Amount lump sum payment at retirement, pension c3 ub | `Numeric(Byte)` | `%222.0g` |
| `ep108e_4` | Amount lump sum payment at retirement, pension c4 | `Numeric(Double)` | `%222.0g` |
| `ep108ub_4` | Amount lump sum payment at retirement, pension c4 ub | `Numeric(Byte)` | `%222.0g` |
| `ep108e_5` | Amount lump sum payment at retirement, pension c5 | `Numeric(Double)` | `%222.0g` |
| `ep108ub_5` | Amount lump sum payment at retirement, pension c5 ub | `Numeric(Byte)` | `%222.0g` |
| `ep108e_6` | Amount lump sum payment at retirement, pension c6 | `Numeric(Double)` | `%222.0g` |
| `ep108ub_6` | Amount lump sum payment at retirement, pension c6 ub | `Numeric(Byte)` | `%222.0g` |
| `ep108e_7` | Amount lump sum payment at retirement, pension c7 | `Numeric(Double)` | `%222.0g` |
| `ep108ub_7` | Amount lump sum payment at retirement, pension c7 ub | `Numeric(Byte)` | `%222.0g` |
| `ep108v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `ep108v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `ep108v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `ep109_1` | Percentage of salary received as pension c1 | `Numeric(Float)` | `%10.0f` |
| `ep109_2` | Percentage of salary received as pension c2 | `Numeric(Byte)` | `%10.0f` |
| `ep109_3` | Percentage of salary received as pension c3 | `Numeric(Byte)` | `%10.0f` |
| `ep109_4` | Percentage of salary received as pension c4 | `Numeric(Float)` | `%10.0f` |
| `ep109_5` | Percentage of salary received as pension c5 | `Numeric(Byte)` | `%10.0f` |
| `ep109_6` | Percentage of salary received as pension c6 | `Numeric(Byte)` | `%10.0f` |
| `ep109_7` | Percentage of salary received as pension c7 | `Numeric(Byte)` | `%10.0f` |
| `ep201e_1` | Taken home from work after tax, (main) job | `Numeric(Double)` | `%222.0g` |
| `ep201ub_1` | Taken home from work after tax, (main) job ub | `Numeric(Byte)` | `%222.0g` |
| `ep201e_2` | Taken home from work after tax, secondary job | `Numeric(Double)` | `%222.0g` |
| `ep201ub_2` | Taken home from work after tax, secondary job ub | `Numeric(Byte)` | `%222.0g` |
| `ep201v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `ep201v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `ep201v3` | Bracket value 3 | `Numeric(Float)` | `%19.0f` |
| `ep204_` | Any earnings from employment previous year | `Numeric(Byte)` | `%10.0f` |
| `ep205e` | Earnings employment per year before taxes | `Numeric(Double)` | `%222.0g` |
| `ep205ub` | Earnings employment per year before taxes ub | `Numeric(Byte)` | `%222.0g` |
| `ep205v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `ep205v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `ep205v3` | Bracket value 3 | `Numeric(Long)` | `%19.0f` |
| `ep206_` | Income from self-employment previous year | `Numeric(Byte)` | `%10.0f` |
| `ep207e` | Earnings self-employment per year before taxes | `Numeric(Double)` | `%222.0g` |
| `ep207ub` | Earnings self-employment per year before taxes ub | `Numeric(Byte)` | `%222.0g` |
| `ep207v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `ep207v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `ep207v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `ep208_1` | How many months received income source c1 | `Numeric(Byte)` | `%10.0f` |
| `ep208_2` | How many months received income source c2 | `Numeric(Byte)` | `%10.0f` |
| `ep208_3` | How many months received income source c3 | `Numeric(Byte)` | `%10.0f` |
| `ep208_4` | How many months received income source c4 | `Numeric(Byte)` | `%10.0f` |
| `ep208_5` | How many months received income source c5 | `Numeric(Byte)` | `%10.0f` |
| `ep208_6` | How many months received income source c6 | `Numeric(Byte)` | `%10.0f` |
| `ep208_7` | How many months received income source c7 | `Numeric(Byte)` | `%10.0f` |
| `ep208_8` | How many months received income source c8 | `Numeric(Byte)` | `%10.0f` |
| `ep208_9` | How many months received income source c9 | `Numeric(Byte)` | `%10.0f` |
| `ep208_10` | How many months received income source c10 | `Numeric(Byte)` | `%10.0f` |
| `ep208_11` | How many months received income source c11 | `Numeric(Byte)` | `%10.0f` |
| `ep209e_1` | Additional payments c1 after taxes | `Numeric(Double)` | `%222.0g` |
| `ep209ub_1` | Additional payments c1 after taxes ub | `Numeric(Byte)` | `%222.0g` |
| `ep209e_2` | Additional payments c2 after taxes | `Numeric(Double)` | `%222.0g` |
| `ep209ub_2` | Additional payments c2 after taxes ub | `Numeric(Byte)` | `%222.0g` |
| `ep209e_3` | Additional payments c3 after taxes | `Numeric(Double)` | `%222.0g` |
| `ep209ub_3` | Additional payments c3 after taxes ub | `Numeric(Byte)` | `%222.0g` |
| `ep209e_4` | Additional payments c4 after taxes | `Numeric(Byte)` | `%222.0g` |
| `ep209ub_4` | Additional payments c4 after taxes ub | `Numeric(Byte)` | `%222.0g` |
| `ep209e_5` | Additional payments c5 after taxes | `Numeric(Int)` | `%222.0g` |
| `ep209ub_5` | Additional payments c5 after taxes ub | `Numeric(Byte)` | `%222.0g` |
| `ep209v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `ep209v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `ep209v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `ep210_` | Who answered section ep | `Numeric(Byte)` | `%20.0f` |
| `ep213_1` | First year received income source c1 | `Numeric(Int)` | `%10.0f` |
| `ep213_2` | First year received income source c2 | `Numeric(Int)` | `%10.0f` |
| `ep213_3` | First year received income source c3 | `Numeric(Int)` | `%10.0f` |
| `ep213_4` | First year received income source c4 | `Numeric(Int)` | `%10.0f` |
| `ep213_5` | First year received income source c5 | `Numeric(Int)` | `%10.0f` |
| `ep213_6` | First year received income source c6 | `Numeric(Int)` | `%10.0f` |
| `ep213_7` | First year received income source c7 | `Numeric(Int)` | `%10.0f` |
| `ep213_8` | First year received income source c8 | `Numeric(Int)` | `%10.0f` |
| `ep213_9` | First year received income source c9 | `Numeric(Int)` | `%10.0f` |
| `ep213_10` | First year received income source c10 | `Numeric(Int)` | `%10.0f` |
| `ep213_11` | First year received income source c11 | `Numeric(Int)` | `%10.0f` |
| `ep214_1` | Amount includes additional payments (main) job | `Numeric(Byte)` | `%10.0f` |
| `ep214_2` | Amount includes additional payments secondary job | `Numeric(Byte)` | `%10.0f` |

### `ex` - Expectations

- Dataset: `sharew1_rel9-0-0_ex.dta`
- Read with: `ps.read_share_module("ex", wave=1)`
- Rows: 30,416
- Variables: 34
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `ex001_` | Introduction and example | `Numeric(Byte)` | `%10.0f` |
| `ex002_` | Chance of receiving inheritance | `Numeric(Byte)` | `%10.0f` |
| `ex003_` | Chance inheritance more than 50000 | `Numeric(Byte)` | `%10.0f` |
| `ex004_` | Chance of leaving inheritance more than 50000 | `Numeric(Byte)` | `%10.0f` |
| `ex005_` | Chance of leaving any inheritance | `Numeric(Byte)` | `%10.0f` |
| `ex006_` | Chance of leaving inheritance more than 150000 | `Numeric(Byte)` | `%10.0f` |
| `ex007_` | Chance government reduces pension | `Numeric(Byte)` | `%10.0f` |
| `ex008_` | Chance government raises retirement age | `Numeric(Byte)` | `%10.0f` |
| `ex009_` | Life expectancy | `Numeric(Byte)` | `%10.0f` |
| `ex009age` | Life expectancy target age | `Numeric(Int)` | `%10.0g` |
| `ex010_` | Chance standard of living will be better | `Numeric(Byte)` | `%10.0f` |
| `ex011_` | Chance standard of living will be worse | `Numeric(Byte)` | `%10.0f` |
| `ex013_` | Save or invest any of the gift | `Numeric(Byte)` | `%10.0f` |
| `ex014_` | Amount save or invest of the gift (local currency) | `Numeric(Long)` | `%222.0g` |
| `ex014e` | Amount save or invest of the gift (euros) | `Numeric(Double)` | `%18.2f` |
| `ex015_` | Use any of the gift to pay off debts | `Numeric(Byte)` | `%10.0f` |
| `ex016_` | Amount using to pay off debts (local currency) | `Numeric(Long)` | `%222.0g` |
| `ex016e` | Amount using to pay debts (euros) | `Numeric(Double)` | `%18.2f` |
| `ex017_` | Give any to relatives or donation | `Numeric(Byte)` | `%10.0f` |
| `ex018_` | Amount giving to relatives or donation (local currency) | `Numeric(Double)` | `%222.0g` |
| `ex018e` | Amount giving to relatives or donation (euros) | `Numeric(Double)` | `%18.2f` |
| `ex019_` | Use to buy durables | `Numeric(Byte)` | `%10.0f` |
| `ex020_` | Amount using to buy durables (local currency) | `Numeric(Long)` | `%222.0g` |
| `ex020e` | Amount using to buy durables (euros) | `Numeric(Double)` | `%18.2f` |
| `ex021_` | Use for holiday or journey | `Numeric(Byte)` | `%10.0f` |
| `ex022_` | Amount holiday or journey (local currency) | `Numeric(Long)` | `%222.0g` |
| `ex022e` | Amount holiday or journey (euros) | `Numeric(Double)` | `%18.2f` |

### `ft` - Financial Transfers

- Dataset: `sharew1_rel9-0-0_ft.dta`
- Read with: `ps.read_share_module("ft", wave=1)`
- Rows: 30,416
- Variables: 64
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `ft002_` | Given financial gift 250 or more | `Numeric(Byte)` | `%10.0f` |
| `ft003_1` | To whom given gift, person 1 | `Numeric(Byte)` | `%18.0f` |
| `ft003_2` | To whom given gift, person 2 | `Numeric(Byte)` | `%18.0f` |
| `ft003_3` | To whom given gift, person 3 | `Numeric(Byte)` | `%18.0f` |
| `ft004e_1` | Amount given to person 1 | `Numeric(Double)` | `%222.0g` |
| `ft004ub_1` | Amount given to person 1 ub | `Numeric(Byte)` | `%222.0g` |
| `ft004e_2` | Amount given to person 2 | `Numeric(Double)` | `%222.0g` |
| `ft004ub_2` | Amount given tp person 2 ub | `Numeric(Byte)` | `%222.0g` |
| `ft004e_3` | Amount given to person 3 | `Numeric(Double)` | `%222.0g` |
| `ft004ub_3` | Amount given tp person 3 ub | `Numeric(Byte)` | `%222.0g` |
| `ft004v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `ft004v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `ft004v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `ft006_1` | Reason given to person 1 | `Numeric(Byte)` | `%67.0f` |
| `ft006_2` | Reason given to person 2 | `Numeric(Byte)` | `%67.0f` |
| `ft006_3` | Reason given to person 3 | `Numeric(Byte)` | `%67.0f` |
| `ft009_` | Received financial gift of 250 or more | `Numeric(Byte)` | `%10.0f` |
| `ft010_1` | From whom recieved gift, person 1 | `Numeric(Byte)` | `%18.0f` |
| `ft010_2` | From whom recieved gift, person 2 | `Numeric(Byte)` | `%18.0f` |
| `ft010_3` | From whom recieved gift, person 3 | `Numeric(Byte)` | `%18.0f` |
| `ft011e_1` | Amount received from person 1 | `Numeric(Double)` | `%222.0g` |
| `ft011ub_1` | Amount received from person 1 ub | `Numeric(Byte)` | `%222.0g` |
| `ft011e_2` | Amount received from person 2 | `Numeric(Double)` | `%222.0g` |
| `ft011ub_2` | Amount received from person 2 ub | `Numeric(Byte)` | `%222.0g` |
| `ft011e_3` | Amount received from person 3 | `Numeric(Double)` | `%222.0g` |
| `ft011ub_3` | Amount received from person 3 ub | `Numeric(Byte)` | `%222.0g` |
| `ft011v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `ft011v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `ft011v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `ft013_1` | Reason received gift from person 1 | `Numeric(Byte)` | `%67.0f` |
| `ft013_2` | Reason received gift from person 2 | `Numeric(Byte)` | `%67.0f` |
| `ft013_3` | Reason received gift from person 3 | `Numeric(Byte)` | `%67.0f` |
| `ft015_` | Ever received gift or inheritance (worth 5000 euros or more) | `Numeric(Byte)` | `%10.0f` |
| `ft016_1` | Year, inheritance or large gift 1 received | `Numeric(Int)` | `%10.0f` |
| `ft016_2` | Year, inheritance or large gift 2 received | `Numeric(Int)` | `%10.0f` |
| `ft016_3` | Year, inheritance or large gift 3 received | `Numeric(Int)` | `%10.0f` |
| `ft016_4` | Year, inheritance or large gift 4 received | `Numeric(Int)` | `%10.0f` |
| `ft016_5` | Year, inheritance or large gift 5 received | `Numeric(Int)` | `%10.0f` |
| `ft017_1` | From whom inheritance or large gift 1 | `Numeric(Byte)` | `%18.0f` |
| `ft017_2` | From whom inheritance or large gift 2 | `Numeric(Byte)` | `%18.0f` |
| `ft017_3` | From whom inheritance or large gift 3 | `Numeric(Byte)` | `%18.0f` |
| `ft017_4` | From whom inheritance or large gift 4 | `Numeric(Byte)` | `%18.0f` |
| `ft017_5` | From whom inheritance or large gift 5 | `Numeric(Byte)` | `%18.0f` |
| `ft018e_1` | Value inheritance 1 | `Numeric(Double)` | `%222.0g` |
| `ft018ub_1` | Value inheritance 1 ub | `Numeric(Byte)` | `%222.0g` |
| `ft018e_2` | Value inheritance 2 | `Numeric(Double)` | `%222.0g` |
| `ft018ub_2` | Value inheritance 2 ub | `Numeric(Byte)` | `%222.0g` |
| `ft018e_3` | Value inheritance 3 | `Numeric(Double)` | `%222.0g` |
| `ft018ub_3` | Value inheritance 3 ub | `Numeric(Byte)` | `%222.0g` |
| `ft018e_4` | Value inheritance 4 | `Numeric(Double)` | `%222.0g` |
| `ft018ub_4` | Value inheritance 4 ub | `Numeric(Byte)` | `%222.0g` |
| `ft018e_5` | Value inheritance 5 | `Numeric(Double)` | `%222.0g` |
| `ft018ub_5` | Value inheritance 5 ub | `Numeric(Byte)` | `%222.0g` |
| `ft018v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `ft018v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `ft018v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `ft021_` | Who answered the questions in ft | `Numeric(Byte)` | `%20.0f` |

### `gs` - Grip Strength

- Dataset: `sharew1_rel9-0-0_gs.dta`
- Read with: `ps.read_share_module("gs", wave=1)`
- Rows: 30,416
- Variables: 13
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `gs001_` | Willing to have handgrip measured | `Numeric(Byte)` | `%31.0f` |
| `gs002_` | Record respondent status | `Numeric(Byte)` | `%48.0f` |
| `gs004_` | Dominant hand | `Numeric(Byte)` | `%13.0f` |
| `gs006_` | 1st measurement: left hand | `Numeric(Byte)` | `%10.0f` |
| `gs007_` | 2nd measurement: left hand | `Numeric(Byte)` | `%10.0f` |
| `gs008_` | 1st measurement: right hand | `Numeric(Byte)` | `%10.0f` |
| `gs009_` | 2nd measurement: right hand | `Numeric(Byte)` | `%10.0f` |

### `hc` - Health Care

- Dataset: `sharew1_rel9-0-0_hc.dta`
- Read with: `ps.read_share_module("hc", wave=1)`
- Rows: 30,416
- Variables: 157
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `hc002_` | How often seen or talked to medical doctor last 12 months | `Numeric(Byte)` | `%10.0f` |
| `hc003_` | How many of these contacts with general practitioner | `Numeric(Byte)` | `%10.0f` |
| `hc004_` | Contacts with specialists | `Numeric(Byte)` | `%10.0f` |
| `hc005_` | Most recent consulted specialist | `Numeric(Byte)` | `%89.0f` |
| `hc006_` | Type of last consultation to specialist | `Numeric(Byte)` | `%66.0f` |
| `hc007_` | Days waiting for emergency consultation to specialist | `Numeric(Byte)` | `%10.0f` |
| `hc008_` | Weeks waiting for non-emergency consultation | `Numeric(Byte)` | `%10.0f` |
| `hc009_` | Wish last specialist contact earlier | `Numeric(Byte)` | `%10.0f` |
| `hc010_` | Seen a dentist/dental hygienist in the last 12 months | `Numeric(Byte)` | `%10.0f` |
| `hc011_` | Contact dentist for routine control/prevention or treatment | `Numeric(Byte)` | `%38.0f` |
| `hc012_` | Stayed over night in hospital last 12 months | `Numeric(Byte)` | `%10.0f` |
| `hc013_` | Times being patient in hospital | `Numeric(Byte)` | `%10.0f` |
| `hc014_` | Total nights stayed in hospital | `Numeric(Int)` | `%10.0f` |
| `hc015d1` | Reason hospital: inpatient surgery | `Numeric(Byte)` | `%12.0g` |
| `hc015d2` | Reason hospital: medical tests or non-surgical treatments | `Numeric(Byte)` | `%12.0g` |
| `hc015d3` | Reason hospital: mental health problems | `Numeric(Byte)` | `%12.0g` |
| `hc016_` | Times overnight in hospital for surgery | `Numeric(Byte)` | `%10.0f` |
| `hc017_` | Had inpatient surgery last 12 months | `Numeric(Byte)` | `%10.0f` |
| `hc018_` | Which inpatient surgery | `Numeric(Byte)` | `%64.0f` |
| `hc019_` | Planned or emergency inpatient surgery | `Numeric(Byte)` | `%17.0f` |
| `hc020_` | Months waiting for last inpatient surgery | `Numeric(Byte)` | `%10.0f` |
| `hc021_` | Wish last inpatient surgery earlier | `Numeric(Byte)` | `%10.0f` |
| `hc022_` | Times overnight in hospital for mental health problems | `Numeric(Byte)` | `%10.0f` |
| `hc023_` | Had outpatient surgery last 12 months | `Numeric(Byte)` | `%10.0f` |
| `hc024_` | Times had outpatient surgery last 12 months | `Numeric(Byte)` | `%10.0f` |
| `hc025_` | Any of these outpatient surgeries last 12 months | `Numeric(Byte)` | `%10.0f` |
| `hc026_` | Which outpatient surgery | `Numeric(Byte)` | `%59.0f` |
| `hc027_` | Months waiting for last outpatient surgery | `Numeric(Byte)` | `%10.0f` |
| `hc028_` | Wish last outpatient surgery earlier | `Numeric(Byte)` | `%10.0f` |
| `hc029_` | In a nursing home during last 12 months | `Numeric(Byte)` | `%16.0f` |
| `hc030_` | Times stayed in a nursing home overnight | `Numeric(Int)` | `%10.0f` |
| `hc031_` | Weeks stayed in a nursing home | `Numeric(Byte)` | `%10.0f` |
| `hc032d1` | Received home care: nursing or personal care | `Numeric(Byte)` | `%12.0g` |
| `hc032d2` | Received home care: domestic tasks | `Numeric(Byte)` | `%12.0g` |
| `hc032d3` | Received home care: meals-on-wheels | `Numeric(Byte)` | `%12.0g` |
| `hc032dno` | Received home care: none of these | `Numeric(Byte)` | `%12.0g` |
| `hc033_` | Weeks received professional nursing care | `Numeric(Byte)` | `%10.0f` |
| `hc034_` | Hours received professional nursing care | `Numeric(Int)` | `%10.0f` |
| `hc035_` | Weeks received paid domestic help | `Numeric(Byte)` | `%10.0f` |
| `hc036_` | Hours received paid domestic help | `Numeric(Int)` | `%10.0f` |
| `hc037_` | Weeks received meals-on-wheels | `Numeric(Byte)` | `%10.0f` |
| `hc038_` | Received care from private providers | `Numeric(Byte)` | `%10.0f` |
| `hc039d1` | Received care: surgery | `Numeric(Byte)` | `%12.0g` |
| `hc039d2` | Received care: care from general practitioner | `Numeric(Byte)` | `%12.0g` |
| `hc039d3` | Received care: care from specialist physician | `Numeric(Byte)` | `%12.0g` |
| `hc039d4` | Received care: drugs | `Numeric(Byte)` | `%12.0g` |
| `hc039d5` | Received care: dental care | `Numeric(Byte)` | `%12.0g` |
| `hc039d6` | Received care: hospital rehabilitation | `Numeric(Byte)` | `%12.0g` |
| `hc039d7` | Received care: ambulatory rehabilitation | `Numeric(Byte)` | `%12.0g` |
| `hc039d8` | Received care: aids and appliances | `Numeric(Byte)` | `%12.0g` |
| `hc039d9` | Received care: care in nursing home | `Numeric(Byte)` | `%12.0g` |
| `hc039d10` | Received care: home care | `Numeric(Byte)` | `%12.0g` |
| `hc039d11` | Received care: paid home help | `Numeric(Byte)` | `%12.0g` |
| `hc039dot` | Received care: other | `Numeric(Byte)` | `%12.0g` |
| `hc040_` | Forgo any types of care because of costs | `Numeric(Byte)` | `%10.0f` |
| `hc041d1` | Too costly care: surgery | `Numeric(Byte)` | `%12.0g` |
| `hc041d2` | Too costly care: care from general practitioner | `Numeric(Byte)` | `%12.0g` |
| `hc041d3` | Too costly care: care from specialist physician | `Numeric(Byte)` | `%12.0g` |
| `hc041d4` | Too costly care: drugs | `Numeric(Byte)` | `%12.0g` |
| `hc041d5` | Too costly care: dental care | `Numeric(Byte)` | `%12.0g` |
| `hc041d6` | Too costly care: hospital rehabilitation | `Numeric(Byte)` | `%12.0g` |
| `hc041d7` | Too costly care: ambulatory rehabilitation | `Numeric(Byte)` | `%12.0g` |
| `hc041d8` | Too costly care: aids and appliances | `Numeric(Byte)` | `%12.0g` |
| `hc041d9` | Too costly care: care in nursing home | `Numeric(Byte)` | `%12.0g` |
| `hc041d10` | Too costly care: home care | `Numeric(Byte)` | `%12.0g` |
| `hc041d11` | Too costly care: paid home help | `Numeric(Byte)` | `%12.0g` |
| `hc041dot` | Too costly care: other | `Numeric(Byte)` | `%12.0g` |
| `hc042_` | Forgo any types of care because unavailable | `Numeric(Byte)` | `%10.0f` |
| `hc043d1` | Unavailable care: surgery | `Numeric(Byte)` | `%12.0g` |
| `hc043d2` | Unavailable care: care from general practitioner | `Numeric(Byte)` | `%12.0g` |
| `hc043d3` | Unavailable care: care from specialist physician | `Numeric(Byte)` | `%12.0g` |
| `hc043d4` | Unavailable care: drugs | `Numeric(Byte)` | `%12.0g` |
| `hc043d5` | Unavailable care: dental care | `Numeric(Byte)` | `%12.0g` |
| `hc043d6` | Unavailable care: hospital rehabilitation | `Numeric(Byte)` | `%12.0g` |
| `hc043d7` | Unavailable care: ambulatory rehabilitation | `Numeric(Byte)` | `%12.0g` |
| `hc043d8` | Unavailable care: aids and appliances | `Numeric(Byte)` | `%12.0g` |
| `hc043d9` | Unavailable care: care in nursing home | `Numeric(Byte)` | `%12.0g` |
| `hc043d10` | Unavailable care: home care | `Numeric(Byte)` | `%12.0g` |
| `hc043d11` | Unavailable care: paid home help | `Numeric(Byte)` | `%12.0g` |
| `hc043dot` | Unavailable care: other | `Numeric(Byte)` | `%12.0g` |
| `hc045e` | Paid out-of-pocket for inpatient care | `Numeric(Double)` | `%222.0g` |
| `hc045ub` | Paid out-of-pocket for inpatient care ub | `Numeric(Byte)` | `%222.0g` |
| `hc045v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `hc045v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `hc045v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `hc047e` | Paid out-of-pocket for outpatient care | `Numeric(Double)` | `%222.0g` |
| `hc047ub` | Paid out-of-pocket for outpatient care ub | `Numeric(Byte)` | `%222.0g` |
| `hc047v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `hc047v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `hc047v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `hc049e` | Paid out-of-pocket for prescribed drugs | `Numeric(Double)` | `%222.0g` |
| `hc049ub` | Paid out-of-pocket for prescribed drugs ub | `Numeric(Byte)` | `%222.0g` |
| `hc049v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `hc049v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `hc049v3` | Bracket value 3 | `Numeric(Float)` | `%19.0f` |
| `hc051e` | Paid out-of-pocket for nursing home, day-care and home-care | `Numeric(Double)` | `%222.0g` |
| `hc051ub` | Paid out-of-pocket for nursing home, day-care and home-care ub | `Numeric(Byte)` | `%222.0g` |
| `hc051v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `hc051v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `hc051v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `hc053_` | Basic health insurance category | `Numeric(Byte)` | `%60.0f` |
| `hc054e` | Deduction basic health insurance | `Numeric(Double)` | `%222.0g` |
| `hc055_` | Basic health insurance gatekeeping | `Numeric(Byte)` | `%10.0f` |
| `hc056_` | Basic health insurance limit choice | `Numeric(Byte)` | `%10.0f` |
| `hc057_` | Basic health insurance coverage | `Numeric(Byte)` | `%10.0f` |
| `hc058_` | Basic health insurance status | `Numeric(Byte)` | `%44.0f` |
| `hc059d1` | Voluntary health insurance: direct access to specialists | `Numeric(Byte)` | `%12.0g` |
| `hc059d2` | Voluntary health insurance: access to specialists through a general practitioner | `Numeric(Byte)` | `%12.0g` |
| `hc059d3` | Voluntary health insurance: unrestricted choice of doctors | `Numeric(Byte)` | `%12.0g` |
| `hc059d4` | Voluntary health insurance: limited choice of doctors | `Numeric(Byte)` | `%12.0g` |
| `hc059d5` | Voluntary health insurance: dental care | `Numeric(Byte)` | `%12.0g` |
| `hc059d6` | Voluntary health insurance: full coverage of drugs expenses | `Numeric(Byte)` | `%12.0g` |
| `hc059d7` | Voluntary health insurance: partial coverage of drugs expenses | `Numeric(Byte)` | `%12.0g` |
| `hc059d8` | Voluntary health insurance: unrestricted choice of hospitals | `Numeric(Byte)` | `%12.0g` |
| `hc059d9` | Voluntary health insurance: limited choice of hospitals | `Numeric(Byte)` | `%12.0g` |
| `hc059d10` | Voluntary health insurance: long term care in nursing home | `Numeric(Byte)` | `%12.0g` |
| `hc059d11` | Voluntary health insurance: nursing care at home | `Numeric(Byte)` | `%12.0g` |
| `hc059d12` | Voluntary health insurance: home help | `Numeric(Byte)` | `%12.0g` |
| `hc059dno` | Voluntary health insurance: none of these | `Numeric(Byte)` | `%12.0g` |
| `hc059dot` | Voluntary health insurance: other | `Numeric(Byte)` | `%12.0g` |
| `hc060d1` | Voluntary supplementary health insurance: country-specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `hc060d2` | Voluntary supplementary health insurance: country-specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `hc060d3` | Voluntary supplementary health insurance: country-specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `hc060d4` | Voluntary supplementary health insurance: country-specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `hc060d5` | Voluntary supplementary health insurance: country-specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `hc060d6` | Voluntary supplementary health insurance: country-specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `hc060d7` | Voluntary supplementary health insurance: country-specific category 7 | `Numeric(Byte)` | `%12.0g` |
| `hc060d8` | Voluntary supplementary health insurance: country-specific category 8 | `Numeric(Byte)` | `%12.0g` |
| `hc060d9` | Voluntary supplementary health insurance: country-specific category 9 | `Numeric(Byte)` | `%12.0g` |
| `hc060d10` | Voluntary supplementary health insurance: country-specific category 10 | `Numeric(Byte)` | `%12.0g` |
| `hc060d11` | Voluntary supplementary health insurance: country-specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `hc060d12` | Voluntary supplementary health insurance: country-specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `hc060d13` | Voluntary supplementary health insurance: country-specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `hc060d14` | Voluntary supplementary health insurance: country-specific category 14 | `Numeric(Byte)` | `%12.0g` |
| `hc060d15` | Voluntary supplementary health insurance: country-specific category 15 | `Numeric(Byte)` | `%12.0g` |
| `hc060d16` | Voluntary supplementary health insurance: country-specific category 16 | `Numeric(Byte)` | `%12.0g` |
| `hc060d17` | Voluntary supplementary health insurance: country-specific category 17 | `Numeric(Byte)` | `%12.0g` |
| `hc060d18` | Voluntary supplementary health insurance: country-specific category 18 | `Numeric(Byte)` | `%12.0g` |
| `hc060d19` | Voluntary supplementary health insurance: country-specific category 19 | `Numeric(Byte)` | `%12.0g` |
| `hc060d20` | Voluntary supplementary health insurance: country-specific category 20 | `Numeric(Byte)` | `%12.0g` |
| `hc060d21` | Voluntary supplementary health insurance: country-specific category 21 | `Numeric(Byte)` | `%12.0g` |
| `hc060d22` | Voluntary supplementary health insurance: country-specific category 22 | `Numeric(Byte)` | `%12.0g` |
| `hc060dno` | Voluntary supplementary health insurance: none of these | `Numeric(Byte)` | `%12.0g` |
| `hc060dot` | Voluntary supplementary health insurance: other | `Numeric(Byte)` | `%12.0g` |
| `hc061e` | Pay for all voluntary health insurance contracts | `Numeric(Double)` | `%222.0g` |
| `hc061ub` | Pay for all voluntary health insurance contracts ub | `Numeric(Byte)` | `%222.0g` |
| `hc061v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `hc061v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `hc061v3` | Bracket value 3 | `Numeric(Float)` | `%19.0f` |
| `hc063_` | Who answered the questions in hc | `Numeric(Byte)` | `%20.0f` |

### `hh` - Household Income

- Dataset: `sharew1_rel9-0-0_hh.dta`
- Read with: `ps.read_share_module("hh", wave=1)`
- Rows: 30,416
- Variables: 20
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `hh001_` | Other contributor to household income | `Numeric(Byte)` | `%10.0f` |
| `hh002e` | Total income (other) household members last year | `Numeric(Double)` | `%222.0g` |
| `hh002ub` | Total income (other) household members last year ub | `Numeric(Byte)` | `%222.0g` |
| `hh002v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `hh002v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `hh002v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `hh010_` | Income from other sources | `Numeric(Byte)` | `%10.0f` |
| `hh011e` | Additional income received by all hh-members last year | `Numeric(Double)` | `%222.0g` |
| `hh011ub` | Additional income received by all hh-members last year ub | `Numeric(Byte)` | `%222.0g` |
| `hh011v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `hh011v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `hh011v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `hh014_` | Who answered the question in hh | `Numeric(Byte)` | `%20.0f` |

### `ho` - Housing

- Dataset: `sharew1_rel9-0-0_ho.dta`
- Read with: `ps.read_share_module("ho", wave=1)`
- Rows: 30,416
- Variables: 68
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `ho001_` | Interview in house of respondent | `Numeric(Byte)` | `%10.0f` |
| `ho002_` | Owner, tenant or rent free | `Numeric(Byte)` | `%23.0f` |
| `ho003_` | Rent payment period | `Numeric(Byte)` | `%22.0f` |
| `ho005e` | Amount last rent payment | `Numeric(Double)` | `%222.0g` |
| `ho005ub` | Amount last rent payment ub | `Numeric(Byte)` | `%222.0g` |
| `ho005v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `ho005v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `ho005v3` | Bracket value 3 | `Numeric(Float)` | `%19.0f` |
| `ho007_` | Last rent payment included all charges and services | `Numeric(Byte)` | `%10.0f` |
| `ho008e` | Amount charges and services | `Numeric(Double)` | `%222.0g` |
| `ho008ub` | Amount charges and services ub | `Numeric(Byte)` | `%222.0g` |
| `ho008v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `ho008v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `ho008v3` | Bracket value 3 | `Numeric(Float)` | `%19.0f` |
| `ho010_` | More than two months behind with rent | `Numeric(Byte)` | `%10.0f` |
| `ho011_` | How property acquired | `Numeric(Byte)` | `%55.0f` |
| `ho012_` | Year acquired property | `Numeric(Int)` | `%10.0f` |
| `ho013_` | Mortgages or loans on property | `Numeric(Byte)` | `%10.0f` |
| `ho014_` | Years left of mortgage or loan | `Numeric(Byte)` | `%10.0f` |
| `ho015e` | Amount still to pay on mortgage or loan | `Numeric(Double)` | `%222.0g` |
| `ho015ub` | Amount still to pay on mortgage or loan ub | `Numeric(Byte)` | `%222.0g` |
| `ho015v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `ho015v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `ho015v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `ho017_` | Regularly repay mortgage or loans | `Numeric(Byte)` | `%10.0f` |
| `ho018_` | period repay mortgage or loan | `Numeric(Byte)` | `%22.0f` |
| `ho020e` | Amount regular repayments on mortgage or loan | `Numeric(Double)` | `%222.0g` |
| `ho020ub` | Amount regular repayments on mortgage or loan ub | `Numeric(Byte)` | `%222.0g` |
| `ho020v1` | Bracket value 1 | `Numeric(Float)` | `%19.0f` |
| `ho020v2` | Bracket value 2 | `Numeric(Float)` | `%19.0f` |
| `ho020v3` | Bracket value 3 | `Numeric(Float)` | `%19.0f` |
| `ho022_` | Behind with regular repay mortgage or loan | `Numeric(Byte)` | `%10.0f` |
| `ho023_` | Sublet or let parts of accommodation | `Numeric(Byte)` | `%10.0f` |
| `ho024e` | Value of property | `Numeric(Double)` | `%222.0g` |
| `ho024ub` | Value of property ub | `Numeric(Byte)` | `%222.0g` |
| `ho024v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `ho024v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `ho024v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `ho026_` | Own other real estate | `Numeric(Byte)` | `%10.0f` |
| `ho027e` | Value of other real estate | `Numeric(Double)` | `%222.0g` |
| `ho027ub` | Value of other real estate ub | `Numeric(Byte)` | `%222.0g` |
| `ho027v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `ho027v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `ho027v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `ho029_` | Received income or rent of other real estate | `Numeric(Byte)` | `%10.0f` |
| `ho030e` | Amount income or rent of other real estate last year | `Numeric(Double)` | `%222.0g` |
| `ho030ub` | Amount income or rent of other real estate last year ub | `Numeric(Byte)` | `%222.0g` |
| `ho030v1` | Bracket value 1 | `Numeric(Double)` | `%19.0f` |
| `ho030v2` | Bracket value 2 | `Numeric(Double)` | `%19.0f` |
| `ho030v3` | Bracket value 3 | `Numeric(Double)` | `%19.0f` |
| `ho032_` | Number of rooms in accommodation | `Numeric(Byte)` | `%10.0f` |
| `ho033_` | Special features in accommodation | `Numeric(Byte)` | `%10.0f` |
| `ho034_` | Years in accommodation | `Numeric(Int)` | `%10.0f` |
| `ho035_` | Years in community | `Numeric(Int)` | `%10.0f` |
| `ho036_` | Type of building | `Numeric(Byte)` | `%61.0f` |
| `ho037_` | Area where respondent lives | `Numeric(Byte)` | `%38.0f` |
| `ho038_` | Spend regulary time in other residence | `Numeric(Byte)` | `%10.0f` |
| `ho039_` | Location of other residence | `Numeric(Byte)` | `%30.0f` |
| `ho041_` | Who answered the questions in ho | `Numeric(Byte)` | `%20.0f` |
| `ho042_` | Number of floors of building | `Numeric(Byte)` | `%10.0f` |
| `ho043_` | Number of steps to entrance | `Numeric(Byte)` | `%12.0f` |

### `iv` - Interviewer Observations

- Dataset: `sharew1_rel9-0-0_iv.dta`
- Read with: `ps.read_share_module("iv", wave=1)`
- Rows: 30,416
- Variables: 42
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
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
| `iv003_` | Intervened in interview | `Numeric(Byte)` | `%17.0f` |
| `iv004_` | Willingness to answer | `Numeric(Byte)` | `%58.0f` |
| `iv005d1` | Why willingness worse: respondent was losing interest | `Numeric(Byte)` | `%12.0g` |
| `iv005d2` | Why willingness worse: respondent was losing concentration | `Numeric(Byte)` | `%12.0g` |
| `iv005d3` | Why willingness worse: other | `Numeric(Byte)` | `%12.0g` |
| `iv007_` | Respondent asked for clarification | `Numeric(Byte)` | `%12.0f` |
| `iv008_` | Respondent understood questions | `Numeric(Byte)` | `%12.0f` |
| `iv009_` | Which area building located | `Numeric(Byte)` | `%42.0f` |
| `iv010_` | Type of building | `Numeric(Byte)` | `%61.0f` |
| `iv011_` | Number of floors of building | `Numeric(Byte)` | `%10.0f` |
| `iv012_` | Number of steps to entrance | `Numeric(Byte)` | `%12.0f` |
| `iv013_` | Sex of interviewer | `Numeric(Byte)` | `%10.0f` |
| `iv014_` | Age of interviewer | `Numeric(Byte)` | `%10.0f` |
| `iv015_` | Highest school interviewer | `Numeric(Byte)` | `%47.0f` |
| `iv016d1` | Higher/vocational degree interviewer: country-specific category 1 | `Numeric(Byte)` | `%12.0g` |
| `iv016d2` | Higher/vocational degree interviewer: country-specific category 2 | `Numeric(Byte)` | `%12.0g` |
| `iv016d3` | Higher/vocational degree interviewer: country-specific category 3 | `Numeric(Byte)` | `%12.0g` |
| `iv016d4` | Higher/vocational degree interviewer: country-specific category 4 | `Numeric(Byte)` | `%12.0g` |
| `iv016d5` | Higher/vocational degree interviewer: country-specific category 5 | `Numeric(Byte)` | `%12.0g` |
| `iv016d6` | Higher/vocational degree interviewer: country-specific category 6 | `Numeric(Byte)` | `%12.0g` |
| `iv016d11` | Higher/vocational degree interviewer: country-specific category 11 | `Numeric(Byte)` | `%12.0g` |
| `iv016d12` | Higher/vocational degree interviewer: country-specific category 12 | `Numeric(Byte)` | `%12.0g` |
| `iv016d13` | Higher/vocational degree interviewer: country-specific category 13 | `Numeric(Byte)` | `%12.0g` |
| `iv016d95` | Higher/vocational degree interviewer: country-specific category 95 | `Numeric(Byte)` | `%12.0g` |
| `iv016dno` | Higher/vocational degree interviewer: none of these | `Numeric(Byte)` | `%12.0g` |
| `iv016dot` | Higher/vocational degree interviewer: other | `Numeric(Byte)` | `%12.0g` |
| `iv018_` | Help needed reading showcards | `Numeric(Byte)` | `%30.0f` |
| `iv020_` | Relationship proxy | `Numeric(Byte)` | `%37.0f` |

### `mh` - Mental Health

- Dataset: `sharew1_rel9-0-0_mh.dta`
- Read with: `ps.read_share_module("mh", wave=1)`
- Rows: 30,416
- Variables: 26
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `mh002_` | Sad or depressed last month | `Numeric(Byte)` | `%10.0f` |
| `mh003_` | Hopes for the future | `Numeric(Byte)` | `%19.0f` |
| `mh004_` | Suicidal feelings or wish to be dead | `Numeric(Byte)` | `%61.0f` |
| `mh005_` | Feels guilty | `Numeric(Byte)` | `%64.0f` |
| `mh006_` | Blame for what | `Numeric(Byte)` | `%55.0f` |
| `mh007_` | Trouble sleeping | `Numeric(Byte)` | `%62.0f` |
| `mh008_` | Less or same interest in things | `Numeric(Byte)` | `%44.0f` |
| `mh009_` | Keeps up interest | `Numeric(Byte)` | `%10.0f` |
| `mh010_` | Irritability | `Numeric(Byte)` | `%10.0f` |
| `mh011_` | Appetite | `Numeric(Byte)` | `%35.0f` |
| `mh012_` | Eating more or less | `Numeric(Byte)` | `%21.0f` |
| `mh013_` | Fatigue | `Numeric(Byte)` | `%10.0f` |
| `mh014_` | Concentration on entertainment | `Numeric(Byte)` | `%60.0f` |
| `mh015_` | Concentration on reading | `Numeric(Byte)` | `%48.0f` |
| `mh016_` | Enjoyment | `Numeric(Byte)` | `%61.0f` |
| `mh017_` | Tearfulness | `Numeric(Byte)` | `%10.0f` |
| `mh018_` | Depression ever | `Numeric(Byte)` | `%10.0f` |
| `mh019_` | Age depression symptoms first time | `Numeric(Byte)` | `%10.0f` |
| `mh020_` | Ever treated for depression by doctor or psychiatrist | `Numeric(Byte)` | `%10.0f` |
| `mh021_` | Ever admitted to mental hospital or psychiatric ward | `Numeric(Byte)` | `%10.0f` |

### `ph` - Physical Health

- Dataset: `sharew1_rel9-0-0_ph.dta`
- Read with: `ps.read_share_module("ph", wave=1)`
- Rows: 30,416
- Variables: 137
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `phrandom` | Random assignment: Health in general questions | `Numeric(Byte)` | `%19.0f` |
| `ph002_` | Health in general question 1 | `Numeric(Byte)` | `%13.0f` |
| `ph003_` | Health in general question 2 | `Numeric(Byte)` | `%13.0f` |
| `ph004_` | Long-term illness | `Numeric(Byte)` | `%10.0f` |
| `ph005_` | Limited in activities because of health | `Numeric(Byte)` | `%32.0f` |
| `ph006d1` | Heart attack: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006d2` | High blood pressure or hypertension: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006d3` | High blood cholesterol: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006d4` | Stroke: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006d5` | Diabetes or high blood sugar: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006d6` | Chronic lung disease: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006d7` | Asthma: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006d8` | Arthritis: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006d9` | Osteoporosis: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006d10` | Cancer: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006d11` | Stomach or duodenal ulcer, peptic ulcer: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006d12` | Parkinson disease: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006d13` | Cataracts: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006d14` | Hip fracture or femoral fracture: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006dno` | None: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
| `ph006dot` | Other: ever diagnosed | `Numeric(Byte)` | `%12.0g` |
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
| `ph009_1` | Age heart attack or other heart problems | `Numeric(Byte)` | `%10.0f` |
| `ph009_2` | Age high blood pressure | `Numeric(Byte)` | `%10.0f` |
| `ph009_3` | Age high blood cholesterol | `Numeric(Byte)` | `%10.0f` |
| `ph009_4` | Age stroke or cerebral vascular disease | `Numeric(Byte)` | `%10.0f` |
| `ph009_5` | Age diabetes | `Numeric(Byte)` | `%10.0f` |
| `ph009_6` | Age chronic lung disease | `Numeric(Byte)` | `%10.0f` |
| `ph009_7` | Age asthma | `Numeric(Byte)` | `%10.0f` |
| `ph009_8` | Age arthritis or rheumatism | `Numeric(Byte)` | `%10.0f` |
| `ph009_9` | Age osteoporosis | `Numeric(Byte)` | `%10.0f` |
| `ph009_10` | Age cancer or malignant tumour | `Numeric(Int)` | `%10.0f` |
| `ph009_11` | Age stomach, duodenal or peptic ulcer | `Numeric(Byte)` | `%10.0f` |
| `ph009_12` | Age parkinson disease | `Numeric(Byte)` | `%10.0f` |
| `ph009_13` | Age cataracts | `Numeric(Byte)` | `%10.0f` |
| `ph009_14` | Age hip or femoral fracture | `Numeric(Byte)` | `%10.0f` |
| `ph009_97` | Age other condition | `Numeric(Int)` | `%10.0f` |
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
| `ph012_` | Weight of respondent | `Numeric(Double)` | `%10.2f` |
| `ph013_` | How tall are you? | `Numeric(Double)` | `%10.2f` |
| `ph024_` | Use dentures | `Numeric(Byte)` | `%10.0f` |
| `ph025_` | Bite on hard foods | `Numeric(Byte)` | `%10.0f` |
| `ph041_` | Wears glasses/contact lenses | `Numeric(Byte)` | `%10.0f` |
| `ph042_` | Eyesight | `Numeric(Byte)` | `%39.0f` |
| `ph043_` | Eyesight distance | `Numeric(Byte)` | `%13.0f` |
| `ph044_` | Eyesight reading | `Numeric(Byte)` | `%13.0f` |
| `ph045_` | Use hearing aid | `Numeric(Byte)` | `%10.0f` |
| `ph046_` | Hearing | `Numeric(Byte)` | `%13.0f` |
| `ph047_` | Hearing with background noise | `Numeric(Byte)` | `%10.0f` |
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
| `ph050_` | Help activities | `Numeric(Byte)` | `%10.0f` |
| `ph051_` | Help meets needs | `Numeric(Byte)` | `%12.0f` |
| `ph052_` | Health in general question 2 | `Numeric(Byte)` | `%13.0f` |
| `ph053_` | Health in general question 1 | `Numeric(Byte)` | `%13.0f` |
| `ph054_` | Who answered the questions in ph | `Numeric(Byte)` | `%20.0f` |
| `ph055_` | Hearing with several people | `Numeric(Byte)` | `%10.0f` |
| `ph056_` | Hearing with one person | `Numeric(Byte)` | `%10.0f` |

### `sp` - Social Support

- Dataset: `sharew1_rel9-0-0_sp.dta`
- Read with: `ps.read_share_module("sp", wave=1)`
- Rows: 30,416
- Variables: 169
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sp002_` | Received help from others (outside hh) | `Numeric(Byte)` | `%10.0f` |
| `sp003_1` | Who gave help: person 1 | `Numeric(Byte)` | `%18.0f` |
| `sp003_2` | Who gave help: person 2 | `Numeric(Byte)` | `%18.0f` |
| `sp003_3` | Who gave help: person 3 | `Numeric(Byte)` | `%18.0f` |
| `sp004d1_1` | Help provided from person 1: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp004d1_2` | Help provided from person 2: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp004d1_3` | Help provided from person 3: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp004d2_1` | Help provided from person 1: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp004d2_2` | Help provided from person 2: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp004d2_3` | Help provided from person 3: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp004d3_1` | Help provided from person 1: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp004d3_2` | Help provided from person 2: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp004d3_3` | Help provided from person 3: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp005_1` | How often received help: from person 1 | `Numeric(Byte)` | `%18.0f` |
| `sp005_2` | How often received help: from person 2 | `Numeric(Byte)` | `%18.0f` |
| `sp005_3` | How often received help: from person 3 | `Numeric(Byte)` | `%18.0f` |
| `sp006_1` | Hours received houshold help: person 1 | `Numeric(Int)` | `%10.0f` |
| `sp006_2` | Hours received houshold help: person 2 | `Numeric(Int)` | `%10.0f` |
| `sp006_3` | Hours received houshold help: person 3 | `Numeric(Int)` | `%10.0f` |
| `sp007_1` | Any other helper from outside the household | `Numeric(Byte)` | `%10.0f` |
| `sp007_2` | Any other helper from outside the household | `Numeric(Byte)` | `%10.0f` |
| `sp008_` | Given help last twelve months | `Numeric(Byte)` | `%10.0f` |
| `sp009_1` | To whom did you give help: person 1 | `Numeric(Byte)` | `%18.0f` |
| `sp009_2` | To whom did you give help: person 2 | `Numeric(Byte)` | `%18.0f` |
| `sp009_3` | To whom did you give help: person 3 | `Numeric(Byte)` | `%18.0f` |
| `sp010d1_1` | Help given person 1: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp010d1_2` | Help given person 2: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp010d1_3` | Help given person 3: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp010d2_1` | Help given person 1: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp010d2_2` | Help given person 2: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp010d2_3` | Help given person 3: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp010d3_1` | Help given person 1: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp010d3_2` | Help given person 2: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp010d3_3` | Help given person 3: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp011_1` | How often given help to person 1 | `Numeric(Byte)` | `%18.0f` |
| `sp011_2` | How often given help to person 2 | `Numeric(Byte)` | `%18.0f` |
| `sp011_3` | How often given help to person 3 | `Numeric(Byte)` | `%18.0f` |
| `sp012_1` | Hours given help to person 1 | `Numeric(Int)` | `%10.0f` |
| `sp012_2` | Hours given help to person 2 | `Numeric(Int)` | `%10.0f` |
| `sp012_3` | Hours given help to person 3 | `Numeric(Int)` | `%10.0f` |
| `sp013_1` | Have you given help to others | `Numeric(Byte)` | `%10.0f` |
| `sp013_2` | Have you given help to others | `Numeric(Byte)` | `%10.0f` |
| `sp014_` | Looked after grandchildren | `Numeric(Byte)` | `%10.0f` |
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
| `sp016_1` | How often did you look after child of child 1 | `Numeric(Byte)` | `%18.0f` |
| `sp016_2` | How often did you look after child of child 2 | `Numeric(Byte)` | `%18.0f` |
| `sp016_3` | How often did you look after child of child 3 | `Numeric(Byte)` | `%18.0f` |
| `sp016_4` | How often did you look after child of child 4 | `Numeric(Byte)` | `%18.0f` |
| `sp016_5` | How often did you look after child of child 5 | `Numeric(Byte)` | `%18.0f` |
| `sp016_6` | How often did you look after child of child 6 | `Numeric(Byte)` | `%18.0f` |
| `sp016_7` | How often did you look after child of child 7 | `Numeric(Byte)` | `%18.0f` |
| `sp016_8` | How often did you look after child of child 8 | `Numeric(Byte)` | `%18.0f` |
| `sp016_9` | How often did you look after child of child 9 | `Numeric(Byte)` | `%18.0f` |
| `sp016_10` | How often did you look after child of child 10 | `Numeric(Byte)` | `%18.0f` |
| `sp016_11` | How often did you look after child of child 11 | `Numeric(Byte)` | `%18.0f` |
| `sp016_12` | How often did you look after child of child 12 | `Numeric(Byte)` | `%18.0f` |
| `sp016_13` | How often did you look after child of child 13 | `Numeric(Byte)` | `%18.0f` |
| `sp016_14` | How often did you look after child of child 14 | `Numeric(Byte)` | `%18.0f` |
| `sp016_17` | How often do you look after child of child 17 | `Numeric(Byte)` | `%18.0f` |
| `sp017_1` | Hours looked after child(ren) of child 1 | `Numeric(Double)` | `%11.0g` |
| `sp017_2` | Hours looked after child(ren) of child 2 | `Numeric(Double)` | `%11.0g` |
| `sp017_3` | Hours looked after child(ren) of child 3 | `Numeric(Int)` | `%11.0g` |
| `sp017_4` | Hours looked after child(ren) of child 4 | `Numeric(Int)` | `%11.0g` |
| `sp017_5` | Hours looked after child(ren) of child 5 | `Numeric(Int)` | `%11.0g` |
| `sp017_6` | Hours looked after child(ren) of child 6 | `Numeric(Int)` | `%11.0g` |
| `sp017_7` | Hours looked after child(ren) of child 7 | `Numeric(Int)` | `%11.0g` |
| `sp017_8` | Hours looked after child(ren) of child 8 | `Numeric(Int)` | `%11.0g` |
| `sp017_9` | Hours looked after child(ren) of child 9 | `Numeric(Byte)` | `%11.0g` |
| `sp017_10` | Hours looked after child(ren) of child 10 | `Numeric(Byte)` | `%11.0g` |
| `sp017_11` | Hours looked after child(ren) of child 11 | `Numeric(Byte)` | `%11.0g` |
| `sp017_12` | Hours looked after child(ren) of child 12 | `Numeric(Byte)` | `%11.0g` |
| `sp017_13` | Hours looked after child(ren) of child 13 | `Numeric(Byte)` | `%11.0g` |
| `sp017_14` | Hours looked after child(ren) of child 14 | `Numeric(Byte)` | `%11.0g` |
| `sp017_17` | Hours looked after child(ren) of child 17 | `Numeric(Byte)` | `%11.0g` |
| `sp018_` | Given help to someone with personal care in the household | `Numeric(Byte)` | `%10.0f` |
| `sp019d1` | R provided help with personal care to: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sp019d2` | R provided help with personal care to: mother | `Numeric(Byte)` | `%12.0g` |
| `sp019d3` | R provided help with personal care to: father | `Numeric(Byte)` | `%12.0g` |
| `sp019d4` | R provided help with personal care to: mother-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp019d5` | R provided help with personal care to: father-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp019d6` | R provided help with personal care to: stepmother | `Numeric(Byte)` | `%12.0g` |
| `sp019d7` | R provided help with personal care to: stepfather | `Numeric(Byte)` | `%12.0g` |
| `sp019d8` | R provided help with personal care to: brother | `Numeric(Byte)` | `%12.0g` |
| `sp019d9` | R provided help with personal care to: sister | `Numeric(Byte)` | `%12.0g` |
| `sp019d10` | R provided help with personal care to: child 1 | `Numeric(Byte)` | `%12.0g` |
| `sp019d11` | R provided help with personal care to: child 2 | `Numeric(Byte)` | `%12.0g` |
| `sp019d12` | R provided help with personal care to: child 3 | `Numeric(Byte)` | `%12.0g` |
| `sp019d13` | R provided help with personal care to: child 4 | `Numeric(Byte)` | `%12.0g` |
| `sp019d14` | R provided help with personal care to: child 5 | `Numeric(Byte)` | `%12.0g` |
| `sp019d15` | R provided help with personal care to: child 6 | `Numeric(Byte)` | `%12.0g` |
| `sp019d16` | R provided help with personal care to: child 7 | `Numeric(Byte)` | `%12.0g` |
| `sp019d17` | R provided help with personal care to: child 8 | `Numeric(Byte)` | `%12.0g` |
| `sp019d18` | R provided help with personal care to: child 9 | `Numeric(Byte)` | `%12.0g` |
| `sp019d19` | R provided help with personal care to: other child | `Numeric(Byte)` | `%12.0g` |
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
| `sp019d33` | R provided help with personal care to: other acquaintance | `Numeric(Byte)` | `%12.0g` |
| `sp020_` | Someone in this household helped you regularly with personal care | `Numeric(Byte)` | `%10.0f` |
| `sp021d1` | R received help with personal care from: spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sp021d2` | R received help with personal care from: mother | `Numeric(Byte)` | `%12.0g` |
| `sp021d3` | R received help with personal care from: father | `Numeric(Byte)` | `%12.0g` |
| `sp021d4` | R received help with personal care from: mother-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp021d5` | R received help with personal care from: father-in-law | `Numeric(Byte)` | `%12.0g` |
| `sp021d6` | R received help with personal care from: stepmother | `Numeric(Byte)` | `%12.0g` |
| `sp021d7` | R received help with personal care from: stepfather | `Numeric(Byte)` | `%12.0g` |
| `sp021d8` | R received help with personal care from: brother | `Numeric(Byte)` | `%12.0g` |
| `sp021d9` | R received help with personal care from: sister | `Numeric(Byte)` | `%12.0g` |
| `sp021d10` | R received help with personal care from: child 1 | `Numeric(Byte)` | `%12.0g` |
| `sp021d11` | R received help with personal care from: child 2 | `Numeric(Byte)` | `%12.0g` |
| `sp021d12` | R received help with personal care from: child 3 | `Numeric(Byte)` | `%12.0g` |
| `sp021d13` | R received help with personal care from: child 4 | `Numeric(Byte)` | `%12.0g` |
| `sp021d14` | R received help with personal care from: child 5 | `Numeric(Byte)` | `%12.0g` |
| `sp021d15` | R received help with personal care from: child 6 | `Numeric(Byte)` | `%12.0g` |
| `sp021d16` | R received help with personal care from: child 7 | `Numeric(Byte)` | `%12.0g` |
| `sp021d17` | R received help with personal care from: child 8 | `Numeric(Byte)` | `%12.0g` |
| `sp021d18` | R received help with personal care from: child 9 | `Numeric(Byte)` | `%12.0g` |
| `sp021d19` | R received help with personal care from: other child | `Numeric(Byte)` | `%12.0g` |
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
| `sp021d33` | R received help with personal care from: other acquaintance | `Numeric(Byte)` | `%12.0g` |
| `sp022_` | Who answered the questions in sp | `Numeric(Byte)` | `%20.0f` |

### `ws` - Walking Speed

- Dataset: `sharew1_rel9-0-0_ws.dta`
- Read with: `ps.read_share_module("ws", wave=1)`
- Rows: 30,416
- Variables: 19
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ws001_` | Record respondent status | `Numeric(Byte)` | `%60.0f` |
| `ws002_` | Able to walk alone (using aid) | `Numeric(Byte)` | `%34.0f` |
| `ws003_` | Is it safe to carry out the test | `Numeric(Byte)` | `%39.0f` |
| `ws004_` | Respondent willing to do walking test | `Numeric(Byte)` | `%10.0f` |
| `ws005_` | Does respondent feel safe to continue | `Numeric(Byte)` | `%10.0f` |
| `ws007_` | Check available space for test | `Numeric(Byte)` | `%24.0f` |
| `ws010_` | Result of first trial | `Numeric(Byte)` | `%58.0f` |
| `ws011_` | Time of first walking speed test | `Numeric(Double)` | `%10.2f` |
| `ws012_` | Result of second trial | `Numeric(Byte)` | `%58.0f` |
| `ws013_` | Time of second walking speed test | `Numeric(Double)` | `%10.2f` |
| `ws014_` | Did the respondent have comment on pain | `Numeric(Byte)` | `%10.0f` |
| `ws015_` | Record type of floor surface | `Numeric(Byte)` | `%21.0f` |
| `ws017_` | Type of aid used during test | `Numeric(Byte)` | `%21.0f` |


## Special Modules

### `dropoff` - Paper-and-pencil drop-off

- Dataset: `sharew1_rel9-0-0_dropoff.dta`
- Read with: `ps.read_share_module("dropoff", wave=1)`
- Rows: 20,190
- Variables: 216
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `q1` | How satisfied with life in general | `Numeric(Byte)` | `%21.0f` |
| `q2_a` | My age prevents me from doing things I would like to | `Numeric(Byte)` | `%41.0f` |
| `q2_b` | I feel that what happens to me is out of my control | `Numeric(Byte)` | `%41.0f` |
| `q2_c` | I feel left out of things | `Numeric(Byte)` | `%41.0f` |
| `q2_d` | I can do the things I want to | `Numeric(Byte)` | `%41.0f` |
| `q2_e` | Family responsibilities prevent me from doing what I want to | `Numeric(Byte)` | `%41.0f` |
| `q2_f` | Shortage of money stops me from doing things I want to do | `Numeric(Byte)` | `%41.0f` |
| `q2_g` | I look forward to each day | `Numeric(Byte)` | `%41.0f` |
| `q2_h` | I feel that my life has a meaning | `Numeric(Byte)` | `%41.0f` |
| `q2_i` | On balance, I look back on my life with a sense of happiness | `Numeric(Byte)` | `%41.0f` |
| `q2_j` | I feel full of energy these days | `Numeric(Byte)` | `%41.0f` |
| `q2_k` | I feel that life is full of opportunities | `Numeric(Byte)` | `%41.0f` |
| `q2_l` | I feel that the future looks good for me | `Numeric(Byte)` | `%41.0f` |
| `q3_a` | I pursue my goals with lots of energy | `Numeric(Byte)` | `%41.0f` |
| `q3_b` | In uncertain times, I usually expect the best | `Numeric(Byte)` | `%41.0f` |
| `q3_c` | I'm always optimistic about my future | `Numeric(Byte)` | `%41.0f` |
| `q3_d` | I hardly ever expect things to go my way | `Numeric(Byte)` | `%41.0f` |
| `q3_e` | I still find ways to solve a problem if others have given up | `Numeric(Byte)` | `%41.0f` |
| `q3_f` | I rarely count on good things happening to me | `Numeric(Byte)` | `%41.0f` |
| `q3_g` | Given my previous experiences I feel well prepared for my future | `Numeric(Byte)` | `%41.0f` |
| `q4_a` | I felt depressed | `Numeric(Byte)` | `%23.0f` |
| `q4_b` | I felt that everything I did was an effort | `Numeric(Byte)` | `%23.0f` |
| `q4_c` | My sleep was restless | `Numeric(Byte)` | `%23.0f` |
| `q4_d` | I was happy | `Numeric(Byte)` | `%23.0f` |
| `q4_e` | I felt lonely | `Numeric(Byte)` | `%23.0f` |
| `q4_f` | I felt people were unfriendly | `Numeric(Byte)` | `%23.0f` |
| `q4_g` | I enjoyed life | `Numeric(Byte)` | `%23.0f` |
| `q4_h` | I felt sad | `Numeric(Byte)` | `%23.0f` |
| `q4_i` | I felt that people disliked me | `Numeric(Byte)` | `%23.0f` |
| `q4_j` | I could not get going | `Numeric(Byte)` | `%23.0f` |
| `q4_k` | I did not feel like eating/my appetite was poor | `Numeric(Byte)` | `%23.0f` |
| `q4_l` | I had a lot of energy | `Numeric(Byte)` | `%23.0f` |
| `q4_m` | I felt tired | `Numeric(Byte)` | `%23.0f` |
| `q4_n` | I felt really rested when I woke up in the morning | `Numeric(Byte)` | `%23.0f` |
| `q5_a` | Always satisfied w. balance btwn. what given partner & what received in return | `Numeric(Byte)` | `%39.0f` |
| `q5_b` | Always received adequate appreciation for providing help in my family | `Numeric(Byte)` | `%39.0f` |
| `q5_c` | Always satisfied with rewards received for efforts in current major activity | `Numeric(Byte)` | `%39.0f` |
| `q5_d` | Been seriously disappointed/hurt by someone to whom I gave my trust | `Numeric(Byte)` | `%39.0f` |
| `q6_a` | Parents duty: do the best for children even at own expense | `Numeric(Byte)` | `%41.0f` |
| `q6_b` | Grandparents duty: be there for grandchildren | `Numeric(Byte)` | `%41.0f` |
| `q6_c` | Grandparents duty: help grandchildren financially | `Numeric(Byte)` | `%41.0f` |
| `q6_d` | Grandparents duty: help looking after young grandchildren | `Numeric(Byte)` | `%41.0f` |
| `q7_a` | Financial support for older persons who are in need | `Numeric(Byte)` | `%14.0f` |
| `q7_b` | Help w. household chores for older persons in need: e.g. cleaning/washing | `Numeric(Byte)` | `%14.0f` |
| `q7_c` | Personal care for older persons in need: e.g. nursing/bathing/dressing | `Numeric(Byte)` | `%14.0f` |
| `q8_a` | Experiences conflict with: parents | `Numeric(Byte)` | `%39.0f` |
| `q8_b` | Experiences conflict with: parents-in-law | `Numeric(Byte)` | `%39.0f` |
| `q8_c` | Experiences conflict with: partner/spouse | `Numeric(Byte)` | `%39.0f` |
| `q8_d` | Experiences conflict with: children | `Numeric(Byte)` | `%39.0f` |
| `q8_e` | Experiences conflict with: other family members | `Numeric(Byte)` | `%39.0f` |
| `q8_f` | Experiences conflict with: friends/coworkers/acquaintances | `Numeric(Byte)` | `%39.0f` |
| `q9` | Conflicts with children(-in-law) over education of grandchild(ren) | `Numeric(Byte)` | `%39.0f` |
| `q10` | Ever shared a household with spouse/partner | `Numeric(Byte)` | `%29.0f` |
| `q11_a` | Main responsibility for: bringing up children | `Numeric(Byte)` | `%29.0f` |
| `q11_b` | Main responsibility for: earning money | `Numeric(Byte)` | `%29.0f` |
| `q11_c` | Main responsibility for: household chores | `Numeric(Byte)` | `%29.0f` |
| `q11_d` | Main responsibility for: caring for elderly | `Numeric(Byte)` | `%29.0f` |
| `q12` | Has a general practitioner | `Numeric(Byte)` | `%29.0f` |
| `q13_a` | How often does general practitioner: ask about physical activity | `Numeric(Byte)` | `%14.0f` |
| `q13_b` | How often does general practitioner: tell you to get exercise | `Numeric(Byte)` | `%14.0f` |
| `q13_c` | How often does general practitioner: ask about falling down | `Numeric(Byte)` | `%14.0f` |
| `q13_d` | How often does general practitioner: check your balance | `Numeric(Byte)` | `%14.0f` |
| `q13_e` | How often does general practitioner: check your weight | `Numeric(Byte)` | `%14.0f` |
| `q13_f` | How often does general practitioner: ask about any drugs | `Numeric(Byte)` | `%14.0f` |
| `q14` | Had a flu vaccination the last year | `Numeric(Byte)` | `%29.0f` |
| `q15` | Adviced to have a flu vaccination the last year | `Numeric(Byte)` | `%29.0f` |
| `q16` | Had any eye exam the last two years | `Numeric(Byte)` | `%29.0f` |
| `q17` | Had a mammogram the last two years (only women) | `Numeric(Byte)` | `%29.0f` |
| `q18` | Recommended to have a sigmoidoscopy/colonoscopy the past ten years | `Numeric(Byte)` | `%29.0f` |
| `q19` | Ever had a sigmoidoscopy/colonoscopy | `Numeric(Byte)` | `%27.0f` |
| `q20` | Had stool blood tested the past ten years | `Numeric(Byte)` | `%29.0f` |
| `q21` | Recommended by health care provider to have a stool blood test past ten years | `Numeric(Byte)` | `%29.0f` |
| `q22` | Been bothered by pain in joints for at least 6 months | `Numeric(Byte)` | `%29.0f` |
| `q23_a` | Pain in hips | `Numeric(Byte)` | `%12.0f` |
| `q23_b` | Pain in knees | `Numeric(Byte)` | `%12.0f` |
| `q23_c` | Pain in other joints (upper/lower limbs) | `Numeric(Byte)` | `%12.0f` |
| `q24` | Joint pain on most days | `Numeric(Byte)` | `%29.0f` |
| `q25` | Currently taking drugs for joint pain | `Numeric(Byte)` | `%29.0f` |
| `q26` | Joint pain controlled when taking drugs | `Numeric(Byte)` | `%12.0f` |
| `q27` | Told doctor about joint pain | `Numeric(Byte)` | `%29.0f` |
| `q28_a` | When told about joint pain: doctor checked joints | `Numeric(Byte)` | `%29.0f` |
| `q28_b` | When told about joint pain: doctor suggested a drug treatment | `Numeric(Byte)` | `%29.0f` |
| `q28_c` | When told about joint pain: doctor told about side effects from anti-inflammator | `Numeric(Byte)` | `%29.0f` |
| `q29_a` | Ever been sent to physioterapy/exercise program for joint pain | `Numeric(Byte)` | `%29.0f` |
| `q29_b` | Ever been told by doctor to have surgery/joint replacement | `Numeric(Byte)` | `%29.0f` |
| `q29_c` | Ever been sent to orthopaedic surgeon | `Numeric(Byte)` | `%29.0f` |
| `q30_a` | Accommodation has: indoor bath/shower for hh's personal use | `Numeric(Byte)` | `%29.0f` |
| `q30_b` | Accommodation has: indoor flushing toilet for hh's personal use | `Numeric(Byte)` | `%29.0f` |
| `q30_c` | Accommodation has: central heating | `Numeric(Byte)` | `%29.0f` |
| `q30_d` | Accommodation has: air condition | `Numeric(Byte)` | `%29.0f` |
| `q30_e` | Accommodation has: elevator | `Numeric(Byte)` | `%29.0f` |
| `q30_f` | Accommodation has: balcony/terrace/garden | `Numeric(Byte)` | `%29.0f` |
| `q31_a` | Accommodation has enough space | `Numeric(Byte)` | `%29.0f` |
| `q31_b` | Accommodation costs too much | `Numeric(Byte)` | `%29.0f` |
| `q31_c` | Accommodation has enough light | `Numeric(Byte)` | `%29.0f` |
| `q31_d` | Accommodation has insufficient heating/cooling facilities | `Numeric(Byte)` | `%29.0f` |
| `q32_a` | Area has: suff. supply of pharmacy/medical care/grocery in reasonable distance | `Numeric(Byte)` | `%29.0f` |
| `q32_b` | Area has: sufficient possibilities for public transportation | `Numeric(Byte)` | `%29.0f` |
| `q32_c` | Area has: pollution/noise/other environmental problems | `Numeric(Byte)` | `%29.0f` |
| `q32_d` | Area has: vandalism/crime | `Numeric(Byte)` | `%29.0f` |
| `q33_a` | Pet(s) in hh: dog | `Numeric(Byte)` | `%12.0f` |
| `q33_b` | Pet(s) in hh: cat | `Numeric(Byte)` | `%12.0f` |
| `q33_c` | Pet(s) in hh: bird | `Numeric(Byte)` | `%12.0f` |
| `q33_d` | Pet(s) in hh: fish | `Numeric(Byte)` | `%12.0f` |
| `q33_e` | Pet(s) in hh: other | `Numeric(Byte)` | `%12.0f` |
| `q33_f` | No pet(s) in hh | `Numeric(Byte)` | `%12.0f` |
| `q34_raw` | Religion belonging or feeling attached to mostly (raw) | `Numeric(Byte)` | `%30.0f` |
| `q34_re` | Religion belonging or feeling attached to mostly | `Numeric(Byte)` | `%10.0g` |
| `q35` | About how often do you pray? | `Numeric(Byte)` | `%26.0f` |
| `q36` | Has been educated religiously by parents | `Numeric(Byte)` | `%29.0f` |
| `q37` | Party preference | `Numeric(Byte)` | `%30.0f` |
| `il_b105` | Country of birth | `Numeric(Byte)` | `%13.0g` |
| `il_b106` | Fathers country of birth | `Numeric(Byte)` | `%13.0g` |
| `il_b107` | Self-definition of identity | `Numeric(Byte)` | `%19.0g` |
| `ilq6` | Experienced the death of a (grand)child | `Numeric(Byte)` | `%29.0g` |
| `ilq7` | How old when experienced death of a (grand)child | `Numeric(Byte)` | `%8.0g` |
| `ilq8` | Effect on life: death of (grand)child | `Numeric(Byte)` | `%29.0g` |
| `ilq9` | Provided long term care to disabled/impaired relative | `Numeric(Byte)` | `%29.0g` |
| `ilq10` | How old when first provided long term care to disabled/impaired relative | `Numeric(Byte)` | `%8.0g` |
| `ilq11` | Effect on life: providing long term care | `Numeric(Byte)` | `%29.0g` |
| `ilq12` | Needed long term care due to difficulty in caring for yourself | `Numeric(Byte)` | `%29.0g` |
| `ilq13` | How old when first needed long term care | `Numeric(Byte)` | `%8.0g` |
| `ilq14` | Effect on life: needing long term care | `Numeric(Byte)` | `%29.0g` |
| `ilq15` | Experienced sexual assault (rape or harassment) | `Numeric(Byte)` | `%29.0g` |
| `ilq16` | How old when first experienced sexual assult | `Numeric(Byte)` | `%8.0g` |
| `ilq17` | Effect on life: experience of sexual assault | `Numeric(Byte)` | `%29.0g` |
| `ilq18` | Been victim of violence/abuse | `Numeric(Byte)` | `%29.0g` |
| `ilq19` | How old when first been victim of violence/abuese | `Numeric(Byte)` | `%8.0g` |
| `ilq20` | Effect on life: been victim of violence/abuese | `Numeric(Byte)` | `%29.0g` |
| `ilq21` | Been victim of crime (theft or fraud) | `Numeric(Byte)` | `%29.0g` |
| `ilq22` | How old when first been victim of crime | `Numeric(Byte)` | `%8.0g` |
| `ilq23` | Effect on life: been victim of crime | `Numeric(Byte)` | `%29.0g` |
| `ilq24` | Witnessed accident/violent act in which someone was killed/seriously injured | `Numeric(Byte)` | `%29.0g` |
| `ilq25` | How old when first witnessed accident/violent act | `Numeric(Byte)` | `%8.0g` |
| `ilq26` | Effect on life: witnessing accident/violent act | `Numeric(Byte)` | `%29.0g` |
| `ilq27` | Experienced extremely severe economic deprivation | `Numeric(Byte)` | `%29.0g` |
| `ilq28` | How old when first experienced extremely severe economic deprivation | `Numeric(Byte)` | `%8.0g` |
| `ilq29` | Effect on life: experience of extremely severe economic deprivation | `Numeric(Byte)` | `%29.0g` |
| `ilq37` | During wwII, ever resided in country under nazi/pro-nazi regime | `Numeric(Byte)` | `%29.0g` |
| `ilq38` | Year 1939: resided in country that was under nazi/pro-nazi regime | `Numeric(Byte)` | `%14.0g` |
| `ilq39` | Year 1940: resided in country that was under nazi/pro-nazi regime | `Numeric(Byte)` | `%14.0g` |
| `ilq40` | Year 1941: resided in country that was under nazi/pro-nazi regime | `Numeric(Byte)` | `%14.0g` |
| `ilq41` | Year 1942: resided in country that was under nazi/pro-nazi regime | `Numeric(Byte)` | `%14.0g` |
| `ilq42` | Year 1943: resided in country that was under nazi/pro-nazi regime | `Numeric(Byte)` | `%14.0g` |
| `ilq43` | Year 1944: resided in country that was under nazi/pro-nazi regime | `Numeric(Byte)` | `%14.0g` |
| `ilq44` | Year 1945: resided in country that was under nazi/pro-nazi regime | `Numeric(Byte)` | `%14.0g` |
| `ilq45` | In which countries resided under nazi/pro-nazi regime | `Numeric(Byte)` | `%48.0g` |
| `ilq47` | In which countries resided under nazi/pro-nazi regime | `Numeric(Byte)` | `%48.0g` |
| `ilq49` | Conditions in nazi/pro-nazi regime: lived in concentration/death camp | `Numeric(Byte)` | `%29.0g` |
| `ilq50` | Conditions in nazi/pro-nazi regime: lived in work camp | `Numeric(Byte)` | `%29.0g` |
| `ilq51` | Conditions in nazi/pro-nazi regime: lived in a ghetto | `Numeric(Byte)` | `%29.0g` |
| `ilq52` | Conditions in nazi/pro-nazi regime: lived in hiding | `Numeric(Byte)` | `%29.0g` |
| `ilq53` | Conditions in nazi/pro-nazi regime: had false papers | `Numeric(Byte)` | `%29.0g` |
| `ilq54` | Conditions in nazi/pro-nazi regime: joined the underground | `Numeric(Byte)` | `%29.0g` |
| `ilq55` | Conditions in nazi/pro-nazi regime: escaped from authorities | `Numeric(Byte)` | `%29.0g` |
| `ilq56` | Conditions in nazi/pro-nazi regime: fled to area free of nazi-control | `Numeric(Byte)` | `%29.0g` |
| `ilq57` | Conditions in nazi/pro-nazi regime: had a resident permit | `Numeric(Byte)` | `%29.0g` |
| `ilq58` | Did your parents reside in nazi/pro-nazi regime during wwII | `Numeric(Byte)` | `%12.0g` |
| `ilq59` | Were parents killed by nazi/pro-nazi regime/died as result of it | `Numeric(Byte)` | `%12.0g` |
| `ilq60` | Agree with a delay in age of eligibility for receipt of pension benefits | `Numeric(Byte)` | `%17.0g` |
| `ilq61` | Employers will fire older workers and hire younger workers in their place | `Numeric(Byte)` | `%17.0g` |
| `ilq62` | Young people will have fewer places of work available | `Numeric(Byte)` | `%17.0g` |
| `ilq63` | Older workers will lack the stamina to work until the new retirement age | `Numeric(Byte)` | `%17.0g` |
| `ilq64` | Extending work until new retirem. age will improve health of older workers | `Numeric(Byte)` | `%17.0g` |
| `ilq65` | Extending work hours until new retirem. age will increase interest of older work | `Numeric(Byte)` | `%17.0g` |
| `ilq66` | Extending work until new retirem. age will decrease older workers leisure time | `Numeric(Byte)` | `%17.0g` |
| `ilq67` | Women: younger than 64/men: younger than 67 | `Numeric(Byte)` | `%29.0g` |
| `ilq68` | Current employment status | `Numeric(Byte)` | `%33.0g` |
| `ilq69` | Interested in working until the new retirement age | `Numeric(Byte)` | `%29.0g` |
| `ilq70` | Age planning to retire | `Numeric(Byte)` | `%29.0g` |
| `ilq72` | Will retire at different time than planned as result of new retirement age | `Numeric(Byte)` | `%40.0g` |
| `ilq73` | Aware change in retir. age may reduce occupational pension allotments | `Numeric(Byte)` | `%29.0g` |
| `ilq74` | Interested in retiring earlier even if pension will be reduced as result | `Numeric(Byte)` | `%30.0g` |
| `ilq75` | Chances to continue working until the new retirement age | `Numeric(Byte)` | `%29.0g` |
| `ilq76` | Chances your employer will continue to employ you until new retirement age | `Numeric(Byte)` | `%29.0g` |
| `ilq77` | Source of add. support: national insurance allotment (yours/other hh-member) | `Numeric(Byte)` | `%29.0g` |
| `ilq78` | Source of add. support: pension/other payments from abroad | `Numeric(Byte)` | `%29.0g` |
| `ilq79` | Source of add. support: savings | `Numeric(Byte)` | `%29.0g` |
| `ilq80` | Source of add. support: profits from property/investments | `Numeric(Byte)` | `%29.0g` |
| `ilq81` | Source of add. support: income from working members of hh | `Numeric(Byte)` | `%29.0g` |
| `ilq82` | Source of add. support: spouse's occupational pension | `Numeric(Byte)` | `%29.0g` |
| `ilq83` | Source of add. support: loans | `Numeric(Byte)` | `%29.0g` |
| `ilq84` | Source of add. support: other sources | `Numeric(Byte)` | `%29.0g` |
| `ilq87` | Been wounded in war/military action | `Numeric(Byte)` | `%29.0g` |
| `ilq88` | How old when first wounded in war/ilitary action | `Numeric(Byte)` | `%8.0g` |
| `ilq89` | Effect on life: been wounded in war/military action | `Numeric(Byte)` | `%29.0g` |
| `ilq90` | Witnessed serious injury/death of someone in war/military action | `Numeric(Byte)` | `%29.0g` |
| `ilq91` | How old when first witnessed serious injury/death of someone in war/military act | `Numeric(Byte)` | `%8.0g` |
| `ilq92` | Effect on life: witnessing serious injury/death of someone in war/military actio | `Numeric(Byte)` | `%29.0g` |
| `ilq93` | Lost close friend/relative in war/military service | `Numeric(Byte)` | `%29.0g` |
| `ilq94` | How old when first lost close friend/relative in war/military service | `Numeric(Byte)` | `%8.0g` |
| `ilq95` | Effect on life: losing a close friend/relative in war/military service | `Numeric(Byte)` | `%29.0g` |
| `ilq96` | Been wounded in a terrorist act (an attack by terrorists against civilians) | `Numeric(Byte)` | `%29.0g` |
| `ilq97` | How old when first wounded in a terrorist act | `Numeric(Byte)` | `%8.0g` |
| `ilq98` | Effect on life: been wounded in a terrorist act | `Numeric(Byte)` | `%29.0g` |
| `ilq99` | Witnessed a terrorist act in which you yourself were not harmed | `Numeric(Byte)` | `%29.0g` |
| `ilq100` | How old when first witnessed a terrorist act | `Numeric(Byte)` | `%8.0g` |
| `ilq101` | Effect on life: witnessing a terrorist act | `Numeric(Byte)` | `%29.0g` |
| `ilq102` | Experienced the injury/death of a close friend/relative in a terrorist act | `Numeric(Byte)` | `%29.0g` |
| `ilq103` | How old when first experienced injury/death of a close friend/relative in a terr | `Numeric(Byte)` | `%8.0g` |
| `ilq104` | Effect on life: experiencing injury/death of a close friend/relative in a terror | `Numeric(Byte)` | `%29.0g` |
| `ilq105` | Been at risk of death due to illness/serious accident | `Numeric(Byte)` | `%29.0g` |
| `ilq106` | How old when first been at rist of death due to illness/serious accident | `Numeric(Byte)` | `%8.0g` |
| `ilq107` | Effect on life: been at rist of death due to illness/serious accident | `Numeric(Byte)` | `%29.0g` |
| `ilq108` | Had a close friend/relative at risk of death due to illness/serious accident | `Numeric(Byte)` | `%29.0g` |
| `ilq109` | How old when first had a close friend/relative at risk of death due to illness/s | `Numeric(Byte)` | `%8.0g` |
| `ilq110` | Effect on life: had a close friend/relative at risk of death due to illness/seri | `Numeric(Byte)` | `%29.0g` |
| `ilq111` | Experienced the death of a spouse | `Numeric(Byte)` | `%29.0g` |
| `ilq112` | How old when first experienced the death of a spouse | `Numeric(Byte)` | `%8.0g` |
| `ilq113` | Effect on life: experiencing the death of a spouse | `Numeric(Byte)` | `%29.0g` |

### `technical_variables` - Technical variables

- Dataset: `sharew1_rel9-0-0_technical_variables.dta`
- Read with: `ps.read_share_module("technical_variables", wave=1)`
- Rows: 30,416
- Variables: 14
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `fam_resp` | Family respondent | `Numeric(Byte)` | `%21.0g` |
| `fin_resp` | Financial respondent | `Numeric(Byte)` | `%24.0g` |
| `hou_resp` | Household respondent | `Numeric(Byte)` | `%24.0g` |
| `mn005_` | Single or couple interview | `Numeric(Byte)` | `%25.0f` |
| `mn016_` | Mother in household | `Numeric(Byte)` | `%10.0f` |
| `mn017_` | Father in household | `Numeric(Byte)` | `%10.0f` |
| `mn018_` | Mother-in-law in household | `Numeric(Byte)` | `%10.0f` |
| `mn019_` | Father-in-law in household | `Numeric(Byte)` | `%10.0f` |

### `vignettes` - Vignettes

- Dataset: `sharew1_rel9-0-0_vignettes.dta`
- Read with: `ps.read_share_module("vignettes", wave=1)`
- Rows: 4,512
- Variables: 41
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `type` | Vignette type | `Str(1)` | `%9s` |
| `v1` | A1-B6: pain self-rating | `Numeric(Byte)` | `%12.0f` |
| `v2` | A2-B5: sleep self-rating | `Numeric(Byte)` | `%12.0f` |
| `v3` | A3-B4: mobility self-rating | `Numeric(Byte)` | `%12.0f` |
| `v4` | A4-B3: memory self-rating | `Numeric(Byte)` | `%12.0f` |
| `v5` | A5-B2: breath self-rating | `Numeric(Byte)` | `%12.0f` |
| `v6` | A6-B1: depress self-rating | `Numeric(Byte)` | `%12.0f` |
| `v7` | A7-B7: work disability self-rating | `Numeric(Byte)` | `%12.0f` |
| `v8` | A8-B25: pain vignette 1 | `Numeric(Byte)` | `%12.0f` |
| `v9` | A9-B24: sleep vignette 1 | `Numeric(Byte)` | `%12.0f` |
| `v10` | A10-B23: pain vignette 2 | `Numeric(Byte)` | `%12.0f` |
| `v11` | A11-B22: sleep vignette 2 | `Numeric(Byte)` | `%12.0f` |
| `v12` | A12-B21: pain vignette 3 | `Numeric(Byte)` | `%12.0f` |
| `v13` | A13-B20: sleep vignette 3 | `Numeric(Byte)` | `%12.0f` |
| `v14` | A14-B19: mobility vignette 1 | `Numeric(Byte)` | `%12.0f` |
| `v15` | A15-B18: memory vignette 1 | `Numeric(Byte)` | `%12.0f` |
| `v16` | A16-B17: mobility vignette 2 | `Numeric(Byte)` | `%12.0f` |
| `v17` | A17-B16: memory vignette 2 | `Numeric(Byte)` | `%12.0f` |
| `v18` | A18-B15: mobility vignette 3 | `Numeric(Byte)` | `%12.0f` |
| `v19` | A19-B14: memory vignette 3 | `Numeric(Byte)` | `%12.0f` |
| `v20` | A20-B13: breath vignette 1 | `Numeric(Byte)` | `%12.0f` |
| `v21` | A21-B12: depress vignette 1 | `Numeric(Byte)` | `%12.0f` |
| `v22` | A22-B11: breath vignette 2 | `Numeric(Byte)` | `%12.0f` |
| `v23` | A23-B10: depress vignette 2 | `Numeric(Byte)` | `%12.0f` |
| `v24` | A24-B9: breath vignette 3 | `Numeric(Byte)` | `%12.0f` |
| `v25` | A25-B8: depress vignette 3 | `Numeric(Byte)` | `%12.0f` |
| `v26` | A26-B34: work disability vignette 1 | `Numeric(Byte)` | `%12.0f` |
| `v27` | A27-B33: work disability vignette 2 | `Numeric(Byte)` | `%12.0f` |
| `v28` | A28-B32: work disability vignette 3 | `Numeric(Byte)` | `%12.0f` |
| `v29` | A29-B31: work disability vignette 4 | `Numeric(Byte)` | `%12.0f` |
| `v30` | A30-B30: work disability vignette 5 | `Numeric(Byte)` | `%12.0f` |
| `v31` | A31-B29: work disability vignette 6 | `Numeric(Byte)` | `%12.0f` |
| `v32` | A32-B28: work disability vignette 7 | `Numeric(Byte)` | `%12.0f` |
| `v33` | A33-B27: work disability vignette 8 | `Numeric(Byte)` | `%12.0f` |
| `v34` | A34-B26: work disability vignette 9 | `Numeric(Byte)` | `%12.0f` |


## Generated Modules

### `gv_exrates` - Exchange rates and PPP variables

- Dataset: `sharew1_rel9-0-0_gv_exrates.dta`
- Read with: `ps.read_share_module("gv_exrates", wave=1)`
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

### `gv_grossnet` - Net income derived from gross income

- Dataset: `sharew1_rel9-0-0_gv_grossnet.dta`
- Read with: `ps.read_share_module("gv_grossnet", wave=1)`
- Rows: 30,416
- Variables: 20
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `hhsize` | Household size | `Numeric(Byte)` | `%9.0g` |
| `htype` | Household type | `Numeric(Byte)` | `%16.0g` |
| `sic` | Social insurance contributions | `Numeric(Double)` | `%9.0g` |
| `tax` | Personal income tax | `Numeric(Double)` | `%9.0g` |
| `ytotg` | Total individual income, gross | `Numeric(Double)` | `%9.0g` |
| `ytotn` | Total individual income, net | `Numeric(Double)` | `%9.0g` |
| `ynrpg` | NRP income, gross | `Numeric(Double)` | `%9.0g` |
| `ynrpn` | NRP income, net | `Numeric(Double)` | `%9.0g` |
| `hhyotg` | Other household members gross income and household benefits | `Numeric(Double)` | `%9.0g` |
| `hhyotn` | Other household members net income and household benefits | `Numeric(Double)` | `%9.0g` |
| `hhytotg` | Total household income, gross | `Numeric(Double)` | `%9.0g` |
| `hhytotn` | Total household income, net | `Numeric(Double)` | `%9.0g` |
| `hhyotg_f` | Other household members gross income and household benefits - Flag | `Numeric(Byte)` | `%46.0g` |
| `hhyotn_f` | Other household members net income and household benefits - Flag | `Numeric(Byte)` | `%44.0g` |

### `gv_health` - Generated health indicators

- Dataset: `sharew1_rel9-0-0_gv_health.dta`
- Read with: `ps.read_share_module("gv_health", wave=1)`
- Rows: 30,416
- Variables: 47
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `adl` | Number of limitations with activities of daily living (adl) | `Numeric(Byte)` | `%10.0g` |
| `adl2` | 1+ adl limitations | `Numeric(Byte)` | `%18.0g` |
| `bmi` | Body mass index | `Numeric(Float)` | `%28.0g` |
| `bmi2` | Bmi categories | `Numeric(Byte)` | `%27.0g` |
| `casp` | CASP index for quality of life and well-being | `Numeric(Byte)` | `%10.0g` |
| `chronic2w1` | 2+ chronic diseases (w1 version) | `Numeric(Byte)` | `%20.0g` |
| `chronicw1` | Number of chronic diseases (w1 version) | `Numeric(Byte)` | `%10.0g` |
| `cusmoke` | Current smoking | `Numeric(Byte)` | `%40.0g` |
| `drinkin2` | Drinking more than 2 glasses of alcohol almost every or 5/6 days a week | `Numeric(Byte)` | `%52.0g` |
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
| `orienti` | Orientation to date, month,year and day of week | `Numeric(Byte)` | `%10.0g` |
| `phactiv` | Physical inactivity | `Numeric(Byte)` | `%45.0g` |
| `spheu` | Self-perceived health - european version | `Numeric(Byte)` | `%10.0g` |
| `spheu2` | Spheu-less than good health | `Numeric(Byte)` | `%14.0g` |
| `sphus` | Self-perceived health - us version | `Numeric(Byte)` | `%10.0g` |
| `sphus2` | Sphus-less than very good health | `Numeric(Byte)` | `%19.0g` |
| `symptoms2w1` | 2+ symptoms (w1 version) | `Numeric(Byte)` | `%20.0g` |
| `symptomsw1` | Number of symptoms (w1 version) | `Numeric(Byte)` | `%10.0g` |
| `wspeed` | Walking speed | `Numeric(Float)` | `%9.0g` |
| `wspeed2` | Walking speed: cut-off point | `Numeric(Byte)` | `%25.0g` |

### `gv_housing` - Housing generated variables

- Dataset: `sharew1_rel9-0-0_gv_housing.dta`
- Read with: `ps.read_share_module("gv_housing", wave=1)`
- Rows: 30,416
- Variables: 11
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `areabldgi` | Area of building | `Numeric(Byte)` | `%38.0g` |
| `typebldgi` | Type of building | `Numeric(Byte)` | `%57.0g` |
| `floorsbli` | Number of floors of building | `Numeric(Byte)` | `%10.0g` |
| `nstepsi` | Number of steps to entrance | `Numeric(Byte)` | `%12.0g` |
| `nuts1_2003` | NUTS level 1: nomenclature of territorial units for statistics | `Str(27)` | `%27s` |

### `gv_imputations` - Multiple imputations

- Dataset: `sharew1_rel9-0-0_gv_imputations.dta`
- Read with: `ps.read_share_module("gv_imputations", wave=1)`
- Rows: 152,080
- Variables: 224
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `implicat` | Implicat number | `Numeric(Byte)` | `%9.0g` |
| `htype` | Household type | `Numeric(Byte)` | `%16.0g` |
| `fam_resp` | Family respondent | `Numeric(Byte)` | `%14.0g` |
| `fin_resp` | Financial respondent | `Numeric(Byte)` | `%14.0g` |
| `hou_resp` | Household respondent | `Numeric(Byte)` | `%14.0g` |
| `exrate` | Exchange rate | `Numeric(Float)` | `%9.0g` |
| `nursinghome` | Living in nursing home | `Numeric(Byte)` | `%14.0g` |
| `single` | Single | `Numeric(Byte)` | `%14.0g` |
| `couple` | Couple | `Numeric(Byte)` | `%14.0g` |
| `partner` | Partner in the couple | `Numeric(Byte)` | `%14.0g` |
| `p_nrp` | Partner of nonresponding partner | `Numeric(Byte)` | `%14.0g` |
| `sample1` | Imputation sample for single | `Numeric(Byte)` | `%14.0g` |
| `sample2` | Imputation sample for couples 2R | `Numeric(Byte)` | `%14.0g` |
| `sample3` | Imputation sample for all couples | `Numeric(Byte)` | `%14.0g` |
| `inpat` | Paid out-of-pocket for inpatient care | `Numeric(Double)` | `%9.0g` |
| `outpa` | Paid out-of-pocket for outpatient care | `Numeric(Double)` | `%9.0g` |
| `drugs` | Paid out-of-pocket for prescribed drugs | `Numeric(Double)` | `%9.0g` |
| `nurs` | Paid out-of-pocket for nursing home | `Numeric(Double)` | `%9.0g` |
| `hinsu` | Paid for voluntary health insurance | `Numeric(Double)` | `%9.0g` |
| `ydip` | Earnings from employment | `Numeric(Double)` | `%9.0g` |
| `yind` | Earnings from self-employment | `Numeric(Double)` | `%9.0g` |
| `ypen1` | Old age, early retirement, and survisor pensions | `Numeric(Double)` | `%9.0g` |
| `ypen2` | Private and occupational pensions | `Numeric(Double)` | `%9.0g` |
| `ypen3` | Disability pensions and benefits | `Numeric(Double)` | `%9.0g` |
| `ypen4` | Unemployment benefits and insurances | `Numeric(Double)` | `%9.0g` |
| `ypen5` | Social assistance | `Numeric(Double)` | `%9.0g` |
| `ypen6` | Sickness benefits and pensions | `Numeric(Double)` | `%9.0g` |
| `yreg1` | Other private pensions | `Numeric(Double)` | `%9.0g` |
| `yreg2` | Private transfers | `Numeric(Double)` | `%9.0g` |
| `aftgiv` | Financial transfers given | `Numeric(Double)` | `%9.0g` |
| `aftrec` | Financial transfers received | `Numeric(Double)` | `%9.0g` |
| `aftinh` | Inheritance received | `Numeric(Double)` | `%9.0g` |
| `rhre` | Rent and home-related expenditures | `Numeric(Double)` | `%9.0g` |
| `home` | Value of main residence | `Numeric(Double)` | `%9.0g` |
| `mort` | Mortgage on main residence | `Numeric(Double)` | `%9.0g` |
| `ores` | Value of other real estate - Amount | `Numeric(Double)` | `%9.0g` |
| `yrent` | Income from rent | `Numeric(Double)` | `%9.0g` |
| `yaohm` | Income from other household members | `Numeric(Double)` | `%9.0g` |
| `fahc` | Food at home consumption | `Numeric(Double)` | `%9.0g` |
| `fohc` | Food outside home consumption | `Numeric(Double)` | `%9.0g` |
| `telc` | Amount spent on telephones | `Numeric(Double)` | `%9.0g` |
| `bacc` | Bank accounts | `Numeric(Double)` | `%9.0g` |
| `bsmf` | Bond, stock and mutual funds | `Numeric(Double)` | `%9.0g` |
| `ybabsmf` | Interest/dividend from financial assett | `Numeric(Double)` | `%9.0g` |
| `slti` | Savings for long-term investments | `Numeric(Double)` | `%9.0g` |
| `vbus` | Value of own business | `Numeric(Double)` | `%9.0g` |
| `sbus` | Share of own business | `Numeric(Double)` | `%9.0g` |
| `car` | Value of cars | `Numeric(Double)` | `%9.0g` |
| `liab` | Financial liabilities | `Numeric(Double)` | `%9.0g` |
| `thinc` | Total household income | `Numeric(Double)` | `%9.0g` |
| `thexp` | Total household expenditure | `Numeric(Double)` | `%9.0g` |
| `hnetw` | Household net worth | `Numeric(Double)` | `%9.0g` |
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
| `symptoms` | Number of symptoms | `Numeric(Byte)` | `%8.0g` |
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
| `maxgrip` | Maximum of grip strength measures | `Numeric(Byte)` | `%14.0g` |
| `eurod` | EURO depression scale | `Numeric(Byte)` | `%14.0g` |
| `doctor` | Seen/Talked to medical doctor | `Numeric(Byte)` | `%10.0g` |
| `hospital` | In hospital last 12 months | `Numeric(Byte)` | `%14.0g` |
| `thospital` | Times being patient in hospital | `Numeric(Byte)` | `%10.0g` |
| `nhospital` | Total nights stayed in hospital | `Numeric(Int)` | `%14.0g` |
| `cjs` | Current job situation | `Numeric(Byte)` | `%63.0f` |
| `pwork` | Did any paid work | `Numeric(Byte)` | `%14.0f` |
| `afwork` | Away from work during last month | `Numeric(Byte)` | `%14.0f` |
| `empstat1` | Employee or self-employed first job | `Numeric(Byte)` | `%15.0f` |
| `mtoj` | More than one job | `Numeric(Byte)` | `%14.0f` |
| `empstat2` | Employee or self-employed second job | `Numeric(Byte)` | `%15.0f` |
| `rhfo` | Received help from others (how many) | `Numeric(Byte)` | `%14.0g` |
| `ghto` | Given help to others (how many) | `Numeric(Byte)` | `%14.0g` |
| `ghih` | Given help in the household (how many) | `Numeric(Byte)` | `%14.0g` |
| `rhih` | Received help in the household (how many) | `Numeric(Byte)` | `%14.0g` |
| `otrf` | Owner, tenant or rent free | `Numeric(Byte)` | `%43.0f` |
| `fdistress` | Household able to make ends meet | `Numeric(Byte)` | `%21.0g` |
| `nalm` | Number of activities last month | `Numeric(Byte)` | `%14.0g` |
| `tppdi` | Third persons present during the interview | `Numeric(Byte)` | `%14.0g` |
| `willans` | Willingness to answer | `Numeric(Byte)` | `%53.0g` |
| `clarif` | Respondent asked for clarifications | `Numeric(Byte)` | `%14.0g` |
| `undersq` | Respondent understood questions | `Numeric(Byte)` | `%14.0g` |
| `hnrsc` | Help needed to read showcards | `Numeric(Byte)` | `%29.0g` |
| `inpat_f` | Paid out-of-pocket for inpatient care - Flag | `Numeric(Byte)` | `%21.0g` |
| `outpa_f` | Paid out-of-pocket for outpatient care - Flag | `Numeric(Byte)` | `%21.0g` |
| `drugs_f` | Paid out-of-pocket for prescribed drugs - Flag | `Numeric(Byte)` | `%21.0g` |
| `nurs_f` | Paid out-of-pocket for nursing home - Flag | `Numeric(Byte)` | `%21.0g` |
| `hinsu_f` | Paid for voluntary health insurance - Flag | `Numeric(Byte)` | `%21.0g` |
| `ydip_f` | Earnings from employment - Flag | `Numeric(Byte)` | `%21.0g` |
| `yind_f` | Earnings from self-employment - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen1_f` | Old age, early retirement, and survisor pensions - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen2_f` | Private and occupational pensions - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen3_f` | Disability pensions and benefits - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen4_f` | Unemployment benefits and insurances - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen5_f` | Social assistance - Flag | `Numeric(Byte)` | `%21.0g` |
| `ypen6_f` | Sickness benefits and pensions - Flag | `Numeric(Byte)` | `%21.0g` |
| `yreg1_f` | Other private pensions - Flag | `Numeric(Byte)` | `%21.0g` |
| `yreg2_f` | Private transfers - Flag | `Numeric(Byte)` | `%21.0g` |
| `aftgiv_f` | Financial transfers given - Flag | `Numeric(Byte)` | `%21.0g` |
| `aftrec_f` | Financial transfers received - Flag | `Numeric(Byte)` | `%21.0g` |
| `aftinh_f` | Inheritance received - Flag | `Numeric(Byte)` | `%21.0g` |
| `rhre_f` | Rent and home-related expenditures - Flag | `Numeric(Byte)` | `%21.0g` |
| `home_f` | Value of main residence - Flag | `Numeric(Byte)` | `%21.0g` |
| `mort_f` | Mortgage on main residence - Flag | `Numeric(Byte)` | `%21.0g` |
| `ores_f` | Value of other real estate - Flag | `Numeric(Byte)` | `%21.0g` |
| `yrent_f` | Income from rent - Flag | `Numeric(Byte)` | `%21.0g` |
| `yaohm_f` | Income from other household members - Flag | `Numeric(Byte)` | `%21.0g` |
| `fahc_f` | Food at home consumption - Flag | `Numeric(Byte)` | `%21.0g` |
| `fohc_f` | Food outside home consumption - Flag | `Numeric(Byte)` | `%21.0g` |
| `telc_f` | Amount spent on telephones - Flag | `Numeric(Byte)` | `%21.0g` |
| `bacc_f` | Bank accounts - Flag | `Numeric(Byte)` | `%21.0g` |
| `bsmf_f` | Bond, stock and mutual funds - Flag | `Numeric(Byte)` | `%21.0g` |
| `ybabsmf_f` | Interest/dividend from financial assett - Flag | `Numeric(Byte)` | `%21.0g` |
| `slti_f` | Savings for long-term investments - Flag | `Numeric(Byte)` | `%21.0g` |
| `vbus_f` | Value of own business - Flag | `Numeric(Byte)` | `%21.0g` |
| `sbus_f` | Share of own business - Flag | `Numeric(Byte)` | `%21.0g` |
| `car_f` | Value of cars - Flag | `Numeric(Byte)` | `%21.0g` |
| `liab_f` | Financial liabilities - Flag | `Numeric(Byte)` | `%21.0g` |
| `thinc_f` | Total household income - Flag | `Numeric(Byte)` | `%20.0g` |
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
| `maxgrip_f` | Maximum of grip strength measures - Flag | `Numeric(Byte)` | `%20.0g` |
| `eurod_f` | EURO depression scale - Flag | `Numeric(Byte)` | `%20.0g` |
| `doctor_f` | Seen/Talked to medical doctor - Flag | `Numeric(Byte)` | `%20.0g` |
| `hospital_f` | In hospital last 12 months - Flag | `Numeric(Byte)` | `%20.0g` |
| `thospital_f` | Times being patient in hospital - Flag | `Numeric(Byte)` | `%20.0g` |
| `nhospital_f` | Total nights stayed in hospital - Flag | `Numeric(Byte)` | `%20.0g` |
| `cjs_f` | Current job situation - Flag | `Numeric(Byte)` | `%20.0g` |
| `pwork_f` | Did any paid work - Flag | `Numeric(Byte)` | `%20.0g` |
| `afwork_f` | Away from work during last month - Flag | `Numeric(Byte)` | `%20.0g` |
| `empstat1_f` | Employee or self-employed first job - Flag | `Numeric(Byte)` | `%20.0g` |
| `mtoj_f` | More than one job - Flag | `Numeric(Byte)` | `%20.0g` |
| `empstat2_f` | Employee or self-employed second job - Flag | `Numeric(Byte)` | `%20.0g` |
| `rhfo_f` | Received help from others (how many) - Flag | `Numeric(Byte)` | `%20.0g` |
| `ghto_f` | Given help to others (how many) - Flag | `Numeric(Byte)` | `%20.0g` |
| `ghih_f` | Given help in the household (how many) - Flag | `Numeric(Byte)` | `%20.0g` |
| `rhih_f` | Received help in the household (how many) - Flag | `Numeric(Byte)` | `%20.0g` |
| `otrf_f` | Owner, tenant or rent free - Flag | `Numeric(Byte)` | `%20.0g` |
| `fdistress_f` | Household able to make ends meet - Flag | `Numeric(Byte)` | `%20.0g` |
| `nalm_f` | Number of activities last month - Flag | `Numeric(Byte)` | `%20.0g` |
| `tppdi_f` | Third persons present during the interview - Flag | `Numeric(Byte)` | `%20.0g` |
| `willans_f` | Willingness to answer - Flag | `Numeric(Byte)` | `%20.0g` |
| `clarif_f` | Respondent asked for clarifications - Flag | `Numeric(Byte)` | `%20.0g` |
| `undersq_f` | Respondent understood questions - Flag | `Numeric(Byte)` | `%20.0g` |
| `hnrsc_f` | Help needed to read showcards â€“ Flag | `Numeric(Byte)` | `%20.0g` |
| `currency` | currency | `Str(14)` | `%14s` |
| `nomx2003` | Nominal exchange rate (national currency/Euro), annual average, 2003 | `Numeric(Double)` | `%10.0g` |
| `nomx2004` | Nominal exchange rate (national currency/Euro), annual average, 2004 | `Numeric(Double)` | `%10.0g` |
| `nomx2005` | Nominal exchange rate (national currency/Euro), annual average, 2005 | `Numeric(Double)` | `%10.0g` |
| `pppc2003` | Current PPP exchange rate (national currency/Euro), 2003 | `Numeric(Double)` | `%10.0g` |
| `pppc2004` | Current PPP exchange rate (national currency/Euro), 2004 | `Numeric(Double)` | `%10.0g` |
| `pppc2005` | Current PPP exchange rate (national currency/Euro), 2005 | `Numeric(Double)` | `%10.0g` |
| `pppk2003` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2003 | `Numeric(Double)` | `%10.0g` |
| `pppk2004` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2004 | `Numeric(Double)` | `%10.0g` |
| `pppk2005` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2005 | `Numeric(Double)` | `%10.0g` |

### `gv_isced` - ISCED education recodes

- Dataset: `sharew1_rel9-0-0_gv_isced.dta`
- Read with: `ps.read_share_module("gv_isced", wave=1)`
- Rows: 30,416
- Variables: 20
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `isced1997_c1` | Respondent's child 1: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c2` | Respondent's child 2: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c3` | Respondent's child 3: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c4` | Respondent's child 4: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_iv` | Interviewer: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_r` | Respondent: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_sp` | Spouse/ex-spouse of respondent: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997y_c1` | Respondent's sel. child 1: years of education derived from ISCED-97 | `Numeric(Float)` | `%25.0g` |
| `isced1997y_c2` | Respondent's sel. child 2: years of education derived from ISCED-97 | `Numeric(Float)` | `%25.0g` |
| `isced1997y_c3` | Respondent's sel. child 3: years of education derived from ISCED-97 | `Numeric(Float)` | `%25.0g` |
| `isced1997y_c4` | Respondent's sel. child 4: years of education derived from ISCED-97 | `Numeric(Float)` | `%25.0g` |
| `isced1997y_iv` | Interviewer: years of education derived from ISCED-97 | `Numeric(Float)` | `%25.0g` |
| `isced1997y_r` | Respondent: years of education derived from ISCED-97 | `Numeric(Float)` | `%25.0g` |
| `isced1997y_sp` | Spouse/ex-spouse of respondent: years of education derived from ISCED-97 | `Numeric(Float)` | `%25.0g` |

### `gv_isco` - Occupation and industry coding

- Dataset: `sharew1_rel9-0-0_gv_isco.dta`
- Read with: `ps.read_share_module("gv_isco", wave=1)`
- Rows: 30,416
- Variables: 24
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `isco_1job` | Isco-88 respondent's first job (ep016_1) | `Str(4)` | `%4s` |
| `text_1job` | Label for isco_1job (respondent's first job) | `Str(100)` | `%100s` |
| `nace_1job` | Nace industry of respondent's first job (ep018_1 / ep023_1) | `Str(4)` | `%9s` |
| `ind_1job` | Label for nace_1job (industry of respondent's first job) | `Str(163)` | `%163s` |
| `isco_2job` | Isco-88 respondent's second job (ep016_2) | `Str(4)` | `%4s` |
| `text_2job` | Label for isco_2job (respondent's second job) | `Str(80)` | `%80s` |
| `nace_2job` | Nace industry of respondent's second job (ep018_2 / ep023_2) | `Str(4)` | `%9s` |
| `ind_2job` | Label for nace_2job (industry of respondent's second job) | `Str(163)` | `%163s` |
| `isco_ljob` | Isco-88 respondent's last job (ep052) | `Str(4)` | `%4s` |
| `text_ljob` | Label for isco_ljob (respondent's last job) | `Str(100)` | `%100s` |
| `nace_ljob` | Nace industry of respondent's last job (ep054 / ep060) | `Str(4)` | `%9s` |
| `ind_ljob` | Label for nace_ljob (industry of respondent's last job) | `Str(163)` | `%163s` |
| `isco_exp` | Isco-88 former partner's job (dn025) | `Str(4)` | `%4s` |
| `text_exp` | Label for isco_exp (former partner's job) | `Str(80)` | `%80s` |
| `isco_mo` | Isco-88 mother's job (dn029_1) | `Str(4)` | `%4s` |
| `text_mo` | Label for isco_mo (mother's job) | `Str(80)` | `%80s` |
| `isco_fa` | Isco-88 father's job (dn029_2) | `Str(4)` | `%4s` |
| `text_fa` | Label for isco_fa (father's job) | `Str(100)` | `%100s` |

### `gv_weights` - Cross-sectional weights

- Dataset: `sharew1_rel9-0-0_gv_weights.dta`
- Read with: `ps.read_share_module("gv_weights", wave=1)`
- Rows: 30,416
- Variables: 14
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `dw_w1` | Design weight - wave 1 | `Numeric(Double)` | `%10.0g` |
| `cchw_w1` | Calibrated cross-sectional household weight - wave 1 | `Numeric(Double)` | `%10.0g` |
| `cciw_w1` | Calibrated cross-sectional individual weight - wave 1 | `Numeric(Double)` | `%10.0g` |
| `subsample` | Indicator for country-specific subsample | `Str(6)` | `%9s` |
| `stratum1` | Indicator for primary stratum (if any) | `Str(9)` | `%9s` |
| `stratum2` | Indicator for secondary stratum (if any) | `Str(4)` | `%9s` |
| `psu` | Primary sampling unit | `Str(10)` | `%10s` |
| `ssu` | Secondary sampling unit (if any) | `Str(5)` | `%9s` |


## Auxiliary Datasets

### `ep_ilextra` - Israel EP add-on

- Dataset: `sharew1_rel9-0-0_ep_ilextra.dta`
- Read with: `ps.read_share_module("ep_ilextra", wave=1)`
- Rows: 575
- Variables: 25
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid1` | Household identifier (wave 1) | `Str(11)` | `%11s` |
| `mergeidp1` | Partner identifier (wave 1) | `Str(12)` | `%12s` |
| `coupleid1` | Couple identifier (wave 1) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `reint` | Re-interview with respondent | `Numeric(Byte)` | `%15.0g` |
| `ep005_reint_recoded` | Current job situation recoded | `Numeric(Byte)` | `%65.0g` |
| `ep005_reint` | Current job situation | `Numeric(Byte)` | `%65.0g` |
| `ep006_reint` | Ever done paid work | `Numeric(Byte)` | `%10.0g` |
| `ep009_1_reint` | Employee or a self-employed | `Numeric(Byte)` | `%13.0g` |
| `ep019_1_reint` | Firm belongs to the public sector | `Numeric(Byte)` | `%10.0g` |
| `ep020_1_reint` | Number of people employed at firm | `Numeric(Byte)` | `%11.0g` |
| `ep021_1_reint` | Responsibility for supervising other employees | `Numeric(Byte)` | `%10.0g` |
| `ep022_1_reint` | Number of people responsible for | `Numeric(Byte)` | `%11.0g` |
| `ep024_1_reint` | Number of employees | `Numeric(Byte)` | `%11.0g` |
| `ep067_reint` | How became unemployed | `Numeric(Byte)` | `%49.0g` |
| `ep068_reint` | Disability caused by work | `Numeric(Byte)` | `%10.0g` |
| `ep069d1_reint` | Reason stopped working: health problems | `Numeric(Byte)` | `%12.0g` |
| `ep069d2_reint` | Reason stopped working: too tiring | `Numeric(Byte)` | `%12.0g` |
| `ep069d3_reint` | Reason stopped working: too expensive to hire someone to look after home or fami | `Numeric(Byte)` | `%12.0g` |
| `ep069d4_reint` | Reason stopped working: wanted to take care of (grand)children | `Numeric(Byte)` | `%12.0g` |
| `ep069dot_reint` | Reason stopped working: other | `Numeric(Byte)` | `%12.0g` |
| `reint_month` | Month of re-interview | `Numeric(Byte)` | `%10.0g` |
| `reint_year` | Year of re-interview | `Numeric(Int)` | `%9.0g` |
