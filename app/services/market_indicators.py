import ta


def analyze_market(df):

    df["rsi"] = ta.momentum.RSIIndicator(df["Close"], window=14).rsi()

    latest_price = df["Close"].iloc[-1]
    prev_price = df["Close"].iloc[-2]

    rsi = df["rsi"].iloc[-1]

    momentum = "UP" if latest_price > prev_price else "DOWN"

    return {
        "price": latest_price,
        "rsi": round(rsi, 2),
        "momentum": momentum
    }