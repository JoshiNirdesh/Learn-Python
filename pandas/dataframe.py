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

import numpy as np

a=np.array([[1,2],[1,3],[2,4],[4,5]])

d = pd.DataFrame(a,columns=['a','b'])
print(d.head(2))
