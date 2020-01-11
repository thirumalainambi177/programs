import pandas as pd
df=pd.read_csv('filew.csv')
print(df.head())

print(df.iloc[:,-2])
