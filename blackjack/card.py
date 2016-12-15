class Card:

    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __str__(self):
        return '%s of %s' % (self.rank, self.suit)

    def __repr__(self):
        return '%s of %s' % (self.rank, self.suit)

