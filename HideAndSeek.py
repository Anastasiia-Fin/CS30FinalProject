###############################################################################
"""
    This module contains the Hide and Seek game.
"""
###############################################################################
import random as r
import characters as ch

map = ["storage", "washroom", "main room", "utility", "medical room"]

def hide_and_seek(opponent):
    '''This function plays the hide and seek game.
    opponent is the character the player is against.'''
    print(f"\nYou are playing Hide and Seek against {opponent.title()}! In 2"
          + " or less guesses, you must find what room they are hiding in! \n")
    # Check if medical room is sealed or not and adjust room options if needed.
    if ch.Katie.status:
        rooms = map
    else:
        map.remove("medical room")
        rooms = map
    # Establish 2 chances to guess
    chances = 2
    # Pick random room
    hiding_room = r.choice(rooms)
    # As long as chances are greater than 0, keep playing.
    while chances >= 0:
        # Losing statement.
        if chances < 1:
            print(f"You lost, {opponent.title()} was hiding in"
                  f" {hiding_room.title()}!")
            break
        # Print options.
        for option in rooms:
            print(f" - {option.title()}")
        # Get input
        checking = input("Where do you want to search? ").lower()
        # Check if their choice is valid.
        if checking in rooms:
            # Check if their choice is the same as the hiding room.
            if checking == hiding_room:
                print(f"\nYou found {opponent.title()} in"
                      + f" {checking.title()}!\n")
                break
            # Choice was wrong, so they have one less chance.
            else:
                print(f"\n{opponent.title()} was not in {checking.title()}.")
                # Remove guessed room from options.
                rooms.remove(checking)
                chances -= 1
        else:
            print("\nThat is not a valid option, try again!")