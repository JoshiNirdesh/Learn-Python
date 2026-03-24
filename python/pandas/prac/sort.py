import pandas as pd

data = {
    'name':['ram','shyam','hari','gita','sita'],
    'age':[10,22,22,5,62],
    'salary':[10000,2000,3000,4000,2000]
}

df = pd.DataFrame(data)
# print(df)

# df.sort_values(by=['age','salary'],ascending=[True,True],inplace=True)
# print(df)
grp=df.groupby("age")['salary'].sum()
print(grp)
