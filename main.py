#-----------------------------------------------------------------------------
#    File name:Paradise Island 2, two worlds
#    Author: Han Wang
#    Date created: 5/25/2023
#    Date last modified: 6/6/2023
#    version 1
#-----------------------------------------------------------------------------
'''   Description: Adventure Games'''
#-----------------------------------------------------------------------------

from map import * 
from item import *
from player import *

playing = True

def mainMenu():
  global playing
  orientating = playing
  while orientating:
    orientating = False
    
    print("Player, choose what you want to do!")
    Choose = ["walk", "look"]
    for do in Choose:
      print((f"- {do.title()}"))
    userInput = input("You choice: ").lower()
    
    if userInput == Choose[0]:
      print("You have multiple roads in front of you.")
      walkto()
    
    elif userInput == Choose[1]:
      print("You look around.")
      printLocation()
      InspectAction(objects)
      backpack = ""
      for item in player.inventory:
        backpack = backpack + item.name + ", "
      print("backpack:" + backpack)
    
    elif userInput == "quit":
      playing = False
      
    else:
      print("Invalid input!")
      orientating = True


def printLocation():
  global map, player
  print()
  print("You are currently at: " + map.detail[player.z][player.x][player.y])
  print("Location: [" + str(player.z) + "][" + str(player.x) + 
        "][" + str(player.y) + "]")
  for place in places:
    if place == map.detail[player.z][player.x][player.y]:
      print(places[place]["Description"])
  print()


def walkto():
  global playing, map, player
  orientating = playing
  while orientating:
    canUp = False
    canDown = False
    canRight = False
    canLeft = False
  
    if player.x > 0:
      canUp = True
      print("you can go up - type:'up'")
  
    if player.x < map.max_x:
      canDown = True
      print("you can go down - type:'down'")
  
    if player.y < map.max_y:
      canRight = True
      print("you can go right - type:'right'")
  
    if player.y > 0:
      canLeft = True
      print("you can go left - type:'left'")

    orientating = False  
    waypoint = input("choose your direction:")
      
    if waypoint == "down" and canDown:
      player.x = player.x + 1
    
    elif waypoint == "up" and canUp:
      player.x = player.x - 1
    
    elif waypoint == "left" and canLeft:
      player.y = player.y - 1
    
    elif waypoint == "right" and canRight:
      player.y = player.y + 1
  
    elif waypoint == "quit":
      playing = False
    
    else:
      print("Sorry you can not move to there.")
      orientating = True 
  if player.z == 0 and player.x == 3 and player.y == 3:
    printLocation()
    print("You got teleported!")
    player.z = 1
    player.x = 0
    player.y = 0

map = map(map_d, 1, 3, 3)
player = player(0, 0, 0,[])

file = open("story.txt", "r")
print(file.read())
file.close()
print()

  
def InspectAction(objects):
  global playing, map, player
  for object in objects:
    object_z = objects[object]["Location"][0]
    object_x = objects[object]["Location"][1]
    object_y = objects[object]["Location"][2]
    object_status = objects[object]["status"]
    if (object_z == player.z and object_x == player.x and 
        object_y == player.y and object_status):
      print(f"{objects[object]['Description']}")
      Choose = objects[object]["Action"]
      for do in Choose:
        print((f"- {do.title()}"))
      userInput = input("You choice: ").lower()
      if userInput == Choose[0]:
        
        if Choose[0] == "take":
          currentItem = objects[object]["armor"]
          print(f"{objects[object]['Take']}")
          player.inventory.append(currentItem)
          加call
          objects[object]["status"] = False

      else:
        print("Invalid input!")
        

while playing:   
  mainMenu()
  
      