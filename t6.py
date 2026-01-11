import pandas as pd
data=pd.read_csv('titanic.csv')
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
pas=data[data['PassengerId']==888]
print(pas['FamilySize'])

# 887    1