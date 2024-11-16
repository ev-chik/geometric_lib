import unittest
import calculate
import circle
import square
import triangle


class TestCalculate(unittest.TestCase):
    raise_test_data = [
        ['hypercube', 'area', [1]], ['triangle', 'height', [1]],
        ['circle', 'area', [1, 2]], ['square', 'perimeter', [2, 3]],
        ['triangle', 'area', [1]]
    ]

    equal_test_data = [
        ['circle', 'area', [2]], ['square', 'perimeter', [5]],
        ['triangle', 'area', [3, 4, 5]], ['circle', 'perimeter', [1.5]],
        ['square', 'area', [2 ** 0.5]]
    ]

    functions = {
        ('circle', 'area'): circle.area,
        ('circle', 'perimeter'): circle.perimeter,
        ('square', 'area'): square.area,
        ('square', 'perimeter'): square.perimeter,
        ('triangle', 'area'): triangle.area,
        ('triangle', 'perimeter'): triangle.perimeter
    }

    def test_raises(self):
        for i in self.raise_test_data:
            figure = i[0]
            function = i[1]
            size = i[2]

            self.assertRaises(AssertionError, calculate.calc,
                              figure, function, size)

    def test_calc(self):
        for i in self.equal_test_data:
            figure = i[0]
            function = i[1]
            size = i[2]

            key = (figure, function)
            expected = self.functions.get(key)(*size)

            self.assertEqual(calculate.calc(figure, function, size), expected)
