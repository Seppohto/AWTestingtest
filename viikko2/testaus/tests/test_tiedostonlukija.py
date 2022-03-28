import unittest
import sys
sys.path.insert(0, '/Users/Olli/Desktop/AW/AW-testing-harjoitukset/viikko2/testaus/tiedostonlukija')

from tiedostonlukija import tiedostonlukija

class TestCalculator(unittest.TestCase):

    def test_FileNotFound(self):        
        para2= 2
        para1 = 'C:/Users/Olli/Desktop/AW/AW-testing-harjoitukset/viikko2/testaus/tiedostonlukija/readmenotfound.txt'
        expected_result = 'File not found'
        result = tiedostonlukija(para1, para2)
        self.assertEqual(result, expected_result)

    def test_FileEmpty(self):        
        para2= 2
        para1 = 'C:/Users/Olli/Desktop/AW/AW-testing-harjoitukset/viikko2/testaus/tiedostonlukija/readmeEmpty.txt'
        expected_result = 'Empty file'
        result = tiedostonlukija(para1, para2)
        self.assertEqual(result, expected_result)

    def test_IndexError(self):        
        para2= 2
        para1 = 'C:/Users/Olli/Desktop/AW/AW-testing-harjoitukset/viikko2/testaus/tiedostonlukija/readmeIndexError.txt'
        expected_result = 'IndexError'
        result = tiedostonlukija(para1, para2)
        self.assertEqual(result, expected_result)
    
    def test_ReadMeSucces(self):        
        para2= 2
        para1 = "C:/Users/Olli/Desktop/AW/AW-testing-harjoitukset/viikko2/testaus/tiedostonlukija/readmeSuccess.txt"
        expected_result = '2'
        result = tiedostonlukija(para1, para2)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
