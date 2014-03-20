import random

from player.utils import eval_cards


class Decision:

    def __init__(self, params):
        self.min_bet = params.get('min')
        self.can_raise = params.get('can_raise')
        self.hand = params.get('hand')
        self.table = params.get('table')
        self.chance = eval_cards(self.hand, self.table)
        self.limit = params.get('limit')

    def _fold(self):
        return 0

    def _bet(self, bet):
        return bet

    def _raise(self, bet):
        bet = self.min_bet + bet
        return bet

    def _check(self):
        return 0

    def _call(self):
        return self.min_bet

    def make_decison(self):
        print(self.chance)
        if self.min_bet: # may fold, call or raise
            if self.chance < 0.3:
                return self._fold()
            else:
                if self.chance > 0.7 and self.can_raise:
                    bet = random.choice(range(1,self.limit))
                    return self._raise(bet)
                return self._call()
        else: # may check or bet
            if self.chance < 0.5:
                return self._check()
            else:
                bet = random.choice(range(1,self.limit))
                return self._bet(bet)
