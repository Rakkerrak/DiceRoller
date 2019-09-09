import random

import creator
import dndclass
import backgrounds
import texts

skills = []
allfreeskill = 0

invalid = "\n\nInvalid input. Try again?\n"


def skillagg():
    global skills
    skills.extend(creator.masterracial_skills)
    global allfreeskill
    freeskillhere = creator.masterfreeskill + dndclass.masterfreeskill2 + backgrounds.masterfreeskill3
    allfreeskill += freeskillhere
    print("Now you will add your skills")
    print("From your race, you have gained the following:\n")
    print(", " .join(skills))
    print("From your class, you are allowed to pick %d skills from\n%s\n" % (dndclass.masterchoiceCL, ", " .join(dndclass.masterclassskill)))
    print("From your background, you have gained \n%s \nas skills\n" % (", " .join(backgrounds.masterskillBG)))
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
                new_skill = str(input("You have %d skills to choose from %s.Please type one below\n" % (choicenum, ", " .join(classskills))))
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
        # while choicenum > 0:
        #     new_skill = str(input("You have %d skills to choose from %s.Please type one below" % (choicenum, classskills)))
        #     tempskills.append(new_skill)
        #     choicenum -= 1
        # print(tempskills)
        # conf = input("Is this good? (y/n)")
        # if conf == "y" of conf == "yes":
        #     global skills
        #     skills.append(tempskills)
        #
    def freeskills():
        global allfreeskill
        if allfreeskill > 0:
            print("Your current skills are:\n")
            global skills
            print(", " .join(skills))
            tempfree = 0
            tempfree += freeskillhere
            tempskill = []
            while tempfree > 0:
                newskill = str(input("You have %d skills to select from any skill. Please type one below\n" % (tempfree)))
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

def agg():
    skillagg()
