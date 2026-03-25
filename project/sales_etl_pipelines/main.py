import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("superstore.csv", encoding='latin1')

df=df.drop_duplicates()
df = df.dropna()

df['Order Date'] = pd.to_datetime(df["Order Date"])
df['year']=df['Order Date'].dt.year

try:
    engine = create_engine("postgresql+psycopg2://nirdeshzoc@localhost:5432/news")
    df.to_sql("sales",engine,if_exists="replace",index=False)
    print("Connected Successfully")
except Exception as e:
    print("Error",e)



query = 'SELECT SUM("Sales") FROM sales' 

result = pd.read_sql(query,engine)
print(result)
