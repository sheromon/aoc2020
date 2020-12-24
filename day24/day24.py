from collections import defaultdict


OPPOSITES = {
    'e': (['w'], ['nw', 'sw']),
    'w': (['e'], ['ne', 'se']),
    'ne': (['sw'], ['w', 'se']),
    'sw': (['ne'], ['nw', 'e']),
    'se': (['nw'], ['ne', 'w']),
    'nw': (['se'], ['e', 'sw']),
}
ALL_DIRS = list(OPPOSITES.keys())
REDUCTIONS = {
    ('nw', 'sw'): 'w',
    ('ne', 'se'): 'e',
    ('w', 'se'): 'sw',
    ('nw', 'e'): 'ne',
    ('ne', 'w'): 'nw',
    ('e', 'sw'): 'se',
}


def day24a(input_path):
    lines = [line.strip() for line in open(input_path)]
    tile_defs = parse_lines(lines)
    tile_counts = defaultdict(int)
    for tile_def in tile_defs:
        tile_def.simplify()
        tile_counts[tile_def.counts] += 1
    num_black = 0
    count_counts = defaultdict(int)
    for tile, count in tile_counts.items():
        if count % 2:
            num_black += 1
        count_counts[count] += 1
    print(count_counts)
    return num_black


def parse_lines(lines):
    tile_defs = []
    for line in lines:
        ind = 0
        tile_def = TileDef()
        while ind < len(line):
            if line[ind] in ['n', 's']:
                dir_len = 2
            else:
                dir_len = 1
            tile_def.dirs[line[ind:ind+dir_len]] += 1
            ind += dir_len
        tile_defs.append(tile_def)
    return tile_defs


def test24a():
    assert 10 == day24a('test_input.txt')


class TileDef:

    def __init__(self):
        # can't use defaultdict here, otherwise dict size will change when any
        # count drops to zero
        self.dirs = {d: 0 for d in ALL_DIRS}

    def __str__(self):
        return str(self.dirs)

    def simplify(self):
        for key in self.dirs.keys():
            opp_lists = OPPOSITES[key]
            for opp_list in opp_lists:
                min_counts = min([self.dirs[key]] + [self.dirs[opp] for opp in opp_list])
                if min_counts:
                    self.dirs[key] -= min_counts
                    for opp in opp_list:
                        self.dirs[opp] -= min_counts
        for key, reduced_dir in REDUCTIONS.items():
            min_counts = min([self.dirs[d] for d in key])
            if min_counts:
                self.dirs[reduced_dir] += min_counts
                for d in key:
                    self.dirs[d] -= min_counts

    @property
    def counts(self):
        return tuple([self.dirs[key] for key in ALL_DIRS])



def day24b(input_path):
    pass


def test24b():
    assert 2208 == day24b('test_input.txt')


if __name__ == '__main__':
    test24a()
    print('Day 24a:', day24a('day24_input.txt'))
    # test24b()
    # print('Day 24b:', day24b('day24_input.txt'))
