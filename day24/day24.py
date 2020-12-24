from collections import defaultdict
import copy
import numpy as np


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
# this is the same as above, just using direction indices instead of strings
TUPLE_REDUCTIONS = {
    (5, 3): 1,
    (2, 4): 0,
    (1, 4): 3,
    (5, 0): 2,
    (2, 1): 5,
    (0, 3): 4,
}


def day24a(input_path):
    lines = [line.strip() for line in open(input_path)]
    tile_defs = parse_lines(lines)
    tile_counts = defaultdict(int)
    for tile_def in tile_defs:
        tile_def.simplify()
        tile_counts[tile_def.counts] += 1
    num_black = 0
    for tile, count in tile_counts.items():
        if count % 2:
            num_black += 1
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
    lines = [line.strip() for line in open(input_path)]
    tile_defs = parse_lines(lines)
    tile_counts = defaultdict(int)
    for tile_def in tile_defs:
        tile_def.simplify()
        tile_counts[tile_def.counts] += 1

    # convert dict of tile counts into status (1: black, 0: white)
    floor_state = tile_counts
    current_black = set()
    current_white = set()
    for tile, count in floor_state.items():
        floor_state[tile] = count % 2
        if count % 2:
            current_black.add(tile)
    current_white = set([tile_def.counts for tile_def in tile_defs]) - current_black

    for day in range(100):

        current_white = set()
        for tile in list(current_black):
            neighbors = get_neighbors(tile)
            for neighbor in neighbors:
                if neighbor not in current_black:
                    current_white.add(neighbor)

        next_black = copy.copy(current_black)
        next_white = copy.copy(current_white)

        for tile in list(current_black):
            neighbors = get_neighbors(tile)
            total_adj_black = 0
            for neighbor in neighbors:
                total_adj_black += (neighbor in current_black)
            if (total_adj_black == 0) or (total_adj_black > 2):
                next_white.add(tile)
                next_black.remove(tile)

        for tile in list(current_white):
            neighbors = get_neighbors(tile)
            total_adj_black = 0
            for neighbor in neighbors:
                total_adj_black += (neighbor in current_black)
            if total_adj_black == 2:
                next_black.add(tile)
                next_white.remove(tile)

        current_black = next_black
        current_white = next_white
        print('Day {}: {}'.format(day + 1, len(current_black)))

    return len(current_black)


def get_neighbors(tile):
    eye = np.eye(6, dtype=np.int32)
    neighbors = np.array(tile) + eye
    simplified = [simplify_tuple(n) for n in neighbors.tolist()]
    return simplified


def simplify_tuple(tile):
    tile = np.array(tile)
    # cancel out opposites
    for ind in range(0, 6, 2):
        min_count = np.min(tile[ind:ind+2])
        tile[ind:ind+2] -= min_count
    for ind_pair, reduced_ind in TUPLE_REDUCTIONS.items():
        min_counts = min(tile[ind_pair[0]], tile[ind_pair[1]])
        if min_counts:
            tile[reduced_ind] += min_counts
            tile[ind_pair[0]] -= min_counts
            tile[ind_pair[1]] -= min_counts
    return tuple(tile)


def test24b():
    tile = np.zeros(6, dtype=np.int32)
    tile[:2] = 1
    tile = tuple(tile)
    assert (0, 0, 0, 0, 0, 0) == simplify_tuple(tile)

    tile = np.zeros(6, dtype=np.int32)
    tile[1:3] = 1
    tile = tuple(tile)
    assert (0, 0, 0, 0, 0, 1) == simplify_tuple(tile)

    assert 2208 == day24b('test_input.txt')


if __name__ == '__main__':
    test24a()
    print('Day 24a:', day24a('day24_input.txt'))
    test24b()
    print('Day 24b:', day24b('day24_input.txt'))
