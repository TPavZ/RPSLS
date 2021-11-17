from player import Player

class Human(Player): #need to make a gesture choice

    def __init__(self, name):
        super().__init__()
        self.name = name
        
    def hand_gesture(self):
        print(f"Pick one of the gestures")
        self.choice = int(input("Press 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, 4 for Spock: "))
        


            #while self.choice not in self.gesture_list:
            #print(f"Invalid gesture, please choose again! ")
            #self.hand_gesture()