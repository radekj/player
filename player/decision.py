import random

from player.utils import eval_cards


class Decision:
    """ Class for encapsulating the decision making algorithm
    and helper methods.
    """

    def __init__(self, params):
        """ Fetching params from request """
        self.min_bet = params.get('min')
        self.can_raise = params.get('can_raise')
        self.hand = params.get('hand')
        self.table = params.get('table')
        self.chance = eval_cards(self.hand, self.table)
        self.limit = params.get('limit')
        self.account = params.get('account')
        self.active_players = params.get('active_players')

    def _fold(self):
        """ Fold:
        You lay down your cards and stop playing the hand.
        (http://pokerterms.com/fold.html)
        """
        return 0

    def _check(self):
        """ Check:
        You bet nothing while remaining in the hand.
        (http://pokerterms.com/check.html)
        """
        return 0

    def _call(self):
        """ Call:
        You match the bet of a player who has already bet.
        (http://pokerterms.com/call.html)
        """
        if self.min_bet >= self.account:
            return 0
        return self.min_bet

    def _bet(self, bet):
        """ Bet:
        You wager an initial amount of money.
        (http://pokerterms.com/bet.html)
        """
        if bet >= self.account:
            return self.account
        return bet

    def _raise(self, bet):
        """ Raise:
        You bet more than the minimum after a bet has been made.
        (http://pokerterms.com/raise.html)
        """
        bet = self.min_bet + bet
        if bet >= self.account:
            return self.account
        return bet

    def make_decison(self):
        """ The method for counting and returning your decision.
        This is the method that is called by the application engine.
        Modify the example code given below to win the game!
        """
        if self.min_bet > self.account:    # not enought money to play
            return self._fold()
        if self.min_bet:    # may fold, call or raise
            if self.chance < 0.3:
                return self._fold()
            else:
                if self.chance > 0.7 and self.can_raise:
                    bet = random.choice(range(1, self.limit))
                    return self._raise(bet)
                return self._call()

        else:   # may check or bet
            if self.chance < 0.5:
                return self._check()
            else:
                bet = random.choice(range(1, self.limit))
                return self._bet(bet)

def chellengers_cards(params):
    """
    The method for processing the information about the cards of final
    challengers and table cards.

    This enable to adapt the algorithm to take into account other players'
    strategies.

    Example params:
    {
        'player3': [['S', '4'], ['S', 'Q']],
        'player1': [['C', 'J'], ['D', '10']],
        'table': [['H', '9'], ['D', 'K'], ['H', 'J'], ['C', '4'], ['S', 'A']]
    }
    """
    return
