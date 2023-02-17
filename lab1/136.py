# https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
import numpy as np
__author__ = "Vlad Karelov"

def main(n: int, a:list):
    result = 0
    for i in range(1, n):
        result += (-1**i)*a[i]
    return result
        


n = int(input("Enter n: "))
data = np.zeros(n, float)
for i in range(n):
    dummy = int(input(f"Enter data[{i+1}]"))
    data[i] = dummy

print(f"Result: {main(n,data)}")



