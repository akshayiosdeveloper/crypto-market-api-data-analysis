from api.fetch_data import fetch_crypto_data
from data.analyse_data import clean_data, top_gainers, top_market_cap
from visualization.plot_data import plot_market_cap, plot_top_gainers, plot_volume
from analysis.insights import generate_insights


def main():
    print("Fetching API Data...")

    df = fetch_crypto_data()

    if df is None:
        return

    df = clean_data(df)

    print("\nTop Gainers")
    gainers = top_gainers(df)
    print(gainers)

    print("\nTop Market Cap Coins")
    top_coins = top_market_cap(df)
    print(top_coins)

    df.to_csv("data/crypto_data.csv", index=False)

    # Generate charts
    plot_market_cap(top_coins)
    plot_top_gainers(gainers)
    plot_volume(top_coins)

    # Generate insights
    generate_insights(df)


if __name__ == "__main__":
    main()