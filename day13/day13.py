import numpy as np


def day13a(input_path):
    lines = [line.strip() for line in open(input_path)]
    start = int(lines[0])
    bus_ids = [int(val) for val in lines[1].split(',') if val != 'x']
    departs = [int(np.ceil(start/bid) * bid) for bid in bus_ids]
    ind = np.argmin(departs)
    my_bus_id = bus_ids[ind]
    wait = departs[ind] - start
    return my_bus_id * wait


def test13a():
    assert 295 == day13a('test_input.txt')


def day13b(bus_ids_str=None):
    if bus_ids_str is None:
        input_path = 'day13_input.txt'
        lines = [line.strip() for line in open(input_path)]
        bus_ids_str = lines[1]

    bus_id_ind_pairs = [(int(val), ind) for ind, val in enumerate(bus_ids_str.split(',')) if val != 'x']
    return check_multiples(bus_id_ind_pairs)


def check_multiples(bus_id_ind_pairs):
    interval, _ = bus_id_ind_pairs.pop(0)
    val = 0
    while bus_id_ind_pairs:
        max_id_pair = max(bus_id_ind_pairs)
        bus_id_ind_pairs.remove(max_id_pair)
        max_bus_id, max_ind = max_id_pair
        while True:
            if (val + max_ind) % max_bus_id == 0:
                break
            val += interval
        interval *= max_bus_id
    return val


def test13b():
    assert 3417 == day13b('17,x,13,19')
    assert 754018 == day13b('67,7,59,61')
    assert 1202161486 == day13b('1789,37,47,1889')


if __name__ == '__main__':
    test13a()
    print('Day 13a:', day13a('day13_input.txt'))
    test13b()
    print('Day 13b:', day13b())
