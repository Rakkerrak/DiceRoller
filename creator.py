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

masterstatsdict = char.masterstats

# masterstatsdict = {}

class Race(object):

    extra = 0
    blurb = ()

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
        print("nothing here")

    def start(self):
        global masterstatsdict
        print(self.name)
        statsOpt()
        # print(masterstatsdict)
        print("Adding racial Ability Modifiers")
        time.sleep(.25)
        Race.abilityMods(self)
        Race.statAdd(self)
        self.subraceMod()
        Race.masterStatus(self)
        # print(masterstatsdict)


class HalfElf(Race):
    extra = 2
    blurb = texts.HE

class Dwarf(Race):
    extra = 0
    blurb = texts.DW
# """
# Skill Proficiencies:
# None
# """
    def subraceMod(self):
        ans = input("As a dwarf you get to pick a subrace!\nHill dwarf(hill) or Mountain dwarf(mnt)?\n")
        if ans == "hill" or ans == "1" or ans == "Hill":
            masterstatsdict["WIS"] += 1
            hillDwarf = True
            # return hillDwarf
        elif ans == "mnt" or ans == "2" or ans == "Mnt" or ans == "mountain":
            masterstatsdict["STR"] += 1
            mntDwarf = True
            # return mntDwarf
        else:
            print(invalid)
            subraceMod()


class Elf(Race):
# """
# Skill Proficiencies:
# Perception
# """
    blurb = texts.ELF
    def subraceMod(self):
        ans = input("As an elf you get to pick betwen \nHigh Elf(hi), \nWood elf(wood, \nDark Elf/Drow(dark)\n")
        def chaUD(self):
             masterstatsdict["CHA"] += 1
             darkElf = True
        def intUD(self):
             masterstatsdict["INT"] += 1
             hiElf = True
        def wisUD(self):
             masterstatsdict["WIS"] += 1
             woodElf = True
        ansdict = {"hi" : intUD, "Hi" : intUD, "1" : intUD, "wood" : wisUD, "Wood" : wisUD, "2" : wisUD, "dark" : chaUD, "Dark" : chaUD, "3" : chaUD}
        if ans in ansdict:
            ansdict[ans](self)
        else:
            print(invalid)
            subraceMod(self)

class Halfling(Race):

    blurb = texts.HL
    def subraceMod(self):
        ans = input("As a halfling you get to pick between \nLightfoot(lit), \nStout(stout)")
        def chaUD(self):
             masterstatsdict["CHA"] += 1
             litHalf = True
        def conUD(self):
             masterstatsdict["CON"] += 1
             stoutHalf = True
        ansdict = {
        "lit": chaUD, "Lit": chaUD, "1": chaUD,
        "stout": conUD, "Stout": conUD, "2": conUD}
        if ans in ansdict:
            ansdict[ans](self)
        else:
            print(invalid)
            subraceMod()






# bark = Race(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# halfelf = Race("20-180+", "Medium", 30, "Common, Elvish", 0, 0, 0, 0, 0, 2)


halfelf = HalfElf("texts.HE", "20-180+", "Medium", 30, "Common, Elvish", 0, 0, 0, 0, 0, 2)
dwarf = Dwarf("texts.DW", "50-350", "Medium", 25, "Common, Dwarvish", 0, 0, 2, 0, 0, 0)
elf = Elf("texts.ELF", "100-750", "Medium", 25, "Common, Elvish", 0, 2, 0, 0, 0, 0)
halfling = Halfling("texts.HL", "20-150", "Small", 25, "Common, Halfling", 0, 2, 0, 0, 0, 0,)
