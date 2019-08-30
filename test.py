import random
import time

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
