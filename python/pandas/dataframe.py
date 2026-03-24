import pandas as pd
# data = {
#     'name':['ram','shyam','hari'],
#     'marks':[10,20,30]
#     }
# d = pd.DataFrame(data)
# print(d)
# print(d['name'])
# print(d[d["marks"]>10])

# data = [
#     {"name":"ram","age":10},
#     {"name":"hari","age":30}
# ]
# d = pd.DataFrame(data,columns=['a1','b2'])
# print(data)

# import numpy as np

# a=np.array([[1,2],[1,3],[2,4],[4,5]])

# d = pd.DataFrame(a,columns=['a','b'])
# # print(d.head(2))
# # print(d.tail(2))
# print(d['a'])

# import pandas as pd

# data = [
#     {"name":"ram","city":"kathmandu"},
#     {"name":"hari","city":"pokhara"},
#     {"name":"shyam","city":"chitwan"}
# ]
# df= pd.DataFrame(data)
# # print(df)
# df['salary']=[10,20,30]
# # print(df)
# df['add-sal']=df['salary']+10
# df['country']='nepal'
# df.loc[0,"city"]="bhaktapur"
# print(df)

import pandas as pd
data = {
    'name':['ram','shyam','hari'],
    'age':[10,20,23],
    'city':['kathmandu','chitwan','bhaktapur']

}
data2 = [
    ['ram',10,'kathmandu'],
    ['shyam',20,'chitwan'],
    ['ram',24,'bhaktapur'],
    ['gita',22,'chitwan'],
    ['monika',22,'bhaktapur']
]
df = pd.DataFrame(data)
# print(df.head(3))
# print(df['name'])
# print(df[df['age']>20])
# df["salary"] = [20000, 25000, 30000]
# print(df)
# print(df['age'].mean())
# print(df.sort_values('age', ascending=False))
print(df.groupby("city")["name"].count())
