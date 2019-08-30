import random
import time



invalid = "\n\nInvalid input. Try again?\n"



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



#def standard_pointbuy():
#    stan = True




def pointbuy():
    print("Welcome to the character roller.")
    pbresp = input("Starting Pointbuy. \nStandard(stan)? or full(full)?\n")
    if pbresp == "stan":
        stan = True
    elif pbresp == "full":
        stan = False
    else:
        print(invalid)
        pointbuy()
    if stan == True:
        start = 8
    else:
        start = 0
    statsdict = {
    "STR": start,
    "DEX": start,
    "CON": start,
    "INT": start,
    "WIS": start,
    "CHA": start,
    }

    tp = 0

    if stan == True:
        tp += 27
    elif stan == False:
        tp += 75


    def statstatus():
        for x in statsdict:
            print(x, ":", statsdict[x])
    print("Starting with:")
    for x in statsdict:
        statstatus()
        print("Total points available:", tp)
        print("What will you add to:")
        add = int(input(x))
        pls = statsdict[x] + add
        if stan == True and pls <= 15 and add <= tp:
            statsdict[x] = pls
            tp -= add
        elif stan == True and pls > 15:
            input ("Sorry! Standard point buy doesn't allow for values over 15!\nTry doing a full pointbuy and making sure all values are over 8 \nif you'd like to break this rule!")
            pointbuy()
        elif stan == True and add > tp:
            input("Whoops! You maxed out your tp! Run your calculations again.")
            pointbuy()
        elif stan == False and pls <= 20 and add <= tp:
            statsdict[x] = pls
            tp -= add
        elif stan == False and pls > 20:
            input("Whoops! 20 is as high as you can go without crazy magic.")
            pointbuy()
        elif stan == False and add > tp:
            input("Whoops! You maxed out your tp! Run your calculations again.")
            pointbuy()
        else:
            input("How did you even get here?")
            pointbuy()

#    STRn = statsdict["STR:"]
    statstatus()
    print("Total points available:", tp)



def die3d6():
    print("Welcome to the character roller.")
    count = int(input("How many stats would you like to roll?"))
    print("Rolling 3d6 for your stats:")
    time.sleep(.25)
    endstats = []
    while count >= count >0:
        def threeD6():
            roll2 = list(roll(3,6," "))
            print(roll2)
            total = sum(roll2)
            print(total)
            endstats.append(total)
        threeD6()
        count -= 1
    print(endstats)
    resp = input("Roll another character? (y/n)")
    if resp == "y" or resp == "1" or resp == "yes":
        die3d6()
    elif resp == "n" or resp == "no" or resp == "0":
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
            for x in statsdict:
                statstatus()
                print("Choose a value from:", endstats)
                val = int(input(x))
                statsdict[x] = val
                usedvalues.append(val)
            statstatus()
            usedvalues.sort(reverse=True)
            endstats.sort(reverse=True)
            print("You used these values:", usedvalues)
            print("Your original rolls were:", endstats)
            conf = input("Are these stats acceptable? (y/n)")
            if conf == "y" or conf == "yes" or conf == "1":
                print("Your final stats are:")
                statstatus()
                return statsdict
            elif conf == "n" or conf == "no" or conf == "0":
                statsadd()
            else:
                return
        statsadd()
    else:
        return




def die4d6():
    print("Welcome to the character roller.")
    print("Rolling with starting rules 4d6, pick best three, lowest replaced with 18")
    time.sleep(.25)
    stat = input("How many stats would you like to roll?\n")
    stats = int(stat)
    endstats = []
    while stats >= stats > 0:
        def fourDsix():
            roll1 = list(roll(4,6," "))
            roll1.sort(reverse=True)
            roll1.pop()
            print(roll1)
            total1 = sum(roll1)
            print(total1)
            endstats.append(total1)

        fourDsix()
        stats = stats-1
    print(endstats)
    stanendstats = endstats.copy()
    print("Making the lowest an 18")
    time.sleep(.35)
    endstats.sort(reverse=True)
    endstats.pop()
    endstats.append(18)
    endstats.sort(reverse=True)
    print(endstats)
#    print(stanendstats)
    resp = input("Roll another character? (y/n)")
    if resp == "y" or resp == "1" or resp == "yes":
        die4d6()
    elif resp == "n" or resp == "no" or resp == "0":
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
            for x in statsdict:
                statstatus()
                stanendstats.sort(reverse=True)
                print("Choose a value from: \nStandard Set:", stanendstats, "\nHomebrew set:", endstats)
                val = int(input(x))
                statsdict[x] = val
                usedvalues.append(val)
            statstatus()
            usedvalues.sort(reverse=True)
            endstats.sort(reverse=True)
            print("You used these values:", usedvalues)
            print("Your original rolls were:", endstats)
            conf = input("Are these stats acceptable? (y/n)")
            if conf == "y" or conf == "yes" or conf == "1":
                print("Your final stats are:")
                statstatus()
                return statsdict
            elif conf == "n" or conf == "no" or conf == "0":
                statsadd()
            else:
                return
        statsadd()
    else:
        return
