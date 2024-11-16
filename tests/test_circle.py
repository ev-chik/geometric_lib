import math
import unittest
import circle


class TestCircleMethods(unittest.TestCase):
    pi = 3.141592653589793

    raise_test_data = [-100000, -500, -100, -1, 0]
    equal_test_data = [1, 100, 10000000, 0.1, 2 ** 0.5, math.e]

    def test_area_raises(self):
        for i in self.raise_test_data:
            self.assertRaises(ValueError, circle.area, i)

    def test_area(self):
        for i in self.equal_test_data:
            input_value = i
            expected = self.pi * input_value ** 2

            self.assertAlmostEqual(circle.area(input_value), expected, 5)

    def test_perimeter_raises(self):
        for i in self.raise_test_data:
            self.assertRaises(ValueError, circle.perimeter, i)

    def test_perimeter(self):
        for i in self.equal_test_data:
            input_value = i
            expected = 2 * self.pi * input_value

            self.assertAlmostEqual(circle.perimeter(input_value), expected, 5)


if __name__ == '__main__':
    unittest.main()
