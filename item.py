import random

class object:
    def __init__(self, name, damage, armor):
        self.name = name
        self.damage = damage
        self.armor = armor

GoldSword = object("GoldSword", 20, 0)
IronHelmet = object("IronHelmet", 5, 15)
IronArmor = object("IronArmor", 5, 30)
FireStaff = object("FireStaff", 30, 0)
IceStaff = object("IceStaff", 15, 10)
AR15 = object("AR15", 35, 1)

objects = {
  "Gold Sword": {
    "Description": "You found a shining sword inserted" +
    " in a stone. That should be the Gold Sword.",
    "Location": [0, 1, 0],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": GoldSword
  },
  "Iron Helmet": {
    "Description":
    "You found a box, opened it, and" + " found a very beautiful helmet.",
    "Location": [0, 2, 1],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": IronHelmet
  },
  "Iron Armor": {
    "Description":
    "You notice that there seems to be" +
    " light in front of you, and after walking over, you find armor on" +
    " the scorched ground.",
    "Location": [0, 3, 1],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": IronArmor
  },
  "Fire Staff": {
    "Description":
    "You notice that there seems to be" +
    " light in front of you, and after walking over, you find armor on" +
    " the scorched ground.",
    "Location": [0, 3, 0],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": FireStaff
  },
  "Ice Staff": {
    "Description":
    "You notice that there seems to be" +
    " light in front of you, and after walking over, you find armor on" +
    " the scorched ground.",
    "Location": [0, 3, 3],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": IceStaff
  },
  "AR15": {
    "Description":
    "You notice that there seems to be" +
    " light in front of you, and after walking over, you find armor on" +
    " the scorched ground.",
    "Location": [0, 2, 3],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": AR15
  },
}