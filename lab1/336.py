# https://ivtipm.github.io/Programming/Glava01/index01.htm#z10
# Даны натуральное число n, действительное число х. 
__author__ = "Vlad Karelov"
from math import factorial

def main(x):
    result = 0
    for i in range(1,x):
        result +=(factorial(2*i)+abs(x))/(factorial(i**2))
    return result

print(main(
    int(input("Enter x:"))
))




