import random

import creator
import dndclass
import backgrounds
import texts

#Aggregator for all other sheets

#GLOBALS
skills = []
allfreeskill = 0
#Sample Miscdict At The Bottom Of This Page
miscdict = {}
freelang = 0

feats = []
tools = []
weapons = []
armor = []

equip = []

saves = []
initi = 0

invalid = "\n\nInvalid input. Try again?\n"


def skillagg():
    global skills
    skills.extend(creator.masterracial_skills)
    global allfreeskill
    freeskillhere = creator.masterfreeskill + dndclass.masterfreeskill2 + backgrounds.masterfreeskill3
    allfreeskill += freeskillhere
    print("\n\nNow you will add your skills")
    print("From your race, you have gained the following:\n")
    print(", " .join(skills))
    print("From your class, you are allowed to pick %d skills from\n%s\n" % (dndclass.masterchoiceCL, ", " .join(dndclass.masterclassskill)))
    print("From your background, you have gained \n%s \n" % (", " .join(backgrounds.masterskillBG)))
    skills.extend(backgrounds.masterskillBG)
    print("From your race, class, and background, you have gained %d skills from any skills you have not already taken a proficiency in\n" % (freeskillhere))
    print("These are your total current skills")
    print(", " .join(skills))
    def class_skill_choice():
        choicenum = 0
        choicenum += dndclass.masterchoiceCL
        tempskills = []
        classskills = dndclass.masterclassskill
        if choicenum > 0:
            while choicenum > 0:
                new_skill = str(input("\nYou have %d skills to choose from %s.\nPlease type one below\n" % (choicenum, ", " .join(classskills))))
                tempskills.append(new_skill)
                choicenum -= 1
                # print(new_skill)
            print(", " .join(tempskills))
            conf = input("Is this good? (y/n)\n")
            if conf == "y" or conf == "yes":
                global skills
                skills.extend(tempskills)
            elif conf == "no" or conf == "n":
                class_skill_choice()
            else:
                print("oops!")
                class_skill_choice()
        else:
            pass
    def freeskills():
        global allfreeskill
        if allfreeskill > 0:
            print("\nYour current skills are:\n")
            global skills
            print(", " .join(skills))
            tempfree = 0
            tempfree += freeskillhere
            tempskill = []
            while tempfree > 0:
                newskill = str(input("\nYou have %d skills to select from any skill. Please type one below\n" % (tempfree)))
                tempskill.append(newskill)
                tempfree -= 1
            print(", " .join(tempskill))
            confi = input("Is this good?(y/n)\n")
            if confi == "y" or confi == "yes":
                skills.extend(tempskill)
            elif confi == "no" or confi == "n":
                freeskills()
            else:
                print(invalid)
                freeskills()

    class_skill_choice()
    freeskills()
    print("Your final skill list:\n")
    print(", " .join(skills))

def miscagg():
    global miscdict
    miscdict.update(creator.miscdictR)
    miscdict.update(dndclass.miscdictC)
    miscdict.update(backgrounds.miscdictBG)
    miscdict.update({"SUBRACE" : creator.mastersub})
    global saves
    saves.extend(dndclass.mastersavesCL)
    # print(miscdict)
    print(creator.masterstatsdict)
    print(creator.mastermodsdict)

def langagg():
    global freelang
    global miscdict
    freelang += backgrounds.masterextralang
    freelang += creator.freelang
    if miscdict["CLASS"] == "Druid":
        miscdict.update({"Secret Language" : "Druidic"})
    elif miscdict["CLASS"] == "Rogue":
        miscdict.update({"Secret Language" : "Thieves' Cant"})
    else:
        pass
    if freelang > 0:
        def freelangadd():
            tempfreelang = 0
            tempfreelang += freelang
            list = []
            print("You have %d languages to add to your character.  If you think the language is too far-fetched, talk it over with your DM\n" % (freelang))
            while tempfreelang > 0:
                inp = input("Please type a language\n")
                list.append(inp)
                tempfreelang -= 1
            confir = input("Are these correct?\n")
            print(", " .join(list))
            if confir == "y" or confir == "yes":
                miscdict.update({"Extra Languages" : ", " .join(list)})
            elif confir == "n" or confir == "no":
                freelangadd()
            else:
                print(invalid)
                freelangadd()
        freelangadd()
    else:
        pass
    # print(miscdict)

    # if freelang > 0:
    #     print("You have %d languages to add to your character.  If you think the language is too far-fetched, talk it over with your DM\n" % (freelang))
    #     while freelang > 0:
    #         inp = input("Please type a language")
def feattoolweaponarmoragg():
    global feats
    global tools
    global weapons
    global armor
    feats.extend(creator.masterfeatsR+dndclass.masterfeatsCL+backgrounds.masterfeats)
    tools.extend(creator.mastertoolsR+dndclass.mastertoolsCL+backgrounds.mastertools)
    weapons.extend(creator.masterweaponsR+dndclass.masterweaponsCL)
    armor.extend(creator.masterarmorR+dndclass.masterarmorCL)


def secPage():
    global miscdict
    def age():
        print("A(n) %s usually lives in this age range: %s" % (miscdict["RACE"], miscdict["AGE"]))
        inp = input("Please type your age:\n")
        conf = input("Your age is %s?(y/n) \n" % (inp))
        if conf == "y" or conf == "yes":
            miscdict["AGE"] = inp
        elif conf == "n" or conf == "no":
            age()
        else:
            print(invalid)
            age()
    def height():
        print("A(n) {} is around {} tall".format(miscdict["RACE"], miscdict["HEIGHT"]))
        inp = input("Please type your height:\n")
        conf = input("Your height is {}?\n".format(inp))
        if conf == "y" or conf == "yes":
            miscdict["HEIGHT"] = inp
        elif conf == "n" or conf == "no":
            height()
        else:
            print(invalid)
            height()
    def weight():
        print("A(n) {} {}".format(miscdict["RACE"], miscdict["WEIGHT"]))
        inp = input("Please type your weight:\n")
        conf = input("Your weight is {}?\n".format(inp))
        if conf == "y" or conf == "yes":
            miscdict["WEIGHT"] = inp
        elif conf == "n" or conf == "no":
            weight()
        else:
            print(invalid)
            weight()
    def eye():
        inp = input("What is your eye color?\n")
        conf = input("Your eye color is {}?\n".format(inp))
        if conf == "y" or conf == "yes":
            miscdict.update({"EYES" : inp })
        elif conf == "n" or conf == "no":
            eye()
        else:
            print(invalid)
            eye()
    def skin():
        inp = input("What is your skin color?\n")
        conf = input("Your skin color is {}?\n".format(inp))
        if conf == "y" or conf == "yes":
            miscdict.update({"SKIN" : inp })
        elif conf == "n" or conf == "no":
            skin()
        else:
            print(invalid)
            skin()
    def hair():
        inp = input("What is your hair color?\n")
        conf = input("Your hair color is {}?\n".format(inp))
        if conf == "y" or conf == "yes":
            miscdict.update({"HAIR" : inp })
        elif conf == "n" or conf == "no":
            hair()
        else:
            print(invalid)
            hair()
    age()
    height()
    weight()
    eye()
    skin()
    hair()

def align():
    print("Now you wil choose your alignment")
    if miscdict["CLASS"] == "CLeric" or miscdict["CLASS"] == "Paladin":
        print("Please be advised. As a %s, your alignment should be compatible with your God as according to your DM" % (miscdict["CLASS"]))
    else:
        pass
    inp = input("Please type your alignment below:\n")
    confi = input("Your alignment is %s?(y/n)" % (inp))
    if confi == "y" or confi == "yes":
        miscdict.update({"Alignment" : inp})
    elif confi == "n" or confi == "no":
        align()
    else:
        print(invalid)
        align()

def equipagg():
    equip.extend(dndclass.masterequipCL)
    equip.extend(backgrounds.masterequip)

def agg():
    skillagg()
    miscagg()
    langagg()
    secPage()
    align()
    feattoolweaponarmoragg()
    equipagg()
    # print(miscdict)



#Sample miscdict:
#All apostrophes are actually quotes
# {'RACE': 'Drangonborn', 'AGE': '16', 'SIZE': 'Medium', 'SPEED': 30, 'Languages': 'Common, Draconic', 'Secret Language' : 'Theives' Cant', 'HEIGHT': '7', 'WEIGHT': '250', 'HP': 11, 'HitDie': 10, 'CLASS': 'Paladin', 'Proficience Bonus': 2, 'BACKGROUND': 'Sage', 'Extra Languages': 'Infernal, Dwarvish', 'EYES': 'green', 'SKIN': 'brown', 'HAIR': 'bald', 'Alignment': 'NN'}
