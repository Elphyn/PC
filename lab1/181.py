# https://ivtipm.github.io/Programming/Glava01/index01.htm#z10
# Даны целые числа a1,...a50. Получить сумму тех чисел данной последовательности, которые кратные 5
__author__ = "Vlad Karelov"
# import numpy as np
import random
def sum_aliquot_numbers(list):
    """Takes array as an argument and returns sum of all numbers that are aliquot to 5"""

    # print(f"Array we work with: {array}")
    result = 0

    for i in range(len(list)):
        if list[i] % 5 == 0:
            result += list[i]
    return result


def create_array(n):
    """creates array of n length and fills it with random numbers from 1-100"""
    data = []

    for i in range(n):
        data.append(random.randint(1,10))
        # dummy = np.random.randint(1,100)
        # data[i] = dummy
    return data

def main():
    """script execution"""

    # create list
    list = create_array(5)
    print(f'Generated list: {list}')

    # sum all numbers that are aliquot to 5
    result = sum_aliquot_numbers(list)

    #print the result
    print(result)



if __name__ == '__main__':
    main()

# переделать проверка a кратности 5✔️
# разбить на функции✔️

# Сделать без numpy✔️





