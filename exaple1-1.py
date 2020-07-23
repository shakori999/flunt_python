import collections
from random import choice

card = collections.namedtuple("card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQka")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, postion):
        return self._cards[postion]


suits_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suits_values) + suits_values[card.suit]


deck = FrenchDeck()
for card in sorted(deck, key=spades_high):
    print(card)

