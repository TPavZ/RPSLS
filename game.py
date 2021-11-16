from human import Human
from ai_player import AI

class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None

    def create_gesture(self):
        pass

    def welcome(self):
        print("\n *** Welcome to \"Rock, Paper, Scissors, Lizzard, Spock\" The Game ***\n")
        new_game = input("Ready to begin the game? Yes or No: ").lower()
        if new_game == "yes":
            return True
        else:
            return False

    def run_game(self):
        start_game = self.welcome()
        if start_game == True:
            self.player_name()
            self.game_mode()
            self.rules()
        else:
            self.run_game()

    def rules(self):
        print(f"\nLet THE GAME BEGIN\n\n{self.player_one.name} & {self.player_two.name}\n*To play*\nEach player chooses one gesture from the list:")
        print("For each players gesture chosen;\n")
        print("Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock")
        print("\nIf the same gestures are played, round results in a tie and must be replayed immediately.")
        print("There can only be one winner per round.\nThe player who wins best out of three will be the champion.")
        print(input("\nPress ENTER to continue..."))

    def game_mode(self):
        print("\nSelect GAMEMODE\nSingle Player or Multi-Player?")
        mode = int(input("\nType \"1\" for Single Player or \"2\" for Multi-Player: "))
        if mode == 2:
            self.player_two = Human(input("Enter a name for the second player: "))
            print(f"{self.player_two.name} is player two.")
            print(input("\nPress ENTER to continue..."))
        else:
            self.player_two = AI()
            print(f"{self.player_two.name} is player two.")
            print(input("\nPress ENTER to continue..."))

    def player_name(self):
        self.player_one = Human(input("Enter a name for the first player: "))
        print(f"{self.player_one.name} is player one.")
        print(input("\nPress ENTER to continue..."))
