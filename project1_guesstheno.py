import random
##Guess The Number Game

#feature to play as many times as one want to
playagain = True

#player score, added on after every win in the loop
#game count, added on after every game
score = 0
games = 0
while playagain:
    games += 1
    #ask for user input for the number
    user = int(input("Guess the no.? (1,2,3) "))
    print(f"You choose {user}")

    #list carrying the numbers
    choices = [1, 2, 3]

    #make the system choose a number randomly from list
    computer = random.choice(choices) 
    print(f"Computer choose {computer}\n")

    #if statements for winning and losing
    if user == computer:
        print("You guessed it correct. You win!!🥳🎉🎉\n")
        score += 1
    else:
        print("Bad luck!! Next time.🙁\n")
    print("**********\n**********\nWant to play again?😀")

    #user input for playagain
    playagain = input(" Press Y for YES\n Press N for NO\n**********\n").lower()

    if playagain == "y":
        continue
    else:
        print(f"You won {score} times out of {games} games!")
        print("Okay! Bye Bye👋")
        playagain = False