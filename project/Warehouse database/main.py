import pandas as pd
from sqlalchemy import create_engine

customers = pd.read_csv("customers.csv" , on_bad_lines="skip")
orders = pd.read_csv("orders.csv", on_bad_lines="skip")
order_details = pd.read_csv("order-details.csv", on_bad_lines="skip")
products = pd.read_csv("products.csv", on_bad_lines="skip")
employees = pd.read_csv("employees.csv", on_bad_lines="skip")
categories = pd.read_csv("categories.csv",on_bad_lines="skip")

# print(orders.columns)
customers = customers.drop_duplicates()
orders = orders.drop_duplicates()
order_details=order_details.drop_duplicates()
products = products.drop_duplicates()
employees = employees.drop_duplicates()

orders['orderDate']=pd.to_datetime(orders['orderDate'])

#dim date
dim_date = orders[["orderDate"]].dropna().drop_duplicates().copy()

dim_date["date_id"] = range(1, len(dim_date) + 1)
dim_date["day"] = dim_date["orderDate"].dt.day
dim_date["month"] = dim_date["orderDate"].dt.month
dim_date["month_name"] = dim_date["orderDate"].dt.month_name()
dim_date["quarter"] = dim_date["orderDate"].dt.quarter
dim_date["year"] = dim_date["orderDate"].dt.year

# dim customer
dim_customers = customers[['customerID',"companyName","contactName","city","country"]].copy()
dim_customers = dim_customers.rename(
    columns={
        "customerID":"customer_id",
        "companyName":"company_name",
        "contactName":"contact_name"
    }
)
#dim employeee
dim_employee=employees[['employeeID','firstName','lastName','title']].copy()
dim_employee['employee_name']=dim_employee['firstName']+" "+ dim_employee['lastName']
dim_employee = dim_employee[["employeeID","employee_name","title"]]



dim_product = products.merge(categories[['categoryID','categoryName']], on="categoryID", how="left")


dim_product = dim_product[['productID','productName','supplierID','categoryName','unitPrice']].copy()
dim_product = dim_product.rename(columns={
    "productID":"product_id",
    "productName":"product_name",
    "supplierId":"supplier_id",
    "categoryName":"category_name",
    "unitPrice":"unit_price"
})
# print(orders.columns)
# print(order_details.columns)
# print(dim_date.columns)

fact_sales = order_details.merge(orders[['orderID','customerID','employeeID','orderDate']],on='orderID', how='left')

fact_sales = dim_date.merge(fact_sales,on="orderDate",how="left")

fact_sales["total_amount"] = (
        fact_sales["quantity"] * fact_sales["unitPrice"] * (1 - fact_sales["discount"])
    )

fact_sales = fact_sales.rename(columns={
        "orderID": "order_id",
        "productID": "product_id",
        "customerID": "customer_id",
        "employeeID": "employee_id",
        "unitPrice": "unit_price"
    })

fact_sales = fact_sales[[
        "order_id",
        "product_id",
        "customer_id",
        "employee_id",
        "date_id",
        "quantity",
        "unit_price",
        "discount",
        "total_amount"
    ]].copy()



fact_sales['sales_id']=range(1,len(fact_sales)+1)
fact_sales = fact_sales[[
        "sales_id",
        "order_id",
        "product_id",
        "customer_id",
        "employee_id",
        "date_id",
        "quantity",
        "unit_price",
        "discount",
        "total_amount"
    ]]

engine = create_engine("postgresql+psycopg2://nirdeshzoc@localhost:5432/warehouse")

dim_date.to_sql("dim_date",engine,if_exists='replace',index=False)
dim_customers.to_sql("dim_customer",engine,if_exists='replace',index=False)
dim_employee.to_sql("dim_employee",engine,if_exists='replace',index=False)
dim_product.to_sql("dim_product",engine,if_exists='replace',index=False)
fact_sales.to_sql("fact_sales",engine,if_exists='replace',index=False)

print("Loaded Successfully")





