import random
import time

import diceroll
import creator

#handles the class assignment


#GLOBALS
masterfreeskill2 = 0
miscdictC = {}

masterfeatsCL = []
masterweaponsCL = []
masterarmorCL = []
mastertoolsCL = []
# masterfeatsCL = []

masterequipCL = []

mastersavesCL = []

masterclassskill = []
masterchoiceCL = 0
masterprof = 0

invalid = "\n\nInvalid input. Try again?\n"

class Classes(object):

    classskill = []
    choiceCL = 0
    prof = 2
    weapons = []
    armor = []
    tools = []
    saves = []
    feats = []
    equip = {}
    equiplong = []
    staticEquip = []

    def __init__ (self, name, hit_die):
        self.name = name
        self.hit_die = hit_die

    def hpgen(self):
        hp = creator.mastermodsdict["CON"] + self.hit_die +creator.masterHPadd
        print("Your HP at level 1 is", hp)
        print("Your hit dice is 1d", self.hit_die)
        global miscdictC
        tempdict = {"HP" : hp, "HitDie" : self.hit_die, "CLASS" : self.name, "Proficience Bonus" : self.prof}
        miscdictC.update(tempdict)

    def skillUD(self):
        global masterchoiceCL
        global masterclassskill
        global masterfreeskill2
        if self.name == "bard":
            masterfreeskill2 += self.choiceCL
        else:
            masterchoiceCL += self.choiceCL
            masterclassskill = self.classskill.copy()

    def clequip(self):
        global masterequipCL
        def addequip():
            quipdict = self.equip
            quip = []
            for x in quipdict:
                choose = input("Please choose from the following: \n1: %s\n2: %s \n" % (x, quipdict[x]))
                if choose == "1":
                    quip.append(x)
                if choose == "2":
                    quip.append(quipdict[x])
            print(", " .join(quip))
            confi = input("Is this correct?\n")
            if confi == "y" or confi == "yes" or confi == "1":
                masterequipCL.extend(quip)
            elif confi == "n" or confi == "no" or confi == "2":
                addequip()
            else:
                print(invalid)
                addequip()

        def eqlong():
            telong = []
            ans = input("Please choose from the following: \n1: %s \n2: %s \n3: %s\n" % (self.equiplong[0], self.equiplong[1], self.equiplong[2]))
            ans2 = int(ans)
            ans2 - 1
            telong.append(self.equiplong[ans2])
            print(", " .join(telong))
            confir = input("Is this correct?\n")
            if confir == "y" or confir == "yes" or confir == "1":
                masterequipCL.extend(telong)
            elif confir == "n" or confir == "no" or confir == "2":
                eqlong()
            else:
                print(invalid)
                eqlong()

        if self.equiplong != []:
            eqlong()
            addequip()

        else:
            addequip()

        masterequipCL.extend(self.staticEquip)


    def globalUD(self):
        global masterfeatsCL
        global masterarmorCL
        global mastertoolsCL
        global masterfeatsCL
        global mastersavesCL
        global masterweaponsCL
        masterfeatsCL.extend(self.feats)
        masterarmorCL.extend(self.armor)
        mastertoolsCL.extend(self.tools)
        mastersavesCL.extend(self.saves)
        masterweaponsCL.extend(self.weapons)


    def start(self):
        global masterfreeskill2
        Classes.hpgen(self)
        self.skillUD()
        self.clequip()

        Classes.globalUD(self)
        # print("limited", masterchoiceCL)
        # print("skill list", masterclassskill)
        # print("freeskill2", masterfreeskill2)

class Barbarian(Classes):
    classskill = ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
    choiceCL = 2
    armor = ["light", "medium", "shields"]
    weapons = ["simple", "martial"]
    saves = ["STR", "CON"]
    feats = ["Rage (pg. 48)", "Unarmored Defense(pg. 48)"]
    equip = {
    "a greataxe" : "any martial weapon",
    "two handaxes": "any simple weapon"
    }
    staticEquip =["an explorer's pack", "four javelins"]


class Bard(Classes):
    classskill = ["Monkeys"]
    choiceCL = 3
    armor = ["light"]
    weapons = ["simple", "hand crossbows", "longswords", "rapiers", "shortswords"]
    tools = ["three musical instrumens of your choice"]
    saves = ["DEX", "CHA"]
    feats = ["Spellcasting(pg. 52)", "Bardic Inspiration(pg. 53)"]
    equip = {"a diplomat's pack" : "an entertainer's pack",
    "a lute" : "any other musical instrument"
    }
    equiplong = ["a rapier", "a longsword", "any simple weapon"]
    staticEquip = ["leather armor", "a dagger"]

class Cleric(Classes):
    classskill = ["History", "Insight", "Medicine", "Persuasion", "Religion"]
    choiceCL = 2
    armor = ["light", "medium", "shields"]
    weapons = ["simple"]
    saves = ["WIS", "CHA"]
    feats = ["Spellcasting(pg. 58)", "Divine Domain(pg. 58)"]
    equip = {
    "a mace" : "a warhammer(if proficient)",
    "a light crossbow and 20 bolts" : "any simple weapon",
    "a priest's pack" : "an explorer's pack"
    }
    equiplong = ["scale mail", "leather armor", "chain mail(if proficient)"]
    staticEquip = ["a shield", "a holy symbol"]


class Druid(Classes):
    classskill = ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"]
    choiceCL = 2
    armor = ["nothing made of metal", "light", "medium", "shields"]
    weapons = ["clubs", "daggers", "darts", "javelins", "maces", "quarterstaffs", "scimitarts", "sickels", "slings", "spears"]
    tools = ["Herbalism Kit"]
    saves = ["INT", "WIS"]
    feats = ["Druidic(pg. 66)", "Spellcasting(pg. 66)", ]
    equip = {
    "a wooden shield" : "any simple weapon",
    "a scimitar" : "any simple melee weapon"
    }
    staticEquip = ["leather armor", "an explorer's pack", "a druidic focus"]

class Fighter(Classes):
    classskill = ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]
    choiceCL = 2
    armor = ["all", "shields"]
    weapons = ["simple", "martial"]
    saves = ["STR", "CON"]
    feats = ["Fighting Style(pg. 72)", "Second Wind(pg. 72)"]
    equip = {
    "chain mail" : "leather armor, a longbow, and 20 arrows",
    "a martial weapon and a shield" : "two martial weapons",
    "a light crossbow and 20 bolts" : "two handaxes",
    "a dungeoneer's pack" : "an explorer's pack"
    }


class Monk(Classes):
    classskill = ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]
    choiceCL = 2
    armor = []
    weapons = ["simple", "shortswords"]
    tools = ["one type of artisan's tools or one musical instrument"]
    saves = ["STR", "DEX"]
    feats = ["Unarmored Defense(pg. 78)", "Martial Arts (pg. 78)"]
    equip = {
    "a shortsword" : "any simple weapon",
    "a dungeoneer's pack" : "an explorere's pack"
    }
    staticEquip = ["10 darts"]

class Paladin(Classes):
    classskill = ["Athletics", "Insight", "Intimidation", "Insight", "Medicine", "Persuasion", "Religion"]
    choiceCL = 2
    armor = ["all", "shields"]
    weapons = ["simple", "martial"]
    saves= ["WIS", "CHA"]
    feats = ["Divine Sense(pg. 84)", "Lay on Hands(pg. 84)"]
    equip = {
    "a martial weapon and a shield" : "two martial weapons",
    "five javelines" : "any simple melee weapon",
    "a priest's pack" : "an explorer's pack"
    }
    staticEquip = ["chain mail", "a holy symbol"]


class Ranger(Classes):
    classskill = ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"]
    choiceCL = 3
    armor = ["light", "medium", "shields"]
    weapons = ["simple", "martial"]
    saves = ["STR", "DEX"]
    feats = ["Favored Enemy(pg. 91)", "Natural Explorer(9g. 91)"]
    equip = {
    "scale mail" : "leather armor",
    "two shortswords" : "two simple melee weapons",
    "a dungeoneer's pack" : "an explorer's pack"
    }
    staticEquip = ["a longbow and a quiver of 20 arrows"]

class Rogue(Classes):
    classskill = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]
    choiceCL = 4
    armor = ["light"]
    weapons = ["simple,", "hand crossbow", "longsword", "rapier", "shortsword"]
    tools = ["Thieves' Tools"]
    saves = ["DEX" "INT"]
    feats = ["Expertise(pg.96)", "Sneak Attack(pg. 96)", "Thieves' Cant(pg. 96)"]
    equip = {
    "a rapier" : "a shortsword",
    "a shortbow and a quiver of 20 arrows" : "a shortsword"
    }
    equiplong = ["a burglar's pack", "a dungeoneer's pack", "am explorer's pack"]
    staticEquip = ["leather armor", "two daggers", "thieves' tools"]

class Sorcerer(Classes):
    classskill = ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"]
    choiceCL = 2
    armor = []
    weapons = ["daggers", "darts", "slings", "quarterstaffs", "light crossbow" ]
    saves = ["CON", "CHA"]
    feats = ["Spellcasting(pg. 101)", "Sorcerous Origin(pg. 101)"]
    equip = {
    "a light crossbow and 20 bolts" : "any simple weapon",
    "a component pouch" : "an arcane focus",
    "a dungeoneer's pack" : "an explorer's pack"
    }
    staticEquip = ["two daggers"]


class Warlock(Classes):
    classskill = ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"]
    choiceCL = 2
    armor = ["light"]
    weapons = ["simple"]
    saves = ["WIS", "CHA"]
    feats = ["Otherworldly Patron(pg. 107)", "Pact Magic(pg. 107)"]
    equip = {
    "a light crossbow and 20 bolts" : "any simple weapon",
    "a component pouch" : "an arcane focus",
    "a scholar's pack" : "an explorer's pack"
    }
    staticEquip = ["leather armor", "any simple weapon", "two daggers"]

class Wizard(Classes):
    classskill = ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
    choiceCL = 2
    armore = {}
    weapons = ["daggers", "darts", "slings", "quarterstaffs", "light crossbows"]
    saves = ["INT", "WIS"]
    feats = ["Spellcasting(pg. 114)", "Arcane Recovery(pg. 115)"]
    equip = {
    "a quarterstaff" : "a dagger",
    "a component pouch" : "an arcane focus",
    "a scholar's pack" : "an explorer's pack"
    }
    staticEquip = ["a spellbook"]

barbarian = Barbarian("Barbarian", 12)
bard = Bard("Bard", 8)
cleric = Cleric("Cleric", 8)
druid = Druid("Druid", 8)
fighter = Fighter("Fighter", 10)
monk = Monk("Monk", 8)
paladin = Paladin("Paladin", 10)
ranger = Ranger("Ranger", 10)
rogue = Rogue("Rogue", 8)
sorcerer = Sorcerer("Sorcerer", 6)
warlock = Warlock("Warlock", 8)
wizard = Wizard("Wizard", 6)
