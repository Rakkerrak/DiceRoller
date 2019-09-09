import random
import time

import diceroll
import creator


#GLOBALS
masterfreeskill2 = 0

masterclassskill = []
masterchoiceCL = 0
masterprof = 0

class Classes(object):

    classskill = []
    choiceCL = 0
    prof = 2

    def __init__ (self, name, hit_die):
        self.name = name
        self.hit_die = hit_die

    def hpgen(self):
        hp = creator.mastermodsdict["CON"] + self.hit_die
        print("Your HP at level 1 is", hp)
        print("Your hit dice is 1d", self.hit_die)

    def skillUD(self):
        global masterchoiceCL
        global masterclassskill
        global masterfreeskill2
        masterchoiceCL += self.choiceCL
        if self.name == "bard":
            masterfreeskill2 += self.choiceCL
        else:
            masterclassskill = self.classskill.copy()

    def start(self):
        global masterfreeskill2
        Classes.hpgen(self)
        self.skillUD()
        print("limited", masterchoiceCL)
        print("skill list", masterclassskill)
        print("freeskill2", masterfreeskill2)

class Barbarian(Classes):
    classskill = ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
    choiceCL = 2

class Bard(Classes):
    classskill = ["Monkeys"]
    choiceCL = 3

class Cleric(Classes):
    classskill = ["History", "Insight", "Medicine", "Persuasion", "Religion"]
    choiceCL = 2

class Druid(Classes):
    classskill = ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"]
    choiceCL = 2

class Fighter(Classes):
    classskill = ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]
    choiceCL = 2

class Monk(Classes):
    classskill = ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]
    choiceCL = 2

class Paladin(Classes):
    classskill = ["Athletics", "Insight", "Intimidation", "Insight", "Medicine", "Persuasion", "Religion"]
    choiceCL = 2

class Ranger(Classes):
    classskill = ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"]
    choiceCL = 3

class Rogue(Classes):
    classskill = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]
    choiceCL = 4

class Sorcerer(Classes):
    classskill = ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"]
    choiceCL = 2

class Warlock(Classes):
    classskill = ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"]
    choiceCL = 2

class Wizard(Classes):
    classskill = ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
    choiceCL = 2

barbarian = Barbarian("barbarian", 12)
bard = Bard("bard", 8)
cleric = Cleric("cleric", 8)
druid = Druid("druid", 8)
fighter = Fighter("fighter", 10)
monk = Monk("monk", 8)
paladin = Paladin("paladin", 10)
ranger = Ranger("ranger", 10)
rogue = Rogue("rogue", 8)
sorcerer = Sorcerer("sorcerer", 6)
warlock = Warlock("warlock", 8)
wizard = Wizard("wizard", 6)
