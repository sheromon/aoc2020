import numpy as np


def day01a(input_path):
    int_list = [int(line) for line in open(input_path)]
    ints1 = np.array(int_list)
    ints2 = np.copy(ints1)
    for _ in range(len(int_list) // 2):
        ints2 = np.append(ints2[1:], ints2[0])
        sums = ints1 + ints2
        match = np.where(sums == 2020)[0]
        if match.size:
            return ints1[match[0]] * ints2[match[0]]


def test01a():
    assert 514579 == day01a('test_input.txt')


if __name__ == '__main__':
    test01a()
    print('Day 01a:', day01a('day01_input.txt'))
