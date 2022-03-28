import unittest
import sys
sys.path.insert(0, '/Users/Olli/Desktop/AW/AW-testing-harjoitukset/viikko2/testaus/calculator')

from calculator import plus,minus,jako,kertolasku

class TestCalculator(unittest.TestCase):

    def test_plus(self):        
        num1 = num2 = 2
        expected_result = 4
        result = plus(num1,num2)
        self.assertEqual(result, expected_result)

    def test_minus(self):        
        num1 = num2 = 2
        expected_result = 0
        result = minus(num1,num2)
        self.assertEqual(result, expected_result)

    def test_jako(self):        
        num1 = num2 = 6
        expected_result = 1
        result = jako(num1,num2)
        self.assertEqual(result, expected_result)
    
    def test_kertolasku(self):        
        num1 = num2 = 3
        expected_result = 9
        result = kertolasku(num1,num2)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()