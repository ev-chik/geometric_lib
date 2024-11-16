
def area(a):
    if a <= 0:
        raise ValueError("Side can't be negative")
    return a * a


def perimeter(a):
    if a <= 0:
        raise ValueError("Side can't be negative")
    return 4 * a
