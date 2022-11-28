from graphics import *
from Button import *

def is_palindrome(text):
    return text == text[::-1]

def main():
    win = GraphWin("Palindrome Checker", 800, 600)
    win.setBackground("beige")

    quit_button = Button(win, Point(10, 10), Point(30, 30), 2, "X", color_rgb(240, 80, 80), color_rgb(0,0,0), color_rgb(0,0,0))
    check_button = Button(win, Point(350, 230), Point(450, 270), 2, "Check Palindrome", color_rgb(80, 80, 240), color_rgb(0,0,0), color_rgb(0,0,0))
    entry_box = Entry(Point(400, 200), 40)
    quit_button.draw()
    entry_box.draw(win)
    check_button.draw()
    output_text = Text(Point(400, 350), "")
    while(True):
        click = win.getMouse()
        if(quit_button.isClick(click)):
            win.close()
            quit()
        elif(check_button.isClick(click)):
            output_text.undraw()
            if(entry_box.getText() == ""):
                output_text.setText("Nice try! No empty strings!")
            elif(is_palindrome(entry_box.getText())):
                output_text.setText(f"{entry_box.getText()} is a palindrome!")
            else:
                output_text.setText(f"{entry_box.getText()} is not a palindrome!")
            output_text.setSize(25)
            output_text.draw(win)
            
if(__name__ == "__main__"):
    main()

