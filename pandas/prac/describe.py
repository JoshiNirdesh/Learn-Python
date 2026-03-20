import pandas as pd 

data = {
    "name":['a','v','s','w','q','w'],
    'age':[10,20,35,42,12,45],
    'salary':[100,244,1242,1242,4214,424],
    'performance':[24,56,32,67,23,12]
}

df = pd.DataFrame(data)
print(df)
print(df.describe())