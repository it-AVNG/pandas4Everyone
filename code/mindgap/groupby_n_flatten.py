import pandas as pd

#read the file
df = pd.read_csv('../data/gapminder.tsv', sep='\t')
columns_list = list(df.columns)
print(columns_list)


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