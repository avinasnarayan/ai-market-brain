import yfinance as yf


def get_index_data():

    nifty = yf.download("^NSEI", period="1d", interval="5m")
    banknifty = yf.download("^NSEBANK", period="1d", interval="5m")

    return nifty, banknifty