import agg
import creator

def start():
    file = open("Charsheet.txt", "a+")

    file.write("\nClass & Level : {} lvl 1      Background: {}".format(agg.miscdict["CLASS"], agg.miscdict["BACKGROUND"]))
    file.write("\nRace: {}      Alignment: {}".format(agg.miscdict["RACE"], agg.miscdict["Alignment"]))
    file.write("\nAge: {}       Height: {}      Weight: {}\nEyes: {}        Skin: {}        Hair: {}".format(agg.miscdict["AGE"], agg.miscdict["HEIGHT"], agg.miscdict["WEIGHT"], agg.miscdict["EYES"], agg.miscdict["SKIN"], agg.miscdict["HAIR"]))
    file.write("\n\n    Your stats")
    for x in creator.masterstatsdict:
        file.write("\n{} : {}".format(x, creator.masterstatsdict[x]))
    file.write("\n\n    Your modifiers")
    for x in creator.mastermodsdict:
        file.write("\n{} : {}".format(x, creator.mastermodsdict[x]))
    file.write("\n\nSave Proficiencies:")
    for x in agg.saves:
        file.write(" \n{}".format(x))
    file.write("\n\nSkill Proficiencies:")
    for x in agg.skills:
        file.write("\n{}".format(x))
    file.write("\n\nSpeed: {}       HP: {}       Hit die: d{}".format(agg.miscdict["SPEED"], agg.miscdict["HP"], agg.miscdict["HitDie"]))
    file.write("\n\nThese are your Tool Proficiencies:")
    for x in agg.tools:
        file.write("\n{}".format(x))
    file.write("\n\nThese are your Weapon Proficiencies:")
    for x in agg.weapons:
        file.write("\n{}".format(x))
    file.write("\n\nThese are your Armor Proficiencies:")
    for x in agg.armor:
        file.write("\n{}".format(x))
    file.write("\n\nThese are your character's feats, including page numbers you can find them on.  Some things have already been added into your character's stats such as proficiencies and stat bonuses.")
    for x in agg.feats:
        file.write("\n{}".format(x))
    file.write("\nLanguages: {}".format(agg.miscdict["Languages"]))
    if "Secret Language" in agg.miscdict:
        file.write("\nSecret Language: {}".format(agg.miscdict["Secret Language"]))
    else:
        pass
    if "Extra Languages" in agg.miscdict:
        file.write("\nExtra Languages: {}".format(agg.miscdict["Extra Languages"]))
    else:
        pass
    file.write("\nEquipment:\n")
    for x in agg.equip:
        file.write("{}, ".format(x))
    file.write("\n\n\nUseful page numbers: \nArmor(to calculate Initiative): pg. 143      Weapons: pg 149         \nEquipment 'Packs'(and the general area for all other equipment): pg. 151 \nLanguages: pg123     Optional Starting Gold(Remove all equipment and gold and self-buy): pg. 143 \nNon-Background Features(Choose one if you're a variant Human!): pg.165")
    os.system('libreoffice Charsheet.txt')
