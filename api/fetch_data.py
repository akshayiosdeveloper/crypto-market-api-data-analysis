import requests
import pandas as pd

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1
    }
    response = requests.get(url,params)
    if response.status_code != 200:
        print("API request failed!!")
        return None
    data = response.json()
    df = pd.DataFrame(data) 
    return df   
    # print(df.head())