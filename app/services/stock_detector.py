STOCK_KEYWORDS = {

    "Reliance": ["reliance", "ril"],
    "TCS": ["tcs", "tata consultancy"],
    "Infosys": ["infosys"],
    "HDFC Bank": ["hdfc"],
    "ICICI Bank": ["icici"],
    "SBI": ["state bank of india", "sbi"],

    "Tesla": ["tesla"],
    "Apple": ["apple"],
    "Microsoft": ["microsoft"],
    "Google": ["google", "alphabet"],
    "Amazon": ["amazon"]

}


def detect_stocks(text):

    text = text.lower()

    detected = []

    for stock, keywords in STOCK_KEYWORDS.items():

        for keyword in keywords:

            if keyword in text:
                detected.append(stock)
                break

    return detected