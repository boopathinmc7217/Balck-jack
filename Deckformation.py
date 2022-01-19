from typing import List, Tuple, Dict, Sequence

card_names: Tuple[str, str, str, str] = ("CLUBS", "DIAMONDS", "HEARTS", "SPADES")
card_numbers: Sequence = (
        "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING", "ACE")
card_symbols: Dict[str, int] = {"TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9,
                                "TEN": 10,
                                "JACK": 10, "QUEEN": 10, "KING": 10, "ACE": 11}

all_cards: List[str] = []


class Deck:
    """
    Formation of Deck (52 cards)

    """

    def __init__(self):
        self.card_names: Tuple = card_names
        self.card_numbers: Sequence = card_numbers

    def deck_formation(self) -> None:
        """
        Formation of Deck (52 cards). Takes Card names and card symbols
        from global and forms a deck of cards and shuffles it

        Return
        ----------
        none

        """
        for card_names_ in self.card_names:
            for card_numbers_ in self.card_numbers:
                all_cards.append(f"{card_names_} {card_numbers_}")

        import random
        random.shuffle(all_cards)
