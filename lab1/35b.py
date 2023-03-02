# https://ivtipm.github.io/Programming/Glava02/index02.htm#z35
# Даны действительные числа x, y, z. Вычислить: 
# max^2(x + y + z/2, xyz) + 1.
__author__ = "Vlad Karelov"


def findMax(x,y,z:float):
    return (max(x+y+z/2,x*y*z))**2 + 1


print(findMax(
    float(input("Enter x:")),
    float(input("Enter y:")),
    float(input("Enter z:"))
))

