import pandas as pd

#read the file
df = pd.read_csv('../data/gapminder.tsv', sep='\t')
columns_list = list(df.columns)
#iterate through the columns
my_list = [item for item in columns_list]
print(my_list)
print(df.columns[0])
#creating subset
string1,string2,string3, string4 = 'country', 'continent','year','lifeExp'
listing = [string1,string2,string3, string4]
subset = df[listing]
subset2 = df [['country', 'continent','year','gdpPercap']]
print(subset)
print(subset2)
