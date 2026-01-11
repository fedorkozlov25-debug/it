import pandas as pd
data=pd.read_csv('titanic.csv')
print(data.count())
print(data.isna().sum()[['Age']])

#PassengerId    891
#Survived       891
#Pclass         891
#Name           891
#Sex            891
#Age            714
#SibSp          891
#Parch          891
#Ticket         891
#Fare           891
#Cabin          204
#Embarked       889
#dtype: int64
#Age    177
#dtype: int64