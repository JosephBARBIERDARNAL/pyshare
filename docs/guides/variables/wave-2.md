---
icon: lucide/list-tree
---

# Wave 2 Variable Dictionary

This page is generated from the local SHARE wave 2 release `9-0-0` Stata files.

It covers 32 datasets and 2,746 variable entries for the files currently available in `data/`.

[Back to variable dictionary](./index.md)

## Overview

| Module | Category | Meaning | Key | Variables | Rows | File |
| --- | --- | --- | --- | --- | --- | --- |
| `ac` | core | Activities | `mergeid` | 91 | 37,132 | `sharew2_rel9-0-0_ac.dta` |
| `as` | core | Assets | `mergeid` | 131 | 37,132 | `sharew2_rel9-0-0_as.dta` |
| `br` | core | Behavioural Risks | `mergeid` | 23 | 37,132 | `sharew2_rel9-0-0_br.dta` |
| `cf` | core | Cognitive Function | `mergeid` | 24 | 37,132 | `sharew2_rel9-0-0_cf.dta` |
| `ch` | core | Children | `mergeid` | 223 | 37,132 | `sharew2_rel9-0-0_ch.dta` |
| `co` | core | Consumption | `mergeid` | 15 | 37,132 | `sharew2_rel9-0-0_co.dta` |
| `cs` | core | Chair Stand | `mergeid` | 25 | 37,132 | `sharew2_rel9-0-0_cs.dta` |
| `cv_r` | core | Coverscreen on individual level | `mergeid` | 30 | 55,262 | `sharew2_rel9-0-0_cv_r.dta` |
| `dn` | core | Demographics | `mergeid` | 79 | 37,132 | `sharew2_rel9-0-0_dn.dta` |
| `ep` | core | Employment and Pensions | `mergeid` | 609 | 37,132 | `sharew2_rel9-0-0_ep.dta` |
| `ex` | core | Expectations | `mergeid` | 27 | 37,132 | `sharew2_rel9-0-0_ex.dta` |
| `ft` | core | Financial Transfers | `mergeid` | 75 | 37,132 | `sharew2_rel9-0-0_ft.dta` |
| `gs` | core | Grip Strength | `mergeid` | 23 | 37,132 | `sharew2_rel9-0-0_gs.dta` |
| `hc` | core | Health Care | `mergeid` | 116 | 37,132 | `sharew2_rel9-0-0_hc.dta` |
| `hh` | core | Household Income | `mergeid` | 21 | 37,132 | `sharew2_rel9-0-0_hh.dta` |
| `ho` | core | Housing | `mergeid` | 79 | 37,132 | `sharew2_rel9-0-0_ho.dta` |
| `iv` | core | Interviewer Observations | `mergeid` | 27 | 37,132 | `sharew2_rel9-0-0_iv.dta` |
| `mh` | core | Mental Health | `mergeid` | 27 | 37,132 | `sharew2_rel9-0-0_mh.dta` |
| `pf` | core | Peak Flow | `mergeid` | 17 | 37,132 | `sharew2_rel9-0-0_pf.dta` |
| `ph` | core | Physical Health | `mergeid` | 168 | 37,132 | `sharew2_rel9-0-0_ph.dta` |
| `sp` | core | Social Support | `mergeid` | 168 | 37,132 | `sharew2_rel9-0-0_sp.dta` |
| `ws` | core | Walking Speed | `mergeid` | 19 | 37,132 | `sharew2_rel9-0-0_ws.dta` |
| `xt` | core | End-of-Life Interview | `mergeid` | 108 | 726 | `sharew2_rel9-0-0_xt.dta` |
| `dropoff` | special | Paper-and-pencil drop-off | `mergeid` | 154 | 8,862 | `sharew2_rel9-0-0_dropoff.dta` |
| `technical_variables` | special | Technical variables | `mergeid` | 16 | 37,132 | `sharew2_rel9-0-0_technical_variables.dta` |
| `vignettes` | special | Vignettes | `mergeid` | 49 | 7,646 | `sharew2_rel9-0-0_vignettes.dta` |
| `gv_exrates` | generated | Exchange rates and PPP variables | `country` | 76 | 29 | `sharew2_rel9-0-0_gv_exrates.dta` |
| `gv_health` | generated | Generated health indicators | `mergeid` | 44 | 37,132 | `sharew2_rel9-0-0_gv_health.dta` |
| `gv_housing` | generated | Housing generated variables | `mergeid` | 11 | 37,132 | `sharew2_rel9-0-0_gv_housing.dta` |
| `gv_imputations` | generated | Multiple imputations | `mergeid` | 245 | 185,660 | `sharew2_rel9-0-0_gv_imputations.dta` |
| `gv_isced` | generated | ISCED education recodes | `mergeid` | 12 | 37,132 | `sharew2_rel9-0-0_gv_isced.dta` |
| `gv_weights` | generated | Cross-sectional weights | `mergeid` | 14 | 37,132 | `sharew2_rel9-0-0_gv_weights.dta` |

## Core Interview Modules

### `ac` - Activities

- Dataset: `sharew2_rel9-0-0_ac.dta`
- Read with: `ps.read_share_module("ac", wave=2)`
- Rows: 37,132
- Variables: 91
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
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
| `ac003_1` | How often in last 4 weeks: voluntary/charity work | `Numeric(Byte)` | `%17.0g` |
| `ac003_2` | How often in last 4 weeks: cared for sick/disabled adult | `Numeric(Byte)` | `%17.0g` |
| `ac003_3` | How often in last 4 weeks: provided help to family/friends/neighbors | `Numeric(Byte)` | `%17.0g` |
| `ac003_4` | How often in last 4 weeks: attended educational/training course | `Numeric(Byte)` | `%17.0g` |
| `ac003_5` | How often in last 4 weeks: sport/social/other club | `Numeric(Byte)` | `%17.0g` |
| `ac003_6` | How often in last 4 weeks: taken part religious organization | `Numeric(Byte)` | `%17.0g` |
| `ac003_7` | How often in last 4 weeks: taken part political/community-rel. org. | `Numeric(Byte)` | `%17.0g` |
| `ac004d1_1` | Voluntary or charity work: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `ac004d1_2` | Cared for sick or disabled adult: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `ac004d1_3` | Help to family, friends or neighbors: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `ac004d1_4` | Educational or training course: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `ac004d1_5` | Sport, social or other club: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `ac004d1_6` | Religious organization: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `ac004d1_7` | Political or community organization: to meet other people | `Numeric(Byte)` | `%12.0g` |
| `ac004d2_1` | Voluntary or charity work: to contribute something useful | `Numeric(Byte)` | `%12.0g` |
| `ac004d2_2` | Cared for sick or disabled adult: to contribute something useful | `Numeric(Byte)` | `%12.0g` |
| `ac004d2_3` | Help to family, friends or neighbors: to contribute something useful | `Numeric(Byte)` | `%12.0g` |
| `ac004d2_4` | Educational or training course: to contribute something useful | `Numeric(Byte)` | `%12.0g` |
| `ac004d2_5` | Sport, social or other club: to contribute something useful | `Numeric(Byte)` | `%12.0g` |
| `ac004d2_6` | Religious organization: to contribute something useful | `Numeric(Byte)` | `%12.0g` |
| `ac004d2_7` | Political or community organization: to contribute something useful | `Numeric(Byte)` | `%12.0g` |
| `ac004d4_1` | Voluntary or charity work: because I am needed | `Numeric(Byte)` | `%12.0g` |
| `ac004d4_2` | Cared for sick or disabled adult: because I am needed | `Numeric(Byte)` | `%12.0g` |
| `ac004d4_3` | Help to family, friends or neighbors: because I am needed | `Numeric(Byte)` | `%12.0g` |
| `ac004d4_4` | Educational or training course: because I am needed | `Numeric(Byte)` | `%12.0g` |
| `ac004d4_5` | Sport, social or other club: because I am needed | `Numeric(Byte)` | `%12.0g` |
| `ac004d4_6` | Religious organization: because I am needed | `Numeric(Byte)` | `%12.0g` |
| `ac004d4_7` | Political or community organization: because I am needed | `Numeric(Byte)` | `%12.0g` |
| `ac004d5_1` | Voluntary or charity work: to earn money | `Numeric(Byte)` | `%12.0g` |
| `ac004d5_2` | Cared for sick or disabled adult: to earn money | `Numeric(Byte)` | `%12.0g` |
| `ac004d5_3` | Help to family, friends or neighbors: to earn money | `Numeric(Byte)` | `%12.0g` |
| `ac004d5_4` | Educational or training course: to earn money | `Numeric(Byte)` | `%12.0g` |
| `ac004d5_5` | Sport, social or other club: to earn money | `Numeric(Byte)` | `%12.0g` |
| `ac004d5_6` | Religious organization: to earn money | `Numeric(Byte)` | `%12.0g` |
| `ac004d5_7` | Political or community organization: to earn money | `Numeric(Byte)` | `%12.0g` |
| `ac004d7_1` | Voluntary or charity work: to use skills or to keep fit | `Numeric(Byte)` | `%12.0g` |
| `ac004d7_2` | Cared for sick or disabled adult: to use skills or to keep fit | `Numeric(Byte)` | `%12.0g` |
| `ac004d7_3` | Help to family, friends or neighbors: to use skills or to keep fit | `Numeric(Byte)` | `%12.0g` |
| `ac004d7_4` | Educational or training course: to use skills or to keep fit | `Numeric(Byte)` | `%12.0g` |
| `ac004d7_5` | Sport, social or other club: to use skills or to keep fit | `Numeric(Byte)` | `%12.0g` |
| `ac004d7_6` | Religious organization: to use skills or to keep fit | `Numeric(Byte)` | `%12.0g` |
| `ac004d7_7` | Political or community organization: to use skills or to keep fit | `Numeric(Byte)` | `%12.0g` |
| `ac004dno_1` | Voluntary or charity work: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac004dno_2` | Cared for sick or disabled adult: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac004dno_3` | Help to family, friends or neighbors: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac004dno_4` | Educational or training course: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac004dno_5` | Sport, social or other club: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac004dno_6` | Religious organization: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac004dno_7` | Political or community organization: none of these | `Numeric(Byte)` | `%12.0g` |
| `ac006_1` | Fully satisfied with what achieved so far | `Numeric(Byte)` | `%26.0g` |
| `ac006_2` | Fully satisfied with what achieved so far | `Numeric(Byte)` | `%26.0g` |
| `ac006_3` | Fully satisfied with what achieved so far | `Numeric(Byte)` | `%26.0g` |
| `ac007_1` | Received adequate appreciation from others | `Numeric(Byte)` | `%26.0g` |
| `ac007_2` | Received adequate appreciation from others | `Numeric(Byte)` | `%26.0g` |
| `ac007_3` | Received adequate appreciation from others | `Numeric(Byte)` | `%26.0g` |
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
| `ac199_` | Feelings: random number | `Numeric(Byte)` | `%8.0g` |
| `ac027_` | Feelings: depressed | `Numeric(Byte)` | `%10.0g` |
| `ac028_` | Feelings: everything effort | `Numeric(Byte)` | `%10.0g` |
| `ac029_` | Feelings: sleep was restless | `Numeric(Byte)` | `%10.0g` |
| `ac030_` | Feelings: happy | `Numeric(Byte)` | `%10.0g` |
| `ac031_` | Feelings: lonely | `Numeric(Byte)` | `%10.0g` |
| `ac032_` | Feelings: enjoyed life | `Numeric(Byte)` | `%10.0g` |
| `ac033_` | Feelings: felt sad | `Numeric(Byte)` | `%10.0g` |
| `ac034_` | Feelings: could not get going | `Numeric(Byte)` | `%10.0g` |

### `as` - Assets

- Dataset: `sharew2_rel9-0-0_as.dta`
- Read with: `ps.read_share_module("as", wave=2)`
- Rows: 37,132
- Variables: 131
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `as003e` | Amount bank account | `Numeric(Double)` | `%10.0g` |
| `as003ub` | Amount bank account ub | `Numeric(Byte)` | `%32.0g` |
| `as003v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as003v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as003v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as005e` | Interest from bank account | `Numeric(Double)` | `%10.0g` |
| `as005ub` | Interest from bank account ub | `Numeric(Byte)` | `%32.0g` |
| `as005v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `as005v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `as005v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `as007e` | Amount in bonds | `Numeric(Double)` | `%10.0g` |
| `as007ub` | Amount in bonds ub | `Numeric(Byte)` | `%32.0g` |
| `as007v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as007v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as007v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as009e` | Interest from bonds | `Numeric(Double)` | `%10.0g` |
| `as009ub` | Interest from bonds ub | `Numeric(Byte)` | `%32.0g` |
| `as009v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `as009v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `as009v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `as011e` | Amount in stocks | `Numeric(Double)` | `%10.0g` |
| `as011ub` | Amount in stocks ub | `Numeric(Byte)` | `%32.0g` |
| `as011v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as011v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as011v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `as015e` | Dividend from stocks | `Numeric(Double)` | `%10.0g` |
| `as015ub` | Dividend from stocks ub | `Numeric(Byte)` | `%32.0g` |
| `as015v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `as015v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `as015v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `as017e` | Amount in mutual funds | `Numeric(Double)` | `%10.0g` |
| `as017ub` | Amount in mutual funds ub | `Numeric(Byte)` | `%32.0g` |
| `as017v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as017v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as017v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as019_` | Mutual funds mostly stocks or bonds | `Numeric(Byte)` | `%26.0g` |
| `as020_` | Who has individual retirement accounts | `Numeric(Byte)` | `%25.0g` |
| `as021e` | Amount individual retirement accounts | `Numeric(Double)` | `%10.0g` |
| `as021ub` | Amount individual retirement accounts ub | `Numeric(Byte)` | `%32.0g` |
| `as021v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as021v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as021v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as023_` | Individual retirement accounts mostly in stocks or bonds | `Numeric(Byte)` | `%29.0g` |
| `as024e` | Partner amount individual retirement accounts | `Numeric(Double)` | `%10.0g` |
| `as024ub` | Partner amount individual retirement accounts ub | `Numeric(Byte)` | `%32.0g` |
| `as024v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `as024v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as024v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as026_` | Partner individual retirement accounts mostly in stocks or bonds | `Numeric(Byte)` | `%32.0g` |
| `as027e` | Amount contractual saving for housing | `Numeric(Double)` | `%10.0g` |
| `as027ub` | Amount contractual saving for housing ub | `Numeric(Byte)` | `%32.0g` |
| `as027v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as027v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as027v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as029_` | Life insurance policies term or whole life | `Numeric(Byte)` | `%19.0g` |
| `as030e` | Face value of whole life policies | `Numeric(Double)` | `%10.0g` |
| `as030ub` | Face value of whole life policies ub | `Numeric(Byte)` | `%32.0g` |
| `as030v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as030v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as030v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `as032e_1` | Amount dependents get from life insurace policies | `Numeric(Double)` | `%10.0g` |
| `as032ub_1` | Amount dependents get from life insurace policies ub | `Numeric(Byte)` | `%32.0g` |
| `as032e_2` | Amount dependents get from term policies | `Numeric(Double)` | `%10.0g` |
| `as032ub_2` | Amount dependents get from term policies ub | `Numeric(Byte)` | `%32.0g` |
| `as032v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as032v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as032v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `as034e_1` | Paid on life insurance policies | `Numeric(Double)` | `%10.0g` |
| `as034ub_1` | Paid on life insurance policies ub | `Numeric(Byte)` | `%32.0g` |
| `as034e_2` | Paid on term policies | `Numeric(Double)` | `%10.0g` |
| `as034ub_2` | Paid on term policies ub | `Numeric(Byte)` | `%32.0g` |
| `as034v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `as034v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `as034v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `as041_` | Own firm company business | `Numeric(Byte)` | `%10.0g` |
| `as042e` | Amount selling firm | `Numeric(Double)` | `%10.0g` |
| `as042ub` | Amount selling firm ub | `Numeric(Byte)` | `%32.0g` |
| `as042v1` | Bracket value 1 | `Numeric(Double)` | `%12.0g` |
| `as042v2` | Bracket value 2 | `Numeric(Double)` | `%12.0g` |
| `as042v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `as044_` | Percentage share firm owned | `Numeric(Double)` | `%10.0g` |
| `as044ub` | Percentage share firm owned ub | `Numeric(Byte)` | `%32.0g` |
| `as044v1` | Bracket value 1 | `Numeric(Byte)` | `%8.0g` |
| `as044v2` | Bracket value 2 | `Numeric(Byte)` | `%8.0g` |
| `as044v3` | Bracket value 3 | `Numeric(Byte)` | `%8.0g` |
| `as049_` | Number of cars | `Numeric(Byte)` | `%10.0g` |
| `as051e` | Amount selling cars | `Numeric(Double)` | `%10.0g` |
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
| `as055e` | Amount owing money in total | `Numeric(Double)` | `%10.0g` |
| `as055ub` | Amount owing money in total ub | `Numeric(Byte)` | `%32.0g` |
| `as055v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as055v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as055v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `as057_` | Who answered the question in as | `Numeric(Byte)` | `%20.0g` |
| `as058e` | Interest or dividend on mutual funds | `Numeric(Double)` | `%10.0g` |
| `as058ub` | Interest or dividend on mutual funds ub | `Numeric(Byte)` | `%32.0g` |
| `as058v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `as058v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `as058v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `as060_` | Has bank account | `Numeric(Byte)` | `%10.0g` |
| `as061_` | Reason for not having a bank account | `Numeric(Byte)` | `%80.0g` |
| `as062_` | Has bonds | `Numeric(Byte)` | `%10.0g` |
| `as063_` | Has stocks | `Numeric(Byte)` | `%10.0g` |
| `as064_` | Has mutual funds | `Numeric(Byte)` | `%10.0g` |
| `as065_` | Has individual retirement accounts | `Numeric(Byte)` | `%10.0g` |
| `as066_` | Has contractual saving | `Numeric(Byte)` | `%10.0g` |
| `as067_` | Has life insurance | `Numeric(Byte)` | `%10.0g` |
| `as068_` | Risk aversion | `Numeric(Byte)` | `%74.0g` |
| `as069e` | Savings/investments og other adults in household | `Numeric(Double)` | `%10.0g` |
| `as069ub` | Savings/investments og other adults in household ub | `Numeric(Byte)` | `%32.0g` |
| `as069v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `as069v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `as069v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |

### `br` - Behavioural Risks

- Dataset: `sharew2_rel9-0-0_br.dta`
- Read with: `ps.read_share_module("br", wave=2)`
- Rows: 37,132
- Variables: 23
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `br001_` | Ever smoked daily | `Numeric(Byte)` | `%10.0g` |
| `br002_` | Smoke at the present time | `Numeric(Byte)` | `%10.0g` |
| `br003_` | How many years smoked | `Numeric(Byte)` | `%10.0g` |
| `br005d1` | Do or did smoke: cigarettes | `Numeric(Byte)` | `%12.0g` |
| `br005d2` | Do or did smoke: pipe | `Numeric(Byte)` | `%12.0g` |
| `br005d3` | Do or did smoke: cigars or cigarillos | `Numeric(Byte)` | `%12.0g` |
| `br006_` | Average amount of cigarettes per day | `Numeric(Int)` | `%10.0g` |
| `br007_` | Average amount of pipes per day | `Numeric(Byte)` | `%10.0g` |
| `br008_` | Average amount of cigars per day | `Numeric(Byte)` | `%10.0g` |
| `br010_` | Days a week consumed alcohol last 3 months | `Numeric(Byte)` | `%42.0g` |
| `br015_` | Sports or activities that are vigorous | `Numeric(Byte)` | `%26.0g` |
| `br016_` | Activities requiring a moderate level of energy | `Numeric(Byte)` | `%26.0g` |
| `br017_` | Who answered the questions in br | `Numeric(Byte)` | `%20.0g` |
| `br019_` | How many drinks in a day | `Numeric(Byte)` | `%10.0g` |
| `br020_` | How often four or more drinks last 3 months | `Numeric(Byte)` | `%10.0g` |
| `br021_` | Ever drunk alcoholic beverages | `Numeric(Byte)` | `%10.0g` |
| `br022_` | Stopped smoking | `Numeric(Byte)` | `%61.0g` |

### `cf` - Cognitive Function

- Dataset: `sharew2_rel9-0-0_cf.dta`
- Read with: `ps.read_share_module("cf", wave=2)`
- Rows: 37,132
- Variables: 24
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `cf001_` | Self-rated reading skills | `Numeric(Byte)` | `%13.0g` |
| `cf002_` | Self-rated writing skills | `Numeric(Byte)` | `%13.0g` |
| `cf003_` | Date: day of month | `Numeric(Byte)` | `%47.0g` |
| `cf004_` | Date: month | `Numeric(Byte)` | `%47.0g` |
| `cf005_` | Date: year | `Numeric(Byte)` | `%45.0g` |
| `cf006_` | Date: day of the week | `Numeric(Byte)` | `%55.0g` |
| `cf008tot` | Ten words list learning first trial total | `Numeric(Byte)` | `%9.0g` |
| `cf010_` | Verbal fluency score: number of animals | `Numeric(Byte)` | `%10.0g` |
| `cf012_` | Numeracy: chance disease 10% of 1000 | `Numeric(Byte)` | `%19.0g` |
| `cf013_` | Numeracy: half price | `Numeric(Byte)` | `%19.0g` |
| `cf014_` | Numeracy: 6000 is two-thirds what is total price | `Numeric(Byte)` | `%21.0g` |
| `cf015_` | Numeracy: amount in the savings account | `Numeric(Byte)` | `%20.0g` |
| `cf016tot` | Ten words list learning delayed recall total | `Numeric(Byte)` | `%9.0g` |
| `cf017_` | Contextual factors during the cognitive function test | `Numeric(Byte)` | `%10.0g` |
| `cf018d1` | Who present during cf: respondent alone | `Numeric(Byte)` | `%12.0g` |
| `cf018d2` | Who present during cf: partner present | `Numeric(Byte)` | `%12.0g` |
| `cf018d3` | Who present during cf: child(ren) present | `Numeric(Byte)` | `%12.0g` |
| `cf018d4` | Who present during cf: other(s) | `Numeric(Byte)` | `%12.0g` |

### `ch` - Children

- Dataset: `sharew2_rel9-0-0_ch.dta`
- Read with: `ps.read_share_module("ch", wave=2)`
- Rows: 37,132
- Variables: 223
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
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
| `ch001_` | Number of children | `Numeric(Byte)` | `%10.0g` |
| `ch002_` | Natural child(ren) | `Numeric(Byte)` | `%10.0g` |
| `ch005_1` | Child 1 gender | `Numeric(Long)` | `%10.0g` |
| `ch005_2` | Child 2 gender | `Numeric(Long)` | `%10.0g` |
| `ch005_3` | Child 3 gender | `Numeric(Long)` | `%10.0g` |
| `ch005_4` | Child 4 gender | `Numeric(Long)` | `%10.0g` |
| `ch005_5` | Child 5 gender | `Numeric(Long)` | `%10.0g` |
| `ch005_6` | Child 6 gender | `Numeric(Byte)` | `%10.0g` |
| `ch005_7` | Child 7 gender | `Numeric(Long)` | `%10.0g` |
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
| `ch006_1` | Child 1 year of birth | `Numeric(Int)` | `%12.0g` |
| `ch006_2` | Child 2 year of birth | `Numeric(Int)` | `%12.0g` |
| `ch006_3` | Child 3 year of birth | `Numeric(Int)` | `%12.0g` |
| `ch006_4` | Child 4 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_5` | Child 5 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_6` | Child 6 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_7` | Child 7 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_8` | Child 8 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_9` | Child 9 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_10` | Child 10 year of birth | `Numeric(Int)` | `%12.0g` |
| `ch006_11` | Child 11 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_12` | Child 12 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_13` | Child 13 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_14` | Child 14 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_15` | Child 15 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_16` | Child 16 year of birth | `Numeric(Int)` | `%10.0g` |
| `ch006_17` | Child 17 year of birth | `Numeric(Byte)` | `%10.0g` |
| `ch006_18` | Child 18 year of birth | `Numeric(Byte)` | `%10.0g` |
| `ch006_19` | Child 19 year of birth | `Numeric(Byte)` | `%10.0g` |
| `ch006_20` | Child 20 year of birth | `Numeric(Byte)` | `%10.0g` |
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
| `ch008c_14` | Child 14 which country - coded | `Numeric(Int)` | `%46.0g` |
| `ch008c_15` | Child 15 which country - coded | `Numeric(Byte)` | `%46.0g` |
| `ch008c_16` | Child 16 which country - coded | `Numeric(Byte)` | `%46.0g` |
| `ch008c_17` | Child 17 which country - coded | `Numeric(Byte)` | `%46.0g` |
| `ch008c_18` | Child 18 which country - coded | `Numeric(Byte)` | `%46.0g` |
| `ch008c_19` | Child 19 which country - coded | `Numeric(Byte)` | `%46.0g` |
| `ch008c_20` | Child 20 which country - coded | `Numeric(Byte)` | `%46.0g` |
| `chselch1` | Child number 1 selected child | `Numeric(Byte)` | `%10.0g` |
| `chselch2` | Child number 2 selected child | `Numeric(Byte)` | `%10.0g` |
| `chselch3` | Child number 3 selected child | `Numeric(Byte)` | `%10.0g` |
| `chselch4` | Child number 4 selected child | `Numeric(Byte)` | `%10.0g` |
| `ch010_1` | Child 1 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_2` | Child 2 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_3` | Child 3 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch010_4` | Child 4 step adoptive or foster child | `Numeric(Byte)` | `%19.0g` |
| `ch011_1` | Child 1 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_2` | Child 2 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_3` | Child 3 own child | `Numeric(Byte)` | `%61.0g` |
| `ch011_4` | Child 4 own child | `Numeric(Byte)` | `%61.0g` |
| `ch012_1` | Child 1 marital status | `Numeric(Byte)` | `%39.0g` |
| `ch012_2` | Child 2 marital status | `Numeric(Byte)` | `%39.0g` |
| `ch012_3` | Child 3 marital status | `Numeric(Byte)` | `%39.0g` |
| `ch012_4` | Child 4 marital status | `Numeric(Byte)` | `%39.0g` |
| `ch013_1` | Child 1 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_2` | Child 2 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_3` | Child 3 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch013_4` | Child 4 has partner | `Numeric(Byte)` | `%10.0g` |
| `ch014_1` | Child 1 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_2` | Child 2 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_3` | Child 3 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch014_4` | Child 4 contact with child | `Numeric(Byte)` | `%27.0g` |
| `ch015_1` | Child 1 year moved out | `Numeric(Int)` | `%12.0g` |
| `ch015_2` | Child 2 year moved out | `Numeric(Int)` | `%12.0g` |
| `ch015_3` | Child 3 year moved out | `Numeric(Int)` | `%12.0g` |
| `ch015_4` | Child 4 year moved out | `Numeric(Int)` | `%12.0g` |
| `ch016_1` | Child 1 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_2` | Child 2 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_3` | Child 3 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch016_4` | Child 4 employment status | `Numeric(Byte)` | `%58.0g` |
| `ch017_1` | Child 1 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_2` | Child 2 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_3` | Child 3 highest school degree | `Numeric(Byte)` | `%47.0g` |
| `ch017_4` | Child 4 highest school degree | `Numeric(Byte)` | `%47.0g` |
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
| `ch019_1` | Child 1 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_2` | Child 2 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_3` | Child 3 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch019_4` | Child 4 number of children | `Numeric(Byte)` | `%10.0g` |
| `ch020_1` | Child 1 year of birth youngest child | `Numeric(Int)` | `%12.0g` |
| `ch020_2` | Child 2 year of birth youngest child | `Numeric(Int)` | `%12.0g` |
| `ch020_3` | Child 3 year of birth youngest child | `Numeric(Int)` | `%12.0g` |
| `ch020_4` | Child 4 year of birth youngest child | `Numeric(Int)` | `%12.0g` |
| `ch021_` | Number of grandchildren | `Numeric(Byte)` | `%10.0g` |
| `ch022_` | Has great-grandchildren | `Numeric(Byte)` | `%10.0g` |
| `ch023_` | Who answered questions in section CH | `Numeric(Byte)` | `%20.0g` |

### `co` - Consumption

- Dataset: `sharew2_rel9-0-0_co.dta`
- Read with: `ps.read_share_module("co", wave=2)`
- Rows: 37,132
- Variables: 15
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `co002e` | Amount spent on food at home | `Numeric(Double)` | `%10.0g` |
| `co003e` | Amount spent on food outside the home | `Numeric(Double)` | `%10.0g` |
| `co004e` | Amount spent on telephones in last month | `Numeric(Double)` | `%10.0g` |
| `co007_` | Is household able to make ends meet | `Numeric(Byte)` | `%28.0g` |
| `co008_` | Situation improvement thinking back one year | `Numeric(Byte)` | `%21.0g` |
| `co009_` | Who answered the questions in co | `Numeric(Byte)` | `%20.0g` |
| `co010_` | Consume home produced food | `Numeric(Byte)` | `%10.0g` |
| `co011e` | Value of home produced food | `Numeric(Double)` | `%10.0g` |

### `cs` - Chair Stand

- Dataset: `sharew2_rel9-0-0_cs.dta`
- Read with: `ps.read_share_module("cs", wave=2)`
- Rows: 37,132
- Variables: 25
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `cs002_` | Safe to do cs | `Numeric(Byte)` | `%10.0g` |
| `cs004_` | Single cs test results | `Numeric(Byte)` | `%38.0g` |
| `cs005d1` | Why not completed sing cs t: tried but unable | `Numeric(Byte)` | `%12.0g` |
| `cs005d2` | Why not completed sing cs t: r could not stand unassisted | `Numeric(Byte)` | `%12.0g` |
| `cs005d3` | Why not completed sing cs t: r felt it would not be safe | `Numeric(Byte)` | `%12.0g` |
| `cs005d4` | Why not completed sing cs t: iwer felt it would not be safe | `Numeric(Byte)` | `%12.0g` |
| `cs005d5` | Why not completed sing cs t: r refused or was not willing to complete the test | `Numeric(Byte)` | `%12.0g` |
| `cs005d6` | Why not completed sing cs t: r did not understand the instructions | `Numeric(Byte)` | `%12.0g` |
| `cs005dot` | Why not completed sing cs t: other | `Numeric(Byte)` | `%12.0g` |
| `cs007_` | Safe to do five times cs | `Numeric(Byte)` | `%10.0g` |
| `cs008_` | Time in seconds used for five stands | `Numeric(Double)` | `%23.0g` |
| `cs009d1` | Why not completed five cs t: tried but unable | `Numeric(Byte)` | `%12.0g` |
| `cs009d2` | Why not completed five cs t: r could not stand unassisted | `Numeric(Byte)` | `%12.0g` |
| `cs009d3` | Why not completed five cs t: r felt it would not be safe | `Numeric(Byte)` | `%12.0g` |
| `cs009d4` | Why not completed five cs t: iwer felt it would not be safe | `Numeric(Byte)` | `%12.0g` |
| `cs009d5` | Why not completed five cs t: r refused or was not willing to complete the test | `Numeric(Byte)` | `%12.0g` |
| `cs009d6` | Why not completed five cs t: r did not understand the instructions | `Numeric(Byte)` | `%12.0g` |
| `cs009dot` | Why not completed five cs t: other | `Numeric(Byte)` | `%12.0g` |
| `cs011_` | Effort that r gave to cs | `Numeric(Byte)` | `%60.0g` |

### `cv_r` - Coverscreen on individual level

- Dataset: `sharew2_rel9-0-0_cv_r.dta`
- Read with: `ps.read_share_module("cv_r", wave=2)`
- Rows: 55,262
- Variables: 30
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `waveid` | Identifier of original wave (person) | `Numeric(Byte)` | `%9.0g` |
| `waveid_hh` | Identifier of original wave (household) | `Numeric(Byte)` | `%9.0g` |
| `firstwave` | First appearance of person in SHARE | `Numeric(Byte)` | `%9.0g` |
| `firstwave_hh` | Wave household was sampled/first participated | `Numeric(Byte)` | `%9.0g` |
| `cvresp` | Coverscreen respondent | `Numeric(Byte)` | `%10.0g` |
| `deceased` | Deceased | `Numeric(Byte)` | `%10.0g` |
| `gender` | Male or female | `Numeric(Byte)` | `%10.0g` |
| `mobirth` | Month of birth | `Numeric(Byte)` | `%10.0g` |
| `yrbirth` | Year of birth | `Numeric(Int)` | `%10.0g` |
| `age2007` | Age in 2007 | `Numeric(Int)` | `%14.0g` |
| `age_int` | Age of respondent at the time of interview | `Numeric(Int)` | `%14.0g` |
| `mobirthp` | Month of birth spouse/partner | `Numeric(Byte)` | `%14.0g` |
| `yrbirthp` | Year of birth spouse/partner | `Numeric(Int)` | `%14.0g` |
| `agep2007` | Age of partner in 2007 | `Numeric(Byte)` | `%14.0g` |
| `partnerinhh` | Partner in household | `Numeric(Byte)` | `%14.0g` |
| `relrpers` | Relation to coverscreen respondent | `Numeric(Byte)` | `%47.0g` |
| `hhsize` | Household size | `Numeric(Byte)` | `%9.0g` |
| `fam_resp` | Family respondent | `Numeric(Byte)` | `%21.0g` |
| `fin_resp` | Financial respondent | `Numeric(Byte)` | `%24.0g` |
| `hou_resp` | Household respondent | `Numeric(Byte)` | `%24.0g` |
| `ILgroup` | Population group (Israel only) | `Numeric(Byte)` | `%38.0g` |
| `interview` | Interview done in wave 2 | `Numeric(Byte)` | `%21.0g` |
| `int_year` | Interview year | `Numeric(Int)` | `%14.0g` |
| `int_month` | Interview month | `Numeric(Byte)` | `%14.0g` |

### `dn` - Demographics

- Dataset: `sharew2_rel9-0-0_dn.dta`
- Read with: `ps.read_share_module("dn", wave=2)`
- Rows: 37,132
- Variables: 79
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `dn002_` | Month of birth | `Numeric(Byte)` | `%10.0g` |
| `dn003_` | Year of birth | `Numeric(Int)` | `%10.0g` |
| `dn042_` | Male or female | `Numeric(Byte)` | `%10.0g` |
| `dn038_` | Who answered the questions in dn | `Numeric(Byte)` | `%20.0g` |
| `dn043_` | Confirm month/year birth | `Numeric(Byte)` | `%10.0g` |
| `dn044_` | Marital status changed | `Numeric(Byte)` | `%49.0g` |
| `dn004_` | Born in the country of interview | `Numeric(Byte)` | `%10.0g` |
| `dn005c` | Foreign country of birth coding | `Numeric(Int)` | `%46.0g` |
| `dn006_` | Year came to live in country | `Numeric(Int)` | `%10.0g` |
| `dn007_` | Citizenship country of interview | `Numeric(Byte)` | `%10.0g` |
| `dn008c` | Other citizenship coding | `Numeric(Int)` | `%46.0g` |
| `dn009_` | Country-specific question | `Numeric(Byte)` | `%25.0g` |
| `dn010_` | Highest school degree obtained | `Numeric(Byte)` | `%47.0g` |
| `dn041_` | Years education | `Numeric(Float)` | `%35.0g` |
| `dn014_` | Marital status | `Numeric(Byte)` | `%39.0g` |
| `dn015_` | Year of marriage, if living together | `Numeric(Int)` | `%10.0g` |
| `dn016_` | Year of registered partnership | `Numeric(Int)` | `%10.0g` |
| `dn017_` | Year of marriage, if living separated | `Numeric(Int)` | `%10.0g` |
| `dn018_` | Since when divorced | `Numeric(Int)` | `%10.0g` |
| `dn019_` | Since when widowed | `Numeric(Int)` | `%10.0g` |
| `dn020_` | Year of birth of former partner | `Numeric(Int)` | `%12.0g` |
| `dn021_` | Highest educational degree of former partner | `Numeric(Byte)` | `%47.0g` |
| `dn040_` | Partner outside household | `Numeric(Byte)` | `%10.0g` |
| `dn026_1` | Is natural parent still alive: mother | `Numeric(Byte)` | `%10.0g` |
| `dn027_1` | Age of death of parent: mother | `Numeric(Int)` | `%10.0g` |
| `dn028_1` | Age of natural parent: mother | `Numeric(Int)` | `%10.0g` |
| `dn030_1` | Where does parent live: mother | `Numeric(Byte)` | `%48.0g` |
| `dn032_1` | Personal contact with parent during past 12 months: mother | `Numeric(Byte)` | `%27.0g` |
| `dn033_1` | Health of parent: mother | `Numeric(Byte)` | `%13.0g` |
| `dn026_2` | Is natural parent still alive: father | `Numeric(Byte)` | `%10.0g` |
| `dn027_2` | Age of death of parent: father | `Numeric(Int)` | `%10.0g` |
| `dn028_2` | Age of natural parent: father | `Numeric(Int)` | `%10.0g` |
| `dn030_2` | Where does parent live: father | `Numeric(Byte)` | `%48.0g` |
| `dn032_2` | Personal contact with parent during past 12 months: father | `Numeric(Byte)` | `%27.0g` |
| `dn033_2` | Health of parent: father | `Numeric(Byte)` | `%13.0g` |
| `dn034_` | Ever had any siblings | `Numeric(Byte)` | `%10.0g` |
| `dn035_` | Oldest or youngest child | `Numeric(Byte)` | `%12.0g` |
| `dn036_` | How many brothers alive | `Numeric(Byte)` | `%10.0g` |
| `dn037_` | How many sisters alive | `Numeric(Byte)` | `%10.0g` |
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
| `dn012dot` | Further education: other | `Numeric(Byte)` | `%12.0g` |
| `dn012dno` | Further education: none | `Numeric(Byte)` | `%12.0g` |
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
| `dn023dot` | Further education former partner: other | `Numeric(Byte)` | `%12.0g` |
| `dn023dno` | Further education former partner: none | `Numeric(Byte)` | `%12.0g` |

### `ep` - Employment and Pensions

- Dataset: `sharew2_rel9-0-0_ep.dta`
- Read with: `ps.read_share_module("ep", wave=2)`
- Rows: 37,132
- Variables: 609
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `ep002_` | Did nevertheless any paid work last four weeks | `Numeric(Byte)` | `%10.0g` |
| `ep005_` | Current job situation | `Numeric(Byte)` | `%65.0g` |
| `ep006_` | Ever done paid work | `Numeric(Byte)` | `%10.0g` |
| `ep007_` | Currently more than one job | `Numeric(Byte)` | `%10.0g` |
| `ep009_` | Employee or self-employed | `Numeric(Byte)` | `%47.0g` |
| `ep010_` | Start of current job (year) | `Numeric(Int)` | `%12.0g` |
| `ep011_` | Term of job | `Numeric(Byte)` | `%10.0g` |
| `ep012_` | Total contracted hours per week in this job | `Numeric(Double)` | `%10.0g` |
| `ep013_` | Total hours usually working per week | `Numeric(Double)` | `%10.0g` |
| `ep014_` | Months per year working in the job (number) | `Numeric(Byte)` | `%10.0g` |
| `ep016_` | Name or title of job | `Numeric(Byte)` | `%63.0g` |
| `ep018_` | Kind of industry working in | `Numeric(Byte)` | `%98.0g` |
| `ep019_` | Firm belongs to the public sector | `Numeric(Byte)` | `%10.0g` |
| `ep021_` | Responsibility for supervising other employees | `Numeric(Byte)` | `%10.0g` |
| `ep022_` | Number of people responsible for | `Numeric(Byte)` | `%11.0g` |
| `ep024_` | Number of employees | `Numeric(Byte)` | `%11.0g` |
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
| `ep038_` | Frequency of payment in job | `Numeric(Byte)` | `%29.0g` |
| `ep041e` | Taken home from work before tax | `Numeric(Double)` | `%10.0g` |
| `ep041ub` | Taken home from work before tax ub | `Numeric(Byte)` | `%32.0g` |
| `ep041v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ep041v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ep041v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ep045e` | Total amount before tax profits end of year | `Numeric(Double)` | `%10.0g` |
| `ep045ub` | Total amount before tax profits end of year ub | `Numeric(Byte)` | `%32.0g` |
| `ep045v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ep045v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ep045v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ep049_` | Years working in last job | `Numeric(Float)` | `%10.0g` |
| `ep050_` | Year last job ended | `Numeric(Int)` | `%10.0g` |
| `ep051_` | Employee or a self employed in last job | `Numeric(Byte)` | `%36.0g` |
| `ep052_` | Name or title of last job | `Numeric(Byte)` | `%63.0g` |
| `ep054_` | Kind of industry working in last job | `Numeric(Byte)` | `%98.0g` |
| `ep055_` | Employed in the public sector, last job | `Numeric(Byte)` | `%10.0g` |
| `ep057_` | Responsibility for supervising others, last job | `Numeric(Byte)` | `%10.0g` |
| `ep058_` | Number of people responsible for, last job | `Numeric(Byte)` | `%11.0g` |
| `ep059_` | Opportunities to work after the official retirement age | `Numeric(Byte)` | `%10.0g` |
| `ep061_` | Number of employees, last job | `Numeric(Byte)` | `%11.0g` |
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
| `ep065_` | Retirement been a relief or a concern | `Numeric(Byte)` | `%30.0g` |
| `ep067_` | How became unemployed | `Numeric(Byte)` | `%55.0g` |
| `ep068_` | Disability caused by work | `Numeric(Byte)` | `%10.0g` |
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
| `ep078e_1` | Typical payment of pension in c1 last year (ep071d1) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_1` | Typical payment of pension in c1 last year ub (ep071d1) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_2` | Typical payment of pension in c2 last year (ep071d2) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_2` | Typical payment of pension in c2 last year ub (ep071d2) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_3` | Typical payment of pension in c3 last year (ep071d3) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_3` | Typical payment of pension in c3 last year ub (ep071d3) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_4` | Typical payment of pension in c4 last year (ep071d4) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_4` | Typical payment of pension in c4 last year ub (ep071d4) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_5` | Typical payment of pension in c5 last year (ep071d5) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_5` | Typical payment of pension in c5 last year ub (ep071d5) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_6` | Typical payment of pension in c6 last year (ep071d6) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_6` | Typical payment of pension in c6 last year ub (ep071d6) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_7` | Typical payment of pension in c7 last year (ep071d7) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_7` | Typical payment of pension in c7 last year ub (ep071d7) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_8` | Typical payment of pension in c8 last year (ep071d8) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_8` | Typical payment of pension in c8 last year ub (ep071d8) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_9` | Typical payment of pension in c9 last year (ep071d9) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_9` | Typical payment of pension in c9 last year ub (ep071d9) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_10` | Typical payment of pension in c10 last year (ep071d10) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_10` | Typical payment of pension in c10 last year ub (ep071d10) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_11` | Typical payment of pension in c11 last year (ep324d1) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_11` | Typical payment of pension in c11 last year ub (ep324d1) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_12` | Typical payment of pension in c12 last year (ep324d2) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_12` | Typical payment of pension in c12 last year ub (ep324d2) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_13` | Typical payment of pension in c13 last year (ep324d3) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_13` | Typical payment of pension in c13 last year ub (ep324d3) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_14` | Typical payment of pension in c14 last year (ep324d4) | `Numeric(Double)` | `%12.0g` |
| `ep078ub_14` | Typical payment of pension in c14 last year ub (ep324d4) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_15` | Typical payment of pension in c15 last year (ep324d5) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_15` | Typical payment of pension in c15 last year ub (ep324d5) | `Numeric(Byte)` | `%32.0g` |
| `ep078e_16` | Typical payment of pension in c16 last year (ep324d6) | `Numeric(Double)` | `%10.0g` |
| `ep078ub_16` | Typical payment of pension in c16 last year ub (ep324d6) | `Numeric(Byte)` | `%32.0g` |
| `ep078v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ep078v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ep078v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `ep081_1` | Lump sum payment income source c1 (ep071d1) | `Numeric(Byte)` | `%10.0g` |
| `ep081_2` | Lump sum payment income source c2 (ep071d2) | `Numeric(Byte)` | `%10.0g` |
| `ep081_3` | Lump sum payment income source c3 (ep071d3) | `Numeric(Byte)` | `%10.0g` |
| `ep081_4` | Lump sum payment income source c4 (ep071d4) | `Numeric(Byte)` | `%10.0g` |
| `ep081_5` | Lump sum payment income source c5 (ep071d5) | `Numeric(Byte)` | `%10.0g` |
| `ep081_6` | Lump sum payment income source c6 (ep071d6) | `Numeric(Byte)` | `%10.0g` |
| `ep081_7` | Lump sum payment income source c7 (ep071d7) | `Numeric(Byte)` | `%10.0g` |
| `ep081_8` | Lump sum payment income source c8 (ep071d8) | `Numeric(Byte)` | `%10.0g` |
| `ep081_9` | Lump sum payment income source c9 (ep071d9) | `Numeric(Byte)` | `%10.0g` |
| `ep081_10` | Lump sum payment income source c10 (ep071d10) | `Numeric(Byte)` | `%10.0g` |
| `ep081_11` | Lump sum payment income source c11 (ep324d1) | `Numeric(Byte)` | `%10.0g` |
| `ep081_12` | Lump sum payment income source c12 (ep324d2) | `Numeric(Byte)` | `%10.0g` |
| `ep081_13` | Lump sum payment income source c13 (ep324d3) | `Numeric(Byte)` | `%10.0g` |
| `ep081_14` | Lump sum payment income source c14 (ep324d4) | `Numeric(Byte)` | `%10.0g` |
| `ep081_15` | Lump sum payment income source c15 (ep324d5) | `Numeric(Byte)` | `%10.0g` |
| `ep081_16` | Lump sum payment income source c16 (ep324d6) | `Numeric(Byte)` | `%10.0g` |
| `ep082e_1` | Total amount of lump sum payment income source c1 last year (ep071d1) | `Numeric(Double)` | `%10.0g` |
| `ep082ub_1` | Total amount of lump sum payment income source c1 ub  last year (ep071d1) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_2` | Total amount of lump sum payment income source c2 last year (ep071d2) | `Numeric(Double)` | `%10.0g` |
| `ep082ub_2` | Total amount of lump sum payment income source c2 ub  last year (ep071d2) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_3` | Total amount of lump sum payment income source c3 last year (ep071d3) | `Numeric(Double)` | `%10.0g` |
| `ep082ub_3` | Total amount of lump sum payment income source c3 ub  last year (ep071d3) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_4` | Total amount of lump sum payment income source c4 last year (ep071d4) | `Numeric(Double)` | `%10.0g` |
| `ep082ub_4` | Total amount of lump sum payment income source c4 ub  last year (ep071d4) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_5` | Total amount of lump sum payment income source c5 last year (ep071d5) | `Numeric(Double)` | `%10.0g` |
| `ep082ub_5` | Total amount of lump sum payment income source c5 ub  last year (ep071d5) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_6` | Total amount of lump sum payment income source c6 last year (ep071d6) | `Numeric(Double)` | `%10.0g` |
| `ep082ub_6` | Total amount of lump sum payment income source c6 ub  last year (ep071d6) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_7` | Total amount of lump sum payment income source c7 last year (ep071d7) | `Numeric(Double)` | `%10.0g` |
| `ep082ub_7` | Total amount of lump sum payment income source c7 ub  last year (ep071d7) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_8` | Total amount of lump sum payment income source c8 last year (ep071d8) | `Numeric(Long)` | `%10.0g` |
| `ep082ub_8` | Total amount of lump sum payment income source c8 ub  last year (ep071d8) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_9` | Total amount of lump sum payment income source c9 last year (ep071d9) | `Numeric(Double)` | `%10.0g` |
| `ep082ub_9` | Total amount of lump sum payment income source c9 ub  last year (ep071d9) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_10` | Total amount of lump sum payment income source c10 last year (ep071d10) | `Numeric(Int)` | `%10.0g` |
| `ep082ub_10` | Total amount of lump sum payment income source c10 ub  last year (ep071d10) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_11` | Total amount of lump sum payment income source c11 last year (ep324d1) | `Numeric(Double)` | `%10.0g` |
| `ep082ub_11` | Total amount of lump sum payment income source c11 last year ub (ep324d1) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_12` | Total amount of lump sum payment income source c12 last year (ep324d2) | `Numeric(Double)` | `%10.0g` |
| `ep082ub_12` | Total amount of lump sum payment income source c12 last year ub (ep324d2) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_13` | Total amount of lump sum payment income source c13 last year (ep324d3) | `Numeric(Float)` | `%10.0g` |
| `ep082ub_13` | Total amount of lump sum payment income source c13 last year ub (ep324d3) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_14` | Total amount of lump sum payment income source c14 last year (ep324d4) | `Numeric(Double)` | `%10.0g` |
| `ep082ub_14` | Total amount of lump sum payment income source c14 last year ub (ep324d4) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_15` | Total amount of lump sum payment income source c15 last year (ep324d5) | `Numeric(Float)` | `%10.0g` |
| `ep082ub_15` | Total amount of lump sum payment income source c15 last year ub (ep324d5) | `Numeric(Byte)` | `%32.0g` |
| `ep082e_16` | Total amount of lump sum payment income source c16 last year (ep324d6) | `Numeric(Double)` | `%10.0g` |
| `ep082ub_16` | Total amount of lump sum payment income source c16 last year ub (ep324d6) | `Numeric(Byte)` | `%32.0g` |
| `ep082v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ep082v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ep082v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `ep089d1` | Regular payments received: life insurance | `Numeric(Byte)` | `%12.0g` |
| `ep089d2` | Regular payments received: private annuity/private personal pension | `Numeric(Byte)` | `%12.0g` |
| `ep089d3` | Regular payments received: alimony | `Numeric(Byte)` | `%12.0g` |
| `ep089d4` | Regular payments received: from charities | `Numeric(Byte)` | `%12.0g` |
| `ep089d5` | Regular payments received: long-term care private insurance | `Numeric(Byte)` | `%12.0g` |
| `ep089dno` | Regular payments received: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep090_1` | Period received payment c1 | `Numeric(Byte)` | `%28.0g` |
| `ep090_2` | Period received payment c2 | `Numeric(Byte)` | `%28.0g` |
| `ep090_3` | Period received payment c3 | `Numeric(Byte)` | `%28.0g` |
| `ep090_4` | Period received payment c4 | `Numeric(Byte)` | `%28.0g` |
| `ep090_5` | Period received payment c5 | `Numeric(Byte)` | `%28.0g` |
| `ep092_1` | Additional payments for this benefit in last year, payment c1 | `Numeric(Byte)` | `%10.0g` |
| `ep092_2` | Additional payments for this benefit in last year, payment c2 | `Numeric(Byte)` | `%10.0g` |
| `ep092_3` | Additional payments for this benefit in last year, payment c3 | `Numeric(Byte)` | `%10.0g` |
| `ep092_4` | Additional payments for this benefit in last year, payment c4 | `Numeric(Byte)` | `%10.0g` |
| `ep092_5` | Additional payments for this benefit in last year, payment c5 | `Numeric(Byte)` | `%10.0g` |
| `ep094e_1` | Total amount payment c1 last year | `Numeric(Double)` | `%10.0g` |
| `ep094ub_1` | Total amount payment c1 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094e_2` | Total amount payment c2 last year | `Numeric(Double)` | `%10.0g` |
| `ep094ub_2` | Total amount payment c2 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094e_3` | Total amount payment c3 last year | `Numeric(Double)` | `%10.0g` |
| `ep094ub_3` | Total amount payment c3 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094e_4` | Total amount payment c4 last year | `Numeric(Double)` | `%10.0g` |
| `ep094ub_4` | Total amount payment c4 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094e_5` | Total amount payment c5 last year | `Numeric(Double)` | `%10.0g` |
| `ep094ub_5` | Total amount payment c5 last year ub | `Numeric(Byte)` | `%32.0g` |
| `ep094v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ep094v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ep094v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
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
| `ep098dno` | Type of pension entitled to: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep102_1` | Compulsory or voluntary participation in pension c1 | `Numeric(Byte)` | `%10.0g` |
| `ep102_2` | Compulsory or voluntary participation in pension c2 | `Numeric(Byte)` | `%10.0g` |
| `ep102_3` | Compulsory or voluntary participation in pension c3 | `Numeric(Byte)` | `%10.0g` |
| `ep102_4` | Compulsory or voluntary participation in pension c4 | `Numeric(Byte)` | `%10.0g` |
| `ep102_5` | Compulsory or voluntary participation in pension c5 | `Numeric(Byte)` | `%10.0g` |
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
| `ep109_1` | Percentage of salary received as pension c1 | `Numeric(Byte)` | `%10.0g` |
| `ep109_2` | Percentage of salary received as pension c2 | `Numeric(Byte)` | `%10.0g` |
| `ep109_3` | Percentage of salary received as pension c3 | `Numeric(Byte)` | `%10.0g` |
| `ep109_4` | Percentage of salary received as pension c4 | `Numeric(Byte)` | `%10.0g` |
| `ep109_5` | Percentage of salary received as pension c5 | `Numeric(Byte)` | `%10.0g` |
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
| `ep111_2_1` | Receive early retirement pension period 1 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_2_2` | Receive early retirement pension period 2 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_2_3` | Receive early retirement pension period 3 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_2_4` | Receive early retirement pension period 4 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_2_5` | Receive early retirement pension period 5 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_3_1` | Receive unemployment benefits period 1 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_3_2` | Receive unemployment benefits period 2 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_3_3` | Receive unemployment benefits period 3 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_3_4` | Receive unemployment benefits period 4 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_3_5` | Receive unemployment benefits period 5 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_4_1` | Receive sickness benefits period 1 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_4_2` | Receive sickness benefits period 2 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_4_3` | Receive sickness benefits period 3 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_4_4` | Receive sickness benefits period 4 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_1` | Receive disability insurance period 1 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_2` | Receive disability insurance period 2 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_3` | Receive disability insurance period 3 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_4` | Receive disability insurance period 4 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_5` | Receive disability insurance period 5 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_6` | Receive disability insurance period 6 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_7` | Receive disability insurance period 7 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_8` | Receive disability insurance period 8 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_9` | Receive disability insurance period 9 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_10` | Receive disability insurance period 10 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_11` | Receive disability insurance period 11 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_12` | Receive disability insurance period 12 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_13` | Receive disability insurance period 13 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_14` | Receive disability insurance period 14 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_15` | Receive disability insurance period 15 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_16` | Receive disability insurance period 16 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_17` | Receive disability insurance period 17 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_18` | Receive disability insurance period 18 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_19` | Receive disability insurance period 19 from month | `Numeric(Byte)` | `%10.0g` |
| `ep111_5_20` | Receive disability insurance period 20 from month | `Numeric(Byte)` | `%10.0g` |
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
| `ep112_2_1` | Receive early retirement pension period 1 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_2_2` | Receive early retirement pension period 2 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_2_3` | Receive early retirement pension period 3 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_2_4` | Receive early retirement pension period 4 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_2_5` | Receive early retirement pension period 5 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_3_1` | Receive unemployment benefits period 1 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_3_2` | Receive unemployment benefits period 2 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_3_3` | Receive unemployment benefits period 3 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_3_4` | Receive unemployment benefits period 4 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_3_5` | Receive unemployment benefits period 5 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_4_1` | Receive sickness benefits period 1 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_4_2` | Receive sickness benefits period 2 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_4_3` | Receive sickness benefits period 3 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_4_4` | Receive sickness benefits period 4 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_1` | Receive disability insurance period 1 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_2` | Receive disability insurance period 2 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_3` | Receive disability insurance period 3 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_4` | Receive disability insurance period 4 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_5` | Receive disability insurance period 5 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_6` | Receive disability insurance period 6 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_7` | Receive disability insurance period 7 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_8` | Receive disability insurance period 8 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_9` | Receive disability insurance period 9 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_10` | Receive disability insurance period 10 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_11` | Receive disability insurance period 11 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_12` | Receive disability insurance period 12 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_13` | Receive disability insurance period 13 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_14` | Receive disability insurance period 14 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_15` | Receive disability insurance period 15 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_16` | Receive disability insurance period 16 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_17` | Receive disability insurance period 17 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_18` | Receive disability insurance period 18 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_19` | Receive disability insurance period 19 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_5_20` | Receive disability insurance period 20 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_6_1` | Receive social assistance period 1 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_6_2` | Receive social assistance period 2 from year | `Numeric(Byte)` | `%15.0g` |
| `ep112_6_3` | Receive social assistance period 3 from year | `Numeric(Byte)` | `%15.0g` |
| `ep113_1_1` | Receive old age pension period 1 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_1_2` | Receive old age pension period 2 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_1_3` | Receive old age pension period 3 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_1_4` | Receive old age pension period 4 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_1_5` | Receive old age pension period 5 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_1_6` | Receive old age pension period 6 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_1_7` | Receive old age pension period 7 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_2_1` | Receive early retirement pension period 1 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_2_2` | Receive early retirement pension period 2 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_2_3` | Receive early retirement pension period 3 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_2_4` | Receive early retirement pension period 4 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_2_5` | Receive early retirement pension period 5 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_3_1` | Receive unemployment benefits period 1 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_3_2` | Receive unemployment benefits period 2 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_3_3` | Receive unemployment benefits period 3 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_3_4` | Receive unemployment benefits period 4 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_3_5` | Receive unemployment benefits period 5 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_4_1` | Receive sickness benefits period 1 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_4_2` | Receive sickness benefits period 2 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_4_3` | Receive sickness benefits period 3 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_4_4` | Receive sickness benefits period 4 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_1` | Receive disability insurance period 1 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_2` | Receive disability insurance period 2 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_3` | Receive disability insurance period 3 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_4` | Receive disability insurance period 4 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_5` | Receive disability insurance period 5 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_6` | Receive disability insurance period 6 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_7` | Receive disability insurance period 7 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_8` | Receive disability insurance period 8 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_9` | Receive disability insurance period 9 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_10` | Receive disability insurance period 10 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_11` | Receive disability insurance period 11 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_12` | Receive disability insurance period 12 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_13` | Receive disability insurance period 13 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_14` | Receive disability insurance period 14 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_15` | Receive disability insurance period 15 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_16` | Receive disability insurance period 16 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_17` | Receive disability insurance period 17 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_18` | Receive disability insurance period 18 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_19` | Receive disability insurance period 19 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_5_20` | Receive disability insurance period 20 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_6_1` | Receive social assistance period 1 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_6_2` | Receive social assistance period 2 to month | `Numeric(Byte)` | `%10.0g` |
| `ep113_6_3` | Receive social assistance period 3 to month | `Numeric(Byte)` | `%10.0g` |
| `ep114_1_1` | Receive old age pension period 1 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_1_2` | Receive old age pension period 2 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_1_3` | Receive old age pension period 3 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_1_4` | Receive old age pension period 4 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_2_1` | Receive early retirement pension period 1 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_2_2` | Receive early retirement pension period 2 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_2_3` | Receive early retirement pension period 3 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_2_4` | Receive early retirement pension period 4 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_3_1` | Receive unemployment benefits period 1 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_3_2` | Receive unemployment benefits period 2 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_3_3` | Receive unemployment benefits period 3 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_3_4` | Receive unemployment benefits period 4 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_4_1` | Receive sickness benefits period 1 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_4_2` | Receive sickness benefits period 2 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_4_3` | Receive sickness benefits period 3 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_4_4` | Receive sickness benefits period 4 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_5_1` | Receive disability insurance period 1 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_5_2` | Receive disability insurance period 2 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_5_3` | Receive disability insurance period 3 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_5_12` | Receive disability insurance period 12 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_6_1` | Receive social assistance period 1 to year | `Numeric(Byte)` | `%10.0g` |
| `ep114_6_2` | Receive social assistance period 2 to year | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_1` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_2` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_3` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_4` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_5` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_6` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_1_7` | Receive old age pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_2_1` | Receive early retirement pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_2_2` | Receive early retirement pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_2_3` | Receive early retirement pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_2_4` | Receive early retirement pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_2_5` | Receive early retirement pension other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_3_1` | Receive unemployment benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_3_2` | Receive unemployment benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_3_3` | Receive unemployment benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_3_4` | Receive unemployment benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_3_5` | Receive unemployment benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_4_1` | Receive sickness benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_4_2` | Receive sickness benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_4_3` | Receive sickness benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_4_4` | Receive sickness benefits other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_1` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_2` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_3` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_4` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_5` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_6` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_7` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_8` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_9` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_10` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_11` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_12` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_13` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_14` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_15` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_16` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_17` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_18` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_19` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_5_20` | Receive disability insurance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_6_1` | Receive social assistance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_6_2` | Receive social assistance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep116_6_3` | Receive social assistance other episodes | `Numeric(Byte)` | `%10.0g` |
| `ep122_` | Receive severance month | `Numeric(Byte)` | `%10.0g` |
| `ep123_` | Receive severance year | `Numeric(Byte)` | `%10.0g` |
| `ep125_` | Continuously working | `Numeric(Byte)` | `%10.0g` |
| `ep127_1` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_2` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_3` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_4` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_5` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_6` | Period from month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep127_21` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_22` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_23` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_24` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep127_25` | Period from month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep128_1` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_2` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_3` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_4` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_5` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_6` | Period from year (working) | `Numeric(Byte)` | `%17.0g` |
| `ep128_21` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_22` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_23` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_24` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep128_25` | Period from year (unemployed) | `Numeric(Byte)` | `%17.0g` |
| `ep129_1` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_2` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_3` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_4` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_5` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_6` | Period to month (working) | `Numeric(Byte)` | `%10.0g` |
| `ep129_21` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_22` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_23` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_24` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep129_25` | Period to month (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep130_1` | Period to year (working) | `Numeric(Byte)` | `%10.0g` |
| `ep130_2` | Period to year (working) | `Numeric(Byte)` | `%10.0g` |
| `ep130_3` | Period to year (working) | `Numeric(Byte)` | `%10.0g` |
| `ep130_4` | Period to year (working) | `Numeric(Byte)` | `%10.0g` |
| `ep130_5` | Period to year (working) | `Numeric(Byte)` | `%10.0g` |
| `ep130_6` | Period to year (working) | `Numeric(Byte)` | `%10.0g` |
| `ep130_21` | Period to year (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep130_22` | Period to year (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep130_23` | Period to year (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep130_24` | Period to year (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep130_25` | Period to year (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_1` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_2` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_3` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_4` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_5` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_6` | Other periods (working) | `Numeric(Byte)` | `%10.0g` |
| `ep133_21` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_22` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_23` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_24` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep133_25` | Other periods (unemployed) | `Numeric(Byte)` | `%10.0g` |
| `ep141d1` | Change in job: type of employment | `Numeric(Byte)` | `%12.0g` |
| `ep141d2` | Change in job: employer | `Numeric(Byte)` | `%12.0g` |
| `ep141d3` | Change in job: promotion | `Numeric(Byte)` | `%12.0g` |
| `ep141d4` | Change in job: job location | `Numeric(Byte)` | `%12.0g` |
| `ep141d5` | Change in job: contract length | `Numeric(Byte)` | `%12.0g` |
| `ep141dno` | Change in job: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep201e` | Taken home from work after tax, (main) job | `Numeric(Double)` | `%10.0g` |
| `ep201ub` | Taken home from work after tax, (main) job | `Numeric(Byte)` | `%32.0g` |
| `ep201v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ep201v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ep201v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `ep204_` | Any earnings from employment previous year | `Numeric(Byte)` | `%10.0g` |
| `ep205e` | Earnings employment per year after taxes | `Numeric(Double)` | `%10.0g` |
| `ep205ub` | Earnings employment per year after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep205v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `ep205v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ep205v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ep206_` | Income from self-employment previous year | `Numeric(Byte)` | `%10.0g` |
| `ep207e` | Earnings self-employment per year after taxes | `Numeric(Double)` | `%10.0g` |
| `ep207ub` | Earnings self-employment per year after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep207v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `ep207v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ep207v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ep208_1` | How many months received income source c1 (ep071d1) | `Numeric(Byte)` | `%10.0g` |
| `ep208_2` | How many months received income source c2 (ep071d2) | `Numeric(Byte)` | `%10.0g` |
| `ep208_3` | How many months received income source c3 (ep071d3) | `Numeric(Byte)` | `%10.0g` |
| `ep208_4` | How many months received income source c4 (ep071d4) | `Numeric(Byte)` | `%10.0g` |
| `ep208_5` | How many months received income source c5 (ep071d5) | `Numeric(Byte)` | `%10.0g` |
| `ep208_6` | How many months received income source c6 (ep071d6) | `Numeric(Byte)` | `%10.0g` |
| `ep208_7` | How many months received income source c7 (ep071d7) | `Numeric(Byte)` | `%10.0g` |
| `ep208_8` | How many months received income source c8 (ep071d8) | `Numeric(Byte)` | `%10.0g` |
| `ep208_9` | How many months received income source c9 (ep071d9) | `Numeric(Byte)` | `%10.0g` |
| `ep208_10` | How many months received income source c10 (ep071d10) | `Numeric(Byte)` | `%10.0g` |
| `ep208_11` | How many months received income source c11 (ep324d1) | `Numeric(Byte)` | `%10.0g` |
| `ep208_12` | How many months received income source c12 (ep324d2) | `Numeric(Byte)` | `%10.0g` |
| `ep208_13` | How many months received income source c13 (ep324d3) | `Numeric(Byte)` | `%10.0g` |
| `ep208_14` | How many months received income source c14 (ep324d4) | `Numeric(Byte)` | `%10.0g` |
| `ep208_15` | How many months received income source c15 (ep324d5) | `Numeric(Byte)` | `%10.0g` |
| `ep208_16` | How many months received income source c16 (ep324d6) | `Numeric(Byte)` | `%10.0g` |
| `ep209e_1` | Additional payments c1 after taxes | `Numeric(Double)` | `%10.0g` |
| `ep209ub_1` | Additional payments c1 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209e_2` | Additional payments c2 after taxes | `Numeric(Double)` | `%10.0g` |
| `ep209ub_2` | Additional payments c2 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209e_3` | Additional payments c3 after taxes | `Numeric(Float)` | `%10.0g` |
| `ep209ub_3` | Additional payments c3 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209e_4` | Additional payments c4 after taxes | `Numeric(Float)` | `%10.0g` |
| `ep209ub_4` | Additional payments c4 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209e_5` | Additional payments c5 after taxes | `Numeric(Long)` | `%10.0g` |
| `ep209ub_5` | Additional payments c5 after taxes ub | `Numeric(Byte)` | `%32.0g` |
| `ep209v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ep209v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ep209v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `ep210_` | Who answered section ep | `Numeric(Byte)` | `%20.0g` |
| `ep213_1` | First year received income source c1 (ep071d1) | `Numeric(Int)` | `%12.0g` |
| `ep213_2` | First year received income source c2 (ep071d2) | `Numeric(Int)` | `%10.0g` |
| `ep213_3` | First year received income source c3 (ep071d3) | `Numeric(Int)` | `%10.0g` |
| `ep213_4` | First year received income source c4 (ep071d4) | `Numeric(Int)` | `%10.0g` |
| `ep213_5` | First year received income source c5 (ep071d5) | `Numeric(Int)` | `%10.0g` |
| `ep213_6` | First year received income source c6 (ep071d6) | `Numeric(Int)` | `%10.0g` |
| `ep213_7` | First year received income source c7 (ep071d7) | `Numeric(Int)` | `%10.0g` |
| `ep213_8` | First year received income source c8 (ep071d8) | `Numeric(Int)` | `%10.0g` |
| `ep213_9` | First year received income source c9 (ep071d9) | `Numeric(Int)` | `%10.0g` |
| `ep213_10` | First year received income source c10 (ep071d10) | `Numeric(Int)` | `%10.0g` |
| `ep213_11` | First year received income source c11 (ep324d1) | `Numeric(Int)` | `%12.0g` |
| `ep213_12` | First year received income source c12 (ep324d2) | `Numeric(Int)` | `%10.0g` |
| `ep213_13` | First year received income source c13 (ep324d3) | `Numeric(Int)` | `%10.0g` |
| `ep213_14` | First year received income source c14 (ep324d4) | `Numeric(Int)` | `%10.0g` |
| `ep213_15` | First year received income source c15 (ep324d5) | `Numeric(Int)` | `%10.0g` |
| `ep213_16` | First year received income source c16 (ep324d6) | `Numeric(Int)` | `%12.0g` |
| `ep214_` | Amount includes additional payments | `Numeric(Byte)` | `%10.0g` |
| `ep301_` | Missed days from work the last 12 months | `Numeric(Byte)` | `%10.0g` |
| `ep302_` | How many days missed from work | `Numeric(Int)` | `%10.0g` |
| `ep305e` | Total amount after taxes profits end of year | `Numeric(Double)` | `%10.0g` |
| `ep305ub` | Total amount after taxes profits end of year ub | `Numeric(Byte)` | `%32.0g` |
| `ep305v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ep305v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ep305v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ep314e` | Total amount of additional payments | `Numeric(Double)` | `%10.0g` |
| `ep321_` | Total hours worked per week second job | `Numeric(Double)` | `%12.0g` |
| `ep322_` | Months per year worked in second job (number) | `Numeric(Byte)` | `%10.0g` |
| `ep324d1` | Occupational pension income: old age pension last job | `Numeric(Byte)` | `%12.0g` |
| `ep324d2` | Occupational pension income: old age pension second job | `Numeric(Byte)` | `%12.0g` |
| `ep324d3` | Occupational pension income: old age pension third job | `Numeric(Byte)` | `%12.0g` |
| `ep324d4` | Occupational pension income: early retirement | `Numeric(Byte)` | `%12.0g` |
| `ep324d5` | Occupational pension income: disability/invalidity insurance | `Numeric(Byte)` | `%12.0g` |
| `ep324d6` | Occupational pension income: survivor pension from spouse/partner's job | `Numeric(Byte)` | `%12.0g` |
| `ep324dno` | Occupational pension income: none of these | `Numeric(Byte)` | `%12.0g` |
| `ep325_` | Unemployed since last interview | `Numeric(Byte)` | `%10.0g` |
| `ep326_` | Received severance payment since last interview | `Numeric(Byte)` | `%10.0g` |
| `ep328_` | Retirement month | `Numeric(Byte)` | `%10.0g` |
| `ep329_` | Retirement year | `Numeric(Int)` | `%12.0g` |

### `ex` - Expectations

- Dataset: `sharew2_rel9-0-0_ex.dta`
- Read with: `ps.read_share_module("ex", wave=2)`
- Rows: 37,132
- Variables: 27
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ex001_` | Introduction and example | `Numeric(Byte)` | `%10.0g` |
| `ex002_` | Chance of receiving inheritance | `Numeric(Byte)` | `%10.0g` |
| `ex003_` | Chance inheritance more than 50000 | `Numeric(Byte)` | `%10.0g` |
| `ex004_` | Chance of leaving inheritance more than 50000 | `Numeric(Byte)` | `%10.0g` |
| `ex005_` | Chance of leaving any inheritance | `Numeric(Byte)` | `%10.0g` |
| `ex006_` | Chance of leaving inheritance more than 150000 | `Numeric(Byte)` | `%10.0g` |
| `ex007_` | Chance government reduces pension | `Numeric(Byte)` | `%10.0g` |
| `ex025_` | Chance to work after age of 63 | `Numeric(Byte)` | `%10.0g` |
| `ex008_` | Chance government raises retirement age | `Numeric(Byte)` | `%10.0g` |
| `ex009_` | Life expectancy | `Numeric(Byte)` | `%10.0g` |
| `ex009age` | Life expectancy target age | `Numeric(Int)` | `%10.0g` |
| `ex010_` | Chance standard of living will be better | `Numeric(Byte)` | `%10.0g` |
| `ex011_` | Chance standard of living will be worse | `Numeric(Byte)` | `%10.0g` |
| `ex026_` | Trust in other people | `Numeric(Byte)` | `%10.0g` |
| `ex028_` | Left or right in politics | `Numeric(Byte)` | `%10.0g` |
| `ex029_` | Frequency of praying | `Numeric(Byte)` | `%31.0g` |
| `ex100_` | Partner available and willing to participate | `Numeric(Byte)` | `%62.0g` |
| `ex102_` | Partner years of education | `Numeric(Byte)` | `%10.0g` |
| `ex103_` | Partner current job situation | `Numeric(Byte)` | `%65.0g` |
| `ex104_` | Partner ever done paid work | `Numeric(Byte)` | `%10.0g` |
| `ex105_` | Partner employee or a self-employed | `Numeric(Byte)` | `%36.0g` |

### `ft` - Financial Transfers

- Dataset: `sharew2_rel9-0-0_ft.dta`
- Read with: `ps.read_share_module("ft", wave=2)`
- Rows: 37,132
- Variables: 75
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Float)` | `%9.0g` |
| `ft002_` | Given financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft003_1` | To whom given gift, person 1 | `Numeric(Byte)` | `%18.0g` |
| `ft003_2` | To whom given gift, person 2 | `Numeric(Byte)` | `%18.0g` |
| `ft003_3` | To whom given gift, person 3 | `Numeric(Byte)` | `%18.0g` |
| `ft004e_1` | Amount given to person 1 | `Numeric(Double)` | `%10.0g` |
| `ft004ub_1` | Amount given to person 1 ub | `Numeric(Byte)` | `%32.0g` |
| `ft004e_2` | Amount given to person 2 | `Numeric(Double)` | `%10.0g` |
| `ft004ub_2` | Amount given tp person 2 ub | `Numeric(Byte)` | `%32.0g` |
| `ft004e_3` | Amount given to person 3 | `Numeric(Double)` | `%10.0g` |
| `ft004ub_3` | Amount given tp person 3 ub | `Numeric(Byte)` | `%32.0g` |
| `ft004v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ft004v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ft004v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ft006_1` | Reason given to person 1 | `Numeric(Byte)` | `%67.0g` |
| `ft006_2` | Reason given to person 2 | `Numeric(Byte)` | `%67.0g` |
| `ft006_3` | Reason given to person 3 | `Numeric(Byte)` | `%67.0g` |
| `ft007_1` | Other persons given financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft007_2` | Other persons given financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft007_3` | Other persons given financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft009_` | Received financial gift of 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft010_1` | From whom recieved gift, person 1 | `Numeric(Byte)` | `%18.0g` |
| `ft010_2` | From whom recieved gift, person 2 | `Numeric(Byte)` | `%18.0g` |
| `ft010_3` | From whom recieved gift, person 3 | `Numeric(Byte)` | `%18.0g` |
| `ft011e_1` | Amount received from person 1 | `Numeric(Double)` | `%10.0g` |
| `ft011ub_1` | Amount received from person 1 ub | `Numeric(Byte)` | `%32.0g` |
| `ft011e_2` | Amount received from person 2 | `Numeric(Double)` | `%10.0g` |
| `ft011ub_2` | Amount received from person 2 ub | `Numeric(Byte)` | `%32.0g` |
| `ft011e_3` | Amount received from person 3 | `Numeric(Double)` | `%10.0g` |
| `ft011ub_3` | Amount received from person 3 ub | `Numeric(Byte)` | `%32.0g` |
| `ft011v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ft011v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ft011v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `ft013_1` | Reason received gift from person 1 | `Numeric(Byte)` | `%67.0g` |
| `ft013_2` | Reason received gift from person 2 | `Numeric(Byte)` | `%67.0g` |
| `ft013_3` | Reason received gift from person 3 | `Numeric(Byte)` | `%67.0g` |
| `ft014_1` | From other persons received financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft014_2` | From other persons received financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft014_3` | From other persons received financial gift 250 or more | `Numeric(Byte)` | `%10.0g` |
| `ft015_` | Ever received gift or inheritance (worth 5000 euros or more) | `Numeric(Byte)` | `%10.0g` |
| `ft016_1` | Year, inheritance or large gift 1 received | `Numeric(Int)` | `%12.0g` |
| `ft016_2` | Year, inheritance or large gift 2 received | `Numeric(Int)` | `%10.0g` |
| `ft016_3` | Year, inheritance or large gift 3 received | `Numeric(Int)` | `%10.0g` |
| `ft016_4` | Year, inheritance or large gift 4 received | `Numeric(Int)` | `%10.0g` |
| `ft016_5` | Year, inheritance or large gift 5 received | `Numeric(Int)` | `%10.0g` |
| `ft017_1` | From whom inheritance or large gift 1 | `Numeric(Byte)` | `%18.0g` |
| `ft017_2` | From whom inheritance or large gift 2 | `Numeric(Byte)` | `%18.0g` |
| `ft017_3` | From whom inheritance or large gift 3 | `Numeric(Byte)` | `%18.0g` |
| `ft017_4` | From whom inheritance or large gift 4 | `Numeric(Byte)` | `%18.0g` |
| `ft017_5` | From whom inheritance or large gift 5 | `Numeric(Byte)` | `%18.0g` |
| `ft018e_1` | Value inheritance 1 | `Numeric(Double)` | `%10.0g` |
| `ft018ub_1` | Value inheritance 1 ub | `Numeric(Byte)` | `%32.0g` |
| `ft018e_2` | Value inheritance 2 | `Numeric(Double)` | `%10.0g` |
| `ft018ub_2` | Value inheritance 2 ub | `Numeric(Byte)` | `%32.0g` |
| `ft018e_3` | Value inheritance 3 | `Numeric(Double)` | `%10.0g` |
| `ft018ub_3` | Value inheritance 3 ub | `Numeric(Byte)` | `%32.0g` |
| `ft018e_4` | Value inheritance 4 | `Numeric(Double)` | `%10.0g` |
| `ft018ub_4` | Value inheritance 4 ub | `Numeric(Byte)` | `%32.0g` |
| `ft018e_5` | Value inheritance 5 | `Numeric(Double)` | `%10.0g` |
| `ft018ub_5` | Value inheritance 5 ub | `Numeric(Byte)` | `%32.0g` |
| `ft018v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `ft018v2` | Bracket value 2 | `Numeric(Double)` | `%12.0g` |
| `ft018v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `ft020_1` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft020_2` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft020_3` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft020_4` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft020_5` | Any further gift or inheritance | `Numeric(Byte)` | `%10.0g` |
| `ft021_` | Who answered the questions in ft | `Numeric(Byte)` | `%20.0g` |

### `gs` - Grip Strength

- Dataset: `sharew2_rel9-0-0_gs.dta`
- Read with: `ps.read_share_module("gs", wave=2)`
- Rows: 37,132
- Variables: 23
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `gs001_` | Willing to have handgrip measured | `Numeric(Byte)` | `%58.0g` |
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
| `gs012_` | How much effort gave r | `Numeric(Byte)` | `%90.0g` |
| `gs013_` | The position of r for this test | `Numeric(Byte)` | `%10.0g` |
| `gs014_` | R rested his/her arms on a support | `Numeric(Byte)` | `%10.0g` |

### `hc` - Health Care

- Dataset: `sharew2_rel9-0-0_hc.dta`
- Read with: `ps.read_share_module("hc", wave=2)`
- Rows: 37,132
- Variables: 116
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `hc002_` | How often seen or talked to medical doctor last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc003_` | How many of these contacts with general practitioner | `Numeric(Byte)` | `%10.0g` |
| `hc004_` | Contacts with specialists | `Numeric(Byte)` | `%10.0g` |
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
| `hc010_` | Seen a dentist/dental hygienist in the last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc011_` | Contact dentist for routine control/prevention or treatment | `Numeric(Byte)` | `%38.0g` |
| `hc012_` | Stayed over night in hospital last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc013_` | Times being patient in hospital | `Numeric(Byte)` | `%10.0g` |
| `hc014_` | Total nights stayed in hospital | `Numeric(Int)` | `%10.0g` |
| `hc015d1` | Reason hospital: inpatient surgery | `Numeric(Byte)` | `%12.0g` |
| `hc015d2` | Reason hospital: medical tests or non-surgical treatments | `Numeric(Byte)` | `%12.0g` |
| `hc015d3` | Reason hospital: mental health problems | `Numeric(Byte)` | `%12.0g` |
| `hc016_` | Times overnight in hospital for surgery | `Numeric(Byte)` | `%10.0g` |
| `hc022_` | Times overnight in hospital for mental health problems | `Numeric(Byte)` | `%10.0g` |
| `hc023_` | Had outpatient surgery last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc024_` | Times had outpatient surgery last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc029_` | In a nursing home during last 12 months | `Numeric(Byte)` | `%16.0g` |
| `hc030_` | Times stayed in a nursing home overnight | `Numeric(Int)` | `%10.0g` |
| `hc031_` | Weeks stayed in a nursing home | `Numeric(Byte)` | `%10.0g` |
| `hc032d1` | Received home care: nursing or personal care | `Numeric(Byte)` | `%12.0g` |
| `hc032d2` | Received home care: domestic tasks | `Numeric(Byte)` | `%12.0g` |
| `hc032d3` | Received home care: meals-on-wheels | `Numeric(Byte)` | `%12.0g` |
| `hc032dno` | Received home care: none of these | `Numeric(Byte)` | `%12.0g` |
| `hc033_` | Weeks received professional nursing care | `Numeric(Byte)` | `%10.0g` |
| `hc034_` | Hours received professional nursing care | `Numeric(Int)` | `%10.0g` |
| `hc035_` | Weeks received paid domestic help | `Numeric(Byte)` | `%10.0g` |
| `hc036_` | Hours received paid domestic help | `Numeric(Int)` | `%10.0g` |
| `hc037_` | Weeks received meals-on-wheels | `Numeric(Byte)` | `%10.0g` |
| `hc038_` | Received care from private providers | `Numeric(Byte)` | `%10.0g` |
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
| `hc045e` | Paid out-of-pocket for inpatient care | `Numeric(Double)` | `%10.0g` |
| `hc045ub` | Paid out-of-pocket for inpatient care ub | `Numeric(Byte)` | `%32.0g` |
| `hc045v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `hc045v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `hc045v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `hc047e` | Paid out-of-pocket for outpatient care | `Numeric(Double)` | `%10.0g` |
| `hc047ub` | Paid out-of-pocket for outpatient care ub | `Numeric(Byte)` | `%32.0g` |
| `hc047v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `hc047v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `hc047v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `hc049e` | Paid out-of-pocket for prescribed drugs | `Numeric(Double)` | `%10.0g` |
| `hc049ub` | Paid out-of-pocket for prescribed drugs ub | `Numeric(Byte)` | `%32.0g` |
| `hc049v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `hc049v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `hc049v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `hc051e` | Paid out-of-pocket for nursing home, day-care and home-care | `Numeric(Double)` | `%10.0g` |
| `hc051ub` | Paid out-of-pocket for nursing home, day-care and home-care ub | `Numeric(Byte)` | `%32.0g` |
| `hc051v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `hc051v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `hc051v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `hc063_` | Who answered the questions in hc | `Numeric(Byte)` | `%20.0g` |
| `hc064_` | In other institutions last 12 months | `Numeric(Byte)` | `%10.0g` |
| `hc065_` | Times being patient in other institutions | `Numeric(Byte)` | `%10.0g` |
| `hc066_` | Total nights stayed in other institutions | `Numeric(Int)` | `%10.0g` |
| `hc068_1` | Current health insurance coverage: visits to a general practitioner | `Numeric(Byte)` | `%88.0g` |
| `hc068_2` | Current health insurance coverage: visits to specialists, prescribed | `Numeric(Byte)` | `%88.0g` |
| `hc068_3` | Current health insurance coverage: visits to specialists, not prescribed | `Numeric(Byte)` | `%88.0g` |
| `hc068_4` | Current health insurance coverage: visits to any doctor | `Numeric(Byte)` | `%88.0g` |
| `hc068_5` | Current health insurance coverage: dental care | `Numeric(Byte)` | `%88.0g` |
| `hc068_6` | Current health insurance coverage: prescribed drugs | `Numeric(Byte)` | `%88.0g` |
| `hc068_7` | Current health insurance coverage: public hospitals | `Numeric(Byte)` | `%88.0g` |
| `hc068_8` | Current health insurance coverage: private hospitals | `Numeric(Byte)` | `%88.0g` |
| `hc068_9` | Current health insurance coverage: nursing home | `Numeric(Byte)` | `%88.0g` |
| `hc068_10` | Current health insurance coverage: nursing care at home | `Numeric(Byte)` | `%88.0g` |
| `hc069_` | Changes health insurance coverage | `Numeric(Byte)` | `%45.0g` |
| `hc070d1` | Better health insurance: visits to a general practitioner | `Numeric(Byte)` | `%12.0g` |
| `hc070d2` | Better health insurance: visits to specialists, prescribed | `Numeric(Byte)` | `%12.0g` |
| `hc070d3` | Better health insurance: visits to specialists, not prescribed | `Numeric(Byte)` | `%12.0g` |
| `hc070d4` | Better health insurance: visits to any doctor | `Numeric(Byte)` | `%12.0g` |
| `hc070d5` | Better health insurance: dental care | `Numeric(Byte)` | `%12.0g` |
| `hc070d6` | Better health insurance: prescribed drugs | `Numeric(Byte)` | `%12.0g` |
| `hc070d7` | Better health insurance: public hospitals | `Numeric(Byte)` | `%12.0g` |
| `hc070d8` | Better health insurance: private hospitals | `Numeric(Byte)` | `%12.0g` |
| `hc070d9` | Better health insurance: nursing home | `Numeric(Byte)` | `%12.0g` |
| `hc070d10` | Better health insurance: nursing care at home | `Numeric(Byte)` | `%12.0g` |
| `hc071d1` | Worse health insurance: visits to a general practitioner | `Numeric(Byte)` | `%12.0g` |
| `hc071d2` | Worse health insurance: visits to specialists, prescribed | `Numeric(Byte)` | `%12.0g` |
| `hc071d3` | Worse health insurance: visits to specialists, not prescribed | `Numeric(Byte)` | `%12.0g` |
| `hc071d4` | Worse health insurance: visits to any doctor | `Numeric(Byte)` | `%12.0g` |
| `hc071d5` | Worse health insurance: dental care | `Numeric(Byte)` | `%12.0g` |
| `hc071d6` | Worse health insurance: prescribed drugs | `Numeric(Byte)` | `%12.0g` |
| `hc071d7` | Worse health insurance: public hospitals | `Numeric(Byte)` | `%12.0g` |
| `hc071d8` | Worse health insurance: private hospitals | `Numeric(Byte)` | `%12.0g` |
| `hc071d9` | Worse health insurance: nursing home | `Numeric(Byte)` | `%12.0g` |
| `hc071d10` | Worse health insurance: nursing care at home | `Numeric(Byte)` | `%12.0g` |
| `hc072_` | Reasons change health insurance coverage | `Numeric(Byte)` | `%83.0g` |

### `hh` - Household Income

- Dataset: `sharew2_rel9-0-0_hh.dta`
- Read with: `ps.read_share_module("hh", wave=2)`
- Rows: 37,132
- Variables: 21
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `hh001_` | Other contributor to household income | `Numeric(Byte)` | `%10.0g` |
| `hh002e` | Total income (other) household members last year | `Numeric(Double)` | `%10.0g` |
| `hh002ub` | Total income (other) household members last year ub | `Numeric(Byte)` | `%32.0g` |
| `hh002v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `hh002v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `hh002v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `hh010_` | Income from other sources | `Numeric(Byte)` | `%10.0g` |
| `hh011e` | Additional income received by all hh-members last year | `Numeric(Double)` | `%10.0g` |
| `hh011ub` | Additional income received by all hh-members last year ub | `Numeric(Byte)` | `%32.0g` |
| `hh011v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `hh011v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `hh011v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `hh014_` | Who answered the question in hh | `Numeric(Byte)` | `%20.0g` |
| `hh017e` | Total income received by all hh members an average month last year | `Numeric(Double)` | `%10.0g` |

### `ho` - Housing

- Dataset: `sharew2_rel9-0-0_ho.dta`
- Read with: `ps.read_share_module("ho", wave=2)`
- Rows: 37,132
- Variables: 79
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `ho001_` | Interview in house of respondent | `Numeric(Byte)` | `%10.0g` |
| `ho002_` | Owner, tenant or rent free | `Numeric(Byte)` | `%36.0g` |
| `ho003_` | Rent payment period | `Numeric(Byte)` | `%22.0g` |
| `ho005e` | Amount last rent payment | `Numeric(Double)` | `%10.0g` |
| `ho005ub` | Amount last rent payment ub | `Numeric(Byte)` | `%32.0g` |
| `ho005v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ho005v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ho005v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `ho007_` | Last rent payment included all charges and services | `Numeric(Byte)` | `%10.0g` |
| `ho008e` | Amount charges and services | `Numeric(Double)` | `%10.0g` |
| `ho008ub` | Amount charges and services ub | `Numeric(Byte)` | `%32.0g` |
| `ho008v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ho008v2` | Bracket value 2 | `Numeric(Float)` | `%8.0g` |
| `ho008v3` | Bracket value 3 | `Numeric(Float)` | `%8.0g` |
| `ho010_` | More than two months behind with rent | `Numeric(Byte)` | `%10.0g` |
| `ho011_` | How property acquired | `Numeric(Byte)` | `%55.0g` |
| `ho012_` | Year acquired property | `Numeric(Int)` | `%12.0g` |
| `ho013_` | Mortgages or loans on property | `Numeric(Byte)` | `%10.0g` |
| `ho014_` | Years left of mortgage or loan | `Numeric(Byte)` | `%10.0g` |
| `ho015e` | Amount still to pay on mortgage or loan | `Numeric(Double)` | `%10.0g` |
| `ho015ub` | Amount still to pay on mortgage or loan ub | `Numeric(Byte)` | `%32.0g` |
| `ho015v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `ho015v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ho015v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `ho017_` | Regularly repay mortgage or loans | `Numeric(Byte)` | `%10.0g` |
| `ho020e` | Amount regular repayments on mortgage or loan | `Numeric(Double)` | `%10.0g` |
| `ho020ub` | Amount regular repayments on mortgage or loan ub | `Numeric(Byte)` | `%32.0g` |
| `ho020v1` | Bracket value 1 | `Numeric(Float)` | `%8.0g` |
| `ho020v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ho020v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ho022_` | Behind with regular repay mortgage or loan | `Numeric(Byte)` | `%10.0g` |
| `ho023_` | Sublet or let parts of accommodation | `Numeric(Byte)` | `%10.0g` |
| `ho024e` | Value of property | `Numeric(Double)` | `%10.0g` |
| `ho024ub` | Value of property ub | `Numeric(Byte)` | `%32.0g` |
| `ho024v1` | Bracket value 1 | `Numeric(Double)` | `%12.0g` |
| `ho024v2` | Bracket value 2 | `Numeric(Double)` | `%12.0g` |
| `ho024v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `ho026_` | Own other real estate | `Numeric(Byte)` | `%10.0g` |
| `ho027e` | Value of other real estate | `Numeric(Double)` | `%10.0g` |
| `ho027ub` | Value of other real estate ub | `Numeric(Byte)` | `%32.0g` |
| `ho027v1` | Bracket value 1 | `Numeric(Double)` | `%12.0g` |
| `ho027v2` | Bracket value 2 | `Numeric(Double)` | `%12.0g` |
| `ho027v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `ho029_` | Received income or rent of other real estate | `Numeric(Byte)` | `%10.0g` |
| `ho030e` | Amount income or rent of other real estate last year | `Numeric(Double)` | `%10.0g` |
| `ho030ub` | Amount income or rent of other real estate last year ub | `Numeric(Byte)` | `%32.0g` |
| `ho030v1` | Bracket value 1 | `Numeric(Double)` | `%8.0g` |
| `ho030v2` | Bracket value 2 | `Numeric(Double)` | `%8.0g` |
| `ho030v3` | Bracket value 3 | `Numeric(Double)` | `%8.0g` |
| `ho032_` | Number of rooms in accommodation | `Numeric(Byte)` | `%10.0g` |
| `ho033_` | Special features in accommodation | `Numeric(Byte)` | `%10.0g` |
| `ho034_` | Years in accommodation | `Numeric(Int)` | `%10.0g` |
| `ho035_` | Years in community | `Numeric(Byte)` | `%10.0g` |
| `ho036_` | Type of building | `Numeric(Byte)` | `%61.0g` |
| `ho037_` | Area where respondent lives | `Numeric(Byte)` | `%38.0g` |
| `ho038_` | Spend regulary time in other residence | `Numeric(Byte)` | `%10.0g` |
| `ho039_` | Location of other residence | `Numeric(Byte)` | `%30.0g` |
| `ho041_` | Who answered the questions in ho | `Numeric(Byte)` | `%20.0g` |
| `ho042_` | Number of floors of building | `Numeric(Byte)` | `%10.0g` |
| `ho043_` | Number of steps to entrance | `Numeric(Byte)` | `%12.0g` |
| `ho044_` | Changed place of residence | `Numeric(Byte)` | `%10.0g` |
| `ho045_` | Main reason move | `Numeric(Byte)` | `%62.0g` |
| `ho050_` | Indoor bath or shower | `Numeric(Byte)` | `%10.0g` |
| `ho051_` | Indoor flushing toilet | `Numeric(Byte)` | `%10.0g` |
| `ho052_` | Central heating | `Numeric(Byte)` | `%10.0g` |
| `ho053_` | Air condition | `Numeric(Byte)` | `%10.0g` |
| `ho054_` | Elevator | `Numeric(Byte)` | `%10.0g` |
| `ho055_` | Balcony, terrace or garden | `Numeric(Byte)` | `%10.0g` |
| `ho056_` | Area facilities | `Numeric(Byte)` | `%10.0g` |
| `ho057_` | Area public transportation | `Numeric(Byte)` | `%10.0g` |
| `ho058_` | Area pollution, noise or other problems | `Numeric(Byte)` | `%10.0g` |
| `ho059_` | Area vandalism or crime | `Numeric(Byte)` | `%10.0g` |

### `iv` - Interviewer Observations

- Dataset: `sharew2_rel9-0-0_iv.dta`
- Read with: `ps.read_share_module("iv", wave=2)`
- Rows: 37,132
- Variables: 27
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
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
| `iv011_` | Number of floors of building | `Numeric(Byte)` | `%10.0g` |
| `iv012_` | Number of steps to entrance | `Numeric(Byte)` | `%12.0g` |
| `iv018_` | Help needed reading showcards | `Numeric(Byte)` | `%30.0g` |
| `iv020_` | Relationship proxy | `Numeric(Byte)` | `%37.0g` |

### `mh` - Mental Health

- Dataset: `sharew2_rel9-0-0_mh.dta`
- Read with: `ps.read_share_module("mh", wave=2)`
- Rows: 37,132
- Variables: 27
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `mh002_` | Sad or depressed last month | `Numeric(Byte)` | `%10.0g` |
| `mh003_` | Hopes for the future | `Numeric(Byte)` | `%19.0g` |
| `mh004_` | Suicidal feelings or wish to be dead | `Numeric(Byte)` | `%61.0g` |
| `mh005_` | Feels guilty | `Numeric(Byte)` | `%64.0g` |
| `mh006_` | Blame for what | `Numeric(Byte)` | `%62.0g` |
| `mh007_` | Trouble sleeping | `Numeric(Byte)` | `%62.0g` |
| `mh008_` | Less or same interest in things | `Numeric(Byte)` | `%44.0g` |
| `mh009_` | Keeps up interest | `Numeric(Byte)` | `%10.0g` |
| `mh010_` | Irritability | `Numeric(Byte)` | `%10.0g` |
| `mh011_` | Appetite | `Numeric(Byte)` | `%35.0g` |
| `mh012_` | Eating more or less | `Numeric(Byte)` | `%21.0g` |
| `mh013_` | Fatigue | `Numeric(Byte)` | `%10.0g` |
| `mh014_` | Concentration on entertainment | `Numeric(Byte)` | `%60.0g` |
| `mh015_` | Concentration on reading | `Numeric(Byte)` | `%48.0g` |
| `mh016_` | Enjoyment | `Numeric(Byte)` | `%62.0g` |
| `mh017_` | Tearfulness | `Numeric(Byte)` | `%10.0g` |
| `mh018_` | Depression ever | `Numeric(Byte)` | `%10.0g` |
| `mh019_` | Age depression symptoms first time | `Numeric(Byte)` | `%10.0g` |
| `mh020_` | Ever treated for depression by doctor or psychiatrist | `Numeric(Byte)` | `%10.0g` |
| `mh021_` | Ever admitted to mental hospital or psychiatric ward | `Numeric(Byte)` | `%10.0g` |
| `mh022_` | Ever told affective or emotional disorders | `Numeric(Byte)` | `%10.0g` |

### `pf` - Peak Flow

- Dataset: `sharew2_rel9-0-0_pf.dta`
- Read with: `ps.read_share_module("pf", wave=2)`
- Rows: 37,132
- Variables: 17
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `pf002_` | Feels safe to do the test | `Numeric(Byte)` | `%10.0g` |
| `pf003_` | Value first measurement | `Numeric(Int)` | `%10.0g` |
| `pf004_` | Value second measurement | `Numeric(Int)` | `%10.0g` |
| `pf005_` | Effort R gave to this measurement | `Numeric(Byte)` | `%60.0g` |
| `pf006_` | Position of R for this test | `Numeric(Byte)` | `%10.0g` |
| `pf007d1` | Why pf not completed: R felt it would not be safe | `Numeric(Byte)` | `%12.0g` |
| `pf007d2` | Why pf not completed: IWER felt it would not be safe | `Numeric(Byte)` | `%12.0g` |
| `pf007d3` | Why pf not completed: R refused or was not willing to complete | `Numeric(Byte)` | `%12.0g` |
| `pf007d4` | Why pf not completed: R tried but was unable to complete | `Numeric(Byte)` | `%12.0g` |
| `pf007d5` | Why pf not completed: R did not understand the instructions | `Numeric(Byte)` | `%12.0g` |
| `pf007dot` | Why pf not completed: Other | `Numeric(Byte)` | `%12.0g` |

### `ph` - Physical Health

- Dataset: `sharew2_rel9-0-0_ph.dta`
- Read with: `ps.read_share_module("ph", wave=2)`
- Rows: 37,132
- Variables: 168
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
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
| `ph009_1` | Age heart attack or other heart problems | `Numeric(Byte)` | `%10.0g` |
| `ph009_2` | Age high blood pressure | `Numeric(Byte)` | `%10.0g` |
| `ph009_3` | Age high blood cholesterol | `Numeric(Byte)` | `%10.0g` |
| `ph009_4` | Age stroke or cerebral vascular disease | `Numeric(Byte)` | `%10.0g` |
| `ph009_5` | Age diabetes | `Numeric(Byte)` | `%10.0g` |
| `ph009_6` | Age chronic lung disease | `Numeric(Byte)` | `%10.0g` |
| `ph009_7` | Age asthma | `Numeric(Byte)` | `%10.0g` |
| `ph009_8` | Age arthritis or rheumatism | `Numeric(Byte)` | `%10.0g` |
| `ph009_9` | Age osteoporosis | `Numeric(Byte)` | `%10.0g` |
| `ph009_10` | Age cancer or malignant tumour | `Numeric(Byte)` | `%10.0g` |
| `ph009_11` | Age stomach, duodenal or peptic ulcer | `Numeric(Byte)` | `%10.0g` |
| `ph009_12` | Age parkinson disease | `Numeric(Byte)` | `%10.0g` |
| `ph009_13` | Age cataracts | `Numeric(Byte)` | `%10.0g` |
| `ph009_14` | Age hip or femoral fracture | `Numeric(Byte)` | `%10.0g` |
| `ph009_15` | Age other fractures | `Numeric(Byte)` | `%10.0g` |
| `ph009_16` | Age alzheimer's disease | `Numeric(Byte)` | `%10.0g` |
| `ph009_17` | Age benign tumor | `Numeric(Byte)` | `%10.0g` |
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
| `ph012_` | Weight of respondent | `Numeric(Double)` | `%10.0g` |
| `ph013_` | How tall are you? | `Numeric(Double)` | `%10.0g` |
| `ph024_` | Use dentures | `Numeric(Byte)` | `%10.0g` |
| `ph025_` | Bite on hard foods | `Numeric(Byte)` | `%10.0g` |
| `ph041_` | Wears glasses/contact lenses | `Numeric(Byte)` | `%10.0g` |
| `ph043_` | Eyesight distance | `Numeric(Byte)` | `%39.0g` |
| `ph044_` | Eyesight reading | `Numeric(Byte)` | `%39.0g` |
| `ph045_` | Use hearing aid | `Numeric(Byte)` | `%10.0g` |
| `ph046_` | Hearing | `Numeric(Byte)` | `%13.0g` |
| `ph047_` | Hearing with background noise | `Numeric(Byte)` | `%10.0g` |
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
| `ph050_` | Help activities | `Numeric(Byte)` | `%10.0g` |
| `ph051_` | Help meets needs | `Numeric(Byte)` | `%12.0g` |
| `ph054_` | Who answered the questions in ph | `Numeric(Byte)` | `%20.0g` |
| `ph056_` | Hearing with one person | `Numeric(Byte)` | `%10.0g` |
| `ph059d1` | Use of aids: a cane or walking stick | `Numeric(Byte)` | `%12.0g` |
| `ph059d2` | Use of aids: a zimmer frame or walker | `Numeric(Byte)` | `%12.0g` |
| `ph059d3` | Use of aids: a manual wheelchair | `Numeric(Byte)` | `%12.0g` |
| `ph059d4` | Use of aids: an electric wheelchair | `Numeric(Byte)` | `%12.0g` |
| `ph059d5` | Use of aids: a buggy or scooter | `Numeric(Byte)` | `%12.0g` |
| `ph059d6` | Use of aids: special eating utensils | `Numeric(Byte)` | `%12.0g` |
| `ph059d7` | Use of aids: a personal alarm | `Numeric(Byte)` | `%12.0g` |
| `ph059dno` | Use of aids: none of these | `Numeric(Byte)` | `%12.0g` |
| `ph060_` | Health in general question 3 | `Numeric(Byte)` | `%10.0g` |
| `ph061_` | Health problem that limits paid work | `Numeric(Byte)` | `%10.0g` |
| `ph062_` | Compare health last wave | `Numeric(Byte)` | `%20.0g` |
| `ph063_` | Health better last wave | `Numeric(Byte)` | `%15.0g` |
| `ph064_` | Health worse last wave | `Numeric(Byte)` | `%14.0g` |
| `ph065_` | Check: lost weight | `Numeric(Byte)` | `%54.0g` |
| `ph066_` | Reason lost weight | `Numeric(Byte)` | `%58.0g` |
| `ph067_1` | Had a heart attack since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph067_2` | Had a stroke/been diagnosed with cerebral vascular disease since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph067_3` | Been diagnosed with cancer since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph067_4` | Suffered a hip fracture since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph068_1` | Had a heart attack before last interview | `Numeric(Byte)` | `%10.0g` |
| `ph068_2` | Had a stroke/been diagnosed with cerebral vascular disease before last interview | `Numeric(Byte)` | `%10.0g` |
| `ph068_3` | Been diagnosed with cancer before last interview | `Numeric(Byte)` | `%10.0g` |
| `ph068_4` | Suffered a hip fracture before last interview | `Numeric(Byte)` | `%10.0g` |
| `ph069_1` | Had ANOTHER heart attack since last interview | `Numeric(Byte)` | `%51.0g` |
| `ph069_2` | Had ANOTHER stroke/been diagnosed with cerebral vascular disease AGAIN since las | `Numeric(Byte)` | `%51.0g` |
| `ph069_3` | Been diagnosed with cancer AGAIN since last interview | `Numeric(Byte)` | `%51.0g` |
| `ph069_4` | Suffered a hip fracture AGAIN since last interview | `Numeric(Byte)` | `%51.0g` |
| `ph071_1` | How many heart attacks since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph071_2` | How many strokes/diagnosed cerebral vascular disease since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph071_3` | How often diagnosed with cancer since last interview | `Numeric(Byte)` | `%10.0g` |
| `ph071_4` | How often suffered a hip fracture since last interview | `Numeric(Byte)` | `%10.0g` |

### `sp` - Social Support

- Dataset: `sharew2_rel9-0-0_sp.dta`
- Read with: `ps.read_share_module("sp", wave=2)`
- Rows: 37,132
- Variables: 168
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sp002_` | Received help from others (outside hh) | `Numeric(Byte)` | `%10.0g` |
| `sp003_1` | Who gave help: person 1 | `Numeric(Byte)` | `%18.0g` |
| `sp003_2` | Who gave help: person 2 | `Numeric(Byte)` | `%18.0g` |
| `sp003_3` | Who gave help: person 3 | `Numeric(Byte)` | `%18.0g` |
| `sp004d1_1` | Help provided from person 1: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp004d1_2` | Help provided from person 2: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp004d1_3` | Help provided from person 3: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp004d2_1` | Help provided from person 1: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp004d2_2` | Help provided from person 2: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp004d2_3` | Help provided from person 3: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp004d3_1` | Help provided from person 1: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp004d3_2` | Help provided from person 2: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp004d3_3` | Help provided from person 3: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp005_1` | How often received help: from person 1 | `Numeric(Byte)` | `%18.0g` |
| `sp005_2` | How often received help: from person 2 | `Numeric(Byte)` | `%18.0g` |
| `sp005_3` | How often received help: from person 3 | `Numeric(Byte)` | `%18.0g` |
| `sp006_1` | Hours received houshold help: person 1 | `Numeric(Int)` | `%12.0g` |
| `sp006_2` | Hours received houshold help: person 2 | `Numeric(Int)` | `%12.0g` |
| `sp006_3` | Hours received houshold help: person 3 | `Numeric(Int)` | `%10.0g` |
| `sp007_1` | Any other helper from outside the household | `Numeric(Byte)` | `%10.0g` |
| `sp007_2` | Any other helper from outside the household | `Numeric(Byte)` | `%10.0g` |
| `sp008_` | Given help last twelve months | `Numeric(Byte)` | `%10.0g` |
| `sp009_1` | To whom did you give help: person 1 | `Numeric(Byte)` | `%18.0g` |
| `sp009_2` | To whom did you give help: person 2 | `Numeric(Byte)` | `%18.0g` |
| `sp009_3` | To whom did you give help: person 3 | `Numeric(Byte)` | `%18.0g` |
| `sp010d1_1` | Help given person 1: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp010d1_2` | Help given person 2: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp010d1_3` | Help given person 3: personal care | `Numeric(Byte)` | `%12.0g` |
| `sp010d2_1` | Help given person 1: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp010d2_2` | Help given person 2: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp010d2_3` | Help given person 3: practical household help | `Numeric(Byte)` | `%12.0g` |
| `sp010d3_1` | Help given person 1: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp010d3_2` | Help given person 2: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp010d3_3` | Help given person 3: help with paperwork | `Numeric(Byte)` | `%12.0g` |
| `sp011_1` | How often given help to person 1 | `Numeric(Byte)` | `%18.0g` |
| `sp011_2` | How often given help to person 2 | `Numeric(Byte)` | `%18.0g` |
| `sp011_3` | How often given help to person 3 | `Numeric(Byte)` | `%18.0g` |
| `sp012_1` | Hours given help to person 1 | `Numeric(Int)` | `%12.0g` |
| `sp012_2` | Hours given help to person 2 | `Numeric(Int)` | `%12.0g` |
| `sp012_3` | Hours given help to person 3 | `Numeric(Int)` | `%10.0g` |
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
| `sp017_1` | Hours looked after child(ren) of child 1 | `Numeric(Int)` | `%12.0g` |
| `sp017_2` | Hours looked after child(ren) of child 2 | `Numeric(Int)` | `%12.0g` |
| `sp017_3` | Hours looked after child(ren) of child 3 | `Numeric(Int)` | `%10.0g` |
| `sp017_4` | Hours looked after child(ren) of child 4 | `Numeric(Int)` | `%10.0g` |
| `sp017_5` | Hours looked after child(ren) of child 5 | `Numeric(Int)` | `%10.0g` |
| `sp017_6` | Hours looked after child(ren) of child 6 | `Numeric(Int)` | `%10.0g` |
| `sp017_7` | Hours looked after child(ren) of child 7 | `Numeric(Byte)` | `%10.0g` |
| `sp017_8` | Hours looked after child(ren) of child 8 | `Numeric(Int)` | `%10.0g` |
| `sp017_9` | Hours looked after child(ren) of child 9 | `Numeric(Byte)` | `%10.0g` |
| `sp017_10` | Hours looked after child(ren) of child 10 | `Numeric(Byte)` | `%10.0g` |
| `sp017_11` | Hours looked after child(ren) of child 11 | `Numeric(Byte)` | `%10.0g` |
| `sp017_12` | Hours looked after child(ren) of child 12 | `Numeric(Int)` | `%10.0g` |
| `sp017_13` | Hours looked after child(ren) of child 13 | `Numeric(Byte)` | `%10.0g` |
| `sp017_14` | Hours looked after child(ren) of child 14 | `Numeric(Byte)` | `%10.0g` |
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
| `sp022_` | Who answered the questions in sp | `Numeric(Byte)` | `%20.0g` |

### `ws` - Walking Speed

- Dataset: `sharew2_rel9-0-0_ws.dta`
- Read with: `ps.read_share_module("ws", wave=2)`
- Rows: 37,132
- Variables: 19
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `ws001_` | Record respondent status | `Numeric(Byte)` | `%60.0g` |
| `ws002_` | Able to walk alone (using aid) | `Numeric(Byte)` | `%34.0g` |
| `ws003_` | Is it safe to carry out the test | `Numeric(Byte)` | `%39.0g` |
| `ws004_` | Respondent willing to do walking test | `Numeric(Byte)` | `%10.0g` |
| `ws005_` | Does respondent feel safe to continue | `Numeric(Byte)` | `%10.0g` |
| `ws007_` | Check available space for test | `Numeric(Byte)` | `%24.0g` |
| `ws010_` | Result of first trial | `Numeric(Byte)` | `%58.0g` |
| `ws011_` | Time of first walking speed test | `Numeric(Double)` | `%10.0g` |
| `ws012_` | Result of second trial | `Numeric(Byte)` | `%58.0g` |
| `ws013_` | Time of second walking speed test | `Numeric(Double)` | `%10.0g` |
| `ws014_` | Did the respondent have comment on pain | `Numeric(Byte)` | `%10.0g` |
| `ws015_` | Record type of floor surface | `Numeric(Byte)` | `%29.0g` |
| `ws017_` | Type of aid used during test | `Numeric(Byte)` | `%21.0g` |

### `xt` - End-of-Life Interview

- Dataset: `sharew2_rel9-0-0_xt.dta`
- Read with: `ps.read_share_module("xt", wave=2)`
- Rows: 726
- Variables: 108
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language_xt` | Language: End of life interview | `Numeric(Byte)` | `%44.0g` |
| `gender_xt` | Gender of the deceased | `Numeric(Byte)` | `%10.0g` |
| `yrbirth_xt` | Year of birth of the deceased | `Numeric(Int)` | `%10.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `xt002_` | Relationship to the deceased | `Numeric(Byte)` | `%61.0g` |
| `xt005_` | How often contact last twelve month | `Numeric(Byte)` | `%27.0g` |
| `xt006_` | Proxy respondent's sex | `Numeric(Byte)` | `%10.0g` |
| `xt007_` | Year of birth proxy | `Numeric(Int)` | `%10.0g` |
| `xt008_` | Month of decease | `Numeric(Byte)` | `%10.0g` |
| `xt009_` | Year of decease | `Numeric(Int)` | `%10.0g` |
| `xt010_` | Age at the moment of decease | `Numeric(Int)` | `%10.0g` |
| `xt011_` | Main cause of death | `Numeric(Byte)` | `%62.0g` |
| `xt012c` | Main cause of death: xt012 coded | `Numeric(Byte)` | `%60.0g` |
| `xt013_` | How long been ill before decease | `Numeric(Byte)` | `%51.0g` |
| `xt014_` | Place of dying | `Numeric(Byte)` | `%43.0g` |
| `xt015_` | Times in hospital last year before dying | `Numeric(Byte)` | `%18.0g` |
| `xt016_` | Total time in hospital last year before dying | `Numeric(Byte)` | `%53.0g` |
| `xt018_1` | Type of medical care in last 12 months: care from a general practitioner | `Numeric(Byte)` | `%10.0g` |
| `xt018_2` | Type of medical care in last 12 months: care from specialist physicians | `Numeric(Byte)` | `%10.0g` |
| `xt018_3` | Type of medical care in last 12 months: hospital stays | `Numeric(Byte)` | `%10.0g` |
| `xt018_4` | Type of medical care in last 12 months: care in a nursing home | `Numeric(Byte)` | `%10.0g` |
| `xt018_5` | Type of medical care in last 12 months: hospice stays | `Numeric(Byte)` | `%10.0g` |
| `xt018_6` | Type of medical care in last 12 months: medication | `Numeric(Byte)` | `%10.0g` |
| `xt018_7` | Type of medical care in last 12 months: aids and appliances | `Numeric(Byte)` | `%10.0g` |
| `xt018_8` | Type of medical care in last 12 months: home care or help due to disability | `Numeric(Byte)` | `%10.0g` |
| `xt019e_1` | Costs: care from a general practitioner | `Numeric(Double)` | `%12.0g` |
| `xt019e_2` | Costs: care from specialist physicians | `Numeric(Double)` | `%12.0g` |
| `xt019e_3` | Costs: hospital stays | `Numeric(Double)` | `%12.0g` |
| `xt019e_4` | Costs: care in a nursing home | `Numeric(Double)` | `%10.0g` |
| `xt019e_5` | Costs: hospice stays | `Numeric(Double)` | `%10.0g` |
| `xt019e_6` | Costs: medication | `Numeric(Double)` | `%12.0g` |
| `xt019e_7` | Costs: aids and appliances | `Numeric(Double)` | `%12.0g` |
| `xt019e_8` | Costs: home care or help due to disability | `Numeric(Double)` | `%12.0g` |
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
| `xt024_` | Time the deceased received help | `Numeric(Byte)` | `%49.0g` |
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
| `xt030_` | The deceased owned home | `Numeric(Byte)` | `%10.0g` |
| `xt031e` | Value of home after mortgages | `Numeric(Double)` | `%12.0g` |
| `xt032d1` | Who inherited the home of the deceased: yourself (proxy) | `Numeric(Byte)` | `%12.0g` |
| `xt032d2` | Who inherited the home of the deceased: spouse/partner of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt032d3` | Who inherited the home of the deceased: sons/daughters | `Numeric(Byte)` | `%12.0g` |
| `xt032d4` | Who inherited the home of the deceased: grandchildren of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt032d5` | Who inherited the home of the deceased: siblings of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt032d6` | Who inherited the home of the deceased: other relatives | `Numeric(Byte)` | `%12.0g` |
| `xt032d7` | Who inherited the home of the deceased: other non-relatives | `Numeric(Byte)` | `%12.0g` |
| `xt033_` | Deceased owned any life insurance policies | `Numeric(Byte)` | `%10.0g` |
| `xt034e` | Value of all life insurance policies | `Numeric(Double)` | `%10.0g` |
| `xt035d1` | Beneficiaries of the life insurance policies: yourself (proxy) | `Numeric(Byte)` | `%12.0g` |
| `xt035d2` | Beneficiaries of the life insurance policies: spouse/partner of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt035d3` | Beneficiaries of the life insurance policies: sons/daughters | `Numeric(Byte)` | `%12.0g` |
| `xt035d4` | Beneficiaries of the life insurance policies: grandchildren of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt035d5` | Beneficiaries of the life insurance policies: siblings of the deceased | `Numeric(Byte)` | `%12.0g` |
| `xt035d6` | Beneficiaries of the life insurance policies: other relatives | `Numeric(Byte)` | `%12.0g` |
| `xt035d7` | Beneficiaries of the life insurance policies: other non-relatives | `Numeric(Byte)` | `%12.0g` |
| `xt037_1` | Deceased owned assets: business, including land or permises | `Numeric(Byte)` | `%10.0g` |
| `xt037_2` | Deceased owned assets: other real estate | `Numeric(Byte)` | `%10.0g` |
| `xt037_3` | Deceased owned assets: cars | `Numeric(Byte)` | `%10.0g` |
| `xt037_4` | Deceased owned assets: financial assets, e.g. cash/bonds/stocks | `Numeric(Byte)` | `%10.0g` |
| `xt037_5` | Deceased owned assets: jewelry or antiquities | `Numeric(Byte)` | `%10.0g` |
| `xt038e_1` | Value of assets: business, including land or permises | `Numeric(Double)` | `%12.0g` |
| `xt038e_2` | Value of assets: other real estate | `Numeric(Double)` | `%12.0g` |
| `xt038e_3` | Value of assets: cars | `Numeric(Double)` | `%10.0g` |
| `xt038e_4` | Value of assets: financial assets, e.g. cash, bonds or stocks | `Numeric(Double)` | `%12.0g` |
| `xt038e_5` | Value of assets: jewelry or antiquities | `Numeric(Double)` | `%12.0g` |
| `xt039_` | Number of children (still alive) deceased had at the end | `Numeric(Byte)` | `%10.0g` |
| `xt040_` | Total estate divided among the children | `Numeric(Byte)` | `%117.0g` |
| `xt041_` | Funeral was accompanied by a religious ceremony | `Numeric(Byte)` | `%10.0g` |
| `xt043_` | Interview mode | `Numeric(Byte)` | `%23.0g` |


## Special Modules

### `dropoff` - Paper-and-pencil drop-off

- Dataset: `sharew2_rel9-0-0_dropoff.dta`
- Read with: `ps.read_share_module("dropoff", wave=2)`
- Rows: 8,862
- Variables: 154
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `q3_a` | I pursue my goals with lots of energy (q1) | `Numeric(Byte)` | `%41.0g` |
| `q3_b` | In uncertain times, I usually expect the best (q1) | `Numeric(Byte)` | `%41.0g` |
| `q3_c` | I'm always optimistic about my future (q1) | `Numeric(Byte)` | `%41.0g` |
| `q3_d` | I hardly ever expect things to go my way (q1) | `Numeric(Byte)` | `%41.0g` |
| `q3_e` | I still find ways to solve a problem if others have given up (q1) | `Numeric(Byte)` | `%41.0g` |
| `q3_f` | I rarely count on good things happening to me (q1) | `Numeric(Byte)` | `%41.0g` |
| `q3_g` | Given my previous experiences I feel well prepared for my future (q1) | `Numeric(Byte)` | `%41.0g` |
| `q6_a` | Parents duty: do the best for children even at own expense (q2) | `Numeric(Byte)` | `%41.0g` |
| `q6_b` | Grandparents duty: be there for grandchildren (q2) | `Numeric(Byte)` | `%41.0g` |
| `q6_c` | Grandparents duty: help grandchildren financially (q2) | `Numeric(Byte)` | `%41.0g` |
| `q6_d` | Grandparents duty: help looking after young grandchildren (q2) | `Numeric(Byte)` | `%41.0g` |
| `q7_a` | Financial support for older persons who are in need (q3) | `Numeric(Byte)` | `%14.0g` |
| `q7_b` | Help w. household chores for older persons in need (q3) | `Numeric(Byte)` | `%14.0g` |
| `q7_c` | Personal care for older persons in need (q3) | `Numeric(Byte)` | `%14.0g` |
| `q8_a` | Experiences conflict with: parents (q4) | `Numeric(Byte)` | `%29.0g` |
| `q8_b` | Experiences conflict with: parents-in-law (q4) | `Numeric(Byte)` | `%29.0g` |
| `q8_c` | Experiences conflict with: partner/spouse (q4) | `Numeric(Byte)` | `%29.0g` |
| `q8_d` | Experiences conflict with: children (q4) | `Numeric(Byte)` | `%29.0g` |
| `q8_e` | Experiences conflict with: other family members (q4) | `Numeric(Byte)` | `%29.0g` |
| `q8_f` | Experiences conflict with: friends/coworkers/acquaintances (q4) | `Numeric(Byte)` | `%29.0g` |
| `q9` | Conflicts with children(-in-law) over education of grandchild(ren) (q5) | `Numeric(Byte)` | `%29.0g` |
| `q10` | Ever shared a household with spouse/partner (q6) | `Numeric(Byte)` | `%29.0g` |
| `q11_a` | Main responsibility for: bringing up children (q7) | `Numeric(Byte)` | `%40.0g` |
| `q11_b` | Main responsibility for: earning money (q7) | `Numeric(Byte)` | `%40.0g` |
| `q11_c` | Main responsibility for: household chores (q7) | `Numeric(Byte)` | `%40.0g` |
| `q11_d` | Main responsibility for: caring for elderly (q7) | `Numeric(Byte)` | `%40.0g` |
| `q13_a` | How often does general practitioner: ask about physical activity (q8) | `Numeric(Byte)` | `%14.0g` |
| `q13_b` | How often does general practitioner: tell you to get exercise (q8) | `Numeric(Byte)` | `%14.0g` |
| `q13_c` | How often does general practitioner: ask about falling down (q8) | `Numeric(Byte)` | `%14.0g` |
| `q13_d` | How often does general practitioner: check your balance (q8) | `Numeric(Byte)` | `%14.0g` |
| `q13_f` | How often does general practitioner: ask about any drugs (q8) | `Numeric(Byte)` | `%14.0g` |
| `q16` | Had any eye exam the last two years (q12) | `Numeric(Byte)` | `%29.0g` |
| `q17` | Had a mammogram the last two years (only women) (q13) | `Numeric(Byte)` | `%29.0g` |
| `q33_a` | Pet(s) in hh: dog (q14) | `Numeric(Byte)` | `%29.0g` |
| `q33_b` | Pet(s) in hh: cat (q14) | `Numeric(Byte)` | `%29.0g` |
| `q33_c` | Pet(s) in hh: bird (q14) | `Numeric(Byte)` | `%29.0g` |
| `q33_d` | Pet(s) in hh: fish (q14) | `Numeric(Byte)` | `%29.0g` |
| `q33_e` | Pet(s) in hh: other (q14) | `Numeric(Byte)` | `%29.0g` |
| `q39_a` | Talk with doctor/nurse about: physical health problems (q9) | `Numeric(Byte)` | `%20.0g` |
| `q39_b` | Talk with doctor/nurse about: emotional problems (q9) | `Numeric(Byte)` | `%20.0g` |
| `q39_c` | Talk with doctor/nurse about: sensitive health problems (q9) | `Numeric(Byte)` | `%20.0g` |
| `q39_d` | Talk with doctor/nurse about: social problems (q9) | `Numeric(Byte)` | `%20.0g` |
| `q40_a` | Does doctor/nurse: explain results (q10) | `Numeric(Byte)` | `%12.0g` |
| `q40_b` | Does doctor/nurse: explain treatment options (q10) | `Numeric(Byte)` | `%12.0g` |
| `q40_c` | Does doctor/nurse: listen to opinion (q10) | `Numeric(Byte)` | `%12.0g` |
| `q41_a` | Had a flu vaccination the last year (q11) | `Numeric(Byte)` | `%29.0g` |
| `q41_b` | A doctor/ nurse checked blood pressure (q11) | `Numeric(Byte)` | `%29.0g` |
| `q41_c` | A doctor/ nurse checked cholesterol (q11) | `Numeric(Byte)` | `%29.0g` |
| `q41_d` | A doctor/ nurse checked blood sugar (q11) | `Numeric(Byte)` | `%29.0g` |
| `ilq6` | Experienced the death of a (grand)child | `Numeric(Byte)` | `%15.0g` |
| `ilq7` | How old when experienced death of a (grand)child | `Numeric(Byte)` | `%40.0g` |
| `ilq8` | Effect on life: death of (grand)child | `Numeric(Byte)` | `%15.0g` |
| `ilq9` | Provided long term care to disabled/impaired relative | `Numeric(Byte)` | `%15.0g` |
| `ilq10` | How old when first provided long term care to disabled/impaired relative | `Numeric(Byte)` | `%40.0g` |
| `ilq11` | Effect on life: providing long term care | `Numeric(Byte)` | `%15.0g` |
| `ilq12` | Needed long term care due to difficulty in caring for yourself | `Numeric(Byte)` | `%15.0g` |
| `ilq13` | How old when first needed long term care | `Numeric(Byte)` | `%40.0g` |
| `ilq14` | Effect on life: needing long term care | `Numeric(Byte)` | `%15.0g` |
| `ilq15` | Experienced sexual assault (rape or harassment) | `Numeric(Byte)` | `%15.0g` |
| `ilq16` | How old when first experienced sexual assult | `Numeric(Byte)` | `%40.0g` |
| `ilq17` | Effect on life: experience of sexual assault | `Numeric(Byte)` | `%15.0g` |
| `ilq18` | Been victim of violence/abuse | `Numeric(Byte)` | `%15.0g` |
| `ilq19` | How old when first been victim of violence/abuese | `Numeric(Byte)` | `%40.0g` |
| `ilq20` | Effect on life: been victim of violence/abuese | `Numeric(Byte)` | `%15.0g` |
| `ilq21` | Been victim of crime (theft or fraud) | `Numeric(Byte)` | `%15.0g` |
| `ilq22` | How old when first been victim of crime | `Numeric(Byte)` | `%40.0g` |
| `ilq23` | Effect on life: been victim of crime | `Numeric(Byte)` | `%15.0g` |
| `ilq24` | Witnessed accident/violent act in which someone was killed/seriously injured | `Numeric(Byte)` | `%15.0g` |
| `ilq25` | How old when first witnessed accident/violent act | `Numeric(Byte)` | `%40.0g` |
| `ilq26` | Effect on life: witnessing accident/violent act | `Numeric(Byte)` | `%15.0g` |
| `ilq27` | Experienced extremely severe economic deprivation | `Numeric(Byte)` | `%15.0g` |
| `ilq28` | How old when first experienced extremely severe economic deprivation | `Numeric(Byte)` | `%40.0g` |
| `ilq29` | Effect on life: experience of extremely severe economic deprivation | `Numeric(Byte)` | `%15.0g` |
| `ilq37` | During wwII, ever resided in country under nazi/pro-nazi regime | `Numeric(Byte)` | `%29.0g` |
| `ilq38` | Year 1939: resided in country that was under nazi/pro-nazi regime | `Numeric(Byte)` | `%29.0g` |
| `ilq39` | Year 1940: resided in country that was under nazi/pro-nazi regime | `Numeric(Byte)` | `%29.0g` |
| `ilq40` | Year 1941: resided in country that was under nazi/pro-nazi regime | `Numeric(Byte)` | `%29.0g` |
| `ilq41` | Year 1942: resided in country that was under nazi/pro-nazi regime | `Numeric(Byte)` | `%29.0g` |
| `ilq42` | Year 1943: resided in country that was under nazi/pro-nazi regime | `Numeric(Byte)` | `%29.0g` |
| `ilq43` | Year 1944: resided in country that was under nazi/pro-nazi regime | `Numeric(Byte)` | `%29.0g` |
| `ilq44` | Year 1945: resided in country that was under nazi/pro-nazi regime | `Numeric(Byte)` | `%29.0g` |
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
| `ilq58` | Did your parents reside in nazi/pro-nazi regime during wwII | `Numeric(Byte)` | `%17.0g` |
| `ilq59` | Were parents killed by nazi/pro-nazi regime/died as result of it | `Numeric(Byte)` | `%17.0g` |
| `ilq60` | Agree with a delay in age of eligibility for receipt of pension benefits | `Numeric(Byte)` | `%17.0g` |
| `ilq61` | Employers will fire older workers and hire younger workers in their place | `Numeric(Byte)` | `%17.0g` |
| `ilq62` | Young people will have fewer places of work available | `Numeric(Byte)` | `%17.0g` |
| `ilq63` | Older workers will lack the stamina to work until the new retirement age | `Numeric(Byte)` | `%17.0g` |
| `ilq64` | Extending work until new retirem. age will improve health of older workers | `Numeric(Byte)` | `%17.0g` |
| `ilq65` | Extending work hours until new retirem. age will increase interest of older work | `Numeric(Byte)` | `%17.0g` |
| `ilq66` | Extending work until new retirem. age will decrease older workers leisure time | `Numeric(Byte)` | `%17.0g` |
| `ilq67` | Women: younger than 64/men: younger than 67 | `Numeric(Byte)` | `%29.0g` |
| `ilq68` | Current employment status | `Numeric(Byte)` | `%40.0g` |
| `ilq69` | Interested in working until the new retirement age | `Numeric(Byte)` | `%40.0g` |
| `ilq70` | Age planning to retire | `Numeric(Byte)` | `%40.0g` |
| `ilq72` | Will retire at different time than planned as result of new retirement age | `Numeric(Byte)` | `%40.0g` |
| `ilq73` | Aware change in retir. age may reduce occupational pension allotments | `Numeric(Byte)` | `%29.0g` |
| `ilq74` | Interested in retiring earlier even if pension will be reduced as result | `Numeric(Byte)` | `%40.0g` |
| `ilq75` | Chances to continue working until the new retirement age | `Numeric(Byte)` | `%40.0g` |
| `ilq76` | Chances your employer will continue to employ you until new retirement age | `Numeric(Byte)` | `%40.0g` |
| `ilq77` | Source of add. support: national insurance allotment (yours/other hh-member) | `Numeric(Byte)` | `%29.0g` |
| `ilq78` | Source of add. support: pension/other payments from abroad | `Numeric(Byte)` | `%29.0g` |
| `ilq79` | Source of add. support: savings | `Numeric(Byte)` | `%29.0g` |
| `ilq80` | Source of add. support: profits from property/investments | `Numeric(Byte)` | `%29.0g` |
| `ilq81` | Source of add. support: income from working members of hh | `Numeric(Byte)` | `%29.0g` |
| `ilq82` | Source of add. support: spouse's occupational pension | `Numeric(Byte)` | `%29.0g` |
| `ilq83` | Source of add. support: loans | `Numeric(Byte)` | `%29.0g` |
| `ilq84` | Source of add. support: other sources | `Numeric(Byte)` | `%29.0g` |
| `ilq87` | Been wounded in war/military action | `Numeric(Byte)` | `%15.0g` |
| `ilq88` | How old when first wounded in war/ilitary action | `Numeric(Byte)` | `%40.0g` |
| `ilq89` | Effect on life: been wounded in war/military action | `Numeric(Byte)` | `%15.0g` |
| `ilq90` | Witnessed serious injury/death of someone in war/military action | `Numeric(Byte)` | `%15.0g` |
| `ilq91` | How old when first witnessed serious injury/death of someone in war/military act | `Numeric(Byte)` | `%40.0g` |
| `ilq92` | Effect on life: witnessing serious injury/death of someone in war/military actio | `Numeric(Byte)` | `%15.0g` |
| `ilq93` | Lost close friend/relative in war/military service | `Numeric(Byte)` | `%15.0g` |
| `ilq94` | How old when first lost close friend/relative in war/military service | `Numeric(Byte)` | `%40.0g` |
| `ilq95` | Effect on life: losing a close friend/relative in war/military service | `Numeric(Byte)` | `%15.0g` |
| `ilq96` | Been wounded in a terrorist act (an attack by terrorists against civilians) | `Numeric(Byte)` | `%15.0g` |
| `ilq97` | How old when first wounded in a terrorist act | `Numeric(Byte)` | `%40.0g` |
| `ilq98` | Effect on life: been wounded in a terrorist act | `Numeric(Byte)` | `%15.0g` |
| `ilq99` | Witnessed a terrorist act in which you yourself were not harmed | `Numeric(Byte)` | `%15.0g` |
| `ilq100` | How old when first witnessed a terrorist act | `Numeric(Byte)` | `%40.0g` |
| `ilq101` | Effect on life: witnessing a terrorist act | `Numeric(Byte)` | `%15.0g` |
| `ilq102` | Experienced the injury/death of a close friend/relative in a terrorist act | `Numeric(Byte)` | `%15.0g` |
| `ilq103` | How old when first experienced injury/death of a close friend/relative in a terr | `Numeric(Byte)` | `%40.0g` |
| `ilq104` | Effect on life: experiencing injury/death of a close friend/relative in a terror | `Numeric(Byte)` | `%15.0g` |
| `ilq105` | Been at risk of death due to illness/serious accident | `Numeric(Byte)` | `%15.0g` |
| `ilq106` | How old when first been at rist of death due to illness/serious accident | `Numeric(Byte)` | `%40.0g` |
| `ilq107` | Effect on life: been at rist of death due to illness/serious accident | `Numeric(Byte)` | `%15.0g` |
| `ilq108` | Had a close friend/relative at risk of death due to illness/serious accident | `Numeric(Byte)` | `%15.0g` |
| `ilq109` | How old when first had a close friend/relative at risk of death due to illness/s | `Numeric(Byte)` | `%40.0g` |
| `ilq110` | Effect on life: had a close friend/relative at risk of death due to illness/seri | `Numeric(Byte)` | `%15.0g` |
| `ilq111` | Experienced the death of a spouse | `Numeric(Byte)` | `%15.0g` |
| `ilq112` | How old when first experienced the death of a spouse | `Numeric(Byte)` | `%40.0g` |
| `ilq113` | Effect on life: experiencing the death of a spouse | `Numeric(Byte)` | `%15.0g` |
| `il_b105` | Country of birth | `Numeric(Byte)` | `%13.0g` |
| `il_b106` | Fathers country of birth | `Numeric(Byte)` | `%13.0g` |
| `il_b107` | Self-definition of identity | `Numeric(Byte)` | `%21.0g` |

### `technical_variables` - Technical variables

- Dataset: `sharew2_rel9-0-0_technical_variables.dta`
- Read with: `ps.read_share_module("technical_variables", wave=2)`
- Rows: 37,132
- Variables: 16
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `fam_resp` | Family respondent | `Numeric(Byte)` | `%21.0g` |
| `fin_resp` | Financial respondent | `Numeric(Byte)` | `%24.0g` |
| `hou_resp` | Household respondent | `Numeric(Byte)` | `%24.0g` |
| `mn005_` | Single or couple interview | `Numeric(Byte)` | `%25.0g` |
| `mn016_` | Mother in household | `Numeric(Byte)` | `%10.0g` |
| `mn017_` | Father in household | `Numeric(Byte)` | `%10.0g` |
| `mn018_` | Mother-in-law in household | `Numeric(Byte)` | `%10.0g` |
| `mn019_` | Father-in-law in household | `Numeric(Byte)` | `%10.0g` |
| `mn024_` | Nursing home interview | `Numeric(Byte)` | `%17.0g` |
| `mn101_` | Questionnaire version | `Numeric(Byte)` | `%26.0g` |

### `vignettes` - Vignettes

- Dataset: `sharew2_rel9-0-0_vignettes.dta`
- Read with: `ps.read_share_module("vignettes", wave=2)`
- Rows: 7,646
- Variables: 49
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `type` | Vignette type | `Str(1)` | `%9s` |
| `v1` | B1-C1: pain self-rating | `Numeric(Byte)` | `%12.0g` |
| `v2` | B2-C2: sleep self-rating | `Numeric(Byte)` | `%12.0g` |
| `v3` | B3-C3: mobility self-rating | `Numeric(Byte)` | `%12.0g` |
| `v4` | B4-C4: memory self-rating | `Numeric(Byte)` | `%12.0g` |
| `v5` | B5-C5: breath self-rating | `Numeric(Byte)` | `%12.0g` |
| `v6` | B6-C6: depress self-rating | `Numeric(Byte)` | `%12.0g` |
| `v7` | B7: work disbility self-rating | `Numeric(Byte)` | `%12.0g` |
| `v8` | B8-C7: pain vignette 1 | `Numeric(Byte)` | `%12.0g` |
| `v13` | B9-C8: sleep vignette 3 | `Numeric(Byte)` | `%12.0g` |
| `v15` | B11-C10: memory vignette 1 | `Numeric(Byte)` | `%12.0g` |
| `v18` | B10-C9: mobility vignette 3 | `Numeric(Byte)` | `%12.0g` |
| `v20` | B12-C11: breath vignette 1 | `Numeric(Byte)` | `%12.0g` |
| `v25` | B13-C12: depress vignette 3 | `Numeric(Byte)` | `%12.0g` |
| `v27` | B14: work disbility vignette 2 | `Numeric(Byte)` | `%12.0g` |
| `v31` | B15: work disbility vignette 6 | `Numeric(Byte)` | `%12.0g` |
| `v32` | B16: work disbility vignette 7 | `Numeric(Byte)` | `%12.0g` |
| `v39` | B17-C13: satisfaction: income | `Numeric(Byte)` | `%34.0g` |
| `v40` | B18-C14: satisfaction: social contacts | `Numeric(Byte)` | `%34.0g` |
| `v41` | B19-C15: satisfaction: daily activities | `Numeric(Byte)` | `%34.0g` |
| `v42` | B20-C16: satisfaction: live in general | `Numeric(Byte)` | `%34.0g` |
| `v43` | B21-C17: satisfaction: income | `Numeric(Byte)` | `%34.0g` |
| `v44` | B22-C18: satisfaction: income | `Numeric(Byte)` | `%34.0g` |
| `v45` | B23-C19: satisfaction: social contacts | `Numeric(Byte)` | `%34.0g` |
| `v46` | B24-C20: satisfaction: social contacts | `Numeric(Byte)` | `%34.0g` |
| `v47` | B25: satisfaction: job | `Numeric(Byte)` | `%34.0g` |
| `v48` | B26: satisfaction: job | `Numeric(Byte)` | `%34.0g` |
| `v49` | B27-C23: satisfaction: live | `Numeric(Byte)` | `%34.0g` |
| `v50` | B28-C24: satisfaction: live | `Numeric(Byte)` | `%34.0g` |
| `v51` | B29-C25: influence: municipality vignette 1 | `Numeric(Byte)` | `%13.0g` |
| `v52` | B30-C26: influence: municipality vignette 2 | `Numeric(Byte)` | `%13.0g` |
| `v53` | B31-C27: influence: municipality vignette 3 | `Numeric(Byte)` | `%13.0g` |
| `v54` | B32-C28: health care responsivness vignette 1 | `Numeric(Byte)` | `%12.0g` |
| `v55` | B33-C29: health care responsivness vignette 2 | `Numeric(Byte)` | `%12.0g` |
| `v56` | B34-C30: health care responsivness vignette 3 | `Numeric(Byte)` | `%12.0g` |
| `v57` | B35-C31: health care responsivness vignette 4 | `Numeric(Byte)` | `%12.0g` |
| `v58` | B36-C32: health care responsivness vignette 5 | `Numeric(Byte)` | `%12.0g` |
| `v59` | B37-C33: health care responsivness vignette 6 | `Numeric(Byte)` | `%12.0g` |
| `v60` | C34: health care responsivness vignette 7 | `Numeric(Byte)` | `%12.0g` |
| `v61` | C35: health care responsivness vignette 8 | `Numeric(Byte)` | `%12.0g` |
| `v62` | C36: health care responsivness vignette 9 | `Numeric(Byte)` | `%12.0g` |
| `v63` | C21: satisfaction: daily activities | `Numeric(Byte)` | `%34.0g` |
| `v64` | C22: satisfaction: daily activities | `Numeric(Byte)` | `%34.0g` |


## Generated Modules

### `gv_exrates` - Exchange rates and PPP variables

- Dataset: `sharew2_rel9-0-0_gv_exrates.dta`
- Read with: `ps.read_share_module("gv_exrates", wave=2)`
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

- Dataset: `sharew2_rel9-0-0_gv_health.dta`
- Read with: `ps.read_share_module("gv_health", wave=2)`
- Rows: 37,132
- Variables: 44
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `adl` | Number of limitations with activities of daily living (adl) | `Numeric(Byte)` | `%10.0g` |
| `adl2` | 1+ adl limitations | `Numeric(Byte)` | `%18.0g` |
| `bmi` | Body mass index | `Numeric(Float)` | `%28.0g` |
| `bmi2` | Bmi categories | `Numeric(Byte)` | `%27.0g` |
| `casp` | CASP index for quality of life and well-being | `Numeric(Byte)` | `%10.0g` |
| `chronic2w2` | 2+ chronic diseases (w2 version) | `Numeric(Byte)` | `%20.0g` |
| `chronicw2` | Number of chronic diseases (w2 version) | `Numeric(Byte)` | `%10.0g` |
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
| `orienti` | Orientation to date, month,year and day of week | `Numeric(Byte)` | `%10.0g` |
| `phactiv` | Physical inactivity | `Numeric(Byte)` | `%45.0g` |
| `sphus` | Self-perceived health - us version | `Numeric(Byte)` | `%10.0g` |
| `sphus2` | Sphus-less than very good health | `Numeric(Byte)` | `%19.0g` |
| `symptoms2w2` | 2+ symptoms (w2 version) | `Numeric(Byte)` | `%20.0g` |
| `symptomsw2` | Number of symptoms (w2 version) | `Numeric(Byte)` | `%10.0g` |
| `wspeed` | Walking speed | `Numeric(Float)` | `%9.0g` |
| `wspeed2` | Walking speed: cut-off point | `Numeric(Byte)` | `%25.0g` |

### `gv_housing` - Housing generated variables

- Dataset: `sharew2_rel9-0-0_gv_housing.dta`
- Read with: `ps.read_share_module("gv_housing", wave=2)`
- Rows: 37,132
- Variables: 11
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `areabldgi` | Area of building | `Numeric(Byte)` | `%38.0g` |
| `typebldgi` | Type of building | `Numeric(Byte)` | `%57.0g` |
| `floorsbli` | Number of floors of building | `Numeric(Byte)` | `%10.0g` |
| `nstepsi` | Number of steps to entrance | `Numeric(Byte)` | `%12.0g` |
| `nuts1_2003` | NUTS level 1: nomenclature of territorial units for statistics | `Str(30)` | `%30s` |

### `gv_imputations` - Multiple imputations

- Dataset: `sharew2_rel9-0-0_gv_imputations.dta`
- Read with: `ps.read_share_module("gv_imputations", wave=2)`
- Rows: 185,660
- Variables: 245
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `implicat` | Implicat number | `Numeric(Byte)` | `%9.0g` |
| `htype` | Household type | `Numeric(Byte)` | `%16.0g` |
| `fam_resp` | Family respondent | `Numeric(Byte)` | `%14.0g` |
| `fin_resp` | Financial respondent | `Numeric(Byte)` | `%14.0g` |
| `hou_resp` | Household respondent | `Numeric(Byte)` | `%14.0g` |
| `exrate` | Exchange rate | `Numeric(Double)` | `%10.0g` |
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
| `aftgiv` | Financial transfers given | `Numeric(Double)` | `%9.0g` |
| `aftrec` | Financial transfers received | `Numeric(Double)` | `%9.0g` |
| `aftinh` | Inheritance received | `Numeric(Double)` | `%9.0g` |
| `rhre` | Rent and home-related expenditures | `Numeric(Double)` | `%9.0g` |
| `home` | Value of main residence | `Numeric(Double)` | `%9.0g` |
| `mort` | Mortgage on main residence | `Numeric(Double)` | `%9.0g` |
| `ores` | Value of other real estate - Amount | `Numeric(Double)` | `%9.0g` |
| `yrent` | Income from rent | `Numeric(Double)` | `%9.0g` |
| `yaohm` | Income from other household members | `Numeric(Double)` | `%9.0g` |
| `fahc` | Amount spent on food at home | `Numeric(Double)` | `%9.0g` |
| `fohc` | Amount spent on food outside home | `Numeric(Double)` | `%9.0g` |
| `telc` | Amount spent on telephones | `Numeric(Double)` | `%9.0g` |
| `hprf` | Value of home produced food | `Numeric(Double)` | `%9.0g` |
| `bacc` | Bank accounts | `Numeric(Double)` | `%9.0g` |
| `bsmf` | Bond, stock and mutual funds | `Numeric(Double)` | `%9.0g` |
| `ybabsmf` | Interest/dividend from financial assett | `Numeric(Double)` | `%9.0g` |
| `slti` | Savings for long-term investments | `Numeric(Double)` | `%9.0g` |
| `vbus` | Value of own business | `Numeric(Double)` | `%9.0g` |
| `sbus` | Share of own business | `Numeric(Double)` | `%9.0g` |
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
| `cjs` | Current job situation | `Numeric(Byte)` | `%63.0g` |
| `pwork` | Did any paid work | `Numeric(Byte)` | `%14.0g` |
| `empstat` | Employee or self-employed | `Numeric(Byte)` | `%15.0g` |
| `rhfo` | Received help from others (how many) | `Numeric(Byte)` | `%14.0g` |
| `ghto` | Given help to others (how many) | `Numeric(Byte)` | `%14.0g` |
| `ghih` | Given help in the household (how many) | `Numeric(Byte)` | `%14.0g` |
| `rhih` | Received help in the household (how many) | `Numeric(Byte)` | `%14.0g` |
| `otrf` | Owner, tenant or rent free | `Numeric(Byte)` | `%43.0g` |
| `fdistress` | Household able to make ends meet | `Numeric(Byte)` | `%21.0g` |
| `nalm` | Number of activities last month | `Numeric(Byte)` | `%14.0g` |
| `lifesat` | Life satisfaction | `Numeric(Byte)` | `%23.0g` |
| `lifehap` | Life happiness | `Numeric(Byte)` | `%14.0g` |
| `tppdi` | Third persons present during the interview | `Numeric(Byte)` | `%14.0g` |
| `willans` | Willingness to answer | `Numeric(Byte)` | `%53.0g` |
| `clarif` | Respondent asked for clarifications | `Numeric(Byte)` | `%14.0g` |
| `undersq` | Respondent understood questions | `Numeric(Byte)` | `%14.0g` |
| `hnrsc` | Help needed to read showcards | `Numeric(Byte)` | `%29.0g` |
| `inpat_f` | Paid out-of-pocket for inpatient care - Flag | `Numeric(Byte)` | `%21.0g` |
| `outpa_f` | Paid out-of-pocket for outpatient care - Flag | `Numeric(Byte)` | `%21.0g` |
| `drugs_f` | Paid out-of-pocket for prescribed drugs - Flag | `Numeric(Byte)` | `%21.0g` |
| `nurs_f` | Paid out-of-pocket for nursing home - Flag | `Numeric(Byte)` | `%21.0g` |
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
| `aftgiv_f` | Financial transfers given - Flag | `Numeric(Byte)` | `%21.0g` |
| `aftrec_f` | Financial transfers received - Flag | `Numeric(Byte)` | `%21.0g` |
| `aftinh_f` | Inheritance received - Flag | `Numeric(Byte)` | `%21.0g` |
| `rhre_f` | Rent and home-related expenditures - Flag | `Numeric(Byte)` | `%21.0g` |
| `home_f` | Value of main residence - Flag | `Numeric(Byte)` | `%21.0g` |
| `mort_f` | Mortgage on main residence - Flag | `Numeric(Byte)` | `%21.0g` |
| `ores_f` | Value of other real estate - Flag | `Numeric(Byte)` | `%21.0g` |
| `yrent_f` | Income from rent - Flag | `Numeric(Byte)` | `%21.0g` |
| `yaohm_f` | Income from other household members - Flag | `Numeric(Byte)` | `%21.0g` |
| `fahc_f` | Amount spent on food at home - Flag | `Numeric(Byte)` | `%21.0g` |
| `fohc_f` | Amount spent on food outside home - Flag | `Numeric(Byte)` | `%21.0g` |
| `telc_f` | Amount spent on telephones - Flag | `Numeric(Byte)` | `%21.0g` |
| `hprf_f` | Value of home produced food - Flag | `Numeric(Byte)` | `%21.0g` |
| `bacc_f` | Bank accounts - Flag | `Numeric(Byte)` | `%21.0g` |
| `bsmf_f` | Bond, stock and mutual funds - Flag | `Numeric(Byte)` | `%21.0g` |
| `ybabsmf_f` | Interest/dividend from financial assett - Flag | `Numeric(Byte)` | `%21.0g` |
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
| `empstat_f` | Employee or self-employed - Flag | `Numeric(Byte)` | `%20.0g` |
| `rhfo_f` | Received help from others (how many) - Flag | `Numeric(Byte)` | `%20.0g` |
| `ghto_f` | Given help to others (how many) - Flag | `Numeric(Byte)` | `%20.0g` |
| `ghih_f` | Given help in the household (how many) - Flag | `Numeric(Byte)` | `%20.0g` |
| `rhih_f` | Received help in the household (how many) - Flag | `Numeric(Byte)` | `%20.0g` |
| `otrf_f` | Owner, tenant or rent free - Flag | `Numeric(Byte)` | `%20.0g` |
| `fdistress_f` | Household able to make ends meet - Flag | `Numeric(Byte)` | `%20.0g` |
| `nalm_f` | Number of activities last month - Flag | `Numeric(Byte)` | `%20.0g` |
| `lifesat_f` | Life satisfaction - Flag | `Numeric(Byte)` | `%20.0g` |
| `lifehap_f` | Life happiness - Flag | `Numeric(Byte)` | `%20.0g` |
| `tppdi_f` | Third persons present during the interview - Flag | `Numeric(Byte)` | `%20.0g` |
| `willans_f` | Willingness to answer - Flag | `Numeric(Byte)` | `%20.0g` |
| `clarif_f` | Respondent asked for clarifications - Flag | `Numeric(Byte)` | `%20.0g` |
| `undersq_f` | Respondent understood questions - Flag | `Numeric(Byte)` | `%20.0g` |
| `hnrsc_f` | Help needed to read showcards â€“ Flag | `Numeric(Byte)` | `%20.0g` |
| `currency` | currency | `Str(14)` | `%14s` |
| `nomx2005` | Nominal exchange rate (national currency/Euro), annual average, 2005 | `Numeric(Double)` | `%10.0g` |
| `nomx2006` | Nominal exchange rate (national currency/Euro), annual average, 2006 | `Numeric(Double)` | `%10.0g` |
| `nomx2007` | Nominal exchange rate (national currency/Euro), annual average, 2007 | `Numeric(Double)` | `%10.0g` |
| `nomx2008` | Nominal exchange rate (national currency/Euro), annual average, 2008 | `Numeric(Double)` | `%10.0g` |
| `nomx2009` | Nominal exchange rate (national currency/Euro), annual average, 2009 | `Numeric(Double)` | `%10.0g` |
| `nomx2010` | Nominal exchange rate (national currency/Euro), annual average, 2010 | `Numeric(Double)` | `%10.0g` |
| `pppc2005` | Current PPP exchange rate (national currency/Euro), 2005 | `Numeric(Double)` | `%10.0g` |
| `pppc2006` | Current PPP exchange rate (national currency/Euro), 2006 | `Numeric(Double)` | `%10.0g` |
| `pppc2007` | Current PPP exchange rate (national currency/Euro), 2007 | `Numeric(Double)` | `%10.0g` |
| `pppc2008` | Current PPP exchange rate (national currency/Euro), 2008 | `Numeric(Double)` | `%10.0g` |
| `pppc2009` | Current PPP exchange rate (national currency/Euro), 2009 | `Numeric(Double)` | `%10.0g` |
| `pppc2010` | Current PPP exchange rate (national currency/Euro), 2010 | `Numeric(Double)` | `%10.0g` |
| `pppk2005` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2005 | `Numeric(Double)` | `%10.0g` |
| `pppk2006` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2006 | `Numeric(Double)` | `%10.0g` |
| `pppk2007` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2007 | `Numeric(Double)` | `%10.0g` |
| `pppk2008` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2008 | `Numeric(Double)` | `%10.0g` |
| `pppk2009` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2009 | `Numeric(Double)` | `%10.0g` |
| `pppk2010` | Constant PPP exchange rate (national currency/Euro), (Germany 2015=1), 2010 | `Numeric(Double)` | `%10.0g` |

### `gv_isced` - ISCED education recodes

- Dataset: `sharew2_rel9-0-0_gv_isced.dta`
- Read with: `ps.read_share_module("gv_isced", wave=2)`
- Rows: 37,132
- Variables: 12
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `isced1997_c1` | Respondent's child 1: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c2` | Respondent's child 2: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c3` | Respondent's child 3: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_c4` | Respondent's child 4: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_r` | Respondent: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |
| `isced1997_sp` | Spouse/ex-spouse of respondent: ISCED-97 coding of education | `Numeric(Byte)` | `%15.0g` |

### `gv_weights` - Cross-sectional weights

- Dataset: `sharew2_rel9-0-0_gv_weights.dta`
- Read with: `ps.read_share_module("gv_weights", wave=2)`
- Rows: 37,132
- Variables: 14
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid2` | Household identifier (wave 2) | `Str(11)` | `%11s` |
| `mergeidp2` | Partner identifier (wave 2) | `Str(12)` | `%12s` |
| `coupleid2` | Couple identifier (wave 2) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `dw_w2` | Design weight - wave 2 | `Numeric(Double)` | `%10.0g` |
| `cchw_w2` | Calibrated cross-sectional household weight - wave 2 | `Numeric(Double)` | `%10.0g` |
| `cciw_w2` | Calibrated cross-sectional individual weight - wave 2 | `Numeric(Double)` | `%10.0g` |
| `subsample` | Indicator for country-specific subsample | `Str(6)` | `%9s` |
| `stratum1` | Indicator for primary stratum (if any) | `Str(9)` | `%9s` |
| `stratum2` | Indicator for secondary stratum (if any) | `Str(4)` | `%9s` |
| `psu` | Primary sampling unit | `Str(10)` | `%10s` |
| `ssu` | Secondary sampling unit (if any) | `Str(5)` | `%9s` |
