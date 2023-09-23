import pandas as pd

#read the file
df = pd.read_csv('../data/gapminder.tsv', sep='\t')
columns_list = list(df.columns)
print(columns_list)
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
#Subset rows and columns
#using loc
print(df.loc[43,'country'])
#using iloc
print(df.iloc[42,0])
#usingmultiple rows and columns notation
print(df.iloc[[0, 99, 999], [0, 3, 5]])

'''
Calculating life expectancy by year
'''
# Split data into parts by year
group_by_year_df = df.groupby('year')
# select the feature we want to calculate
group_by_year_lifeExp_df = group_by_year_df['lifeExp']
# calculating the mean using the mean() method
mean_lifeExp_by_year = group_by_year_lifeExp_df.mean()
print(mean_lifeExp_by_year)

'''
calculating life expectantcy by country and year
'''
group_by_country_year_df = df.groupby(['country','year'])
mean_group_by_country_year_lifeEXP = group_by_country_year_df['lifeExp'].mean()
print(mean_group_by_country_year_lifeEXP)

# multiple features and data
# mean_group_by_place_time_dataGDP_LifeEXP = df.groupby(['country','year'])[['lifeExp','gdpPercap']].mean()
#method chaining
mean_group_by_place_time_dataGDP_LifeEXP =(
										   df.groupby(['country','year'])
										   [['lifeExp','gdpPercap']].
										   mean()
										   )
print(mean_group_by_place_time_dataGDP_LifeEXP)
#flaten data
flat = mean_group_by_place_time_dataGDP_LifeEXP.reset_index()
print(flat)