import random

def make_decisom(params):
    return 0
    min_bet = params.get('min')
    max_bet = params.get('max')
    bet = random.choice([0, 1, 2,  3, 4, 5])
    if min_bet:
        #bet = min_bet
        bet = random.choice([min_bet, min_bet, min_bet + 2])
    if max_bet:
        #bet = max_bet
        bet = min_bet
        #bet = random.choice([0, max_bet, max_bet])
    print(bet)
    return bet
