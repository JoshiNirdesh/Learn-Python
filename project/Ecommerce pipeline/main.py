import pandas as pd 
from sqlalchemy import create_engine
customers=pd.read_csv("olist_customers_dataset.csv")
orders  = pd.read_csv("olist_orders_dataset.csv")

df = orders.merge(customers,on="customer_id")
print(df.columns)

try:
    engine = create_engine("postgresql+psycopg2://nirdeshzoc@localhost:5432/ecommerce")
    df.to_sql("cusorder", engine,if_exists='replace', index=False)
    print("Connected")
except Exception as e:
    print("Error",e)


# print(customers.columns)
# print(orders.columns)