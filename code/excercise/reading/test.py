import unittest
from read_json_excercise import artist_json

class TestClass(unittest.TestCase):

    def test_artist_1(self):
        print()
        print('Test check artist DataFrame shape equal to (5,5)')
        self.assertEqual(artist_json.read_artist_json(self).shape,
                         (5,5))
        
        
    def test_artist_2(self): 
        print()       
        print('Test check artist name at index_name 2 is Diego Rivera')
        self.assertEqual(artist_json.read_artist_json(self).iloc[2]['name'],
                         'Diego Rivera')
        
        
    def test_biography_1(self):
        print()
        print('Test check Biography DataFrame shape equal to (5,7)')
        self.assertEqual(artist_json.read_bio_json(self).shape,
                         (5,7))
        

    def test_biography_2(self):
        print()
        print('Test check Biography number of painting at index_name 4 is 194')
        self.assertEqual(artist_json.read_bio_json(self).iloc[4]['paintings'],
                         194)
        
    
    def test_biography_3(self):
        print()
        print('Test check biography include the name col by index_name 3 is equal to Claude Monet')
        self.assertEqual(artist_json.read_bio_json(self).iloc[3]['name'],
                         'Claude Monet')
        
if __name__=='__main__':
    unittest.main()