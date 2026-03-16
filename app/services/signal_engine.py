import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator


def generate_signal():

    try:

        data = yf.download("^NSEBANK", period="5d", interval="5m")

        if data.empty:
            return {"error": "Market data unavailable"}

        df = pd.DataFrame(data)

        df["Close"] = df["Close"].squeeze()

        df["ema9"] = EMAIndicator(close=df["Close"], window=9).ema_indicator()
        df["ema20"] = EMAIndicator(close=df["Close"], window=20).ema_indicator()
        df["rsi"] = RSIIndicator(close=df["Close"], window=14).rsi()

        df = df.dropna()

        latest = df.iloc[-1]

        price = float(latest["Close"])
        ema9 = float(latest["ema9"])
        ema20 = float(latest["ema20"])
        rsi = float(latest["rsi"])

        signal = "NO TRADE"
        confidence = 50

        if ema9 > ema20 and rsi > 55:
            signal = "BUY CE"
            confidence = 70

        elif ema9 < ema20 and rsi < 45:
            signal = "BUY PE"
            confidence = 70

        entry = round(price, 2)
        target = round(price * 1.01, 2)
        stoploss = round(price * 0.995, 2)

        return {
            "symbol": "BANKNIFTY",
            "signal": signal,
            "entry": entry,
            "target": target,
            "stoploss": stoploss,
            "confidence": confidence
        }

    except Exception as e:

        return {
            "error": str(e)
        }