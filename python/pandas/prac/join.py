import pandas as pd

df1 = pd.DataFrame({
    'customerId':[10,20,30,12,11],
    'Name':['ram','shyam','hari','gita','birat']
})

df2 = pd.DataFrame({
    'customerId':[10,20],
    'order_amount':[1000,2000]
})

data = pd.merge(df1,df2,on="customerId",how="left")
print(data)