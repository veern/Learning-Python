from Human import Human
from CPU import CPU
from Scoreboard import Scoreboard


def start_and_choose_player_amount() -> int:
    print("Welcome to a rock, paper and scissors game!")
    while True:
        choice = int(input("First of all, I would like to know how many human players are taking part in this game: "))
        if choice == 0:
            print("The game will be between two CPUs.")
        elif choice == 1:
            print("The game will be between 1 human player (Player 1) and 1 CPU.")
        elif choice == 2:
            print("The game will be between 2 human players.")
        else:
            print("The input was not valid, try again.")
            continue
        return choice


def who_won_round(player1: Human | CPU, player2: Human | CPU, scoreboard: Scoreboard) -> None:
    winning_relations = [
        ("Rock", "Scissors"),
        ("Paper", "Rock"),
        ("Scissors", "Paper"),
    ]

    if (player1.entity, player2.entity) in winning_relations:
        print(f"{player1.entity} wins over {player2.entity}!\nPlayer 1 wins!")
        scoreboard.add_point(player1)
    elif player1.entity == player2.entity:
        print(f"It's a tie!")
    else:
        print(f"{player2.entity} wins over {player1.entity}!\nPlayer 2 wins!")
        scoreboard.add_point(player2)


def generate_players_and_scoreboard(choice: int) -> (Human | CPU, Human | CPU, Scoreboard):
    if choice == 0:
        player1, player2 = CPU(), CPU()
    elif choice == 1:
        player1, player2 = Human(), CPU()
    else:
        player1, player2 = Human(), Human()
    scoreboard = Scoreboard(player1, player2)
    return player1, player2, scoreboard
