###############################################################################
"""
    This module contain the Rock, Paper, Scissors game.
"""
###############################################################################
import random as r

def rock_paper_scissors(opponent):
    """ This function gives the player the option to play rock, paper,
    or scissors against a given opponent. The opponent's choice is
    randomly generated. The outcome is printed to the player, along
    with what the opponent chose if relevant.
    opponent: the NPC the character is playing against.
    """
    print(f"You are playing Rock, Paper, Scissors against {opponent.title()}.")
    options = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("What would you like to choose (rock, paper, scissors): ").lower()
        # Check if user's choice is valid.
        if user_choice in options:
            # Generate opponent's random choice.
            generated_choice = r.choice(options)
            # Compare the user's and opponent's choices and print the outcome.
            if user_choice == generated_choice:
                print("You tied!")
            elif ((user_choice=="rock" and generated_choice=="scissors")
                  or (user_choice=="paper" and generated_choice=="rock")
                  or (user_choice=="scissors" and generated_choice=="paper")):
                print(f"{opponent.title()} chose {generated_choice}, you won!")
            else:
                print(f"{opponent.title()} chose {generated_choice}, you lost.")
            break
        else:
            print("That was an invalid option, please try again!")