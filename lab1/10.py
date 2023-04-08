# https://ivtipm.github.io/Programming/Glava01/index01.htm#z10
# Определить время падения камня на поверхности земли с высоты h.
__author__ = "Vlad Karelov"
from math import sqrt
import pytest
g = 9.81


def falltime(height:float):
    """returns time for objects fall"""
    result = sqrt(2*height/g)
    return result


def test_falltime():
    # Test Case 1
    # Input: height = 0
    # Expected Output: 0.00
    assert falltime(0) == 0.00

    # Test Case 2
    # Input: height = 10
    # Expected Output: 1.43 (approx +-0.01)
    assert falltime(10) == pytest.approx(1.43, rel=1e-2)

    # Test Case 3
    # Input: height = 100
    # Expected Output: 4.52 (approx +-0.01)
    assert falltime(100) == pytest.approx(4.52, rel=1e-2)


if __name__ == '__main__':
    h = float(input("Enter height: "))
    print(f"Time: {falltime(h):.2f}")

    # run the test function
    test_falltime()
