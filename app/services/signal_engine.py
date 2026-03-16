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

        # FIX → convert to 1D series
        close = df["Close"].values.flatten()

        close_series = pd.Series(close)

        ema9 = EMAIndicator(close_series, window=9).ema_indicator()
        ema20 = EMAIndicator(close_series, window=20).ema_indicator()
        rsi = RSIIndicator(close_series, window=14).rsi()

        price = float(close_series.iloc[-1])
        ema9_val = float(ema9.iloc[-1])
        ema20_val = float(ema20.iloc[-1])
        rsi_val = float(rsi.iloc[-1])

        signal = "NO TRADE"
        confidence = 50

        if ema9_val > ema20_val and rsi_val > 55:
            signal = "BUY CE"
            confidence = 70

        elif ema9_val < ema20_val and rsi_val < 45:
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

        return {"error": str(e)}