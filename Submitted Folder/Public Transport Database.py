import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Read the datasets into DataFrames
nyc_subway_df = pd.read_csv('nyc_subway_monthly_ridership.csv')
chicago_cta_df = pd.read_csv('chicago_cta_daily_boarding_totals.csv')

# Transform NYC Subway DataFrame
nyc_subway_df['month'] = pd.to_datetime(nyc_subway_df['month'], format='%Y-%m-%d').dt.to_period('M')
nyc_subway_df['city'] = 'NYC'
nyc_subway_df['transportation_type'] = 'metro'
nyc_subway_df.rename(columns={'ridership': 'ridership_count'}, inplace=True)

# Transform Chicago CTA DataFrame
chicago_cta_df['date'] = pd.to_datetime(chicago_cta_df['date'], format='%m/%d/%Y')
chicago_cta_df['month'] = chicago_cta_df['date'].dt.to_period('M')
chicago_cta_df['city'] = 'Chicago'
chicago_cta_df['transportation_type'] = 'bus'
chicago_cta_df.rename(columns={'rides': 'ridership_count'}, inplace=True)

# Concatenate the transformed DataFrames
monthly_totals_df = pd.concat([nyc_subway_df[['month', 'city', 'transportation_type', 'ridership_count']],
                                chicago_cta_df[['month', 'city', 'transportation_type', 'ridership_count']]])

# Create a PostgreSQL connection and engine
conn = psycopg2.connect(
    dbname="public_transit",
    user="katykat",
    password="hellosql",
    host="localhost"
)
engine = create_engine('postgresql://postgres:hellosql@localhost:5432/public_transit')

# Load the data into PostgreSQL database
monthly_totals_df.to_sql('monthly_totals', engine, if_exists='replace', index=False)

# Create bus_monthly_totals and metro_monthly_totals tables using SQL
create_bus_table_sql = """
CREATE TABLE bus_monthly_totals AS
SELECT * FROM monthly_totals WHERE transportation_type = 'bus';
"""

create_metro_table_sql = """
CREATE TABLE metro_monthly_totals AS
SELECT * FROM monthly_totals WHERE transportation_type = 'metro';
"""

# Execute SQL commands
with conn.cursor() as cursor:
    cursor.execute(create_bus_table_sql)
    cursor.execute(create_metro_table_sql)
    conn.commit()

# Close the connection
conn.close()
