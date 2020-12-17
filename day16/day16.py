import numpy as np


def day16a(input_path):
    rules, your_ticket, nearby_tickets = parse_input(input_path)
    invalid_vals = []
    for ticket_vals in nearby_tickets:
        for val in ticket_vals:
            if not is_potentially_valid(val, rules):
                invalid_vals.append(val)
    return sum(invalid_vals)


def parse_input(input_path):
    lines = [line.strip() for line in open(input_path)]
    rules = dict()

    your_ind = lines.index('your ticket:')
    rule_lines = lines[:your_ind - 1]
    your_line = lines[your_ind + 1]
    near_ind = lines.index('nearby tickets:')
    nearby_lines = lines[near_ind + 1:]

    for line in rule_lines:
        if not line:
            continue
        field, _, ranges = line.partition(':')
        ranges = ranges.split(' or ')
        bounds = []
        for range_str in ranges:
            lo, hi = range_str.split('-')
            bounds.append((int(lo), int(hi)))
        rules[field] = bounds

    your_ticket = [int(val) for val in your_line.split(',')]

    nearby_tickets = []
    for line in nearby_lines:
        vals = [int(val) for val in line.split(',')]
        nearby_tickets.append(vals)

    return rules, your_ticket, nearby_tickets


def is_potentially_valid(val, rules):
    for rule in rules.values():
        for bounds in rule:
            if bounds[0] <= val <= bounds[1]:
                return True
    return False


def test16a():
    assert 71 == day16a('test_input.txt')


def day16b(input_path):
    rules, your_ticket, nearby_tickets = parse_input(input_path)
    nearby_tickets = remove_invalid_tickets(rules, nearby_tickets)
    nearby_tickets = np.array(nearby_tickets)

    fields = sorted(list(rules.keys()))
    valid = np.zeros((len(fields), len(fields)), dtype=np.bool)
    for irow, field in enumerate(fields):
        rule = rules[field]
        valid_this_rule = np.zeros_like(nearby_tickets).astype(np.bool)
        for bounds in rule:
            valid_this_rule |= (bounds[0] <= nearby_tickets) & (nearby_tickets <= bounds[1])
        valid[irow, :] |= np.all(valid_this_rule, axis=0)

    my_ticket = dict()
    while len(my_ticket) < len(fields):
        sum_valid = np.sum(valid, axis=1)
        field_ind = np.argmin(sum_valid)
        col_ind = np.argmax(valid[field_ind, :])
        my_ticket[fields[field_ind]] = your_ticket[col_ind]
        # once this column is matched, no other field may match it
        valid[:, col_ind] = False
        # set the whole row to True so that it won't come up as the one with the
        # lowest number of valid values
        valid[field_ind, :] = True

    product = 1
    for field in fields:
        if field.startswith('departure'):
            product *= my_ticket[field]
    return product


def remove_invalid_tickets(rules, nearby_tickets):
    valid_tickets = []
    for ticket_vals in nearby_tickets:
        valid = True
        for val in ticket_vals:
            if not is_potentially_valid(val, rules):
                valid = False
                break
        if valid:
            valid_tickets.append(ticket_vals)
    return valid_tickets


if __name__ == '__main__':
    test16a()
    print('Day 16a:', day16a('day16_input.txt'))
    # today's test for the second part was to print the ticket for the example
    print('Day 16b:', day16b('day16_input.txt'))
