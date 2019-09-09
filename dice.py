import random
import time

import char
import diceroll
import creator
import texts
import dndclass
import backgrounds
import agg


invalid = "\n\nInvalid input. Try again?\n"

while True:
    print("Welcome to the dice roller.")
    time.sleep(0.25)
    start = input("Would you like to: \nRoll dice (roll), \nroll a character(stats)\ncreate a character(create)\n")
    if start == "roll":
        print("When prompted please input the number of sides for your dice and the amount of them you would like to roll.")
        diceroll.diceroll()
    elif start == "stats":
        creator.statsOpt()
    elif start == "create":
        texts.raceOpt()
        texts.classOpt()
        texts.bgOpt()
        agg.agg()
        # dndclass.cleric.start()
        # print("choicecheck", dndclass.cleric.choiceCL)
        # print("creatorpage", creator.masterfreeskill)
        # print("dndpagedice", dndclass.masterfreeskill2)
    elif start == "test":
        texts.bgOpt()

    else:
        time.sleep(.25)
        print(invalid)









#def die(sides):
#    sides = inp(int)
#    inp = input("What would you like to roll? \n")
#    roll = random.randint(1,sides)
#    print("You have rolled" + random.randint(1,sides))

#while True:
#    inp = input("What would you like to roll? \n")
#    die(inp)

#if True:
#    die()
#    else:
#    print("Not sure what yuo mean")



#name2 = input("Ebter Character Name")
#charclass = input("Enter Character Class")
#level = input("Enter Character Level")
#line1 = "{0} is a level {2} {1}"

#print(line1.format(name2, charclass, level,))
