import random
import time
import string

# import char
# import creator
# import dndclass
a = ["a", "b"]
b = ["c", "d"]

a.extend(b)
print(a)

a.append(b)

print(a)

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
