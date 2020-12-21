from collections import defaultdict
import re
import time

import numpy as np


def day20a(input_path):
    """Return the product of the four corner tile IDs."""
    tile_dict = parse_input(input_path)
    borders = make_border_dict(tile_dict)
    shared_border_counts = get_shared_border_info(borders)[0]

    product = 1
    for tile_id, count in shared_border_counts.items():
        if count == 4:
            product *= tile_id
    return product


def parse_input(input_path):
    """Return a dictionary with tile IDs as keys and pixels as values."""
    lines = [line.strip() for line in open(input_path)]
    tile_dict = dict()
    tile_id = None
    tile_lines = []
    tile_pattern = re.compile('Tile (\d+):')
    for line in lines:
        if not line:
            continue
        header_match = tile_pattern.match(line)
        if header_match:
            if tile_id:
                tile_dict[tile_id] = np.array(tile_lines)
            tile_id = int(header_match.group(1))
            tile_lines = []
        else:
            tile_lines.append(list(line))
    tile_dict[tile_id] = np.array(tile_lines)
    return tile_dict


def make_border_dict(tile_dict):
    """Return a dictionary with unique borders as keys.

    For a given border, the value is a list of tuples (tile_id, orientation),
    where orientation is an integer in [0, 7] that defines the transformations
    applied to the pixels such that the top row is the border.
    """
    borders = defaultdict(list)
    for tile_id, tile in tile_dict.items():
        for n in range(8):
            pixels = reorient(tile, n)
            border = tuple(pixels[0, :])
            borders[border].append((tile_id, n))
    return borders


def get_shared_border_info(borders):
    """Return a dictionary that counts how many times each tile has a shared
    border and a dictionary of shared borders.

    The shared borders dictionary is a subset of the borders dictionary with
    only shared borders retained.

    Tile IDs in the counts dictionary with a value of 4 are corners because
    each corner tile has two shared borders. Each shared border counts once in
    one orientation and again when it is reversed, for a total of four matches.
    """
    total = 0
    counts = defaultdict(int)
    shared_borders = dict()
    for border, matches in borders.items():
        if len(matches) > 1:
            shared_borders[border] = matches
            for match in matches:
                tile_id = match[0]
                counts[tile_id] += 1
            total += 1
    return counts, shared_borders


def reorient(pixels, num):
    """Given a numpy array, return one of 8 transformed versions.

    :param pixels: numpy array
    :param num: int in [0, 7]
    :return: transformed copy of input array
    """
    def flip_rows(array):
        return array[::-1, :]

    def flip_cols(array):
        return array[:, ::-1]

    transforms = []
    for power in [2, 1, 0]:
        bit = num // 2**power
        num = num % 2**power
        transforms.append(bit)
    pixels = np.copy(pixels)
    if transforms[0]:
        pixels = flip_rows(pixels)
    if transforms[1]:
        pixels = flip_cols(pixels)
    if transforms[2]:
        pixels = pixels.T
    return pixels


def test20a():
    assert 20899048083289 == day20a('test_input.txt')


def day20b(input_path):
    t_start = time.time()
    tile_dict = parse_input(input_path)
    borders = make_border_dict(tile_dict)
    counts, shared_borders = get_shared_border_info(borders)
    image = construct_image(tile_dict, counts, shared_borders)
    print('Initial number of #s:', np.sum(image == '#'))

    monster_pattern = get_monster_pattern()
    monster_inds = np.where(monster_pattern == '#')

    shape = monster_pattern.shape
    min_matches = (monster_pattern == '#').sum()
    spaces = np.array(image.shape) - np.array(shape) + 1

    original_image = np.copy(image)
    for orientation in range(8):
        image = reorient(original_image, orientation)
        total_monsters = 0
        for row in range(spaces[0]):
            for col in range(spaces[1]):
                patch = image[row:row+shape[0], col:col+shape[1]]
                if np.sum(patch[monster_inds] == '#') == min_matches:
                    total_monsters += 1
                    patch[monster_inds] = 'O'
        if total_monsters:
            break
    print('Total monsters:', total_monsters)
    print('Final number of #s:', np.sum(image == '#'))
    print('Final number of Os:', np.sum(image == 'O'))
    t_stop = time.time()
    print(t_stop - t_start)
    return (image == '#').sum()


def get_monster_pattern():
    monster_pattern = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   ',
    ]
    return np.array([list(row) for row in monster_pattern])


def construct_image(tile_dict, counts, shared_borders):
    num_tiles = int(np.sqrt(len(tile_dict)))

    # find a corner tile id
    for tile_id, count in counts.items():
        if count == 4:
            break
    # find an orientation such that the bottom border and right border are
    # shared with other tiles
    bottom_border = None
    for orientation in range(8):
        pixels = reorient(tile_dict[tile_id], orientation)
        bottom_border = tuple(pixels[-1, :])
        right_border = tuple(pixels[:, -1])
        if (bottom_border in shared_borders) and (right_border in shared_borders):
            break

    row = []

    col = [pixels[1:-1, 1:-1]]

    for icol in range(num_tiles):

        finish_column(col, num_tiles, tile_dict, shared_borders, tile_id, bottom_border)
        row.append(np.vstack(col))
        if icol == num_tiles - 1:
            break

        # start the next column
        tile_info_list = shared_borders[right_border]
        for tile_info in tile_info_list:
            if tile_info[0] != tile_id:
                break
        tile_id, orientation = tile_info

        pixels = reorient(tile_dict[tile_id], orientation).T
        bottom_border = tuple(pixels[-1, :])
        right_border = tuple(pixels[:, -1])
        col = [pixels[1:-1, 1:-1]]

    image = np.hstack(row)
    return image


def finish_column(col, num_tiles, tile_dict, shared_borders, tile_id, bottom_border):
    for itile in range(num_tiles - 1):
        tile_info_list = shared_borders[bottom_border]
        for tile_info in tile_info_list:
            if tile_info[0] != tile_id:
                break
        tile_id, orientation = tile_info

        pixels = reorient(tile_dict[tile_id], orientation)
        bottom_border = tuple(pixels[-1, :])
        col.append(pixels[1:-1, 1:-1])



def test20b():
    assert 273 == day20b('test_input.txt')


if __name__ == '__main__':
    test20a()
    print('Day 20a:', day20a('day20_input.txt'))
    test20b()
    print('Day 20b:', day20b('day20_input.txt'))
