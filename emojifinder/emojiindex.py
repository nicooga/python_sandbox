#!/usr/bin/env python

"""
Class ``InvertedIndex`` builds an inverted index mapping each word to
the set of Unicode characters which contain that word in their names.

Optional arguments to the constructor are ``first`` and ``last+1``
character codes to index, to make testing easier. In the examples
below, only the ASCII range was indexed.

The `entries` attribute is a `defaultdict` with uppercased single
words as keys::

    >>> idx = InvertedIndex(32, 128)
    >>> idx.entries['DOLLAR']
    {'$'}
    >>> sorted(idx.entries['SIGN'])
    ['#', '$', '%', '+', '<', '=', '>']
    >>> idx.entries['A'] & idx.entries['SMALL']
    {'a'}
    >>> idx.entries['BRILLIG']
    set()

The `.search()` method takes a string, uppercases it, splits it into
words, and returns the intersection of the entries for each word::

    >>> idx.search('capital a')
    {'A'}

"""

import sys
import unicodedata
from collections import defaultdict
from collections.abc import Iterator

STOP_CODE: int = sys.maxunicode + 1

Emoji = str
Index = defaultdict[str, set[Emoji]]


def tokenize(text: str) -> Iterator[str]:
    """return iterator of uppercased words"""
    for word in text.upper().replace('-', ' ').split():
        yield word


class EmojiInvertedIndex:
    entries: Index


    def __init__(self):
        entries: Index = defaultdict(set)
        start = 0x1F600
        stop = 0x1F64F

        for i in range(start, stop):
            emoji = chr(i)
            name = unicodedata.name(emoji, '')

            if name:
                for word in tokenize(name):
                    entries[word].add(emoji)

        self.entries = entries


    def search(self, query: str) -> set[Emoji]:
        words = tokenize(query)
        result = set[Emoji]()
        for word in words: result.update(self.entries[word])
        return result


def main() -> None:
    index = EmojiInvertedIndex()
    print(index.search('fire'))


if __name__ == '__main__':
    main()