from Player import Player


class Human(Player):

    def __init__(self):
        super().__init__()

    def make_choice(self):
        while True:
            self.entity = input("Which one do you choose: Rock, Paper, or Scissors?: ").lower().capitalize()
            if self.entity not in self.possibilities:
                print("Not a valid choice, try again")
                continue
            break
