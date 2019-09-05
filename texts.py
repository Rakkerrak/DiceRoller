
import creator

invalid = "\n\nInvalid input. Try again?\n"

HE = ("Half-elves have two points they may add to any skill.(One point per skill)")
DW = ("Dwarves get stats based on their subrace")
ELF = ("Elves get stats based on their subrace")
HL = ("Halflings get stats based on their subrace")
HU = (" ")
DB = ("Dragonborn have no subraces.")
GN = ("Gnomes get stats based on their subrace")
HO = ("Half-Orcs do not have subraces!")
TF = ("Tieflings have no subraces.")

def raceOpt():
    opt = input("There are several races for you to choose from: \nHalf elf(he)\nDwarf(dw)\nElf(elf)\nHalfling(hl)\nHuman(hu)\nDragonborn(db)\nGnome(gn)\nHalf-Orc(ho)\nTiefling(tf)")
    raceOptDict = {
    "he" : creator.halfelf.start, "HE" : creator.halfelf.start, "halfelf" : creator.halfelf.start,
    "dw" : creator.dwarf.start, "DW" : creator.dwarf.start, "dwarf" : creator.dwarf.start,
    "elf" : creator.elf.start,
    "hl" : creator.halfling.start, "HL" : creator.halfling.start, "halfling" : creator.halfling.start,
    "hu" : creator.human.start, "HU" : creator.human.start, "human" : creator.human.start,
    "db" : creator.dragonborn.start, "DB" : creator.dragonborn.start, "dragonborn" : creator.dragonborn.start,
    "gn" : creator.gnome.start, "GN" : creator.gnome.start, "gnome" : creator.gnome.start,
    "tf" : creator.tiefling.start, "TF" : creator.tiefling.start, "tiefling" : creator.tiefling.start
    }
    if opt in raceOptDict:
        raceOptDict[opt]()
    else:
        print(invalid)
        raceOpt()
