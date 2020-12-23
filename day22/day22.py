import copy


def day22a(input_path):
    decks = parse_input(input_path)
    round_loser = 1  # arbitrary value to start the loop
    cards = {1: None, 2: None}
    while decks[round_loser]:
        for player in [1, 2]:
            cards[player] = decks[player].pop()
        if cards[1] > cards[2]:
            round_winner = 1
            round_loser = 2
        else:
            round_winner = 2
            round_loser = 1
        decks[round_winner] = [cards[round_loser], cards[round_winner]] + \
            decks[round_winner]

    return calc_score(decks[round_winner])


def parse_input(input_path):
    lines = [line.strip() for line in open(input_path)]
    decks = {
        1: [],
        2: [],
    }
    player = None
    for line in lines:
        if not line:
            continue
        if line == 'Player 1:':
            player = 1
        elif line == 'Player 2:':
            player = 2
        else:
            decks[player].append(int(line))
    # reverse the order of the cards so that pop() will return the next card
    for player in decks.keys():
        decks[player] = decks[player][::-1]
    return decks


def calc_score(deck):
    score = 0
    for ind, card in enumerate(deck):
        score += (ind + 1) * card
    return score


def test22a():
    assert 306 == day22a('test_input.txt')


def day22b(input_path):
    decks = parse_input(input_path)
    winner, loser = recurse(decks)
    return calc_score(decks[winner])


def recurse(decks, level=0):
    history = []
    round_loser = 1  # arbitrary value to start the loop
    cards = {1: None, 2: None}
    while decks[round_loser]:
        state = tuple([tuple(deck) for deck in decks.values()])
        if state in history:
            round_winner = 1
            round_loser = 2
            break
        history.append(state)
        recurse_ok = True
        for player in [1, 2]:
            cards[player] = decks[player].pop()
            recurse_ok = recurse_ok and (len(decks[player]) >= cards[player])
        if recurse_ok:
            decks_copy = {player: copy.deepcopy(deck[-cards[player]:])
                     for player, deck in decks.items()}
            round_winner, round_loser = recurse(decks_copy, level + 1)
        else:
            if cards[1] > cards[2]:
                round_winner = 1
                round_loser = 2
            else:
                round_winner = 2
                round_loser = 1
        # print('Player {} wins\n'.format(round_winner))
        decks[round_winner] = [cards[round_loser], cards[round_winner]] + \
            decks[round_winner]
    return round_winner, round_loser


def test22b():
    assert 291 == day22b('test_input.txt')
    decks = parse_input('test_input2.txt')
    winner, loser = recurse(decks)


if __name__ == '__main__':
    test22a()
    print('Day 22a:', day22a('day22_input.txt'))
    test22b()
    print('Day 22b:', day22b('day22_input.txt'))
