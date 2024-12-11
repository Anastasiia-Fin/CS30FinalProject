###############################################################################
# Title:
# Name: Anastasiia Finovska Kiera Fellinger
# Class: CS30
# Assignment: Final Project
# Version: 1.1
###############################################################################
"""
    Character class and main functions!
    
"""
###############################################################################
# Imports and Global Variables-------------------------------------------------

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


class Items:
    pass


class Storage:
    pass


def win():
    print("win")


def end():
    print("lose")


def quit():
    pass


def explore():
    pass


def chat():
    pass


def day():
    pass


def fight():
    pass


def intro():
    pass


def game():
    day = 0
    while player.status and day<21:
        print(day)
        day += 1
    if player.status == False:
        end()
    else:
        win()


# Main-------------------------------------------------------------------------
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
