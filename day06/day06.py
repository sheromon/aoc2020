

def day06a(input_path):
    responses = [line.strip() for line in open(input_path)]
    group_response = set()
    total = 0
    for response in responses:
        if not response:
            group_total = len(group_response)
            total += group_total
            group_response = set()
        else:
            group_response |= set(response)
    group_total = len(group_response)
    total += group_total
    return total


def test06a():
    assert 11 == day06a('test_input.txt')


def day06b(input_path):
    responses = [line.strip() for line in open(input_path)]
    group_response = None
    total = 0
    for response in responses:
        if not response:
            group_total = len(group_response)
            total += group_total
            group_response = None
        elif group_response is None:
            group_response = set(response)
        else:
            group_response &= set(response)
    group_total = len(group_response)
    total += group_total
    return total


def test06b():
    assert 6 == day06b('test_input.txt')


if __name__ == '__main__':
    test06a()
    print('Day 06a:', day06a('day06_input.txt'))
    test06b()
    print('Day 06b:', day06b('day06_input.txt'))
