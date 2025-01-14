###############################################################################
"""
    This module contains the hangman game.
"""
###############################################################################
import random as r
words = ["bunker", "survival", "biography", "auction", "dress", "prescription",
         "depressed", "surprise", "broccoli", "warning", "zombie",
         "preparation", "dance", "decide", "soldier", "government",
         "understand", "humanity", "question", "authority", "education",
         "company", "horoscope", "terminal", "python"]

hangman_pic = [" ----------\n   |     |\n   |\n   |\n   |\n   |\n   |\n   |\n"
               + " ----------",
               " ----------\n   |     |\n   |     O\n   |\n   |\n   |\n   "
               + "|\n   |\n ----------",
               " ----------\n   |     |\n   |     O\n   |     |\n   |\n   "
               + "|\n   |\n   |\n ----------",
               " ----------\n   |     |\n   |     O\n   |    /|\n   |\n   "
               + "|\n   |\n   |\n ----------",
               " ----------\n   |     |\n   |     O\n   |    /|\ \n   |\n   "
               +"|\n   |\n   |\n ----------",
               " ----------\n   |     |\n   |     O\n   |    /|\ \n   |     "
               + "|\n   |\n   |\n   |\n ----------",
               " ----------\n   |     |\n   |     O\n   |    /|\ \n   |     "
               + "|\n   |    /\n   |\n   |\n ----------",
               " ----------\n   |     |\n   |     O\n   |    /|\ \n   |     "
               + "|\n   |    / \ \n   |\n   |\n ----------"]

def hangman():
    """ This function contains the hangman game. It contains a list of
    the alphabet, a list of the available letters, and a lives variable
    that keeps track of the user's mistakes (max of 7). A random word
    is chosen from the list of words, and the user is asked to guess a
    letter, word, or quit the game. A picture of the hangman diagram is
    printed each time a mistake is made with a new body part being
    added each time.
    """
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                "y", "z"]
    # Letters that the player has not used.
    letters_remaining = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                         "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                         "u", "v", "w", "x", "y", "z"]
    # Pick a random word from list.
    word = r.choice(words)
    lives = 7
    # Create a list of underscores to represent the word.
    printed_word = list("_"*len(word))
    # List of options user can choose.
    options = ["word", "letter", "quit"]
    # Instructions
    print("\nWelcome to Hangman! You have 7 lives to guess the word."
         + " You can guess the word, letter, or quit. Making a mistakes does"
         + " not take away a life. Enjoy!\n")
    print(f'{" ".join(printed_word)}\n')
    while lives>0 and ("".join(printed_word) != word):
        # Print options.
        for option in options:
            print(f"- {option.title()}")
        user_choice = (input("What would you like to"
                             + " guess/do: ").lower()).strip()
        if user_choice == "word":
            user_word = (input("What is your guess for"
                               + " the word: ").lower()).strip()
            # Check if user guessed the word correctly
            if user_word == word:
                print("Great job, you guessed the word correctly!")
                break
            else:
                # Take away life and print hangman diagram.
                print("That was an incorrect guess.")
                lives -= 1
                print(hangman_pic[7-lives])
                # Print the word with the underscore and letters.
                print(" ".join(printed_word))
                print(f"{lives} mistake(s) remaining.\n")
        elif user_choice == "letter":
            user_letter = (str(input("Pick a letter"
                                     + f"({', '.join(letters_remaining)}):"
                                     + " ")).lower()).strip()
            if user_letter in letters_remaining:
                # Take away letter from list of letters remaining.
                letters_remaining.remove(user_letter)
                if user_letter in word:
                    # Check if letter is in word and replace underscore.
                    for i, char in enumerate(word):
                        if user_letter == char:
                            printed_word[i] = user_letter
                    # Print the word with the underscore and letters.
                    print(" ".join(printed_word))
                    # Check if the word has been guessed by gussing letters.
                    if "".join(printed_word) == word:
                        print("Good job, you guessed the word correctly!")
                else:
                    # Take away life and print hangman diagram.
                    print("Not in word.")
                    lives -= 1
                    print(hangman_pic[7-lives])
                    # Print the word with the underscore and letters.
                    print(" ".join(printed_word))
                    print(f"\n{lives} mistake(s) remaining.\n")
            # Check if user has already guessed the letter.
            elif user_letter in alphabet:
                print("You already guessed that letter, try another one!")
            else:
                print("That was an invalid option, please try again!")
        elif user_choice == "quit":
            print("You've chosen to quit the game.")
            break
        else:
            print("That was an invalid choice, please try again!")
    # Check if player did not guess the word.
    if lives == 0:
        print(f"The word was '{word}', better luck next time!")
