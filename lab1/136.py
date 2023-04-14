# https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
# Даны натуральное число n, действительные числа a1,..., an. Вычислить:
#  a1 - a2 + a3 - ... + (-1)^n+1an;
# import numpy as np
__author__ = "Vlad Karelov"
from module import generate_list, sum_arr
import unittest

def main():
    n = int(input("Enter n: "))

    data = generate_list(n)

    print(f"List we work with: {data}")
    print(f"Result: {sum_arr(data)}")


class TestFunctions(unittest.TestCase):

    def test_sum_arr(self):
        # Test Case 1
        # Input: a = [1, 2, 3, 4, 5]
        # Expected Output: -14
        self.assertEqual(sum_arr([1, 2, 3, 4, 5]), -14)

        # Test Case 2
        # Input: a = [1, -2, 3, -4, 5]
        # Expected Output: -2
        self.assertEqual(sum_arr([1, -2, 3, -4, 5]), -2)

    def test_generate_list(self):
        # Test Case 1
        # Input: n = 3
        # Expected Output: A list of 3 random numbers between 1 and 10
        self.assertEqual(len(generate_list(3)), 3)
        for num in generate_list(3):
            self.assertGreaterEqual(num, 1)
            self.assertLessEqual(num, 10)

        # Test Case 2
        # Input: n = 0
        # Expected Output: An empty list
        self.assertEqual(generate_list(0), [])

if __name__ == '__main__':
    unittest.main()

# функция заполнения масива рандомно✔️
# добавить коментарии✔️
# функция генерация списка, не использовать numpy✔️

