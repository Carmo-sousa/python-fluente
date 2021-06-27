""" um barralho com sequência de cartas """
import collections
from typing import NamedTuple

Card: NamedTuple[str, str] = collections.namedtuple("Card", ["rank", "suit"])

suit_values: dict[str, int] = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card: Card) -> int:
    rank_value: int = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        self._cards: list[Card] = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    def __len__(self) -> int:
        """Retorna o tamanho do deck"""
        return len(self._cards)

    def __getitem__(self, position: int) -> Card:
        return self._cards[position]
