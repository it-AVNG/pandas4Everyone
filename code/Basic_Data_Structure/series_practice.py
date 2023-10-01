import pandas as pd

scientists = pd.read_csv('data\scientists.csv')
print(scientists)
age = scientists['Age']
print(age.describe())

#subsetting using attributes
age_above_mean = age[age > age.mean()]
print(age_above_mean)

#Formating datetime 
born_datetime = pd.to_datetime(scientists['Born'],format='%Y-%m-%d')
died_datetime = pd.to_datetime(scientists['Died'], format ='%Y-%m-%d')
#creating new datetime columns for dataframe:
scientists['born_dt'], scientists['died_dt'] = (
    born_datetime,
    died_datetime
)

#computing a new columns
scientists['age_days'] = scientists['died_dt'] - scientists['born_dt']
#computing the existed column
occ_count = scientists['Occupation'].nunique()
print('Total occupation:',occ_count)

print(scientists.head())
print(scientists.dtypes)
