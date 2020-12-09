import numpy as np


def day09a(input_path, pre_length=25):
    int_list = [int(line.strip()) for line in open(input_path)]
    for ind in range(pre_length, len(int_list)):
        val = int_list[ind]
        print(val)
        pre_vals = int_list[ind-pre_length:ind]
        if not is_valid(val, pre_vals):
            return val
    print('No solution found')


def is_valid(val, pre_vals):
    pre_vals = np.array(pre_vals)
    pre_vals2 = np.append(pre_vals[1:], pre_vals[0])
    for n in range(len(pre_vals)):
        sums = pre_vals + pre_vals2
        if val in sums.tolist():
            return True
        pre_vals2 = np.append(pre_vals2[1:], pre_vals2[0])


def test09a():
    assert 127 == day09a('test_input.txt', 5)


def day09b(input_path):
    pass


def test09b():
    assert 62 == day09b('test_input.txt', 5)


if __name__ == '__main__':
    test09a()
    print('Day 09a:', day09a('day09_input.txt'))
    # test09b()
    # print('Day 09b:', day09b('day09_input.txt'))
