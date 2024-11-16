import math
import unittest
import triangle


class TestTriangleMethods(unittest.TestCase):
    raise_test_data = [[-1, 1, 1], [1, -1, 1], [1, 1, -1], [0, 0, 0], [10, 1, 1], [1, 10, 1], [1, 1, 10]]
    equal_test_data = [[1, 1, 1], [2 * 2 ** 0.5, math.e, 3], [3, 4, 5], [10000, 10001, 10002]]

    def test_area_raises(self):
        for i in self.raise_test_data:
            a = i[0]
            b = i[1]
            c = i[2]
            self.assertRaises(ValueError, triangle.area, a, b, c)

    def test_area(self):
        for i in self.equal_test_data:
            a = i[0]
            b = i[1]
            c = i[2]
            p = (a + b + c) / 2
            expected = p ** 0.5 * (p - a) * (p - b) * (p - c)

            self.assertEqual(triangle.area(a, b, c), expected)

    def test_perimeter_raises(self):
        for i in self.raise_test_data:
            a = i[0]
            b = i[1]
            c = i[2]
            self.assertRaises(ValueError, triangle.perimeter, a, b, c)

    def test_perimeter(self):
        for i in self.equal_test_data:
            a = i[0]
            b = i[1]
            c = i[2]
            expected = a + b + c

            self.assertEqual(triangle.perimeter(a, b, c), expected)


if __name__ == '__main__':
    unittest.main()
