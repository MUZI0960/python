from random import random

def getHollJak():
    rnd = random()
    if rnd > 0.5 :
        com = "홀"
    else :
        com = "짝"
    
    return com

com = getHollJak()
print("com", com)