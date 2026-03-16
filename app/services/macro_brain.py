import yfinance as yf
import pandas as pd


def get_change(symbol):

    data = yf.download(symbol, period="2d", interval="1d")

    if data.empty:
        return 0

    close = data["Close"].values.flatten()

    if len(close) < 2:
        return 0

    change = (close[-1] - close[-2]) / close[-2]

    return float(change)


def get_vix():

    data = yf.download("^VIX", period="1d", interval="1d")

    if data.empty:
        return 15

    close = data["Close"].values.flatten()

    return float(close[-1])


def macro_prediction():

    try:

        sp = get_change("^GSPC")
        nas = get_change("^IXIC")
        dow = get_change("^DJI")
        oil = get_change("CL=F")

        vix = get_vix()

        score = 0

        score += sp * 100
        score += nas * 100
        score += dow * 100
        score += oil * 50
        score -= vix * 0.5

        if score > 2:
            outlook = "Bullish"
        elif score < -2:
            outlook = "Bearish"
        else:
            outlook = "Neutral"

        gap_probability = min(max(abs(score) * 10, 10), 90)

        confidence = min(abs(score) * 20, 85)

        return {

            "nifty_outlook": outlook,
            "banknifty_outlook": outlook,
            "gap_probability": round(gap_probability, 2),
            "confidence": round(confidence, 2)

        }

    except Exception as e:

        return {"error": str(e)}