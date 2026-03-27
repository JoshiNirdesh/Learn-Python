import pandas as pd 

def transform_data(df):
    df = df.drop_duplicates()

    df = df.dropna(subset=['order_id','order_date','product','quantity','price'])

    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')  
    df = df.dropna(subset=["order_date", "quantity", "price"])

    df['total_amount'] = df["quantity"] * df['price']

    return df