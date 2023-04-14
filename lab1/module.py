from math import sqrt

g = 9.81

def falltime(height:float):
    """returns time for objects fall"""
    result = sqrt(2*height/g)
    return result


def findMax(x,y,z:float):
    return (max(x+y+z/2,x*y*z))**2 + 1

def maxx(a,b):
    if a > b:
        return a
    else:
        return b

def main(k: int,l: int):
    if k != l:
        k,l = maxx(k,l), maxx(k,l)
    else:
        k,l = 0,0
    # print(f"k: {k} \nl: {l}")
    return k, l

def calc(n):
    k = 1
    result = 0
    for k in range(k,n):
        result += 1/(2*k+1)**2
    return result 

import random
import random


# решение
def sum_arr(a):
    result = 0
    for i in range(1, len(a)):
        result += (-1**i)*a[i]
    return result
        

def generate_list(n):
    """Generates a list with random numbers n lenght"""
    list = []
    for i in range(n):
        list.append(random.uniform(1,10))
    return list

import random
def sum_aliquot_numbers(list, check):
    """Takes array as an argument and returns sum of all numbers that are aliquot to 5"""

    # print(f"Array we work with: {array}")
    result = 0

    for i in range(len(list)):
        if check(list[i]):
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


def foo(n, x):
    """Takes n and x, returns calculated value"""
    result = 0
    F = 2
    denominator_factorial = 1

    for i in range(1, n):
        # Update the denominator's factorial
        denominator_factorial *= i ** 2

        # Calculate the current term of the series
        term = (F + abs(x)) / denominator_factorial

        # next
        F *= i + 2
        F *= i + 3

        # Add the term to the result
        result += term

    # Return the final result
    return result

import numpy as np

def array_transpose(a: np.array):
    """Transposes given array"""
    result = np.transpose(a)
    return result