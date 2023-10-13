import numpy as pd
import pandas as pd
import json
from pandas import json_normalize
import urllib.request as request

class artist_json:
    def __init__(self):
        self.artist = pd.DataFrame(data=[None])
        self.biography = pd.DataFrame(data=[None])
               
    def read_artist_json(self):
        url_json='https://raw.githubusercontent.com/krishnatray/RDP-Reading-Data-with-Python-and-Pandas/master/unit-1-reading-data-with-python-and-pandas/lesson-10-artists-nested-biography/files/artists.json'
        with request.urlopen(url_json) as f:
            # read artists.json into an artists dataFrame varable,
            art_json = json.loads(f.read().decode()) 
        # using json_normalize create data Frame
        
        self.artist = json_normalize(art_json)
        return self.artist

    def read_bio_json(self):
        url_json ='https://raw.githubusercontent.com/krishnatray/RDP-Reading-Data-with-Python-and-Pandas/master/unit-1-reading-data-with-python-and-pandas/lesson-10-artists-nested-biography/files/artists.json'
        with request.urlopen(url_json) as f:
            # read artists.json into an artists dataFrame varable,
            art_json = json.loads(f.read().decode()) 

        # using json_normalize create DataFrame and add the name column
        self.biography = json_normalize(art_json,
                           'bio',
                           meta=['name']
                           )
        return self.biography