'''
Read and store in a movies DataFrame the data within the movies.csv file.

This assignment will require a few extra steps. We will be using the same movies.csv as the previous exercise.

Use the appropriate separator.
The given data doesn't have a defined header. Use the column names given in the column_names variable.
Missing values are encoded as ? characters. Parse those values as NaN objects.
The budget column has commas separating the thousands, make sure the column is of float data type.
The index of the DataFrame should be represented by the movie_title column.

'''

import pandas as pd

class imdb:        
    def movies():
        url ='https://raw.githubusercontent.com/krishnatray/RDP-Reading-Data-with-Python-and-Pandas/master/unit-1-reading-data-with-python-and-pandas/lesson-3-advanced-parsing-on-movies-dataset/files/movies.csv'
        column_names = ['color', 'director_name', 'num_critic_for_reviews', 'duration',
                'gross', 'movie_title', 'num_user_for_reviews', 'country',
                'cotent_rating', 'budget', 'title_year', 'imdb_score', 'genre']
        df = pd.read_csv(url, 
                    sep='|',
                    header=None,
                    names=column_names,
                    na_values='?',
                    thousands=',',
                    index_col='movie_title')
        return df
        
    
        
        
        
        
        

    