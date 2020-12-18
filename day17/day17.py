from collections import defaultdict
import copy

import numpy as np


ACTIVE = 1
INACTIVE = 0


def day17a(input_path):
    num_cycles = 6
    dimension = Dimension(input_path)
    print(dimension.total)
    for step in range(num_cycles):
        dimension.step()
        print('Step:', step)
        print(dimension.total)
    return dimension.total


def test17a():
    assert 112 == day17a('test_input.txt')


class Dimension:

    def __init__(self, input_path):
        self.state = defaultdict(int)
        lines = np.array([list(line.strip()) for line in open(input_path)])
        lines[lines == '#'] = 1
        lines[lines == '.'] = 0
        init_slice = 0
        x, y = np.meshgrid(np.arange(lines.shape[0]), np.arange(lines.shape[1]))
        x = x.flatten().tolist()
        y = y.flatten().tolist()
        for ix, iy in zip(x, y):
            self.state[(ix, iy) + (0,)] = int(lines[ix, iy])

        meshgrid_input = 3 * ((-1, 0, 1),)
        self.deltas = np.stack(np.meshgrid(*meshgrid_input))
        self.deltas = np.reshape(np.transpose(self.deltas), (-1, 3))
        all_zeros = np.all(self.deltas == 0, axis=1)
        self.deltas = self.deltas[~all_zeros, :]

    @property
    def total(self):
        return sum(self.state.values())

    def step(self):
        next_state = copy.deepcopy(self.state)
        current_keys = list(self.state.keys())
        mins = np.array(current_keys).min(axis=0) - 1
        maxs = np.array(current_keys).max(axis=0) + 1
        meshgrid_input = [np.arange(bounds[0], bounds[1]+1) for bounds in zip(mins, maxs)]
        inds_to_check = np.stack(np.meshgrid(*meshgrid_input))
        inds_to_check = np.reshape(np.transpose(inds_to_check), (-1, 3)).tolist()
        for key in inds_to_check:
            key = tuple(key)
            total = self.count_occupied_neighbors(key)
            if (self.state[key] == INACTIVE) and (total == 3):
                next_state[key] = ACTIVE
            elif (self.state[key] == ACTIVE) and (total in [2, 3]):
                next_state[key] = ACTIVE
            else:
                next_state[key] = INACTIVE
        self.state = next_state

    def count_occupied_neighbors(self, key):
        total = 0
        for delta in self.deltas:
            neighbor = tuple(np.array(key) + np.array(delta))
            total += (self.state[neighbor] == ACTIVE)
        return total


def day17b(input_path):
    pass


def test17b():
    assert 848 == day17b('test_input.txt')


if __name__ == '__main__':
    test17a()
    print('Day 17a:', day17a('day17_input.txt'))
    # test17b()
    # print('Day 17b:', day17b('day17_input.txt'))
