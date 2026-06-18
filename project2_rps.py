import random
import sys


def play_rps():
    #list consisting the options
    choices = ["R", "P", "S"]

    playagain = True

    while playagain:
    #user input with verification
        player = input("Choose from R, P, S for Rock🪨, Paper📄, Scissors✂️! ").upper()
        if player not in choices:
            sys.exit("choose correct attack")
        else:
            print(f"You choose {player}")


    #system random choice
        computer = random.choice(choices)
        print(f"Computer choose {computer}")


    #if statements for wining losing
        if player == computer:
            print("It's a tie! Same attack!")
        elif player == "R" and computer == "S":
            print("You win!")
        elif player == "P" and computer == "R":
            print("You win!")
        elif player == "S" and computer == "P":
            print("You win!")
        else:
            print("You lose! Can't beat the Computer!")

    #play again option
        print("\nPlay again?")
        user = input("Y for YES\nQ for QUIT ").upper()
        if user.upper() == "Y":
            return play_rps()
        else:
            print("Thank you for playing!!🎉")
            playagain = False

if __name__ == "__main__":
    play_rps()