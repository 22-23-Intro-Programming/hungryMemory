#Welcome to Character Creator, with 157464 possible combinations!

from random import randint

from graphics import *
from Button import *

colors = {
    "white": color_rgb(255, 255, 255),
    "grey": color_rgb(180, 180, 180),
    "black": color_rgb(0, 0, 0),
    "red": color_rgb(255, 0, 0),
    "yellow": color_rgb(255, 255, 0),
    "green": color_rgb(0, 255, 0),
    "cyan": color_rgb(0, 255, 255),
    "blue": color_rgb(0, 0, 255),
    "magenta": color_rgb(255, 0, 255)
}

color_list = [colors["red"], colors["yellow"], colors["green"], colors["cyan"], colors["blue"], colors["magenta"]]

attribute_texts = {
    "head": {
        "size": ["Small", "Medium", "Large"],
        "shape": ["Square", "Circle"],
        "color": ["Red", "Yellow", "Green", "Cyan", "Blue", "Magenta"]
    },
    "nose": {
        "size": ["Small", "Medium", "Large"],
        "shape": ["Square", "Circle"],
        "color": ["Red", "Yellow", "Green", "Cyan", "Blue", "Magenta"]
    },
    "eyes": {
        "size": ["Small", "Medium", "Large"],
        "shape": ["Square", "Circle"],
        "color": ["Red", "Yellow", "Green", "Cyan", "Blue", "Magenta"]
    }
}

character = {
    "head": {
        "size": 0,
        "shape": 0,
        "color": 0
    },
    "nose": {
        "size": 0,
        "shape": 0,
        "color": 0
    },
    "eyes": {
        "size": 0,
        "shape": 0,
        "color": 0
    }
}

def getsavecode():
    return str(character["head"]["size"]) + str(character["head"]["shape"]) + str(character["head"]["color"]) + str(character["nose"]["size"]) + str(character["nose"]["shape"]) + str(character["nose"]["color"]) + str(character["eyes"]["size"]) + str(character["eyes"]["shape"]) + str(character["eyes"]["color"])
def loadsavecode(code):
    character["head"]["size"] = int(code[0])
    character["head"]["shape"] = int(code[1])
    character["head"]["color"] = int(code[2])
    character["nose"]["size"] = int(code[3])
    character["nose"]["shape"] = int(code[4])
    character["nose"]["color"] = int(code[5])
    character["eyes"]["size"] = int(code[6])
    character["eyes"]["shape"] = int(code[7])
    character["eyes"]["color"] = int(code[8])

def main():
    win = GraphWin("Character Creator", 1000, 600)
    #initialize selection buttons
    head_size_button = Button(win, Point(600,50), Point(700,150), 5, attribute_texts["head"]["size"][character["head"]["size"]], colors["grey"], colors["black"], colors["black"])
    head_shape_button = Button(win, Point(725,50), Point(825,150), 5, attribute_texts["head"]["shape"][character["head"]["shape"]], colors["grey"], colors["black"], colors["black"])
    head_color_button = Button(win, Point(850,50), Point(950,150), 5, attribute_texts["head"]["color"][character["head"]["color"]], colors["grey"], colors["black"], colors["black"])
    nose_size_button = Button(win, Point(600,175), Point(700,275), 5, attribute_texts["nose"]["size"][character["nose"]["size"]], colors["grey"], colors["black"], colors["black"])
    nose_shape_button = Button(win, Point(725,175), Point(825,275), 5, attribute_texts["nose"]["shape"][character["nose"]["shape"]], colors["grey"], colors["black"], colors["black"])
    nose_color_button = Button(win, Point(850,175), Point(950,275), 5, attribute_texts["nose"]["color"][character["nose"]["color"]], colors["grey"], colors["black"], colors["black"])
    eyes_size_button = Button(win, Point(600,300), Point(700,400), 5, attribute_texts["eyes"]["size"][character["eyes"]["size"]], colors["grey"], colors["black"], colors["black"])
    eyes_shape_button = Button(win, Point(725,300), Point(825,400), 5, attribute_texts["eyes"]["shape"][character["eyes"]["shape"]], colors["grey"], colors["black"], colors["black"])
    eyes_color_button = Button(win, Point(850,300), Point(950,400), 5, attribute_texts["eyes"]["color"][character["eyes"]["color"]], colors["grey"], colors["black"], colors["black"])
    #initialize meta buttons
    save_button = Button(win, Point(600,450), Point(700,550), 5, "Save as .char", colors["grey"], colors["black"], colors["black"])
    load_button = Button(win, Point(725,450), Point(825,550), 5, "Load from .char", colors["grey"], colors["black"], colors["black"])
    quit_button = Button(win, Point(850,450), Point(950,550), 5, "Quit", colors["grey"], colors["black"], colors["black"])
    #draw constant
    color1 = [60, 60, 60]
    p  = []
    for i in range(600):
        p.append(Line(Point(0,i), Point(1000,i)))
        p[i].setFill(color_rgb(round(color1[0]), round(color1[1]), round(color1[2])))
        p[i].draw(win)
        color1[0] += 1/12
        color1[1] += 1/12
        color1[2] += 1/12
    save_button.draw()
    load_button.draw()
    quit_button.draw()
    #draw initial
    head_size_button.editText(attribute_texts["head"]["size"][character["head"]["size"]])
    head_shape_button.editText(attribute_texts["head"]["shape"][character["head"]["shape"]])
    head_color_button.editText(attribute_texts["head"]["color"][character["head"]["color"]])
    nose_size_button.editText(attribute_texts["nose"]["size"][character["nose"]["size"]])
    nose_shape_button.editText(attribute_texts["nose"]["shape"][character["nose"]["shape"]])
    nose_color_button.editText(attribute_texts["nose"]["color"][character["nose"]["color"]])
    eyes_size_button.editText(attribute_texts["eyes"]["size"][character["eyes"]["size"]])
    eyes_shape_button.editText(attribute_texts["eyes"]["shape"][character["eyes"]["shape"]])
    eyes_color_button.editText(attribute_texts["eyes"]["color"][character["eyes"]["color"]])
    head_size_button.undraw()
    head_shape_button.undraw()
    head_color_button.undraw()
    nose_size_button.undraw()
    nose_shape_button.undraw()
    nose_color_button.undraw()
    eyes_size_button.undraw()
    eyes_shape_button.undraw()
    eyes_color_button.undraw()
    head_size_button.draw()
    head_shape_button.draw()
    head_color_button.draw()
    nose_size_button.draw()
    nose_shape_button.draw()
    nose_color_button.draw()
    eyes_size_button.draw()
    eyes_shape_button.draw()
    eyes_color_button.draw()
    head = Rectangle(Point(250, 250), Point(350, 350))
    head.setFill(color_list[0])
    nose = Point(10, 10)
    eye1 = Point(10, 10)
    eye2 = Point(10, 10)
    while(True):
        #drawcharacter
        head.undraw()
        nose.undraw()
        eye1.undraw()
        eye2.undraw()
        if(character["head"]["shape"] == 0):
            if(character["head"]["size"] == 0):
                head = Rectangle(Point(150, 150), Point(450, 450))
                head.setFill(color_list[character["head"]["color"]])
            elif(character["head"]["size"] == 1):
                head = Rectangle(Point(100, 100), Point(500, 500))
                head.setFill(color_list[character["head"]["color"]])
            elif(character["head"]["size"] == 2):
                head = Rectangle(Point(50, 50), Point(550, 550))
                head.setFill(color_list[character["head"]["color"]])
        elif(character["head"]["shape"] == 1):
            if(character["head"]["size"] == 0):
                head = Oval(Point(150, 150), Point(450, 450))
                head.setFill(color_list[character["head"]["color"]])
            elif(character["head"]["size"] == 1):
                head = Oval(Point(100, 100), Point(500, 500))
                head.setFill(color_list[character["head"]["color"]])
            elif(character["head"]["size"] == 2):
                head = Oval(Point(50, 50), Point(550, 550))
                head.setFill(color_list[character["head"]["color"]])
        if(character["nose"]["shape"] == 0):
            if(character["nose"]["size"] == 0):
                nose = Rectangle(Point(275, 275), Point(325, 325))
                nose.setFill(color_list[character["nose"]["color"]])
            elif(character["nose"]["size"] == 1):
                nose = Rectangle(Point(250, 250), Point(350, 350))
                nose.setFill(color_list[character["nose"]["color"]])
            elif(character["nose"]["size"] == 2):
                nose = Rectangle(Point(225, 225), Point(375, 375))
                nose.setFill(color_list[character["nose"]["color"]])
        elif(character["nose"]["shape"] == 1):
            if(character["nose"]["size"] == 0):
                nose = Circle(Point(300, 300), 25)
                nose.setFill(color_list[character["nose"]["color"]])
            elif(character["nose"]["size"] == 1):
                nose = Circle(Point(300, 300), 50)
                nose.setFill(color_list[character["nose"]["color"]])
            elif(character["nose"]["size"] == 2):
                nose = Circle(Point(300, 300), 75)
                nose.setFill(color_list[character["nose"]["color"]])
        if(character["eyes"]["shape"] == 0):
            if(character["eyes"]["size"] == 0):
                eye1 = Rectangle(Point(190, 190), Point(210, 210))
                eye2 = Rectangle(Point(390, 190), Point(410, 210))
                eye1.setFill(color_list[character["eyes"]["color"]])
                eye2.setFill(color_list[character["eyes"]["color"]])
            elif(character["eyes"]["size"] == 1):
                eye1 = Rectangle(Point(175, 175), Point(225, 225))
                eye2 = Rectangle(Point(375, 175), Point(425, 225))
                eye1.setFill(color_list[character["eyes"]["color"]])
                eye2.setFill(color_list[character["eyes"]["color"]])
            elif(character["eyes"]["size"] == 2):
                eye1 = Rectangle(Point(160, 160), Point(240, 240))
                eye2 = Rectangle(Point(360, 160), Point(440, 240))
                eye1.setFill(color_list[character["eyes"]["color"]])
                eye2.setFill(color_list[character["eyes"]["color"]])
        elif(character["eyes"]["shape"] == 1):
            if(character["eyes"]["size"] == 0):
                eye1 = Oval(Point(190, 190), Point(210, 210))
                eye2 = Oval(Point(390, 190), Point(410, 210))
                eye1.setFill(color_list[character["eyes"]["color"]])
                eye2.setFill(color_list[character["eyes"]["color"]])
            elif(character["eyes"]["size"] == 1):
                eye1 = Oval(Point(175, 175), Point(225, 225))
                eye2 = Oval(Point(375, 175), Point(425, 225))
                eye1.setFill(color_list[character["eyes"]["color"]])
                eye2.setFill(color_list[character["eyes"]["color"]])
            elif(character["eyes"]["size"] == 2):
                eye1 = Oval(Point(160, 160), Point(240, 240))
                eye2 = Oval(Point(360, 160), Point(440, 240))
                eye1.setFill(color_list[character["eyes"]["color"]])
                eye2.setFill(color_list[character["eyes"]["color"]])
        head.setWidth(0)
        nose.setWidth(0)
        eye1.setWidth(0)
        eye2.setWidth(0)
        head.draw(win)
        nose.draw(win)
        eye1.draw(win)
        eye2.draw(win)
        #click management
        click = win.getMouse()
        if(50 < click.getY() and click.getY() < 150):
            if(600 < click.getX() and click.getX() < 700):
                if(character["head"]["size"] == 2):
                    character["head"]["size"] = 0
                else:
                    character["head"]["size"] += 1
                head_size_button.editText(attribute_texts["head"]["size"][character["head"]["size"]])
                head_size_button.undraw()
                head_size_button.draw()
            elif(725 < click.getX() and click.getX() < 825):
                if(character["head"]["shape"] == 1):
                    character["head"]["shape"] = 0
                else:
                    character["head"]["shape"] += 1
                head_shape_button.editText(attribute_texts["head"]["shape"][character["head"]["shape"]])
                head_shape_button.undraw()
                head_shape_button.draw()
            elif(850 < click.getX() and click.getX() < 950):
                if(character["head"]["color"] == 5):
                    character["head"]["color"] = 0
                else:
                    character["head"]["color"] += 1
                head_color_button.editText(attribute_texts["head"]["color"][character["head"]["color"]])
                head_color_button.undraw()
                head_color_button.draw()
        elif(175 < click.getY() and click.getY() < 275):
            if(600 < click.getX() and click.getX() < 700):
                if(character["nose"]["size"] == 2):
                    character["nose"]["size"] = 0
                else:
                    character["nose"]["size"] += 1
                nose_size_button.editText(attribute_texts["nose"]["size"][character["nose"]["size"]])
                nose_size_button.undraw()
                nose_size_button.draw()
            elif(725 < click.getX() and click.getX() < 825):
                if(character["nose"]["shape"] == 1):
                    character["nose"]["shape"] = 0
                else:
                    character["nose"]["shape"] += 1
                nose_shape_button.editText(attribute_texts["nose"]["shape"][character["nose"]["shape"]])
                nose_shape_button.undraw()
                nose_shape_button.draw()
            elif(850 < click.getX() and click.getX() < 950):
                if(character["nose"]["color"] == 5):
                    character["nose"]["color"] = 0
                else:
                    character["nose"]["color"] += 1
                nose_color_button.editText(attribute_texts["nose"]["color"][character["nose"]["color"]])
                nose_color_button.undraw()
                nose_color_button.draw()
        elif(300 < click.getY() and click.getY() < 400):
            if(600 < click.getX() and click.getX() < 700):
                if(character["eyes"]["size"] == 2):
                    character["eyes"]["size"] = 0
                else:
                    character["eyes"]["size"] += 1
                eyes_size_button.editText(attribute_texts["eyes"]["size"][character["eyes"]["size"]])
                eyes_size_button.undraw()
                eyes_size_button.draw()
            elif(725 < click.getX() and click.getX() < 825):
                if(character["eyes"]["shape"] == 1):
                    character["eyes"]["shape"] = 0
                else:
                    character["eyes"]["shape"] += 1
                eyes_shape_button.editText(attribute_texts["eyes"]["shape"][character["eyes"]["shape"]])
                eyes_shape_button.undraw()
                eyes_shape_button.draw()
            elif(850 < click.getX() and click.getX() < 950):
                if(character["eyes"]["color"] == 5):
                    character["eyes"]["color"] = 0
                else:
                    character["eyes"]["color"] += 1
                eyes_color_button.editText(attribute_texts["eyes"]["color"][character["eyes"]["color"]])
                eyes_color_button.undraw()
                eyes_color_button.draw()
        elif(450 < click.getY() and click.getY() < 550):
            if(600 < click.getX() and click.getX() < 700):#save
                code = randint(0,999999)
                file = open(f"character_download_{code}.char", "x")
                file = open(f"character_download_{code}.char", "w")
                file.write(getsavecode())
                file.close()
                print(f"File saved as character_download_{code}.char")
            elif(725 < click.getX() and click.getX() < 825):#load
                file = input("Enter file to load: ")
                if(file[-5:] != ".char"):
                    print("Unable to read file")
                else:
                    file = open(file)
                    loadsavecode(file.read())
            elif(850 < click.getX() and click.getX() < 950):
                win.close()
                exit()
                
if(__name__ == "__main__"):
    main()
