

def day07a(input_path):
    rules_dict = get_rules_dict(input_path)
    holders = []
    get_holders('shiny gold', rules_dict, holders)
    return len(holders)


def get_rules_dict(input_path):
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
    return rules_dict


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
    rules_dict = get_rules_dict(input_path)
    return get_total_contents('shiny gold', rules_dict)


def get_total_contents(target, rules_dict):
    contents = rules_dict[target]
    total_contents = 0
    for color, quantity in contents.items():
        total_contents += quantity * (1 + get_total_contents(color, rules_dict))
    return total_contents


def test07b():
    assert 126 == day07b('test_input2.txt')


if __name__ == '__main__':
    test07a()
    print('Day 07a:', day07a('day07_input.txt'))
    test07b()
    print('Day 07b:', day07b('day07_input.txt'))
