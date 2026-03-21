import matplotlib.pyplot as plt


def plot_market_cap(df):
    df = df.sort_values(by="market_cap", ascending=True)

    plt.figure(figsize=(14,7))
    plt.barh(df["name"], df["market_cap"])

    for index, value in enumerate(df["market_cap"]):
        plt.text(value, index, f"${value:,.0f}")

    plt.title("Top Cryptocurrencies by Market Cap")
    plt.xlabel("Market Cap")
    plt.tight_layout()

    plt.savefig("charts/market_cap.png")
    plt.show()


def plot_top_gainers(df):
    df = df.sort_values(by="price_change_percentage_24h", ascending=True)

    plt.figure(figsize=(14,7))
    plt.barh(df["name"], df["price_change_percentage_24h"])

    for index, value in enumerate(df["price_change_percentage_24h"]):
        plt.text(value, index, f"{value:.2f}%")

    plt.title("Top Gainers (24h)")
    plt.xlabel("Price Change %")
    plt.tight_layout()

    plt.savefig("charts/top_gainers.png")
    plt.show()


def plot_volume(df):
    df = df.sort_values(by="total_volume", ascending=True)

    plt.figure(figsize=(14,7))
    plt.barh(df["name"], df["total_volume"])

    for index, value in enumerate(df["total_volume"]):
        plt.text(value, index, f"${value:,.0f}")

    plt.title("Trading Volume")
    plt.xlabel("Volume")
    plt.tight_layout()

    plt.savefig("charts/volume.png")
    plt.show()