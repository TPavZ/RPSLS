print("\n *** Welcome to \"Rock, Paper, Scissors, Lizzard, Spock\" The Game ***\n")
start_new = input("Ready to begin the game? Yes or No: ").lower

print("\nLet THE GAME BEGIN\n\n*To play*\nEach player chooses one gesture from the list:")
print("For each players gesture chosen;\n")
print("Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock")
print("\nIf the same gestures are played, round results in a tie and must be replayed immediately.")
print("There can only be one winner per round.\nThe player who wins best out of three will be the champion.")
print(input("\nPress ENTER to continue..."))

print("Select GAMEMODE\nSingle Player or Multi-Player")
mode = int(input("\nType \"1\" for Single Player or \"2\" for Multi-Player: ")
if mode == 1:
    player1 = "human"
    #self.player_two = Human()
else:
    player1 = "AI"
    #self.player_two = AI()
print({player1})