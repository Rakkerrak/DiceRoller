

#GLOBALS
masterfreeskill3 = 0
masterextralang = 0
masterskillBG = []
mastertools = []
masterfeats = []


class Background(object):

    customskill = 0
    customlang = 0
    bgskills = []
    bgFeat = []
    tools = []


    def __init__(self, name, extra_languages):
        self.name = name
        self.extra_languages = extra_languages

    def start(self):
        def start2():
            global masterfreeskill3
            global masterskillBG
            global masterextralang
            global mastertools
            global masterfeats
            masterfeats.extend(self.bgFeat)
            masterskillBG.extend(self.bgskills)
            mastertools.extend(self.tools)
            masterextralang += self.extra_languages
            masterextralang += self.customlang
            masterfreeskill3 += self.customskill
            print(masterskillBG)


        if self.name == "custom":
            print("A custom background is made from the following:\nOne feature among those mentioned in a 5e background (PHB pg. 127-141)\nAny two skill proficiencies\nA total of two tool or language proficiencies from existing D&D backgrounds")
            def bgskills_adder(self):
                def tool_adder(self, num):
                    while num > 0:
                        temptools = []
                        newskill = input("Please type a tool:\n")
                        if newskill in temptools:
                            print("Don't add the same tools twice")
                            tool_adder()
                        else:
                            temptools.append(newskill)
                            num -= 1
                    self.tools.extend(temptools)
                    print("You have selected:", self.tools)
                num = input("How many languages will you add to your custom background?")
                if num == "1":
                    self.customlang += 1
                    tool_adder(self, 1)
                    print("You will be able to select any language. You may select one tool proficiency")
                elif num == "2":
                    self.customlang += 2
                    print("You will be able to select any two languages. You will gain no new tool profiencies from your background")
                elif num == "0":
                    print("You gain no languages but will be ble to select two tools")
                    Background.tool_adder(self, 2)
                else:
                    print(texts.invalid)
                    Background.bgskills_adder(self)
            def feat_adder(self):
                feat = str(input("Please select a Background feat. from D&D 5e. Make sure to talk it over with your DM\n Type your feat. below\n"))
                self.bgfeat.append(feat)
            bgskills_adder(self)
            feat_adder(self)
            start2()
        else:
            start2()




class Acolyte(Background):
    bgskills = ["Insight", "Religion"]
    bgFeat = ["Shelter of the Faithful(pg. 127)"]

class Charlatan(Background):
    bgskills = ["Deception", "Sleight of Hand"]
    bgFeat = ["False Identity(pg. 128)"]
    tools = ["Disguise Kit", "Forgery Kit"]

class Criminal(Background):
    bgskills = ["Deception", "Stealth"]
    bgFeat = ["Criminal Contact(pg. 129)"]
    tools = ["One Type of Gaming Set", "Thieves' Tools"]

class Entertainer(Background):
    bgskills = ["Acrobatics", "Performance"]
    bgFeat = ["By Popular Demand(pg. 130)"]
    tools = ["Disguise Kit", "One Type of Musical Instrument"]

class FolkHero(Background):
    bgskills = ["Animal Handling", "Survival"]
    bgFeat = ["Hospitality(pg. 131)"]
    tools = ["One Type of Artisan's Tools", "Vehicles (land)"]

class GArtisan(Background):
    bgskills = ["Insight", "Persuasion"]
    bgFeat = ["Guild Membership(pg. 133)"]
    tools = ["One Type of Artisan's Tools"]

class Merchant(Background):
    bgskills = ["Insight", "Persuasion"]
    bgFeat = ["Guild Membership(pg. 133)"]
    tools = ["Navigator's Tools OR An additional Language"]

class Hermit(Background):
    bgskills = ["Medicine", "Religion"]
    bgFeat = ["Discovery(pg. 134)"]
    tools = ["Herbalism Kit"]

class Noble(Background):
    bgskills = ["History", "Persuasion"]
    bgFeat = ["Position of Privilege(pg. 135)"]
    tools = ["One Type of Gaming Set"]

class NobleKnight(Background):
    bgskills = ["History", "Persuasion"]
    bgFeat = ["Retainers(pg. 136)"]
    tools = ["One Type of Gaming Set"]

class Outlander(Background):
    bgskills = ["Athletics", "Survival"]
    bgFeat = ["Wanderer(pg. 136)"]
    tools = ["One Type of Musical Instrument"]

class Sage(Background):
    bgskills = ["Arcana", "History"]
    bgFeat = ["Researcher(pg. 138)"]

class Sailor(Background):
    bgskills = ["Athletics", "Perception"]
    bgFeat = ["Ship's Passage(pg. 139)"]
    tools = ["Navigator's Tools", "Vehicles(water)"]

class Pirate(Background):
    bgskills = ["Athletics", "Perception"]
    bgFeat = ["Bad Reputation(pg. 139)"]
    tools = ["Navigator's Tools", "Vehicles(water)"]

class Soldier(Background):
    bgskills = ["Athletics", "Intimidation"]
    bgFeat = ["Military Rank(pg. 140)"]
    tools = ["One Type of Gaming Set", "Vehicles(land)"]

class Urchin(Background):
    bgskills = ["Sleight of Hand", "Stealth"]
    bgFeat = ["City Secrets(pg. 141)"]
    tools = ["Disguise Kit", "Stealth"]

class Custom(Background):
    bgskills = []
    bgFeat = []
    tools = []


acolyte = Acolyte("acolyte", 2)
charlatan = Charlatan("charlatan", 0)
criminal = Criminal("criminal", 0)
entertainer = Entertainer("entertainer", 0)
folkhero = FolkHero("folkhero", 0)
gArtisan = GArtisan("guild_artisan", 1)
merchant = Merchant("merchant", 1)
hermit = Hermit("hermit", 1)
noble = Noble("noble", 1)
nobleknight = NobleKnight("knight", 1)
outlander = Outlander("outlander", 1)
sage = Sage("sage", 2)
sailor = Sailor("sailor", 0)
pirate = Pirate("pirate", 0)
soldier = Soldier("soldier", 0)
urchin = Urchin("urchin", 0)
custom = Custom("custom", 0)
