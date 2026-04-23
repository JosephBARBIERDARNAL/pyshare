---
icon: lucide/list-tree
---

# Wave 3 Variable Dictionary

This page is generated from the local SHARE wave 3 release `9-0-0` Stata files.

It covers 18 datasets and 3,409 variable entries for the files currently available in `data/`.

[Back to variable dictionary](./index.md)

## Overview

| Module | Category | Meaning | Key | Variables | Rows | File |
| --- | --- | --- | --- | --- | --- | --- |
| `cv_r` | core | Coverscreen on individual level | `mergeid` | 26 | 40,630 | `sharew3_rel9-0-0_cv_r.dta` |
| `gs` | core | Grip Strength | `mergeid` | 24 | 28,454 | `sharew3_rel9-0-0_gs.dta` |
| `iv` | core | Interviewer Observations | `mergeid` | 32 | 28,454 | `sharew3_rel9-0-0_iv.dta` |
| `xt` | core | End-of-Life Interview | `mergeid` | 172 | 1,207 | `sharew3_rel9-0-0_xt.dta` |
| `ac` | sharelife | Retrospective Accommodation | `mergeid` | 916 | 28,454 | `sharew3_rel9-0-0_ac.dta` |
| `cs` | sharelife | Childhood Section | `mergeid` | 28 | 28,454 | `sharew3_rel9-0-0_cs.dta` |
| `dq` | sharelife | Disability | `mergeid` | 177 | 28,454 | `sharew3_rel9-0-0_dq.dta` |
| `fs` | sharelife | Financial Section | `mergeid` | 19 | 28,454 | `sharew3_rel9-0-0_fs.dta` |
| `gl` | sharelife | General Life and Persecution | `mergeid` | 90 | 28,454 | `sharew3_rel9-0-0_gl.dta` |
| `hc` | sharelife | Retrospective Health Care | `mergeid` | 179 | 28,454 | `sharew3_rel9-0-0_hc.dta` |
| `hs` | sharelife | Health History / Health Section | `mergeid` | 175 | 28,454 | `sharew3_rel9-0-0_hs.dta` |
| `rc` | sharelife | Retrospective Children History | `mergeid` | 360 | 28,454 | `sharew3_rel9-0-0_rc.dta` |
| `re` | sharelife | Retrospective Employment | `mergeid` | 724 | 28,454 | `sharew3_rel9-0-0_re.dta` |
| `rp` | sharelife | Retrospective Partner History | `mergeid` | 127 | 28,454 | `sharew3_rel9-0-0_rp.dta` |
| `st` | sharelife | SHARELIFE demographics | `mergeid` | 12 | 28,454 | `sharew3_rel9-0-0_st.dta` |
| `wq` | sharelife | Work Quality | `mergeid` | 258 | 28,454 | `sharew3_rel9-0-0_wq.dta` |
| `gv_exrates` | generated | Exchange rates and PPP variables | `country` | 76 | 29 | `sharew3_rel9-0-0_gv_exrates.dta` |
| `gv_weights` | generated | Cross-sectional weights | `mergeid` | 14 | 28,454 | `sharew3_rel9-0-0_gv_weights.dta` |

## Core Interview Modules

### `cv_r` - Coverscreen on individual level

- Dataset: `sharew3_rel9-0-0_cv_r.dta`
- Read with: `ps.read_share_module("cv_r", wave=3)`
- Rows: 40,630
- Variables: 26
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `waveid` | Identifier of original wave (person) | `Numeric(Byte)` | `%9.0g` |
| `waveid_hh` | Identifier of original wave (household) | `Numeric(Byte)` | `%10.0g` |
| `firstwave` | First appearance of person in SHARE | `Numeric(Byte)` | `%9.0g` |
| `firstwave_hh` | Wave household was sampled | `Numeric(Byte)` | `%9.0g` |
| `cvresp` | Coverscreen respondent | `Numeric(Byte)` | `%10.0g` |
| `deceased` | Deceased | `Numeric(Byte)` | `%9.0g` |
| `gender` | Male or female | `Numeric(Byte)` | `%10.0g` |
| `mobirth` | Month of birth | `Numeric(Byte)` | `%10.0g` |
| `yrbirth` | Year of birth | `Numeric(Int)` | `%10.0g` |
| `age2009` | Age in 2009 | `Numeric(Int)` | `%14.0g` |
| `age_int` | Age of respondent at the time of interview | `Numeric(Int)` | `%14.0g` |
| `mobirthp` | Month of birth spouse/partner | `Numeric(Byte)` | `%14.0g` |
| `yrbirthp` | Year of birth spouse/partner | `Numeric(Int)` | `%14.0g` |
| `agep2009` | Age of partner in 2009 | `Numeric(Byte)` | `%14.0g` |
| `partnerinhh` | Partner in household | `Numeric(Byte)` | `%21.0g` |
| `relrpers` | Relation to coverscreen respondent | `Numeric(Byte)` | `%20.0g` |
| `hhsize` | Household size | `Numeric(Byte)` | `%9.0g` |
| `interview` | Interview done in wave 3 | `Numeric(Byte)` | `%21.0g` |
| `int_year` | Interview year | `Numeric(Int)` | `%14.0g` |
| `int_month` | Interview month | `Numeric(Byte)` | `%14.0g` |

### `gs` - Grip Strength

- Dataset: `sharew3_rel9-0-0_gs.dta`
- Read with: `ps.read_share_module("gs", wave=3)`
- Rows: 28,454
- Variables: 24
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sl_gs001_` | Willing to have handgrip measured | `Numeric(Byte)` | `%31.0g` |
| `sl_gs010d1` | Why not completed gs test: r felt it would not be safe | `Numeric(Byte)` | `%12.0g` |
| `sl_gs010d2` | Why not completed gs test: iwer felt it would not be safe | `Numeric(Byte)` | `%12.0g` |
| `sl_gs010d3` | Why not completed gs test: r refused, no reason given | `Numeric(Byte)` | `%12.0g` |
| `sl_gs010d4` | Why not completed gs test: r tried but was unable to complete test | `Numeric(Byte)` | `%12.0g` |
| `sl_gs010d5` | Why not completed gs test: r did not understand the instructions | `Numeric(Byte)` | `%12.0g` |
| `sl_gs010d6` | Why not completed gs test: r had surgery, injury, swelling, etc. | `Numeric(Byte)` | `%12.0g` |
| `sl_gs010dot` | Why not completed gs test: others | `Numeric(Byte)` | `%12.0g` |
| `sl_gs002_` | Record respondent status | `Numeric(Byte)` | `%39.0g` |
| `sl_gs004_` | Dominant hand | `Numeric(Byte)` | `%10.0g` |
| `sl_gs006_` | 1st measurement: left hand | `Numeric(Byte)` | `%10.0g` |
| `sl_gs007_` | 2nd measurement: left hand | `Numeric(Byte)` | `%10.0g` |
| `sl_gs008_` | 1st measurement: right hand | `Numeric(Byte)` | `%10.0g` |
| `sl_gs009_` | 2nd measurement: right hand | `Numeric(Byte)` | `%10.0g` |
| `sl_gs012_` | How much effort gave r | `Numeric(Byte)` | `%90.0g` |
| `sl_gs013_` | The position of r for this test | `Numeric(Byte)` | `%10.0g` |
| `sl_gs014_` | R rested his/her arms on a support | `Numeric(Byte)` | `%10.0g` |
| `sl_maxgrip` | Max. of grip strength measures | `Numeric(Byte)` | `%9.0g` |

### `iv` - Interviewer Observations

- Dataset: `sharew3_rel9-0-0_iv.dta`
- Read with: `ps.read_share_module("iv", wave=3)`
- Rows: 28,454
- Variables: 32
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `intid` | Interviewer identifier (wave-specific) | `Str(10)` | `%10s` |
| `intidwX` | Interviewer identifier (fix across waves) | `Str(11)` | `%11s` |
| `sl_iv002d1` | Third persons present: nobody | `Numeric(Byte)` | `%12.0g` |
| `sl_iv002d2` | Third persons present: spouse or partner | `Numeric(Byte)` | `%12.0g` |
| `sl_iv002d3` | Third persons present: parent or parents | `Numeric(Byte)` | `%12.0g` |
| `sl_iv002d4` | Third persons present: child or children | `Numeric(Byte)` | `%12.0g` |
| `sl_iv002d5` | Third persons present: other relatives | `Numeric(Byte)` | `%12.0g` |
| `sl_iv002d6` | Third persons present: other persons present | `Numeric(Byte)` | `%12.0g` |
| `sl_iv003_` | Intervened in interview | `Numeric(Byte)` | `%17.0g` |
| `sl_iv003a_` | Filled in appointment card | `Numeric(Byte)` | `%10.0g` |
| `sl_iv003b_` | Used incentive | `Numeric(Byte)` | `%10.0g` |
| `sl_iv003c_` | Form of incentive | `Numeric(Byte)` | `%10.0g` |
| `sl_iv003d_` | Worth of incentive | `Numeric(Byte)` | `%27.0g` |
| `sl_iv004_` | Willingness to answer | `Numeric(Byte)` | `%53.0g` |
| `sl_iv005d1` | Why willingness worse: r was losing interest | `Numeric(Byte)` | `%12.0g` |
| `sl_iv005d2` | Why willingness worse: r was losing concentration/was getting tired | `Numeric(Byte)` | `%12.0g` |
| `sl_iv005dot` | Why willingness worse: other (specify) | `Numeric(Byte)` | `%12.0g` |
| `sl_iv007_` | Respondent asked for clarification | `Numeric(Byte)` | `%12.0g` |
| `sl_iv008_` | Respondent understood questions | `Numeric(Byte)` | `%12.0g` |
| `sl_iv009_` | Help needed reading showcards | `Numeric(Byte)` | `%29.0g` |
| `sl_iv010_` | Interview in house of respondent | `Numeric(Byte)` | `%10.0g` |
| `sl_iv011_` | Which area building located | `Numeric(Byte)` | `%38.0g` |
| `sl_iv012_` | Type of building | `Numeric(Byte)` | `%57.0g` |
| `sl_iv013_` | Number of floors of building | `Numeric(Byte)` | `%10.0g` |
| `sl_iv014_` | Number of steps to entrance | `Numeric(Byte)` | `%12.0g` |
| `sl_iv021_` | Relationship proxy to respondent | `Numeric(Byte)` | `%21.0g` |

### `xt` - End-of-Life Interview

- Dataset: `sharew3_rel9-0-0_xt.dta`
- Read with: `ps.read_share_module("xt", wave=3)`
- Rows: 1,207
- Variables: 172
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language_xt` | Language: End of life interview | `Numeric(Byte)` | `%44.0g` |
| `gender_xt` | Gender of the deceased | `Numeric(Byte)` | `%10.0g` |
| `yrbirth_xt` | Year of birth of the deceased | `Numeric(Int)` | `%10.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `sl_xt002_` | Relationship to the deceased | `Numeric(Byte)` | `%50.0g` |
| `sl_xt005_` | How often contact last twelve months | `Numeric(Byte)` | `%27.0g` |
| `sl_xt006_` | Proxy respondent's sex | `Numeric(Byte)` | `%10.0g` |
| `sl_xt007_` | Year of birth proxy | `Numeric(Int)` | `%12.0g` |
| `sl_xt008_` | Month of decease | `Numeric(Byte)` | `%10.0g` |
| `sl_xt009_` | Year of decease | `Numeric(Int)` | `%10.0g` |
| `sl_xt010_` | Age at the moment of decease | `Numeric(Int)` | `%10.0g` |
| `sl_xt011_` | Main cause of death | `Numeric(Byte)` | `%90.0g` |
| `sl_xt012c` | Main cause of death: xt012 coded | `Numeric(Byte)` | `%60.0g` |
| `sl_xt013_` | How long been ill before decease | `Numeric(Byte)` | `%51.0g` |
| `sl_xt014_` | Place of dying | `Numeric(Byte)` | `%42.0g` |
| `sl_xt015_` | Times in hospital last year before dying | `Numeric(Byte)` | `%18.0g` |
| `sl_xt016_` | Total time in hospital last year before dying | `Numeric(Byte)` | `%53.0g` |
| `sl_xt018_1` | Had medical care in last 12 months: care from a general practitioner | `Numeric(Byte)` | `%10.0g` |
| `sl_xt018_2` | Had medical care in last 12 months: care from specialist physicians | `Numeric(Byte)` | `%10.0g` |
| `sl_xt018_3` | Had medical care in last 12 months: hospital stays | `Numeric(Byte)` | `%10.0g` |
| `sl_xt018_4` | Had medical care in last 12 months: care in a nursing home | `Numeric(Byte)` | `%10.0g` |
| `sl_xt018_5` | Had medical care in last 12 months: hospice stays | `Numeric(Byte)` | `%10.0g` |
| `sl_xt018_6` | Had medical care in last 12 months: medication | `Numeric(Byte)` | `%10.0g` |
| `sl_xt018_7` | Had medical care in last 12 months: aids and appliances | `Numeric(Byte)` | `%10.0g` |
| `sl_xt018_8` | Had medical care in last 12 months: home care or home help due to disability | `Numeric(Byte)` | `%10.0g` |
| `sl_xt019e_1` | Costs medical care in last 12 months: care from a general practitioner | `Numeric(Double)` | `%12.0g` |
| `sl_xt019e_2` | Costs medical care in last 12 months: care from specialist physicians | `Numeric(Double)` | `%12.0g` |
| `sl_xt019e_3` | Costs medical care in last 12 months: hospital stays | `Numeric(Double)` | `%12.0g` |
| `sl_xt019e_4` | Costs medical care in last 12 months: care in a nursing home | `Numeric(Double)` | `%12.0g` |
| `sl_xt019e_5` | Costs medical care in last 12 months: hospice stays | `Numeric(Double)` | `%10.0g` |
| `sl_xt019e_6` | Costs medical care in last 12 months: medication | `Numeric(Double)` | `%12.0g` |
| `sl_xt019e_7` | Costs medical care in last 12 months: aids and appliances | `Numeric(Double)` | `%12.0g` |
| `sl_xt019e_8` | Costs medical care in last 12 months: home care or home help due to disability | `Numeric(Double)` | `%12.0g` |
| `sl_xt019ub_1` | Costs medical care in last 12 months: care from a general practitioner ub | `Numeric(Byte)` | `%32.0g` |
| `sl_xt019ub_2` | Costs medical care in last 12 months: care from specialist physicians ub | `Numeric(Byte)` | `%32.0g` |
| `sl_xt019ub_3` | Costs medical care in last 12 months: hospital stays ub | `Numeric(Byte)` | `%32.0g` |
| `sl_xt019ub_4` | Costs medical care in last 12 months: care in a nursing home ub | `Numeric(Byte)` | `%32.0g` |
| `sl_xt019ub_5` | Costs medical care in last 12 months: hospice stays ub | `Numeric(Byte)` | `%32.0g` |
| `sl_xt019ub_6` | Costs medical care in last 12 months: medication ub | `Numeric(Byte)` | `%32.0g` |
| `sl_xt019ub_7` | Costs medical care in last 12 months: aids and appliances ub | `Numeric(Byte)` | `%32.0g` |
| `sl_xt019ub_8` | Costs medical care in last 12 months: home care or home help due to disability u | `Numeric(Byte)` | `%32.0g` |
| `sl_xt019v1_1` | Bracket value 1: care from a general practitioner | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v1_2` | Bracket value 1: care from specialist physicians | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v1_3` | Bracket value 1: hospital stays | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v1_4` | Bracket value 1: care in a nursing home | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v1_5` | Bracket value 1: hospice stays | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v1_6` | Bracket value 1: medication | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v1_7` | Bracket value 1: aids and appliances | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v1_8` | Bracket value 1: home care or home help due to disability | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v2_1` | Bracket value 2: care from a general practitioner | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v2_2` | Bracket value 2: care from specialist physicians | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v2_3` | Bracket value 2: hospital stays | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v2_4` | Bracket value 2: care in a nursing home | `Numeric(Double)` | `%8.0g` |
| `sl_xt019v2_5` | Bracket value 2: hospice stays | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v2_6` | Bracket value 2: medication | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v2_7` | Bracket value 2: aids and appliances | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v2_8` | Bracket value 2: home care or home help due to disability | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v3_1` | Bracket value 3: care from a general practitioner | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v3_2` | Bracket value 3: care from specialist physicians | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v3_3` | Bracket value 3: hospital stays | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v3_4` | Bracket value 3: care in a nursing home | `Numeric(Double)` | `%8.0g` |
| `sl_xt019v3_5` | Bracket value 3: hospice stays | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v3_6` | Bracket value 3: medication | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v3_7` | Bracket value 3: aids and appliances | `Numeric(Float)` | `%8.0g` |
| `sl_xt019v3_8` | Bracket value 3: home care or home help due to disability | `Numeric(Float)` | `%8.0g` |
| `sl_xt020d1` | Difficulties: dressing, including putting on shoes and socks | `Numeric(Byte)` | `%12.0g` |
| `sl_xt020d2` | Difficulties: walking across a room | `Numeric(Byte)` | `%12.0g` |
| `sl_xt020d3` | Difficulties: bathing or showering | `Numeric(Byte)` | `%12.0g` |
| `sl_xt020d4` | Difficulties: eating, such as cutting up your food | `Numeric(Byte)` | `%12.0g` |
| `sl_xt020d5` | Difficulties: getting in or out of bed | `Numeric(Byte)` | `%12.0g` |
| `sl_xt020d6` | Difficulties: using the toilet, including getting up or down | `Numeric(Byte)` | `%12.0g` |
| `sl_xt020d7` | Difficulties: preparing a hot meal | `Numeric(Byte)` | `%12.0g` |
| `sl_xt020d8` | Difficulties: shopping for groceries | `Numeric(Byte)` | `%12.0g` |
| `sl_xt020d9` | Difficulties: making telephone calls | `Numeric(Byte)` | `%12.0g` |
| `sl_xt020d10` | Difficulties: taking medication | `Numeric(Byte)` | `%12.0g` |
| `sl_xt020dno` | Difficulties: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_xt022_` | Anyone helped with adl | `Numeric(Byte)` | `%10.0g` |
| `sl_xt023d1` | Who has helped with adl: proxy respondent | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023d2` | Who has helped with adl: husband/wife/partner of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023d3` | Who has helped with adl: mother/father of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023d4` | Who has helped with adl: son of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023d5` | Who has helped with adl: son-in-law of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023d6` | Who has helped with adl: daughter of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023d7` | Who has helped with adl: daughter-in-law of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023d8` | Who has helped with adl: grandson of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023d9` | Who has helped with adl: granddaughter of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023d10` | Who has helped with adl: sister of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023d11` | Who has helped with adl: brother of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023d12` | Who has helped with adl: other relative | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023d13` | Who has helped with adl: unpaid volunteer | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023d14` | Who has helped with adl: professional helper (e.g. nurse) | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023d15` | Who has helped with adl: friend/neighbor of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt023dot` | Who has helped with adl: other person | `Numeric(Byte)` | `%12.0g` |
| `sl_xt024_` | Time the deceased received help | `Numeric(Byte)` | `%49.0g` |
| `sl_xt025_` | Hours of help necessary during typical day | `Numeric(Byte)` | `%10.0g` |
| `sl_xt026_` | The deceased had a will | `Numeric(Byte)` | `%10.0g` |
| `sl_xt027d1` | Beneficiaries of estate: proxy respondent | `Numeric(Byte)` | `%12.0g` |
| `sl_xt027d2` | Beneficiaries of estate: husband/wife/partner of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt027d3` | Beneficiaries of estate: children of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt027d4` | Beneficiaries of estate: grandchildren of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt027d5` | Beneficiaries of estate: siblings of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt027d6` | Beneficiaries of estate: other relatives of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt027d7` | Beneficiaries of estate: other non-relatives | `Numeric(Byte)` | `%12.0g` |
| `sl_xt027d8` | Beneficiaries of estate: church, foundation or charitable organization | `Numeric(Byte)` | `%12.0g` |
| `sl_xt027d9` | Beneficiaries of estate: deceased did not leave anything at all (spontaneous) | `Numeric(Byte)` | `%12.0g` |
| `sl_xt030_` | The deceased owned home | `Numeric(Byte)` | `%10.0g` |
| `sl_xt031e` | Value home after mortgages | `Numeric(Double)` | `%10.0g` |
| `sl_xt031ub` | Value home after mortgages ub | `Numeric(Byte)` | `%32.0g` |
| `sl_xt031v1` | Bracket value 1 | `Numeric(Double)` | `%12.0g` |
| `sl_xt031v2` | Bracket value 2 | `Numeric(Double)` | `%12.0g` |
| `sl_xt031v3` | Bracket value 3 | `Numeric(Double)` | `%12.0g` |
| `sl_xt032d1` | Who inherited home of the deceased: proxy respondent | `Numeric(Byte)` | `%12.0g` |
| `sl_xt032d2` | Who inherited home of the deceased: husband/wife/partner of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt032d3` | Who inherited home of the deceased: sons or daughters | `Numeric(Byte)` | `%12.0g` |
| `sl_xt032d4` | Who inherited home of the deceased: grandchildren | `Numeric(Byte)` | `%12.0g` |
| `sl_xt032d5` | Who inherited home of the deceased: siblings | `Numeric(Byte)` | `%12.0g` |
| `sl_xt032d6` | Who inherited home of the deceased: other relatives | `Numeric(Byte)` | `%12.0g` |
| `sl_xt032d7` | Who inherited home of the deceased: other non-relatives | `Numeric(Byte)` | `%12.0g` |
| `sl_xt033_` | The deceased owned any life insurance policies | `Numeric(Byte)` | `%10.0g` |
| `sl_xt034e` | Value of all life insurance policies | `Numeric(Double)` | `%12.0g` |
| `sl_xt035d1` | Beneficiaries of life insurance policies: proxy respondent | `Numeric(Byte)` | `%12.0g` |
| `sl_xt035d2` | Beneficiaries of life insurance policies: husband/wife/partner of the deceased | `Numeric(Byte)` | `%12.0g` |
| `sl_xt035d3` | Beneficiaries of life insurance policies: sons or daughters | `Numeric(Byte)` | `%12.0g` |
| `sl_xt035d4` | Beneficiaries of life insurance policies: grandchildren | `Numeric(Byte)` | `%12.0g` |
| `sl_xt035d5` | Beneficiaries of life insurance policies: siblings | `Numeric(Byte)` | `%12.0g` |
| `sl_xt035d6` | Beneficiaries of life insurance policies: other relatives | `Numeric(Byte)` | `%12.0g` |
| `sl_xt035d7` | Beneficiaries of life insurance policies: other non-relatives | `Numeric(Byte)` | `%12.0g` |
| `sl_xt037_1` | Deceased owned assets: businesses (incl. land or premises) | `Numeric(Byte)` | `%10.0g` |
| `sl_xt037_2` | Deceased owned assets: other real estate | `Numeric(Byte)` | `%10.0g` |
| `sl_xt037_3` | Deceased owned assets: cars | `Numeric(Byte)` | `%10.0g` |
| `sl_xt037_4` | Deceased owned assets: financial assets (e.g. cash/money/stocks) | `Numeric(Byte)` | `%10.0g` |
| `sl_xt037_5` | Deceased owned assets: jewelry or antiquities | `Numeric(Byte)` | `%10.0g` |
| `sl_xt038e_1` | Value: businesses (incl. land or premises) | `Numeric(Double)` | `%10.0g` |
| `sl_xt038e_2` | Value: other real estate | `Numeric(Double)` | `%12.0g` |
| `sl_xt038e_3` | Value: cars | `Numeric(Double)` | `%10.0g` |
| `sl_xt038e_4` | Value: financial assets (e.g. cash/money/stocks) | `Numeric(Double)` | `%10.0g` |
| `sl_xt038e_5` | Value: jewelry or antiquities | `Numeric(Double)` | `%10.0g` |
| `sl_xt038ub_1` | Value: businesses (incl. land or premises) ub | `Numeric(Byte)` | `%32.0g` |
| `sl_xt038ub_2` | Value: other real estate ub | `Numeric(Byte)` | `%32.0g` |
| `sl_xt038ub_3` | Value: cars ub | `Numeric(Byte)` | `%32.0g` |
| `sl_xt038ub_4` | Value: financial assets (e.g. cash/money/stocks) ub | `Numeric(Byte)` | `%32.0g` |
| `sl_xt038ub_5` | Value: jewelry or antiquities ub | `Numeric(Byte)` | `%32.0g` |
| `sl_xt038v1_1` | Bracket value 1: businesses (incl. land or premises) | `Numeric(Double)` | `%8.0g` |
| `sl_xt038v1_2` | Bracket value 1: other real estate | `Numeric(Double)` | `%8.0g` |
| `sl_xt038v1_3` | Bracket value 1: cars | `Numeric(Float)` | `%8.0g` |
| `sl_xt038v1_4` | Bracket value 1: financial assets (e.g. cash/money/stocks) | `Numeric(Double)` | `%8.0g` |
| `sl_xt038v1_5` | Bracket value 1: jewelry or antiquities | `Numeric(Float)` | `%8.0g` |
| `sl_xt038v2_1` | Bracket value 2: businesses (incl. land or premises) | `Numeric(Double)` | `%12.0g` |
| `sl_xt038v2_2` | Bracket value 2: other real estate | `Numeric(Double)` | `%8.0g` |
| `sl_xt038v2_3` | Bracket value 2: cars | `Numeric(Double)` | `%8.0g` |
| `sl_xt038v2_4` | Bracket value 2: financial assets (e.g. cash/money/stocks) | `Numeric(Double)` | `%8.0g` |
| `sl_xt038v2_5` | Bracket value 2: jewelry or antiquities | `Numeric(Float)` | `%8.0g` |
| `sl_xt038v3_1` | Bracket value 3: businesses (incl. land or premises) | `Numeric(Double)` | `%12.0g` |
| `sl_xt038v3_2` | Bracket value 3: other real estate | `Numeric(Double)` | `%8.0g` |
| `sl_xt038v3_3` | Bracket value 3: cars | `Numeric(Double)` | `%8.0g` |
| `sl_xt038v3_4` | Bracket value 3: financial assets (e.g. cash/money/stocks) | `Numeric(Double)` | `%8.0g` |
| `sl_xt038v3_5` | Bracket value 3: jewelry or antiquities | `Numeric(Double)` | `%8.0g` |
| `sl_xt039_` | Number of children the deceased had at the end | `Numeric(Byte)` | `%10.0g` |
| `sl_xt040a_` | Total estate divided among the children | `Numeric(Byte)` | `%62.0g` |
| `sl_xt040b_` | Some children received more to make up for previous gifts | `Numeric(Byte)` | `%10.0g` |
| `sl_xt040c_` | Some children received more to give them financial support | `Numeric(Byte)` | `%10.0g` |
| `sl_xt040d_` | Some children received more for caring | `Numeric(Byte)` | `%10.0g` |
| `sl_xt040e_` | Some children received more for other reasons | `Numeric(Byte)` | `%10.0g` |
| `sl_xt041_` | The funeral was accompanied by a religious ceremony | `Numeric(Byte)` | `%10.0g` |
| `sl_xt043_` | Interview mode | `Numeric(Byte)` | `%23.0g` |
| `sl_xt105_` | Difficulties remembering where | `Numeric(Byte)` | `%10.0g` |
| `sl_xt106_` | Difficulties remembering the year | `Numeric(Byte)` | `%10.0g` |
| `sl_xt107_` | Difficulties recognizing | `Numeric(Byte)` | `%10.0g` |
| `sl_xt109_` | Deceased married at time of death | `Numeric(Byte)` | `%10.0g` |


## SHARELIFE Modules

### `ac` - Retrospective Accommodation

- Dataset: `sharew3_rel9-0-0_ac.dta`
- Read with: `ps.read_share_module("ac", wave=3)`
- Rows: 28,454
- Variables: 916
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sl_ac002d1` | Events in accomodation: lived in children's home | `Numeric(Byte)` | `%12.0g` |
| `sl_ac002d2` | Events in accomodation: fostered with another family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac002d3` | Events in accomodation: evacuated/relocated during war | `Numeric(Byte)` | `%12.0g` |
| `sl_ac002d4` | Events in accomodation: lived in prisoner of war camp | `Numeric(Byte)` | `%12.0g` |
| `sl_ac002d5` | Events in accomodation: lived in prison | `Numeric(Byte)` | `%12.0g` |
| `sl_ac002d6` | Events in accomodation: lived in labor camp | `Numeric(Byte)` | `%12.0g` |
| `sl_ac002d7` | Events in accomodation: lived in concentration camp | `Numeric(Byte)` | `%12.0g` |
| `sl_ac002d8` | Events in accomodation: inpatient in tb institution | `Numeric(Byte)` | `%12.0g` |
| `sl_ac002d9` | Events in accomodation: stayed in psychiatric hospital | `Numeric(Byte)` | `%12.0g` |
| `sl_ac002d10` | Events in accomodation: homeless for 1 month + | `Numeric(Byte)` | `%12.0g` |
| `sl_ac002dno` | Events in accomodation: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_ac003_` | When established home | `Numeric(Int)` | `%24.0g` |
| `sl_ac004_` | When born lived in same residence more than 6 months | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_1` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac007_1` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_1` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_1` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_1` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_1` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_1` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_1` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_1` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_1` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_1_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_1` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_1` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_1` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_1` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_1` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_1` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_1` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_1` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_1` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_1` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_1` | Currency of owned property - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_ac021_1` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_1` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_1` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_1` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac023_1` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_1` | Sale currency of owned property  - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_ac005_2` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_2` | Start living at residence | `Numeric(Int)` | `%12.0g` |
| `sl_ac007_2` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_2` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_2` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_2` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_2` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_2` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_2` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_2` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_2` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_2_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_2` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_2` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_2` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_2` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_2` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_2` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_2` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_2` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_2` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_2` | Price of owned property | `Numeric(Double)` | `%10.0g` |
| `sl_ac020c_2` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_2` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_2` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_2` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_2` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_2` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_2` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_2` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_3` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_3` | Start living at residence | `Numeric(Int)` | `%12.0g` |
| `sl_ac007_3` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_3` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_3` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_3` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_3` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_3` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_3` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_3` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_3` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_3_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_3` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_3` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_3` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_3` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_3` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_3` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_3` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_3` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_3` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_3` | Price of owned property | `Numeric(Double)` | `%10.0g` |
| `sl_ac020c_3` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_3` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_3` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_3` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_3` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_3` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_3` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_3` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_4` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_4` | Start living at residence | `Numeric(Int)` | `%12.0g` |
| `sl_ac007_4` | Estimated start year of accommodation | `Numeric(Int)` | `%12.0g` |
| `sl_ac008_4` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_4` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_4` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_4` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_4` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_4` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_4` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_4` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_4_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_4` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_4` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_4` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_4` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_4` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_4` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_4` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_4` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_4` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_4` | Price of owned property | `Numeric(Double)` | `%10.0g` |
| `sl_ac020c_4` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_4` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_4` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_4` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_4` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_4` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_4` | Sale price of owned property | `Numeric(Double)` | `%10.0g` |
| `sl_ac024c_4` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_5` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_5` | Start living at residence | `Numeric(Int)` | `%12.0g` |
| `sl_ac007_5` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_5` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_5` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_5` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_5` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_5` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_5` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_5` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_5` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_5_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_5` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_5` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_5` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_5` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_5` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_5` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_5` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_5` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_5` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_5` | Price of owned property | `Numeric(Double)` | `%10.0g` |
| `sl_ac020c_5` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_5` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_5` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_5` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_5` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_5` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_5` | Sale price of owned property | `Numeric(Double)` | `%10.0g` |
| `sl_ac024c_5` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_6` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_6` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac007_6` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_6` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_6` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_6` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_6` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_6` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_6` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_6` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_6` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_6_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_6` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_6` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_6` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_6` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_6` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_6` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_6` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_6` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_6` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_6` | Price of owned property | `Numeric(Double)` | `%10.0g` |
| `sl_ac020c_6` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_6` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_6` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_6` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_6` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_6` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_6` | Sale price of owned property | `Numeric(Double)` | `%10.0g` |
| `sl_ac024c_6` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_7` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_7` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac007_7` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_7` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_7` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_7` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_7` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_7` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_7` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_7` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_7` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_7_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_7` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_7` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_7` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_7` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_7` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_7` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_7` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_7` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_7` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_7` | Price of owned property | `Numeric(Double)` | `%10.0g` |
| `sl_ac020c_7` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_7` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_7` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_7` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_7` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_7` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_7` | Sale price of owned property | `Numeric(Long)` | `%12.0g` |
| `sl_ac024c_7` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_8` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_8` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac007_8` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_8` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_8` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_8` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_8` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_8` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_8` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_8` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_8` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_8_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_8` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_8` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_8` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_8` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_8` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_8` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_8` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_8` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_8` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_8` | Price of owned property | `Numeric(Double)` | `%10.0g` |
| `sl_ac020c_8` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_8` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_8` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_8` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_8` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_8` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_8` | Sale price of owned property | `Numeric(Double)` | `%12.0g` |
| `sl_ac024c_8` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_9` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_9` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac007_9` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_9` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_9` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_9` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_9` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_9` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_9` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_9` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_9` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_9_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_9` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_9` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_9` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_9` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_9` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_9` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_9` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_9` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_9` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_9` | Price of owned property | `Numeric(Double)` | `%10.0g` |
| `sl_ac020c_9` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_9` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_9` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_9` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_9` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_9` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_9` | Sale price of owned property | `Numeric(Long)` | `%12.0g` |
| `sl_ac024c_9` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_10` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_10` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac007_10` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_10` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_10` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_10` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_10` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_10` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_10` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_10` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_10` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_10_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_10` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_10` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_10` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_10` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_10` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_10` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_10` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_10` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_10` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_10` | Price of owned property | `Numeric(Double)` | `%12.0g` |
| `sl_ac020c_10` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_10` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_10` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_10` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_10` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_10` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_10` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_10` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_11` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_11` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac007_11` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_11` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_11` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_11` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_11` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_11` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_11` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_11` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_11` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_11_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_11` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_11` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_11` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_11` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_11` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_11` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_11` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_11` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_11` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_11` | Price of owned property | `Numeric(Long)` | `%12.0g` |
| `sl_ac020c_11` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_11` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_11` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_11` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_11` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_11` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_11` | Sale price of owned property | `Numeric(Double)` | `%10.0g` |
| `sl_ac024c_11` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_12` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_12` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac007_12` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_12` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_12` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_12` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_12` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_12` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_12` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_12` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_12` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_12_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_12` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_12` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_12` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_12` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_12` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_12` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_12` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_12` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_12` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_12` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_12` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_12` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_12` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_12` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_12` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_12` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_12` | Sale price of owned property | `Numeric(Long)` | `%12.0g` |
| `sl_ac024c_12` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_13` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_13` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_13` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_13` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_13` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_13` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_13` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_13` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_13` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_13` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_13_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_13` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_13` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_13` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_13` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_13` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_13` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_13` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_13` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_13` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_13` | Price of owned property | `Numeric(Long)` | `%12.0g` |
| `sl_ac020c_13` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_13` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_13` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_13` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_13` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_13` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_13` | Sale price of owned property | `Numeric(Long)` | `%12.0g` |
| `sl_ac024c_13` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_14` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_14` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac007_14` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_14` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_14` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_14` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_14` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_14` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_14` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_14` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_14` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_14_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_14` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_14` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_14` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_14` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_14` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_14` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_14` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_14` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_14` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_14` | Price of owned property | `Numeric(Double)` | `%10.0g` |
| `sl_ac020c_14` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_14` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_14` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_14` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_14` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_14` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_14` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_14` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_15` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_15` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_15` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_15` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_15` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_15` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_15` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_15` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_15` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_15` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_15_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_15` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_15` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_15` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_15` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_15` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_15` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_15` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_15` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_15` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_15` | Price of owned property | `Numeric(Double)` | `%12.0g` |
| `sl_ac020c_15` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_15` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_15` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_15` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_15` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_15` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_15` | Sale price of owned property | `Numeric(Double)` | `%10.0g` |
| `sl_ac024c_15` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_16` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_16` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_16` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_16` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_16` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_16` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_16` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_16` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_16` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_16` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_16_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_16` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_16` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_16` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_16` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_16` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_16` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_16` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_16` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_16` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_16` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_16` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_16` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_16` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_16` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_16` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_16` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_16` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_16` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_17` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_17` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac007_17` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_17` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_17` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_17` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_17` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac012c_17` | Specify other: none-private residence - coded | `Numeric(Byte)` | `%30.0g` |
| `sl_ac013_17` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_17` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_17` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_17_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_17` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_17` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_17` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_17` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_17` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_17` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_17` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_17` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_17` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_17` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_17` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_17` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_17` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_17` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_17` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_17` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_17` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_17` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_18` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_18` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac007_18` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_18` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_18` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_18` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_18` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac013_18` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_18` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_18` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_18_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_18` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_18` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_18` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_18` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_18` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_18` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_18` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_18` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_18` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_18` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_18` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_18` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_18` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_18` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_18` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_18` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_18` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_18` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_19` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_19` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac007_19` | Estimated start year of accommodation | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_19` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_19` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_19` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac011_19` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac013_19` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_19` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_19` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_19_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_19` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_19` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_19` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_19` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_19` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_19` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_19` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_19` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_19` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_19` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_19` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_19` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_19` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_19` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_19` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_19` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_19` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_19` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_20` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_20` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_20` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_20` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_20` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac013_20` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_20` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_20` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_20_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_20` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_20` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_20` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_20` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_20` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_20` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_20` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_20` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_20` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_20` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_20` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_20` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_20` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022a_20` | Still own property | `Numeric(Byte)` | `%10.0g` |
| `sl_ac022b_20` | Do with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac022c_20` | When sell property | `Numeric(Int)` | `%10.0g` |
| `sl_ac023_20` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_20` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_21` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_21` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_21` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_21` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac013_21` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac015_21` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_21` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_21` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_21` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_21` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_21` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_21` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_21` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_21` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_21` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_21` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_21` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_21` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac023_21` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_21` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_22` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_22` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_22` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_22` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac010c_22` | Specify other: private residence - coded | `Numeric(Byte)` | `%34.0g` |
| `sl_ac013_22` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_22` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_22` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_22_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_22` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_22` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_22` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_22` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_22` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_22` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_22` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_22` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_22` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_22` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_22` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_22` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_22` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac023_22` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_22` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_23` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_23` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_23` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_23` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac013_23` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_23` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_23` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_23_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_23` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_23` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_23` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_23` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_23` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_23` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_23` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_23` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_23` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_23` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_23` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_23` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_23` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac023_23` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_23` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_24` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_24` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_24` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_24` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac013_24` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac014_24` | Country of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac014c_24` | Country of residence (not current) - coded | `Numeric(Byte)` | `%37.0g` |
| `sl_ac014c_24_iso` | Country of residence (not current) - ISO coded | `Numeric(Int)` | `%46.0g` |
| `sl_ac015_24` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_24` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_24` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_24` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_24` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_24` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_24` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_24` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_24` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_24` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_24` | Currency of owned property - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac021_24` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_24` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac023_24` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_24` | Sale currency of owned property  - coded | `Numeric(Int)` | `%63.0g` |
| `sl_ac005_25` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_25` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_25` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_25` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac013_25` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac015_25` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_25` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_25` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_25` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_25` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_25` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_25` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_25` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_25` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_25` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_25` | Currency of owned property - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_ac021_25` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_25` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac005_26` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_26` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_26` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_26` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac013_26` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac015_26` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_26` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_26` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_26` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_26` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_26` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_26` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_26` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_26` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_26` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_26` | Currency of owned property - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_ac021_26` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_26` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac023_26` | Sale price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac024c_26` | Sale currency of owned property  - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_ac005_27` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_27` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_27` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_27` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac013_27` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac015_27` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_27` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_27` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_27` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_27` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_27` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_27` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_27` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_27` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_27` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_27` | Currency of owned property - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_ac021_27` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_27` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac005_28` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_28` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_28` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_28` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac011_28` | Type of non-private residence | `Numeric(Byte)` | `%43.0g` |
| `sl_ac013_28` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac015_28` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_28` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_28` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_28` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_28` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_28` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_28` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_28` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_28` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac019_28` | Price of owned property | `Numeric(Long)` | `%10.0g` |
| `sl_ac020c_28` | Currency of owned property - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_ac021_28` | Stopped living at residence | `Numeric(Int)` | `%25.0g` |
| `sl_ac022_28` | What done with property | `Numeric(Byte)` | `%28.0g` |
| `sl_ac005_29` | Short term living | `Numeric(Byte)` | `%10.0g` |
| `sl_ac006_29` | Start living at residence | `Numeric(Int)` | `%10.0g` |
| `sl_ac008_29` | Type of residence | `Numeric(Byte)` | `%10.0g` |
| `sl_ac009_29` | Type of private residence | `Numeric(Byte)` | `%24.0g` |
| `sl_ac013_29` | Was residence in current country | `Numeric(Byte)` | `%10.0g` |
| `sl_ac015_29` | Region of residence (not current) | `Numeric(Byte)` | `%29.0g` |
| `sl_ac015c_29` | Region of residence (not current) - coded | `Numeric(Int)` | `%83.0g` |
| `sl_ac017_29` | Area of residence | `Numeric(Byte)` | `%38.0g` |
| `sl_ac018d1_29` | Property: purchased/built with own means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d2_29` | Property: purchased/built with mortgage | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d3_29` | Property: purchased/built with help from family | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d4_29` | Property: received as bequest | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d5_29` | Property: received as gift | `Numeric(Byte)` | `%12.0g` |
| `sl_ac018d6_29` | Property: acquired through other means | `Numeric(Byte)` | `%12.0g` |
| `sl_ac027_` | Proxy check | `Numeric(Byte)` | `%20.0g` |
| `sl_ac020_2_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Int)` | `%22.0g` |
| `sl_ac020_3_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Int)` | `%22.0g` |
| `sl_ac020_4_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Float)` | `%22.0g` |
| `sl_ac020_5_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Float)` | `%22.0g` |
| `sl_ac020_6_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Int)` | `%22.0g` |
| `sl_ac020_7_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Float)` | `%22.0g` |
| `sl_ac020_10_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Int)` | `%22.0g` |
| `sl_ac020_11_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_ac020_12_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_ac020_13_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Float)` | `%22.0g` |
| `sl_ac024_2_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_ac024_3_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_ac024_4_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Int)` | `%22.0g` |
| `sl_ac024_5_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_ac024_6_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Int)` | `%22.0g` |
| `sl_ac024_7_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_ac024_10_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Int)` | `%22.0g` |
| `sl_ac008_1_flag` | ac008_1 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_1_flag` | ac009_1 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_1_flag` | ac010c_1 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_1_flag` | ac011_1 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_1_flag` | ac012c_1 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_2_flag` | ac008_2 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_2_flag` | ac009_2 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_2_flag` | ac010c_2 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_2_flag` | ac011_2 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_2_flag` | ac012c_2 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_3_flag` | ac008_3 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_3_flag` | ac009_3 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_3_flag` | ac010c_3 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_3_flag` | ac011_3 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_3_flag` | ac012c_3 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_4_flag` | ac008_4 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_4_flag` | ac009_4 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_4_flag` | ac010c_4 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_4_flag` | ac011_4 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_4_flag` | ac012c_4 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_5_flag` | ac008_5 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_5_flag` | ac009_5 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_5_flag` | ac010c_5 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_5_flag` | ac011_5 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_5_flag` | ac012c_5 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_6_flag` | ac008_6 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_6_flag` | ac009_6 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_6_flag` | ac010c_6 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_6_flag` | ac011_6 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_6_flag` | ac012c_6 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_7_flag` | ac008_7 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_7_flag` | ac009_7 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_7_flag` | ac010c_7 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_7_flag` | ac011_7 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_7_flag` | ac012c_7 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_8_flag` | ac008_8 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_8_flag` | ac009_8 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_8_flag` | ac010c_8 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_8_flag` | ac011_8 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_8_flag` | ac012c_8 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_9_flag` | ac008_9 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_9_flag` | ac009_9 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_9_flag` | ac010c_9 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_9_flag` | ac011_9 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_9_flag` | ac012c_9 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_10_flag` | ac008_10 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_10_flag` | ac009_10 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_10_flag` | ac010c_10 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_10_flag` | ac011_10 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_10_flag` | ac012c_10 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_11_flag` | ac008_11 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_11_flag` | ac009_11 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_11_flag` | ac010c_11 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_11_flag` | ac011_11 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_11_flag` | ac012c_11 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_12_flag` | ac008_12 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_12_flag` | ac009_12 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_12_flag` | ac010c_12 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_12_flag` | ac011_12 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_12_flag` | ac012c_12 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_13_flag` | ac008_13 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_13_flag` | ac009_13 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_13_flag` | ac010c_13 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_13_flag` | ac011_13 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_13_flag` | ac012c_13 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_14_flag` | ac008_14 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_14_flag` | ac009_14 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_14_flag` | ac010c_14 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_14_flag` | ac011_14 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_14_flag` | ac012c_14 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_15_flag` | ac008_15 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_15_flag` | ac009_15 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_15_flag` | ac010c_15 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_15_flag` | ac011_15 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_15_flag` | ac012c_15 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_16_flag` | ac008_16 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_16_flag` | ac009_16 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_16_flag` | ac010c_16 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_16_flag` | ac011_16 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_16_flag` | ac012c_16 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_17_flag` | ac008_17 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_17_flag` | ac009_17 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_17_flag` | ac010c_17 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_17_flag` | ac011_17 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_17_flag` | ac012c_17 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_18_flag` | ac008_18 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_18_flag` | ac009_18 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_18_flag` | ac010c_18 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_18_flag` | ac011_18 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_18_flag` | ac012c_18 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_19_flag` | ac008_19 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_19_flag` | ac009_19 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_19_flag` | ac010c_19 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_19_flag` | ac011_19 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_19_flag` | ac012c_19 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_20_flag` | ac008_20 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_20_flag` | ac009_20 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_20_flag` | ac010c_20 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_20_flag` | ac011_20 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_20_flag` | ac012c_20 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_21_flag` | ac008_21 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_21_flag` | ac009_21 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_21_flag` | ac010c_21 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_21_flag` | ac011_21 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_21_flag` | ac012c_21 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac008_22_flag` | ac008_22 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac009_22_flag` | ac009_22 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac010c_22_flag` | ac010c_22 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac011_22_flag` | ac011_22 modified due to 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |
| `sl_ac012c_22_flag` | ac012c_22 code generated from 'other/specify' information? | `Numeric(Byte)` | `%31.0g` |

### `cs` - Childhood Section

- Dataset: `sharew3_rel9-0-0_cs.dta`
- Read with: `ps.read_share_module("cs", wave=3)`
- Rows: 28,454
- Variables: 28
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sl_cs002_` | Rooms when ten years old | `Numeric(Byte)` | `%10.0g` |
| `sl_cs003_` | Number of people living in household when ten | `Numeric(Int)` | `%10.0g` |
| `sl_cs004d1` | Lived in hh when ten: biological mother | `Numeric(Byte)` | `%12.0g` |
| `sl_cs004d2` | Lived in hh when ten: biological father | `Numeric(Byte)` | `%12.0g` |
| `sl_cs004d3` | Lived in hh when ten: adoptive/step/foster mother | `Numeric(Byte)` | `%12.0g` |
| `sl_cs004d4` | Lived in hh when ten: adoptive/step/foster father | `Numeric(Byte)` | `%12.0g` |
| `sl_cs004d5` | Lived in hh when ten: biological sibling(s) | `Numeric(Byte)` | `%12.0g` |
| `sl_cs004d6` | Lived in hh when ten: adoptive/step/foster/half sibling(s) | `Numeric(Byte)` | `%12.0g` |
| `sl_cs004d7` | Lived in hh when ten: grandparent(s) | `Numeric(Byte)` | `%12.0g` |
| `sl_cs004d8` | Lived in hh when ten: other relative(s) | `Numeric(Byte)` | `%12.0g` |
| `sl_cs004d9` | Lived in hh when ten: other non-relative(s) | `Numeric(Byte)` | `%12.0g` |
| `sl_cs007d1` | Features of accommodation when ten: fixed bath | `Numeric(Byte)` | `%12.0g` |
| `sl_cs007d2` | Features of accommodation when ten: cold running water supply | `Numeric(Byte)` | `%12.0g` |
| `sl_cs007d3` | Features of accommodation when ten: hot running water supply | `Numeric(Byte)` | `%12.0g` |
| `sl_cs007d4` | Features of accommodation when ten: inside toilet | `Numeric(Byte)` | `%12.0g` |
| `sl_cs007d5` | Features of accommodation when ten: central heating | `Numeric(Byte)` | `%12.0g` |
| `sl_cs007dno` | Features of accommodation when ten: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_cs008_` | Number of books when ten | `Numeric(Byte)` | `%58.0g` |
| `sl_cs009_` | Occupation of main breadwinner when ten | `Numeric(Byte)` | `%47.0g` |
| `sl_cs010_` | Relative position to others when ten: mathematically | `Numeric(Byte)` | `%36.0g` |
| `sl_cs010a_` | Relative position to others when ten: language | `Numeric(Byte)` | `%36.0g` |
| `sl_cs012_` | Proxy check | `Numeric(Byte)` | `%20.0g` |

### `dq` - Disability

- Dataset: `sharew3_rel9-0-0_dq.dta`
- Read with: `ps.read_share_module("dq", wave=3)`
- Rows: 28,454
- Variables: 177
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sl_dq001_` | Ever left job because of disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq002d1` | Left which job because of disability: job 1 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d2` | Left which job because of disability: job 2 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d3` | Left which job because of disability: job 3 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d4` | Left which job because of disability: job 4 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d5` | Left which job because of disability: job 5 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d6` | Left which job because of disability: job 6 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d7` | Left which job because of disability: job 7 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d8` | Left which job because of disability: job 8 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d9` | Left which job because of disability: job 9 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d10` | Left which job because of disability: job 10 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d11` | Left which job because of disability: job 11 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d12` | Left which job because of disability: job 12 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d13` | Left which job because of disability: job 13 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d14` | Left which job because of disability: job 14 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d15` | Left which job because of disability: job 15 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d16` | Left which job because of disability: job 16 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq002d17` | Left which job because of disability: job 17 | `Numeric(Byte)` | `%12.0g` |
| `sl_dq003_1` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq005_1` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `sl_dq003_2` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq005_2` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `sl_dq003_3` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq005_3` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `sl_dq003_4` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq005_4` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `sl_dq003_5` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq005_5` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `sl_dq003_6` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq005_6` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `sl_dq003_7` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq005_7` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `sl_dq003_8` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq005_8` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `sl_dq003_9` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq005_9` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `sl_dq003_10` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq005_10` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `sl_dq003_11` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq005_11` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `sl_dq003_12` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq005_12` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `sl_dq003_13` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq003_14` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq003_15` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq005_15` | Found job suitable for limitation | `Numeric(Byte)` | `%10.0g` |
| `sl_dq003_16` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq003_20` | Extent of limitation | `Numeric(Byte)` | `%24.0g` |
| `sl_dq007_` | Took temporary leave of absence for disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq008_1` | Temp leave which job because of disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq009_1` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `sl_dq010_1` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `sl_dq011d1_1` | Income during gap after leaving job 1: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d2_1` | Income during gap after leaving job 1: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d3_1` | Income during gap after leaving job 1: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d4_1` | Income during gap after leaving job 1: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d5_1` | Income during gap after leaving job 1: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d6_1` | Income during gap after leaving job 1: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011dot_1` | Income during gap after leaving job 1: other | `Numeric(Byte)` | `%12.0g` |
| `sl_dq012_1` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq008_2` | Temp leave which job because of disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq009_2` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `sl_dq010_2` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `sl_dq011d1_2` | Income during gap after leaving job 2: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d2_2` | Income during gap after leaving job 2: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d3_2` | Income during gap after leaving job 2: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d4_2` | Income during gap after leaving job 2: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d5_2` | Income during gap after leaving job 2: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d6_2` | Income during gap after leaving job 2: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011dot_2` | Income during gap after leaving job 2: other | `Numeric(Byte)` | `%12.0g` |
| `sl_dq012_2` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq008_3` | Temp leave which job because of disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq009_3` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `sl_dq010_3` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `sl_dq011d1_3` | Income during gap after leaving job 3: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d2_3` | Income during gap after leaving job 3: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d3_3` | Income during gap after leaving job 3: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d4_3` | Income during gap after leaving job 3: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d5_3` | Income during gap after leaving job 3: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d6_3` | Income during gap after leaving job 3: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011dot_3` | Income during gap after leaving job 3: other | `Numeric(Byte)` | `%12.0g` |
| `sl_dq012_3` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq008_4` | Temp leave which job because of disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq009_4` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `sl_dq010_4` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `sl_dq011d1_4` | Income during gap after leaving job 4: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d2_4` | Income during gap after leaving job 4: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d3_4` | Income during gap after leaving job 4: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d4_4` | Income during gap after leaving job 4: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d5_4` | Income during gap after leaving job 4: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d6_4` | Income during gap after leaving job 4: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011dot_4` | Income during gap after leaving job 4: other | `Numeric(Byte)` | `%12.0g` |
| `sl_dq012_4` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq008_5` | Temp leave which job because of disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq009_5` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `sl_dq010_5` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `sl_dq011d1_5` | Income during gap after leaving job 5: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d2_5` | Income during gap after leaving job 5: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d3_5` | Income during gap after leaving job 5: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d4_5` | Income during gap after leaving job 5: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d5_5` | Income during gap after leaving job 5: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d6_5` | Income during gap after leaving job 5: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011dot_5` | Income during gap after leaving job 5: other | `Numeric(Byte)` | `%12.0g` |
| `sl_dq012_5` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq008_6` | Temp leave which job because of disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq009_6` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `sl_dq010_6` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `sl_dq011d1_6` | Income during gap after leaving job 6: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d2_6` | Income during gap after leaving job 6: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d3_6` | Income during gap after leaving job 6: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d4_6` | Income during gap after leaving job 6: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d5_6` | Income during gap after leaving job 6: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d6_6` | Income during gap after leaving job 6: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011dot_6` | Income during gap after leaving job 6: other | `Numeric(Byte)` | `%12.0g` |
| `sl_dq012_6` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq008_7` | Temp leave which job because of disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq009_7` | When took leave for disability | `Numeric(Int)` | `%10.0g` |
| `sl_dq010_7` | How long lasted leave for disability | `Numeric(Byte)` | `%29.0g` |
| `sl_dq011d1_7` | Income during gap after leaving job 7: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d2_7` | Income during gap after leaving job 7: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d3_7` | Income during gap after leaving job 7: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d4_7` | Income during gap after leaving job 7: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d5_7` | Income during gap after leaving job 7: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011d6_7` | Income during gap after leaving job 7: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_dq011dot_7` | Income during gap after leaving job 7: other | `Numeric(Byte)` | `%12.0g` |
| `sl_dq012_7` | Other temp leaves for disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq013_` | Ever limited hours because of disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq014_1` | Left which job because of disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq015_1` | Reduction extent of hours | `Numeric(Byte)` | `%10.0g` |
| `sl_dq016_1` | Other jobs reduce hours for disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq014_2` | Left which job because of disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq015_2` | Reduction extent of hours | `Numeric(Byte)` | `%10.0g` |
| `sl_dq016_2` | Other jobs reduce hours for disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq014_3` | Left which job because of disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq015_3` | Reduction extent of hours | `Numeric(Byte)` | `%10.0g` |
| `sl_dq016_3` | Other jobs reduce hours for disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq014_4` | Left which job because of disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq015_4` | Reduction extent of hours | `Numeric(Byte)` | `%10.0g` |
| `sl_dq016_4` | Other jobs reduce hours for disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq014_5` | Left which job because of disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq015_5` | Reduction extent of hours | `Numeric(Byte)` | `%10.0g` |
| `sl_dq016_5` | Other jobs reduce hours for disability | `Numeric(Byte)` | `%10.0g` |
| `sl_dq017_` | Ever applied for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `sl_dq018_1` | When apply for public disability pension | `Numeric(Int)` | `%12.0g` |
| `sl_dq019_1` | Was public disability pension granted | `Numeric(Byte)` | `%13.0g` |
| `sl_dq020_1` | Ever again apply for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `sl_dq018_2` | When apply for public disability pension | `Numeric(Int)` | `%10.0g` |
| `sl_dq019_2` | Was public disability pension granted | `Numeric(Byte)` | `%13.0g` |
| `sl_dq020_2` | Ever again apply for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `sl_dq018_3` | When apply for public disability pension | `Numeric(Int)` | `%10.0g` |
| `sl_dq019_3` | Was public disability pension granted | `Numeric(Byte)` | `%13.0g` |
| `sl_dq020_3` | Ever again apply for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `sl_dq018_4` | When apply for public disability pension | `Numeric(Int)` | `%10.0g` |
| `sl_dq019_4` | Was public disability pension granted | `Numeric(Byte)` | `%13.0g` |
| `sl_dq020_4` | Ever again apply for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `sl_dq018_5` | When apply for public disability pension | `Numeric(Int)` | `%10.0g` |
| `sl_dq019_5` | Was public disability pension granted | `Numeric(Byte)` | `%13.0g` |
| `sl_dq020_5` | Ever again apply for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `sl_dq018_6` | When apply for public disability pension | `Numeric(Int)` | `%10.0g` |
| `sl_dq019_6` | Was public disability pension granted | `Numeric(Byte)` | `%13.0g` |
| `sl_dq020_6` | Ever again apply for public disability pension | `Numeric(Byte)` | `%10.0g` |
| `sl_dq018_7` | When apply for public disability pension | `Numeric(Int)` | `%10.0g` |
| `sl_dq019_7` | Was public disability pension granted | `Numeric(Byte)` | `%13.0g` |
| `sl_dq021a_` | Ever purchased private disability insurance | `Numeric(Byte)` | `%10.0g` |
| `sl_dq021_` | Ever applied for private disability insurance | `Numeric(Byte)` | `%10.0g` |
| `sl_dq022_1` | When apply for private disability insurance | `Numeric(Int)` | `%10.0g` |
| `sl_dq023_1` | Was private disability insurance granted | `Numeric(Byte)` | `%13.0g` |
| `sl_dq024_1` | Ever again apply for private disability insurance | `Numeric(Byte)` | `%10.0g` |
| `sl_dq022_2` | When apply for private disability insurance | `Numeric(Int)` | `%10.0g` |
| `sl_dq023_2` | Was private disability insurance granted | `Numeric(Byte)` | `%13.0g` |
| `sl_dq024_2` | Ever again apply for private disability insurance | `Numeric(Byte)` | `%10.0g` |

### `fs` - Financial Section

- Dataset: `sharew3_rel9-0-0_fs.dta`
- Read with: `ps.read_share_module("fs", wave=3)`
- Rows: 28,454
- Variables: 19
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `exrate` | Exchange rate 1 euro | `Numeric(Double)` | `%10.0g` |
| `sl_fs002_` | Ever had any stocks or shares | `Numeric(Byte)` | `%10.0g` |
| `sl_fs003_` | When invested in stocks first | `Numeric(Int)` | `%12.0g` |
| `sl_fs004_` | Ever had any mutual funds | `Numeric(Byte)` | `%10.0g` |
| `sl_fs005_` | When invested in mutual funds first | `Numeric(Int)` | `%12.0g` |
| `sl_fs006_` | Ever had retirement account | `Numeric(Byte)` | `%10.0g` |
| `sl_fs007_` | When subscribed to retirement account first | `Numeric(Int)` | `%12.0g` |
| `sl_fs008_` | Ever taken out a life insurance policy | `Numeric(Byte)` | `%10.0g` |
| `sl_fs009_` | When taken out a life insurance policy first | `Numeric(Int)` | `%12.0g` |
| `sl_fs010_` | Ever owned business | `Numeric(Byte)` | `%10.0g` |
| `sl_fs011_` | When first owned business | `Numeric(Int)` | `%12.0g` |
| `sl_hh017e` | Total household net income in average month | `Numeric(Double)` | `%10.0g` |
| `sl_fs013_` | Proxy check | `Numeric(Byte)` | `%20.0g` |

### `gl` - General Life and Persecution

- Dataset: `sharew3_rel9-0-0_gl.dta`
- Read with: `ps.read_share_module("gl", wave=3)`
- Rows: 28,454
- Variables: 90
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sl_gl002_` | Period of happiness | `Numeric(Byte)` | `%10.0g` |
| `sl_gl003_` | When happiness period started | `Numeric(Int)` | `%10.0g` |
| `sl_gl004_` | When happiness period stopped | `Numeric(Int)` | `%21.0g` |
| `sl_gl005_` | Period of stress | `Numeric(Byte)` | `%10.0g` |
| `sl_gl006_` | When stress period started | `Numeric(Int)` | `%12.0g` |
| `sl_gl007_` | When stress period stopped | `Numeric(Int)` | `%21.0g` |
| `sl_gl008_` | Period of poor health | `Numeric(Byte)` | `%10.0g` |
| `sl_gl009_` | When poor health period started | `Numeric(Int)` | `%10.0g` |
| `sl_gl010_` | When poor health period stopped | `Numeric(Int)` | `%21.0g` |
| `sl_gl011_` | Period of financial hardship | `Numeric(Byte)` | `%10.0g` |
| `sl_gl012_` | When financial hardship period started | `Numeric(Int)` | `%12.0g` |
| `sl_gl013_` | When financial hardship period stopped | `Numeric(Int)` | `%21.0g` |
| `sl_gl014_` | Period of hunger | `Numeric(Byte)` | `%10.0g` |
| `sl_gl015_` | When hunger period started | `Numeric(Int)` | `%10.0g` |
| `sl_gl016_` | When hunger period stopped | `Numeric(Int)` | `%21.0g` |
| `sl_gl018_` | Anything else that has happened | `Numeric(Byte)` | `%10.0g` |
| `sl_gl022_` | Discriminated against | `Numeric(Byte)` | `%10.0g` |
| `sl_gl023_` | Main reason of persecution | `Numeric(Byte)` | `%45.0g` |
| `sl_gl024_` | Forced to stop working | `Numeric(Byte)` | `%10.0g` |
| `sl_gl025d1` | Stopped jobs because of persecution: job 1 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl025d2` | Stopped jobs because of persecution: job 2 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl025d3` | Stopped jobs because of persecution: job 3 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl025d4` | Stopped jobs because of persecution: job 4 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl025d5` | Stopped jobs because of persecution: job 5 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl025d6` | Stopped jobs because of persecution: job 6 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl025d7` | Stopped jobs because of persecution: job 7 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl025d8` | Stopped jobs because of persecution: job 8 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl025d9` | Stopped jobs because of persecution: job 9 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl025d10` | Stopped jobs because of persecution: job 10 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl025d11` | Stopped jobs because of persecution: job 11 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl025d12` | Stopped jobs because of persecution: job 12 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl025d13` | Stopped jobs because of persecution: job 13 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl026d1` | Experiences in job: denied promotions | `Numeric(Byte)` | `%12.0g` |
| `sl_gl026d2` | Experiences in job: assignment to a task with fewer responsibilities | `Numeric(Byte)` | `%12.0g` |
| `sl_gl026d3` | Experiences in job: working on tasks below your qualifications | `Numeric(Byte)` | `%12.0g` |
| `sl_gl026d4` | Experiences in job: harassment by your boss or colleagues | `Numeric(Byte)` | `%12.0g` |
| `sl_gl026d5` | Experiences in job: pay cuts | `Numeric(Byte)` | `%12.0g` |
| `sl_gl026dno` | Experiences in job: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_gl027d1` | Which jobs consequence of persecution: job 1 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl027d2` | Which jobs consequence of persecution: job 2 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl027d3` | Which jobs consequence of persecution: job 3 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl027d4` | Which jobs consequence of persecution: job 4 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl027d5` | Which jobs consequence of persecution: job 5 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl027d6` | Which jobs consequence of persecution: job 6 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl027d7` | Which jobs consequence of persecution: job 7 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl027d8` | Which jobs consequence of persecution: job 8 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl027d9` | Which jobs consequence of persecution: job 9 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl027d10` | Which jobs consequence of persecution: job 10 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl027d11` | Which jobs consequence of persecution: job 11 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl027d12` | Which jobs consequence of persecution: job 12 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl027d13` | Which jobs consequence of persecution: job 13 | `Numeric(Byte)` | `%12.0g` |
| `sl_gl028_` | Difficulties finding a job because of reason for persecution | `Numeric(Byte)` | `%10.0g` |
| `sl_gl029_` | First experience difficulties finding a job | `Numeric(Int)` | `%10.0g` |
| `sl_gl031_` | Dispossessed because of reason for persecution | `Numeric(Byte)` | `%10.0g` |
| `sl_gl030_1` | In prison because of reason for persecution | `Numeric(Byte)` | `%10.0g` |
| `sl_gl030_2` | In prisoner of war camp because of reason for persecution | `Numeric(Byte)` | `%10.0g` |
| `sl_gl030_3` | In labor camp because of reason for persecution | `Numeric(Byte)` | `%10.0g` |
| `sl_gl030_4` | In concentration camp because of reason for persecution | `Numeric(Byte)` | `%10.0g` |
| `sl_gl030_5` | Forced labor/jail because of reason for persecution | `Numeric(Byte)` | `%10.0g` |
| `sl_gl033_1` | When property taken away | `Numeric(Int)` | `%12.0g` |
| `sl_gl032d1_1` | Type of property: businesses or companies | `Numeric(Byte)` | `%12.0g` |
| `sl_gl032d2_1` | Type of property: houses or buildings | `Numeric(Byte)` | `%12.0g` |
| `sl_gl032d3_1` | Type of property: farmland or other land | `Numeric(Byte)` | `%12.0g` |
| `sl_gl032d4_1` | Type of property: flat or apartment | `Numeric(Byte)` | `%12.0g` |
| `sl_gl032d5_1` | Type of property: money or assets | `Numeric(Byte)` | `%12.0g` |
| `sl_gl034_1` | Compensated | `Numeric(Byte)` | `%14.0g` |
| `sl_gl035_1` | Another time dispossessed of any property | `Numeric(Byte)` | `%10.0g` |
| `sl_gl033_2` | When property taken away | `Numeric(Int)` | `%10.0g` |
| `sl_gl032d1_2` | Type of property: businesses or companies | `Numeric(Byte)` | `%12.0g` |
| `sl_gl032d2_2` | Type of property: houses or buildings | `Numeric(Byte)` | `%12.0g` |
| `sl_gl032d3_2` | Type of property: farmland or other land | `Numeric(Byte)` | `%12.0g` |
| `sl_gl032d4_2` | Type of property: flat or apartment | `Numeric(Byte)` | `%12.0g` |
| `sl_gl032d5_2` | Type of property: money or assets | `Numeric(Byte)` | `%12.0g` |
| `sl_gl034_2` | Compensated | `Numeric(Byte)` | `%14.0g` |
| `sl_gl035_2` | Another time dispossessed of any property | `Numeric(Byte)` | `%10.0g` |
| `sl_gl033_3` | When property taken away | `Numeric(Int)` | `%10.0g` |
| `sl_gl032d1_3` | Type of property: businesses or companies | `Numeric(Byte)` | `%12.0g` |
| `sl_gl032d2_3` | Type of property: houses or buildings | `Numeric(Byte)` | `%12.0g` |
| `sl_gl032d3_3` | Type of property: farmland or other land | `Numeric(Byte)` | `%12.0g` |
| `sl_gl032d4_3` | Type of property: flat or apartment | `Numeric(Byte)` | `%12.0g` |
| `sl_gl032d5_3` | Type of property: money or assets | `Numeric(Byte)` | `%12.0g` |
| `sl_gl034_3` | Compensated | `Numeric(Byte)` | `%14.0g` |
| `sl_gl035_3` | Another time dispossessed of any property | `Numeric(Byte)` | `%10.0g` |
| `sl_gl036_` | Proxy check | `Numeric(Byte)` | `%20.0g` |

### `hc` - Retrospective Health Care

- Dataset: `sharew3_rel9-0-0_hc.dta`
- Read with: `ps.read_share_module("hc", wave=3)`
- Rows: 28,454
- Variables: 179
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sl_hc002_` | Vaccinations during childhood | `Numeric(Byte)` | `%10.0g` |
| `sl_hc003d1` | Why no childhood vaccinations: not affordable | `Numeric(Byte)` | `%12.0g` |
| `sl_hc003d2` | Why no childhood vaccinations: not covered by health insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_hc003d3` | Why no childhood vaccinations: did not have health insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_hc003d4` | Why no childhood vaccinations: time constraints | `Numeric(Byte)` | `%12.0g` |
| `sl_hc003d5` | Why no childhood vaccinations: not enough information about it | `Numeric(Byte)` | `%12.0g` |
| `sl_hc003d6` | Why no childhood vaccinations: not usual to get it | `Numeric(Byte)` | `%12.0g` |
| `sl_hc003d7` | Why no childhood vaccinations: no place to receive it close to home | `Numeric(Byte)` | `%12.0g` |
| `sl_hc003d8` | Why no childhood vaccinations: not considered to be necessary | `Numeric(Byte)` | `%12.0g` |
| `sl_hc003dot` | Why no childhood vaccinations: other reasons | `Numeric(Byte)` | `%12.0g` |
| `sl_hc005_` | Usual source of care | `Numeric(Byte)` | `%10.0g` |
| `sl_hc005ad1` | No usual source of care: when between 0-15 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc005ad2` | No usual source of care: when between 16-25 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc005ad3` | No usual source of care: when between 26-40 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc005ad4` | No usual source of care: when between 41-55 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc005ad5` | No usual source of care: when between 56-65 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc005ad6` | No usual source of care: when between 66-75 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc005ad7` | No usual source of care: when older than 75 years | `Numeric(Byte)` | `%12.0g` |
| `sl_hc015_` | Ever regular dentist | `Numeric(Byte)` | `%10.0g` |
| `sl_hc016_` | Childhood regular dentist | `Numeric(Byte)` | `%10.0g` |
| `sl_hc017_` | Year regular dentist visits started | `Numeric(Int)` | `%12.0g` |
| `sl_hc018_` | Continuity regular dentist | `Numeric(Byte)` | `%10.0g` |
| `sl_hc018ad1` | No dental care: when between 0-15 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc018ad2` | No dental care: when between 16-25 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc018ad3` | No dental care: when between 26-40 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc018ad4` | No dental care: when between 41-55 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc018ad5` | No dental care: when between 56-65 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc018ad6` | No dental care: when between 66-75 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc018ad7` | No dental care: when older than 75 years | `Numeric(Byte)` | `%12.0g` |
| `sl_hc025_` | Frequency regular dentist | `Numeric(Byte)` | `%44.0g` |
| `sl_hc026d1` | Why no regular dental care: not affordable | `Numeric(Byte)` | `%12.0g` |
| `sl_hc026d2` | Why no regular dental care: not covered by health insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_hc026d3` | Why no regular dental care: did not have health insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_hc026d4` | Why no regular dental care: time constraints | `Numeric(Byte)` | `%12.0g` |
| `sl_hc026d5` | Why no regular dental care: not enough information about it | `Numeric(Byte)` | `%12.0g` |
| `sl_hc026d6` | Why no regular dental care: not usual to get it | `Numeric(Byte)` | `%12.0g` |
| `sl_hc026d7` | Why no regular dental care: no place to receive it close to home | `Numeric(Byte)` | `%12.0g` |
| `sl_hc026d8` | Why no regular dental care: not considered to be necessary | `Numeric(Byte)` | `%12.0g` |
| `sl_hc026dot` | Why no regular dental care: other reasons | `Numeric(Byte)` | `%12.0g` |
| `sl_hc028_` | Regular gynaecological visits | `Numeric(Byte)` | `%10.0g` |
| `sl_hc029_` | Year regular gyn visits started | `Numeric(Int)` | `%12.0g` |
| `sl_hc030_` | Continuity regular gyn visits | `Numeric(Byte)` | `%10.0g` |
| `sl_hc030ad1` | No gyn checks: when between 0-15 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc030ad2` | No gyn checks: when between 16-25 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc030ad3` | No gyn checks: when between 26-40 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc030ad4` | No gyn checks: when between 41-55 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc030ad5` | No gyn checks: when between 56-65 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc030ad6` | No gyn checks: when between 66-75 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc030ad7` | No gyn checks: when older than 75 years | `Numeric(Byte)` | `%12.0g` |
| `sl_hc037_` | Frequency regular gyn visits | `Numeric(Byte)` | `%44.0g` |
| `sl_hc038d1` | Why no regular gyn visits: not affordable | `Numeric(Byte)` | `%12.0g` |
| `sl_hc038d2` | Why no regular gyn visits: not covered by health insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_hc038d3` | Why no regular gyn visits: did not have health insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_hc038d4` | Why no regular gyn visits: time constraints | `Numeric(Byte)` | `%12.0g` |
| `sl_hc038d5` | Why no regular gyn visits: not enough information about it | `Numeric(Byte)` | `%12.0g` |
| `sl_hc038d6` | Why no regular gyn visits: not usual to get it | `Numeric(Byte)` | `%12.0g` |
| `sl_hc038d7` | Why no regular gyn visits: no place to receive it close to home | `Numeric(Byte)` | `%12.0g` |
| `sl_hc038d8` | Why no regular gyn visits: not considered to be necessary | `Numeric(Byte)` | `%12.0g` |
| `sl_hc038dot` | Why no regular gyn visits: other reasons | `Numeric(Byte)` | `%12.0g` |
| `sl_hc040_` | Regular blood pressure checks | `Numeric(Byte)` | `%10.0g` |
| `sl_hc041_` | Year regular blood pressure checks started | `Numeric(Int)` | `%12.0g` |
| `sl_hc049_` | Frequency regular blood pressure | `Numeric(Byte)` | `%44.0g` |
| `sl_hc042_` | Continuity regular blood pressure | `Numeric(Byte)` | `%10.0g` |
| `sl_hc042ad1` | No blood pressure checks: when between 0-15 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc042ad2` | No blood pressure checks: when between 16-25 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc042ad3` | No blood pressure checks: when between 26-40 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc042ad4` | No blood pressure checks: when between 41-55 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc042ad5` | No blood pressure checks: when between 56-65 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc042ad6` | No blood pressure checks: when between 66-75 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc042ad7` | No blood pressure checks: when older than 75 years | `Numeric(Byte)` | `%12.0g` |
| `sl_hc050d1` | Why no regular blood pressure checks: not affordable | `Numeric(Byte)` | `%12.0g` |
| `sl_hc050d2` | Why no regular blood pressure checks: not covered by health insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_hc050d3` | Why no regular blood pressure checks: did not have health insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_hc050d4` | Why no regular blood pressure checks: time constraints | `Numeric(Byte)` | `%12.0g` |
| `sl_hc050d5` | Why no regular blood pressure checks: not enough information about it | `Numeric(Byte)` | `%12.0g` |
| `sl_hc050d6` | Why no regular blood pressure checks: not usual to get it | `Numeric(Byte)` | `%12.0g` |
| `sl_hc050d7` | Why no regular blood pressure checks: no place to receive it close to home | `Numeric(Byte)` | `%12.0g` |
| `sl_hc050d8` | Why no regular blood pressure checks: not considered to be necessary | `Numeric(Byte)` | `%12.0g` |
| `sl_hc050dot` | Why no regular blood pressure checks: other reasons | `Numeric(Byte)` | `%12.0g` |
| `sl_hc052_` | Regular blood tests | `Numeric(Byte)` | `%10.0g` |
| `sl_hc053_` | Year regular blood tests started | `Numeric(Int)` | `%12.0g` |
| `sl_hc054_` | Continuity regular blood tests | `Numeric(Byte)` | `%10.0g` |
| `sl_hc054ad1` | No blood tests: when between 0-15 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc054ad2` | No blood tests: when between 16-25 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc054ad3` | No blood tests: when between 26-40 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc054ad4` | No blood tests: when between 41-55 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc054ad5` | No blood tests: when between 56-65 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc054ad6` | No blood tests: when between 66-75 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc054ad7` | No blood tests: when older than 75 years | `Numeric(Byte)` | `%12.0g` |
| `sl_hc061_` | Frequency regular blood tests | `Numeric(Byte)` | `%44.0g` |
| `sl_hc062d1` | Why no regular blood tests: not affordable | `Numeric(Byte)` | `%12.0g` |
| `sl_hc062d2` | Why no regular blood tests: not covered by health insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_hc062d3` | Why no regular blood tests: did not have health insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_hc062d4` | Why no regular blood tests: time constraints | `Numeric(Byte)` | `%12.0g` |
| `sl_hc062d5` | Why no regular blood tests: not enough information about it | `Numeric(Byte)` | `%12.0g` |
| `sl_hc062d6` | Why no regular blood tests: not usual to get it | `Numeric(Byte)` | `%12.0g` |
| `sl_hc062d7` | Why no regular blood tests: no place to receive it close to home | `Numeric(Byte)` | `%12.0g` |
| `sl_hc062d8` | Why no regular blood tests: not considered to be necessary | `Numeric(Byte)` | `%12.0g` |
| `sl_hc062dot` | Why no regular blood tests: other reasons | `Numeric(Byte)` | `%12.0g` |
| `sl_hc064_` | Regular mammograms | `Numeric(Byte)` | `%10.0g` |
| `sl_hc065_` | Year regular mammograms started | `Numeric(Int)` | `%12.0g` |
| `sl_hc066_` | Continuity regular mammograms | `Numeric(Byte)` | `%10.0g` |
| `sl_hc066ad1` | No mammography: when between 0-15 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc066ad2` | No mammography: when between 16-25 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc066ad3` | No mammography: when between 26-40 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc066ad4` | No mammography: when between 41-55 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc066ad5` | No mammography: when between 56-65 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc066ad6` | No mammography: when between 66-75 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc066ad7` | No mammography: when older than 75 years | `Numeric(Byte)` | `%12.0g` |
| `sl_hc073_` | Frequency regular mammograms | `Numeric(Byte)` | `%44.0g` |
| `sl_hc074d1` | Why no regular mammograms: not affordable | `Numeric(Byte)` | `%12.0g` |
| `sl_hc074d2` | Why no regular mammograms: not covered by health insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_hc074d3` | Why no regular mammograms: did not have health insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_hc074d4` | Why no regular mammograms: time constraints | `Numeric(Byte)` | `%12.0g` |
| `sl_hc074d5` | Why no regular mammograms: not enough information about it | `Numeric(Byte)` | `%12.0g` |
| `sl_hc074d6` | Why no regular mammograms: not usual to get it | `Numeric(Byte)` | `%12.0g` |
| `sl_hc074d7` | Why no regular mammograms: no place to receive it close to home | `Numeric(Byte)` | `%12.0g` |
| `sl_hc074d8` | Why no regular mammograms: not considered to be necessary | `Numeric(Byte)` | `%12.0g` |
| `sl_hc074dot` | Why no regular mammograms: other reasons | `Numeric(Byte)` | `%12.0g` |
| `sl_hc076_` | Regular vision tests | `Numeric(Byte)` | `%10.0g` |
| `sl_hc077_` | Year regular vision tests started | `Numeric(Int)` | `%12.0g` |
| `sl_hc078_` | Continuity regular vision tests | `Numeric(Byte)` | `%10.0g` |
| `sl_hc078ad1` | No vision tests: when between 0-15 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc078ad2` | No vision tests: when between 16-25 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc078ad3` | No vision tests: when between 26-40 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc078ad4` | No vision tests: when between 41-55 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc078ad5` | No vision tests: when between 56-65 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc078ad6` | No vision tests: when between 66-75 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc078ad7` | No vision tests: when older than 75 years | `Numeric(Byte)` | `%12.0g` |
| `sl_hc085_` | Frequency regular vision tests | `Numeric(Byte)` | `%44.0g` |
| `sl_hc086d1` | Why no regular vision tests: not affordable | `Numeric(Byte)` | `%12.0g` |
| `sl_hc086d2` | Why no regular vision tests: not covered by health insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_hc086d3` | Why no regular vision tests: did not have health insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_hc086d4` | Why no regular vision tests: time constraints | `Numeric(Byte)` | `%12.0g` |
| `sl_hc086d5` | Why no regular vision tests: not enough information about it | `Numeric(Byte)` | `%12.0g` |
| `sl_hc086d6` | Why no regular vision tests: not usual to get it | `Numeric(Byte)` | `%12.0g` |
| `sl_hc086d7` | Why no regular vision tests: no place to receive it close to home | `Numeric(Byte)` | `%12.0g` |
| `sl_hc086d8` | Why no regular vision tests: not considered to be necessary | `Numeric(Byte)` | `%12.0g` |
| `sl_hc086dot` | Why no regular vision tests: other reasons | `Numeric(Byte)` | `%12.0g` |
| `sl_hc088d1` | Changes in behavior: increased physical activity | `Numeric(Byte)` | `%12.0g` |
| `sl_hc088d2` | Changes in behavior: changed diet | `Numeric(Byte)` | `%12.0g` |
| `sl_hc088d3` | Changes in behavior: stopped smoking | `Numeric(Byte)` | `%12.0g` |
| `sl_hc088d4` | Changes in behavior: reduced alcohol consumption | `Numeric(Byte)` | `%12.0g` |
| `sl_hc088dno` | Changes in behavior: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d1_1` | Started increased physical activity: when between 0-15 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d2_1` | Started increased physical activity: when between 16-25 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d3_1` | Started increased physical activity: when between 26-40 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d4_1` | Started increased physical activity: when between 41-55 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d5_1` | Started increased physical activity: when between 56-65 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d6_1` | Started increased physical activity: when between 66-75 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d7_1` | Started increased physical activity: when older than 75 years | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d1_2` | Started changed diet: when between 0-15 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d2_2` | Started changed diet: when between 16-25 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d3_2` | Started changed diet: when between 26-40 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d4_2` | Started changed diet: when between 41-55 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d5_2` | Started changed diet: when between 56-65 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d6_2` | Started changed diet: when between 66-75 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d7_2` | Started changed diet: when older than 75 years | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d1_3` | Stopped smoking: when between 0-15 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d2_3` | Stopped smoking: when between 16-25 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d3_3` | Stopped smoking: when between 26-40 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d4_3` | Stopped smoking: when between 41-55 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d5_3` | Stopped smoking: when between 56-65 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d6_3` | Stopped smoking: when between 66-75 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d7_3` | Stopped smoking: when older than 75 years | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d1_4` | Reduced alcohol consumption: when between 0-15 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d2_4` | Reduced alcohol consumption: when between 16-25 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d3_4` | Reduced alcohol consumption: when between 26-40 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d4_4` | Reduced alcohol consumption: when between 41-55 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d5_4` | Reduced alcohol consumption: when between 56-65 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d6_4` | Reduced alcohol consumption: when between 66-75 years old | `Numeric(Byte)` | `%12.0g` |
| `sl_hc089d7_4` | Reduced alcohol consumption: when older than 75 years | `Numeric(Byte)` | `%12.0g` |
| `sl_hc098_` | Proxy check | `Numeric(Byte)` | `%20.0g` |

### `hs` - Health History / Health Section

- Dataset: `sharew3_rel9-0-0_hs.dta`
- Read with: `ps.read_share_module("hs", wave=3)`
- Rows: 28,454
- Variables: 175
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sl_ph003_` | Health in general question for wave 3 | `Numeric(Byte)` | `%10.0g` |
| `sl_hs003_` | Childhood health status | `Numeric(Byte)` | `%40.0g` |
| `sl_hs004_` | Childhood health: missed school for 1 month or longer | `Numeric(Byte)` | `%10.0g` |
| `sl_hs005_` | Childhood health: confined to bed or home for 1 month or longer | `Numeric(Byte)` | `%10.0g` |
| `sl_hs006_` | Childhood health: in hospital for 1 month or longer | `Numeric(Byte)` | `%10.0g` |
| `sl_hs007_` | Childhood in hospital 3 times in 12 months | `Numeric(Byte)` | `%10.0g` |
| `sl_hs008d1` | Childhood illness 1: infectious disease | `Numeric(Byte)` | `%12.0g` |
| `sl_hs008d2` | Childhood illness 1: polio | `Numeric(Byte)` | `%12.0g` |
| `sl_hs008d3` | Childhood illness 1: asthma | `Numeric(Byte)` | `%12.0g` |
| `sl_hs008d4` | Childhood illness 1: respiratory problems other than asthma | `Numeric(Byte)` | `%12.0g` |
| `sl_hs008d5` | Childhood illness 1: allergies (other than asthma) | `Numeric(Byte)` | `%12.0g` |
| `sl_hs008d6` | Childhood illness 1: severe diarrhoea | `Numeric(Byte)` | `%12.0g` |
| `sl_hs008d7` | Childhood illness 1: meningitis/encephalitis | `Numeric(Byte)` | `%12.0g` |
| `sl_hs008d8` | Childhood illness 1: chronic ear problems | `Numeric(Byte)` | `%12.0g` |
| `sl_hs008d9` | Childhood illness 1: speech impairment | `Numeric(Byte)` | `%12.0g` |
| `sl_hs008d10` | Childhood illness 1: difficulty seeing even with eyeglasses | `Numeric(Byte)` | `%12.0g` |
| `sl_hs008dno` | Childhood illness 1: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_hs009d1` | Childhood illness 2: severe headaches or migraines | `Numeric(Byte)` | `%12.0g` |
| `sl_hs009d2` | Childhood illness 2: epilepsy, fits or seizures | `Numeric(Byte)` | `%12.0g` |
| `sl_hs009d3` | Childhood illness 2: emotional, nervous, or psychiatric problem | `Numeric(Byte)` | `%12.0g` |
| `sl_hs009d4` | Childhood illness 2: broken bones, fractures | `Numeric(Byte)` | `%12.0g` |
| `sl_hs009d5` | Childhood illness 2: appendicitis | `Numeric(Byte)` | `%12.0g` |
| `sl_hs009d6` | Childhood illness 2: childhood diabetes or high blood sugar | `Numeric(Byte)` | `%12.0g` |
| `sl_hs009d7` | Childhood illness 2: heart trouble | `Numeric(Byte)` | `%12.0g` |
| `sl_hs009d8` | Childhood illness 2: leukaemia or lymphoma | `Numeric(Byte)` | `%12.0g` |
| `sl_hs009d9` | Childhood illness 2: cancer or malignant tumour (excluding minor skin cancers) | `Numeric(Byte)` | `%12.0g` |
| `sl_hs009dot` | Childhood illness 2: other serious health condition | `Numeric(Byte)` | `%12.0g` |
| `sl_hs009dno` | Childhood illness 2: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_hs011_` | When infectious disease | `Numeric(Byte)` | `%34.0g` |
| `sl_hs015_` | When polio | `Numeric(Byte)` | `%34.0g` |
| `sl_hs018_` | When asthma | `Numeric(Byte)` | `%34.0g` |
| `sl_hs019_` | Did asthma last for a year or longer | `Numeric(Byte)` | `%10.0g` |
| `sl_hs020_` | When respiratory problems | `Numeric(Byte)` | `%34.0g` |
| `sl_hs021_` | Did respiratory problems last for a year or longer | `Numeric(Byte)` | `%10.0g` |
| `sl_hs022_` | When allergies | `Numeric(Byte)` | `%34.0g` |
| `sl_hs023_` | Did allergies last for a year or longer | `Numeric(Byte)` | `%10.0g` |
| `sl_hs024_` | When severe diarrhoea | `Numeric(Byte)` | `%34.0g` |
| `sl_hs025_` | Did severe diarrhoea last for a year or longer | `Numeric(Byte)` | `%10.0g` |
| `sl_hs027_` | When meningitis | `Numeric(Byte)` | `%34.0g` |
| `sl_hs028_` | When ear problems | `Numeric(Byte)` | `%34.0g` |
| `sl_hs029_` | Did ear problems last for a year or longer | `Numeric(Byte)` | `%10.0g` |
| `sl_hs030_` | When headaches or migraines | `Numeric(Byte)` | `%34.0g` |
| `sl_hs031_` | Did headaches or migraines last for a year or longer | `Numeric(Byte)` | `%10.0g` |
| `sl_hs032_` | When epilepsy | `Numeric(Byte)` | `%34.0g` |
| `sl_hs033_` | Did epilepsy last for a year or longer | `Numeric(Byte)` | `%10.0g` |
| `sl_hs034_` | When psychiatric problems | `Numeric(Byte)` | `%34.0g` |
| `sl_hs035_` | Did psychiatric problems last for a year or longer | `Numeric(Byte)` | `%10.0g` |
| `sl_hs036_` | When broken bones and fractures | `Numeric(Byte)` | `%34.0g` |
| `sl_hs037_` | When appendicitis | `Numeric(Byte)` | `%34.0g` |
| `sl_hs038_` | When childhood diabetes | `Numeric(Byte)` | `%34.0g` |
| `sl_hs039_` | When heart trouble | `Numeric(Byte)` | `%34.0g` |
| `sl_hs040_` | When leukaemia | `Numeric(Byte)` | `%34.0g` |
| `sl_hs041_` | When childhood cancer | `Numeric(Byte)` | `%34.0g` |
| `sl_hs042_` | When speech impairment | `Numeric(Byte)` | `%34.0g` |
| `sl_hs043_` | When difficulty with eyeglasses | `Numeric(Byte)` | `%34.0g` |
| `sl_hs044_` | When other serious condition | `Numeric(Byte)` | `%34.0g` |
| `sl_hs049_` | Start of menstrual period | `Numeric(Int)` | `%12.0g` |
| `sl_hs050_` | Estimate start of menstrual period | `Numeric(Byte)` | `%27.0g` |
| `sl_hs051_` | End of menstrual period | `Numeric(Int)` | `%28.0g` |
| `sl_hs045d1` | Did parents: smoke | `Numeric(Byte)` | `%12.0g` |
| `sl_hs045d2` | Did parents: drink heavily | `Numeric(Byte)` | `%12.0g` |
| `sl_hs045d3` | Did parents: have mental health problems | `Numeric(Byte)` | `%12.0g` |
| `sl_hs045dno` | Did parents: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_hs052_` | Ever had physical injury to disability | `Numeric(Byte)` | `%10.0g` |
| `sl_hs053_` | When received this injury | `Numeric(Int)` | `%10.0g` |
| `sl_hs054_` | Number periods of ill health | `Numeric(Byte)` | `%47.0g` |
| `sl_hs059_1` | When did illness period 1 start | `Numeric(Int)` | `%10.0g` |
| `sl_hs055d1_1` | Type 1 illness period 1: back pain | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d2_1` | Type 1 illness period 1: arthritis, including osteoarthritis and rheumatism | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d3_1` | Type 1 illness period 1: osteoporosis | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d4_1` | Type 1 illness period 1: angina or heart attack | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d5_1` | Type 1 illness period 1: other heart disease | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d6_1` | Type 1 illness period 1: diabetes or high blood sugar | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d7_1` | Type 1 illness period 1: stroke | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d8_1` | Type 1 illness period 1: asthma | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d9_1` | Type 1 illness period 1: respiratory problems other than asthma | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d10_1` | Type 1 illness period 1: tuberculosis | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d11_1` | Type 1 illness period 1: severe headaches or migraines | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055dno_1` | Type 1 illness period 1: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d1_1` | Type 2 illness period 1: leukaemia or lymphoma | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d2_1` | Type 2 illness period 1: cancer or malignant tumour | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d3_1` | Type 2 illness period 1: emotional, nervous, or psychiatric problem | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d4_1` | Type 2 illness period 1: fatigue, e.g. with ME, MS | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d5_1` | Type 2 illness period 1: gynaecological (women's) problem | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d6_1` | Type 2 illness period 1: eyesight problems | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d7_1` | Type 2 illness period 1: infectious disease (e.g. shingles, mumps, TB, HIV) | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d8_1` | Type 2 illness period 1: allergies (other than asthma) | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056dot_1` | Type 2 illness period 1: other | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056dno_1` | Type 2 illness period 1: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_hs060_1` | When did illness period 1 stop | `Numeric(Int)` | `%21.0g` |
| `sl_hs061_1` | Did family and friends help (illness period 1) | `Numeric(Byte)` | `%14.0g` |
| `sl_hs062d1_1` | Experiences at work (illness period 1): denied promotions | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062d2_1` | Experiences at work (illness period 1): fewer responsibilities | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062d3_1` | Experiences at work (illness period 1): tasks below qualifications | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062d4_1` | Experiences at work (illness period 1): harassment by boss/colleagues | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062d5_1` | Experiences at work (illness period 1): pay cuts | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062dno_1` | Experiences at work (illness period 1): none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_hs059_2` | When did illness period 2 start | `Numeric(Int)` | `%10.0g` |
| `sl_hs055d1_2` | Type 1 illness period 2: back pain | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d2_2` | Type 1 illness period 2: arthritis, including osteoarthritis and rheumatism | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d3_2` | Type 1 illness period 2: osteoporosis | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d4_2` | Type 1 illness period 2: angina or heart attack | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d5_2` | Type 1 illness period 2: other heart disease | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d6_2` | Type 1 illness period 2: diabetes or high blood sugar | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d7_2` | Type 1 illness period 2: stroke | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d8_2` | Type 1 illness period 2: asthma | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d9_2` | Type 1 illness period 2: respiratory problems other than asthma | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d10_2` | Type 1 illness period 2: tuberculosis | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d11_2` | Type 1 illness period 2: severe headaches or migraines | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055dno_2` | Type 1 illness period 2: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d1_2` | Type 2 illness period 2: leukaemia or lymphoma | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d2_2` | Type 2 illness period 2: cancer or malignant tumour | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d3_2` | Type 2 illness period 2: emotional, nervous, or psychiatric problem | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d4_2` | Type 2 illness period 2: fatigue, e.g. with ME, MS | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d5_2` | Type 2 illness period 2: gynaecological (women's) problem | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d6_2` | Type 2 illness period 2: eyesight problems | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d7_2` | Type 2 illness period 2: infectious disease (e.g. shingles, mumps, TB, HIV) | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d8_2` | Type 2 illness period 2: allergies (other than asthma) | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056dot_2` | Type 2 illness period 2: other | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056dno_2` | Type 2 illness period 2: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_hs060_2` | When did illness period 2 stop | `Numeric(Int)` | `%21.0g` |
| `sl_hs061_2` | Did family and friends help (illness period 2) | `Numeric(Byte)` | `%14.0g` |
| `sl_hs062d1_2` | Experiences at work (illness period 2): denied promotions | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062d2_2` | Experiences at work (illness period 2): fewer responsibilities | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062d3_2` | Experiences at work (illness period 2): tasks below qualifications | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062d4_2` | Experiences at work (illness period 2): harassment by boss/colleagues | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062d5_2` | Experiences at work (illness period 2): pay cuts | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062dno_2` | Experiences at work (illness period 2): none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_hs059_3` | When did illness period 3 start | `Numeric(Int)` | `%10.0g` |
| `sl_hs055d1_3` | Type 1 illness period 3: back pain | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d2_3` | Type 1 illness period 3: arthritis, including osteoarthritis and rheumatism | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d3_3` | Type 1 illness period 3: osteoporosis | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d4_3` | Type 1 illness period 3: angina or heart attack | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d5_3` | Type 1 illness period 3: other heart disease | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d6_3` | Type 1 illness period 3: diabetes or high blood sugar | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d7_3` | Type 1 illness period 3: stroke | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d8_3` | Type 1 illness period 3: asthma | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d9_3` | Type 1 illness period 3: respiratory problems other than asthma | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d10_3` | Type 1 illness period 3: tuberculosis | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055d11_3` | Type 1 illness period 3: severe headaches or migraines | `Numeric(Byte)` | `%12.0g` |
| `sl_hs055dno_3` | Type 1 illness period 3: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d1_3` | Type 2 illness period 3: leukaemia or lymphoma | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d2_3` | Type 2 illness period 3: cancer or malignant tumour | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d3_3` | Type 2 illness period 3: emotional, nervous, or psychiatric problem | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d4_3` | Type 2 illness period 3: fatigue, e.g. with ME, MS | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d5_3` | Type 2 illness period 3: gynaecological (women's) problem | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d6_3` | Type 2 illness period 3: eyesight problems | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d7_3` | Type 2 illness period 3: infectious disease (e.g. shingles, mumps, TB, HIV) | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056d8_3` | Type 2 illness period 3: allergies (other than asthma) | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056dot_3` | Type 2 illness period 3: other | `Numeric(Byte)` | `%12.0g` |
| `sl_hs056dno_3` | Type 2 illness period 3: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_hs060_3` | When did illness period 3 stop | `Numeric(Int)` | `%21.0g` |
| `sl_hs061_3` | Did family and friends help (illness period 3) | `Numeric(Byte)` | `%14.0g` |
| `sl_hs062d1_3` | Experiences at work (illness period 3): denied promotions | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062d2_3` | Experiences at work (illness period 3): fewer responsibilities | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062d3_3` | Experiences at work (illness period 3): tasks below qualifications | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062d4_3` | Experiences at work (illness period 3): harassment by boss/colleagues | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062d5_3` | Experiences at work (illness period 3): pay cuts | `Numeric(Byte)` | `%12.0g` |
| `sl_hs062dno_3` | Experiences at work (illness period 3): none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_hs063d1` | Consequences of illness period: limited opportunities for paid work | `Numeric(Byte)` | `%12.0g` |
| `sl_hs063d2` | Consequences of illness period: negative effect on family life | `Numeric(Byte)` | `%12.0g` |
| `sl_hs063d3` | Consequences of illness period: positive effect on family life | `Numeric(Byte)` | `%12.0g` |
| `sl_hs063d4` | Consequences of illness period: made social life more difficult | `Numeric(Byte)` | `%12.0g` |
| `sl_hs063d5` | Consequences of illness period: limited leisure activities | `Numeric(Byte)` | `%12.0g` |
| `sl_hs063d6` | Consequences of illness period: made determined to get the best out of life | `Numeric(Byte)` | `%12.0g` |
| `sl_hs063d7` | Consequences of illness period: opened up new opportunities | `Numeric(Byte)` | `%12.0g` |
| `sl_hs063dot` | Consequences of illness period: other | `Numeric(Byte)` | `%12.0g` |
| `sl_hs063dno` | Consequences of illness period: none of these | `Numeric(Byte)` | `%12.0g` |
| `sl_hs066_` | Proxy check | `Numeric(Byte)` | `%20.0g` |

### `rc` - Retrospective Children History

- Dataset: `sharew3_rel9-0-0_rc.dta`
- Read with: `ps.read_share_module("rc", wave=3)`
- Rows: 28,454
- Variables: 360
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
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
| `sl_childid_adopted_1` | Child identifier (fix across modules and waves): Child 1 (SHARELIFE: adopted) | `Str(14)` | `%14s` |
| `sl_childid_adopted_2` | Child identifier (fix across modules and waves): Child 2 (SHARELIFE: adopted) | `Str(14)` | `%14s` |
| `sl_childid_adopted_3` | Child identifier (fix across modules and waves): Child 3 (SHARELIFE: adopted) | `Str(14)` | `%14s` |
| `sl_childid_adopted_4` | Child identifier (fix across modules and waves): Child 4 (SHARELIFE: adopted) | `Str(14)` | `%14s` |
| `sl_childid_adopted_5` | Child identifier (fix across modules and waves): Child 5 (SHARELIFE: adopted) | `Str(14)` | `%14s` |
| `sl_childid_adopted_6` | Child identifier (fix across modules and waves): Child 6 (SHARELIFE: adopted) | `Str(14)` | `%14s` |
| `sl_rc022_` | Ever had other non_mentioned children | `Numeric(Byte)` | `%10.0g` |
| `sl_rc023_` | Number of other children | `Numeric(Byte)` | `%10.0g` |
| `sl_rc024_1` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_1` | Gender other child | `Numeric(Long)` | `%10.0g` |
| `sl_rc027_1` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc028_1` | Year of death other child | `Numeric(Int)` | `%12.0g` |
| `sl_rc029_1` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc030_1` | How long was maternity interruption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc030a_1` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc031d1_1` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d2_1` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d3_1` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d4_1` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d5_1` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d6_1` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031dot_1` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc032_1` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc033c_1` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_rc024_2` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_2` | Gender other child | `Numeric(Long)` | `%10.0g` |
| `sl_rc027_2` | Other child still alive | `Numeric(Int)` | `%10.0g` |
| `sl_rc028_2` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc029_2` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc030_2` | How long was maternity interruption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc030a_2` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc031d1_2` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d2_2` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d3_2` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d4_2` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d5_2` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d6_2` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031dot_2` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc032_2` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc033c_2` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_rc024_3` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_3` | Gender other child | `Numeric(Long)` | `%10.0g` |
| `sl_rc027_3` | Other child still alive | `Numeric(Int)` | `%10.0g` |
| `sl_rc028_3` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc029_3` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc030_3` | How long was maternity interruption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc030a_3` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc031d1_3` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d2_3` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d3_3` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d4_3` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d5_3` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d6_3` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031dot_3` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc032_3` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc033c_3` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_rc024_4` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_4` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `sl_rc027_4` | Other child still alive | `Numeric(Int)` | `%10.0g` |
| `sl_rc028_4` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc029_4` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc030_4` | How long was maternity interruption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc030a_4` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc031d1_4` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d2_4` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d3_4` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d4_4` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d5_4` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d6_4` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031dot_4` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc032_4` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc033c_4` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_rc024_5` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_5` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `sl_rc027_5` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc028_5` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc029_5` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc030_5` | How long was maternity interruption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc030a_5` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc031d1_5` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d2_5` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d3_5` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d4_5` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d5_5` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d6_5` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031dot_5` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc032_5` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc033c_5` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_rc024_6` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_6` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `sl_rc027_6` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc028_6` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc029_6` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc030_6` | How long was maternity interruption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc030a_6` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc031d1_6` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d2_6` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d3_6` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d4_6` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d5_6` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d6_6` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031dot_6` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc032_6` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc033c_6` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_rc024_7` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_7` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `sl_rc027_7` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc028_7` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc029_7` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc030_7` | How long was maternity interruption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc030a_7` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc031d1_7` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d2_7` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d3_7` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d4_7` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d5_7` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d6_7` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031dot_7` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc032_7` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc024_8` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_8` | Gender other child | `Numeric(Long)` | `%10.0g` |
| `sl_rc027_8` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc028_8` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc029_8` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc030_8` | How long was maternity interruption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc030a_8` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc031d1_8` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d2_8` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d3_8` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d4_8` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d5_8` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d6_8` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031dot_8` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc032_8` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc033c_8` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_rc024_9` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_9` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `sl_rc027_9` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc028_9` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc029_9` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc030_9` | How long was maternity interruption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc030a_9` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc031d1_9` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d2_9` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d3_9` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d4_9` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d5_9` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d6_9` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031dot_9` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc032_9` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc033c_9` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_rc024_10` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_10` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `sl_rc027_10` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc028_10` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc029_10` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc030_10` | How long was maternity interruption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc030a_10` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc031d1_10` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d2_10` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d3_10` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d4_10` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d5_10` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d6_10` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031dot_10` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc032_10` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc024_11` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_11` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `sl_rc027_11` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc028_11` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc029_11` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc030_11` | How long was maternity interruption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc030a_11` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc031d1_11` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d2_11` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d3_11` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d4_11` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d5_11` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d6_11` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031dot_11` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc032_11` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc024_12` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_12` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `sl_rc027_12` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc028_12` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc029_12` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc030_12` | How long was maternity interruption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc030a_12` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc031d1_12` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d2_12` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d3_12` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d4_12` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d5_12` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d6_12` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031dot_12` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc032_12` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc024_13` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_13` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `sl_rc027_13` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc028_13` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc029_13` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc030_13` | How long was maternity interruption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc030a_13` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc031d1_13` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d2_13` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d3_13` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d4_13` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d5_13` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d6_13` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031dot_13` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc024_14` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_14` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `sl_rc027_14` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc028_14` | Year of death other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc029_14` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc031d1_14` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d2_14` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d3_14` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d4_14` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d5_14` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031d6_14` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc031dot_14` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc024_15` | Year of birth other child | `Numeric(Int)` | `%10.0g` |
| `sl_rc026_15` | Gender other child | `Numeric(Byte)` | `%10.0g` |
| `sl_rc027_15` | Other child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc038_` | Other adopted children | `Numeric(Byte)` | `%10.0g` |
| `sl_rc039_` | Number of other adopted | `Numeric(Byte)` | `%10.0g` |
| `sl_rc041_1` | Other child year of adoption | `Numeric(Int)` | `%10.0g` |
| `sl_rc042_1` | Other adopted child gender | `Numeric(Byte)` | `%10.0g` |
| `sl_rc043_1` | Other adopted child year of birth | `Numeric(Int)` | `%10.0g` |
| `sl_rc044_1` | Other adopted child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc045_1` | Other adopted child year of death | `Numeric(Int)` | `%10.0g` |
| `sl_rc046_1` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc047_1` | How long was maternity interuption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc047a_1` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc048d1_1` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d2_1` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d3_1` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d4_1` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d5_1` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d6_1` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048dot_1` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc049_1` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc050c_1` | Currency maternity benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_rc041_2` | Other child year of adoption | `Numeric(Int)` | `%10.0g` |
| `sl_rc042_2` | Other adopted child gender | `Numeric(Byte)` | `%10.0g` |
| `sl_rc043_2` | Other adopted child year of birth | `Numeric(Int)` | `%10.0g` |
| `sl_rc044_2` | Other adopted child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc045_2` | Other adopted child year of death | `Numeric(Int)` | `%10.0g` |
| `sl_rc046_2` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc047_2` | How long was maternity interuption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc047a_2` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc048d1_2` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d2_2` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d3_2` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d4_2` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d5_2` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d6_2` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048dot_2` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc049_2` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc050c_2` | Currency maternity benefit - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_rc041_3` | Other child year of adoption | `Numeric(Int)` | `%10.0g` |
| `sl_rc042_3` | Other adopted child gender | `Numeric(Byte)` | `%10.0g` |
| `sl_rc043_3` | Other adopted child year of birth | `Numeric(Int)` | `%10.0g` |
| `sl_rc044_3` | Other adopted child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc046_3` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc047_3` | How long was maternity interuption | `Numeric(Byte)` | `%49.0g` |
| `sl_rc047a_3` | When started working again | `Numeric(Int)` | `%10.0g` |
| `sl_rc048d1_3` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d2_3` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d3_3` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d4_3` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d5_3` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d6_3` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048dot_3` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc049_3` | Maternity benefit amount | `Numeric(Long)` | `%10.0g` |
| `sl_rc050c_3` | Currency maternity benefit - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_rc041_4` | Other child year of adoption | `Numeric(Int)` | `%10.0g` |
| `sl_rc042_4` | Other adopted child gender | `Numeric(Byte)` | `%10.0g` |
| `sl_rc043_4` | Other adopted child year of birth | `Numeric(Int)` | `%10.0g` |
| `sl_rc044_4` | Other adopted child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc046_4` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc048d1_4` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d2_4` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d3_4` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d4_4` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d5_4` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d6_4` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048dot_4` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc041_5` | Other child year of adoption | `Numeric(Int)` | `%10.0g` |
| `sl_rc042_5` | Other adopted child gender | `Numeric(Byte)` | `%10.0g` |
| `sl_rc043_5` | Other adopted child year of birth | `Numeric(Int)` | `%10.0g` |
| `sl_rc044_5` | Other adopted child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc046_5` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc048d1_5` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d2_5` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d3_5` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d4_5` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d5_5` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d6_5` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048dot_5` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc041_6` | Other child year of adoption | `Numeric(Int)` | `%10.0g` |
| `sl_rc042_6` | Other adopted child gender | `Numeric(Byte)` | `%10.0g` |
| `sl_rc043_6` | Other adopted child year of birth | `Numeric(Int)` | `%10.0g` |
| `sl_rc044_6` | Other adopted child still alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc046_6` | Left job because of child | `Numeric(Byte)` | `%44.0g` |
| `sl_rc048d1_6` | Sources of income maternity leave: income from (self-)employment | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d2_6` | Sources of income maternity leave: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d3_6` | Sources of income maternity leave: maternity benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d4_6` | Sources of income maternity leave: child benefits | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d5_6` | Sources of income maternity leave: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048d6_6` | Sources of income maternity leave: running down assets or bank accounts | `Numeric(Byte)` | `%12.0g` |
| `sl_rc048dot_6` | Sources of income maternity leave: other | `Numeric(Byte)` | `%12.0g` |
| `sl_rc054_` | Children born not alive | `Numeric(Byte)` | `%10.0g` |
| `sl_rc055_` | Number of pregnancies not alive children | `Numeric(Byte)` | `%10.0g` |
| `sl_rc056_1` | Year pregnancy ended | `Numeric(Int)` | `%12.0g` |
| `sl_rc057_1` | Months pregnancy lasted | `Numeric(Byte)` | `%10.0g` |
| `sl_rc056_2` | Year pregnancy ended | `Numeric(Int)` | `%10.0g` |
| `sl_rc057_2` | Months pregnancy lasted | `Numeric(Byte)` | `%10.0g` |
| `sl_rc056_3` | Year pregnancy ended | `Numeric(Int)` | `%10.0g` |
| `sl_rc057_3` | Months pregnancy lasted | `Numeric(Byte)` | `%10.0g` |
| `sl_rc056_4` | Year pregnancy ended | `Numeric(Int)` | `%10.0g` |
| `sl_rc057_4` | Months pregnancy lasted | `Numeric(Byte)` | `%10.0g` |
| `sl_rc056_5` | Year pregnancy ended | `Numeric(Int)` | `%10.0g` |
| `sl_rc057_5` | Months pregnancy lasted | `Numeric(Byte)` | `%10.0g` |
| `sl_rc056_6` | Year pregnancy ended | `Numeric(Int)` | `%10.0g` |
| `sl_rc057_6` | Months pregnancy lasted | `Numeric(Byte)` | `%10.0g` |
| `sl_rc056_7` | Year pregnancy ended | `Numeric(Int)` | `%10.0g` |
| `sl_rc057_7` | Months pregnancy lasted | `Numeric(Byte)` | `%10.0g` |
| `sl_rc056_8` | Year pregnancy ended | `Numeric(Int)` | `%10.0g` |
| `sl_rc057_8` | Months pregnancy lasted | `Numeric(Byte)` | `%10.0g` |
| `sl_rc056_9` | Year pregnancy ended | `Numeric(Byte)` | `%10.0g` |
| `sl_rc057_9` | Months pregnancy lasted | `Numeric(Byte)` | `%10.0g` |
| `sl_rc056_10` | Year pregnancy ended | `Numeric(Byte)` | `%10.0g` |
| `sl_rc057_10` | Months pregnancy lasted | `Numeric(Byte)` | `%10.0g` |
| `sl_rc056_11` | Year pregnancy ended | `Numeric(Byte)` | `%10.0g` |
| `sl_rc057_11` | Months pregnancy lasted | `Numeric(Byte)` | `%10.0g` |
| `sl_rc059_` | Presence of people during children section | `Numeric(Byte)` | `%10.0g` |
| `sl_rc061_` | Proxy check | `Numeric(Byte)` | `%20.0g` |

### `re` - Retrospective Employment

- Dataset: `sharew3_rel9-0-0_re.dta`
- Read with: `ps.read_share_module("re", wave=3)`
- Rows: 28,454
- Variables: 724
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sl_re002_` | Year finished fulltime education | `Numeric(Int)` | `%20.0g` |
| `sl_re003_` | Situation at age 15 if no education | `Numeric(Byte)` | `%45.0g` |
| `sl_re005_` | Ever done paid work | `Numeric(Byte)` | `%10.0g` |
| `sl_re006_` | Start first paid job | `Numeric(Byte)` | `%51.0g` |
| `sl_re007_` | Situation in gap after education | `Numeric(Byte)` | `%45.0g` |
| `sl_re008_1` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `sl_re009_1` | Year of change of situation | `Numeric(Int)` | `%12.0g` |
| `sl_re010_1` | Situation changed to | `Numeric(Byte)` | `%45.0g` |
| `sl_re008_2` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `sl_re009_2` | Year of change of situation | `Numeric(Int)` | `%12.0g` |
| `sl_re010_2` | Situation changed to | `Numeric(Byte)` | `%45.0g` |
| `sl_re008_3` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `sl_re009_3` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `sl_re010_3` | Situation changed to | `Numeric(Byte)` | `%45.0g` |
| `sl_re008_4` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `sl_re009_4` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `sl_re010_4` | Situation changed to | `Numeric(Byte)` | `%45.0g` |
| `sl_re008_5` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `sl_re009_5` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `sl_re010_5` | Situation changed to | `Numeric(Byte)` | `%45.0g` |
| `sl_re008_6` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `sl_re009_6` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `sl_re010_6` | Situation changed to | `Numeric(Byte)` | `%45.0g` |
| `sl_re008_7` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `sl_re009_7` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `sl_re010_7` | Situation changed to | `Numeric(Byte)` | `%45.0g` |
| `sl_re008_8` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `sl_re009_8` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `sl_re010_8` | Situation changed to | `Numeric(Byte)` | `%45.0g` |
| `sl_re008_9` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `sl_re009_9` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `sl_re010_9` | Situation changed to | `Numeric(Byte)` | `%45.0g` |
| `sl_re008_10` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `sl_re009_10` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `sl_re010_10` | Situation changed to | `Numeric(Byte)` | `%45.0g` |
| `sl_re008_11` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `sl_re009_11` | Year of change of situation | `Numeric(Int)` | `%10.0g` |
| `sl_re010_11` | Situation changed to | `Numeric(Byte)` | `%45.0g` |
| `sl_re008_12` | Did situation ever change | `Numeric(Byte)` | `%10.0g` |
| `sl_re011_1` | Year started job | `Numeric(Int)` | `%12.0g` |
| `sl_re012isco_1` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_1` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_1` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_1` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_1` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_1` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_1` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_1` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_1` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_1` | First monthly wage in job | `Numeric(Double)` | `%10.0g` |
| `sl_re022c_1` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_1` | First monthly work income in self-employment | `Numeric(Double)` | `%10.0g` |
| `sl_re024c_1` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_1` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_1` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_1` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_1` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_1` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_1` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `sl_re028c_1` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re029_1` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `sl_re030c_1` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re031_1` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_1` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_1` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_1` | Income during gap after leaving job 1: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_1` | Income during gap after leaving job 1: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_1` | Income during gap after leaving job 1: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_1` | Income during gap after leaving job 1: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_1` | Income during gap after leaving job 1: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_1` | Income during gap after leaving job 1: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_1` | Income during gap after leaving job 1: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_2` | Year started job | `Numeric(Int)` | `%12.0g` |
| `sl_re012isco_2` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_2` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_2` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_2` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_2` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_2` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_2` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_2` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_2` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_2` | First monthly wage in job | `Numeric(Double)` | `%10.0g` |
| `sl_re022c_2` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_2` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `sl_re024c_2` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_2` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_2` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_2` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_2` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_2` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_2` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `sl_re028c_2` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re029_2` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `sl_re030c_2` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re031_2` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_2` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_2` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_2` | Income during gap after leaving job 2: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_2` | Income during gap after leaving job 2: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_2` | Income during gap after leaving job 2: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_2` | Income during gap after leaving job 2: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_2` | Income during gap after leaving job 2: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_2` | Income during gap after leaving job 2: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_2` | Income during gap after leaving job 2: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_3` | Year started job | `Numeric(Int)` | `%12.0g` |
| `sl_re012isco_3` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_3` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_3` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_3` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_3` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_3` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_3` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_3` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_3` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_3` | First monthly wage in job | `Numeric(Double)` | `%10.0g` |
| `sl_re022c_3` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_3` | First monthly work income in self-employment | `Numeric(Double)` | `%10.0g` |
| `sl_re024c_3` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_3` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_3` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_3` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_3` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_3` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_3` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `sl_re028c_3` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re029_3` | Current work income if still self-employed | `Numeric(Double)` | `%10.0g` |
| `sl_re030c_3` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re031_3` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_3` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_3` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_3` | Income during gap after leaving job 3: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_3` | Income during gap after leaving job 3: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_3` | Income during gap after leaving job 3: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_3` | Income during gap after leaving job 3: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_3` | Income during gap after leaving job 3: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_3` | Income during gap after leaving job 3: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_3` | Income during gap after leaving job 3: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_4` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_4` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_4` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_4` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_4` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_4` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_4` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_4` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_4` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_4` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_4` | First monthly wage in job | `Numeric(Double)` | `%10.0g` |
| `sl_re022c_4` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_4` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `sl_re024c_4` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_4` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_4` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_4` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_4` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_4` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_4` | Current wage if still employed | `Numeric(Double)` | `%10.0g` |
| `sl_re028c_4` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re029_4` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `sl_re030c_4` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re031_4` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_4` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_4` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_4` | Income during gap after leaving job 4: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_4` | Income during gap after leaving job 4: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_4` | Income during gap after leaving job 4: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_4` | Income during gap after leaving job 4: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_4` | Income during gap after leaving job 4: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_4` | Income during gap after leaving job 4: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_4` | Income during gap after leaving job 4: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_5` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_5` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_5` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_5` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_5` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_5` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_5` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_5` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_5` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_5` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_5` | First monthly wage in job | `Numeric(Double)` | `%10.0g` |
| `sl_re022c_5` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_5` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `sl_re024c_5` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_5` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_5` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_5` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_5` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_5` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_5` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `sl_re028c_5` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re029_5` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `sl_re030c_5` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re031_5` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_5` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_5` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_5` | Income during gap after leaving job 5: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_5` | Income during gap after leaving job 5: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_5` | Income during gap after leaving job 5: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_5` | Income during gap after leaving job 5: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_5` | Income during gap after leaving job 5: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_5` | Income during gap after leaving job 5: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_5` | Income during gap after leaving job 5: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_6` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_6` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_6` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_6` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_6` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_6` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_6` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_6` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_6` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_6` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_6` | First monthly wage in job | `Numeric(Double)` | `%10.0g` |
| `sl_re022c_6` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_6` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `sl_re024c_6` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_6` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_6` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_6` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_6` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_6` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_6` | Current wage if still employed | `Numeric(Double)` | `%10.0g` |
| `sl_re028c_6` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re029_6` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `sl_re030c_6` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re031_6` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_6` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_6` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_6` | Income during gap after leaving job 6: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_6` | Income during gap after leaving job 6: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_6` | Income during gap after leaving job 6: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_6` | Income during gap after leaving job 6: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_6` | Income during gap after leaving job 6: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_6` | Income during gap after leaving job 6: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_6` | Income during gap after leaving job 6: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_7` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_7` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_7` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_7` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_7` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_7` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_7` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_7` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_7` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_7` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_7` | First monthly wage in job | `Numeric(Double)` | `%10.0g` |
| `sl_re022c_7` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_7` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `sl_re024c_7` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_7` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_7` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_7` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_7` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_7` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_7` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `sl_re028c_7` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re029_7` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `sl_re030c_7` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re031_7` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_7` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_7` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_7` | Income during gap after leaving job 7: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_7` | Income during gap after leaving job 7: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_7` | Income during gap after leaving job 7: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_7` | Income during gap after leaving job 7: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_7` | Income during gap after leaving job 7: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_7` | Income during gap after leaving job 7: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_7` | Income during gap after leaving job 7: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_8` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_8` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_8` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_8` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_8` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_8` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_8` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_8` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_8` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_8` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_8` | First monthly wage in job | `Numeric(Double)` | `%10.0g` |
| `sl_re022c_8` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_8` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `sl_re024c_8` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_8` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_8` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_8` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_8` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_8` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_8` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `sl_re028c_8` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re029_8` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `sl_re030c_8` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re031_8` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_8` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_8` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_8` | Income during gap after leaving job 8: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_8` | Income during gap after leaving job 8: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_8` | Income during gap after leaving job 8: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_8` | Income during gap after leaving job 8: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_8` | Income during gap after leaving job 8: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_8` | Income during gap after leaving job 8: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_8` | Income during gap after leaving job 8: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_9` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_9` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_9` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_9` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_9` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_9` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_9` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_9` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_9` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_9` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_9` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `sl_re022c_9` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_9` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `sl_re024c_9` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_9` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_9` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_9` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_9` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_9` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_9` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `sl_re028c_9` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re029_9` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `sl_re030c_9` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re031_9` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_9` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_9` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_9` | Income during gap after leaving job 9: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_9` | Income during gap after leaving job 9: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_9` | Income during gap after leaving job 9: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_9` | Income during gap after leaving job 9: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_9` | Income during gap after leaving job 9: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_9` | Income during gap after leaving job 9: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_9` | Income during gap after leaving job 9: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_10` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_10` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_10` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_10` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_10` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_10` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_10` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_10` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_10` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_10` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_10` | First monthly wage in job | `Numeric(Long)` | `%12.0g` |
| `sl_re022c_10` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_10` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `sl_re024c_10` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_10` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_10` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_10` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_10` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_10` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_10` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `sl_re028c_10` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re029_10` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `sl_re030c_10` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re031_10` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_10` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_10` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_10` | Income during gap after leaving job 10: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_10` | Income during gap after leaving job 10: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_10` | Income during gap after leaving job 10: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_10` | Income during gap after leaving job 10: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_10` | Income during gap after leaving job 10: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_10` | Income during gap after leaving job 10: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_10` | Income during gap after leaving job 10: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_11` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_11` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_11` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_11` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_11` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_11` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_11` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_11` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_11` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_11` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_11` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `sl_re022c_11` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_11` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `sl_re024c_11` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_11` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_11` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_11` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_11` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_11` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_11` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `sl_re028c_11` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re029_11` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `sl_re031_11` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_11` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_11` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_11` | Income during gap after leaving job 11: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_11` | Income during gap after leaving job 11: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_11` | Income during gap after leaving job 11: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_11` | Income during gap after leaving job 11: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_11` | Income during gap after leaving job 11: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_11` | Income during gap after leaving job 11: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_11` | Income during gap after leaving job 11: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_12` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_12` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_12` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_12` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_12` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_12` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_12` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_12` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_12` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_12` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_12` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `sl_re022c_12` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_12` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `sl_re024c_12` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_12` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_12` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_12` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_12` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_12` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_12` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `sl_re028c_12` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re029_12` | Current work income if still self-employed | `Numeric(Long)` | `%10.0g` |
| `sl_re030c_12` | Currency of current work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re031_12` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_12` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_12` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_12` | Income during gap after leaving job 12: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_12` | Income during gap after leaving job 12: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_12` | Income during gap after leaving job 12: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_12` | Income during gap after leaving job 12: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_12` | Income during gap after leaving job 12: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_12` | Income during gap after leaving job 12: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_12` | Income during gap after leaving job 12: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_13` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_13` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_13` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_13` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_13` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_13` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_13` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_13` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_13` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_13` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_13` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `sl_re022c_13` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_13` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `sl_re024c_13` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_13` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_13` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_13` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_13` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_13` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_13` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `sl_re028c_13` | Currency of current wage - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_re029_13` | Current work income if still self-employed | `Numeric(Int)` | `%10.0g` |
| `sl_re030c_13` | Currency of current work income - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_re031_13` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_13` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_13` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_13` | Income during gap after leaving job 13: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_13` | Income during gap after leaving job 13: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_13` | Income during gap after leaving job 13: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_13` | Income during gap after leaving job 13: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_13` | Income during gap after leaving job 13: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_13` | Income during gap after leaving job 13: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_13` | Income during gap after leaving job 13: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_14` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_14` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_14` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_14` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_14` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_14` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_14` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_14` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_14` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_14` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_14` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `sl_re022c_14` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_14` | First monthly work income in self-employment | `Numeric(Long)` | `%10.0g` |
| `sl_re024c_14` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_14` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_14` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_14` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_14` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_14` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_14` | Current wage if still employed | `Numeric(Int)` | `%10.0g` |
| `sl_re028c_14` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re031_14` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_14` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_14` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_14` | Income during gap after leaving job 14: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_14` | Income during gap after leaving job 14: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_14` | Income during gap after leaving job 14: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_14` | Income during gap after leaving job 14: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_14` | Income during gap after leaving job 14: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_14` | Income during gap after leaving job 14: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_14` | Income during gap after leaving job 14: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_15` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_15` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_15` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_15` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_15` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_15` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_15` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_15` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_15` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_15` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_15` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `sl_re022c_15` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_15` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_15` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_15` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_15` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_15` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_15` | Current wage if still employed | `Numeric(Long)` | `%10.0g` |
| `sl_re028c_15` | Currency of current wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re031_15` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_15` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_15` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_15` | Income during gap after leaving job 15: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_15` | Income during gap after leaving job 15: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_15` | Income during gap after leaving job 15: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_15` | Income during gap after leaving job 15: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_15` | Income during gap after leaving job 15: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_15` | Income during gap after leaving job 15: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_15` | Income during gap after leaving job 15: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_16` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_16` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_16` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_16` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_16` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_16` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_16` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re018_16` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_16` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re020_16` | When changed to full-time | `Numeric(Int)` | `%10.0g` |
| `sl_re021_16` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `sl_re022c_16` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re023_16` | First monthly work income in self-employment | `Numeric(Int)` | `%10.0g` |
| `sl_re024c_16` | Currency of work income - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_16` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_16` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_16` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_16` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_16` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_16` | Current wage if still employed | `Numeric(Int)` | `%10.0g` |
| `sl_re028c_16` | Currency of current wage - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_re031_16` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_16` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_16` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_16` | Income during gap after leaving job 16: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_16` | Income during gap after leaving job 16: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_16` | Income during gap after leaving job 16: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_16` | Income during gap after leaving job 16: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_16` | Income during gap after leaving job 16: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_16` | Income during gap after leaving job 16: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_16` | Income during gap after leaving job 16: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_17` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_17` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_17` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_17` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_17` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_17` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re017_17` | Why worked part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re021_17` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `sl_re022c_17` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_17` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_17` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_17` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_17` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_17` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_17` | Current wage if still employed | `Numeric(Int)` | `%10.0g` |
| `sl_re028c_17` | Currency of current wage - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_re031_17` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_17` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re033_17` | Done in gap after leaving this job | `Numeric(Byte)` | `%45.0g` |
| `sl_re034d1_17` | Income during gap after leaving job 17: financial support from spouse/partner | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d2_17` | Income during gap after leaving job 17: financial support from family/friends | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d3_17` | Income during gap after leaving job 17: private or public disability insurance | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d4_17` | Income during gap after leaving job 17: benefits or grants from state | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d5_17` | Income during gap after leaving job 17: sold property | `Numeric(Byte)` | `%12.0g` |
| `sl_re034d6_17` | Income during gap after leaving job 17: running down asset or bank account | `Numeric(Byte)` | `%12.0g` |
| `sl_re034dot_17` | Income during gap after leaving job 17: other | `Numeric(Byte)` | `%12.0g` |
| `sl_re011_18` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_18` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_18` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_18` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_18` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_18` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re018_18` | When changed to part-time | `Numeric(Int)` | `%10.0g` |
| `sl_re019_18` | Reasons changing to part-time | `Numeric(Byte)` | `%45.0g` |
| `sl_re021_18` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `sl_re022c_18` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_18` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_18` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_18` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_18` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_18` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re027_18` | Current wage if still employed | `Numeric(Int)` | `%10.0g` |
| `sl_re028c_18` | Currency of current wage - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_re031_18` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_18` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re011_19` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_19` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_19` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_19` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_19` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_19` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re021_19` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `sl_re022c_19` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_19` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_19` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_19` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_19` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_19` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re031_19` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re032_19` | Gap after leaving this job | `Numeric(Byte)` | `%64.0g` |
| `sl_re011_20` | Year started job | `Numeric(Int)` | `%10.0g` |
| `sl_re012isco_20` | ISCO-08 code: Title of job | `Numeric(Int)` | `%14.0g` |
| `sl_re013_20` | Job description | `Numeric(Byte)` | `%38.0g` |
| `sl_re014_20` | Job industry | `Numeric(Byte)` | `%44.0g` |
| `sl_re015_20` | Was employee civil servant or self | `Numeric(Byte)` | `%53.0g` |
| `sl_re016_20` | Job was part or full time | `Numeric(Byte)` | `%40.0g` |
| `sl_re021_20` | First monthly wage in job | `Numeric(Long)` | `%10.0g` |
| `sl_re022c_20` | Currency of wage - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re025d1_20` | Contributions to retirement plans: public pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d2_20` | Contributions to retirement plans: occupational pension plan | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d3_20` | Contributions to retirement plans: private pension plan/individual retirement pl | `Numeric(Byte)` | `%12.0g` |
| `sl_re025d4_20` | Contributions to retirement plans: no contributions paid | `Numeric(Byte)` | `%12.0g` |
| `sl_re026_20` | Year stopped in this job | `Numeric(Int)` | `%17.0g` |
| `sl_re031_20` | Reasons left job | `Numeric(Byte)` | `%34.0g` |
| `sl_re035_1` | Situation in after last job | `Numeric(Byte)` | `%45.0g` |
| `sl_re035a_1` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `sl_re036_1` | Pension benefit when retired | `Numeric(Double)` | `%10.0g` |
| `sl_re037c_1` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re038_1` | Paid job after retirement | `Numeric(Byte)` | `%10.0g` |
| `sl_re039_1` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `sl_re039a_1` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `sl_re035_2` | Situation in after last job | `Numeric(Byte)` | `%45.0g` |
| `sl_re035a_2` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `sl_re036_2` | Pension benefit when retired | `Numeric(Double)` | `%10.0g` |
| `sl_re037c_2` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re039_2` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `sl_re039a_2` | Year changing situation after last job | `Numeric(Int)` | `%12.0g` |
| `sl_re035_3` | Situation in after last job | `Numeric(Byte)` | `%45.0g` |
| `sl_re035a_3` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `sl_re036_3` | Pension benefit when retired | `Numeric(Long)` | `%10.0g` |
| `sl_re037c_3` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re039_3` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `sl_re039a_3` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `sl_re035_4` | Situation in after last job | `Numeric(Byte)` | `%45.0g` |
| `sl_re035a_4` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `sl_re036_4` | Pension benefit when retired | `Numeric(Long)` | `%10.0g` |
| `sl_re037c_4` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re039_4` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `sl_re039a_4` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `sl_re035_5` | Situation in after last job | `Numeric(Byte)` | `%45.0g` |
| `sl_re035a_5` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `sl_re036_5` | Pension benefit when retired | `Numeric(Long)` | `%10.0g` |
| `sl_re037c_5` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re039_5` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `sl_re039a_5` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `sl_re035_6` | Situation in after last job | `Numeric(Byte)` | `%45.0g` |
| `sl_re035a_6` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `sl_re036_6` | Pension benefit when retired | `Numeric(Int)` | `%10.0g` |
| `sl_re037c_6` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re039_6` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `sl_re039a_6` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `sl_re035_7` | Situation in after last job | `Numeric(Byte)` | `%45.0g` |
| `sl_re035a_7` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `sl_re036_7` | Pension benefit when retired | `Numeric(Long)` | `%10.0g` |
| `sl_re037c_7` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re039_7` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `sl_re039a_7` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `sl_re035_8` | Situation in after last job | `Numeric(Byte)` | `%45.0g` |
| `sl_re039_8` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `sl_re039a_8` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `sl_re035_9` | Situation in after last job | `Numeric(Byte)` | `%45.0g` |
| `sl_re035a_9` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `sl_re036_9` | Pension benefit when retired | `Numeric(Int)` | `%10.0g` |
| `sl_re037c_9` | Currency of pension benefit - coded | `Numeric(Byte)` | `%63.0g` |
| `sl_re039_9` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `sl_re039a_9` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `sl_re035_10` | Situation in after last job | `Numeric(Byte)` | `%45.0g` |
| `sl_re035a_10` | Receive retirement benefits | `Numeric(Byte)` | `%10.0g` |
| `sl_re036_10` | Pension benefit when retired | `Numeric(Int)` | `%10.0g` |
| `sl_re037c_10` | Currency of pension benefit - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re039_10` | Has situation changed after last job | `Numeric(Byte)` | `%10.0g` |
| `sl_re039a_10` | Year changing situation after last job | `Numeric(Int)` | `%10.0g` |
| `sl_re040_` | Which was main job in career | `Numeric(Byte)` | `%10.0g` |
| `sl_re041_` | Wage at end of main job | `Numeric(Double)` | `%10.0g` |
| `sl_re042c` | Currency of wage at end of main job - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re043_` | Work income at end of main job | `Numeric(Double)` | `%10.0g` |
| `sl_re044c` | Currency of work income at end of main job - coded | `Numeric(Int)` | `%63.0g` |
| `sl_re046_` | Number of jobs r had | `Numeric(Byte)` | `%10.0g` |
| `sl_re047_` | R is still working | `Numeric(Byte)` | `%10.0g` |
| `sl_re048_` | Proxy check | `Numeric(Byte)` | `%20.0g` |
| `sl_re022_1_curRefPer_flag` | Currency string includes information about reference period | `Numeric(Byte)` | `%9.0g` |
| `sl_re022_1_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Int)` | `%22.0g` |
| `sl_re022_2_curRefPer_flag` | Currency string includes information about reference period | `Numeric(Byte)` | `%9.0g` |
| `sl_re022_2_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_re022_3_curRefPer_flag` | Currency string includes information about reference period | `Numeric(Byte)` | `%9.0g` |
| `sl_re022_3_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_re022_4_curRefPer_flag` | Currency string includes information about reference period | `Numeric(Byte)` | `%9.0g` |
| `sl_re022_4_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Int)` | `%22.0g` |
| `sl_re022_5_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_re022_6_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_re022_8_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_re024_1_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_re024_2_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_re024_3_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_re028_2_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |
| `sl_re028_3_curRefPer_flag` | Currency string includes information about reference period | `Numeric(Byte)` | `%9.0g` |
| `sl_re037_1_curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Int)` | `%22.0g` |
| `sl_re042__curRefPer_flag` | Currency string includes information about reference period | `Numeric(Byte)` | `%9.0g` |
| `sl_re042__curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Int)` | `%22.0g` |
| `sl_re044__curScale_flag` | Currency string includes scaling information (e.g. times 1000) | `Numeric(Byte)` | `%22.0g` |

### `rp` - Retrospective Partner History

- Dataset: `sharew3_rel9-0-0_rp.dta`
- Read with: `ps.read_share_module("rp", wave=3)`
- Rows: 28,454
- Variables: 127
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sl_rp002_` | Ever been married | `Numeric(Byte)` | `%10.0g` |
| `sl_rp002d_` | Ever had unmarried partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp002e_` | How often married | `Numeric(Byte)` | `%10.0g` |
| `sl_rp004c_1` | When relationship start | `Numeric(Int)` | `%12.0g` |
| `sl_rp008_1` | Year married | `Numeric(Int)` | `%12.0g` |
| `sl_rp004b_1` | Year started living with married partner | `Numeric(Int)` | `%20.0g` |
| `sl_rp009_1` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp010_1` | Reasons for not living with partner | `Numeric(Byte)` | `%42.0g` |
| `sl_rp011_1` | Year of death partner | `Numeric(Int)` | `%12.0g` |
| `sl_rp012_1` | Year stopped living with partner | `Numeric(Int)` | `%12.0g` |
| `sl_rp013_1` | Divorced partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp014_1` | Year of divorce | `Numeric(Int)` | `%12.0g` |
| `sl_rp004c_2` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `sl_rp008_2` | Year married | `Numeric(Int)` | `%10.0g` |
| `sl_rp004b_2` | Year started living with married partner | `Numeric(Int)` | `%20.0g` |
| `sl_rp009_2` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp010_2` | Reasons for not living with partner | `Numeric(Byte)` | `%42.0g` |
| `sl_rp011_2` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp012_2` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp013_2` | Divorced partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp014_2` | Year of divorce | `Numeric(Int)` | `%10.0g` |
| `sl_rp004c_3` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `sl_rp008_3` | Year married | `Numeric(Int)` | `%10.0g` |
| `sl_rp004b_3` | Year started living with married partner | `Numeric(Int)` | `%20.0g` |
| `sl_rp009_3` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp010_3` | Reasons for not living with partner | `Numeric(Byte)` | `%42.0g` |
| `sl_rp011_3` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp012_3` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp013_3` | Divorced partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp014_3` | Year of divorce | `Numeric(Int)` | `%10.0g` |
| `sl_rp004c_4` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `sl_rp008_4` | Year married | `Numeric(Int)` | `%10.0g` |
| `sl_rp004b_4` | Year started living with married partner | `Numeric(Int)` | `%20.0g` |
| `sl_rp009_4` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp010_4` | Reasons for not living with partner | `Numeric(Byte)` | `%42.0g` |
| `sl_rp012_4` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp013_4` | Divorced partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp014_4` | Year of divorce | `Numeric(Int)` | `%10.0g` |
| `sl_rp004c_5` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `sl_rp008_5` | Year married | `Numeric(Int)` | `%10.0g` |
| `sl_rp004b_5` | Year started living with married partner | `Numeric(Int)` | `%20.0g` |
| `sl_rp009_5` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp004c_6` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `sl_rp008_6` | Year married | `Numeric(Int)` | `%10.0g` |
| `sl_rp004b_6` | Year started living with married partner | `Numeric(Int)` | `%20.0g` |
| `sl_rp009_6` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp004c_11` | When relationship start | `Numeric(Int)` | `%12.0g` |
| `sl_rp003_11` | Year started living with partner | `Numeric(Int)` | `%12.0g` |
| `sl_rp009_11` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp010_11` | Reasons for not living with partner | `Numeric(Byte)` | `%42.0g` |
| `sl_rp011_11` | Year of death partner | `Numeric(Int)` | `%12.0g` |
| `sl_rp012_11` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp015a_11` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `sl_rp004c_12` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `sl_rp003_12` | Year started living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp009_12` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp010_12` | Reasons for not living with partner | `Numeric(Byte)` | `%42.0g` |
| `sl_rp011_12` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp012_12` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp015a_12` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `sl_rp004c_13` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `sl_rp003_13` | Year started living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp009_13` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp010_13` | Reasons for not living with partner | `Numeric(Byte)` | `%42.0g` |
| `sl_rp011_13` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp012_13` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp015a_13` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `sl_rp004c_14` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `sl_rp003_14` | Year started living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp009_14` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp010_14` | Reasons for not living with partner | `Numeric(Byte)` | `%42.0g` |
| `sl_rp011_14` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp012_14` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp015a_14` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `sl_rp004c_15` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `sl_rp003_15` | Year started living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp009_15` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp010_15` | Reasons for not living with partner | `Numeric(Byte)` | `%42.0g` |
| `sl_rp011_15` | Year of death partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp012_15` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp015a_15` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `sl_rp004c_16` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `sl_rp003_16` | Year started living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp009_16` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp010_16` | Reasons for not living with partner | `Numeric(Byte)` | `%42.0g` |
| `sl_rp012_16` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp015a_16` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `sl_rp004c_17` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `sl_rp003_17` | Year started living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp009_17` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp010_17` | Reasons for not living with partner | `Numeric(Byte)` | `%42.0g` |
| `sl_rp012_17` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp015a_17` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `sl_rp004c_18` | When relationship start | `Numeric(Int)` | `%10.0g` |
| `sl_rp003_18` | Year started living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp009_18` | Still living with partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp010_18` | Reasons for not living with partner | `Numeric(Byte)` | `%42.0g` |
| `sl_rp012_18` | Year stopped living with partner | `Numeric(Int)` | `%10.0g` |
| `sl_rp015a_18` | Any other cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `sl_rp016_` | Non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `sl_rp017_1` | Start non-cohabitating partnership | `Numeric(Int)` | `%12.0g` |
| `sl_rp019_1` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp020_1` | End non-cohabitating partnership | `Numeric(Int)` | `%12.0g` |
| `sl_rp021_1` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `sl_rp017_2` | Start non-cohabitating partnership | `Numeric(Int)` | `%12.0g` |
| `sl_rp019_2` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp020_2` | End non-cohabitating partnership | `Numeric(Int)` | `%12.0g` |
| `sl_rp021_2` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `sl_rp017_3` | Start non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `sl_rp019_3` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp020_3` | End non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `sl_rp021_3` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `sl_rp017_4` | Start non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `sl_rp019_4` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp020_4` | End non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `sl_rp021_4` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `sl_rp017_5` | Start non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `sl_rp019_5` | Still in a relationship with non-cohabitating partner | `Numeric(Byte)` | `%10.0g` |
| `sl_rp020_5` | End non-cohabitating partnership | `Numeric(Int)` | `%10.0g` |
| `sl_rp021_5` | Any other non cohabitating partners | `Numeric(Byte)` | `%10.0g` |
| `sl_rp023_` | Proxy check | `Numeric(Byte)` | `%20.0g` |

### `st` - SHARELIFE demographics

- Dataset: `sharew3_rel9-0-0_st.dta`
- Read with: `ps.read_share_module("st", wave=3)`
- Rows: 28,454
- Variables: 12
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sl_st006_` | Month of birth of respondent | `Numeric(Byte)` | `%10.0g` |
| `sl_st007_` | Year of birth of respondent | `Numeric(Int)` | `%10.0g` |
| `sl_st011_` | Gender of respondent | `Numeric(Byte)` | `%10.0g` |
| `sl_st001a_` | Check if proxy | `Numeric(Byte)` | `%20.0g` |
| `sl_st001b_` | Validate proxy | `Numeric(Byte)` | `%10.0g` |
| `sl_st016_` | Proxy check | `Numeric(Byte)` | `%20.0g` |

### `wq` - Work Quality

- Dataset: `sharew3_rel9-0-0_wq.dta`
- Read with: `ps.read_share_module("wq", wave=3)`
- Rows: 28,454
- Variables: 258
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `sl_wq016_1` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_1` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_1` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_1` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_1` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_1` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_1` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_1` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_1` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_1` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_1` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_1` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_1` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_2` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_2` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_2` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_2` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_2` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_2` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_2` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_2` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_2` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_2` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_2` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_2` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_2` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_3` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_3` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_3` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_3` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_3` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_3` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_3` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_3` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_3` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_3` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_3` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_3` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_3` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_4` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_4` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_4` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_4` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_4` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_4` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_4` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_4` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_4` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_4` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_4` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_4` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_4` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_5` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_5` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_5` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_5` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_5` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_5` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_5` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_5` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_5` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_5` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_5` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_5` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_5` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_6` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_6` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_6` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_6` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_6` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_6` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_6` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_6` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_6` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_6` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_6` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_6` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_6` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_7` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_7` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_7` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_7` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_7` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_7` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_7` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_7` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_7` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_7` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_7` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_7` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_7` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_8` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_8` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_8` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_8` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_8` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_8` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_8` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_8` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_8` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_8` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_8` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_8` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_8` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_9` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_9` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_9` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_9` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_9` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_9` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_9` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_9` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_9` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_9` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_9` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_9` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_9` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_10` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_10` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_10` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_10` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_10` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_10` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_10` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_10` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_10` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_10` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_10` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_10` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_10` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_11` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_11` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_11` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_11` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_11` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_11` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_11` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_11` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_11` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_11` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_11` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_11` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_11` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_12` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_12` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_12` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_12` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_12` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_12` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_12` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_12` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_12` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_12` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_12` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_12` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_12` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_13` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_13` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_13` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_13` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_13` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_13` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_13` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_13` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_13` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_13` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_13` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_13` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_13` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_14` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_14` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_14` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_14` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_14` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_14` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_14` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_14` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_14` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_14` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_14` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_14` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_14` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_15` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_15` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_15` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_15` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_15` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_15` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_15` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_15` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_15` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_15` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_15` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_15` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_15` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_16` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_16` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_16` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_16` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_16` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_16` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_16` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_16` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_16` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_16` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_16` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_16` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_16` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_17` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_17` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_17` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_17` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_17` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_17` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_17` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_17` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_17` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_17` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_17` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_17` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_17` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq016_18` | Work is physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq017_18` | Work is uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq018_18` | Work has heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq019_18` | Work is emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq020_18` | Work involves conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq021_18` | Work has little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq022_18` | Work allows development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq023_18` | Work gives recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq024_18` | Work has adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq025_18` | Work has adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq026_18` | Current work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq027_18` | Work employees are treated fairly | `Numeric(Byte)` | `%17.0g` |
| `sl_wq028_18` | Current work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq002_` | Work was physically demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq003_` | Work was uncomfortable | `Numeric(Byte)` | `%17.0g` |
| `sl_wq004_` | Work had heavy time pressure | `Numeric(Byte)` | `%17.0g` |
| `sl_wq005_` | Work was emotionally demanding | `Numeric(Byte)` | `%17.0g` |
| `sl_wq006_` | Work involved conflicts | `Numeric(Byte)` | `%17.0g` |
| `sl_wq007_` | Work had little freedom to decide | `Numeric(Byte)` | `%17.0g` |
| `sl_wq008_` | Work allowed development of skills | `Numeric(Byte)` | `%17.0g` |
| `sl_wq009_` | Work gave recognition | `Numeric(Byte)` | `%17.0g` |
| `sl_wq010_` | Work had adequate salary | `Numeric(Byte)` | `%17.0g` |
| `sl_wq011_` | Work had adequate support | `Numeric(Byte)` | `%17.0g` |
| `sl_wq012_` | Work atmosphere | `Numeric(Byte)` | `%17.0g` |
| `sl_wq013_` | Work employees treated fair | `Numeric(Byte)` | `%17.0g` |
| `sl_wq014_` | Work health risk reduced | `Numeric(Byte)` | `%17.0g` |
| `sl_wq030_` | Satisfaction with job career | `Numeric(Byte)` | `%17.0g` |
| `sl_wq031_` | Had disappointing job career | `Numeric(Byte)` | `%17.0g` |
| `sl_wq032_` | Satisfied with achievements | `Numeric(Byte)` | `%17.0g` |
| `sl_wq033_` | Sacrificed too much for job | `Numeric(Byte)` | `%17.0g` |
| `sl_wq035_` | Health has suffered at work | `Numeric(Byte)` | `%17.0g` |


## Generated Modules

### `gv_exrates` - Exchange rates and PPP variables

- Dataset: `sharew3_rel9-0-0_gv_exrates.dta`
- Read with: `ps.read_share_module("gv_exrates", wave=3)`
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

### `gv_weights` - Cross-sectional weights

- Dataset: `sharew3_rel9-0-0_gv_weights.dta`
- Read with: `ps.read_share_module("gv_weights", wave=3)`
- Rows: 28,454
- Variables: 14
- Key hint: `mergeid`

| Variable | Label | Type | Format |
| --- | --- | --- | --- |
| `mergeid` | Person identifier (fix across modules and waves) | `Str(12)` | `%12s` |
| `hhid3` | Household identifier (wave 3) | `Str(11)` | `%11s` |
| `mergeidp3` | Partner identifier (wave 3) | `Str(12)` | `%12s` |
| `coupleid3` | Couple identifier (wave 3) | `Str(15)` | `%15s` |
| `country` | Country identifier | `Numeric(Byte)` | `%14.0g` |
| `language` | Language of questionnaire | `Numeric(Byte)` | `%44.0g` |
| `dw_w3` | Design weight - wave 3 | `Numeric(Double)` | `%10.0g` |
| `cchw_w3` | Calibrated cross-sectional household weight - wave 3 | `Numeric(Double)` | `%10.0g` |
| `cciw_w3` | Calibrated cross-sectional individual weight - wave 3 | `Numeric(Double)` | `%10.0g` |
| `subsample` | Indicator for country-specific subsample | `Str(6)` | `%9s` |
| `stratum1` | Indicator for primary stratum (if any) | `Str(9)` | `%9s` |
| `stratum2` | Indicator for secondary stratum (if any) | `Str(4)` | `%9s` |
| `psu` | Primary sampling unit | `Str(9)` | `%9s` |
| `ssu` | Secondary sampling unit (if any) | `Str(5)` | `%9s` |
