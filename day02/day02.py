

def day02a(input_path):
    valid_count = 0
    with open(input_path) as file_obj:
        for line in file_obj:
            low, _, remainder = line.partition('-')
            low = int(low)
            high, _, remainder = remainder.partition(' ')
            high = int(high)
            letter, _, remainder = remainder.partition(':')
            password = list(remainder.strip())
            counts = sum([char == letter for char in password])
            if low <= counts <= high:
                valid_count += 1
    return valid_count


def test02a():
    assert 2 == day02a('test_input.txt')


def day02b(input_path):
    valid_count = 0
    with open(input_path) as file_obj:
        for line in file_obj:
            one, _, remainder = line.partition('-')
            one = int(one) - 1
            two, _, remainder = remainder.partition(' ')
            two = int(two) - 1
            letter, _, remainder = remainder.partition(':')
            password = list(remainder.strip())
            condition1 = password[one] == letter
            condition2 = password[two] == letter
            if condition1 + condition2 == 1:
                valid_count += 1
    return valid_count


def test02b():
    assert 1 == day02b('test_input.txt')


if __name__ == '__main__':
    test02a()
    print('Day 02a:', day02a('day02_input.txt'))
    test02b()
    print('Day 02b:', day02b('day02_input.txt'))
