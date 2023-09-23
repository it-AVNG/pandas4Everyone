'''
let us plot the avarage mean and Gdp per countries
'''
import pandas as pd
import matplotlib.pyplot as plt

# mean life expectancy per year
df=pd.read_csv("../data/gapminder.tsv", sep="\t")
print(df)
mean_lifeEXP_groupby_year = (
    df.groupby(['year'])
    ['lifeExp']
    .mean()
)
print(mean_lifeEXP_groupby_year)
mean_lifeEXP_groupby_year.plot()
plt.show()
