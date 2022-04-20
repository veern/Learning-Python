from Player import Player
from Human import Human
from CPU import CPU


class Scoreboard:

    def __init__(self, player_1: Human | CPU, player_2: Human | CPU) -> None:
        self.players = (player_1, player_2)
        self.players_scores = {self.players[0]: 0, self.players[1]: 0}

    def add_point(self, player: Human | CPU) -> None:
        if player in self.players:
            self.players_scores[player] += 1

    def display_scores(self) -> None:
        idx = 1
        for key, value in self.players_scores.items():
            if isinstance(key, Human):
                print(f"Player {idx}, which is a human: score of {value}")
            elif isinstance(key, CPU):
                print(f"Player {idx}, which is a CPU: score of {value}")
            idx += 1
