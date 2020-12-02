import numpy as np


def day01(input_path, n=2):
    # n is the number of numbers in the list that must sum to 2020
    int_array = np.array([int(line) for line in open(input_path)])
    initial_inds = np.array(range(n))[::-1]
    inds = np.copy(initial_inds)
    return recursive_check(int_array, initial_inds, inds, n - 1)


def recursive_check(int_array, initial_inds, inds, level):
    for _ in range(len(int_array) - initial_inds[level] - 1):
        if level:
            result = recursive_check(int_array, initial_inds, inds, level - 1)
            if result:
                return result
        if 2020 == int_array[inds].sum():
            return int_array[inds].prod()
        inds[level] += 1
    inds[level] = initial_inds[level]


def test01a():
    assert 514579 == day01('test_input.txt')


def test01b():
    assert 241861950 == day01('test_input.txt', 3)


if __name__ == '__main__':
    test01a()
    print('Day 01a:', day01('day01_input.txt'))
    test01b()
    print('Day 01b:', day01('day01_input.txt', 3))
