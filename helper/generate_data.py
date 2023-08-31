import pandas as pd

from web_scraper import scrape_data

def main(observations = 1):
    df = scrape_data(observations)
    print(df.head())