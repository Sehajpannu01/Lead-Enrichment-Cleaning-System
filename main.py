from Scripts.extract import extract_data
from Scripts.transform import transform
from Scripts.load import load_tocsv, load_to_postgres


def main():

    movies = extract_data()
    if movies:
        df = transform(movies)
        load_tocsv(df)
        print("Data loaded to csv")
    else:
        print("No movies were extracted. Halting pipeline")




if __name__ == "__main__":
    main()