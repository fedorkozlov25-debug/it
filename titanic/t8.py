import pandas as pd
data=pd.read_csv('titanic.csv')
women=data[data['Sex']== 'female']
class_women=women[women['Pclass']==1]
print(class_women['Survived'].sum())
child=data[data['Age']<18]
without_par=child[child['Parch']==0]
print(len(without_par))

#91
#32