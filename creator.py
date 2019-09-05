import random
import time


import char
import texts

# def tempstatuselfs():
#     for x in tempdict:
#         print(x, ":", tempdict[x])

invalid = "\n\nInvalid input. Try again?\n"

def statsOpt():
    statOptDict = {"4d6": char.die4d6, "3d6": char.die3d6, "point": char.pointbuy}
    stat_options = input("Standard 4d6 with home rules option(4d6)? \n3d6(3d6?)\nor pointbuy(point)?\n")
    if stat_options in statOptDict:
        statOptDict[stat_options]()
    else:
        print(invalid)
        statsOpt()
masterstatsdict = char.masterstats

# masterstatsdict = {}

class Race(object):

    extra = 0
    blurb = ()
    blurb2 = 0

    statsdict = masterstatsdict
    # HE = "Half-elves have two points they may add to any skill."

    def masterStatus(self):
        for x in masterstatsdict:
            print(x, ":", masterstatsdict[x])

    def __init__ (self, name, age, size, speed, languages, STRMod, DEXMod, CONMod, INTMod, WISMod, CHAMod):
        self.name = name
        self.age = age
        self.size = size
        self.speed = speed
        self.languages = languages
        self.STRMod = STRMod
        self.DEXMod = DEXMod
        self.CONMod = CONMod
        self.INTMod = INTMod
        self.WISMod = WISMod
        self.CHAMod = CHAMod

    def abilityMods(self):
        global masterstatsdict
        masterstatsdict = char.masterstats
        masterstatsdict["STR"] += self.STRMod
        masterstatsdict["DEX"] += self.DEXMod
        masterstatsdict["CON"] += self.CONMod
        masterstatsdict["INT"] += self.INTMod
        masterstatsdict["WIS"] += self.WISMod
        masterstatsdict["CHA"] += self.CHAMod

    def statAdd(self):
        print(self.blurb)
        if self.extra == 0:
            pass
        else:
            def tempstatus(self):
                for x in tempdict:
                    print(x, ":", tempdict[x])
            global masterstatsdict
            tempdict = dict(masterstatsdict)
            extra = self.extra
            for x in tempdict:
                tempstatus(self)
                print("Points avaiable:", extra)
                print("Addition to(type 0 if no addition):")
                add = int(input(x))
                pls = tempdict[x] + add
                if add <= extra:
                    tempdict[x] = pls
                    extra -= add
                else:
                    print(invalid)
                    statAdd(self)
            tempstatus(self)
            answ = input("Are these acceptable?\n")
            if answ == "y" or answ == "yes" or answ == "1":
                print("Stats Updating")
                # global masterstatsdict
                masterstatsdict = dict(tempdict)
                Race.masterStatus(self)
            elif answ == "n" or answ == "no" or answ == "0":
                statAdd(self)
            else:
                print(invalid)
                statAdd(self)

    def subraceMod(self):
        if self.blurb2 == 0:
            pass
        else:
            ans = input(self.blurb2)
            def chaUD(self):
                 masterstatsdict["CHA"] += 1
            def intUD(self):
                 masterstatsdict["INT"] += 1
            def wisUD(self):
                 masterstatsdict["WIS"] += 1
            def strUD(self):
                 masterstatsdict["STR"] += 1
            def conUD(self):
                 masterstatsdict["CON"] += 1
            def dexUD(self):
                 masterstatsdict["DEX"] += 1
            ansdict = {
            "hill" : wisUD, "Hill": wisUD,
            "mnt": strUD, "Mnt" : strUD,
            "hi" : intUD, "Hi" : intUD,
            "wood" : wisUD, "Wood" : wisUD,
            "dark" : chaUD, "Dark" : chaUD,
            "lit" : chaUD, "Lit" : chaUD,
            "stout" : conUD, "Stout" : conUD,
            "for" : dexUD, "For" : dexUD,
            "rock" : conUD, "Rock" : conUD}
            if ans in ansdict:
                ansdict[ans](self)
            else:
                print(invalid)
                Race.subraceMod(self)

    def start(self):
        global masterstatsdict
        statsOpt()
        def start2():
            print("Adding racial Ability Modifiers")
            time.sleep(.25)
            Race.abilityMods(self)
            Race.statAdd(self)
            Race.subraceMod(self)
            Race.masterStatus(self)

        if self.name == "HU":
            self.variant()
            start2()
        else:
            start2()
    # print(masterstatsdict)


class HalfElf(Race):
    extra = 2
    blurb = texts.HE


class Dwarf(Race):
    extra = 0
    blurb = texts.DW
    blurb2 = "As a dwarf you get to pick a subrace!\nHill dwarf(hill) or Mountain dwarf(mnt)?\n"

class Elf(Race):


    blurb = texts.ELF
    blurb2 = "As an elf you get to pick betwen \nHigh Elf(hi), \nWood elf(wood, \nDark Elf/Drow(dark)\n"


class Halfling(Race):

    blurb = texts.HL
    blurb2 = "As a halfling you get to pick between \nLightfoot(lit), \nStout(stout)"

class Human(Race):
    extra = 0
    blurb = texts.HU

    def variant(self):
        vari = input("Humans have two options: \nIn standard rules they get +1 to all stats.(stan) \nIn variant rules they get +1 to two stats, a proficiency, and a skill.(var)")
        if vari == "stan":
            for x in masterstatsdict:
                masterstatsdict[x] += 1
        elif vari == "var":
            self.extra += 2
        else:
            print(invalid)
            self.variant()
        pass

class Dragonborn(Race):
    blurb = texts.DB

class Gnome(Race):
    blurb  = texts.GN
    blurb2 = "As a gnome, you get to pick between: \nRock gnome (rock) \nForest Gnome (for)\n"

class HalfOrc(Race):
    blurb = texts.HO

class Tiefling(Race):
    blurb = texts.TF

halfelf = HalfElf("HE", "20-180+", "Medium", 30, "Common, Elvish", 0, 0, 0, 0, 0, 2)
dwarf = Dwarf("DW", "50-350", "Medium", 25, "Common, Dwarvish", 0, 0, 2, 0, 0, 0)
elf = Elf("ELF", "100-750", "Medium", 25, "Common, Elvish", 0, 2, 0, 0, 0, 0)
halfling = Halfling("HL", "20-150", "Small", 25, "Common, Halfling", 0, 2, 0, 0, 0, 0)
human = Human("HU", "late teens - 100-", "Medium", 30, "Common, choice", 0, 0, 0, 0, 0, 0)
dragonborn = Dragonborn("DB", "15-80", "Medium", 30, "Common, Draconic", 2, 0, 0, 0, 0, 1)
gnome = Gnome("GN", "40-500", "Small", 25, "Common, Gnomish", 0, 0, 0, 2, 0, 0)
halforc = HalfOrc("HO", "14-75", "Medium", 30, "Common, Orc", 2, 0, 1, 0, 0, 0)
tiefling = Tiefling("TF", "late teens - 100+", "Medium", 30, "Common, Infernal", 0, 0, 0, 1, 0, 2)
