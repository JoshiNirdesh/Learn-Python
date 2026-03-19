# import pandas as pd
# s=pd.Series([10,20,30,40])
# print(s)

import pandas as pd 

s = pd.Series([5,10,15,20],index=['a','b','c','d'])
# print(s)
# print(s[s>10])
# print(s.sum())
# print(s.mean())
s3 = pd.Series([10,20,None])
print(s3.fillna(0))

s4 =pd.Series([12,32,42,53])
print(s4.sort_values())

s5 = pd.Series([1,2,4,1,1,2])
print(s5.value_counts())