class Player:
    def __init__(self):
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.name = ""
        self.choice = ""
        self.score = 0
        

    def choose_gesture(self):
        validation = False
        print(f"\n{self.name} pick one of the gestures below ↓")
        while validation == False:
            input_int = int(input("\nPress 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, 4 for Spock: "))
            if input_int <= 4:
                validation = True
            else:
                validation = False
                print(f"\nInvalid gesture, please choose again! ")
        self.choice = self.gesture_list[input_int]
        print(f"\n{self.name} has selected {self.choice}")
        return self.choice