import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/jorisvandenbossche/pandas-tutorial/master/data/titanic.csv')

df.to_csv('./new_copy.csv')

# df.info()
# df.shape()
# print(df.dtypes)

#print(df[['Name', 'Age']])

#print(df[df['Age']>18])

df1 = df.sort_values(['Age', 'Name'], ascending=[False, True]).copy(deep=True)

#print(df1[['Name', 'Age']])


print('Среднее значение возраста пассажира: ', df1['Age'].mean(),'      ', 'Медиана возраста: ', df1['Age'].median())

print('Среднее значение возраста среди мужчин: ', df1[df1['Sex'] == 'male']['Age'].mean())
print('Среднее значение возраста среди женщин: ', df1[df1['Sex'] == 'female']['Age'].mean(), '\n')

print(df1.groupby('Sex')['Age'].describe(), '\n')

print(df.groupby(['Sex', 'Survived'])['Age'].agg(['mean', 'median']), '\n')

df1['Age'].plot(kind='hist', bins=20)

df1.groupby('Sex')['Age'].plot(kind='kde', xlim=[0, 100], legend=True)
