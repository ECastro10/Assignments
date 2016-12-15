import random as r
from card import Card


class Deck:
    def __init__(self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                      'Jack', 'Queen', 'King', 'Ace']
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.card = []

        for suit in self.suits:
            i = 0
            for rank in self.ranks:
                self.card.append(Card(rank, suit, self.value[i]))
                i += 1


