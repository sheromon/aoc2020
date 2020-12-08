

class Console:

    def __init__(self, input_path):
        self.instructions = []
        self._read_program(input_path)
        self.accumulator = 0
        self.loop = False  # switches to True when revisiting an instruction

    def _read_program(self, input_path):
        lines = [line.strip() for line in open(input_path)]
        for line in lines:
            action, value = line.split(' ')
            self.instructions.append({
                'action': action,
                'value': int(value),
            })

    def run(self):
        seen = set()
        ind = 0
        while ind < len(self.instructions):
            if ind in seen:
                self.loop = True
                break
            seen.add(ind)
            action = self.instructions[ind]['action']
            value = self.instructions[ind]['value']
            if action == 'nop':
                ind += 1
            elif action == 'acc':
                self.accumulator += value
                ind += 1
            elif action == 'jmp':
                ind += value
            else:
                raise RuntimeError("Invalid action")

def day08a(input_path):
    console = Console(input_path)
    console.run()
    return console.accumulator


def test08a():
    assert 5 == day08a('test_input.txt')


def day08b(input_path):
    console = Console(input_path)
    jmp_inds = [ind for ind, inst in enumerate(console.instructions) if inst['action'] == 'jmp']
    for ind in jmp_inds:
        console = Console(input_path)
        console.instructions[ind]['action'] = 'nop'
        console.run()
        if not console.loop:
            return console.accumulator

    nop_inds = [ind for ind, inst in enumerate(console.instructions) if inst['action'] == 'nop']
    for ind in nop_inds:
        console = Console(input_path)
        console.instructions[ind]['action'] = 'jmp'
        console.run()
        if not console.loop:
            return console.accumulator
    print('No solution found')


def test08b():
    assert 8 == day08b('test_input.txt')


if __name__ == '__main__':
    test08a()
    print('Day 08a:', day08a('day08_input.txt'))
    test08b()
    print('Day 08b:', day08b('day08_input.txt'))
