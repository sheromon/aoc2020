import numpy as np
import matplotlib.pyplot as plt


def day05a(input_path):
    seat_codes = [line.strip() for line in open(input_path)]
    max_seat_id = 0
    for seat_code in seat_codes:
        row, col = calc_row_col(seat_code)
        seat_id = calc_seat_id(row, col)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id


def calc_row_col(directions):
    num_rows = 128
    rows = list(range(num_rows))
    for char in directions[:7]:
        if char == 'F':
            rows = rows[:int(num_rows/2)]
        elif char == 'B':
            rows = rows[int(num_rows/2):]
        else:
            raise RuntimeError("Expected 'F' or 'B'")
        num_rows = len(rows)

    num_cols = 8
    cols = list(range(num_cols))
    for char in directions[7:]:
        if char == 'L':
            cols = cols[:int(num_cols/2)]
        elif char == 'R':
            cols = cols[int(num_cols/2):]
        else:
            raise RuntimeError("Expected 'L' or 'R'")
        num_cols = len(cols)

    return rows[0], cols[0]


def calc_seat_id(row, col):
    return row * 8 + col


def test05a():
    assert 820 == day05a('test_input.txt')


def day05b(input_path):
    seat_codes = [line.strip() for line in open(input_path)]
    seating = np.zeros([128, 8], dtype=np.uint8)
    for seat_code in seat_codes:
        row, col = calc_row_col(seat_code)
        seating[row, col] = 1

    # I used the plot at first to get the row and column
    # plt.figure()
    # plt.imshow(seating)
    # plt.show()

    empty_inds = np.where(seating == 0)
    row_deltas = np.diff(empty_inds[0])
    my_seat_ind = np.where(row_deltas > 1)[0][1]
    my_row = empty_inds[0][my_seat_ind]
    my_col = empty_inds[1][my_seat_ind]
    return calc_seat_id(my_row, my_col)


if __name__ == '__main__':
    test05a()
    print('Day 05a:', day05a('day05_input.txt'))
    print('Day 05b:', day05b('day05_input.txt'))
