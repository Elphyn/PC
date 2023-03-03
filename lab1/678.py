# https://ivtipm.github.io/Programming/Glava01/index01.htm#z10
# Дана действительная квадратная матрица, порядка n. Преобразовать матрицу по правилу:
#  строку с номером n сделать столбцом с номером n, а столбец с номером n сделать строкой с номером n.
__author__ = "Vlad Karelov"
import numpy as np


def foo(a: np.array):
    """Transposes given array"""
    result = np.transpose(a)
    return result
    
def main():
    """Script execution"""

    # User input
    n = int(input("Enter n: "))

    # Random generated numpy array with size n
    a = np.random.randint(0, 10, size=(n,n))

    # Generated array
    print(f"{a}\n")

    # Transpose array
    a = foo(a)

    # Result
    print(a)

if __name__ == '__main__':
    main()


# одна строчка Numpy transpose?✔️
# в numpy методы работают быстрей✔️
# рандомная генерация массива✔️