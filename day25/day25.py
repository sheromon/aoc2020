import numpy as np


def day25a(input_path):
    lines = [line.strip() for line in open(input_path)]
    subject = 7
    max_loop_size = 11  # chosen so that prev_remainder * subject ** loop won't overflow
    public = dict()
    loop_size = dict()
    for ind, line in enumerate(lines):
        public[ind] = int(line)
        loop_base = 0
        prev_remainder = 1
        while True:
            loop_guesses = np.arange(max_loop_size, dtype=np.uint64)
            results = prev_remainder * subject ** loop_guesses % 20201227
            loop_ind = np.argmax(results == public[ind])
            if loop_ind:
                break
            prev_remainder = results[-1]
            loop_base += (max_loop_size - 1)
        loop_size[ind] = loop_base + loop_ind
    key = transform(public[0], loop_size[1])
    return key


def transform(subject, loop_size):
    val = 1
    for _ in range(loop_size):
        val *= subject
        val = val % 20201227
    return val


def test25a():
    assert 14897079 == day25a('test_input.txt')


if __name__ == '__main__':
    test25a()
    print('Day 25a:', day25a('day25_input.txt'))
