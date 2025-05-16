import pandas as pd

df = pd.read_csv('Cryptocurrency Transaction Data.csv')
r = df["Gas_Price_Gwei"].nunique() 
print(r)

