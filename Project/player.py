class Player:
    def __init__(self):
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.name = ""
        self.choice = ""
        self.score = 0
        

    def choose_gesture(self):
        print(f"\n{self.name} pick one of the gestures below ↓")
        self.choice = int(input("Press 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, 4 for Spock: "))
        validation = self.validation(self.choice)
        self.choice = self.gesture_list[validation]
        print(f"\n{self.name} selects {self.choice}")
        return self.choice

    def validation(self, validation):
        if validation > len(self.gesture_list):
            print(f"Invalid gesture, please choose again! ")
            self.choose_gesture()
        else:
            return validation

    