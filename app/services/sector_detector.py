SECTOR_KEYWORDS = {

    "Banking": [
        "bank", "rbi", "interest rate", "loan", "credit"
    ],

    "IT": [
        "software", "technology", "cloud", "ai", "semiconductor"
    ],

    "Oil & Gas": [
        "oil", "crude", "petroleum", "opec", "gas"
    ],

    "Automobile": [
        "auto", "vehicle", "car", "ev", "electric vehicle"
    ],

    "Pharma": [
        "drug", "pharma", "fda", "medicine", "vaccine"
    ],

    "Finance": [
        "insurance", "financial services", "nbfc"
    ]

}


def detect_sector(text):

    text = text.lower()

    for sector, keywords in SECTOR_KEYWORDS.items():

        for keyword in keywords:

            if keyword in text:
                return sector

    return "General"