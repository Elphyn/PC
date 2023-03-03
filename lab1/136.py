# https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
# Даны натуральное число n, действительные числа a1,..., an. Вычислить:
#  a1 - a2 + a3 - ... + (-1)^n+1an;
# import numpy as np
import random
__author__ = "Vlad Karelov"


# решение
def sum_arr(a):
    """"""
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

def main():
    # ввод данных
    n = int(input("Enter n: "))

    data = generate_list(n)

    print(f"List we work with: {data}")
    print(f"Result: {sum_arr(data)}")

if __name__ == '__main__':
    main()

# функция заполнения масива рандомно✔️
# добавить коментарии✔️

# функция генерация списка, не использовать numpy✔️

