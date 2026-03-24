import requests
import pandas as pd
from sqlalchemy import create_engine

url = "https://newsdata.io/api/1/latest?apikey=pub_4ccfa82a7fa94e56b7a99d394c12bf76"
data  = requests.get(url).json()

articles = data['results']

df = pd.DataFrame(articles)
df = df[['article_id','title','pubDate','source_id','country']]

df['pubDate']=pd.to_datetime(df['pubDate'], errors='coerce')

df['title_length']=df['title'].str.len()
df = df.dropna()
df=df.drop_duplicates(subset=['article_id'])
# print(df)

try:
    engine = create_engine("postgresql+psycopg2://nirdeshzoc@localhost:5432/news")

    df.to_sql("rawdata",engine,if_exists='replace',index=False)

    print("Data Loaded Successfully")
except Exception as e:
    print("Error",e)

