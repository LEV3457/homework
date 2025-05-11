import pandas as pd

df = pd.read_csv('Fake.csv')
age = df["date"][-1: -4]
print([i + "\n" for i in age])