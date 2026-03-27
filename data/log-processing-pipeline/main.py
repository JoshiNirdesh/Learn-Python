import pandas as pd 

def extract_data ():
    customers = pd.read_csv("customers.csv")
    products = pd.read_csv("products.csv")
    sales = pd.read_csv("sales.csv")
    return customers,products,sales

def transform(customers,products,sales):

    sales['order_date']=pd.to_datetime(sales['order_date'], errors="coerce")
    sales["total_amount"]=sales['quantity']*sales['unit_price']

    dim_date = sales[['order_date']].drop_duplicates().copy()
    dim_date= dim_date.sort_values('order_date').reset_index(drop=True)
    dim_date['date_id'] = range(1,len(dim_date)+1)
    print(dim_date)

    sales  = sales.merge(dim_date,on="order_date", how="left")
    print(sales)
customers,products,sales = extract_data()
transform(customers,products,sales)
