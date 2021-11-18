import random

from player import Player

class AI(Player):
    def __init__(self):
        super().__init__()
        self.set_name()
        
    def hand_gesture(self):
        self.choice = random.choice(self.gesture_list)
        if self.choice == "Rock":
           print(f'\n{self.name} has randomly selected {self.choice}')
        elif self.choice == "Paper":
           print(f'\n{self.name} has randomly selected {self.choice}')
        elif self.choice == "Scissors":
           print(f'\n{self.name} has randomly selected {self.choice}')
        elif self.choice == "Lizard":
           print(f'\n{self.name} has randomly selected {self.choice}')
        elif self.choice == "Spock":
           print(f'\n{self.name} has randomly selected {self.choice}')

    def set_name(self):
        self.name = "Master AI"
