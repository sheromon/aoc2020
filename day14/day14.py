import numpy as np


def day14a(input_path):
    lines = [line.strip() for line in open(input_path)]
    memory = dict()
    mask = None
    powers = 2 ** np.arange(36)[::-1]
    for line in lines:
        if line.startswith('mask'):
            _, _, mask = line.partition('=')
            mask = np.array(list(mask.strip()))
            continue
        _, _, remainder = line.partition('[')
        address, _, remainder = remainder.partition(']')
        _, _, remainder = remainder.partition('=')
        val = int(remainder.strip())
        bits = np.array(int2bin(val))
        bits[mask != 'X'] = mask[mask != 'X']
        memory[address] = bits

    total = np.zeros(36, dtype=np.int32)
    for val in memory.values():
        total += val
    return np.sum(powers * total)


def int2bin(val):
    bits = []
    for power in range(35, -1, -1):
        bits.append(val // (2**power))
        val = val % (2**power)
    return bits


def test14a():
    assert 165 == day14a('test_input.txt')


def day14b(input_path):
    lines = [line.strip() for line in open(input_path)]
    memory = dict()
    mask = None
    powers = 2 ** np.arange(36)[::-1]
    for line in lines:
        if line.startswith('mask'):
            _, _, mask = line.partition('=')
            mask = np.array(list(mask.strip()))
            continue
        _, _, remainder = line.partition('[')
        address, _, remainder = remainder.partition(']')
        _, _, remainder = remainder.partition('=')
        val = int(remainder.strip())
        bits = np.array(int2bin(int(address)))
        bits[mask == '1'] = 1
        x_inds = np.where(mask == 'X')[0]
        all_bits = np.reshape(bits, (1, -1))
        for ind in x_inds:
            bits2 = np.copy(all_bits)
            current = all_bits[0, ind]
            bits2[:, ind] = not current
            all_bits = np.concatenate((all_bits, bits2), axis=0)
        addresses = np.sum(powers * all_bits, axis=1)
        for address in addresses:
            memory[address] = val
    total = 0
    for val in memory.values():
        total += val
    return total


def test14b():
    assert 208 == day14b('test_input2.txt')


if __name__ == '__main__':
    test14a()
    print('Day 14a:', day14a('day14_input.txt'))
    test14b()
    print('Day 14b:', day14b('day14_input.txt'))
