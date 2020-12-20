import re


def day19a(input_path):
    rules, input_strs = parse_input(input_path)
    total_valid = 0
    for input_str in input_strs:
        total_valid += check_match(input_str, rules, rule_num=0)
    return total_valid


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


def check_match(input_str, rules, rule_num, max_times=1):
    pattern = '^' + build_pattern(rules, rule_num, max_times) + '$'
    pattern = re.compile(pattern)
    result = pattern.match(input_str)
    return result is not None


def build_pattern(rules, rule_num, max_times=1):
    if isinstance(rules[rule_num], str):
        return rules[rule_num]

    # updated rule 8 simplifies to one or more occurrences of rule 42
    if rules[rule_num] == [[42], [42, 8]]:
        pattern = '(?:{})+'.format(
            build_pattern(rules, 42, max_times),
        )
        return pattern

    # updated rule 11 simplifies to one or more occurrences of rule 42 followed
    # by the same number of occurrences of rule 31
    if rules[rule_num] == [[42, 31], [42, 11, 31]]:
        options = []
        # I don't like this, but I couldn't figure out how to enforce that
        # the first subgroup and the second subgroup had to repeat the same
        # number of times in a different way.
        for times in range(1, max_times):
            options.append('((?:{}){{{times}}}(?:{}){{{times}}})'.format(
                build_pattern(rules, 42, max_times),
                build_pattern(rules, 31, max_times),
                times=times,
            ))
            pattern = '(?:{})'.format('|'.join(options))
        return pattern

    or_patterns = []
    for rule_list in rules[rule_num]:
        pattern = ''
        for next_rule in rule_list:
            pattern += build_pattern(rules, next_rule, max_times)
        or_patterns.append(pattern)
    return '(?:{})'.format('|'.join(or_patterns))


def test19a():
    rules, input_strs = parse_input('test_input.txt')
    expected_results = [True, False, True, False, False]
    for input_str, expected in zip(input_strs, expected_results):
        assert expected == check_match(input_str, rules, 0)
    assert 2 == day19a('test_input.txt')


def day19b(input_path):
    rules, input_strs = parse_input(input_path)
    # update rules
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    total_valid = 0
    for input_str in input_strs:
        valid = check_match(input_str, rules, rule_num=0, max_times=20)
        total_valid += valid
    return total_valid


def test19b():
    assert 3 == day19a('test_input2.txt')
    assert 12 == day19b('test_input2.txt')


if __name__ == '__main__':
    test19a()
    print('Day 19a:', day19a('day19_input.txt'))
    test19b()
    print('Day 19b:', day19b('day19_input.txt'))
