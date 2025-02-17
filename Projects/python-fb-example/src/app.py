# src/app.py
import requests
import pandas as pd

def fetch_data(url):
    response = requests.get(url)
    return response.json()

def main():
    url = 'https://api.github.com/events'
    data = fetch_data(url)
    df = pd.DataFrame(data)
    print(df.head())

if __name__ == '__main__':
    main()
