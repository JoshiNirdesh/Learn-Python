import pandas as pd

data = {
    "salary":[10,None,20,None,50]
}

df = pd.DataFrame(data)
df['salary']=df['salary'].interpolate(method='linear')
print(df)