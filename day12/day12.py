import numpy as np


def day12a(input_path):
    lines = [line.strip() for line in open(input_path)]

    ship = ShipA()
    for line in lines:
        letter, value = line[0], line[1:]
        ship.step(letter, int(value))
    return ship.distance


def test12a():
    assert 25 == day12a('test_input.txt')


class ShipA:

    def __init__(self):
        # starting position and angle
        self.position = np.array([0, 0])
        self.angle = 90

        # lookups
        self.angles = {
            'L': -1,
            'R': 1,
        }
        self.directions = {
            'N': [1, 0],
            'S': [-1, 0],
            'E': [0, 1],
            'W': [0, -1],
        }
        self.angle_to_dir = {
            0: 'N',
            90: 'E',
            180: 'S',
            270: 'W',
        }

    def step(self, letter, value):
        if letter == 'F':
            letter = self.angle_to_dir[self.angle]
        elif letter in self.angles:
            self.angle += int(value * self.angles[letter])
            self.angle =  self.angle % 360
        if letter in self.directions:
            self.position += value * np.array(self.directions[letter])

    @property
    def distance(self):
        return np.sum(np.abs(self.position))



def day12b(input_path):
    lines = [line.strip() for line in open(input_path)]

    ship = ShipB()
    for line in lines:
        letter, value = line[0], line[1:]
        ship.step(letter, int(value))
    return ship.distance


class ShipB(ShipA):

    def __init__(self):
        super().__init__()
        # initial waypoint
        self.waypoint = np.array([1, 10])

    def step(self, letter, value):
        if letter == 'F':
            self.position += value * self.waypoint
        elif letter in self.angles:
            angle = int(value * self.angles[letter]) % 360
            if angle == 90:
                self.waypoint = self.waypoint[::-1] * np.array([-1, 1])
            elif angle == 180:
                self.waypoint *= -1
            elif angle == 270:
                self.waypoint = self.waypoint[::-1] * np.array([1, -1])
        if letter in self.directions:
            self.waypoint += value * np.array(self.directions[letter])


def test12b():
    assert 286 == day12b('test_input.txt')


if __name__ == '__main__':
    test12a()
    print('Day 12a:', day12a('day12_input.txt'))
    test12b()
    print('Day 12b:', day12b('day12_input.txt'))
