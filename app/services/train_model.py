import pandas as pd
import yfinance as yf
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():

    data = yf.download("^NSEI", period="1y", interval="1d")

    data["return"] = data["Close"].pct_change()
    data["direction"] = (data["return"] > 0).astype(int)

    data["ma5"] = data["Close"].rolling(5).mean()
    data["ma10"] = data["Close"].rolling(10).mean()
    data["volatility"] = data["return"].rolling(5).std()

    data = data.dropna()

    features = data[["ma5","ma10","volatility"]]
    target = data["direction"]

    model = RandomForestClassifier()

    model.fit(features, target)

    joblib.dump(model, "model.pkl")

    print("Model trained")

if __name__ == "__main__":
    train_model()