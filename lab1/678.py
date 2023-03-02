# https://ivtipm.github.io/Programming/Glava01/index01.htm#z10
# Дана действительная квадратная матрица, порядка n. Преобразовать матрицу по правилу:
#  строку с номером n сделать столбцом с номером n, а столбец с номером n сделать строкой с номером n.
__author__ = "Vlad Karelov"
import numpy as np

def main(a,n):
    print(f"{a}\n")
    result = np.zeros_like(a)
    for i in range(len(a)):
        for j in range(len(a)):
            result[i,j] = a[j,i]
    return result
    


n = int(input("Enter n: "))
a = np.array([[i for i in range(n)] for i in range(n)])
print(
    main(a,n)
)

# одна строчка Numpy transpose?
# рандомная генерация массива