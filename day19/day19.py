import re


def day19a(input_path):
    rules, input_strs = parse_input(input_path)
    valid_list = []
    for input_str in input_strs:
        valid = check_match(input_str, rules, rule_num=0)
        valid_list.append(valid)
    return sum(valid_list)


def parse_input(input_path):
    lines = [line.strip() for line in open(input_path)]
    rules = dict()
    for iline, line in enumerate(lines):
        if not line:
            break
        rule_num, _, remain = line.partition(':')
        if remain.endswith('"'):
            rule_contents = remain[-2]
        else:
            conditions = remain.split('|')
            rule_contents = []
            for cond in conditions:
                int_list = [int(val) for val in cond.split()]
                rule_contents.append(int_list)
        rules[int(rule_num)] = rule_contents
    input_strs = lines[iline+1:]
    return rules, input_strs


def check_match(input_str, rules, rule_num):
    pattern = '^' + build_pattern(rules, rule_num) + '$'
    # print(pattern)
    pattern = re.compile(pattern)
    return pattern.match(input_str) is not None


def build_pattern(rules, rule_num):
    if isinstance(rules[rule_num], str):
        return rules[rule_num]

    or_patterns = []
    for rule_list in rules[rule_num]:
        pattern = ''
        for next_rule in rule_list:
            pattern += build_pattern(rules, next_rule)
        or_patterns.append(pattern)
    return '({})'.format('|'.join(or_patterns))


def test19a():
    rules, input_strs = parse_input('test_input.txt')
    expected_results = [True, False, True, False, False]
    for input_str, expected in zip(input_strs, expected_results):
        assert expected == check_match(input_str, rules, 0)
    assert 2 == day19a('test_input.txt')


def day19b(input_path):
    pass


def test19b():
    assert 286 == day19b('test_input.txt')


if __name__ == '__main__':
    test19a()
    print('Day 19a:', day19a('day19_input.txt'))
    # test19b()
    # print('Day 19b:', day19b('day19_input.txt'))
