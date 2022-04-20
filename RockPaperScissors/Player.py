class Player:

    def __init__(self):
        self.possibilities = ("Rock", "Paper", "Scissors")
        self.entity = ""

    def delete_choice(self):
        self.entity = ""
