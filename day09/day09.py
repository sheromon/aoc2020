import numpy as np


def day09a(input_path, pre_length=25):
    int_list = [int(line.strip()) for line in open(input_path)]
    for ind in range(pre_length, len(int_list)):
        val = int_list[ind]
        pre_vals = int_list[ind-pre_length:ind]
        if not is_valid(val, pre_vals):
            return val


def is_valid(val, pre_vals):
    pre_vals = np.array(pre_vals)
    pre_vals2 = np.copy(pre_vals)
    pre_vals2 = np.append(pre_vals2[1:], pre_vals2[0])
    for _ in range(len(pre_vals)):
        sums = pre_vals + pre_vals2
        if val in sums:
            return True
        pre_vals2 = np.append(pre_vals2[1:], pre_vals2[0])


def test09a():
    assert 127 == day09a('test_input.txt', 5)


def day09b(input_path, pre_length=25):
    val = day09a(input_path, pre_length)
    int_array = np.array([int(line.strip()) for line in open(input_path)])
    cumsum = np.cumsum(int_array)
    for ind in range(len(cumsum)):
        deltas = cumsum[ind+1:] - cumsum[ind]
        if np.any(deltas == val):
            delta_ind = np.where(deltas == val)[0][0]
            first_ind = ind + 1
            last_ind = ind + delta_ind + 1
            min_val = np.min(int_array[first_ind:last_ind+1])
            max_val = np.max(int_array[first_ind:last_ind+1])
            return min_val + max_val


def test09b():
    assert 62 == day09b('test_input.txt', 5)


if __name__ == '__main__':
    test09a()
    print('Day 09a:', day09a('day09_input.txt'))
    test09b()
    print('Day 09b:', day09b('day09_input.txt'))
