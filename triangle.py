def area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side can't be negative")
    elif a + b <= c or b + c <= a or a + c <= b:
        raise ValueError("One side can't be longer than two other")
    p = perimeter(a, b, c) / 2
    return p ** 0.5 * (p - a) * (p - b) * (p - c)


def perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side can't be negative")
    elif a + b <= c or b + c <= a or a + c <= b:
        raise ValueError("One side can't be longer than two other")
    return a + b + c
