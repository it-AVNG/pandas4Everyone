import pandas as pd
import unittest
import numpy as np
from read_xlsx import read_file,top_25

class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'
        
    def test_date_update(self):
        assert read_file(self.url)['Last_Updated'].dtype  == np.dtype('<datetime64[ns]')

        
    def test_top25_index(self):
        assert top_25(self.url).iloc[23]['App'] == 'Ulta Beauty'
        assert top_25(self.url).iloc[1]['App'] == 'CDL Practice Test 2018 Edition'   
        
    def test_top25_shape(self):
        assert top_25(self.url).shape == (25, 5)
                    
if __name__ == '__main__':
    unittest.main()