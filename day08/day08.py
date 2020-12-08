

class Console:

    def __init__(self, input_path):
        self.instructions = []
        self.accumulator = 0
        self._read_program(input_path)

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
        while ind not in seen:
            seen.add(ind)
            action = self.instructions[ind]['action']
            value = self.instructions[ind]['value']
            if action == 'nop':
                ind += 1
            elif action == 'acc':
                self.accumulator += value
                # print(self.accumulator)
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
    rules_dict = get_rules_dict(input_path)
    return get_total_contents('shiny gold', rules_dict)


def test08b():
    assert 126 == day08b('test_input2.txt')


if __name__ == '__main__':
    test08a()
    print('Day 08a:', day08a('day08_input.txt'))
    # test08b()
    # print('Day 08b:', day08b('day08_input.txt'))
