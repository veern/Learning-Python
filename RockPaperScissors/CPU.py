from Player import Player
from random import choice


class CPU(Player):

    def __init__(self):
        super().__init__()

    def make_choice(self):
        self.entity = choice(self.possibilities)
