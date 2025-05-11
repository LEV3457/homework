import pandas as pd

# Загрузка данных
df = pd.read_csv('titanic.csv')

# Первые 5 строк
df.head()

df[df['Age'] > 30]

# Пассажиры 1-го класса
df[df['Pclass'] == 1]