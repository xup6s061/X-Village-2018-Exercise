import random

class HungryException(Exception):
    def __init__(self,m):
        self.msg= "I'm hungry (status:"+str(m['hunger'])+"), need to eat."
        print(self.msg)
        eat(m)
    def __str__(self):
        return False

class ThirstyException(Exception):
    def __init__(self,m):
        self.msg= "I'm thirsty (status:"+str(m['water'])+"), need to drink."
        print(self.msg)
        drink(m)
    def __str__(self):
        return False

class BoredException(Exception):
    def __init__(self,m):
        self.msg= "I'm bored (status:"+str(m['mood'])+"), need to play."
        print(self.msg)
        play(m)
    def __str__(self):
        return False

def check(man):

    if man["hunger"] <=0:
        raise HungryException(man)
    if man["water"] <=0:
        raise ThirstyException(man)
    if man["mood"] <=0:
        raise BoredException(man)
        

def play(man):
    print("playing...")
    man["hunger"] -= 15
    man["water"] -= 15
    man["mood"] += 5
    check(man)
def eat(man):
    print("eating...")
    man["hunger"] += 5
    check(man)
def drink(man):
    print("drinking...")
    man["water"] += 5
    check(man)
    
actionList = [play, eat, drink]
    
child = {"hunger": 20, "water": 20, "mood": 20}

while True:
    # cnt -= 1
    rand = random.randint(0,2)
    
    # TODO: 把隨機的動作用 try...except 包起來   
    try:
        actionList[rand](child)
    except Exception:
        break
