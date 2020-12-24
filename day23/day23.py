import logging

logging.basicConfig(level=logging.INFO)


def day23a(input_str, num_moves=100):
    cups = [int(val) for val in list(input_str)]

    cup_links = make_cup_links(cups)
    run_game(cup_links, num_moves, cups[0])

    # get all of the cups after 1, and join them into a string
    cup = 1
    cups = []
    for _ in range(len(cup_links) - 1):
        next_cup = cup_links[cup]
        cups.append(next_cup)
        cup = next_cup
    final_ordering = [str(cup) for cup in cups]
    return ''.join(final_ordering)


def make_cup_links(cups):
    """Reformat list of cups into a dict with cup pointing to next cups."""
    cup_links = dict()
    prev_cup = cups[0]
    for cup in cups[1:]:
        cup_links[prev_cup] = cup
        prev_cup = cup
    cup_links[prev_cup] = cups[0]
    return cup_links


def run_game(cup_links, num_moves, current):
    """This should be self-explanatory."""
    num_cups = len(cup_links)
    for move in range(num_moves):
        # whoops, can't have this enabled when doing part 2, even if log level
        # is higher than debug because it still runs the function
        # logging.debug('cups: %s', get_cup_list(cup_links, current))
        next_three = []
        cup = current
        for _ in range(3):
            next_cup = cup_links[cup]
            next_three.append(next_cup)
            cup = next_cup
        logging.debug('next three: %s', next_three)
        dest_cup = (current - 2) % num_cups + 1
        while dest_cup in next_three:
            dest_cup -= 1
            dest_cup = (dest_cup - 1) % num_cups + 1
        logging.debug('destination: %s', dest_cup)
        logging.debug('')
        cup_links[current] = cup_links[next_cup]
        cup_links[next_three[-1]] = cup_links[dest_cup]
        cup_links[dest_cup] = next_three[0]
        current = cup_links[current]
        if move % 100000 == 0:
            logging.info('move %d, completion %.2f', move, move/10000000)


def get_cup_list(cup_links, starting_cup):
    """Make the full list of cups for debugging purposes."""
    cup = starting_cup
    cups = [starting_cup]
    for _ in range(len(cup_links) - 1):
        next_cup = cup_links[cup]
        cups.append(next_cup)
        cup = next_cup
    return cups


def test23a():
    assert '92658374' == day23a('389125467', 10)


def day23b(input_str, num_moves=10000000, num_cups=1000000):
    cups = [int(val) for val in list(input_str)]
    remaining_cups = list(range(len(cups) + 1, num_cups + 1))
    cups = cups + remaining_cups

    cup_links = make_cup_links(cups)
    run_game(cup_links, num_moves, cups[0])

    # return the product of the two cups after 1
    cup = 1
    product = 1
    for _ in range(2):
        next_cup = cup_links[cup]
        product *= next_cup
        cup = next_cup
    return product


def test23b():
    assert 149245887792 == day23b('389125467')


if __name__ == '__main__':
    test23a()
    print('Day 23a:', day23a('362981754'))
    test23b()
    print('Day 23b:', day23b('362981754'))
