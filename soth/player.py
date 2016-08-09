from .card import *
from .utility import *

class_adjective = ['strong', 'spiritual', 'sneaky',
                    'righteous', 'heartless', 'wild',
                    'wicked', 'magical', 'holy',]

text = {
    'drawCard': [
        '{0} pops out from between your muscles!',
        'you spot {0} amongst your totems!',
        '{0} slips out from your sleeve!',
        'a law-abiding citizen hands you {0}, how virtuous!',
        'you sniff out {0} from the tall grass!',
        'a mass of critters from the forest floor compress into {0} for you!',
        'a voice in your head echoes... "here, take {0}!"',
        'you wave your hands about you... *poof*... you get {0}!',
        'a beacon of light beams from the heavens, {0} lies at your feet!'
    ],
    'shuffleDeck': [
        'you furiously shuffle your deck!',
        'you sense the disorder in your deck manifest!',
        'you never really "shuffle" your deck, but you do try!',
        'you riffle shuffle your deck at least seven times!',
        'the way you shuffle leaves a lot to be desired, you even bend the corners as you jam them together',
        'you try to shuffle your deck the way nature would have done it!',
        'some imps shuffle your deck. Neat!',
        'you make pretend magic noises... *poof*... your deck is shuffled!',
        'you notice a faint glimmer of light on your deck. The Heavens make light off your situation and have decided to shuffle your deck for you!',
    ],
    'mulligan': [
        'you HATE these cards! these are decidedly the WORST of the bunch!',
        'these were not todays cards.',
        'dismay strikes you as you scoff at the hand you drew',
        'the RULES say you can redraw your cards! it\'s fair and just!',
        '*growling noises*',
        'nature makes a lot of mistakes...',
        '\"another nasty hand\" you begrudge',
        '\"My magic will mulligan this\"... the cards float back onto your deck',
        'you stretch out your hand and clench it as if to take your opponents hand...\"this is a bad hand!, i don\'t like it!\" you announce to your opponent.',
    ],
}

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

    def feelings(self):
        if self.npc:
            print('your opponent feels ' + class_adjective[self.classtype])
        else:
            print('you feel ' + class_adjective[self.classtype])
        print()

    # aka. the cards you currently have
    def display_choices(self):
        pass

    def end_turn(self):
        pass

    def mulligan(self):
        print("do you like these cards?\n")
        print("1. yes")
        print("2. no")
        choice = prompt_action(2)
        if choice == 1:
            self.deck.add(self.hand.cards) # deck your hand
            if not self.npc:
                print(self.text('mulligan'))
            del self.hand.cards[:] # empty your hand
            if not self.npc:
                print(self.text('shuffleDeck'))
            random.shuffle(self.deck.cards)

    def text(self, event):
        return text[event][self.classtype]
