###############################################################################
# Title: Survival Bunker
# Name: Anastasiia Finovska Kiera Fellinger
# Class: CS30
# Assignment: Final Project
# Version: 1.3
###############################################################################
"""
    Character class and main functions, map and main logic, Storage class
"""
###############################################################################
# Imports and Global Variables-------------------------------------------------
from tabulate import tabulate
map_file = 'map.txt'
npc = {"dr.tucker": {"name": "Dr.Tucker", "role": "doctor",
                      "description": "PLACE HOLDER", 
                      "status": True, "infected": False, 
                     "dialogue": "PLACE HOLDER"},
      "ella": {"name": "Ella", "role": "mechanic",
                "description": "PLACE HOLDER", 
               "status": True, "infected": False, 
               "dialogue": "PLACE HOLDER"},
      "mick": {"name": "Mick", "role": "comedian",
                "description": "PLACE HOLDER", 
               "status": True, "infected": False,
               "dialogue": "PLACE HOLDER"},
      "katie": {"name": "Katie", "role": "FBI agent",
                 "description": "PLACE HOLDER", 
                "status": True, "infected": False, 
                "dialogue": "PLACE HOLDER"}
      }

rooms = {"storage": {"description": "PLACE HOLDER"},
        "washroom": {"description": "PLACE HOLDER"},
        "utility": {"description": "PLACE HOLDER"},
        "medical room": {"description": "PLACE HOLDER"}}

items = {"water": {"name": "water", "description": "PLACE HOLDER", "value": 3},
         "food": {"name": "food", "description": "PLACE HOLDER", "value": 20},
         "medical supplies": {"name": "medical_supplies", "description": "PLACE HOLDER", "value": True},
         "weapons": {"gun": {"description": "PLACE HOLDER", "value": True},
                     "ammunition": {"description": "PLACE HOLDER", "value": True},
                     "axe": {"description": "PLACE HOLDER", "value": True},
                     "hands": {"description": "PLACE HOLDER", "value": True}},
         "radio": {"name": "radio", "description": "PLACE HOLDER", "value": True},
         "flashlight": {"name": "flashlight", "description": "PLACE HOLDER", "value": True}}

map = [["Storage", "Washroom"],
       ["Main Room"],
       ["Utility", "Medical Room"]]

# Functions--------------------------------------------------------------------
class Character:

    def __init__(self, name, role, description, status, infected, inventory):
        self.name = name
        self.role = role
        self.description = description
        self.status = status
        self.infected = infected
        self.inventory = inventory

    def __str__(self):
        message = (f"Attributes: {self.name}, {self.role}, {self.description},{self.status}, {self.infected}, {self.inventory}")
        return message

    def add_item(self, item):
        self.inventory.append(item)

    def destroy_item(self, item):
        self.inventory.remove(item)


class Storage:

    def __init__(self, item_list):
        self.item_list = item_list


def win():
    print("The FBI has sucessfully rescued you, and your team." + 
          "The furture is uncertain, but you know your safe for now." + 
          "Thank you for playing our game!")
    exit()


def end():
    if (player.inventory.item_list["water"]["value"] == 0) and (player.inventory.item_list["food"]["value"] == 0):
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
    elif player.infected == True:
            print("The virus has spread to you." + 
                  "Your brain in slowly rotting away," + 
                  "turning you into a zombie. You died from infection.")
            exit()
    else:
            print("You stood there in fear of your mutated teamate." + 
                  "She ate you alive with the rest of your team." + 
                  "You died like a coward from cannibalization.")
    
        
    


def quit():
    print("You chose to quit the game. Thanks for playing!")
    exit()


def storage():
    print(f"Storage: {rooms['storage']['description']}")


def washroom():
    print(f"Washroom: {rooms['washroom']['description']}")


def utility():
    print(f"Utility: {rooms['utility']['description']}")

    
def medical_room():
    print(f"Medical Room: {rooms['medical room']['description']}")


def explore():
    exploring = True
    while exploring:
        for option in menus["room menu"]:
            print(f" - {option.title()}")
        choice = input("Where do you want to explore? ").lower()
        if choice in menus["room menu"]:
            menus["room menu"][choice]()
        else:
            print("Thats not an option try again.")
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
       "day11": day11, "day12": day12, "day13": day13, "day14": day14, "day15": day15,
       "day16": day16, "day17": day17, "day18": day18, "day19": day19, "day20": day20}

def game():
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
