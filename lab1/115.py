# Дано натуральное число n. Вычислить: 
__author__ = "Vlad Karelov"
import unittest
from module import calc



class TestFunctions(unittest.TestCase):
    def test_calc(self):
        # Test Case 1
        # Input: n = 1
        # Expected Output: 0
        self.assertEqual(calc(1), 0)

        # Test Case 2
        # Input: n = 2
        # Expected Output: 0.11 (approximate)
        self.assertAlmostEqual(calc(2), 0.11, delta=0.01)

        # Test Case 3
        # Input: n = 5
        # Expected Output: 0.18 (approximate)
        self.assertAlmostEqual(calc(5), 0.18, delta=0.01)

if __name__ == '__main__':
    unittest.main()


