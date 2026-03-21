import pandas as pd
from datetime import datetime
import os

FILE_PATH = "data/crypto_history.csv"


def save_history(df):
    df = df.copy()
    df["date"] = datetime.now().date()

    if os.path.exists(FILE_PATH):
        old_df = pd.read_csv(FILE_PATH)
        new_df = pd.concat([old_df, df])
    else:
        new_df = df

    new_df.to_csv(FILE_PATH, index=False)
    print("Historical data updated")