import pandas as pd

# df = pd.read_csv("../data/engine_data.csv")
df = pd.read_csv("../data/uploaded_data.csv")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df


