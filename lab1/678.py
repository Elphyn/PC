# https://ivtipm.github.io/Programming/Glava01/index01.htm#z10
# Дана действительная квадратная матрица, порядка n. Преобразовать матрицу по правилу:
#  строку с номером n сделать столбцом с номером n, а столбец с номером n сделать строкой с номером n.
__author__ = "Vlad Karelov"
import numpy as np
from module import array_transpose

def main():
    """Script execution"""

    # User input
    n = int(input("Enter n: "))

    # Random generated numpy array with size n
    a = np.random.randint(0, 10, size=(n,n))

    # Generated array
    print(f"{a}\n")

    # Transpose array
    a = array_transpose(a)

    # Result
    print(a)

import unittest

class TestArrayTranspose(unittest.TestCase):

    def test_2d_array(self):
        input_array = np.array([[1, 2], [3, 4]])
        expected_output = np.array([[1, 3], [2, 4]])
        self.assertTrue(np.array_equal(array_transpose(input_array), expected_output))


    def test_empty_array(self):
        input_array = np.array([])
        expected_output = np.array([])
        self.assertTrue(np.array_equal(array_transpose(input_array), expected_output))


if __name__ == '__main__':
    unittest.main()





# одна строчка Numpy transpose?✔️
# в numpy методы работают быстрей✔️
# рандомная генерация массива✔️