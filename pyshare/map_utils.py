MAP_YES_NO: dict[int, bool] = {1: True, 5: False}

MAP_CANCER: dict[int, bool] = {0: False, 1: True}

MAP_GENDER: dict[int, str] = {1: "Male", 2: "Female"}

MAP_COMPUTER_SKILLS: dict[int, str] = {
    1: "Excellent",
    2: "Very good",
    3: "Good",
    4: "Fair",
    5: "Poor",
    6: "Never used a computer",
}

MAP_HEALTH_LITERACY_HELP: dict[int, str] = {
    1: "Always",
    2: "Often",
    3: "Sometimes",
    4: "Rarely",
    5: "Never",
}

MAP_ENDS_MEET: dict[int, str] = {
    1: "With great difficulty",
    2: "With some difficulty",
    3: "Fairly easily",
    4: "Easily",
}

MAP_ISCED_1997: dict[int, str] = {
    0: "Pre-primary",
    1: "Primary",
    2: "Lower secondary",
    3: "Upper secondary",
    4: "Post-secondary non-tertiary",
    5: "First stage tertiary",
    6: "Second stage tertiary",
}

MAP_SHARE_MISSING_CODES: list[int] = [-1, -2, -3, -4, -5, -7, -9]

MAP_SHARE_FINANCIAL_MISSING_CODES: list[int] = [-9999991, -9999992]

MAP_ID_TO_COUNTRY: dict[int, str] = {
    11: "Austria",
    12: "Germany",
    13: "Sweden",
    14: "Netherlands",
    15: "Spain",
    16: "Italy",
    17: "France",
    18: "Denmark",
    19: "Greece",
    20: "Switzerland",
    23: "Belgium",
    25: "Israel",
    28: "Czech Republic",
    29: "Poland",
    30: "Ireland",
    31: "Luxembourg",
    32: "Hungary",
    33: "Portugal",
    34: "Slovenia",
    35: "Estonia",
    47: "Croatia",
    48: "Lithuania",
    51: "Bulgaria",
    53: "Cyprus",
    55: "Finland",
    57: "Latvia",
    59: "Malta",
    61: "Romania",
    63: "Slovakia",
}
