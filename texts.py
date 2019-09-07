
import creator
import dndclass
import backgrounds

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

#ALL SKILLS
allskills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]



def raceOpt():
    opt = input("There are several races for you to choose from: \nHalf elf(he)\nDwarf(dw)\nElf(elf)\nHalfling(hl)\nHuman(hu)\nDragonborn(db)\nGnome(gn)\nHalf-Orc(ho)\nTiefling(tf)\n")
    raceOptDict = {
    "he" : creator.halfelf.start, "HE" : creator.halfelf.start, "halfelf" : creator.halfelf.start,
    "dw" : creator.dwarf.start, "DW" : creator.dwarf.start, "dwarf" : creator.dwarf.start,
    "elf" : creator.elf.start,
    "hl" : creator.halfling.start, "HL" : creator.halfling.start, "halfling" : creator.halfling.start,
    "hu" : creator.human.start, "HU" : creator.human.start, "human" : creator.human.start,
    "db" : creator.dragonborn.start, "DB" : creator.dragonborn.start, "dragonborn" : creator.dragonborn.start,
    "gn" : creator.gnome.start, "GN" : creator.gnome.start, "gnome" : creator.gnome.start,
    "ho" : creator.halforc.start, "HO" : creator.halforc.start, "halforc" : creator.halforc.start,
    "tf" : creator.tiefling.start, "TF" : creator.tiefling.start, "tiefling" : creator.tiefling.start
    }
    if opt in raceOptDict:
        raceOptDict[opt]()
    else:
        print(invalid)
        raceOpt()

def classOpt():
    print("This program has 12 classes for D&D5e!")
    print(
" Barbarian(barbar)  Bard(bard)       Cleric(cler)    Druid(druid)\n",
"Fighter(fit)       Monk(monk)       Paladin(pal)    Ranger(rang)\n",
"Rogue(rog)         Sorcerer(sorc)   Warlock(war)    Wizard(wiz)")
    opt = input("Please choose from above\n")
    lopt = opt.lower()
    classOptDict = {
    "barbar" : dndclass.barbarian.start, "barbarian" : dndclass.barbarian.start,
    "bard" : dndclass.bard.start,
    "cleric" : dndclass.cleric.start, "cler" : dndclass.cleric.start,
    "druid" : dndclass.druid.start,
    "fit" : dndclass.fighter.start, "fight" : dndclass.fighter.start, "fighter" : dndclass.fighter.start,
    "rog" : dndclass.rogue.start, "rogue" : dndclass.rogue.start,
    "monk" : dndclass.monk.start, "mon" : dndclass.monk.start,
    "paladin" : dndclass.paladin.start, "pal" : dndclass.paladin.start,
    "ranger" : dndclass.ranger.start, "rang" : dndclass.ranger.start,
    "sorc" : dndclass.sorcerer.start, "sorcerer" : dndclass.sorcerer.start,
    "war": dndclass.warlock.start, "warlock" : dndclass.warlock.start,
    "wiz" : dndclass.wizard.start, "wizard" : dndclass.wizard.start
    }
    if lopt in classOptDict:
        classOptDict[lopt]()
    else:
        print(invalid)
        classOpt()

def bgOpt():
    print("There are currently 14 background options from the PHB and a custom option for your background.\n Please carefully choose one of the folowing:\n")
    print(
    " Acolyte(aco)                Charlatan(char)    Criminal(crim)\n",
    "Entertainer(ent)            Folk Hero (fh)     Guild Artisan(ga)\n",
    "G. Artisan:Merchant(merch)  Hermit(herm)       Noble(nob)\n",
    "Noble: Knight(nit)          Outlander(out)     Sage(sage)\n",
    "Sailor(sail)                Sailor:Pirate(pir) Soldier(sold)\n",
    "Urchin(urch)                Custom(custom)"
    )
    bgoptu = input("Please choose:\n")
    bgopt = bgoptu.lower()
    bgOptDict = {
    "aco" : backgrounds.acolyte.start, "acolyte" : backgrounds.acolyte.start,
    "char" : backgrounds.charlatan.start, "charlatan" : backgrounds.charlatan.start,
    "crim" : backgrounds.criminal.start, "criminal" : backgrounds.criminal.start,
    "ent" : backgrounds.entertainer.start, "entertainer" : backgrounds.entertainer.start,
    "fh" : backgrounds.folkhero.start, "folkhero" : backgrounds.folkhero.start, "folk hero" : backgrounds.folkhero.start,
    "ga" : backgrounds.gArtisan.start, "guildartisan" : backgrounds.gArtisan.start, "guild artisan" : backgrounds.gArtisan.start,
    "merch" : backgrounds.merchant.start, "merchant" : backgrounds.merchant.start,
    "herm" : backgrounds.hermit.start, "hermit" : backgrounds.hermit.start,
    "nob" : backgrounds.noble.start, "noble" : backgrounds.noble.start,
    "nit" : backgrounds.nobleknight.start, "knight" : backgrounds.nobleknight.start, "nite" : backgrounds.nobleknight.start,
    "out" : backgrounds.outlander.start, "outlander" : backgrounds.outlander.start,
    "sage" : backgrounds.sage.start, "sag" : backgrounds.sage.start,
    "sail" : backgrounds.sailor.start, "sailor" : backgrounds.sailor.start,
    "pir" : backgrounds.pirate.start, "pirate" : backgrounds.pirate.start,
    "sold" : backgrounds.soldier.start, "soldier" : backgrounds.soldier.start,
    "urch" : backgrounds.urchin.start, "urchin" : backgrounds.urchin.start,
    "custom" : backgrounds.custom.start, "cust" : backgrounds.custom.start
    }
    if bgopt in bgOptDict:
        bgOptDict[bgopt]()
    else:
        print(invalid)
        bgOpt()
