

def day15a(input_str, n_turns=2020):
    int_list = [int(val) for val in input_str.split(',')]
    spoken = dict()
    prev = None
    for turn in range(n_turns):
        if turn < len(int_list):
            val = int_list[turn]
        elif prev not in spoken:
            val = 0
        else:
            val = turn - 1 - spoken[prev]
        spoken[prev] = turn - 1
        prev = val
    return val


def test15a():
    assert 436 == day15a('0,3,6')


def day15b(input_str):
    return day15a(input_str, 30000000)


def test15b():
    assert 175594 == day15b('0,3,6')


if __name__ == '__main__':
    test15a()
    print('Day 15a:', day15a('10,16,6,0,1,17'))
    test15b()
    print('Day 15b:', day15b('10,16,6,0,1,17'))
