import random

def play(man):
    print("playing...")
    man["hunger"] -= 15
    man["water"] -= 15
    man["mood"] += 5
    # check(man)
def eat(man):
    print("eating...")
    man["hunger"] += 5
    # check(man)
def drink(man):
    print("drinking...")
    man["water"] += 5
    # check(man)
child = {"hunger": 20, "water": 20, "mood": 20}
actionList = [play, eat, drink]
rand = random.randint(0,2)
actionList[rand](child)