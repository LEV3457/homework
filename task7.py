import pandas as pd

df = pd.read_csv("TheUnsinkable.csv")
w = pd.crosstab(df['sex'], df['alive'])

# Процент выживших в каждом классе
i = df.groupby('pclass')['alive'].mean() * 100
print(w)
print(i)