import collections
import math

import numpy as np


def day10a(input_path):
    deltas = get_consecutive_deltas(input_path)
    count = collections.Counter(deltas)
    return count[1] * count[3]


def get_consecutive_deltas(input_path):
    int_list = [int(line.strip()) for line in open(input_path)]
    device = np.max(int_list) + 3  # device joltage is 3 higher than the max adapter
    outlet = 0  # outlet is always 0
    int_list = [outlet] + int_list + [device]
    sorted_ints = np.sort(int_list)
    deltas = np.diff(sorted_ints)
    return deltas


def test10a():
    assert 35 == day10a('test_input.txt')


def day10b(input_path):
    deltas = get_consecutive_deltas(input_path)
    count = collections.Counter(deltas)
    assert len(count) == 2
    assert 1 in count
    assert 3 in count

    # the count shows that the deltas between consecutive values are all either
    # ones or threes. in any consecutive sequence of ones, the number of
    # optional adapters is len(consecutive ones) - 1. each group of one or more
    # consecutive optional adapters is independent of the others, so we can
    # calculate the number of combinations for each group and multiply them all.
    total_combs = 1
    counter = 0
    lookup = CombinationLookup()
    for delta in deltas:
        if delta == 1:
            counter += 1
        elif counter >= 1:
            options = counter - 1
            total_combs *= lookup[options]
            counter = 0

    return total_combs


class CombinationLookup:
    # sadly, I couldn't figure out a formula to calculate the number of
    # combinations for a given number of consecutive optional adapters, but
    # after calculating a number of cases by hand, I noticed a pattern.
    def __init__(self):
        self.num_combinations = [1, 2, 4, 7]

    def __getitem__(self, num_optional):
        ind = len(self.num_combinations)
        while num_optional >= ind:
            self.num_combinations[ind] = np.sum(self.num_combinations[ind-3:ind])
            ind += 1
        return self.num_combinations[num_optional]


def test10b():
    assert 8 == day10b('test_input.txt')
    assert 19208 == day10b('test_input2.txt')


if __name__ == '__main__':
    test10a()
    print('Day 10a:', day10a('day10_input.txt'))
    test10b()
    print('Day 10b:', day10b('day10_input.txt'))
