import numpy as np


def day23a(input_str, num_moves=100):
    cups = [int(val) for val in list(input_str)]

    current_ind = 0
    prev_cups_after_one = None
    for move in range(num_moves):
        increment = 1
        current_label = cups[current_ind]
        next_three = []
        next_ind = current_ind + 1
        for _ in range(3):
            next_ind = next_ind % len(cups)
            next_three.append(cups.pop(next_ind))
            increment -= (next_ind < current_ind)
        dest_label = current_label - 1
        while dest_label not in cups:
            dest_label -= 1
            if dest_label < min(cups):
                dest_label = max(cups)
                break
        dest_ind = cups.index(dest_label)
        cups = cups[:dest_ind+1] + next_three + cups[dest_ind+1:]
        if dest_ind < current_ind:
            increment += 3
        current_ind += increment
        current_ind = current_ind % len(cups)

    ind = cups.index(1)
    next_ind = (ind + 1) % len(cups)
    final_ordering = [str(cup) for cup in cups[next_ind:] + cups[:next_ind-1]]
    return ''.join(final_ordering)


def test23a():
    assert '92658374' == day23a('389125467', 10)


def day23b(input_str, num_moves=10000000, num_cups=1000000):
    pass


def test23b():
    assert 149245887792 == day23b('389125467', 10, 100)


if __name__ == '__main__':
    test23a()
    print('Day 23a:', day23a('362981754'))
    # test23b()
    # print('Day 23b:', day23b('362981754'))
