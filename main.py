###############################################################################
# Title: Survival Bunker
# Name: Anastasiia Finovska, Kiera Fellinger
# Class: CS30
# Assignment: Final Project
# Version: 3.6
###############################################################################
"""
    This program is a text-based adventure game. The user is a survivor
    that is stuck in a bunker with NPCs and has to survive 20 days with
    varying scenarios. The user is given daily options, fighting
    opportunities, and survival problems and must make the right
    choices.
"""
###############################################################################
# Imports and Global Variables-------------------------------------------------
import RockPaperScissors as rps
import TicTacToe as ttt
import HangMan as hm
import HideAndSeek as has
import storyline as sl
import characters as ch
import fighting as f
import random as r
import map as m

# Functions--------------------------------------------------------------------
def quit():
    """ This function quits the game."""
    print("You chose to quit the game. Thanks for playing!")
    exit()


def explore():
    """ This function prints room options that the player can explore.
    If the player gives an invalid answer, they are asked to try again.
    After exploring room, player is given option to explore again.
    To explore again they must give a valid answer of y/n.
    """
    exploring = True
    while exploring:
        # Print room options.
        for option in menus["room menu"]:
            print(f" - {option.title()}")
        choice = input("Where do you want to explore? ").lower()
        # Verify user chose valid input.
        if choice in menus["room menu"]:
            menus["room menu"][choice]()
        else:
            print("That's not an option try again.")
        # Ask user if they want to explore again.
        while True:
            again = input("Do you want to explore again? (y/n) ").lower()
            if again == "y":
                break
            elif again == "n":
                exploring = False
                break
            else:
                print("Thats not an option try again.")


def chat():
    """ This function is used to chat with the NPCs in the game. """
    # Check which characters are alive.
    chars = sl.check_chars()
    while True:
        # Print list of characters.
        for person in chars:
            char_name = ch.npc[person.name]["name"]
            print(f" - {char_name.title()}")
        character = input("Who do you want to chat with? ").lower()
        # Check if user's choice is valid.
        if character in ch.npc:
            # Print a random phrase from character's dialogue list.
            print(f"{character.title()}:"
                  + f" {r.choice(ch.npc[character]['dialogue'])}")
            break
        else:
            print("That was an invalid choice.")


def pick_game():
    """ This function is used to pick a game to play with a
    random, alive character.
    """
    # Pick random, alive character to play game with.
    index = r.randrange(0, len(sl.check_chars()))
    character = sl.check_chars()[index]
    while True:
        # Print game options.
        for i, option in enumerate(menus["games"]):
            print(f" {i+1}. {option.title()}")
        choice = (input("Choose the corresponding number to play the game you"
                        + " want: ").lower()).strip()
        # Check user's choice.
        if choice == "1":
            rps.rock_paper_scissors(character.name)
            break
        elif choice == "2":
            hm.hangman()
            break
        elif choice == "3":
            ttt.tic_tac_toe(character.name)
            break
        elif choice == "4":
            has.hide_and_seek(character.name)
            break
        else:
            print("That was an invalid choice, try again!")


def next_day():
    """ This function is used to move to the next day. """
    print("Time for bed!\n")


menus = {"game options": {"explore": explore, "chat": chat,
                          "check map": m.check_map, "games": pick_game,
                          "next day": next_day, "quit": quit},
         "room menu": {"storage": m.storage, "washroom": m.washroom,
                        "utility": m.utility, "medical room": m.medical_room},
        "games": {"rock paper scissors": rps.rock_paper_scissors,
                  "hangman": hm.hangman, "tic tac toe": ttt.tic_tac_toe, 
                  "hide and seek": has.hide_and_seek}}


def day():
    """ This function gives the daily options of exploring, chatting,
    checking the map, going to the next day, playing games, or quitting
    the game.
    """
    choice = True
    while choice:
        # Give user options and ask for input
        for option in menus["game options"]:
            print(f"- {option.title()}")
        user_input = input("What would you like to do? ").lower()
        # Check if user's input is an valid and if it is, call the
        # corresponding function and break out of loop.
        if user_input.lower() in menus["game options"]:
            menus["game options"][user_input.lower()]()
            if user_input == "next day":
                choice = False
        else:
            print("That is not a valid option.")


days = {"day1": sl.day1, "day2": sl.day2, "day3": sl.day3, "day4": sl.day4,
        "day5": sl.day5, "day6": sl.day6, "day7": sl.day7, "day8": sl.day8,
        "day9": sl.day9, "day10": sl.day10, "day11": sl.day11,
        "day12": sl.day12, "day13": sl.day13, "day14": sl.day14,
        "day15": sl.day15, "day16": sl.day16, "day17": sl.day17, 
        "day18": sl.day18, "day19": sl.day19, "day20": sl.day20}


def game():
    """ This function is the main game loop. The days that pass are
    counted and the corresponding day function is called. The day
    function is called to give the user generic options to explore,
    chat, check the map, go to the next day, or quit the game. Everyday
    the water and food rations are decreased by one. If the player
    status is dead before day 20, the end function is called, otherwise
    the win function is called.
    """
    day_count = 1
    while ch.player.status and (not ch.player.infected) and day_count<20:
        # Print and call days
        print(f"{'-'*13}\nIt is day {day_count}.\n{'-'*13}\n")
        days[f"day{str(day_count)}"]()
        if ch.player.status and (not ch.player.infected):
            day()
            day_count += 1
            # Take away daily ration of food and water
            ch.player.inventory.item_list["water"]["value"] -= 1
            ch.player.inventory.item_list["food"]["value"] -= 1
            # Check if ch.player ran out of food or water
            if (ch.player.inventory.item_list["water"]["value"]==0 or
                ch.player.inventory.item_list["food"]["value"]==0):
                ch.player.status = False
    if day_count == 20 and ch.player.status:
        days[f"day{str(day_count)}"]()
    if not ch.player.status or ch.player.infected:
        sl.end()
    else:
        sl.win()


# Main-------------------------------------------------------------------------
sl.intro()
m.make_map(m.map)
game()