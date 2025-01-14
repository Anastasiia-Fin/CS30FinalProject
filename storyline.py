###############################################################################
"""
    This module contains the storyline for the game. Every day has a
    function that with events and characters development. End, win, and
    introduction functions are also included.
"""
###############################################################################
import characters as ch
import fighting as f
import map as m

def check_chars():
    """This function checks the status of the characters in the game
    and returns a list of alive characters.
    """
    current_list = []
    # Check who is alive using the status attribute and add to local list.
    if ch.DrTucker.status:
        current_list.append(ch.DrTucker)
    if ch.Ella.status:
        current_list.append(ch.Ella)
    if ch.Mick.status:
        current_list.append(ch.Mick)
    if ch.Katie.status:
        current_list.append(ch.Katie)
    # Return list of alive characters.
    return current_list


def win():
    """ This function has the rescue message if the player wins."""
    print("The FBI has successfully rescued you, and your team."
          + " The future is uncertain, but you know your safe for now."
          + " Thank you for playing our game!")
    exit()


def end():
    """ This function ends the game, based on how the player dies. """
    # If user ran out of food and water.
    if ((ch.player.inventory.item_list["water"]["value"]==0)
        and (ch.player.inventory.item_list["food"]["value"]==0)):
        print("You tried your best to survive, but you ran out"
        + " of resources. You die from lack of nutrients.")
        exit()
    # If user ran out of water.
    elif (ch.player.inventory.item_list["water"]["value"] == 0):
        print("You have no clean source of water left."
              + " You died from dehydration.")
        exit()
    # If user ran out of food.
    elif (ch.player.inventory.item_list["food"]["value"] == 0):
        print("You have no more food left. You die from starvation.")
        exit()
    # If user was infected.
    elif ch.player.infected:
            print("The virus has spread to you."
                  + " Your brain in slowly rotting away,"
                  + " turning you into a zombie. You died from infection.")
            exit()
    else:
            print("You couldn't escape. As you stood there in fear of your"
                  + " mutated teammate, you were eaten you alive with the"
                  + " rest of your team. You died like a coward from"
                  + " cannibalization.")
            exit()


def intro():
    """ This function prints game intro."""
    print("Welcome to Survive Below, a story-driven game where you must"
          + " make the right choices to survive!\n")
    print("You're relaxing on your couch, watching TV on your day off,"
          + " when all of a sudden, breaking news pops up. A global virus" 
          + " has spread rapidly all over the world and authorities"
          + " are advising you to stay home to avoid breathing the outside"
          + " air. The virus spreads through spores from infected"
          + " individuals. Symptoms of this virus include fever, cough,"
          + " and mental disorientation. \n\nYou look outside your window"
          + " and see pure chaos on the streets. Your neighbour, Bob, has"
          + " some sort of fungus growing all over his body and is attacking"
          + " someone. You realize how serious this situation is and decide"
          + " there is only one safe place for you: a bunker. \n\nYou"
          + " stuff some water, food, and other supplies into your backpack."
          + " You cover your face with a cloth and head to your"
          + " neighbour's bunker. The bunker is owned by an old friend of"
          + " yours, working for the FBI. Katie always believed in crazy"
          + " things like the apocalypse, and now it has come true. \n\nAs"
          + " Katie welcomes you into her bunker, you see some of your other"
          + f" neighbours there. {ch.npc['katie']['description']}"
          + f" {ch.npc['dr.tucker']['description']}"
          + f" {ch.npc['ella']['description']}"
          + f" {ch.npc['mick']['description']}\n")


def day1():
    """ This function prints the first day."""
    print("It is the first day of the apocalypse. You sit isolated in the"
        + " bunker with your team. Everyone is a bit on edge. You decide to"
        + " break the ice with your team and get to know your surroundings."
        + " \n\nYou wonder what is going on in Katie's head. She always"
        + " fantasized about this situation. \n\nDr.Tucker is sitting alone"
        + " in a corner, he isn't doing so well. \n\nElla and Mick are having"
        + " a conversation, they are very chatty. \n")


def day2():
    """ This function prints the second day."""
    print("You survived another day. Everyone is trying to adapt to this new"
        + " life, but it's not easy. \n\nKatie has been acting a bit strange,"
        + " but everything seems strange during the apocalypse. She tries to"
        + " hide her cough and isolates herself. You wonder if the others"
        + " have noticed. \n\nThe rest of the group seems to be slowly"
        + " warming up to each other.")


def day3():
    """This function prints the third day. It calls the fight or run
    function based on player input. It changes Katie's status to false
    if she dies.
    """
    print("It is early in the morning when you wake up to the sound of"
        + " commotion. Katie is screaming and her skin is partially"
        + " covered in brown fungus, she suddenly turns her body towards you."
        + "\nShe charges at you and you must prepare to attack. What will"
        + " you do?\n\n")
    while True:
        choice = input("What will you do? (fight/run) ").lower()
        if choice == "fight":
            f.fight()
            break
        elif choice == "run":
            f.run()
            break
        else:
            print("That was not a valid option, pick again quick!")
    if ch.player.status:
        print("\n\nYou need to store Katie's body somewhere so that you are"
              + " not at risk for infection, but you do not want to risk"
              + " opening the bunker door and choose to use the medical room."
              + " You and your team put on layers of clothes and carry"
              + " Katie's body into the medical room. You seal the room.")
        # Kill Katie.
        ch.Katie.status = False


def day4():
    """ This function prints the fourth day."""
    print("It is quiet in the bunker after yesterday. Everyone witnessed"
        + " Katie turn into a monster and her body still lays in the medical"
        + " room. You peak into the window, seeing the rotting fungus growing"
        + " from her body and spores emitting into the air.")


def day5():
    """ This function prints the fifth day. Gives player choice to keep
    or kick Ella.
    """
    print("You wake up to coughing late in the night. You look over to see"
          + " Ella sitting straight up. Quietly you sneak to the storage room"
          + " to have a conversation with her. \n\nElla is terrified that she"
          + " has the infection but is more concerned for the sake of her"
          + " teammates. She is sick, and doesn't know what to do. \n\nElla"
          + " wants you to choose if she will stay in the bunker or if you"
          + " kick her out of the bunker.")
    while True:
        choice = input("What will you do with Ella? (keep/kick) ").lower()
        if choice == "keep":
          print("You decide to keep Ella, but moniter her closely in case she"
                + " turns.")
          break
        elif choice == "kick":
          print("You decide to kick Ella out of the bunker. You unseal the"
                + " door and she quickly slips out into the outside world."
                + " You close the bunker immediately.")
          # Kill Ella.
          ch.Ella.status = False
          break
        else:
          print("That was not a valid choice, try again.")


def day6():
    """ This function prints the sixth day. Player will die if they
    choose to kick Ella. If player keeps Ella they continue.
    """
    print("You were feeling nervous about yesterday. You had to make the"
          + " decision on what to do about Ella. It is what she wanted, but"
          + " it still left you on edge. \n\nAll of a sudden, a loud alarm"
          + " system went off in the utility room. You run in to see a hole"
          + " in the air filtration system. You have no idea how to fix it,"
          + " but if it's not fixed soon your whole team will turn into"
          + " crazed fungus zombies. \n")
    while True:
        # If Ella is dead, user become infected and dead.
        if not ch.Ella.status:
            print("You made the decision for Ella to leave the bunker, and"
                  + " now you are paying the consequences. No one knows how"
                  + " to fix the filter and you all have inhaled the spores"
                  + " by now.")
            ch.player.infected = True
            ch.player.status = False
            break
        # If Ella is alive, user makes it through air filter emergency.
        if ch.Ella.status:
            print("You thankfully made the decision to keep Ella in the"
                  + " bunker. She runs straight into the room and repairs the"
                  + " filter right away. She saved your and your teammates'"
                  + " lives. Without her you would have become zombies. You"
                  + " knew you couldn't turn your back on your fellow"
                  + " teammates.")
            break
        else:
            print("That was not a valid choice, try again.")


def day7():
    """ This function prints the seventh day."""
    print("Your team has had an eventful couple of days for being stuck in a"
          + " bunker. Everyone is trying to relax and calm their nerves."
          + " \n\nElla's sickness ended up being the flu! She is feeling a"
          + " lot better now. \n\nMick is cracking some bad jokes to lighten"
          + " the mood. \n\nDr.Tucker has warmed up more to the team.\n")
    print("Dr.Tucker was walking into the storage room when all of a sudden,"
          + " you hear a loud slam. Dr.Tucker had tripped over his foot, and"
          + " spilled a large amount of you water. You wonder if this will"
          + " affect your ability to last.\n")
    # Give user the choice to cut water. If they don't, more water
    # will be taken away and will affect the outcome of the game.
    while True:
        choice = (input("Will you ration the water more strictly"
                        + " now? (y/n) ").lower()).strip()
        if choice == "n":
            print("You decide to not cut rations.")
            # Take away water.
            ch.player.inventory.item_list["water"]["value"] -= 4
            break
        elif choice == "y":
            print("You decide to cut water to make sure you can stay alive"
                  + " for as long as possible.")
            break
        else:
            print("That was not a valid choice, please try again.")
    


def day8():
    """ This function prints the eigth day. The radio is deleted from
    inventory this day.
    """
    print("Today Ella was playing around with the radio when it picked up a"
          + " signal. You hear national breaking news. The world is being"
          + " destroyed by the infection. It is a worldwide apocalypse, but"
          + " some governments around the world are trying to save the"
          + " non-infected. \n\nThis scares your team, pushing them into an"
          + " argument on what to do next. Resources are looking low and"
          + " there is very little chance you will be found in this"
          + " underground bunker. Hope will save no one. Mick is getting into"
          + " a commotion and ends up tripping and taking the radio down with"
          + " him. Irreplaceable parts shatter into pieces. Your one"
          + " connection to the outside world is unfixable. Eveyone goes"
          + " silent. \n\nMick sits alone in the corner quiet. \n\nDr.Tucker"
          + " can't help but cry silently. \n\nElla tells you she will try"
          + " her best to fix the radio. She still has hope in the team.")
    # Delete radio from game.
    del ch.player.inventory.item_list["radio"]


def day9():
    """ This function prints the ninth day. The player looses 2
    values of food. This function calls mick fighting function.
    """
    print("Everyone went to sleep tense last night. You wake up to find Mick"
          + " locked in the supply room. Your team isn't too sure why, but"
          + " resources are sparse and you have to get Mick out of there to"
          + " make sure your supplies are safe.\n\nWith full force, all three"
          + " of you slam yourselves into the door. It busts open, almost"
          + " crushing Mick. He is screaming at you. Nothing he says is"
          + " making sense. You see the cans of empty food lying around."
          + " \n\nOut of anger you charge at Mick, attacking him.")
    # Decrease amount of food.
    ch.player.inventory.item_list["food"]["value"] -= 2
    # Fight Mick.
    f.fight_mick()
    print("You finally knocked out Mick. You wake up to Dr. Tucker fixing you"
          + " up. Mick is lying in his sleeping bag across the room. Someone"
          + " had to stop Mick, he wasn't in his right mind. \n\nMick ate a"
          + " decent amount of food supplies. You are even lower now. \n\n"
          + " Dr.Tucker's used all the medical supplies available to fix both"
          + " of you up. \n\nWith time, Mick has gone crazy. It's to be"
          + " expected when you've been stuck in a bunker for so long, but"
          + " you have to keep an eye on him. \n\nDr. Tucker and Ella have"
          + " been acting normal, but even so, can you trust them at this"
          + " point? \n\nYou rested up and took the day to sleep.")


def day10():
    """ This function prints the tenth day."""
    print("Today everyone felt more clam with each other, and the tension has"
          + " lowered. Ella had been trying some work out to keep herself"
          + " motivated when she twisted her ankle. She was unable to move it"
          + ", and was in extreme pain. After the fight, you had no more"
          + " medical equpment. \n\nUntil Dr. Tucker mentioned that he wasn't"
          + " able to get all the medical supplies out before Katie was"
          + " locked in the room. Going into the room has a chance of the"
          + " infection being spread. \n\nElla says she will try her best"
          + " to go without the medical help.")


def day11():
    """ This function prints the eleventh day. The user is given the
    option to send a character into the medical room to retrieve
    necessary supplies. If they choose someone, they will be infected.
    If they choose nobody, Ella will die.
    """
    print("Ella has a fever and her ankle has swelled up significantly."
          + " Dr. Tucker is trying to help her, but he is unable to do much"
          + " without proper medical supplies. He fears that her bone was"
          + " broken and infection has started to set in. It's up to you to"
          + " decide who should retrieve the medical supplies or do nothing."
          + " Dr. Tucker is terrified of going in, but he knows what to look"
          + " for best. Mick is also scared and says he is mentally not"
          + " recovered enough to go in. Ella is the one injured afterall,"
          + " so maybe she should get it herself. Who will you choose?")
    choices = check_chars()
    while True:
        # Print out options.
        for option in choices:
            print(f" - {option.name.title()}")
        print(" - No One")
        # Get input
        choice = (input("Who will you choose? ").lower()).strip()
        # If user picks no one, Ella dies.
        if choice == "noone":
            print("You decide to do nothing about Ella's injury and hope for"
                  + " the best. Maybe things will look better in the"
                  + " morning. \n")
            ch.Ella.status = False
            break
        chosen_person = False
        # Check if user's input is a person.
        for person in choices:
          if person.name == choice:
              chosen_person = True
              break
        if chosen_person:
            for person in choices:
                if person.name == choice:
                    # Infect the chosen person.
                    person.infected = True
                    print(f"You decide to go with {choice.title()}."
                          + f" {choice.title()} suited up with the clothes"
                          + " and materials available and got the supplies."
                          + " Dr.Tucker was able to help Ella and she has"
                          + " started showing signs of improvement.\n")
                    break
            break
        else:
            print("That was an invalid option, please try again.")


def day12():
    """ This function prints the twelfth day."""
    # If Ella was infected due to user choosing no one on day 11, let
    # user know she is dead.
    if not ch.Ella.status:
        print("Unfortuantely, Ella has suddenly passed away due to her injury"
              + ". The team is in shock at how quick the infection spread and"
              + " spirits are low. You decide to stow her body in a"
              + " compartment of the main room and hope that someone will"
              + " rescue you.")
    else:
        # Check who was infected.
        if ch.Mick.infected:
            character = ch.Mick
        elif ch.DrTucker.infected:
            character = ch.DrTucker
        elif ch.Ella.infected:
            character = ch.Ella
        else:
            character = ch.Ella
        # Let user know character is infected.
        print("Ella seemed much better last night, but unfortunately the"
              + f" DIY hazmat suit made for {character.name.title()}"
              + f" proved ineffective. {character.name.title()} has"
              + " started to act strange and by now you recognize the"
              + " symptoms of the infection. You can either kill"
              + f" {character.name.title()} or see if it's a false"
              + " alarm.\n")
        while True:
            # Ask if user wants to kill the infected character of not.
            choice = input("What will you do? (nothing/kill) ").lower()
            # If choice is to do nothing, infect player.
            if choice == "nothing":
                print("You decide to do nothing and hope for the best."
                      + " Unfortunately, the infection was not a"
                      + " false alarm...\n")
                ch.player.infected = True
                break
            # If choice is to kill character, kill off character
            elif choice == "kill":
                print("While it was a tough choice, your team agrees you"
                      + f" must kill {character.name.title()}, but you do it"
                      + " with dignity. You decide to stow"
                      + f" {character.name.title()}'s body in a compartment"
                      + " of the main room and hope that someone will rescue"
                      + " you soon.\n")
                character.status = False
                break
            else:
                print("That was an invalid option, please try again.")


def day13():
    """ This function prints the thirteenth day. User will be given
    option to ration. This will decrease their rate of survival.
    """
    print("You and your team are still processing the past few days. You"
          + " notice that your food and water are starting to get low.")
    # Give user the choice to cut rations. If they don't, more food
    # will be taken away and will affect the outcome of the game.
    while True:
        choice = input("Do you want to cut rations? (y/n) ").lower()
        if choice == "n":
            print("You decide to not cut rations.")
            # Take away rations.
            ch.player.inventory.item_list["food"]["value"] -= 3
            ch.player.inventory.item_list["water"]["value"] -= 3
            break
        elif choice == "y":
            print("You decide to cut rations and make sure you can stay"
                  + " alive for as long as possible, even if it"
                  + " means struggling.")
            break
        else:
            print("That was not a valid choice, please try again.")


def day14():
    """ This function prints the fourteenth day.
    Flashlight is deleted from player inventory"""
    characters = check_chars()
    # Pick character to break flashlight.
    character = characters[0]
    print("You wake up to some odd scratching, but think nothing of"
          + f" it. \n\n {character.name.title()} was doing an inspection of"
          + " some of your supplies and dropped the flashlight onto"
          + f" the floor. It stopped working and {character.name.title()} is"
          + " attempting to fix it. Maybe if Ella was here, she could"
          + " have helped. You also notice some odd bitemarks"
          + " on the floor...")
    # Delete flashlight from inventory.
    del ch.player.inventory.item_list["flashlight"]


def day15():
    """ This function prints the fifteenth day. The map is ruined. """
    # Pick character to ruin map.
    characters = check_chars()
    character = characters[1]
    print(f"{character.name.title()} was looking at the map while having some"
          + " canned soup and accidently spilled it. Now you can't"
          + " see anything on it, but it doesn't really matter anyway."
          + " The atmosphere got a bit more tense. You also find some"
          + " small holes around your bunker, they almost look like"
          + " they could be rat holes.")
    # Create new ruined map for user.
    m.make_map(m.ruined_map)
    # Print map for user to see new version.
    m.check_map()


def day16():
    """ This function prints the sixteenth day. Use has to fight rats,
    which can decrease more of their food.
    """
    print("You wake up to an odd squeaking sound. You get up and check"
          + " the storage room to find rats! It is an infestation."
          + " They have been slowly eating your food, and now you must"
          + " save your resources. \n\n")
    # Fight rats.
    f.fight()


def day17():
    """ This function prints the seventeenth day. Player is given the
    choice to eat a rat.
    """
    print("You left the rats in a corner of the room and the thoughts"
          + " of your diminishing supplies and growing hunger has made"
          + " you consider eating the rats. Your teammates are unsure, but"
          + " they also need to eat.\n\n")
    while True:
        # Give user option to eat rats.
        choice = input("Will you eat the rodents? (y/n) ").lower()
        if choice == "y":
            print("You decide to eat the rodents. You and your team try to"
                  + " cook the rats and dig in. You feel good about saving"
                  + " some of your food, but after a while your stomach"
                  + " starts to ache. What an interesting choice...\n")
            # Increase food by one.
            ch.player.inventory.item_list["food"]["value"] += 1
            break
        elif choice == "n":
            print("You decide to spare them. Who knows where they have been?"
                  + " You are crazy to even consider eating them.\n")
            break
        else:
            print("That was not a valid option, please try again.")


def day18():
    """ This function prints the eighteenth day. Player is able to talk
    to any alive characters.
    """
    # Print out more dialogue for alive characters.
    if ch.Ella.status:
        print("You have a conversation with Ella. She opens up to you about"
              + " her injury. She has been through a lot, but is glad that"
              + " you're leading the team to survive. She goes on to talk"
              + " about some nerdy electrician stuff. You are amazed by her"
              + " knowledge, but very lost on what she is saying.\n")
    if ch.DrTucker.status:
        print("You check up on Dr. Tucker. Times have been tough for him, but"
              + " he feels he has grown as a person and opened up"
              + " significantly. He's glad he has been able to help you and"
              + " your teammates with injuries and such. He's also happy he"
              + " has been able to sharpen his tic-tac-toe skills.\n")
    if ch.Mick.status:
        # Tell joke.
        print("Mick comes up to you and asks, 'What do you call a"
              + " flesh-eating bee?'")
        user_dialogue = input("What do you say back? ").lower()
        if user_dialogue == "zombee":
            print("Mick is impressed you got it right, good job!")
        else:
            print("'It's a zomBEE!' Mick says.'")
            print("You talk with Mick a more and he apologizes for the time"
                  + " he went a little bit crazy and ate the food. He says he"
                  + " is pretty scared and is struggling with staying in this"
                  + " bunker for so long. Mick opened up, and you learn he's"
                  + " not so bad.\n")

def day19():
    """ This function prints the nineteenth day. Player is given choice
    to eat someone. If they try to eat the player, their team will stop
    them.
    """
    print("You wake up with a stomach ache. You are starving. With decreasing"
          + " rations, the rats, and Mick's psychotic break, you are going"
          + " insane. You can't stand to just keep going with no sign of an"
          + " end to this madness. Your instincts are to survive. You must"
          + " feed your hunger somehow, or you could die trying. \n\nYou"
          + " never thought you could come to this conclusion, but maybe"
          + " eating your teammates couldn't be so bad. One person could hold"
          + " the rest of the team off for a long time. \n\nYou must make a "
          + " choice.")
    characters = check_chars()
    while True:
        choice = input("Will you kill someone to save yourself?"
                       + " (y/n) ").lower()
        if choice == "y":
            print(f"\nYou see {characters[0].name.title()} sleeping. They are"
                 + " helpless there, and you can strike at any moment. Your"
                 + " team should be grateful for increasing their chances."
                 + " You lunge at them yelling, and in a flash you are"
                 + " tackled and knocked out. \n\nYou wake up to your team"
                 + " disappointed. Trying to explain to them, they only lose"
                 + " respect for you. Why did you even consider this???")
            break
        elif choice == "n":
            print("You need to get in your right mind! Cannibalism is crazy,"
                  + " there's still some portion of food, and it would just"
                  + " be selfish to act on a crazy impulse. You just decide"
                  + " you need to eat your ration of the day sooner than"
                  + " later.")
            break
        else:
            print("That is not a choice try again!")


def day20():
    """ This function prints the twentieth day. The user gets the
    option to leave the bunker due to a knock. If they open the door,
    they will be rescued. Otherwise, they will die from lack of
    resources.
    """
    print("You wake up to a loud bang. It's coming from the bunker door and"
          + " you and your teammates look around in panic at each other. Who"
          + " could be knocking on your bunker? Who even knows about it? It"
          + " could be scavengers, someone who could help you, or maybe the"
          + " infected have gotten smarter. There is almost no food or water"
          + " in your bunker, but do you really want to risk everything?\n\n")
    while True:
        # Give user to choice to get out of bunker.
        choice = input("Do you open the door? (y/n) ").lower()
        if choice == "n":
            print("\nYou chose to not open the door. Who knows what could be"
                  + " out there? Maybe you and your teammates will find"
                  + " another way to survive. You continue living your days"
                  + " out in the bunker. You're unsure if you will ever make"
                  + " it out of here one day. You tried to lead your team to"
                  + " survival, but you have failed. After a few days,"
                  + " resources got scarce. You had nothing left. At that"
                  + " point, your teammates couldn't take the starvation, and"
                  + " ventured out of the bunker. You died alone in the"
                  + " bunker, too scared to face the outside world.")
            ch.player.status = False
            ch.player.inventory.item_list["water"]["value"] = 0
            ch.player.inventory.item_list["food"]["value"] = 0
            break
        elif choice == "y":
            print("\nYou chose to open the door. Your team works up"
                  + " the courage and unseal the door. Anything could be"
                  + " waiting on the other side. You open the door to an FBI"
                  + " agent. She introduces herself as Amirah, a close"
                  + " co-worker of Katie's. She has brought a helicopter and"
                  + " is here to save you. You all jump into saftey and fly"
                  + " off to a government compound. You are grateful for"
                  + " Katie's sacrifice and your teammates. You don't know"
                  + " what is next, but you're glad you escaped the bunker."
                  + " \n")
            break
        else:
            print("That was not a valid option, please try again.")
