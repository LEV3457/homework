import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("train_and_test2.csv")
o = df['Age'].hist(bins=20)
plt.title('Распределение возрастов')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
print(o)
# # Boxplot цен билетов для выживших и погибших
# import seaborn as sns
# sns.boxplot(x='Survived', y='Fare', data=df)
# plt.title('Fare vs Survived')
# plt.show()