import pandas as pd
data=pd.read_csv('titanic.csv')
med=data['Age'].median()
data['Age'].fillna(med)
print(med)

#28.0