import random
from words import words
from hangman_character import hangman_charc_visual



def hangman():
    #generating a random word
    word = random.choice(words).upper()

    word_letters = set(word)   #letters in the word
    used_letters = set()       #what user has guessed
    

    # Asthetics of game
    print("\n\n|| THE HANGMAN GAME || \n\nLet's Begin!!\n\n")

    lives = 7

    while len(word_letters) != 0 and lives != 0:
        print(f"You have {lives} lives and you have used these letters:", " ".join(used_letters))
        
        #the current word with correct guesses (- - a - e)
        list = [letter if letter in used_letters else "-" for letter in word]

        print(hangman_charc_visual[lives])       #hangman character according to lives left
        print("\nCurrent word: ", " ".join(list))

        #ask user for an alphabet to guess
        user_letter = input("Guess the letter: ").upper()
        

    #statement to check the user alphabet in the word_letters
        if user_letter in word_letters:
            print("Correct!!✅\n\n")
            word_letters.remove(user_letter)
            
        
        elif user_letter in used_letters:
            print("You have already used that letter.\n\n")

        else:
            lives -= 1  #removes a life for wrong guess
            print(f"Incorrect!! Your letter {user_letter} is not in the word.\n\n")

        used_letters.add(user_letter)

    # conditions for end of while loop 
    if lives == 0:
        print(hangman_charc_visual[lives])   
        print(f"Sorry! You died.🙁 The word was {word}.")
    if len(word_letters) == 0:
        print(f"Yeah!! You WON!! Guessed it like a pro!🥳 \n{word}")

    print("\n##########\nPlay again?")

    # play again loop 
    while True:
        playagain = input("\nY for Yes or \nQ to Quit\n##########\n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return hangman()
    else:
        print("\n 🎉🎉🎉🎉")
        print("ThankYou for playing!\n")
        


if __name__ == "__main__":
    hangman()


 