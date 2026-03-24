import requests
import pandas as pd
url = "https://newsdata.io/api/1/latest?apikey=pub_4ccfa82a7fa94e56b7a99d394c12bf76"
data  = requests.get(url).json()

articles = data['results']

df = pd.DataFrame(articles)
df = df[['article_id','title','pubDate','source_id','country']]
print(df.dtypes)