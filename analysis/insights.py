def generate_insights(df):
    top_coin = df.loc[df["market_cap"].idxmax()]
    top_gainer = df.loc[df["price_change_percentage_24h"].idxmax()]
    highest_volume = df.loc[df["total_volume"].idxmax()]

    print("\n----- Market Insights -----")

    print("\nTop Coin by Market Cap:")
    print(top_coin["name"], top_coin["market_cap"])

    print("\nTop Gainer Today:")
    print(top_gainer["name"], f"{top_gainer['price_change_percentage_24h']:.2f}%")

    print("\nHighest Trading Volume:")
    print(highest_volume["name"], highest_volume["total_volume"])