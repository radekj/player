import random

from player.utils import eval_cards


class Decision:

    def __init__(self, params):
        self.min_bet = params.get('min')
        self.can_raise = params.get('can_raise')
        self.hand = params.get('hand')
        self.table = params.get('table')
        self.chance = eval_cards(self.hand, self.table)

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
        if self.min_bet: # may fold, call or raise
            if self.chance < 0.3:
                return self._fold()
            else:
                if self.chance > 0.7 and self.can_raise:
                    return self._raise(3)
                return self._call()
        else: # may check or bet
            if self.chance < 0.5:
                return self._check()
            else:
                return self._bet(2)
