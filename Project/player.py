class Player:
    def __init__(self):
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.name = ""
        self.choice = ""
        self.score = 0
        

    def choose_gesture(self):
        print(f"Pick one of the gestures")
        self.choice = (input("Press 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, 4 for Spock: "))
        validated_choice = self.user_input_validation(self.choice)
        if validated_choice == 0:
            print(f"{self.name} selected {self.gesture_list[0]}")
        elif validated_choice == 1:
            print(f"{self.name} selected {self.gesture_list[1]}")
        elif validated_choice == 2:
            print(f"{self.name} selected {self.gesture_list[2]}")
        elif validated_choice == 3:
            print(f"{self.name} selected {self.gesture_list[3]}")
        elif validated_choice == 4:
            print(f"{self.name} selected {self.gesture_list[4]}")

    def user_input_validation(self, choice):
        if int(choice) > len(self.gesture_list):
            print(f"Invalid gesture, please choose again! ")
            self.choose_gesture()
        else:
            return int(choice)