def send_notification(title, sentiment, impact, source, sector, stocks, confidence, confidence_level, brain):

    print("\n")
    print("🚨 AI MARKET ALERT")
    print("--------------------------------")

    print("Title:", title)
    print("Sentiment:", sentiment)
    print("Impact Score:", impact)

    print("Confidence:", confidence, "%", confidence_level)

    print("Sector:", sector)

    if stocks:
        print("Stocks:", ", ".join(stocks))

    print("\nAI Market Brain")

    print("NIFTY RSI:", brain["nifty"]["rsi"])
    print("BANKNIFTY RSI:", brain["banknifty"]["rsi"])

    print("Trade Idea:", brain["trade"])
    print("Confidence:", brain["confidence"])

    print("--------------------------------")