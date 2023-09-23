import pandas as pd

#read the file
df = pd.read_csv('../data/gapminder.tsv', sep='\t')
columns_list = list(df.columns)
print(columns_list)

'''
count number of countries per continents
'''
freq_n = (
    df.groupby('continent')['country']
    .nunique()
)
print(freq_n)