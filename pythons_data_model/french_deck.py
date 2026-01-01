from collections import namedtuple

# namedtuple is a class that creates a new class from a tuple.
# Useful when defining a simple data class with no additional methods.
Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list[str]('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [
            Card(rank, suit)
            for rank in self.ranks
            for suit in self.suits
        ]

    # Special "dunder" methods are methods that are called when the object is used in a special way.
    # "dunder" means "double underscore before and after".
    # For instance, __len__ is called when the object is used in a len() function.
    # Usage: len(deck)
    def __len__(self):
        return len(self._cards)

    # __getitem__ is called when the object is used in a [] operator.
    # Usage: deck[0]
    def __getitem__(self, position):
        return self._cards[position]

if __name__ == '__main__':
    # Because FrenchDeck is a sequence, we can use the choice function to randomly select a card.
    # No need to implement .pick() method ourselves.
    from random import choice
    deck = FrenchDeck()
    print(choice(deck))
