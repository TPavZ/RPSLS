class Player:
    def __init__(self,name):
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.name = name
        self.choice = ""
        self.score = 0
        

    def choose_gesture(self):
        print("Pick one of the gestures")
        for gesture in self.gesture_list:
            print(gesture)
            
        user_input = int(input("Press 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, 4 for Spock: "))
        if user_input == 0:
            print(f"{self.name} selected {self.gesture_list[0]}")
        elif user_input == 1:
            print(f"{self.name} selected {self.gesture_list[1]}")
        elif user_input == 2:
            print(f"{self.name} selected {self.gesture_list[2]}")
        elif user_input == 3:
            print(f"{self.name} selected {self.gesture_list[3]}")
        elif user_input == 4:
            print(f"{self.name} selected {self.gesture_list[4]}")
        