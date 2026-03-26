import requests
import pandas as pd 
from sqlalchemy import create_engine

url = "https://newsdata.io/api/1/latest?apikey=pub_4ccfa82a7fa94e56b7a99d394c12bf76"
data = requests.get(url).json()

articles = data['results']

df = pd.DataFrame(articles)
df = df[['article_id','title','pubDate','source_id','country']]
df['pubDate']=pd.to_datetime(df['pubDate'])

df = df.dropna()

engine = create_engine("postgresql+psycopg2://nirdeshzoc@localhost:5432/news")
df.to_sql("rawnews",engine,if_exists='replace',index=False)
print("Connected")


