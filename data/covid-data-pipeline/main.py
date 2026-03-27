import pandas as pd 

def extract_data(path):
    return pd.read_csv(path)

def transform(df):
    df =df[["iso_code", "continent", "location", "date",
        "new_cases", "new_deaths", "total_cases", "total_deaths",
        "population"]].copy()
    
    df['date']=pd.to_datetime(df['date'])

    numeric_cols = ["new_cases", "new_deaths", "total_cases", "total_deaths", "population"]
    for col in numeric_cols:
        df[col]=pd.to_numeric(df[col], errors='coerce')
    
    df['new_cases']=df['new_cases'].fillna(0)
    df['new_deaths']=df['new_deaths'].fillna(0)

    df = df.dropna(subset=['location','date'])
    df["new_cases_7day_avg"] = (
        df.groupby("location")["new_cases"]
        .transform(lambda x: x.rolling(7, min_periods=1).mean())
    )
    df["cases_per_million_calc"] = (df["total_cases"] / df["population"]) * 1_000_000
    print(df)

df = extract_data("covid_data.csv")

transform(df)