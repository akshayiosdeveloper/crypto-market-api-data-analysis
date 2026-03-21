from api.fetch_data import fetch_crypto_data
from data.analyse_data import clean_data ,top_gainers,top_market_cap
from visualization.plot_data import plot_market_cap

def main():
    df = fetch_crypto_data()
    if df is None:
        return
    
    df = clean_data(df)
    print(df)
    print("---cleaning")
    print("\n Topp gainers")
    print(top_gainers(df))
    
    print("\n Top market cap coins")
    top_coins = top_market_cap(df)
    print(top_coins)
    
    df.to_csv("data/crypto_data.csv", index=False)
    
    # plot
    plot_market_cap(df)
    
if __name__ == "__main__":
    main()    
    
    
