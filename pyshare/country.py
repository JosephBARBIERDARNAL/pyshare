def id_to_country(id: int) -> str:
    country_dict: dict[int, str] = {
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

    return country_dict[id]
