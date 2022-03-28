import unittest
import sys
sys.path.insert(0, '/Users/Olli/Desktop/AW/AW-testing-harjoitukset/viikko2/testaus/FizzBuzz')

from fizzbuzz import fizzbuzz

class TestCalculator(unittest.TestCase):

    def test_Fizz(self):        
        num1 = 9
        expected_result = 'Fizz'
        result = fizzbuzz(num1)
        self.assertEqual(result, expected_result)

    def test_Buzz(self):        
        num1 = 10
        expected_result = 'Buzz'
        result = fizzbuzz(num1)
        self.assertEqual(result, expected_result)

    def test_jako(self):        
        num1 = 15
        expected_result = 'FizzBuzz'
        result = fizzbuzz(num1)
        self.assertEqual(result, expected_result)
    
    def test_kertolasku(self):        
        num1 = 8
        expected_result = 8
        result = fizzbuzz(num1)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()