import re
import numpy as np


def day21a(input_path):
    ingreds_list, allergen_map = parse_input(input_path)
    potentially_bad_ingreds = set()
    for val in allergen_map.values():
        potentially_bad_ingreds.update(val)
    ok_ingreds = set(ingreds_list) - potentially_bad_ingreds
    return sum([item in ok_ingreds for item in ingreds_list])


def parse_input(input_path):
    lines = [line.strip() for line in open(input_path)]
    ingreds_list = list()
    allergen_map = dict()
    for line in lines:
        sections = line.split('(')
        these_ingreds = sections[0].split()
        ingreds_list += these_ingreds
        if len(sections) > 1:
            allergens = sections[1][len('contains'):-1].split(',')
            for allergen in allergens:
                allergen = allergen.strip()
                if allergen not in allergen_map:
                    allergen_map[allergen] = set(these_ingreds)
                else:
                    allergen_map[allergen] &= set(these_ingreds)
    return ingreds_list, allergen_map


def test21a():
    assert 5 == day21a('test_input.txt')


def day21b(input_path):
    _, allergen_map = parse_input(input_path)
    sorted_allergens = sorted(list(allergen_map.keys()))
    # need to get the allergen map down to a one-to-one mapping
    counts = [len(allergen_map[allergen]) for allergen in sorted_allergens]
    while sum(counts) > len(counts):
        for val, allergen in zip(counts, sorted_allergens):
            known_bad_set = allergen_map[allergen]
            # if we have a candidate ingredient list of size 1 for an allergen,
            # we know that allergen is in that ingredient and can remove that
            # ingredient from the set of suspected ingredients for all others.
            if val == 1:
                for key, ingreds in allergen_map.items():
                    if key == allergen:
                        continue
                    allergen_map[key] -= known_bad_set
        counts = [len(allergen_map[allergen]) for allergen in sorted_allergens]
    dangerous_ingreds = [allergen_map[allergen].pop() for allergen in sorted_allergens]
    return ','.join(dangerous_ingreds)


def test21b():
    assert 'mxmxvkd,sqjhc,fvjkl' == day21b('test_input.txt')


if __name__ == '__main__':
    test21a()
    print('Day 21a:', day21a('day21_input.txt'))
    test21b()
    print('Day 21b:', day21b('day21_input.txt'))
