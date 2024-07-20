import pandas as pd

def store_data(data, path):
    data.to_csv(path, index=False)
