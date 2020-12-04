

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
    passports = []
    pairs = []
    with open(input_path) as file_obj:
        for line in file_obj:
            line = line.strip()
            if not line:
                passports.append(pairs)
                pairs = []
                continue
            pairs += line.split()
        passports.append(pairs)
    print('Total passports:', len(passports))

    total = 0
    for passport in passports:
        present = []
        for pair in passport:
            key, _, val = pair.partition(':')
            present.append(key)
        absent = required - set(present)
        valid = len(absent) == 0
        total += valid
        print(valid, 'total:', total, '# present:', len(present), 'absent:', absent)
    return total


def test04a():
    assert 2 == day04a('test_input.txt')


if __name__ == '__main__':
    test04a()
    print('Day 04a:', day04a('day04_input.txt'))
