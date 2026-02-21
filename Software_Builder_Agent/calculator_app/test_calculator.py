import unittest
from main import calculate

class TestCalculator(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(calculate("3 + 2"), 5)
        self.assertEqual(calculate("3+2"), 5)
        
    def test_subtraction(self):
        self.assertEqual(calculate("5 - 2"), 3)
        self.assertEqual(calculate("5-2"), 3)
        self.assertEqual(calculate("3 - -2"), 5)
        
    def test_multiplication(self):
        self.assertEqual(calculate("3 * 4"), 12)
        self.assertEqual(calculate("3*4"), 12)
        
    def test_division(self):
        self.assertEqual(calculate("10 / 2"), 5.0)
        self.assertEqual(calculate("10/2"), 5.0)
        
    def test_multiple_operations(self):
        self.assertEqual(calculate("3 + 2 * 2"), 10)  # Left to right evaluation
        self.assertEqual(calculate("10 - 3 + 2"), 9)  # Left to right evaluation
        
    def test_negative_numbers(self):
        self.assertEqual(calculate("-3 + 5"), 2)
        self.assertEqual(calculate("5 + -3"), 2)
        
    def test_division_by_zero(self):
        self.assertEqual(calculate("10 / 0"), "Error: Division by zero.")
        
    def test_invalid_input(self):
        self.assertEqual(calculate("3 + abc"), "Error: Operand must be a number.")
        self.assertEqual(calculate("abc + 3"), "Error: The first token must be a number.")
        self.assertEqual(calculate("3 +"), "Error: Missing operand after operator.")
        self.assertEqual(calculate(""), "Error: Empty expression")
        self.assertEqual(calculate("3 % 2"), "Error: Unknown operator.")

if __name__ == '__main__':
    unittest.main()