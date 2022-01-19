from typing import Tuple, List

import Deckformation

card_symbols = Deckformation.card_symbols
all_cards = Deckformation.all_cards


class Card:
    """
    Class Card is responsible the cards given to players at each step of the game

    """
    def __init__(self):
        self.card_value: int = 0
        self.card_list: List[str] = []
        self.user_cards_list: List[str] = []

    def player_data_generation(self) -> Tuple[str, int]:
        """
        Player_data_generation is responsible for the Single cards given to the player
        when player chooses to hit

        -------------
        Takes a card from shuffled deck looks for it's rank and gives the total rank of the player
        and drawn card

        return
        -----------------
        card drawn from the deck and rank of the player

        """
        user_cards: str = all_cards.pop(0)
        temp_variable = user_cards.split()
        temp_variable = temp_variable[1].upper()
        self.card_list.append(user_cards)
        self.user_cards_list.append(temp_variable)
        card_value_holder: int = int(card_symbols[temp_variable])
        self.card_value = self.card_value + card_value_holder
        return user_cards, self.card_value

    def player_data_start(self) -> None:
        """
        Player_data_start is responsible for the two cards given to the player
        at the start of the game

        -------------
        It sums the Rank for the player and adds two cards to the individual player

        return
        -----------------
        none
        """
        for two_cards in range(2):
            user_cards: str = all_cards.pop(0)
            temp_variable = user_cards.split()
            temp_variable = temp_variable[1].upper()
            self.card_list.append(user_cards)
            self.user_cards_list.append(temp_variable)
            card_value_holder = int(card_symbols[temp_variable])
            self.card_value = self.card_value + card_value_holder
            """ To avoid Ace & Ace Conflict at start """
            if temp_variable == "ACE" and self.card_value > 21:
                self.card_value = self.card_value - 10
