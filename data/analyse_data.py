def clean_data(df):

    columns_needed = [
        "name",
        "symbol",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h"
    ]

    df = df[columns_needed]

    print("Columns after cleaning:")
    print(df.head())

    return df


def top_gainers(df):
    top_gainer = df.sort_values(
        by="price_change_percentage_24h",
        ascending=False
    ).head(10)

    return top_gainer


def top_market_cap(df):
    return df.sort_values(
        by="market_cap",
        ascending=False
    ).head(10)