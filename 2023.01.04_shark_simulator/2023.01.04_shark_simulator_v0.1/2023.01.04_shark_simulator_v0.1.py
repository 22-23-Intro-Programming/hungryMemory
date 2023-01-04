#Shark Simulator v0.1
"""
20 400 20 140 20

"""

from time import sleep
from random import randint
from graphics import *

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y

def postopoint(pos):
    return Point(pos.getX()*20+20, pos.getY()*20+20)

def pointtopos(p):
    return Position((p.getX()-20)/20, (p.getY()-20)/20)




    
def main():
    window = GraphWin("Shark Simulator", 600, 600)
    


if(__name__ == "__main__"):
    main()

