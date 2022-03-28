import unittest
import sys
sys.path.insert(0, '/Users/Olli/Desktop/AW/AW-testing-harjoitukset/viikko2/testaus/editstring')

from editstring import reverse

class TestEditstrings(unittest.TestCase):

    def test_reserve(self):        
        string = "Pluto is a doG!"
        expected_result = "OtulP IS a doG!"
        result = reverse(string)
        self.assertEqual(result, expected_result)

    def test_reserve1(self):        
        string = "if this would be crazy!"
        expected_result = "IF this dluow BE !yzarc."
        result = reverse(string)
        self.assertEqual(result, expected_result)
    
    def test_reserve2(self):        
        string = "shit is rad!"
        expected_result = "Shit IS rad!"
        result = reverse(string)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()