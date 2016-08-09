import json
import random

cardsfile = open('cards.json', 'r')
allcards = json.load(cardsfile)

classIdx = { 'WARRIOR':0, 'SHAMAN':1, 'ROGUE':2,
             'PALADIN':3, 'HUNTER':4, 'DRUID':5,
             'WARLOCK':6,  'MAGE':7, 'PRIEST':8,
             'DREAM':9, }

id2Idx = {}

classcards = [[], [], [], [], [], [], [], [], [], []]
neutralcards = []

for idx in range(0, len(allcards) - 1):
    card = allcards[idx]

    id = card.get('id')
    id2Idx[id] = idx

    pc = card.get('playerClass', None)
    if pc:
        classcards[classIdx[pc]].append(idx)
    else:
        neutralcards.append(idx)

# print(allcards[random.randint(0, len(allcards)-1 )]) # DEBUG

class Card:
    def __init__(self, idx):
        self.idx = idx
        self.id = allcards[idx]['id']
        self.name = allcards[idx]['name']
        self.type = allcards[idx]['type']
        self.mechanics = allcards[idx].get('mechanics', None)
        self.playerclass = allcards[idx].get('playerClass', None)
        self.set = allcards[idx]['set']
    def __repr__(self):
        return allcards[self.idx]['name']

class Deck:
    def __init__(self, owner, count=30):
        self.owner = owner
        self.cards = []

        for i in range(count):
            combinedset = list(classcards[owner.classtype])
            combinedset.extend(neutralcards)
            card = Card(random.choice(combinedset))
            self.add([card]) # add takes a list of cards

    def draw(self, target, count=1):
        for i in range(count):
            card = self.cards.pop(0)
            target.add([card])
            if self.owner.npc == False:
                print(self.owner.text('drawCard').format(str(card)))
                # print('your deck has ' + str(len(self.cards)) + ' cards!') # DEBUG

    def add(self, cards):
        self.cards.extend(cards)

        # if self.owner.npc == False:
        #     print('your deck has ' + str(len(self.cards)) + ' cards!') # DEBUG

class Hand:

    def __init__(self, owner):
        self.owner = owner
        self.cards = []

    def add(self, cards):
        self.cards.extend(cards)

    def remove(self, idx):
        card = self.cards.pop(idx)
        print('you remove: ' + str(idx) + ' from your hand!')

    def play(self, idx):
        card = self.cards.pop(idx)
        print('you play: ' + str(idx) + ' from your hand!')

class Board:
    def __init__(self, owner):
        self.owner = owner
        self.cards = []
