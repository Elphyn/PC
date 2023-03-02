# https://ivtipm.github.io/Programming/Glava01/index01.htm#z10
# Даны целые числа a1,...a50. Получить сумму тех чисел данной последовательности, которые кратные 5
__author__ = "Vlad Karelov"
import numpy as np

def sum_aliquot_numbers(array):
    """Takes array as an argument and returns sum of all numbers that are aliquot to 5"""
    print(f"Array we work with: {array}")
    result = 0

    for i in range(len(array)):
        if array[i] % 5 == 0:
            result += array[i]
    return result


def create_array(n):
    """creates array of n length and fills it with random numbers from 1-100"""
    data = np.zeros(n, dtype=int)

    for i in range(n):
        dummy = np.random.randint(1,100)
        data[i] = dummy

    return data

def main():
    """script execution"""

    # create an array
    array = create_array(50)

    # sum all numbers that are aliquot to 5
    result = sum_aliquot_numbers(array)

    #print the result
    print(result)

if __name__ == '__main__':
    main()


# переделать проверка a кратности 5✔️
# разбить на функции✔️






