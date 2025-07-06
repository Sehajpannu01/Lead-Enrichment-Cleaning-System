import pandas as pd
from Scripts.extract import extract_data
from pandas import json_normalize

def transform(movies):
    print("Transforming data...")

    if not movies:
        print("WARNING: No movies to transform! Creating empty DataFrame.")

    flat_record = json_normalize(movies)

    print("Done with transform")

    return pd.DataFrame(data= flat_record)

if __name__ == "__main__":
    movies = extract_data(num_results=500)
    df = transform(movies)
    print(df.head())