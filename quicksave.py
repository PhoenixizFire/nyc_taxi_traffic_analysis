import pandas as pd

def save(df,name):
    df.to_json(f'{name}.json')

def load(name):
    return pd.read_json(f'{name}.json')