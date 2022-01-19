import Cards

from typing import ClassVar, List

Card: ClassVar = Cards.Card


class UserDisplay:

    def __init__(self, player_name: str) -> None:
        self.player_name: str = player_name
        self.card_value: int = 0
        self.user_cards_list: List[str] = []
        self.card_list: List[str] = []
        self.bet_balance: int = 0
        self.starting_balance: int = 5000
        self.hit_ace: int = 0

    def game_start(self) -> None:
        Card.player_data_start(self)

    def game_continue(self) -> None:
        Card.player_data_generation(self)

    def reset(self) -> None:
        self.card_value = 0
        self.card_list = []
        self.user_cards_list = []
        self.bet_balance = 0
        self.hit_ace = 0
