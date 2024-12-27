###############################################################################
# Title: Survival Bunker
# Name: Anastasiia Finovska Kiera Fellinger
# Class: CS30
# Assignment: Final Project
# Version: 3.5
###############################################################################
"""
    Character class and main functions, map and main logic, Storage
    class, chat function basic, specific dialogue, character
    descriptions, introduction, days 1-5, fight logic
"""
###############################################################################
# Imports and Global Variables-------------------------------------------------
from tabulate import tabulate
map_file = 'map.txt'
npc = {"dr.tucker": {"name": "Dr.Tucker", "role": "doctor",
                     "description": "Dr. Tucker is a shy and quiet doctor, but"
                     + " in your situation he may just come in handy.",
                      "status": True, "infected": False, 
                     "dialogue": "PLACE HOLDER"},
      "ella": {"name": "Ella", "role": "mechanic",
               "description": "Ella is a layed-back mechanic who can keep " 
               + "calm in stressfull times. She's good to have on your team.",
               "status": True, "infected": False, 
               "dialogue": "PLACE HOLDER"},
      "mick": {"name": "Mick", "role": "comedian",
                "description": "Mick is a silly comedian, cracking jokes " 
               + "at any chance he gets. He may actually help "
               + "to keep your team sane.", 
               "status": True, "infected": False,
               "dialogue": "PLACE HOLDER"},
      "katie": {"name": "Katie", "role": "FBI agent",
                "description": "Katie is a serious FBI agent. She stands "
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
                   "value": 23},
         "food": {"name": "food", 
                  "description": "You grab a can of food off the shelf. " 
                  + "Looks unappetizing.", 
                  "value": 25},
         "medical supplies": {"name": "medical supplies", 
                              "description": "You grab a med kit filled " 
                              + "with bandages, pills, and needles.", 
                              "value": True},
         "weapons": {"gun": {"description": "You hold the heavey cold gun " 
                             + "in your hand and aim.", 
                             "value": True},
                     "axe": {"description": "You pick up the axe. Holding " 
                             + "onto the wooden handled tight, as you get " 
                             + "ready to attack.", 
                             "value": True},
                     "hands": {"description": "You ball your hands up into "
                               + "fists, ready to fight.", 
                               "value": True}},
         "ammunition": {"description": "You have a small box " 
             + "of limited ammunition. Use it wisely.",
             "value": True},
         "radio": {"name": "radio", 
                   "description": "You pick up the radio. It has a bunch of "
                   + "buttons, but you're not sure how to work it.", 
                   "value": True},
         "flashlight": {"name": "flashlight", 
                        "description": "You take your flashlight. The light " 
                        + "it emits is dim, and you have no extra batteries.",
                        "value": True},
         "books": {"name": "book", 
                   "description": "A collection of how to survive the " 
                   + "apocalypse and romance novels.",
                   "value": True},
         "cards": {"name": "cards", 
                   "description": "Cards to play a game of blackjack, Go Fish "
                   + ", or whatever you would like.",
                   "value": True}
        }

map = [["Storage", "Washroom"],
       ["Main Room"],
       ["Utility", "Medical Room"]]

ruined_map = [["----------", "----------"],
       ["----------"],
       ["----------", "----------"]]

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
        print("You tried your best to survive, but you ran out " + 
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
            print("You stood there in fear of your mutated teamate. " + 
                  "She ate you alive with the rest of your team. " + 
                  "You died like a coward from cannibalization.")



def check_chars():
    current_list = []
    if DrTucker.status:
        current_list.append(DrTucker)
    if Ella.status:
        current_list.append(Ella)
    if Mick.status:
        current_list.append(Mick)
    if Katie.status:
        current_list.append(Katie)
    return current_list


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
    with open(map_file) as file:
        print(file.read())
    #print(tabulate(map, tablefmt = "fancy_grid"))


def make_map():
    """ This function creates the map in an external file. """
    with open(map_file, "w") as file:
        file.write(tabulate(map, tablefmt = "fancy_grid"))


def gun():
    print("\nYou quickly pull out the gun, aiming it at your enemy, shooting point blank. You've killed your enemy, but now have no ammunition.")
    del player.inventory.item_list["ammunition"]
    del player.inventory.item_list["weapons"]["gun"]
    del menus["weapons"]["gun"]


def axe():
    print("\nYou quickly grab the axe, swinging it at your enemy. It was a direct hit and they fall to the ground. Your axe shatters after the attack, making it unusable.")
    del player.inventory.item_list["weapons"]["axe"]
    del menus["weapons"]["axe"]


def hands():
    if Katie.status:
        print("\nYou ball your hands up into fists, ready to take on your enemy. You were unsucessful, as your hands were not the best choice of weapon.")
        player.status = False
    else:
        print("\nYou ball your hands up into fists, ready to take on your enemy. You fall on your face trying to catch the rats, but they manage to get away and eat more of your food. You scratched up your hands and cannot continue to fight with them.")
        player.inventory.item_list["food"]["value"] -= 1
        del player.inventory.item_list["weapons"]["hands"]
        del menus["weapons"]["hands"]
        fight()


def fight():
    print("Act fast and choose your weapon.")
    while True:
        for option in menus["weapons"]:
            print(f" - {option.title()}")
        choice = input("What will you pick? ").lower()
        if choice in menus["weapons"]:
            menus["weapons"][choice]()
            break
        else:
            print("That not a valid choice, choose again quickly!")


def run():
    print("You try to run, but you fail.")
    player.status = False



def intro():
    """ This function prints game intro."""
    print(f"You're relaxing on your couch, watching TV on your day off. When all of a sudden, breaking news pops up. A global virus has spread rapidly all over the world and authorities are advising you to stay home to avoid breathing the outside air. The virus spreads through spores from infected individuals. Symptoms of this virus include fever, cough, and mental disorientation. \n\nYou look outside your window and see pure chaos on the streets. Your neighbour, Bob, has some sort of fungus growing all over his body and he is attacking someone. You realize how serious this situation is and decide that there is only one safe place for you: a bunker. \n\nYou stuff some water, food, and other supplies into your backpack. You cover your face with a cloth and head over to your neighbour's bunker. The bunker is owned by an old friend of yours, working for the FBI. Katie always believed in crazy things like the apocalypse and now it has come true. \n\nAs Katie welcomes you into her bunker, you see some of your other neighbours in there. {npc['katie']['description']} {npc['dr.tucker']['description']} {npc['ella']['description']} {npc['mick']['description']}\n")


def next_day():
    print("Time for bed!\n")


def day1():
    print("It is the first day of the apocalypse. You sit isolated in the bunker with your team. Eveyone is a bit on edge. You decide to break the ice with your team and get to know your surroundings. \n\nYou wonder what is going on in Katie's head. She always fantazied about this situation. \n\nDr.Tucker is sitting alone in a corner, he isn't doing so good. \n\n Ella and Mick are having a conversation, they are very chatty. \n")


def day2():
    print("You survived another day. Everyone is trying to adapt to this new life, but it's not easy. \n\nKatie has been acting a bit strange, but everything seems strange during the apocalypse. She tries to hide her cough and isolates herself. You wonder if the others have noticed. \n\nThe rest of the group seems to be slowly warming up to each other.")


def day3():
    print("It is early in the morning when you wake up to the sound of commotion. Katie is screaming and her skin is partially covered in brown fungus, she suddenly turns her body towards you. \nShe charges at you and you have to prepare to attack. What will you do?\n\n")
    while True:
        choice = input("What will you do? (fight/run) ").lower()
        if choice == "fight":
            fight()
            break
        elif choice == "run":
            run()
            break
        else:
            print("That was not a valid option, pick again quick!")
    if player.status:
        print("\n\nYou need to store Katie's body somewhere so that you are not at risk for infection, but you do not want to risk opening the bunker door and choose to use the medical room. You and your team put on layers of clothes and carry Katie's body into the medical room.")
    Katie.status = False


def day4():
    print("It is quiet in the bunker after yesterday. Everyone witnessed Katie turn into a monster and her body still lays in the medical room. You peak into the window, seeing the rotting fungus growing from her body and spores emitting from her body.")


def day5():
    print("You wake up to coughing late in the night. You look over to see Ella sitting straight up. Quietly you sneak to the storage room to have a conversation with her. \n\nElla is terrified that she has the infection but is more concerned for the sake of her teamates. She is sick, and doesn't know what to do. \n\nElla wants you to choose, if she will stay in the bunker or kick her out of the bunker.")
    while True:
        choice = input("What will you do with Ella? (keep/kick) ").lower()
        if choice == "keep":
            print("You decide to keep Ella, but moniter her closely in case she turns.")
            break
        elif choice == "kick":
            print("You decide to kick Ella out of the bunker. You unseal the door and she quickly slips out into the outside world. You close the bunker immediately.")
            Ella.status = False
            break
        else:
            print("That was not a valid choice, try again.")


def day6():
    print("You are feeling nervous about yesterday. You had to make the decision on what to do about Ella. It is what she wanted, but it still left you on edge. \n\nAll of a sudden, a loud alarm system went off in the utility room. You run in to see a hole in the air filtration system. You have no idea how to fix it but if it's not fixed soon your whole team will turn into crazed fungus zombies. \n")
    while True:
        if not Ella.status:
            print("You made the decision for Ella to leave the bunker, and now you are paying the consequense. No one knows how to fix the filter and you all have enhaled the spores by now.")
            player.infected = True
            player.status = False
            break
        if Ella.status:
            print("You thankfully made the decision to keep Ella in the bunker. She runs straight into the room and repairs the filter right away. She saved your and your teammates' lives. Without her you would have become zombies. You knew you couldn't turn your back on your fellow teammates. ")
            break
        else:
            print("That was not a valid choice, try again.")


def day7():
    print("Your team has had an eventful couple of days for being stuck in a bunker. Everyone is trying to relax and calm theri nerves. \n\nElla's sickness ended up being the flu! She is feeling a lot better now. \n\nMick is cracking some bad jokes to lighten the mood. \n\nDr.Tucker has warmed up more to the team.")


def day8():
    print("Today Ella was playing around with the radio when it picked up a signal. You hear national breaking news. The world is being destroyed by the infection. It is a worldwide apocalypse, but some governments around the world are trying to save the non-infected. \n\nThis scares your team, pushing them into an argument on what to do next. Resources are looking low and there is very little chance you will be found in this underground bunker. Hope will save no one. Mick is getting into a commotion and ends up tripping and taking the radio down with him. Irreplaceable parts shatter into pieces. Your one connection to the outside world is unfixable. Eveyone goes silent. \n\nMick sits alone in the corner quiet. \n\nDr.Tucker can't help but cry silently. \n\nElla tells you she will try her best to fix the radio. She still has hope in the team.")
    del (player.inventory.item_list["radio"])


def day9():
    print("Everyone went to sleep tense last night. You wake up to find Mick locked in the supplies room. Your team isn't too sure why, but resources are sparse and you have to get Mick out of there to make sure your supplies are safe. \n\nWith full force, all three of you slam yourselves into the door. It busts open, almost crushing Mick. He is screaming at you. Nothing he says is making sense. You see the cans of empty food lying around. \n\nOut of anger you charge at Mick, attacking him. You both throw some solid punches until Mick is knocked out. Soon after, you pass out too. \n\nYou wake up to Dr.Tucker fixing you up. Mick is lying in his sleeping bag across the room.\n\nMick ate a decent amount of food supplies. You are even lower now. \n\nDr.Tuckers used all the medical supplies available to fix both of you up. \n\nWith time, Mick has gone crazy. It's to be expected when you've been stuck in a bunker for so long, but you have to keep an eye on him. \n\nDr.Tucker and Ella have been acting normal, but even so, can you trust them at this point?")
    player.inventory.item_list["food"]["value"] -= 2
# Story line Note: Does this need to be edited more or changed? Should we add a fight funtion #2 where you have to fight mick? (it adds more player interation)

def day10():
    print("Today everyone felt more clam with eachother, and the tension has lowered. Ella had been trying some workout to keep herself motivated when she twisted her ankle. She was unable to move it, and was in extreme pain. After the fight you had no more medical equpment. \n\nUntil Dr. Tucker mentioned that he wasn't able to get all the medical supplies out before Katie was locked in the room. Going into the room has a chance of the infection being spread. \n\nElla says she will try her best to go without the medical help.") # Problem with this is that Ella may not be in the bunker at that point (Day 5)


def day11():
    print("Ella has a fever and her ankle has swelled up significantly. Dr. Tucker is trying to help her, but he is unable to do much without proper medical supplies. He fears that her bone was broken and infection has started to set in. It's up to you to decide who should retrieve the medical supplies or do nothing. Dr. Tucker is terrified of going in, but he knows what to look for best. Mick is also scared and says he is mentally not recovered enough to go in. Ella is the one injured afterall, so maybe she should get it herself. Who will you choose?")
    choices = check_chars()
    while True:
        for option in choices:
            print(f" - {option.name}")
        print(" - No One")
        choice = input("Who will you choose? ").title()
        if choice == "No One":
            print("You decide to do nothing about Ella's injury and hope for the best. Hopefully things will look better in the morning.\n")
            Ella.status = False
            break
        chosen_person = False
        for person in choices:
            if person.name == choice:
                chosen_person = True
                break
        if chosen_person:
            for person in choices:
                if person.name == choice:
                    person.infected = True
                    print(f"You decide to go with {choice.title()}. {choice.title()} suited up with the clothes and materials available and got the supplies. Dr. Tucker was able to help Ella and she has started showing signs of improvement.\n")
                    break
            break
        else:
            print("That was an invalid option, please try again.")


def day12():
    if not Ella.status:
        print("Unfortuantely, Ella has suddenly passed away due to her injury. The team is in shock at how quick the infection spread and spirits are low. You decide to stow her body in a compartment of the main room and hope that someone will rescue you.")
    else:
        if Mick.infected:
            character = Mick
        elif DrTucker.infected:
            character = DrTucker
        elif Ella.infected:
            character = Ella
        character.status = False
        print(f"Ella seemed much better last night, but unfortunately the DIY hazmat suit made for {character.name} proved ineffective. {character.name} has started to act strange and by now you recognize the symptoms of the infection. You can either kill {character.name} or see if it's a false alarm.\n")
        while True:
            choice = input("What will you do? (nothing/kill) ").lower()
            if choice == "nothing":
                print("You decide to do nothing and hope for the best. Unfortunately, the infection was not a false alarm...\n")
                player.infected = True
                break
            elif choice == "kill":
                print(f"While it was a tough choice, your team agrees you must kill {character.name}, but you do it with dignity. You decide to stow {character.name}'s body in a compartment of the main room and hope that someone will rescue you soon.\n") # Problem with compartment
                character.status = False
                break
            else:
                print("That was an invalid option, please try again.")


def day13():
    print("You and your team are still processing the past few days. You notice that your food and water are starting to get low.")
    # Give user the choice to cut rations. If they don't, more food
    # will be taken away and will affect the outcome of the game.
    while True:
        choice = input("Do you want to cut rations? (y/n) ").lower()
        if choice == "n":
            print("You decide to not cut rations.")
            player.inventory.item_list["food"]["value"] -= 3
            player.inventory.item_list["water"]["value"] -= 3
            break
        elif choice == "y":
            print("You decide to cut rations and make sure you can stay alive for as long as possible, even if it means struggling.")
            break
        else:
            print("That was not a valid choice, please try again.")


def day14():
    print("You wake up to some odd scratching, but think nothing of it. \n\n Dr.Tucker was doing an inspection of some of your supplies and dropped the flashlight onto the floor. It stopped working and Dr.Tucker is attempting to fix it. Maybe if Ella was here, she could have helped. You also notice some odd bitemarks on the floor...") # Dr.Tucker may be out of the bunker (day 11/12)
    del (player.inventory.item_list["flashlight"])


def day15():
    print("Mick was looking at the map while having some canned soup and accidently spilled it. Now you can't see anything on it, but it doesn't really matter anyway. The atmosphere got a bit more tense. You also find some small holes around your bunker, they almost look like they could be rat holes.")
    with open(map_file, "w") as file:
        file.write(tabulate(ruined_map, tablefmt = "fancy_grid"))
    check_map()


def day16():
    print("You wake up to a odd squeaking sound. You get up and check the storage room to find rats! It is an infestation. They have been slowly eating your food, and now you must save your resources. \n\n")
    fight()


def day17():
    print("You left the rats in a corner of the room and the thoughts of your diminishing supplies and growing hunger has made you consider eating the rats. Your teammates are unsure, but they also need to eat.\n\n")
    while True:
        choice = input("Will you eat the rodents? (y/n) ").lower()
        if choice == "y":
            print("You decide to eat the rodents. You and your team try to cook the rats and dig in. You feel good about saving some of your food, but after a while your stomach starts to ache. What an interesting choice...\n")
            player.inventory.item_list["food"]["value"] += 1
            break
        elif choice == "n":
            print("You decide to spare them. Who knows where they have been? You are crazy to even consider eating them.\n")
            break
        else:
            print("That was not a valid option, please try again.")


def day18():
    if Ella.status:
        print("You have a conversation with Ella. She opens up to you abouit her injury. She has been through a lot, but is glad that you're leading the team to survival. She goes on to talk about some nerdy electrition stuff. You are amazed by her knowledge, but very lost on what she is saying.\n")
    if DrTucker.status:
        print("You check up on Dr.Tucker. Times have been tough for him, but he feels he has grown as a person and opened up significantly. He's glad he has been able to help you and your teammates with injuries and such. He's also happy he has been able to sharpen his card-playing skills and teaches you Blackjack.\n")
    if Mick.status:
        print("Mick comes up to you and asks 'What do you call a flesh-eating bee?'")
        user_dialogue = input("What do you say back? ").lower()
        if user_dialogue == "zombee":
            print("Mick is impressed you got it right, good job!")
        else:
            print("'It's a zomBEE!' Mick says.'")
        print("You talk with Mick a more and he apologizes for the time he went a little bit crazy and ate the food. He says he is pretty scared and is struggling with staying in this bunker for so long. Mick opened up, and you learn hes not so bad.\n")

def day19():
    print("You wake up with a stomach ache. You are starving. With decreasing rations, the rats, and Mick's psychotic break, you are going insane. You can't stand to just keep going with no sign of an end to this madness. Your instincts are to survive. You must feed your hunger somehow, or you could die trying. \n\nYou never thought you could come to this conclusion, but maybe eating your teamates couldn't be so bad. One person could hold the rest of the team off for a long time. \n\nYou must make a choice.")
    characters = check_chars()
    while True:
        choice = input("Will you kill a teamate to save yourself? (y/n) ").lower()
        if choice == "y":
            print(f"You see {characters[0].name} sleeping. They are helpless there and you can strike at any momnet. Your team shall be truely grateful your act of providing. You lunge at them yelling, and in a flash you are tackled and knocked out. \n\nYou wake up to your team dissapointed. Trying to explain to them, they only lose respect for you. Why did you even consider this???")
            break
        elif choice == "n":
            print("You need to get in your right mind! cannabalism is crazy, theres still some portion of food, and it would just be selfish to act on a crazy impulse. You just decide you need to eat your ration of the day sooner than later.")
            break
        else:
            print("That is not a choice try again!")


def day20():
    print("You wake up to a loud bang. It's coming frmom the bunker door and you and your teammates look around in panic at each other. Who could be knocking on your bunker? Who even knows about it? It could be scavengers, someone who could help you, or maybe the infected have gotten smarter. There is almost no food or water in your bunker, but do you really want to risk everything?\n\n")
    while True:
        choice = input("Do you open the door? (y/n) ").lower()
        if choice == "n":
            print("You chose to not open the door. Who knows what could be out there? Maybe you and your teammates will find another way to survive. You continue living your days out in the bunker. You're unsure if you would ever make it out of here one day. You tried to lead your team to survival, but you have failed. After a few days, resources got scarce. You had nothing left. At that point your teammates couldn't take the starvation, and ventured out of the bunker. You died alone in the bunker, too scared to face the outside world.")
            player.status = False
            player.inventory.item_list["water"]["value"] = 0
            player.inventory.item_list["food"]["value"] = 0
            break
        elif choice == "y":
            print("You chose to open the door. You and your teammates work up the courage and unseal the door. Anything could be waiting on the other side. You open the door to an FBI agent. She introduces herself as Amirah, a close co-worker of Katie's. She has brought a hellicopter and is here to save you. You all jump into saftey and fly off to a government compound. You are grateful for Katie's sacrafice and your teammates. You don't know what is next, but you glad you escaped the bunker. \n")
            break
        else:
            print("That was not a valid option, please try again.")


menus = {"game options": {"explore": explore, "chat": chat,
                        "check map": check_map, "next day": next_day, 
                        "quit": quit},
         "room menu": {"storage": storage, "washroom": washroom,
                        "utility": utility, "medical room": medical_room},
        "fight": {"fight": fight, "run": run},
        "weapons" : {"gun": gun, "axe": axe, "hands": hands}}


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
    while player.status and (not player.infected) and day_count<20:
        # Print and call days
        print(f"-----------------------\nIt is day {day_count}.\n-----------------------\n")
        days[f"day{str(day_count)}"]()
        if player.status and (not player.infected):
            day()
            day_count += 1
            # Take away daily ration of food and water
            player.inventory.item_list["water"]["value"] -= 1
            player.inventory.item_list["food"]["value"] -= 1
            # Check if player ran out of food or water
            if (player.inventory.item_list["water"]["value"]==0 or
                player.inventory.item_list["food"]["value"]==0):
                player.status = False
    if day_count == 20 and player.status:
        days[f"day{str(day_count)}"]()
    if not player.status or player.infected:
        end()
    else:
        win()


# Main-------------------------------------------------------------------------
intro()
make_map()
# Create storage
player_items = Storage(items)
# Create characters
player = Character("Bob", "player", "description", True, False, player_items)
DrTucker = Character(npc["dr.tucker"]["name"], npc["dr.tucker"]["role"],
                     npc["dr.tucker"]["description"],
                     npc["dr.tucker"]["status"], npc["dr.tucker"]["infected"],
                     None)
Ella = Character(npc["ella"]["name"], npc["ella"]["role"],
                 npc["ella"]["description"], npc["ella"]["status"],
                 npc["ella"]["infected"], None)
Mick = Character(npc["mick"]["name"], npc["mick"]["role"],
                 npc["mick"]["description"], npc["mick"]["status"],
                 npc["mick"]["infected"], None)
Katie = Character(npc["katie"]["name"], npc["katie"]["role"],
                  npc["katie"]["description"], npc["katie"]["status"],
                  npc["katie"]["infected"], None)
game()