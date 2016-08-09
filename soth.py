import random

from soth.player import *
from soth.card import *
from soth.utility import *

command = ""

def fill_deck():
    pass

greet()
me = Player(prompt_action(9))
me.feelings()

other = Player(random.randint(0, 8), npc=True)
other.feelings()

me.deck = Deck(me)
me.hand = Hand(me)
me.board = Board(me)

other.deck = Deck(other)
other.hand = Hand(other)
other.board = Board(other)

# decide who gets to start
coinflip = random.randint(0,1)
if coinflip == 1:
    print('you spring into action!\n')
    me.deck.draw(me.hand, 3)
    other.deck.draw(other.hand, 4)
else:
    print('your opponent gets the jump on you!\n')
    other.deck.draw(other.hand, 3)
    me.deck.draw(me.hand, 4)
print()

me.mulligan()

if coinflip == 1:
    other.hand.add([Card(id2Idx['GAME_005'])]) # the coin
else:
    me.hand.add([Card(id2Idx['GAME_005'])]) # the coin


# while not end_of_game :
#     prompt_action()
