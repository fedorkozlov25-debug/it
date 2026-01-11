import pandas as pd
data=pd.read_csv('titanic.csv')
tick=data[data['Pclass']== 1]
print((tick['Fare'].mean()).round(2))
third=data[data['Pclass']==3]
print((third['Survived'].mean()*100).round(2))

#84.15
#24.24