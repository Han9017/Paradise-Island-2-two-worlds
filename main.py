#-----------------------------------------------------------------------------
#    File name:Paradise Island 2, two worlds
#    Author: Han Wang
#    Date created: 5/25/2023
#    Date last modified: 6/18/2023
#    version 1.1.4
#-----------------------------------------------------------------------------
'''   Description: Adventure Games'''
#-----------------------------------------------------------------------------
# Imports and-----------------------------------------------------------------
from map import *
from item import *
from player import *

playing = True

map = map(map_d, 1, 3, 3)
player = player(0, 0, 0, [], 1, 1)
summonCondition = 0

# open the story.txt file, and then read
file = open("story.txt", "r")
print(file.read())
file.close()
# print it(story)
print()


# Functions ------------------------------------------------------------------
def mainMenu():
  global playing
  orientating = playing
  while orientating:
    orientating = False

    print("Player, choose what you want to do!")
    # List the options that players can choose from.
    Choose = ["walk", "look", "throw an item", "quit"]
    for do in Choose:
      print((f"- {do.title()}"))
    # Allow players to freely choose capitalization
    userInput = input("You choice: ").lower()

    # If the player chooses 0
    if userInput == Choose[0]:
      print("You have multiple roads in front of you.")
      walkto()

    # If the player chooses 1
    elif userInput == Choose[1]:
      print("You look around.")
      # Tell the player the location
      printLocation()
      InspectAction(objects, npcs)
      InspectAction1(npcs)
      InspectAction2(medicine)

      # Players' backpack and can add items to it.
      backpack = ""
      for item in player.inventory:
        backpack = backpack + item.name + ", "
      # Print out and tell the player the items already in the backpack
      print("backpack:" + backpack)

    # If the player chooses 2
    elif userInput == Choose[2]:
      throwitem(player)

    # If the player chooses quit.
    elif userInput == "quit":
      # change playing to false (stop the game).
      playing = False

    else:
      # If the player inputs other words, languages, or letters that have not 
      # been set properly
      print("Invalid input!")
      # Restart Selection
      orientating = True


def printLocation():
  global map, player
  print()
  # Tell the player the location
  print("You are currently at: " + map.detail[player.z][player.x][player.y])
  print("Location: [" + str(player.z) + "][" + str(player.x) + "][" +
        str(player.y) + "]")
  for place in places:
    # Print corresponding descriptions based on the location of the player.
    if place == map.detail[player.z][player.x][player.y]:
      print(places[place]["Description"])
  print()


# movement------------------------------------------------------------------
def walkto():
  global playing, map, player
  orientating = playing
  while orientating:
    canUp = False
    canDown = False
    canRight = False
    canLeft = False

    # up
    if player.x > 0:
      canUp = True
      print("you can go up - type:'up'")

    # down
    if player.x < map.max_x:
      canDown = True
      print("you can go down - type:'down'")

    # right
    if player.y < map.max_y:
      canRight = True
      print("you can go right - type:'right'")

    # left
    if player.y > 0:
      canLeft = True
      print("you can go left - type:'left'")

    orientating = False
    # let player choose where is he want to go.
    waypoint = input("choose your direction:")

    # player go up
    if waypoint == "down" and canDown:
      player.x = player.x + 1

    # player go down
    elif waypoint == "up" and canUp:
      player.x = player.x - 1

    # player go left
    elif waypoint == "left" and canLeft:
      player.y = player.y - 1

    # player go right
    elif waypoint == "right" and canRight:
      player.y = player.y + 1

    elif waypoint == "quit":
      playing = False

    # If the player touches the map boundary
    else:
      print("Sorry you can not move to there.")
      orientating = True
  # The coordinates transmitted by the player. 
  # If the player reaches [0][3][3], change z.
  if player.z == 0 and player.x == 3 and player.y == 3:
    printLocation()
    print("You got teleported!")
    #change the z-axis to 1
    player.z = 1
    player.x = 0
    player.y = 0


# Interactive boss and items present in the game.
def InspectAction(objects, npcs):
  global playing, map, player, summonCondition
  for object in objects:
    object_z = objects[object]["Location"][0]
    object_x = objects[object]["Location"][1]
    object_y = objects[object]["Location"][2]
    object_status = objects[object]["status"]
    if (object_z == player.z and object_x == player.x and object_y == player.y
        and object_status):
      print(f"{objects[object]['Description']}")
      Choose = objects[object]["Action"]

      for do in Choose:
        print((f"- {do.title()}"))
      userInput = input("You choice: ").lower()
      if userInput == Choose[0]:

        # Code for summoning boss
        if Choose[0] == "take":
          currentItem = objects[object]["armor"]
          print(f"{objects[object]['Take']}")
          # Three necessary summoning items
          if (currentItem.name != "DarkStone"
              and currentItem.name != "LightStone"
              and currentItem.name != "BloodyStone"):

            if len(player.inventory) >= 6:
              print("Your bag is full!")
              throwitem(player)
            player.inventory.append(currentItem)
            print("you have " + str(len(player.inventory)) + " items")
            player.armored(currentItem.armor, currentItem.damage)

          else:
            summonCondition += 1

          # If all three summoning objects have been gathered
          if summonCondition == 3:
            # Tell the player where the boss is generated
            print("The Boss has been summoned at [1][3][3]")
            # Summon boss
            npcs["Elder Dragon"]["status"] = True

          objects[object]["status"] = False

      # If the player chooses to avoid the battle and leave
      elif userInput == Choose[1]:
        print("You leave")

      else:
        print("Invalid input!")


# Interactive npcs present in the game.
def InspectAction1(npcs):
  global playing, map, player
  for npc in npcs:
    npc_z = npcs[npc]["Location"][0]
    npc_x = npcs[npc]["Location"][1]
    npc_y = npcs[npc]["Location"][2]
    npc_status = npcs[npc]["status"]
    if (npc_z == player.z and npc_x == player.x and npc_y == player.y
        and npc_status):
      print(f"{npcs[npc]['Name']}")
      print(f"{npcs[npc]['Description']}")
      Choose = npcs[npc]["Action"]
      for do in Choose:
        print((f"- {do.title()}"))
      userInput = input("You choice: ").lower()
      if userInput == Choose[0]:

        # If the player chooses to engage npc
        if Choose[0] == "fight":
          print(f"{npcs[npc]['fight']}")
          if fight(player, npcs[npc]['Power']):
            print("You Win!")
            # Notify players of their health after completing the battle
            print("Remain Health: " + str(player.health))
            #Keep npc from appearing again if it has already been defeated
            npcs[npc]["status"] = False
            if (boss_point[0] == player.z and boss_point[1] == player.x
                and boss_point[2] == player.y):
              print("You did it!")
              playing = False

          # If the player fails to defeat the boss
          else:
            print("You lost! Try to get stronger!")

      elif userInput == Choose[1]:
        print("You leave")

      else:
        print("Invalid input!")


# Medicines that can restore health in the game
def InspectAction2(medicines):
  global playing, map, player
  for medicine in medicines:
    medicine_z = medicines[medicine]["Location"][0]
    medicine_x = medicines[medicine]["Location"][1]
    medicine_y = medicines[medicine]["Location"][2]
    medicine_status = medicines[medicine]["status"]
    if (medicine_z == player.z and medicine_x == player.x
        and medicine_y == player.y and medicine_status):
      print(f"{medicines[medicine]['Description']}")
      Choose = medicines[medicine]["Action"]
      for do in Choose:
        print((f"- {do.title()}"))
      userInput = input("You choice: ").lower()
      if userInput == Choose[0]:

        # If the player chooses to pick up medication for treatment, 
        # the player gains health recovery.
        if Choose[0] == "take":
          currentItem = medicines[medicine]["health"]
          print(f"{medicines[medicine]['Take']}")
          player.heal(currentItem)
          medicines[medicine]["status"] = False

      elif userInput == Choose[1]:
        print("You leave")

      else:
        print("Invalid input!")


# Continuous game play loop.
while playing:
  mainMenu()
