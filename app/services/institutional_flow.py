import requests


def get_institutional_flow():

    try:

        url = "https://www.nseindia.com/api/allIndices"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(url, headers=headers)

        data = r.json()

        indices = data["data"]

        nifty = None
        banknifty = None

        for i in indices:

            if i["index"] == "NIFTY 50":
                nifty = i

            if i["index"] == "NIFTY BANK":
                banknifty = i

        if not nifty or not banknifty:
            return {"error": "Index data unavailable"}

        nifty_change = nifty["percentChange"]
        bank_change = banknifty["percentChange"]

        avg = (nifty_change + bank_change) / 2

        if avg > 0.5:

            bias = "Bullish"
            fii = "Buying"
            dii = "Selling"

        elif avg < -0.5:

            bias = "Bearish"
            fii = "Selling"
            dii = "Buying"

        else:

            bias = "Neutral"
            fii = "Neutral"
            dii = "Neutral"

        confidence = round(abs(avg) * 100)

        return {

            "institutional_bias": bias,
            "fii_activity": fii,
            "dii_activity": dii,
            "confidence": confidence,
            "nifty_change": nifty_change,
            "banknifty_change": bank_change

        }

    except Exception as e:

        return {"error": str(e)}