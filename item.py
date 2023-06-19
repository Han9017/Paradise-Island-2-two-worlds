# Imports --------------------------------------------------------------------
import random

class object:
    def __init__(self, name, damage, armor):
        self.name = name
        self.damage = damage
        self.armor = armor

# Detailed numerical values of various items
GoldSword = object("GoldSword", 25, 0)
IronHelmet = object("IronHelmet", 5, 80)
IronArmor = object("IronArmor", 5, 90)
FireStaff = object("FireStaff", 70, 0)
IceStaff = object("IceStaff", 50, 10)
AR15 = object("AR15", 350, 1)
DarkStone = object("DarkStone", 0, 0)
LightStone = object("LightStone", 0, 0)
BloodyStone = object("BloodyStone", 0, 0)
SickleOfDeath = object("SickleOfDeath", 300, 100)
PsychoKnife = object("PsychoKnife", 150, 0)
FlowerBomb = object("BloodyStone", 10000, 10000)

# Object information
objects = {
  "Gold Sword": {
    "Description": '''"You found a shining sword inserted" +
    " in a stone. That should be the Gold Sword."''',
    "Location": [0, 1, 0],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": GoldSword
  },
  "Iron Helmet": {
    "Description":
    '''You found a box, opened it, and" + " found a very beautiful helmet."''',
    "Location": [0, 2, 1],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": IronHelmet
  },
  "Iron Armor": {
    "Description":
    '''"You notice that there seems to be" +
    " light in front of you, and after walking over, you find armor on" +
    " the scorched ground."''',
    "Location": [0, 3, 1],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": IronArmor
  },
  "Fire Staff": {
    "Description":
    '''"You notice that there seems to be" +
    " light in front of you, and after walking over, you find Fire Staff on" +
    " the scorched ground."''',
    "Location": [1, 3, 0],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": FireStaff
  },
  "Ice Staff": {
    "Description":
    "You notice that there seems to be" +
    " light in front of you, and after walking over, you find Ice Staff on" +
    " the scorched ground.",
    "Location": [0, 3, 3],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": IceStaff
  },
  "AR15": {
    "Description":
    '''"This is much easier to use than magic"''',
    "Location": [0, 2, 3],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": AR15
  },
  "Flower Bomb": {
    "Description": '''"Dangerous Beauty"''',
    "Location": [1, 3, 2],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": FlowerBomb
  },  
  "Sickle of Death": {
    "Description": '''"In carnage, i bloom, like a flower in the dawn"''',
    "Location": [1, 3, 2],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": SickleOfDeath
  },  
  "Psycho Knife": {
    "Description": '''"The knife used by Jason Voorhees"''',
    "Location": [0, 2, 2],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": PsychoKnife
  },  
  "Dark Stone": {
    "Description": '''"Ahhhhhhhhhhhhhhhhhhhhhhh"''',
    "Location": [1, 1, 3],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": DarkStone
  },
  "Light Stone": {
    "Description": '''"It's so warm!"''',
    "Location": [1, 0, 3],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": LightStone
  },
  "Bloody Stone": {
    "Description": '''"Noooo! noO! NoOOooOOOoo!!!!"''',
    "Location": [1, 2, 0],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you took the item",
    "armor": BloodyStone
  },
}

medicine = {
  "medicine": {
    "Description": '''"You found medicine."''',
    "Location": [0, 3, 0],
    "Action": ["take", "leave"],
    "status": True,
    "Take": "you restored the health",
    "health": 25
  },
}


# Let players can discard items
def throwitem(player):
  orientating = True
  inventory = player.inventory
  while orientating:
    try:
      print("Please choose an item you want to throw.(type the number)")
      print("Please remember this item will be gone forever!")
      i = 0
      for item in inventory:
        i = i + 1
        print((f"{i} - ({item.name.title()})"))
      # Determine the maximum limit for player backpacks
      if len(inventory) < 6:
        i = i + 1
        print((f"{i} - I don't want to throw"))
      userInput = int(input("You choice: "))
      orientating = False
  
    except ValueError:
      print("WRONG INPUT!!!!!!!!!")
      continue
  
    else:
      if userInput >= 1 and userInput <= len(inventory):
        
        player.unarmored(inventory[userInput - 1].armor, 
                         inventory[userInput - 1].damage)
        del inventory[userInput - 1]
      elif userInput == len(inventory) + 1 and userInput <= 6:
        break
      else:
        print("Invalid input!")
        orientating = True
  