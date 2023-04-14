# https://ivtipm.github.io/Programming/Glava02/index02.htm#z35
# Даны действительные числа x, y, z. Вычислить: 
# max^2(x + y + z/2, xyz) + 1.
__author__ = "Vlad Karelov"
import pytest
from module import findMax

def test_findMax():
    # Test Case 1
    # Input: x = 1, y = 2, z = 3
    # Expected Output: 8.25
    assert findMax(1, 2, 3) == pytest.approx(8.25, rel=1e-2)

    # Test Case 2
    # Input: x = 4, y = 5, z = 6
    # Expected Output: 3810.25
    assert findMax(4, 5, 6) == pytest.approx(3810.25, rel=1e-2)

    # Test Case 3
    # Input: x = 0.5, y = 0.5, z = 0.5
    # Expected Output: 1.25
    assert findMax(0.5, 0.5, 0.5) == pytest.approx(1.25, rel=1e-2)

    

