import pandas as pd
from datetime import datetime

README_FILE = "README.md"


def update_readme(df):
    top_coin = df.loc[df["market_cap"].idxmax()]
    top_gainer = df.loc[df["price_change_percentage_24h"].idxmax()]
    highest_volume = df.loc[df["total_volume"].idxmax()]

    snapshot = f"""
## Latest Market Snapshot

Top Coin: {top_coin['name']}  
Top Gainer: {top_gainer['name']}  
Highest Volume: {highest_volume['name']}  
Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

    with open(README_FILE, "r") as file:
        content = file.read()

    if "## Latest Market Snapshot" in content:
        start = content.index("## Latest Market Snapshot")
        content = content[:start] + snapshot
    else:
        content += "\n" + snapshot

    with open(README_FILE, "w") as file:
        file.write(content)

    print("README updated with latest market snapshot")