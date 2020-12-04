

def day04a(input_path):
    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID) (optional)
    required = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'ecl',
        'pid',
    }
    present = set()
    total = 0
    with open(input_path) as file_obj:
        for line in file_obj:
            line = line.strip()
            if not line:
                absent = required - present
                valid = len(absent) == 0
                total += valid
                present = set()
                continue
            pairs = line.split()
            for pair in pairs:
                key, _, val = pair.partition(':')
                present.update([key])
        absent = required - present
        valid = len(absent) == 0
        total += valid
    return total


def test04a():
    assert 2 == day04a('test_input.txt')


if __name__ == '__main__':
    test04a()
    print('Day 04a:', day04a('day04_input.txt'))
