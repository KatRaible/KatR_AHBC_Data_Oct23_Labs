import pandas as pd
import requests
import psycopg2
import time

# Function to extract data from the XML file
def extract():


# Function to transform data
def transform(df):


# Function to load data into PostgreSQL
def load(df):


# main function
def main():
    print("Begin reading new label releases from discogs.com")
    df = extract()
    print(f"Successfully loaded {len(df)} labels into DataFrame")
    print("Begin cleaning columns")
    df = transform(df)
    print(f"Completed cleaning columns for {len(df)} labels")
    load(df)

if __name__ == '__main__':
    main()
