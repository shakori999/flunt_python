import collections

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


deck = FrenchDeck()

print(len(deck))
for card in deck:
    print(card)
