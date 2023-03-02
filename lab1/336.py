# https://ivtipm.github.io/Programming/Glava01/index01.htm#z10
# Даны натуральное число n, действительное число х. 
__author__ = "Vlad Karelov"
from math import factorial

def foo(n, x):
    """Takes n and x, returns calculated value"""
    result = 0
    for i in range(1, n):
        result += (factorial(2*i)+abs(x))/factorial(i**2)
    return result


def main():
    """Script execution"""

    # User input
    n = int(input('Enter n: '))
    x = int(input('Enter x: '))

    # Main part
    result = foo(n, x)
    print(f'Result: {result}')


if __name__ == '__main__':
    main()

# факториал переделать


