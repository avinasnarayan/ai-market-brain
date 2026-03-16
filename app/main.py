import requests


def fetch_option_chain():

    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive"
    }

    session = requests.Session()

    # First visit homepage to obtain cookies
    session.get("https://www.nseindia.com", headers=headers)

    response = session.get(url, headers=headers)

    if response.status_code != 200:
        return None

    return response.json()


def analyze_option_chain():

    try:

        data = fetch_option_chain()

        if not data or "records" not in data:
            return {"error": "Option chain data unavailable"}

        strikes = data["records"]["data"]

        total_ce_oi = 0
        total_pe_oi = 0

        max_ce_oi = 0
        max_pe_oi = 0

        resistance = None
        support = None

        for item in strikes:

            strike = item.get("strikePrice")

            ce = item.get("CE")
            pe = item.get("PE")

            if ce:

                ce_oi = ce.get("openInterest", 0)

                total_ce_oi += ce_oi

                if ce_oi > max_ce_oi:
                    max_ce_oi = ce_oi
                    resistance = strike

            if pe:

                pe_oi = pe.get("openInterest", 0)

                total_pe_oi += pe_oi

                if pe_oi > max_pe_oi:
                    max_pe_oi = pe_oi
                    support = strike

        if total_ce_oi == 0:
            return {"error": "Invalid option chain data"}

        pcr = total_pe_oi / total_ce_oi

        if pcr > 1:
            bias = "Bullish"
        elif pcr < 0.8:
            bias = "Bearish"
        else:
            bias = "Neutral"

        max_pain = None

        if support and resistance:
            max_pain = (support + resistance) / 2

        return {

            "smart_money_bias": bias,
            "pcr": round(pcr, 2),
            "support": support,
            "resistance": resistance,
            "max_pain": max_pain

        }

    except Exception as e:

        return {"error": str(e)}