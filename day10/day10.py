import collections
import math

import numpy as np


def day10a(input_path):
    int_list = [int(line.strip()) for line in open(input_path)]
    device = np.max(int_list) + 3
    outlet = 0
    int_list = [outlet] + int_list + [device]
    sorted_ints = np.sort(int_list)
    deltas = np.diff(sorted_ints)
    count = collections.Counter(deltas)
    return count[1] * count[3]


def test10a():
    assert 35 == day10a('test_input.txt')


def day10b(input_path):
    int_list = [int(line.strip()) for line in open(input_path)]
    device = np.max(int_list) + 3
    outlet = 0
    int_list = [outlet] + int_list + [device]
    sorted_ints = np.sort(int_list)
    deltas = np.diff(sorted_ints)

    options = 0
    counter = 0
    for delta in deltas:
        if delta == 1:
            counter += 1
        elif counter >= 1:
            options += counter - 1
            counter = 0
    import pdb; pdb.set_trace()

    return get_total_combinations(options)

def get_total_combinations(options):
    total = 0
    for val in range(1, options):
        total += n_choose_k(options, val)
    total += 2  # n choose n, n choose 0
    return total

def n_choose_k(n, k):
    return math.factorial(n) / math.factorial(k) / math.factorial(n - k)


def test10b():
    assert 8 == day10b('test_input.txt')
    assert 19208 == day10b('test_input2.txt')


if __name__ == '__main__':
    test10a()
    print('Day 10a:', day10a('day10_input.txt'))
    test10b()
    # print('Day 10b:', day10b('day10_input.txt'))
