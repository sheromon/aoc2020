

def day16a(input_path):
    lines = [line.strip() for line in open(input_path)]
    rules = dict()
    invalid_vals = []
    section = 'rules'
    for line in lines:
        if not line:
            continue
        if section == 'rules':
            if line == 'your ticket:':
                section = 'your ticket'
                continue
            field, _, ranges = line.partition(':')
            ranges = ranges.split(' or ')
            bounds = []
            for range_str in ranges:
                lo, hi = range_str.split('-')
                bounds.append((int(lo), int(hi)))
            rules[field] = bounds
        elif section == 'your ticket':
            if line == 'nearby tickets:':
                section = 'nearby tickets'
        elif section == 'nearby tickets':
            vals = [int(val) for val in line.split(',')]
            for val in vals:
                if not is_potentially_valid(val, rules):
                    invalid_vals.append(val)
    return sum(invalid_vals)


def is_potentially_valid(val, rules):
    for rule in rules.values():
        for bounds in rule:
            if bounds[0] <= val <= bounds[1]:
                return True
    return False

def test16a():
    assert 71 == day16a('test_input.txt')


def day16b(input_path):
    pass


# def test16b():
#     assert 286 == day16b('test_input.txt')


if __name__ == '__main__':
    test16a()
    print('Day 16a:', day16a('day16_input.txt'))
    # test16b()
    # print('Day 16b:', day16b('day16_input.txt'))
