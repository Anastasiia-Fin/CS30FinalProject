###############################################################################
# Title: Survival Bunker
# Name: Anastasiia Finovska Kiera Fellinger
# Class: CS30
# Assignment: Final Project
# Version: 2.2
###############################################################################
"""
    Character class and main functions, map and main logic, Storage
    class, chat function basic, specific dialogue and character
    descriptions.
"""
###############################################################################
# Imports and Global Variables-------------------------------------------------
from tabulate import tabulate
map_file = 'map.txt'
npc = {"dr.tucker": {"name": "Dr.Tucker", "role": "doctor",
                     "description": "Dr. Tucker is a shy and quiet guy, but"
                     + " in your situation he may just come in handy.",
                      "status": True, "infected": False, 
                     "dialogue": "PLACE HOLDER"},
      "ella": {"name": "Ella", "role": "mechanic",
               "description": "Ella is a layed-back person, who can keep " 
               + "calm in stressfull times. She's good to have on your team.",
               "status": True, "infected": False, 
               "dialogue": "PLACE HOLDER"},
      "mick": {"name": "Mick", "role": "comedian",
                "description": "Mick is a silly dude, cracking jokes " 
               + "at any chance he gets. He may actually help "
               + "to keep your team sane.", 
               "status": True, "infected": False,
               "dialogue": "PLACE HOLDER"},
      "katie": {"name": "Katie", "role": "FBI agent",
                "description": "Katie is a serious character. She stands "
                + "on buisness and is prepared to survive.", 
                "status": True, "infected": False, 
                "dialogue": "PLACE HOLDER"}
      }

rooms = {"storage": {"description": "You walk into the small storage "
                     + "closet. It's filled wall to wall with shelves."},
         "washroom": {"description": "The washroom is cramped, but at "
                      + "least you have one."},
         "utility": {"description": "There are wires and filters filling the "
                     + "whole room. You don't know much about elecrical "
                     + "stuff."},
         "medical room": {"description": "The room has a small desk with "
                          + "chairs. A cabinate sits on the wall with limited "
                          + "resources."}}

items = {"water": {"name": "water", 
                   "description": "You pick up a bottle of water. " 
                   + "Super refreshing.", 
                   "value": 3},
         "food": {"name": "food", 
                  "description": "You grab a can of food off the shelf. " 
                  + "Looks unappetizing.", 
                  "value": 20},
         "medical supplies": {"name": "medical supplies", 
                              "description": "You grab a med kit filled " 
                              + "with bandages, pills, and needles.", 
                              "value": True},
         "weapons": {"gun": {"description": "You hold the heavey cold gun " 
                             + "in your hand and aim.", 
                             "value": True},
                     "ammunition": {"description": "You have a small box " 
                                    + "of limited ammunition. Use it wisely.",
                                    "value": True},
                     "axe": {"description": "You pick up the axe. Holding " 
                             + "onto the wooden handled tight, as you get " 
                             + "ready to attack.", 
                             "value": True},
                     "hands": {"description": "You ball your hands up into "
                               + "fists, ready to fight.", 
                               "value": True}},
         "radio": {"name": "radio", 
                   "description": "You pick up the radio. It has a bunch of "
                   + "buttons, but you're not sure how to work it.", 
                   "value": True},
         "flashlight": {"name": "flashlight", 
                        "description": "You take your flashlight. The light " 
                        + "it emits is dim, and you have no extra batteries.",
                        "value": True}}

map = [["Storage", "Washroom"],
       ["Main Room"],
       ["Utility", "Medical Room"]]

# Functions--------------------------------------------------------------------
class Character:
    """ This class creates characters using passed values.
    name = name of character.
    role = role of character.
    description = description of character.
    status = status of character.
    infected = status of whether character is infected or helathy.
    inventory = inventory of character.
    """
    def __init__(self, name, role, description, status, infected, inventory):
        self.name = name
        self.role = role
        self.description = description
        self.status = status
        self.infected = infected
        self.inventory = inventory

    def __str__(self):
        message1 = f"Attributes: {self.name}, {self.role}, {self.description},"
        message2 = f" {self.status}, {self.infected}, {self.inventory}"
        return message1 + message2

    def add_item(self, item):
        """ This method adds an item to the inventory of the character.
        item = item to be added to inventory.
        """
        self.inventory.append(item)

    def destroy_item(self, item):
        """ This method removes an item from the inventory of the
        character.
        item = item to be removed from inventory.
        """
        self.inventory.remove(item)


class Storage:
    """ This class is the inventory of the game items the character
    has/picks up.
    item_list: list of items.
    """
    def __init__(self, item_list):
        self.item_list = item_list


def win():
    """ This function has the rescue message if the player wins. """
    print("The FBI has sucessfully rescued you, and your team."
          + "The furture is uncertain, but you know your safe for now."
          + "Thank you for playing our game!")
    exit()


def end():
    """ This function ends the game, based on how the
    player dies.
    """
    if ((player.inventory.item_list["water"]["value"]==0)
        and (player.inventory.item_list["food"]["value"]==0)):
        print("You tired your best to survive, but you ran out" + 
              "of resources. You die from lack of nutrients.")
        exit()
    elif (player.inventory.item_list["water"]["value"] == 0):
        print("You have no clean source of water left." + 
              "You died from dehydration.")
        exit()
    elif (player.inventory.item_list["food"]["value"] == 0):
        print("You have no more food left. You die from starvation.")
        exit()
    elif player.infected:
            print("The virus has spread to you." + 
                  "Your brain in slowly rotting away," + 
                  "turning you into a zombie. You died from infection.")
            exit()
    else:
            print("You stood there in fear of your mutated teamate." + 
                  "She ate you alive with the rest of your team." + 
                  "You died like a coward from cannibalization.")
    
        
    


def quit():
    """ This function quits the game."""
    print("You chose to quit the game. Thanks for playing!")
    exit()


def storage():
    """ This function calls the storage description in the rooms
    dictionary.
    """
    print(f"Storage: {rooms['storage']['description']}")


def washroom():
    """ This function calls the washroom description in the rooms
    dictionary.
    """
    print(f"Washroom: {rooms['washroom']['description']}")


def utility():
    """ This function calls the utility description in the rooms
    dictionary.
    """
    print(f"Utility: {rooms['utility']['description']}")

    
def medical_room():
    """ This function calls the medical room description in the rooms
    dictionary.
    """
    print(f"Medical Room: {rooms['medical room']['description']}")


def explore():
    """ This function prints room options that the player can explore.
    If the player gives an invalid answer, they are asked to try again.
    After exploring room, player is given option to explore again.
    To explore again they must give a valid answer of y/n.
    """
    exploring = True
    while exploring:
        for option in menus["room menu"]:
            print(f" - {option.title()}")
        choice = input("Where do you want to explore? ").lower()
        if choice in menus["room menu"]:
            menus["room menu"][choice]()
        else:
            print("That's not an option try again.")
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
    while True:
        for person in npc:
            print(f" - {npc[person]['name']}")
        choice = input("Who do you want to chat with? ").lower()
        if choice in npc:
            print(f"{npc[choice]['dialogue']}")
            break
        else:
            print("That was an invalid choice.")
    

def check_map():
    """ This function prints the map from an external file. """
    print(tabulate(map, tablefmt = "fancy_grid"))


def make_map():
    """ This function creates the map in an external file. """
    with open(map_file, "w") as file:
        file.write(tabulate(map, tablefmt = "fancy_grid"))


def fight():
    print("You are fighting.")


def intro():
    """ This function prints game intro."""
    print("You're in a bunker with some people.")


def next_day():
    print("Time for bed!")


def day1():
    print(1)


def day2():
    print(2)


def day3():
    print(3)


def day4():
    print(4)


def day5():
    print(5)


def day6():
    print(6)


def day7():
    print(7)


def day8():
    print(8)


def day9():
    print(9)


def day10():
    print(10)


def day11():
    print(11)


def day12():
    print(12)


def day13():
    print(13)


def day14():
    print(14)


def day15():
    print(15)


def day16():
    print(16)


def day17():
    print(17)


def day18():
    print(18)


def day19():
    print(19)


def day20():
    print(20)


menus = {"game options": {"explore": explore, "chat": chat,
                        "check map": check_map, "next day": next_day, 
                        "quit": quit},
         "room menu": {"storage": storage, "washroom": washroom,
                        "utility": utility, "medical room": medical_room}}


def day():
    """ This function gives the daily options of exploring, chatting,
    checking the map, going to the next day, or quitting the game to
    the user.
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
    
days = {"day1": day1, "day2": day2, "day3": day3, "day4": day4, "day5": day5,
        "day6": day6, "day7": day7, "day8": day8, "day9": day9, "day10": day10,
        "day11": day11, "day12": day12, "day13": day13, "day14": day14,
        "day15": day15, "day16": day16, "day17": day17, "day18": day18,
        "day19": day19, "day20": day20}

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
    while player.status and day_count<21:
        # Print and call days
        print(f"It is day {day_count}.")
        days[f"day{str(day_count)}"]()
        day()
        day_count += 1
        # Take away daily ration of food and water
        player.inventory.item_list["water"]["value"] -= 1
        player.inventory.item_list["food"]["value"] -= 1
        # Check if player ran out of food or water
        if (player.inventory.item_list["water"]["value"]==0 or
            player.inventory.item_list["food"]["value"]==0):
            player.status = False
    if not player.status:
        end()
    else:
        win()


# Main-------------------------------------------------------------------------
make_map()
# Create storage
player_items = Storage(items)
# Create characters
player = Character("Bob", "player", "description", True, False, player_items)
DrTucker = Character(npc["dr.tucker"]["name"], npc["dr.tucker"]["role"],
                     npc["dr.tucker"]["description"],
                     npc["dr.tucker"]["status"], npc["dr.tucker"]["infected"],
                     None)
print(DrTucker)
Ella = Character(npc["ella"]["name"], npc["ella"]["role"],
                 npc["ella"]["description"], npc["ella"]["status"],
                 npc["ella"]["infected"], None)
print(Ella)
Mick = Character(npc["mick"]["name"], npc["mick"]["role"],
                 npc["mick"]["description"], npc["mick"]["status"],
                 npc["mick"]["infected"], None)
print(Mick)
Katie = Character(npc["katie"]["name"], npc["katie"]["role"],
                  npc["katie"]["description"], npc["katie"]["status"],
                  npc["katie"]["infected"], None)
print(Katie)
game()