import re


def day04a(input_path, validate_fields=False):
    passports = bulk_to_passports(input_path)

    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID) (optional)
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    total = 0
    for passport in passports:
        absent = required - set(passport.keys())
        valid = not absent and (not validate_fields or fields_valid(passport))
        total += valid
    return total


def bulk_to_passports(input_path):
    passports = []
    pairs = {}
    with open(input_path) as file_obj:
        for line in file_obj:
            line = line.strip()
            if not line:
                passports.append(pairs)
                pairs = {}
                continue
            pairs_list = line.split()
            for pair in pairs_list:
                key, _, val = pair.partition(':')
                pairs[key] = val
    passports.append(pairs)
    print('Total passports:', len(passports))
    return passports


def test04a():
    assert 2 == day04a('test_input.txt')


def day04b(input_path):
    return day04a(input_path, validate_fields=True)


def fields_valid(passport):
    four_digits = re.compile('^[0-9]{4}$')
    for key, val in passport.items():
        if key == 'byr':
            if len(val) != 4:
                return False
            if not four_digits.match(val):
                return False
            val = int(val)
            if (val < 1920) or (val > 2002):
                return False
        elif key == 'iyr':
            if len(val) != 4:
                return False
            if not four_digits.match(val):
                return False
            val = int(val)
            if (val < 2010) or (val > 2020):
                return False
        elif key == 'eyr':
            if len(val) != 4:
                return False
            if not four_digits.match(val):
                return False
            val = int(val)
            if (val < 2020) or (val > 2030):
                return False
        elif key == 'hgt':
            if len(val) <= 2:
                return False
            val, units = val[:-2], val[-2:]
            if units not in ('cm', 'in'):
                return False
            try:
                val = int(val)
            except:
                return False
            if units == 'cm':
                if val < 150 or val > 193:
                    return False
            elif val < 59 or val > 76:
                return False
        elif key == 'hcl':
            pattern = re.compile('#[0-9a-f]{6}')
            if not pattern.match(val):
                return False 
        elif key == 'ecl':
            valid_vals = (
                'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth',
            )
            if val not in valid_vals:
                return False
        elif key == 'pid':
            pattern = re.compile('^[0-9]{9}$')
            if not pattern.match(val):
                return False 
    return True


def test04b():
    assert fields_valid({'byr': '2002'}) == True
    assert fields_valid({'byr': '2003'}) == False
    assert fields_valid({'hgt': '60in'}) == True
    assert fields_valid({'hgt': '190cm'}) == True
    assert fields_valid({'hgt': '190in'}) == False
    assert fields_valid({'hgt': '190'}) == False
    assert fields_valid({'hcl': '#123abc'}) == True
    assert fields_valid({'hcl': '#123abz'}) == False
    assert fields_valid({'hcl': '123abc'}) == False
    assert fields_valid({'ecl': 'brn'}) == True
    assert fields_valid({'ecl': 'wat'}) == False
    assert fields_valid({'pid': '000000001'}) == True
    assert fields_valid({'pid': '0123456789'}) == False


if __name__ == '__main__':
    test04a()
    print('Day 04a:', day04a('day04_input.txt'))
    test04b()
    print('Day 04b:', day04b('day04_input.txt'))
