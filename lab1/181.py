# https://ivtipm.github.io/Programming/Glava01/index01.htm#z10
# Даны целые числа a1,...a50. Получить сумму тех чисел данной последовательности, которые кратные 5
__author__ = "Vlad Karelov"
from module import sum_aliquot_numbers, create_array

def main():
    """script execution"""

    # create list
    list = create_array(5)
    print(f'Generated list: {list}')

    # sum all numbers that are aliquot to 5
    result = sum_aliquot_numbers(list, lambda x: x % 5 == 0)

    #print the result
    print(result)

import unittest
def is_aliquot_to_5(num):
    return num % 5 == 0    
class TestSumAliquotNumbers(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_aliquot_numbers([], is_aliquot_to_5), 0)

    def test_no_aliquot_numbers(self):
        self.assertEqual(sum_aliquot_numbers([1, 2, 3, 4], is_aliquot_to_5), 0)

    def test_some_aliquot_numbers(self):
        self.assertEqual(sum_aliquot_numbers([5, 10, 15, 20], is_aliquot_to_5), 50)

    def test_all_aliquot_numbers(self):
        self.assertEqual(sum_aliquot_numbers([5, 25, 125], is_aliquot_to_5), 155)

if __name__ == '__main__':
    unittest.main()


# переделать проверка a кратности 5✔️
# разбить на функции✔️
# Сделать без numpy✔️





