# https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
# Даны натуральное число n, действительные числа a1,..., an. Вычислить: 
import numpy as np
__author__ = "Vlad Karelov"


# решение
def main(n: int, a:list):
    result = 0
    for i in range(1, n):
        result += (-1**i)*a[i]
    return result
        

# ввод данных
n = int(input("Enter n: "))
# генерация массива
data = np.random.uniform(1,10,n)
print(data)


print(f"Result: {main(n,data)}")

# функция заполнения масива рандомно✔️
# добавить коментарии✔️

