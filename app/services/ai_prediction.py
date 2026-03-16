import joblib
import yfinance as yf
import pandas as pd

model = joblib.load("model.pkl")

def predict_market():

    data = yf.download("^NSEI", period="20d", interval="1d")

    data["return"] = data["Close"].pct_change()

    data["ma5"] = data["Close"].rolling(5).mean()
    data["ma10"] = data["Close"].rolling(10).mean()
    data["volatility"] = data["return"].rolling(5).std()

    data = data.dropna()

    latest = data.iloc[-1][["ma5","ma10","volatility"]]

    prediction = model.predict([latest])[0]

    confidence = model.predict_proba([latest]).max()

    if prediction == 1:
        direction = "Bullish"
    else:
        direction = "Bearish"

    return {
        "prediction": direction,
        "confidence": round(confidence*100,2)
    }