# https://ivtipm.github.io/Programming/Glava01/index01.htm#z10
# Определить время падения камня на поверхности земли с высоты h.
__author__ = "Vlad Karelov"
from math import sqrt
g = 9.81;


def fallTime(height:float):
    """returns time for objects fall"""
    return sqrt(2*height/g)



h = float(input("Enter height: "))
print(f"Time: {fallTime(h):.2f}")
