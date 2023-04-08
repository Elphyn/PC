# Даны целые числа k, l. Если числа не равны, то заменить каждое из них одним и тем же числом,
# равным большему из исходных, а если равны, то заменить числа нулями.
__author__ = "Vlad Karelov"

import unittest

def maxx(a,b):
    if a > b:
        return a
    else:
        return b

def main(k: int,l: int):
    if k != l:
        k,l = maxx(k,l), maxx(k,l)
    else:
        k,l = 0,0
    # print(f"k: {k} \nl: {l}")
    return k, l
class TestFunctions(unittest.TestCase):
    def test_main_different_values(self):
        # Test Case 1
        # Input: k = 3, l = 7
        # Expected Output: (7, 7)
        self.assertEqual(main(3, 7), (7, 7))

        # Test Case 2
        # Input: k = 10, l = 2
        # Expected Output: (10, 10)
        self.assertEqual(main(10, 2), (10, 10))

    def test_main_same_values(self):
        # Test Case 3
        # Input: k = 5, l = 5
        # Expected Output: (0, 0)
        self.assertEqual(main(5, 5), (0, 0))

if __name__ == '__main__':
    unittest.main()


# написать max руками ✔️






