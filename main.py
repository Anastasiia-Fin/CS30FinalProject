###############################################################################
# Title: Survival Bunker
# Name: Anastasiia Finovska Kiera Fellinger
# Class: CS30
# Assignment: Final Project
# Version: 1.2
###############################################################################
"""
    Character class and main functions, map and main logic
"""
###############################################################################
# Imports and Global Variables-------------------------------------------------
from tabulate import tabulate
map_file = 'map.txt'
npc = {"Dr.Tucker": {"name": "Dr. Tucker", "role": "doctor",
                      "description": "PLACE HOLDER", 
                      "status": True, "infected": False},
      "Ella": {"name": "Ella", "role": "mechanic",
                "description": "PLACE HOLDER", 
               "status": True, "infected": False},
      "Mick": {"name": "Mick", "role": "comedian",
                "description": "PLACE HOLDER", 
               "status": True, "infected": False},
      "Katie": {"name": "Katie", "role": "FBI agent",
                 "description": "PLACE HOLDER", 
                "status": True, "infected": False}
      }

rooms = {"storage": {"description": "PLACE HOLDER"},
        "washroom": {"description": "PLACE HOLDER"},
        "utility": {"description": "PLACE HOLDER"},
        "medical room": {"description": "PLACE HOLDER"}}

map = [["Storage", "Washroom"],
       ["Main Room"],
       ["Utility", "Medical Room"]]

# Functions--------------------------------------------------------------------
class Character:

    def __init__(self, name, role, description, status, infected):
        self.name = name
        self.role = role
        self.description = description
        self.status = status
        self.infected = infected

    def __str__(self):
        message = f"Attributes: {self.name}, {self.role}, {self.description}, {self.status}, {self.infected}."
        return message


class Item:

    def __init__(self):
        pass

class Storage:

    def __init__(self):
        pass

class Items:
    pass


class Storage:
    pass


def win():
    print("You win!")


def end():
    print("You lose!")


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
    print("You talked with your bunker mates")


def check_map():
    print(tabulate(map, tablefmt = "fancy_grid"))


def make_map():
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
    choice = True
    while choice:
        for option in menus["game options"]:
            print(f"- {option.title()}")
        user_input = input("What would you like to do? ").lower()
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
        print(f"It is day {day_count}.")
        days[f"day{str(day_count)}"]()
        day()
        day_count += 1
    if player.status == False:
        end()
    else:
        win()


# Main-------------------------------------------------------------------------
make_map()
player = Character("Bob", "player", "description", True, False)
print(player)
DrTucker = Character(npc["Dr.Tucker"]["name"], npc["Dr.Tucker"]["role"], npc["Dr.Tucker"]["description"], npc["Dr.Tucker"]["status"], npc["Dr.Tucker"]["infected"])
print(DrTucker)
Ella = Character(npc["Ella"]["name"], npc["Ella"]["role"], npc["Ella"]["description"], npc["Ella"]["status"], npc["Ella"]["infected"])
print(Ella)
Mick = Character(npc["Mick"]["name"], npc["Mick"]["role"], npc["Mick"]["description"], npc["Mick"]["status"], npc["Mick"]["infected"])
print(Mick)
Katie = Character(npc["Katie"]["name"], npc["Katie"]["role"], npc["Katie"]["description"], npc["Katie"]["status"], npc["Katie"]["infected"])
print(Katie)
game()
