import pandas as pd

df = pd.read_csv('cat_breeds_clean.csv')
r = df["Breeds"].nunique()
print(r)

