import yfinance as yf


def get_global_data():

    sp500 = yf.download("^GSPC", period="2d", interval="1d")
    nasdaq = yf.download("^IXIC", period="2d", interval="1d")
    dow = yf.download("^DJI", period="2d", interval="1d")
    oil = yf.download("CL=F", period="2d", interval="1d")
    vix = yf.download("^VIX", period="2d", interval="1d")

    sp_change = (sp500["Close"].iloc[-1] - sp500["Close"].iloc[-2]) / sp500["Close"].iloc[-2]
    nas_change = (nasdaq["Close"].iloc[-1] - nasdaq["Close"].iloc[-2]) / nasdaq["Close"].iloc[-2]
    dow_change = (dow["Close"].iloc[-1] - dow["Close"].iloc[-2]) / dow["Close"].iloc[-2]
    oil_change = (oil["Close"].iloc[-1] - oil["Close"].iloc[-2]) / oil["Close"].iloc[-2]

    vix_value = float(vix["Close"].iloc[-1])

    return sp_change, nas_change, dow_change, oil_change, vix_value


def macro_prediction():

    sp, nas, dow, oil, vix = get_global_data()

    score = 0

    score += sp * 100
    score += nas * 100
    score += dow * 100
    score -= vix

    if score > 2:
        outlook = "Bullish"
    elif score < -2:
        outlook = "Bearish"
    else:
        outlook = "Neutral"

    gap_probability = min(max(abs(score) * 10, 10), 90)

    return {

        "nifty_outlook": outlook,

        "banknifty_outlook": outlook,

        "gap_probability": round(gap_probability, 2),

        "confidence": round(min(abs(score) * 20, 85), 2)
    }