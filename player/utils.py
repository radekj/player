from pokereval.card import Card
from pokereval.hand_evaluator import HandEvaluator

COLORS = {
    'S': 1,
    'H': 2,
    'D': 3,
    'C': 4,
}

TRUMPS = {
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}


def translate_to_value(card):
    """
    Translates card's tuple-of-strings representation that is fetched
    from the request param into tuple-of-integers representation that matches
    the pokereval cards evaluation algorithm:

    >>> translate_to_value(('S', '7'))
    (7, 1)
    >>> translate_to_value(('D', 'Q'))
    (12, 3)

    """
    try:
        value = int(card[1])
    except ValueError:
        value = TRUMPS.get(card[1])
    color = COLORS.get(card[0])
    return (value, color)


def card_values(cards):
    """
    Translates a sequence of cards into tuple-of-integers representation:

    >>> card_values((('S', '2'), ('H', 'A'), ('C', '6')))
    [(2, 1), (14, 2), (6, 4)]
    """
    cards_translated = map(translate_to_value, cards)
    return [i for i in cards_translated]


def eval_cards(hand, table):
    """
    Returns the cards' strength value evaluated with the pokereval
    cards evaluation algorithm.

    No cards on table (only hand cards are known):
    >>> table = []
    >>> hand = [('S', '2'), ('H', 'A')]
    >>> eval_cards(hand, table)
    0.6817496229260935

    Three cards on table:
    >>> table = [('D', '3'), ('D', 'J'), ('C', 'Q')]
    >>> hand = [('S', '2'), ('H', 'A')]
    >>> eval_cards(hand, table)
    0.5074005550416282

    Four cards on table:
    >>> table = [('D', '3'), ('D', 'J'), ('C', 'Q'), ('C', 'K')]
    >>> hand = [('S', '2'), ('H', 'A')]
    >>> eval_cards(hand, table)
    0.39468599033816426

    Five cards on table:
    >>> table = [('D', '3'), ('D', 'J'), ('C', 'Q'), ('C', 'K'), ('S', '10')]
    >>> hand = [('S', '2'), ('H', 'A')]
    >>> eval_cards(hand, table)
    0.9348484848484848
    """
    hand = [Card(*card) for card in card_values(hand)]
    table = [Card(*card) for card in card_values(table)]
    chance = HandEvaluator.evaluate_hand(hand, table)
    return chance
