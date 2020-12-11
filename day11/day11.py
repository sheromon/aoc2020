import numpy as np


def day11a(input_path):
    seating = Seating(input_path)
    prev_total = 0
    delta = 1
    while delta:
        seating.step()
        delta = seating.total - prev_total
        prev_total = seating.total
    return seating.total


def test11a():
    assert 37 == day11a('test_input.txt')


class Seating:

    def __init__(self, input_path):
        self.max_neighbors = 4
        lines = [list(line.strip()) for line in open(input_path)]
        self.state = np.array(lines)
        self.deltas = [  # the eight directions
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]

    @property
    def total(self):
        return np.sum(self.state == '#')

    def step(self):
        next_state = np.copy(self.state)
        n_rows, n_cols = self.state.shape
        for row in range(n_rows):
            for col in range(n_cols):
                total = self.count_occupied(row, col)
                if (self.state[row, col] == 'L') and (total == 0):
                    next_state[row, col] = '#'
                elif (self.state[row, col] == '#') and (total >= self.max_neighbors):
                    next_state[row, col] = 'L'
        self.state = next_state

    def count_occupied(self, row, col):
        n_rows, n_cols = self.state.shape
        total = 0
        for delta in self.deltas:
            next_row, next_col = row + delta[0], col + delta[1]
            val = '.'
            if (next_row < 0) or (next_col < 0) or (next_row >= n_rows) \
                or (next_col >= n_cols):
                continue
            val = self.state[next_row, next_col]
            total += (val == '#')
        return total


class Seating2(Seating):

    def __init__(self, input_path):
        super().__init__(input_path)
        self.max_neighbors = 5

    def count_occupied(self, row, col):
        n_rows, n_cols = self.state.shape
        total = 0
        for delta in self.deltas:
            done = False
            val = '.'
            next_row, next_col = row, col
            while not done:
                next_row += delta[0]
                next_col += delta[1]
                if (next_row < 0) or (next_col < 0) or (next_row >= n_rows) or (next_col >= n_cols):
                    break
                val = self.state[next_row, next_col]
                done = val != '.'
            total += (val == '#')
        return total



def day11b(input_path):
    seating = Seating2(input_path)
    prev_total = 0
    delta = 1
    while delta:
        seating.step()
        delta = seating.total - prev_total
        prev_total = seating.total
    return seating.total


def test11b():
    assert 26 == day11b('test_input.txt')


if __name__ == '__main__':
    test11a()
    print('Day 11a:', day11a('day11_input.txt'))
    test11b()
    print('Day 11b:', day11b('day11_input.txt'))
