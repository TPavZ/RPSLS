class Player:
    def __init__(self):
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.name = ""
        self.choice = ""
        self.score = 0
        

    def choose_gesture(self):
        if self.choice == 0:
            print(f"{self.name} selected {self.gesture_list[0]}")
        elif self.choice == 1:
            print(f"{self.name} selected {self.gesture_list[1]}")
        elif self.choice == 2:
            print(f"{self.name} selected {self.gesture_list[2]}")
        elif self.choice == 3:
            print(f"{self.name} selected {self.gesture_list[3]}")
        elif self.choice == 4:
            print(f"{self.name} selected {self.gesture_list[4]}")

    