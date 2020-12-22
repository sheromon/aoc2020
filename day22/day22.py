import queue


def day22a(input_path):
    lines = [line.strip() for line in open(input_path)]
    decks = {
        1: queue.Queue(),
        2: queue.Queue(),
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
            decks[player].put(int(line))

    done = False
    cards = {1: None, 2: None}
    while not done:
        for player in [1, 2]:
            cards[player] = decks[player].get()
        if cards[1] > cards[2]:
            round_winner = 1
            round_loser = 2
        else:
            round_winner = 2
            round_loser = 1
        decks[round_winner].put(cards[round_winner])
        decks[round_winner].put(cards[round_loser])
        done = decks[round_loser].empty()

    return calc_score(decks[round_winner])


def calc_score(deck):
    all_cards = []
    while not deck.empty():
        all_cards.append(deck.get())
    score = 0
    for ind, card in enumerate(all_cards[::-1]):
        score += (ind + 1) * card
    return score


def test22a():
    assert 306 == day22a('test_input.txt')


def day22b(input_path):
    pass


# def test22b():
#     assert 286 == day22b('test_input.txt')


if __name__ == '__main__':
    test22a()
    print('Day 22a:', day22a('day22_input.txt'))
    # test22b()
    # print('Day 22b:', day22b('day22_input.txt'))
