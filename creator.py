import random
import time

import char

masterstatsdict =char.masterstats

class Race(object):

    statsdict = masterstatsdict

    def __init__ (self, age):
        self.age = age
    def start(self):
        global masterstatsdict
        char.die4d6()
        print(masterstatsdict)
elf = Race("100-200")

def raceage():
    print(elf.age)
