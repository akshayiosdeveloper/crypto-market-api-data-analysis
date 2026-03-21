import matplotlib.pyplot as plt

def plot_market_cap(df):
    plt.figure(figsize=(14,6))
    plt.bar(df["name"], df["market_cap"])
    plt.xticks(rotation=45, ha="right")  # rotate labels
    plt.title("Top Cryptocurrencies by Market Cap")

    plt.tight_layout()
    plt.savefig("charts/market_cap.png")
    plt.show()