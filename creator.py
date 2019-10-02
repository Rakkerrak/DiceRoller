import random
import time


import char
import texts


#handles the race assignment

##GLOBALS
masterfreeskill = 0
masterracial_skills = []
miscdictR = {}

masterfeatsR = []
masterweaponsR = []
mastertoolsR = []
masterarmorR = []

mastersub = []

masterstatsdict = char.masterstats
mastermodsdict = {}
freelang = 0
masterHPadd = 0



invalid = "\n\nInvalid input. Try again?\n"

def statsOpt():
    statOptDict = {"4d6": char.die4d6, "3d6": char.die3d6, "point": char.pointbuy}
    stat_options = input("Standard 4d6 with home rules option(4d6)? \n3d6(3d6?)\nor pointbuy(point)?\n")
    if stat_options in statOptDict:
        statOptDict[stat_options]()
    else:
        print(invalid)
        statsOpt()



class Race(object):

    extra = 0
    blurb = ()
    blurb2 = 0

    freeskill = 0
    racial_skills = []
    feats = []
    weapons = []
    armor = []
    sub = []
    hpadd = 0
    tools = []


    statsdict = masterstatsdict

    def masterStatus(self):
        for x in masterstatsdict:
            print(x, ":", masterstatsdict[x])

    def __init__ (self, name, age, height, weight, size, speed, languages, STRMod, DEXMod, CONMod, INTMod, WISMod, CHAMod):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
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
            tempdict = {}
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
                    self.statAdd()
            tempstatus(self)
            answ = input("Are these acceptable?\n")
            if answ == "y" or answ == "yes" or answ == "1":
                print("Stats Updating")
                # global masterstatsdict
                masterstatsdict = dict(tempdict)
                Race.masterStatus(self)
                # print("I'ma loop now")
                # quit()
                # pass
            elif answ == "n" or answ == "no" or answ == "0":

                self.statAdd()
            else:
                print(invalid)
                self.statAdd()

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
            def hill():
                self.hill()
                wisUD(self)
            def mnt():
                self.mnt()
                strUD(self)
            def hi():
                self.hi()
                intUD(self)
            def wood():
                self.wood()
                wisUD(self)
            def dark():
                self.dark()
                chaUD(self)
            def lit():
                self.lit()
                chaUD(self)
            def stout():
                self.stout()
                conUD(self)
            def fore():
                self.fore()
                dexUD(self)
            def rock():
                self.rock()
                conUD(self)

            ansdict = {
            "stout" : conUD, "Stout" : conUD,
            "for" : dexUD, "For" : dexUD,
            "rock" : conUD, "Rock" : conUD,
            "hill" : hill, "Hill": hill,
            "mnt": mnt, "Mnt" : mnt,
            "hi" : hi, "Hi" : hi,
            "wood" : wood, "Wood" : wood,
            "dark" : dark, "Dark" : dark,
            "lit" : lit, "Lit" : lit,
            "stout" : stout, "Stout" : stout,
            "for" : fore, "For" : fore,
            "rock" : rock, "Rock" : rock
            }

            if ans in ansdict:
                try:
                    ansdict[ans]()
                    # self.sub.append(ans)
                except AttributeError:
                    print("This doesn't work")
            else:
                print(invalid)
                Race.subraceMod(self)


    def modGen(self):
        global mastermodsdict
        mastermodsdict = masterstatsdict.copy()
        for x in mastermodsdict:
            mastermodsdict[x] -= 10
            mastermodsdict[x] //= 2
        print("These are your modifiers")
        for x in mastermodsdict:
            print(x, ":", mastermodsdict[x])

    def miscdictUD(self):
        global miscdictR
        tempdict = {"RACE" : self.name, "AGE" : self.age, "SIZE" : self.size, "SPEED" : self.speed, "Languages" : self.languages, "HEIGHT" : self.height, "WEIGHT" : self.weight}
        miscdictR.update(tempdict)

    def globalizer(self):
        if self.hpadd == 0:
            pass
        else:
            global masterHPadd
            masterHPadd += self.hpadd
        global masterfeatsR
        masterfeatsR.extend(self.feats)
        global mastertoolsR
        mastertoolsR.extend(self.tools)
        global masterweaponsR
        masterweaponsR.extend(self.weapons)
        global masterarmorR
        masterarmorR.extend(self.armor)
        global mastersub
        mastersub.extend(self.sub)

    def start(self):
        global masterstatsdict
        statsOpt()
        def start2():
            print("Adding racial Ability Modifiers")
            time.sleep(.25)
            Race.abilityMods(self)
            Race.statAdd(self)
            # quit()
            Race.subraceMod(self)
            Race.masterStatus(self)
            Race.modGen(self)
            global masterracial_skills
            global masterfreeskill
            masterracial_skills.extend(self.racial_skills)
            masterfreeskill = 0
            masterfreeskill += self.freeskill
            Race.miscdictUD(self)
            # Race.subraceelse(self)
            Race.globalizer(self)


        if self.name == "Human":
            self.variant()
            start2()
        else:
            start2()
    # print(masterstatsdict)



class Dwarf(Race):
    extra = 0
    blurb = texts.DW
    blurb2 = "As a dwarf you get to pick a subrace!\nHill dwarf(hill) or Mountain dwarf(mnt)?\n"

    feats = ["Darkvision(pg. 20)", "Dwarven Resliience(pg. 20)", "Dwarven Combat Training(pg. 20)", "Tool Proficiency(pg. 20)", "Stonecunning(pg. 20)"]
    weapons = ["battle axe", "handaxe", "light hammer", "warhammer"]
    tools = ["Choose 1: Smith's Tools, Brewer's Tools,Mason's Tools" ]


    def hill(self):
        self.feats.append("Dwarven Toughness(pg. 20)")
        print("Adding 1HP to your total because you are a hill dwarf.")
        self.hpadd += 1
        self.sub.append("Hill")

    def mnt(self):
        self.feats.append("Dwarven Armor Training(pg. 20)")
        mntarmo = ["light", "medium"]
        self.armor.extend(mntarmo)
        self.sub.append("Mountain")


class Elf(Race):

    racial_skills = ["Perception"]
    blurb = texts.ELF
    blurb2 = "As an elf you get to pick betwen \nHigh Elf(hi), \nWood elf(wood, \nDark Elf/Drow(dark)\n"

    feats = ["Darkvision(pg. 23)", "Keen Senses(pg. 23)" "Fey Ancestry(pg. 23)", "Trance(pg. 23)"]

    def hi(self):
        hiwep = ["longsword", "shortsword", "shortbow", "longbow"]
        self.weapons.extend(hiwep)
        self.feats.append("Cantrip(pg. 24)")
        global freelang
        freelang +=1
        self.sub.append("High")

    def wood(self):
        woodwep = ["longword", "shortsword", "shortbow", "longbow"]
        self.weapons.extend(woodwep)
        self.speed += 5
        wfeat = ["Mask of the Wild(pg. 24)", "Fleet of Foot(pg. 24)"]
        self.feats.extend(wfeat)
        self.sub.append("Wood")


    def dark(self):
        dfeat = ["Superior Darkvision(pg. 24)", "Sunlight Sensitivity(pg. 24)", "Drow Magic(pg. 24)"]
        self.feats.extend(dfeat)
        dwep = ["rapiers", "shortswords", "hand crossbows"]
        self.weapons.extend(dwep)
        self.sub.append("Dark")



class Halfling(Race):

    blurb = texts.HL
    blurb2 = "As a halfling you get to pick between \nLightfoot(lit), \nStout(stout)"

    feats = ["Lucky(pg. 28)", "Brave(pg. 28)", "Halfling Nimbleness(pg. 28)"]


    def lit(self):
        self.feats.append("Naturally Stealthy(pg. 28)")
        self.sub.append("Lightfoot")

    def stout(self):
        self.feats.append("Stout Resilience(pg. 28)")
        self.sub.append("Stout")

class Human(Race):
    extra = 0
    blurb = texts.HU
    freeskill = 0

    def variant(self):
        vari = input("Humans have two options: \nIn standard rules they get +1 to all stats.(stan) \nIn variant rules they get +1 to two stats, a proficiency, and a skill.(var)")
        if vari == "stan":
            for x in masterstatsdict:
                masterstatsdict[x] += 1
        elif vari == "var":
            self.extra += 2
            self.freeskill = 1
            global freelang
            freelang += 1
        else:
            print(invalid)
            self.variant()
        pass

class Dragonborn(Race):
    blurb = texts.DB



class Gnome(Race):
    blurb  = texts.GN
    blurb2 = "As a gnome, you get to pick between: \nRock gnome (rock) \nForest Gnome (for)\n"

    feats = ["Darkvision(pg. 37)", "Gnome Cunning(pg. 37)"]

    def fore(self):
        forfe = ["Natural Illusionist(pg. 37)", "Speak with Small Beasts(pg. 37)"]
        self.feats.append(forfe)
        self.sub.append("Forest")


    def rock(self):
        rfe = ["Artificer's Lore(pg. 37)", "Tinker(pg. 37)"]
        self.feats.extend(rfe)
        self.tools.append("Artisan'sTools(Tinker's Tools)")
        self.sub.append("Rock")

class HalfElf(Race):
    extra = 2
    blurb = texts.HE
    freeskill = 2

    feats = ["Darkvision(pg. 39)", "Fey Ancestry(pg. 39)"]


class HalfOrc(Race):
    blurb = texts.HO
    racial_skills = ["Intimidation"]
    feats = ["Darkvision(pg. 41)", "Relentless Endurance(pg. 41)", "Savage Attacks(pg. 41)"]

class Tiefling(Race):
    blurb = texts.TF
    feats = ["Darkvision(pg. 43)", "Hellish Resistance(pg. 41)", "Infernal Legacy(pg. 41)"]

dwarf = Dwarf("Dwarf", "50-350", "4 to 5 feet", "weighs about 150 pounds", "Medium", 25, "Common, Dwarvish", 0, 0, 2, 0, 0, 0)
elf = Elf("Elf", "100-750", "under 5 to 6 feet", "has a slender build", "Medium", 25, "Common, Elvish", 0, 2, 0, 0, 0, 0)
halfling = Halfling("Halfling", "20-150", "3 feet", "weighs about 40 pounds", "Small", 25, "Common, Halfling", 0, 2, 0, 0, 0, 0)
human = Human("Human", "late teens - 100-", "almost 5 to over 6 feet", "weighs as much as a human weighs", "Medium", 30, "Common", 0, 0, 0, 0, 0, 0)
dragonborn = Dragonborn("Drangonborn", "15-80", "6+ feet", "weighs almost 250 pounds", "Medium", 30, "Common, Draconic", 2, 0, 0, 0, 0, 1)
gnome = Gnome("Gnome", "40-500", "3 to 4 feet", "weighs about 40 pounds", "Small", 25, "Common, Gnomish", 0, 0, 0, 2, 0, 0)
halfelf = HalfElf("Half Elf", "20-180+", "5 to 6 feet", "weighs as much as a human", "Medium", 30, "Common, Elvish", 0, 0, 0, 0, 0, 2)
halforc = HalfOrc("Half-Orc", "14-75", "5 to over 6 feet", "weighs a bit more than a human", "Medium", 30, "Common, Orc", 2, 0, 1, 0, 0, 0)
tiefling = Tiefling("Tiefling", "late teens - 100+", "almost 5 to over 6 feet", "weighs about as much as a human", "Medium", 30, "Common, Infernal", 0, 0, 0, 1, 0, 2)
