import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {'circle': 1,
         'square': 1,
         'triangle': 3}


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs
    assert len(size) == sizes.get(fig)

    result = eval(f'{fig}.{func}(*{size})')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}"):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square, 3 for triangle\n").split(' ')))

    calc(fig, func, size)
