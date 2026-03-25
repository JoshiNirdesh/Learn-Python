import requests
import pandas as pd
from sqlalchemy import create_engine
import streamlit as st


url = "https://newsdata.io/api/1/latest?apikey=pub_4ccfa82a7fa94e56b7a99d394c12bf76"
data  = requests.get(url).json()

articles = data['results']

df = pd.DataFrame(articles)
df = df[['article_id','title','pubDate','source_id','country']]

df['pubDate']=pd.to_datetime(df['pubDate'], errors='coerce')

df['title_length']=df['title'].str.len()
df = df.dropna()
df=df.drop_duplicates(subset=['article_id'])
df=df.explode("country")

try:
    engine = create_engine("postgresql+psycopg2://nirdeshzoc@localhost:5432/news")

    df.to_sql("rawdata",engine,if_exists='replace',index=False)

    print("Data Loaded Successfully")
except Exception as e:
    print("Error",e)

dim_date = df[['pubDate']].copy()
# print(dim_date.dtypes)

dim_date["date_id"]=range(1,len(dim_date)+1)
dim_date["year"] = dim_date["pubDate"].dt.year
dim_date['month']=dim_date['pubDate'].dt.month
dim_date['day']=dim_date['pubDate'].dt.day
# print(dim_date.head())

fact_news = df.merge(dim_date,on="pubDate")
fact_news = fact_news[["article_id", "date_id", "source_id", "title_length"]]
st.dataframe(fact_news)

df = pd.read_sql("SELECT * FROM rawdata", engine)

st.title("News Analytics Dashboard")

st.bar_chart(df["title_length"])


 