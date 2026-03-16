import requests


def analyze_option_chain():

    try:

        session = requests.Session()

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
        }

        # First request to get cookies
        session.get("https://www.nseindia.com", headers=headers)

        url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

        response = session.get(url, headers=headers)

        data = response.json()

        if "records" not in data:
            return {"error": "NSE response invalid"}

        strikes = data["records"]["data"]

        total_ce = 0
        total_pe = 0

        max_ce = 0
        max_pe = 0

        resistance = None
        support = None

        for item in strikes:

            strike = item["strikePrice"]

            ce = item.get("CE")
            pe = item.get("PE")

            if ce:

                ce_oi = ce["openInterest"]
                total_ce += ce_oi

                if ce_oi > max_ce:
                    max_ce = ce_oi
                    resistance = strike

            if pe:

                pe_oi = pe["openInterest"]
                total_pe += pe_oi

                if pe_oi > max_pe:
                    max_pe = pe_oi
                    support = strike

        if total_ce == 0:
            return {"error": "Invalid option chain"}

        pcr = total_pe / total_ce

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