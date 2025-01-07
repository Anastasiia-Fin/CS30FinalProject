###############################################################################
"""
    This module contains The items dictionary with the name,
    description, and value of each item. It also contains the storage class.
"""
###############################################################################
items = {"water": {"name": "water", 
           "description": "You pick up a bottle of water." 
           + " Super refreshing.", 
           "value": 23},
 "food": {"name": "food", 
          "description": "You grab a can of food off the shelf." 
          + " Looks unappetizing.", 
          "value": 25},
 "medical supplies": {"name": "medical supplies", 
                      "description": "You grab a med kit filled" 
                      + " with bandages, pills, and needles.", 
                      "value": True},
 "weapons": {"gun": {"description": "You hold the heavey cold gun" 
                     + " in your hand and aim.", 
                     "value": True},
             "axe": {"description": "You pick up the axe. Holding" 
                     + " onto the wooden handled tight, as you get" 
                     + " ready to attack.", 
                     "value": True},
             "hands": {"description": "You ball your hands up into"
                       + " fists, ready to fight.", 
                       "value": True}},
 "ammunition": {"description": "You have a small box" 
     + " of limited ammunition. Use it wisely.",
     "value": True},
 "radio": {"name": "radio", 
           "description": "You pick up the radio. It has a bunch of"
           + " buttons, but you're not sure how to work it.", 
           "value": True},
 "flashlight": {"name": "flashlight", 
                "description": "You take your flashlight. The light" 
                + " it emits is dim, and you have no extra batteries.",
                "value": True}
}

class Storage:
    """ This class is the inventory of the game items the character
    has/picks up.
    item_list: list of items.
    """
    def __init__(self, item_list):
        self.item_list = item_list

# Create storage
player_items = Storage(items)