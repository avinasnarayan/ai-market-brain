import ta
import pandas as pd


def analyze_market(df):

    if df is None or df.empty:
        return {"price": None, "rsi": None, "momentum": None}

    # Fix Yahoo dataframe column shape
    close = df["Close"]

    # Convert 2D array to Series if needed
    if isinstance(close, pd.DataFrame):
        close = close.squeeze()

    df["rsi"] = ta.momentum.RSIIndicator(close, window=14).rsi()

    latest_price = close.iloc[-1]
    prev_price = close.iloc[-2]

    rsi = df["rsi"].iloc[-1]

    momentum = "UP" if latest_price > prev_price else "DOWN"

    return {
        "price": float(latest_price),
        "rsi": float(rsi),
        "momentum": momentum
    }