import pandas as pd 

data = {
    "name":['a','v','s','w','q','w'],
    'age':[10,20,35,42,12,45],
    'salary':[100,244,1242,1242,4214,424],
    'performance':[24,56,32,67,23,12]
}

df = pd.DataFrame(data)
# print(df)
# print(df.describe())

# print(df.shape)
# print(df.columns)

# print(df[['name','age']])
# high_salary = df[df['salary']>1000]
# filter = df[(df['salary']>1000) & (df['age']>20)]
# print(filter)
print(df)

# df['bonus']=df['salary']*0.1
# print(df)

# df.insert(0,"Employee Id",[1,2,3,4,5,6])
# print(df)

# df.loc[0,'salary']=500
# print(df)
# df['salary']=df['salary']*1.05
# print(df)

df.drop(columns=['performance'], inplace = True)
print(df)