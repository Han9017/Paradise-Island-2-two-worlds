# inport
from map import *

# Determination of injury
class player:
  def __init__(self, z, x, y, inventory, armor, damage):
    self.z = z
    self.x = x
    self.y = y
    self.inventory = inventory
    self.armor = armor
    self.damage = damage
    self.health = 100
    self.maxhealth = 100

  def armored(self, armor, damage):
    self.armor += armor
    self.damage += damage

  def unarmored(self, armor,damage):
    self.armor -= armor
    self.damage -= damage

  def heal(self, health):
    self.health += health
    if self.health > self.maxhealth:
      self.health  = self.maxhealth

class Character:

  def __init__(self, health, armor, damage):
    self.health = health
    self.armor = armor
    self.damage = damage


# On the Determination of Battle Victory and Defeat
def fight(actor1, actor2):
  if (actor1.armor > actor2.damage):
    actor1hurt = 1
  else:
    actor1hurt = actor2.damage - actor1.armor

  if (actor2.armor > actor1.damage):
    actor2hurt = 1
  else:
    actor2hurt = actor1.damage - actor2.armor

  while actor1.health > 0 and actor2.health > 0:
    actor1.health = actor1.health - actor1hurt
    actor2.health = actor2.health - actor2hurt

  if actor1.health <= 0:
    actor1.health = 20
    return False
  else:
    return True


# Value of npcs (health, damage, armor)
DragonPower = Character(50, 15, 28)
SpiderPower = Character(10, 5, 5)
GargoylePower = Character(200, 10, 40)
GhostPower = Character(50, 60, 70)
ZombiePower = Character(10, 10, 10)
TigerPower = Character(20, 10, 15)
DemonPower = Character(40, 100, 80)
BossPower = Character(500, 100, 100)

#Description about npc "Little Demon Legion", "Eric", and "Injured Old Man".
npcs = {
  "Gragon": {
    "Name" : "Gragonn",
    "Description": '''"What caused it to be so cruel?"''',
    "Location": [0, 2, 3],
    "Action": ["fight", "leave"],
    "fight": "You fight with them.",
    "status": True,
    "Power": DragonPower
  },
  "Gargoyle": {
    "Name" : "Gargoyle",
    "Description": '''"It's real, so terrifying!"''',
    "Location": [0, 0, 3],
    "Action": ["fight", "leave"],
    "fight": "You face pure evil directly.",
    "status": True,
    "Power": GargoylePower
  },
  "Spider": {
    "Name" : "Spider",
    "Description": '''"Its mouth is so big"''',
    "Location": [0, 2, 0],
    "Action": ["fight", "leave"],
    "fight": "You fight with him.",
    "status": True,
    "Power": SpiderPower
  },
    "Ghost": {
    "Name" : "Ghost",
    "Description": '''"Translucent disgusting creature."''',
    "Location": [1, 0, 0],
    "Action": ["fight", "leave"],
    "fight": "You fight with him.",
    "status": True,
    "Power": GhostPower
  },
    "Zombie": {
    "Name" : "Zombie",
    "Description": '''"Is that you Carl?."''',
    "Location": [1, 1, 1],
    "Action": ["fight", "leave"],
    "fight": "You fight with him.",
    "status": True,
    "Power": ZombiePower
  },
    "Saber-Toothed Tiger": {
    "Name" : "Tiger",
    "Description": '''"Isn't it extinct?"''',
    "Location": [0, 1, 1],
    "Action": ["fight", "leave"],
    "fight": "You fight with him.",
    "status": True,
    "Power": TigerPower
  },
    "White Demon": {
    "Name" : "Demon",
    "Description": '''"Beautiful sins, accompanied by the smell of death"''',
    "Location": [1, 2, 3],
    "Action": ["fight", "leave"],
    "fight": "You fight with him.",
    "status": True,
    "Power": DemonPower
  },
  "Elder Dragon": {
    "Name" : "Dragon",
    "Description": '''"It's the sin itself"''',
    "Location": [1, 3, 3],
    "Action": ["fight", "leave"],
    "fight": "You fight with them.",
    "status": False,
    "Power": BossPower
  }
}
