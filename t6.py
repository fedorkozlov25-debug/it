import pandas as pd
data=pd.read_csv('titanic.csv')
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
pas=data[data['PassengerId']==889]
print(pas['FamilySize'])

# 888    4