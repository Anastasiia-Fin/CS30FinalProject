###############################################################################
"""
    This module has all map realated functions and dictionaries.
    It holds each room function, room description, and map versions.
"""
###############################################################################
from tabulate import tabulate
map_file = 'map.txt'

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

map = [["Storage", "Washroom"],
["Main Room"],
["Utility", "Medical Room"]]

ruined_map = [["----------", "----------"],
["----------"],
["----------", "----------"]]


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


def check_map():
  """ This function prints the map from an external file. """
  with open(map_file, "r", encoding="utf-8") as file:
      print(file.read())


def make_map(map_version):
  """ This function creates the map in an external file. """
  with open(map_file, "w", encoding='utf-8') as file:
      file.write(tabulate(map_version, tablefmt = "fancy_grid"))
