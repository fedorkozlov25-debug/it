import pandas as pd
data=pd.read_csv('titanic.csv')
print((data['Survived']==1).sum())
print(((data['Survived']==1).mean()*100).round(2))
women=data[data['Sex']=='female']
print((women['Survived'].mean()*100).round(2))
men=data[data['Sex']=='male']
print((men['Survived'].mean()*100).round(2))

#342
#38.38
#74.2
#18.89