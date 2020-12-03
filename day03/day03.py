import numpy as np


def day03a(input_path, slope):
    '''Count the number of "trees" encountered going down the slope.'''
    rows = []
    with open(input_path) as file_obj:
        for line in file_obj:
            row = list(line.strip())
            rows.append([val == '#' for val in row])
    pattern = np.array(rows).astype(np.uint8)
    total = 0
    coords = np.array([0, 0])
    slope = np.array(slope[::-1])
    for irow in range(pattern.shape[0]):
        total += pattern[coords[0], coords[1]]
        coords += slope
        if coords[0] > pattern.shape[0]:
            break
        coords[1] = coords[1] % pattern.shape[1]
    return total


def test03a():
    assert 7 == day03a('test_input.txt', [3, 1])


def day03b(input_path):
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    product = 1
    for slope in slopes:
        product *= day03a(input_path, slope)
    return product


def test03b():
    assert 336 == day03b('test_input.txt')


if __name__ == '__main__':
    test03a()
    print('Day 03a:', day03a('day03_input.txt', [3, 1]))
    test03b()
    print('Day 03b:', day03b('day03_input.txt'))
