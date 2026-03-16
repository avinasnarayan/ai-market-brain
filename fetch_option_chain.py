import requests
import time

SERVER_URL = "https://ai-market-brain-production-0891.up.railway.app/update-option-chain"


def fetch_market_data():

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
            return None

        nifty_change = nifty["percentChange"]
        bank_change = banknifty["percentChange"]

        avg = (nifty_change + bank_change) / 2

        if avg > 0.5:
            bias = "Bullish"
        elif avg < -0.5:
            bias = "Bearish"
        else:
            bias = "Neutral"

        return {
            "smart_money_bias": bias,
            "pcr": None,
            "support": None,
            "resistance": None,
            "max_pain": None
        }

    except Exception as e:

        print("Fetch error:", e)
        return None


while True:

    result = fetch_market_data()

    if result:

        try:

            r = requests.post(SERVER_URL, json=result)

            print("Market bias updated:", result)

        except Exception as e:

            print("Server update failed:", e)

    else:

        print("Market fetch failed")

    time.sleep(300)