import random

from player import Player

class AI(Player):
    def __init__(self, name):
        self.name = name
        super().__init__(name)
        
    def hand_gesture(self):
        self.gesture = random.choice()
        if self.gesture == "Rock":
            print(f'Player 2 selected {self.gesture}')
        elif self.gesture == "Paper":
            print(f'Player 2 selected {self.gesture}')
        elif self.gesture == "Scissors":
            print(f'Player 2 selected {self.gesture}')
        elif self.gesture == "Lizard":
            print(f'Player 2 selected {self.gesture}')
        elif self.gesture == "Spock":
            print(f'Player 2 selected {self.gesture}')