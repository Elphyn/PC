# https://ivtipm.github.io/Programming/Glava01/index01.htm#z10
# Даны натуральное число n, действительное число х. 
__author__ = "Vlad Karelov"
from module import sum336


def main():
    """Script execution"""

    # User input
    n = int(input('Enter n: '))
    x = int(input('Enter x: '))

    # Main part
    result = sum336(n, x)
    print(f'Result: {result}')


import unittest

class TestFoo(unittest.TestCase):

    def test_foo_with_positive_x(self):
        self.assertAlmostEqual(sum336(3, 2), 10.5, delta=0.01)
        self.assertAlmostEqual(sum336(4, 3), 25.16, delta=0.01)

    def test_foo_with_negative_x(self):
        self.assertAlmostEqual(sum336(5, -1), 47.61, delta=0.01)

    def test_foo_with_zero_x(self):
        self.assertAlmostEqual(sum336(6, 0), 88.33, delta=0.01)

if __name__ == '__main__':
    # main()
    unittest.main()



# факториал переделать


