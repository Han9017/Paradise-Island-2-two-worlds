#this is a nested dictionary that contains all the place and descriptions
place = ["Swamp", "pond", "forest", "grassland", "ruins", "garbage dump", 
         "charred orphanage", "abandoned town", "stone forest", 
         "decayed place", "old site of observatory", "unmanned RV campsite",
         "cemetery", "zoo", "unmanned area", "wheat field", "Pigman house", 
         "cave", "demon garden", "magma river", "blood lake", 
         "headless queen statue", "fishman house", "tentacle land", 
         "twisted statue", "Dragon Den", "eerie crack", "upside down cross", 
         "odd Skeleton", "altar", "waterless river", "flower free grassland"]
places = {
  place[0]: {
    "Description": "Everything here looks so bad."
  },
  place[1]: {
    "Description": "Ophelia? Are you down there?"
  },
  place[2]: {
    "Description": "Full of a natural aura."
  },
  place[3]: {
    "Description": "I have seen beautiful storms here before."
  },
  place[4]: {
    "Description": "I can imagine the glory here used to be."
  },
  place[5]: {
    "Description": "Can we get out of here quickly?"
  },
  place[6]: {
    "Description": "Perhaps this is the expected outcome."
  },
  place[7]: {
    "Description": "Do you still have a supermarket here? I want to buy some supplies."
  },
  place[8]: {
    "Description": "I don't really like this place"
  },
  place[9]: {
    "Description": "Hope and light have been away from here for a long time."
  },
  place[10]: {
    "Description": "No one left, even the stars are not permanent."
  },
  place[11]: {
    "Description": "Can I drive them away for free?"
  },
  place[12]: {
    "Description": "Some day, I will join you guys."
  },
  place[13]: {
    "Description": "Do you see an elephant sitting on the ground?"
  },
  place[14]: {
    "Description": "I can feel a dangerous aura"
  },
  place[15]: {
    "Description": "I can stay here forever."
  },
  place[16]: {
    "Description": "I hate the guys who live inside."
  },
  place[17]: {
    "Description": "It's so dark inside."
  },
  place[18]: {
    "Description": "Why do those flowers have eyes on them?"
  },
  place[19]: {
    "Description": "I don't want to swim there."
  },
  place[20]: {
    "Description": "Fresh blood is boiling inside."
  },
  place[21]: {
    "Description": "Its beauty is twinged with a heartbreaking sadness."
  },
  place[22]: {
    "Description": "The guy live inside is very smelly and fishy."
  },
  place[23]: {
    "Description": "Why do tentacles protrude from the ground?"
  },
  place[24]: {
    "Description": "A tortured soul."
  },
  place[25]: {
    "Description": "Cruel hearts dwell within."
  },
  place[26]: {
    "Description": "Purple light spewed out from it."
  },
  place[27]: {
    "Description": "No, it shouldn't be done that way."
  },
  place[28]: {
    "Description": "What horrors have we resurrected here today?"
  },
  place[29]: {
    "Description": "The smell of blood drifted in the air."
  },
  place[30]: {
    "Description": "bad omen."
  },
  place[31]: {
    "Description": "It shouldn't be like this."
  },
}

#map------------------------------------------------------------------
map = [[[place[0], place[1], place[2], place[3]],
       [place[4], place[5], place[6], place[7]],
       [place[8], place[9], place[10], place[11]],
       [place[12], place[13], place[14], place[15]]],
       [[place[16], place[17], place[18], place[19]],
       [place[20], place[21], place[22], place[23]],
       [place[24], place[25], place[26], place[27]],
       [place[28], place[29], place[30], place[31]]]]

start_point = [0, 0, 0]

class player:
  def __init__(self, z, x, y):
    self.z = z
    self.x = x
    self.y = y

player = player(0, 0, 0)

print(map[player.z][player.x][player.y]["Description"])



         
         

