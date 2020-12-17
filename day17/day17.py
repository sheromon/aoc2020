import numpy as np


ACTIVE = 1
INACTIVE = 0


def day17a(input_path):
    num_cycles = 6
    dimension = Dimension(input_path)
    for step in range(num_cycles):
        dimension.step()
        print('Step:', step)
        print(np.transpose(dimension.state[5:15, 5:15, 9:12], (2, 0, 1)))
    return dimension.total


def test17a():
    assert 112 == day17a('test_input.txt')


class Dimension:

    def __init__(self, input_path):
        init_size = 20
        self.state = np.zeros(3 * (init_size,))
        lines = np.array([list(line.strip()) for line in open(input_path)])
        lines[lines == '#'] = 1
        lines[lines == '.'] = 0
        start_ind = int(np.ceil(init_size / 2 - len(lines) / 2))
        self.state[start_ind:start_ind + len(lines),
                   start_ind:start_ind + len(lines),
                   int(init_size / 2)] = np.array(lines)
        self.deltas = np.stack(np.meshgrid((-1, 0, 1), (-1, 0, 1), (-1, 0, 1)))
        self.deltas = np.reshape(np.transpose(self.deltas), (27, 3))
        all_zeros = np.all(self.deltas == 0, axis=1)
        self.deltas = self.deltas[~all_zeros, :]

    @property
    def total(self):
        return np.sum(self.state == ACTIVE)

    def step(self):
        next_state = np.copy(self.state)
        n_rows, n_cols, n_slices = self.state.shape
        for row in range(n_rows):
            for col in range(n_cols):
                for slc in range(n_slices):
                    total = self.count_occupied(row, col, slc)
                    if (self.state[row, col, slc] == INACTIVE) and (total == 3):
                        next_state[row, col, slc] = ACTIVE
                    elif (self.state[row, col, slc] == ACTIVE) and (total in [2, 3]):
                        next_state[row, col, slc] = ACTIVE
                    else:
                        next_state[row, col, slc] = INACTIVE
        self.state = next_state

    def count_occupied(self, row, col, slc):
        n_rows, n_cols, n_slices = self.state.shape
        total = 0
        for delta in self.deltas:
            next_row, next_col, next_slc = row + delta[0], col + delta[1], slc + delta[2]
            val = '.'
            if (next_row < 0) or (next_col < 0) or (next_row >= n_rows) \
                or (next_col >= n_cols) or (next_slc < 0) or (next_slc >= n_slices):
                continue
            val = self.state[next_row, next_col, next_slc]
            total += (val == ACTIVE)
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
