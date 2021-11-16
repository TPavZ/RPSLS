class Player:
    def __init__(self):
        self.score = ""
        self.gesture = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def choose_gesture(self):
        self.gesture = "" #input a gesture from a selection to play.
        return self.gesture