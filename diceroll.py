import random


invalid = "\n\nInvalid input. Try again?\n"

def diceroll():

    while True:
#        numdooside = input("What would you like to roll?\n")
#        num, doo, side, = numdooside.split(",")
        num = int(input("Amount?\n"))
        side = int((input("Sides?\n")))
#        max = int(side)
#        times = int(num)

        allrolls = []

        while num >= num > 0:
            roll = random.randint(1,side)
            print("You have rolled",roll)
            allrolls.append(roll)
            num = num-1

        print(allrolls)
        total = sum(allrolls)
        print("Total:", total)
        confirm = input("Again?\n")
        if confirm == "yes" or confirm =="y":
            print("All right!")
            continue
        elif confirm == "n" or confirm =="no":
            break
        else:
            print(invalid)
            break
