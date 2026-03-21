from api.fetch_data import fetch_crypto_data
from data.analyse_data import clean_data, top_gainers, top_market_cap
from visualization.plot_data import plot_market_cap, plot_top_gainers, plot_volume
from analysis.insights import generate_insights
from analysis.history import save_history
from analysis.trend_analysis import market_trend
from visualization.plot_data import plot_market_trend

def main():
    print("Fetching API Data...")

    df = fetch_crypto_data()

    if df is None:
        return
    
    # clean data
    df = clean_data(df)
    
    # save history
    save_history(df)
    
    # get top gainers
    gainers = top_gainers(df)
    print(gainers)
    
    # get top_market_cap
    print("\nTop Market Cap Coins")
    top_coins = top_market_cap(df)
    print(top_coins)
    
    # save to csv
    df.to_csv("data/crypto_data.csv", index=False)

    # Generate insights
    generate_insights(df)
    
    # Generate trend
    trend = market_trend()
    
    # Generate charts
    plot_market_cap(top_coins)
    plot_top_gainers(gainers)
    plot_volume(top_coins)
    plot_market_trend(trend)


if __name__ == "__main__":
    main()