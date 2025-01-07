###############################################################################
"""
    This module contains the fighting functions and menus for the game.
"""
###############################################################################
import characters as ch

def gun():
    """ This function is used to fight with a gun. """
    print("\nYou quickly pull out the gun, aiming it at your enemy, shooting"
          + " point blank. You've killed your enemy, but now have no"
          + " ammunition.")
    # Delete items used from player's inventory and menu.
    del ch.player.inventory.item_list["ammunition"]
    del ch.player.inventory.item_list["weapons"]["gun"]
    del fight_menus["weapons"]["gun"]


def axe():
    """ This function is used to fight with an axe."""
    print("\nYou quickly grab the axe, swinging it at your enemy. It was a"
          + " direct hit and they fall to the ground. Your axe shatters after"
          +" the attack, making it unusable.")
    # Delete items used from player's inventory and menu.
    del ch.player.inventory.item_list["weapons"]["axe"]
    del fight_menus["weapons"]["axe"]


def hands():
    """ This function is used to fight with hands."""
    # What happens if Katie is still alive.
    if ch.Katie.status:
        print("\nYou ball your hands up into fists, ready to take on your."
              + " enemy. You were unsucessful, as your hands were not the best"
              + " choice of weapon.")
        # Kill player.
        ch.player.status = False
    # What happens after Katie is dead.
    else:
        print("\nYou ball your hands up into fists, ready to take on your"
              + " enemy. You fall on your face trying to catch the rats, but"
              + " they manage to get away and eat more of your food. You"
              + " scratched up your hands and cannot continue to fight with"
              + " them.")
        # Delete items used from player's inventory and menu.
        ch.player.inventory.item_list["food"]["value"] -= 1
        del ch.player.inventory.item_list["weapons"]["hands"]
        del fight_menus["weapons"]["hands"]
        fight()


def fight():
    """ This function gives the player their fighting options and
    obtains their weapon when it's time to fight.
    """
    print("Act fast and choose your weapon.")
    while True:
        # Print options
        for option in fight_menus["weapons"]:
            print(f" - {option.title()}")
        choice = input("What will you pick? ").lower()
        # Check user's choice.
        if choice in fight_menus["weapons"]:
            fight_menus["weapons"][choice]()
            break
        else:
            print("That not a valid choice, choose again quickly!")


def run():
    """ This function is used to run from a fight and kills the player
    if chosen.
    """
    print("You try to run, but you fail.")
    ch.player.status = False


def punch():
    """ This function is used to punch Mick. """
    print("You punch Mick swiftly as he fights you back.")


def kick():
    """ This function is used to kick Mick. """
    print("You kick Mick over, but he grabs you, pulling you down.")


def slap():
    """ This function is used to skap Mick, but is not effective at
    stopping him.
    """
    print("You slap Mick to snap him out! This does nothing and he punches you"
          + " in the face.")
    del fight_menus["fight_mick"]["slap"]
    fight_mick()


def fight_mick():
    """ This function is used to fight Mick. """
    print("Quickly choose what to do!")
    while True:
        # Print options.
        for option in fight_menus["fight_mick"]:
            print(f" - {option.title()}")
        choice = input("What will you pick? ").lower()
        # Check user's choice of weapon.
        if choice in fight_menus["fight_mick"]:
            fight_menus["fight_mick"][choice]()
            break
        else:
            print("That not a valid choice, choose again quickly!")

fight_menus = {"fight": {"fight": fight, "run": run},
               "weapons" : {"gun": gun, "axe": axe, "hands": hands},
               "fight_mick": {"punch": punch, "kick": kick, "slap": slap}}