import pandas as pd


def read_file(url):
    excel_df = pd.read_excel(
        url,
        usecols=['App', 'Rating', 'Installs', 'Rating', 'Genres', 'Last_Updated'],
        parse_dates=['Last_Updated']
    )
    return excel_df

def top_25(url):
    top_25_df = (read_file(url)
                 .sort_values(by=['Rating'],ascending=False)
                 .head(25))
    return top_25_df

url ='https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'