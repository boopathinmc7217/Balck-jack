from Userdisplay import UserDisplay
from Deckformation import Deck
from typing import List, Optional, Sequence, Union


class complete:
    # __metaclass__ = Cards, UserDisplay
    @staticmethod
    def hit(a_object) -> Optional[str]:
        a_object.game_continue()
        if "ACE" in a_object.user_cards_list and a_object.card_value > 21:
            if a_object.card_value > 21 and a_object.hit_ace == 0:
                a_object.card_value = a_object.card_value - 10
                a_object.hit_ace += 1
            if a_object.user_cards_list.count("ACE") == 2 and a_object.hit_ace == 1:
                a_object.card_value = a_object.card_value - 10
                a_object.hit_ace += 1
            if a_object.user_cards_list.count("ACE") == 3 and a_object.hit_ace == 2:
                a_object.card_value = a_object.card_value - 10
                a_object.hit_ace += 1
            if a_object.user_cards_list.count("ACE") == 4 and a_object.hit_ace == 3:
                a_object.card_value = a_object.card_value - 10
                a_object.hit_ace += 1
        if a_object.card_value < 21:
            print(f"{a_object.player_name}:{a_object.card_list},Rank : {a_object.card_value}")
            return
        if a_object.card_value > 21:
            print(f"{'=' * 5}  {a_object.player_name} BUSTED {'=' * 5}")
            print(f"{a_object.player_name}:{a_object.card_list},Rank : {a_object.card_value}")
            return "BUST"

    @staticmethod
    def winner_bet_balance(user_count_list: Sequence) -> [Union[str, int]]:
        win_rank: int = 0
        if len(user_count_list) == 2 and (user_count_list[0].card_value == user_count_list[1].card_value):
            print(("=" * 5), "PUSH", ("=" * 5))
            print(
                f"{user_count_list[0].player_name}:{user_count_list[0].card_list},Rank : "
                f"{user_count_list[0].card_value}")
            print(
                f"{user_count_list[1].player_name}:{user_count_list[1].card_list},Rank : "
                f"{user_count_list[1].card_value}")
            print("PUSH")
            return "PUSH", "NO Winner"
        winner_prediction: List[int] = [cards_value.card_value for cards_value in user_count_list]
        win_rank = max([i for i in winner_prediction if 21 >= i > win_rank])
        c = [cards_value.player_name for cards_value in user_count_list if cards_value.card_value == win_rank]
        if len(c) == 2:
            return " Two Players Tied", " considered as Push"
        bet_winner: str = "".join(c)
        winner_balance: int = sum([i.bet_balance for i in user_count_list if i.player_name != bet_winner])
        for i in user_count_list:
            if i.player_name != bet_winner:
                i.starting_balance = i.starting_balance - i.bet_balance

        for i in user_count_list:
            if i.player_name == bet_winner:
                i.starting_balance = i.starting_balance + winner_balance
        if bet_winner == "Dealer":
            return bet_winner, "Dealer Takes ALL"
        return bet_winner, winner_balance

    def gameplay(self, user_count_list: List) -> str:
        list_index: int = 0
        while True:
            a_object = user_count_list[list_index]

            if a_object.player_name == "Dealer":
                a_object.starting_balance = 0
                while a_object.card_value < 17:
                    return_holder = self.hit(a_object)
                    if return_holder == "BUST":
                        game_winner, winner_balance = self.winner_bet_balance(user_count_list)
                        print(f"{a_object.player_name}: {a_object.card_list} Rank : {a_object.card_value}")
                        break
                    elif a_object.card_value >= 17:
                        print(f"{a_object.player_name}: {a_object.card_list} Rank : {a_object.card_value}")
                        game_winner, winner_balance = self.winner_bet_balance(user_count_list)
                        break
                else:
                    print(f"{a_object.player_name}: {a_object.card_list} Rank : {a_object.card_value}")
                    game_winner, winner_balance = self.winner_bet_balance(user_count_list)
                break
            a_object.bet_balance = (input(f"{a_object.player_name} enter bet amount : "))
            while True:
                if a_object.bet_balance.isdigit() and int(a_object.bet_balance) in range(1, 5001):
                    a_object.bet_balance = int(a_object.bet_balance)
                    break
                else:
                    print("Enter numbers between 1-5000 only : ")
                    a_object.bet_balance = input(f"{a_object.player_name} enter bet amount : ")
            a_hit_stand = input(f"{a_object.player_name}Want to Hit(h) or Stand(s) : ").upper()
            while a_hit_stand in ["HIT", "H"]:
                return_holder = self.hit(a_object)
                if return_holder == "BUST":
                    list_index += 1
                    break
                else:
                    a_hit_stand = input(f"{a_object.player_name}Want to Hit(h) or Stand(s) : ").upper()
            while a_hit_stand in ["STAND", "S"]:
                list_index = 1 + list_index
                print(f"{a_object.player_name}: {a_object.card_list} Rank : {a_object.card_value}")
                break
        print(f"Winner is {game_winner}")
        for i in user_count_list:
            if i != "Dealer":
                print(f"{i.player_name} balance: {i.starting_balance}")
        Deck().deck_formation()
        new_game = input("Want a new game Yes").upper()

        return new_game

    def set_up(self) -> None:
        Deck().deck_formation()
        user_count: int = int(input("enter number of users"))
        user_count_list: Sequence[UserDisplay] = [UserDisplay(input("enter username")) for _ in range(user_count)]
        user_count_list.append(UserDisplay("Dealer"))

        def new_play() -> None:
            for object_player in user_count_list:
                object_player.game_start()
            for index in range(len(user_count_list)):
                a_object = user_count_list[index]  # need to ask meeting about
                print(f"{a_object.player_name} balance is {a_object.starting_balance}")
                if a_object.player_name == "Dealer":
                    print(f"{a_object.player_name}:{a_object.card_list[0]}")
                else:
                    print(f"{a_object.player_name}:{a_object.card_list},Rank :{a_object.card_value}")
            user_choice = self.gameplay(user_count_list)
            if user_choice in ["YES", "Y"]:
                for i in user_count_list:
                    i.reset()
                new_play()
                self.gameplay(user_count_list)

        new_play()


if __name__ == "__main__":
    Deck().deck_formation()
    print("Welcome to BlackJack")
    complete().set_up()
