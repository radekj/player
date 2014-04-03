Poker Player app
================

The Poker Player application

Acts as the client application that counts and returns the decision for the
poker [Dealer server](https://github.com/radekj/dealer).


Installation
------------

Use the [player-buildout](https://github.com/radekj/player-buildout) to install
the application.


Technical description
---------------------

The application runs with pure Python (>=3.3). The only dependency is the
[pokereval](https://github.com/aliang/pokerhand-eval) package which provides a
helper algorithm for evaluating poker cards hand that may support the decision
counting process.

The application runs a simple wsgi server for http communication with the
dealer app. The parameters are sent in json format.


Game rules
----------

The game's rules are very close to the
[rules of Texas hold'em](http://en.wikipedia.org/wiki/Texas_hold_%27em#Rules)
variation of the standard card game of poker. The only main difference is
that the maximal bet is limited - there is no possibility of making *all-in* bet.

The objective is to modify the decision calculating algorithm to win the game.
User can use the card's evaluation algorithm -
[pokereval](https://github.com/aliang/pokerhand-eval) but in some situations
the algorithm is not accurate, for example: it evaluates the strength
of **current** set of cards without taking into account a potential cards
that can appear on the table in the next phases, which is significant in
case of *straight* or *colour* hands.

The Dealer application's params send in request:

- `hand` - (list of tuples) - Your hand cards, example: `[('S', 'A'), ('H', '7')]` 
  (Ace of spades and 7 of Hearts)
- `table` - (list of tuples) - The cards on the table,
  example: `[('D', '2'), ('H', '7'), ('H', 'Q')]` 
- `min` - (int) - The minimal amount you must bet to stay in the game
- `limit` - (int) - The maximal amount you can bet
- `can_raise` - (bool) - The iformation if you can raise the bet in this turn
- `pot` - (int) - the actual amount of coins in the pot
- `account` - (int) - the actual amount of coins in your account


Before accessing the game - the user **must ensure that all the tests passes**:

`./bin/test`


