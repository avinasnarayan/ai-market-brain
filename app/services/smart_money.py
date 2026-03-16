import yfinance as yf


def analyze_option_chain():

    try:

        ticker = yf.Ticker("NIFTYBEES.NS")

        expiries = ticker.options

        if len(expiries) == 0:
            return {"error": "Options data unavailable"}

        expiry = expiries[0]

        opt = ticker.option_chain(expiry)

        calls = opt.calls
        puts = opt.puts

        total_call_oi = calls["openInterest"].sum()
        total_put_oi = puts["openInterest"].sum()

        if total_call_oi == 0:
            return {"error": "Invalid options data"}

        pcr = total_put_oi / total_call_oi

        call_max = calls.loc[calls["openInterest"].idxmax()]
        put_max = puts.loc[puts["openInterest"].idxmax()]

        resistance = int(call_max["strike"])
        support = int(put_max["strike"])

        max_pain = int((support + resistance) / 2)

        if pcr > 1:
            bias = "Bullish"
        elif pcr < 0.8:
            bias = "Bearish"
        else:
            bias = "Neutral"

        return {

            "smart_money_bias": bias,
            "pcr": round(float(pcr), 2),
            "support": support,
            "resistance": resistance,
            "max_pain": max_pain

        }

    except Exception as e:

        return {"error": str(e)}