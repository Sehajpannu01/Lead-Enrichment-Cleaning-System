import pandas as pd
from dotenv import load_dotenv
import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
 

load_dotenv()

API_KEY = os.getenv("API_KEY")


print("----APIKEY----",API_KEY)


def create_requests_session():
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def extract_data(num_results = 500):
    print(f"Extracting data for total {num_results} records")

    if not API_KEY:
        print("API KEY NOT FOUND CHECK .ENV FILE")
        return []
    
    else:
        print(f"API KEY = [{API_KEY}]")
    
    all_records = []
    session = create_requests_session()

    results_per_call = 100  # Max limit for RandomUser API
    pages = num_results // results_per_call

    for i in range(pages):
        response = session.get(f"https://randomuser.me/api/?results={results_per_call}&nat=in,us,gb,ca,au")
        if response.status_code == 200:
            data = response.json()
            all_records.extend(data['results'])
            print(f"Page {i+1}: {len(data['results'])} records added")
        else:
            print(f"Failed on page {i+1} with status: {response.status_code}")
  
    return all_records


    


    
if __name__ == "__main__":
    movies = extract_data(num_results=500)