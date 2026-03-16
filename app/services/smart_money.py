import requests


def fetch_option_chain():
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/option-chain",
        "Connection": "keep-alive",
    }

    session = requests.Session()

    # Get cookies
    session.get("https://www.nseindia.com", headers=headers, timeout=10)

    response = session.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        return None

    try:
        return response.json()
    except Exception:
        return None


def analyze_option_chain():

    try:

        data = fetch_option_chain()

        if not data:
            return {"error": "Failed to fetch option chain"}

        if "records" not in data:
            return {"error": "Unexpected NSE response format"}

        strikes = data["records"]["data"]

        total_ce = 0
        total_pe = 0

        max_ce = 0
        max_pe = 0

        resistance = None
        support = None

        for item in strikes:

            strike = item.get("strikePrice")

            ce = item.get("CE")
            pe = item.get("PE")

            if ce:
                ce_oi = ce.get("openInterest", 0)
                total_ce += ce_oi

                if ce_oi > max_ce:
                    max_ce = ce_oi
                    resistance = strike

            if pe:
                pe_oi = pe.get("openInterest", 0)
                total_pe += pe_oi

                if pe_oi > max_pe:
                    max_pe = pe_oi
                    support = strike

        if total_ce == 0:
            return {"error": "Invalid option chain data"}

        pcr = total_pe / total_ce

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