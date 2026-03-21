import pandas as pd


def market_trend():

    df = pd.read_csv("data/crypto_history.csv")

    df["date"] = pd.to_datetime(df["date"])   # important

    trend = df.groupby("date")["market_cap"].sum()

    print("\nMarket Trend Over Time!!!!")
    print(trend)

    return trend