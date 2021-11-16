import random

from player import Player

class AI(Player):
    def __init__(self):
        super().__init__()
        self.set_name()
        
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
            
            
    def set_name(self):
        self.name = "Master AI"