#Button thging
from graphics import *

class Button:
    def __init__(self, window, point1, point2, border_weight, text, fill_color, border_color, text_color):
        self.window = window
        self.body = Rectangle(point1, point2)
        self.border_weight = border_weight
        self.text = Text(self.body.getCenter(), text)
        self.fill_color = fill_color
        self.border_color = border_color
        self.text_color = text_color
    def draw(self):
        self.body.draw(self.window)
        self.body.setWidth(self.border_weight)
        self.body.setFill(self.fill_color)
        self.body.setOutline(self.border_color)
        self.text.setTextColor(self.text_color)
        self.text.draw(self.window)
    def undraw(self):
        self.body.undraw()
        self.text.undraw()
    def move(self, dx, dy):
        self.body.move(dx, dy)
        self.text.move(dx, dy)
    def setText(self, text):
        self.text = Text(self.body.getCenter(), text)
    def setBorderWeight(self, border_weight):
        self.border_weight = border_weight
    def setFillColor(self, fill_color):
        self.fill_color = fill_color
    def setBorderColor(self, border_color):
        self.border_color = border_color
    def setTextColor(self, text_color):
        self.text_color = text_color
    def isClick(self, point):
        point1 = self.body.getP1()
        point2 = self.body.getP2()
        #return(point.getX() > point1.getX() and point.getX() < point2.getX() and point.getY() > point1.getY() and point.getY() < point2.getY()
        return point.getX() > point1.getX() and point.getX() < point2.getX() and point.getY() > point1.getY() and point.getY() < point2.getY()
        #return point.getX() > (self.body.getP1()).getX() and point.getX() < (self.body.getP2()).getX() and point.getY() > (self.body.getP1()).getY() and point.getY() < (self.body.getP2).getY()
        #change this to account for border
        
