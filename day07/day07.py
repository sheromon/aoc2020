

def day07a(input_path):
    rules = [line.strip() for line in open(input_path)]
    rules_dict = dict()
    leftovers = set(['s.', '.'])
    for rule in rules:
        color, _, remainder = rule.partition(' bags contain ')
        remainder = remainder.replace('s,', '')
        remainder = remainder.replace(',', '')
        remainder = remainder.replace('s.', '')
        remainder = remainder.replace('.', '')
        contents = [item.strip() for item in remainder.split('bag')]
        inner_colors = dict()
        for bag in contents:
            if not bag:
                continue
            if bag == 'no other':
                continue
            number, _, inner_color = bag.partition(' ')
            inner_colors[inner_color] = int(number)
        rules_dict[color] = inner_colors

    holders = []
    get_holders('shiny gold', rules_dict, holders)
    print(holders)
    return len(holders)


def get_holders(target, rules_dict, holders):
    done = True
    for color, contents in rules_dict.items():
        if target in contents.keys():
            if color in holders:
                continue
            holders.append(color)
            done = False
    if not done:
        for color in holders:
            done = get_holders(color, rules_dict, holders)
    return done

def test07a():
    assert 4 == day07a('test_input.txt')


def day07b(input_path):
    return total


def test07b():
    assert 6 == day07b('test_input2.txt')


if __name__ == '__main__':
    test07a()
    print('Day 07a:', day07a('day07_input.txt'))
    # test07b()
    # print('Day 07b:', day07b('day07_input.txt'))
