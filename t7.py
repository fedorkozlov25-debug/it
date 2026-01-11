import pandas as pd
data=pd.read_csv('titanic.csv')
alive=data[data['Survived']== 1]
print((alive['Age'].mean()).round(2))
dead=data[data['Survived']== 0]
print((dead['Age'].mean()).round(2))

#28.34
#30.63