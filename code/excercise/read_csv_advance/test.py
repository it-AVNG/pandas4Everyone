import unittest
from csv_ad import imdb

class TestClass(unittest.TestCase):
    def test_shape(self):
        assert imdb.movies().shape == (100, 12)
    def test_country(self):
        assert '?' not in imdb.movies().country.unique()
    def test_budget(self):
        assert imdb.movies().loc[:, 'budget'].min() == 105000000.0
        
        
if __name__=='__main__':
    unittest.main()