import unittest
from calculator import Calculator

class TestAddFunction(unittest.TestCase):
    def test_add_function(self):
        result = Calculator.add_function(1, 3)
        self.assertEqual(result, 4)

        result = Calculator.add_function(-3, 3)
        self.assertEqual(result, 0)

        result = Calculator.add_function(-4, -4)
        self.assertEqual(result, -8)

if __name__ == "__main__":
    unittest.main()
