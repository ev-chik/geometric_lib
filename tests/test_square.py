import math
import unittest
import square


class TestSquareMethods(unittest.TestCase):
    raise_test_data = [-100000, -500, -100, -1, 0]
    equal_test_data = [1, 100, 10000000, 0.1, 2 ** 0.5, math.e]

    def test_area_raises(self):
        for i in self.raise_test_data:
            self.assertRaises(ValueError, square.area, i)

    def test_area(self):
        for i in self.equal_test_data:
            input_value = i
            expected = input_value ** 2

            self.assertEqual(square.area(input_value), expected)

    def test_perimeter_raises(self):
        for i in self.raise_test_data:
            self.assertRaises(ValueError, square.perimeter, i)

    def test_perimeter(self):
        for i in self.equal_test_data:
            input_value = i
            expected = 4 * input_value

            self.assertEqual(square.perimeter(input_value), expected)


if __name__ == '__main__':
    unittest.main()
