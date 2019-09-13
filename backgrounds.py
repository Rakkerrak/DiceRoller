

import texts




#handles the backgrounds

#GLOBALS
masterfreeskill3 = 0
masterskillBG = []
masterextralang = 0
miscdictBG = {}

mastertools = []
masterfeats = []

masterequip = []



class Background(object):

    customskill = 0
    customlang = 0
    bgskills = []
    bgFeat = []
    tools = []
    equip = []


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
            global miscdictBG
            masterfeats.extend(self.bgFeat)
            masterskillBG.extend(self.bgskills)
            mastertools.extend(self.tools)
            masterextralang += self.extra_languages
            masterextralang += self.customlang
            masterfreeskill3 += self.customskill
            miscdictBG.update({"BACKGROUND" : self.name})
            # print(masterskillBG)

##THIS IS FOR CUSTOM BG ONLY
        if self.name == "Custom":
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
    equip = ["A holy symbol(a gift to you when you entered the priesthood)", "a prayer book or prayer wheel", "5 sticks of incense", "vestments", "an set of common clothes", "a pouch containing 15 gp"]


class Charlatan(Background):
    bgskills = ["Deception", "Sleight of Hand"]
    bgFeat = ["False Identity(pg. 128)"]
    tools = ["Disguise Kit", "Forgery Kit"]
    equip = ["a set of fine clothes", "a disguise kit", "tools of the con of your choice: ten stoppered bottles filled with colorful liquid OR a set of weighted dice OR a deck of marked cards OR a signet ring of an imaginary duke", "a pouch containing 15 GP"]

class Criminal(Background):
    bgskills = ["Deception", "Stealth"]
    bgFeat = ["Criminal Contact(pg. 129)"]
    tools = ["One Type of Gaming Set", "Thieves' Tools"]
    equip = ["a crowbar", "a set of dark common clothes including a hood", "a pouch containing 15 gp"]

class Entertainer(Background):
    bgskills = ["Acrobatics", "Performance"]
    bgFeat = ["By Popular Demand(pg. 130)"]
    tools = ["Disguise Kit", "One Type of Musical Instrument"]
    equip = ["one musical instrument", "a token from an adrmirer", "a costume", "a pouch containing 15 gp"]

class FolkHero(Background):
    bgskills = ["Animal Handling", "Survival"]
    bgFeat = ["Hospitality(pg. 131)"]
    tools = ["One Type of Artisan's Tools", "Vehicles (land)"]
    equip = ["a set of artisan's tools", "a shovel", "an iron pot", "a set of common clothes", "a pouch containing 10 gp"]

class GArtisan(Background):
    bgskills = ["Insight", "Persuasion"]
    bgFeat = ["Guild Membership(pg. 133)"]
    tools = ["One Type of Artisan's Tools"]
    equip = ["a set of artisan's tools", "aletter of introduction from your guild", "a set of traveler's clothes", "a pouch containing 15 gp"]

class Merchant(Background):
    bgskills = ["Insight", "Persuasion"]
    bgFeat = ["Guild Membership(pg. 133)"]
    tools = ["Navigator's Tools OR An additional Language"]
    equip = ["Navigator's Tools OR a mule and cart", "a letter of introduction from your guild", "a set of traveler's clothes", "a pouch containing 15 gp"]

class Hermit(Background):
    bgskills = ["Medicine", "Religion"]
    bgFeat = ["Discovery(pg. 134)"]
    tools = ["Herbalism Kit"]
    equip = ["a scroll case stuffed full of notes from your studies or prayers", "a winter blanket", "a set of common clothes", " an herbalism kit", "5 gp"]

class Noble(Background):
    bgskills = ["History", "Persuasion"]
    bgFeat = ["Position of Privilege(pg. 135)"]
    tools = ["One Type of Gaming Set"]
    equip = ["a set of fine clothes, a signet ring", "a scroll of pedigree", "a purse containing 25gp"]

class NobleKnight(Background):
    bgskills = ["History", "Persuasion"]
    bgFeat = ["Retainers(pg. 136)"]
    tools = ["One Type of Gaming Set"]
    equip = ["a set of fine clothes, a signet ring", "a scroll of pedigree", "a purse containing 25gp", "option: a banner or token from the noble you have sworn fealty or devotion to"]

class Outlander(Background):
    bgskills = ["Athletics", "Survival"]
    bgFeat = ["Wanderer(pg. 136)"]
    tools = ["One Type of Musical Instrument"]
    equip = ["a staff", "a hunting trap", "a trophy from an animal you killed", "a set of traveler's clothes", "a pouch containing 10 gp"]

class Sage(Background):
    bgskills = ["Arcana", "History"]
    bgFeat = ["Researcher(pg. 138)"]
    equip = ["a bottle of black ink", "a quill", "a small knife", "a letter from a dead colleagu posing a question you have not yet been able to answer", "a set of common clothes", "a pouch containing 10 gp"]

class Sailor(Background):
    bgskills = ["Athletics", "Perception"]
    bgFeat = ["Ship's Passage(pg. 139)"]
    tools = ["Navigator's Tools", "Vehicles(water)"]
    equip = ["a belaying pin(club)", "50 feet of silk rope", "a lucky charm such as a rabbit's foot or small stone with a hole in the center(or you may roll for a random Trinket on page 160-161)", "a set of common clothes", "a pouch containing 10 gp"]

class Pirate(Background):
    bgskills = ["Athletics", "Perception"]
    bgFeat = ["Bad Reputation(pg. 139)"]
    tools = ["Navigator's Tools", "Vehicles(water)"]
    equip = ["a belaying pin(club)", "50 feet of silk rope", "a lucky charm such as a rabbit's foot or small stone with a hole in the center(or you may roll for a random Trinket on page 160-161)", "a set of common clothes", "a pouch containing 10 gp"]

class Soldier(Background):
    bgskills = ["Athletics", "Intimidation"]
    bgFeat = ["Military Rank(pg. 140)"]
    tools = ["One Type of Gaming Set", "Vehicles(land)"]
    equip = ["an insignia of rank", "a trophy taken from a fallen enemy(a dagger, broken blade, or piece of a hammer)", "a set of bone dice OR deck of cards", "a set of common clothes", "a pouch containing 10 gp"]

class Urchin(Background):
    bgskills = ["Sleight of Hand", "Stealth"]
    bgFeat = ["City Secrets(pg. 141)"]
    tools = ["Disguise Kit", "Stealth"]
    equip = ["a small knife", "a map of the city you grew up in", "a pet mouse", "a token to remember your parents by", "a set of common clothes", "a pouch containing 10 gp"]

class Custom(Background):
    bgskills = []
    bgFeat = []
    tools = []


acolyte = Acolyte("Acolyte", 2)
charlatan = Charlatan("Charlatan", 0)
criminal = Criminal("Criminal", 0)
entertainer = Entertainer("Entertainer", 0)
folkhero = FolkHero("Folk Hero", 0)
gArtisan = GArtisan("Guild Artisan", 1)
merchant = Merchant("Merchant", 1)
hermit = Hermit("Hermit", 1)
noble = Noble("Noble", 1)
nobleknight = NobleKnight("Knight", 1)
outlander = Outlander("Outlander", 1)
sage = Sage("Sage", 2)
sailor = Sailor("Sailor", 0)
pirate = Pirate("Pirate", 0)
soldier = Soldier("Soldier", 0)
urchin = Urchin("Urchin", 0)
custom = Custom("Custom", 0)
