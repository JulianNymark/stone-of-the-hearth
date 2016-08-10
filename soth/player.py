from .card import *
from .utility import *
from .textstrings import *

class Player:
    """A player in the game"""
    mana = 1
    mana_used = 0
    overload_now = 0
    overload_next = 0
    health = 30
    armour = 0
    damage = 0
    attack = 0

    def __init__(self, ct, npc=False):
        self.classtype = ct
        self.npc = npc
        self.adj = class_adjective[self.classtype]

    def feelings(self):
        if self.npc:
            print('your opponent feels ' + self.adj)
        else:
            print('you feel ' + self.adj)
        print()

    def display_choices(self):
        self.choice_count = 2 # end turn & hero power
        self.choice_count += len(self.hand.cards) # card hand
        # attackers

        print()
        print('1. end turn')
        print('2. become more {0}'.format(self.adj))

        for i in range(len(self.hand.cards)):
            card = self.hand.cards[i]
            print('{0}. {1}'.format(i + 3, str(card)))

    def start_turn(self):
        self.mana_used = 0
        if self.mana < 10:
            self.mana += 1

    def end_turn(self):
        pass

    def mulligan(self):
        print("do you like these cards?\n")
        print("1. yes")
        print("2. no")
        choice = prompt_action(2)
        if choice == 1:
            handsize = len(self.hand.cards)
            self.deck.add(self.hand.cards) # deck your hand
            if not self.npc:
                print(self.text('mulligan'))
            del self.hand.cards[:] # empty your hand
            if not self.npc:
                print(self.text('shuffleDeck'))
                print()
            random.shuffle(self.deck.cards)
            self.deck.draw(self.hand, handsize) # re-draw hand

    def text(self, event):
        return text[event][self.classtype]

    def take_turn(self):
        if not self.npc:
            self.start_turn()

            while True:
                self.display_choices()
                choice = prompt_action(self.choice_count)
                if choice == 0:
                    break
                elif choice == 1:
                    self.mana_used += 2
                    print('you chant {0}... {0}...{0}!'.format(self.adj))
                else:
                    self.hand.play(choice - 2)

            self.end_turn()

        else:
            self.start_turn()
            # do random shit
            self.end_turn()
