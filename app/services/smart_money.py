import requests


def fetch_option_chain():

    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br"
    }

    session = requests.Session()

    session.get("https://www.nseindia.com", headers=headers)

    response = session.get(url, headers=headers)

    data = response.json()

    return data


def analyze_option_chain():

    try:

        data = fetch_option_chain()

        strikes = data["records"]["data"]

        total_ce_oi = 0
        total_pe_oi = 0

        max_ce_oi = 0
        max_pe_oi = 0

        resistance = None
        support = None

        pain = []

        for item in strikes:

            strike = item["strikePrice"]

            if "CE" in item:

                ce_oi = item["CE"]["openInterest"]

                total_ce_oi += ce_oi

                if ce_oi > max_ce_oi:
                    max_ce_oi = ce_oi
                    resistance = strike

            if "PE" in item:

                pe_oi = item["PE"]["openInterest"]

                total_pe_oi += pe_oi

                if pe_oi > max_pe_oi:
                    max_pe_oi = pe_oi
                    support = strike

        pcr = total_pe_oi / total_ce_oi if total_ce_oi else 0

        if pcr > 1:
            bias = "Bullish"
        elif pcr < 0.8:
            bias = "Bearish"
        else:
            bias = "Neutral"

        max_pain = (support + resistance) / 2 if support and resistance else None

        return {

            "smart_money_bias": bias,

            "pcr": round(pcr, 2),

            "support": support,

            "resistance": resistance,

            "max_pain": max_pain
        }

    except Exception as e:

        return {"error": str(e)}