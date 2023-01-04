#Shark Simulator v0.1
"""
20 400 20 140 20

"""

from time import sleep
from random import randint
from graphics import *
from Button import *

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y

def postopoint(pos):
    return Point((pos.getX()-1)*20+20, (pos.getY()-1)*20+20)

def pointtopos(p):
    return Position((p.getX()-20)/20+1, (p.getY()-20)/20+1)




    
def main():
    window = GraphWin("Shark Simulator", 600, 600)
    for i in range(1, 21):
        l = Line(postopoint(Position(i, 1)), postopoint(Position(i, 20)))
        l.setWidth(2)
        l.draw(window)
    for i in range(1, 21):
        l = Line(postopoint(Position(1, i)), postopoint(Position(20, i)))
        l.setWidth(2)
        l.draw(window)
    


    B = Button(window, Point(440, 00), Point(580, 50), 2, "Reset", "red", "grey", "black")
    B2 = Button(window, Point(440, 100), Point(580, 150), 2, "One Turn", "cyan", "black", "blue")
    B3 = Button(window, Point(440, 200), Point(580, 250), 2, "Fast Foward", "cyan", "black", "blue")
    Q = Button(window, Point(440, 300), Point(580, 350), 2, "Quit", "tomato", "black", "blue")

    B.draw()
    B2.draw()
    B3.draw()
    Q.draw()




    while True:
    
        m = win.getMouse()

        '''if B.isClick(m):

        if B2.isClick(m):

        if B3.isClick(m):'''

        if Q.isClick(m):

            break


    win.close()


        
   


if(__name__ == "__main__"):
    main()

