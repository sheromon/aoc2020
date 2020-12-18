import re


def day18a(input_path):
    lines = [line.strip() for line in open(input_path)]
    return sum([process(line) for line in lines])


def process(line):
    parens = re.compile('\([^()]+\)')
    result = parens.search(line)
    while result:
        inner_expr = line[result.start()+1:result.end()-1]
        inner_val = process(inner_expr)
        line = line[:result.start()] + str(inner_val) + line[result.end():]
        result = parens.search(line)

    pair = re.compile('\d+\s*[*+]\s*\d+')
    result = pair.match(line)
    while result:
        val = eval(result.group(0))
        line = str(val) + line[result.end(0):]
        result = pair.match(line)
    return int(line)


def test18a():
    assert 26 == process('2 * 3 + (4 * 5)')
    assert 437 == process('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    assert 12240 == process('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    assert 13632 == process('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')


def day18b(input_path):
    lines = [line.strip() for line in open(input_path)]
    return sum([process2(line) for line in lines])


def process2(line):
    parens = re.compile('\([^()]+\)')
    result = parens.search(line)
    while result:
        inner_expr = line[result.start()+1:result.end()-1]
        inner_val = process2(inner_expr)
        line = line[:result.start()] + str(inner_val) + line[result.end():]
        result = parens.search(line)

    pair = re.compile('\d+\s*[+]\s*\d+')
    result = pair.search(line)
    while result:
        val = eval(result.group(0))
        line = line[:result.start()] + str(val) + line[result.end(0):]
        result = pair.search(line)

    pair = re.compile('\d+\s*[*]\s*\d+')
    result = pair.match(line)
    while result:
        val = eval(result.group(0))
        line = str(val) + line[result.end(0):]
        result = pair.match(line)

    return int(line)


def test18b():
    assert 51 == process2('1 + (2 * 3) + (4 * (5 + 6))')
    assert 46 == process2('2 * 3 + (4 * 5)')
    assert 1445 == process2('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    assert 669060 == process2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    assert 23340 == process2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')


if __name__ == '__main__':
    test18a()
    print('Day 18a:', day18a('day18_input.txt'))
    test18b()
    print('Day 18b:', day18b('day18_input.txt'))
