###############################################################################
"""
    This module holds all character related functions, classes, and 
    dictionaries. The npc database, character classes, and 
    also holds the player and character creation.
"""
###############################################################################
import items as i

npc = {"dr.tucker": {"name": "dr.tucker", "role": "doctor",
                     "description": "Dr. Tucker is a shy and quiet doctor," 
                     + " but in your situation he may just come in handy.",
                     "status": True, "infected": False, 
                     "dialogue": ["I really hope my family is doing okay"
                                  + " through this. The thought just makes me"
                                  + " worried.", "I wish I was helping people" 
                                  + " in the hospital and not stuck in this"
                                  + " bunker. At least we have shelter.", 
                                  "I hope i can be good help taking care" 
                                  + " everyone."]},
       "ella": {"name": "ella", "role": "mechanic",
                "description": "Ella is a layed-back mechanic who can keep "
                + "calm in stressfull times. She's good to have on your team.",
                "status": True, "infected": False, 
                "dialogue": ["It sure is stuffy being lock in here, but we can"
                             + " get through this!", "Hey if you ever need" 
                             + " help fixing stuff, I am your gal!", "Being"
                             + " stuck down here sucks! I totally miss my"
                             + " work desk."]},
       "mick": {"name": "mick", "role": "comedian",
                "description": "Mick is a silly comedian, cracking jokes" 
                + " at any chance he gets. He may actually help"
                + " to keep your team sane.", 
                "status": True, "infected": False,
                "dialogue": ["Why did the zombie go to see the doctor?"
                             + " beacause he was coffin!", "What kind of" 
                             + " zombie doesn't laugh at my jokes? a dead"
                             + " serious one!", "Whats a zombie's"
                             + " favourite weather? B-rain!"]},
       "katie": {"name": "katie", "role": "FBI agent",
                 "description": "Katie is a serious FBI agent. She stands"
                 + " on buisness and is prepared to survive.", 
                 "status": True, "infected": False, 
                 "dialogue": ["This bunker has everything we could want for"
                              + " survival.", "I have read many books about"
                              + " the apocalypse. I am prepaered to live.",
                              "This bunker has been passed down through my"
                              + " family. The knowlege of the apocalypse runs"
                              + " in my family!"]}
}

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


# Create characters
player = Character("Bob", "player", "description", True, False, i.player_items)
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