import random
import time
import os
# import string

# import char
# import creator
# import dndclass

# import datetime from datetime

dict1 = {"a" : 3,
"c" : 5,
"b" : 2}

dict2 = {"F" : 8,
"v" : 4,
"b" : 7}

dict1.copy(dict2)
print(dict1)
print(dict2)
"""
import agg

miscdict = {"RACE" : "halfling", "CLASS" : "Cleric", "AGE" : 25}

name = "{}{}{}".format(agg.miscdict["RACE"], agg.miscdict["CLASS"], agg.miscdict["AGE"])
print(name)

# print(datetime.day + datetime.month + datetime.year + datetime.hour + datetime.minute)
"""
"""
os.system('libreoffice Charsheet.txt')
"""
"""
stats = {
"STR" : 0,
"DEX" : 1,
"CON" : 3,
"WIS" : 4,
"INT" : 4,
"CHA" : 6
}
mods = {
"STR" : 10,
"DEX" : 11,
"CON" : 13,
"WIS" : 14,
"INT" : 14,
"CHA" : 16
}

skills = ["Animal Handling", "Perception", "Intimidation"]
allfreeskill = 0
miscdict = {"RACE" : "Human", "AGE" : 25, "SIZE" : "Medium", "SPEED" : 15, "Languages" : "lingo", "HP" : 10, "HitDie" : 12, "CLASS" : "Cleric", "Proficience Bonus" : 5, "BACKGROUND" : "Criminal", "Alignment" : "CN", "Secret Language" : "Mormonism"}
freelang = 0

feats = ["This is a feat(pg. 5)", "This is another(pg. 6)"]
tools = ["Thieves' Tools", "Herbalistm Kit"]
weapons = ["simple", "martial"]
armor = ["light", "medium"]


equip = ["a", "bunch", "of", "crap"]

saves = ["CHA", "WIS"]
initi = 0

def start():
    file = open("Charsheet.txt", "a+")

    file.write("\nClass & Level : {} lvl 1      Background: {}".format(miscdict["CLASS"], miscdict["BACKGROUND"]))
    file.write("\nRace: {}      Alignment: {}".format(miscdict["RACE"], miscdict["Alignment"]))
    file.write("\n\n    Your stats")
    for x in stats:
        file.write("\n{} : {}".format(x, stats[x]))
    file.write("\n\n    Your modifiers")
    for x in mods:
        file.write("\n{} : {}".format(x, mods[x]))
    file.write("\n\nSave Proficiencies:")
    for x in saves:
        file.write(" \n{}".format(x))
    file.write("\n\nSkill Proficiencies:")
    for x in skills:
        file.write("\n{}".format(x))
    file.write("\n\nSpeed: {}       HP: {}       Hit die: d{}".format(miscdict["SPEED"], miscdict["HP"], miscdict["HitDie"]))
    file.write("\n\nThese are your Tool Proficiencies:")
    for x in tools:
        file.write("\n{}".format(x))
    file.write("\n\nThese are your Weapon Proficiencies:")
    for x in weapons:
        file.write("\n{}".format(x))
    file.write("\n\nThese are your Armor Proficiencies:")
    for x in armor:
        file.write("\n{}".format(x))
    file.write("\n\nThese are your character's feats, including page numbers you can find them on.  Some things have already been added into your character's stats such as proficiencies and stat bonuses.")
    for x in feats:
        file.write("\n{}".format(x))
    file.write("\nLanguages: {}".format(miscdict["Languages"]))
    if "Secret Language" in miscdict:
        file.write("\nSecret Language: {}".format(miscdict["Secret Language"]))
    if "Extra Languages" in miscdict:
        file.write("\nExtra Languages: {}".format(miscdict["Extra Languages"]))
    file.write("\nEquipment:\n")
    for x in equip:
        file.write("{}, ".format(x))
    file.write("\n\n\nUseful page numbers: \nArmor(to calculate Initiative): pg. 143      Weapons: pg 149         \nEquipment 'Packs'(and the general area for all other equipment): pg. 151 \nLanguages: pg123     Optional Starting Gold(Remove all equipment and gold and self-buy): pg. 143 \nNon-Background Features(Choose one if you're a variant Human!): pg.165")
start()
"""
"""
#This syntax works to reference a function in a child class

class Arms(object):

    def __init__(self, name):
        self.name = name

    def start(self):
        if self.name == "Cow":
            print("workingdocus")
        else:
            self.start(self)

class Leg(Arms):

    def start(self):
        print("porcupine")

leg = Leg("Leg")

leg.start()
"""


"""
#Equip test


def equiplong():
    equip = []
    eql = ["a", "d", "c"]
    # for x in eql:
    # chool = input("Please choose from the following: \n%s \n%s \n%s" % (eql[0], eql[1], eql[2]))
    # # chooldict = {"1" : equip.extend(eql[0]), "2" : equip.extend(eql[1]), "3" : equip.extend(eql[2])}
    # if chool in chooldict:
    #     chooldict[chool]
    # else:
    #     print("error")
    ans = int(input("Please choose from the following: \n%s \n%s \n%s" % (eql[0], eql[1], eql[2])))
    ans -= 1
    equip.extend(eql[ans])
    print(equip)
    print(eql[0])

equiplong()

quip = []

def equip():
    quipdict = {"a" : "b", "c" : "d"
    }

    global quip
    for x in quipdict:
        choose = int(input("Which? \n1: %s\n2: %s \n" % (x, quipdict[x])))
        if choose == 1:
            quip.append(x)
        if choose == 2:
            quip.append(quipdict[x])

# while True:
#     equip()
#     # global quip
#     print(quip)



# """
"""
a = ["1", "2"]
b = ["3", "4"]

c = []

c.extend(a+b)

print(c)


"""
"""
# Yeah global matters
marking = 0

def change():
    global marking
    marking += 2

change()
print(marking)
"""
"""
#Huh....
msub = []
class Mork(object):
    sub = []

    def __init__(self, portals):
        self.portals = portals

    def start(self):
        self.portals += 1
        print(self.portals)
        self.sub.append("Markle")
        global msub
        msub.extend(self.sub)


corp = Mork(5)

corp.start()
print(msub)
"""
"""
self = ["Monkey"]

def func():
    if self == []:
        pass
    else:
        print("didn't work")
        for x in self:
            x.lower()
            print(self)
mork = ["Caterpullars", "Macteria"]
self.extend(mork)
self.append(["Carterpullers"])

func()


"""

"""
miscdict = {"AGE" : "150-250", "NAME" : "Elf", "CLASS" : "Cleric"}

def align():
    print("Now you wil choose your alignment")
    if miscdict["CLASS"] == "CLeric":
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

align()
print(miscdict)
"""
"""
def ageagg():
    global miscdict
    print("A(n) %s usually lives in this age range: %s" % (miscdict["NAME"], miscdict["AGE"]))
    inp = input("Please type your age:\n")
    conf = input("Your age is %s?(y/n) \n" % (inp))
    if conf == "y" or conf == "yes":
        miscdict["AGE"] = inp
    elif conf == "n" or conf == "no":
        ageagg()
    else:
        print(invalid)

ageagg()
print(miscdict)
"""
"""
freelang = 2
dict = {}
def func():
    if freelang > 0:
        tempfreelang = 0
        tempfreelang += freelang
        list = []
        print("You have %d languages to add to your character.  If you think the language is too far-fetched, talk it over with your DM\n" % (freelang))
        while tempfreelang > 0:
            inp = input("Please type a language\n")
            list.append(inp)
            tempfreelang -= 1
    dict.update({"Extra Languages" : ", " .join(list)})
    print(dict)
func()

"""
"""
#You must declare the dict before you update?
miscdictR = {}
a = 2
b = 3
tempdict = {"NAME" : a, "AGE" : b }
miscdictR.update(tempdict)


print(miscdictR)
"""
"""
# adding to dictionaries using outside variables

a1 = {"a" : 2, "d" : 54}
b =  "x"
c = 5
newdict = {b : c}
print(newdict)
a1.update(newdict)
print(a1)

"""
"""
#Strings formatted to not look like hot garbo
a = ["core", "message", "what", "even", "is", "it"]
print("Can I do this %s" % (", " .join(a)))
print("\n","Can I do this %s" % (", " .join(a)) )
"""
"""
#extend vs append because i didn't get it the first six times
a = ["a", "b"]
b = ["c", "d"]

a.extend(b)
print(a)

a.append(b)

print(a)

f = "corpse"

a.extend(f)
print(a)
##v This one works
a.append(f)
print(a)
"""

"""
skills = ["core"]

def skillagg():
    global skills
    # skills.extend(creator.masterracial_skills)
    def class_skill_choice():
        masterchoiceCL = 3
        masterclassskill = ["a"]
        choicenum = 0
        choicenum += masterchoiceCL
        tempskills = []
        classskills = masterclassskill
        if choicenum > 0:
            while choicenum > 0:
                new_skill = str(input("You have %d skills to choose from %s.Please type one below\n" % (choicenum, classskills)))
                tempskills.append(new_skill)
                choicenum -= 1
                print(new_skill)
            print(tempskills)
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

    class_skill_choice()
    print(skills)

skillagg()

# """
"""
int = 6
inp = input("Please choose %d skills" % (int))
"""

"""
#This works
def func():
    a = ["a", "b"]
    b = ["d"]
    a.extend(b)
    print(a)
func()
"""

"""
#FILE WRITING PRACTICE
cows = "cows have legs"

crabs = ["1", "2", "3", "4"]
# strcrabs = str(crabs)
# f=open("guru99.txt", "a+")
# for i in range(2):
#      f.write("Appended line %d\r\n%s\n%s"  % (i+15, cows, strcrabs))
# print(strcrabs)
f=open("test.txt", "a+")
f.write("Feats:\n")
for x in crabs:
    f=open("test.txt", "a+")
    f.write("%s\n" % (x))

f = open("test.txt")
lines = f.readlines()
print(lines[2])
print(lines[1])


max = []
def add(num):
    num2 = int(num)
    line = f.readlines()
    max.append(line[num2])
add(3)


read = f.readlines()
for x in read:
    print(x)
"""


"""
a+ makes new file. allows read and append
r+ does not make new file. allows write and read
\t tab
\n line break
\r return to the beginning of the line
%s is a placeholder for a string
    [list] is formatted with " and ,
        str(list) doesn't fix that
%d is a placeholderlder for a number % (i+0) defines starting number?
"""
"""
#add a string to a list with append not extend
def func():
    feats = []
    feat = str(input("Please select a Background feat. from D&D 5e. Make sure to talk it over with your DM\n Type your feat. below\n"))
    feats.append(feat)
    print(feats)

func()
"""
"""
#OH MY GOSH SOMETHING WORKED FIRST TRY HALLELUJAH
def add():
    list = []
    addition = input("gah")
    list.append(addition)
    print(list)
add()
"""
"""
#Still no and I'm tired
words = ['hello,','i','am','ROB','ALSOD',"i'm", "how do"]
words2 = [word[:1].upper() + word[1:] for word in words]
print(words2)
"""

"""
#AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
stre = ["mar", "mark's"]

def cap():
    str = ["mar", "mark's"]
    for x in str:
        x.join(w.capitalize() for w in x.split())
    print(str)

def cap2():
    str = ["mar", "mark's"]
    for x in str:
        string.capwords(x)
    print(str)

def cap3():
    str = ["mar", "mark's"]
    for x in str:
        str[x].title()
    print(str)
cap2()
cap3()
print(stre[1].capitalize())
"""
"""
#This doesn't work. Sad.
#Scratch tha. It works with a while loop not a for loop booyah

def func(can):
    while can > 0:
        print("This is a number")
        can -= 1

func(2)
"""

"""
a = [1, 2, 3, 4, 5]
print(' '.join(map(str, a)))

print("in new line")
print('\n'.join(map(str, a)))

print("a     b c")
"""
"""
#DICTIONARY COPY METHODS
dicta = {
"a" : 5,
"b" : 5,
"c" : 4
}

dictb = dicta
dictc = dict(dicta)
dictd = dicta.copy()

dicta = {
"a" : 5,
"b" : 6,
"c" : 45
}

print(dicta)
print(dictb)
print(dictc)
print(dictd)
"""

"""
tup = (None)
print(tup)

"""
"""
#CONVERTS STATS TO MODS
set = int(5.5)
print(set)

dict = {
"A" : 5,
"B" : 16,
"C" : 18,
"D" : 13,
"E" : 15
}
def func():
    dict2 = dict.copy()
    for x in dict2:
        dict2[x] -= 10
        dict2[x] = dict2[x] // 2
    print(dict2)

func()
"""
"""
# HI IM DUMB
start = 0

masterstatsdict = {
"STR": start,
"DEX": start,
"CON": start,
"INT": start,
"WIS": start,
"CHA": start,
}

def chaUD():
     masterstatsdict["CHA"] += 1
def intUD():
     masterstatsdict["INT"] += 1
def wisUD():
     masterstatsdict["WIS"] += 1

def subraceMod():
    ans = input("As an elf you get to pick betwen \nHigh Elf(hi), \nWood elf(wood, \nDark Elf/Drow(dark)\n")
    ansdict = {"hi": intUD, "Hi": intUD, "1": intUD, "wood": wisUD, "Wood": wisUD, "2": wisUD, "dark": chaUD, "Dark": chaUD, "3": chaUD}
    if ans in ansdict:
        ansdict[ans]()
        print(masterstatsdict)
    else:
        print(invalid)
        subraceMod()



def statsOpt():
    statOptDict = {"4d6": char.die4d6, "3d6": char.die3d6, "point": char.pointbuy}
    stat_options = input("Standard 4d6 with home rules option(4d6)? \n3d6(3d6?)\nor pointbuy(point)?\n")
    if stat_options in statOptDict:
        statOptDict[stat_options]()
    else:
        print(invalid)

# statsOpt()
subraceMod()
"""
"""
#WHY WONT MY CHILD FUNCTIONS OVERRIDE THE PARENT CLASSSSSS

class Morals(object):
    def start(self):
        print("Muskrats")

class Milk(Morals):
    def start(self):
        print("Mongrels")

cows = Milk()

cows.start()
"""
"""
dict = {"a": 5, "b": 65465}

print(dict["a"])


def run():
    print("You've won!")



def maxy():
    choices = {"cows": run, "Elf": 7}
    imps = input("cows Elf")
    if imps in choices:
        choices[imps]()

#        print(out)
#        if out == 7:
#            run()
#        elif out == 8:
#            print(choices[imps])
    else:
        "Whoops!"
        maxy()

maxy()
"""
"""
#CLASS PRACTICE
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Max(object):
    setvar = 5
    setvar2 = "an uwu"

    def __init__ (self, marx, karl, carpl):
        self.marx = marx
        self.karl = karl
        self.carpl = carpl

    def marxymoo(self):
        return print(self.karl, self.marx, "is", self.setvar2)

Commie = Max("Marx", "Karl", "Carpool")

print(Commie.marxymoo())
"""
"""
def roll(amount, sides, message):
    numb = int(amount)
    dwhat = int(sides)
    results = []
    while numb >= numb > 0:
        result = random.randint(1,dwhat)
        print(message, result)
        results.append(result)
        numb = numb-1
    return(results)
"""

"""
BABY STATSTATUS
def statstatus():
    for x in statsdict:
        print(x, ":", statsdict[x])



def statsadd():

    statsdict = {
        "STR": 0,
        "DEX": 0,
        "CON": 0,
        "INT": 0,
        "WIS": 0,
        "CHA": 0,
    }
    usedvalues = []
    def statstatus():
        for x in statsdict:
            print(x, ":", statsdict[x])
#    while _ >= 6 > 0:
    for x in statsdict:
        statstatus()
        print("Choose a value for:")
        val = input(x)
        statsdict[x] = val
        usedvalues.append(val)
    statstatus()
    print("You used these values:")
    print(usedvalues)
statsadd()
"""




"""
#list = [5, 6, 7]
list = list(input("type"))
dict = {
    "STR": "q",
    "DEX": "1",
    "CON": "c"
    }

print(list)
print(dict)
"""

"""
#RETURN PRACTICE
def f1():
    seth = random.randint(1,10)
    return seth

def f2():
    seth = random.randint(11,20)
    return print(seth)

cows = input("Cows")
if cows == "1":
    f2()

elif cows == "0":
    f2()


def f3():
    print(5 * int(f1()))

f3()

print(f1())
"""
"""

#LISTS INTO DICTIONARIES
list = [5,6]

dict = {
"a": 1,
"b": 2
}

for x in dict:
    for i in list:
        dict[x] = i

print(dict)
"""



"""
#DICTIONARY FORMATTING
for x in dict:
    print(x, dict[x])


for x in dict:
    for x in dict:
        print(x, dict[x])
    add = int(input("add"))
    pls = dict[x] + add
    dict[x] = pls

for x in dict:
    print(x, dict[x])
"""

"""
#THE BEGINNING OF UTTER CRAP
    INTadd = int(input("What will you add to INT?\n"))
    INTpls = statsdict["INT:"] + INTadd
    if stan == True and INTpls <= 15:
        statsdict["INT:"] = INTpls
        tp -= INTadd
"""
"""
#BABY DICE ROLLER
def roll(amount, sides, message):
    numb = int(amount)
    dwhat = int(sides)
    results = []
    while numb >= numb > 0:
        result = random.randint(1,dwhat)
        print(message, result)
        results.append(result)
        numb = numb-1
    return(results)
"""



"""
#TIME MODULE TEST
print("Hello")
time.sleep(2.0)
print("Goodbye")
"""



"""
#MORE BABY DICE ROLLERS
def roll(amount, sides, message):
    numb = int(amount)
    dwhat = int(sides)
    results = []
    while numb >= numb > 0:
        result = random.randint(1,dwhat)
        print(message, result)
        results.append(result)
        numb = numb-1
    print(results)


roll(2,6,"Done")
print(results)
"""
"""
#UTTER CRAP
    STRadd = int(input("What will you add to STR?\n"))
    STRpls = statsdict["STR:"] + STRadd
    if stan == True and STRpls <= 15:
        statsdict["STR:"] = STRpls
        tp -= STRadd
    statstatus()
    DEXadd = int(input("What will you add to DEX?\n"))
    DEXpls = statsdict["DEX:"] + DEXadd
    if stan == True and DEXpls <= 15:
        statsdict["DEX:"] = DEXpls
        tp -= DEXadd
    statstatus()
    CONadd = int(input("What will you add to CON?\n"))
    CONpls = statsdict["CON:"] + CONadd
    if stan == True and CONpls <= 15:
        statsdict["CON:"] = CONpls
        tp -= CONadd
    statstatus()
    INTadd = int(input("What will you add to INT?\n"))
    INTpls = statsdict["INT:"] + INTadd
    if stan == True and INTpls <= 15:
        statsdict["INT:"] = INTpls
        tp -= INTadd
    statstatus()


    DEXpls = statsdict["DEX:"] + int(input("What will you add to DEX?\n"))
    if stan == True and DEXpls <= 15 and STRpls + DEXpls <= tp :
        statsdict["DEX:"] = DEXpls
    CONpls = statsdict["CON:"] + int(input("What will you add to CON?\n"))
    if stan == True and CONpls <= 15 and STRpls + CONpls + DEXpls<= tp :
        statsdict["CON:"] = CONpls
    INTpls = statsdict["INT:"] + int(input("What will you add to INT?\n"))
    if stan == True and INTpls <= 15 and STRpls + INTpls + DEXpls + CONpls <= tp :
        statsdict["INT:"] = INTpls

    print()
    for x in statsdict:
        print(x, statsdict[x])
"""
