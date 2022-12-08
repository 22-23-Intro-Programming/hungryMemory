"""
hello mr considine
i met all the reqs but some additional filters dont work (soften, blur, and pen)
this will be fixed in later versions
anyway in case the ui isnt intuitive enough
here are instructions on how to test all of the things that were required for this project

setup:
click the load button (bottom left)
enter a filename to load (must be no greater than 1087x750) also must be in same dir
click execute to load it

to test lighten/darken:
select the button 1 down from the top left button
enter l or d for lighten and darken
enter a strength (0-255)
click execute to apply changes

to test greyscale:
select the button another one down from the lighten/darken button
enter g for greyscale
click execute to apply changes

to test contrast:
select the button 1 right of the lighten/darken button
enter c for contrast
enter a strength (0-255)
click execute to apply changes

to test the quit button:
its more of a save+quit button
click the bottom right button
enter a filename to save the image as (!! it will overwrite a file if you use an existing name !!) and then click execute
"""


#PIXEL EDITOR v0.14
#Thomas Sands

from graphics import *
from Button import Button

def bind(value, minimum, maximum):
    if(value > maximum):
        return maximum
    if(value < minimum):
        return minimum
    return value

def hextorgb(hex_color):
    rgb = []
    rgb.append(int(hex_color[1:3], 16))
    rgb.append(int(hex_color[3:5], 16))
    rgb.append(int(hex_color[5:], 16))
    return rgb

#colors passed in as hex without a #

def replace(img_state, color_find, color_replace, leniency):
    findc = hextorgb("#" + color_find)
    for i in range(img_state.getWidth()):
        for j in range(img_state.getHeight()):
            p = img_state.getPixel(i, j)
            if(abs(findc[0] - p[0]) <= leniency and abs(findc[1] - p[1]) <= leniency and abs(findc[2] - p[2]) <= leniency):
                img_state.setPixel(i, j, "#" + color_replace)
    return img_state

def lighten(img_state, strength):
    for i in range(img_state.getWidth()):
        for j in range(img_state.getHeight()):
            p = img_state.getPixel(i, j)
            if(p[0] + strength > 255):
                p[0] = 255
            else:
                p[0] += strength
            if(p[1] + strength > 255):
                p[1] = 255
            else:
                p[1] += strength
            if(p[2] + strength > 255):
                p[2] = 255
            else:
                p[2] += strength
            img_state.setPixel(i, j, color_rgb(p[0], p[1], p[2]))
    return img_state

def darken(img_state, strength):
    for i in range(img_state.getWidth()):
        for j in range(img_state.getHeight()):
            p = img_state.getPixel(i, j)
            if(p[0] - strength < 0):
                p[0] = 0
            else:
                p[0] -= strength
            if(p[1] - strength < 0):
                p[1] = 0
            else:
                p[1] -= strength
            if(p[2] - strength < 0):
                p[2] = 0
            else:
                p[2] -= strength
            img_state.setPixel(i, j, color_rgb(p[0], p[1], p[2]))
    return img_state

def contrast(img_state, strength):
    for i in range(img_state.getWidth()):
        for j in range(img_state.getHeight()):
            p = img_state.getPixel(i, j)
            if(p[0] + p[1] + p[2] > 382):
                if(p[0] + strength > 255):
                    p[0] = 255
                else:
                    p[0] += strength
                if(p[1] + strength > 255):
                    p[1] = 255
                else:
                    p[1] += strength
                if(p[2] + strength > 255):
                    p[2] = 255
                else:
                    p[2] += strength
            else:
                if(p[0] - strength < 0):
                    p[0] = 0
                else:
                    p[0] -= strength
                if(p[1] - strength < 0):
                    p[1] = 0
                else:
                    p[1] -= strength
                if(p[2] - strength < 0):
                    p[2] = 0
                else:
                    p[2] -= strength
            img_state.setPixel(i, j, color_rgb(p[0], p[1], p[2]))
    return img_state

def soften(img_state, strength):#make this work (ik whats wrong with it)
    for i in range(img_state.getWidth()):
        for j in range(img_state.getHeight()):
            p = img_state.getPixel(i, j)
            if(p[0] + p[1] + p[2] <= 382):
                if(p[0] + strength > 255):
                    p[0] = 255
                else:
                    p[0] += strength
                if(p[1] + strength > 255):
                    p[1] = 255
                else:
                    p[1] += strength
                if(p[2] + strength > 255):
                    p[2] = 255
                else:
                    p[2] += strength
            else:
                if(p[0] - strength < 0):
                    p[0] = 0
                else:
                    p[0] -= strength
                if(p[1] - strength < 0):
                    p[1] = 0
                else:
                    p[1] -= strength
                if(p[2] - strength < 0):
                    p[2] = 0
                else:
                    p[2] -= strength
            img_state.setPixel(i, j, color_rgb(p[0], p[1], p[2]))
    return img_state

def greyscale(img_state):
    for i in range(img_state.getWidth()):
        for j in range(img_state.getHeight()):
            p = img_state.getPixel(i, j)
            avg = round((p[0] + p[1] + p[2])/3)
            img_state.setPixel(i, j, color_rgb(avg, avg, avg))
    return img_state

def invert(img_state):
    for i in range(img_state.getWidth()):
        for j in range(img_state.getHeight()):
            p = img_state.getPixel(i, j)
            img_state.setPixel(i, j, color_rgb(255 - p[0], 255 - p[1], 255 - p[2]))
    return img_state

def blur(img_state):#unfinished
    pass

def fill(img_state, color_fill):
    for i in range(img_state.getWidth()):
        for j in range(img_state.getHeight()):
            img_state.setPixel(i, j, "#" + color_fill)
    return img_state

tool_selected = "pen"

def main():
    window = GraphWin("Pixel Editor", 1399, 799)
    #define tool buttons
    button_pen = Button(window, Point(1149, 24), Point(1249, 124), 3, "", "#9d9d9d", "#000000", "#000000")
    button_replace = Button(window, Point(1274, 24), Point(1374, 124), 3, "", "#9d9d9d", "#000000", "#000000")
    button_brightness = Button(window, Point(1149, 149), Point(1249, 249), 3, "", "#9d9d9d", "#000000", "#000000")
    button_contrast = Button(window, Point(1274, 149), Point(1374, 249), 3, "", "#9d9d9d", "#000000", "#000000")
    button_filter = Button(window, Point(1149, 274), Point(1249, 374), 3, "", "#9d9d9d", "#000000", "#000000")
    button_fill = Button(window, Point(1274, 274), Point(1374, 374), 3, "", "#9d9d9d", "#000000", "#000000")
    button_load = Button(window, Point(1149, 674), Point(1249, 774), 3, "", "#9d9d9d", "#000000", "#000000")
    button_save = Button(window, Point(1274, 674), Point(1374, 774), 3, "", "#9d9d9d", "#000000", "#000000")
    #define tool icons
    icon_pen = Image(Point(1199, 74), "icon_pen.png")
    icon_replace = Image(Point(1324, 74), "icon_replace.png")
    icon_brightness = Image(Point(1199, 199), "icon_brightness.png")
    icon_contrast = Image(Point(1324, 199), "icon_contrast.png")
    icon_filter = Image(Point(1199, 324), "icon_filter.png")
    icon_fill = Image(Point(1324, 324), "icon_fill.png")
    icon_load = Image(Point(1199, 724), "icon_load.png")
    icon_save = Image(Point(1324, 724), "icon_save.png")
    #define argument interface
    pen_field_size = Entry(Point(1261, 429), 16)
    pen_text_size = Text(Point(1261, 399), "Pen Size (1-10)")
    pen_field_color = Entry(Point(1261, 499), 16)
    pen_text_color = Text(Point(1261, 469), "Pen Color (000000-ffffff)")
    replace_field_color_find = Entry(Point(1261, 429), 16)
    replace_text_color_find = Text(Point(1261, 399), "Find Color (000000-ffffff)")
    replace_field_replace_color = Entry(Point(1261, 499), 16)
    replace_text_replace_color = Text(Point(1261, 469), "Replace Color (000000-ffffff)")
    replace_field_leniency = Entry(Point(1261, 569), 16)
    replace_text_leniency = Text(Point(1261, 539), "Leniency (0-255)")
    brightness_field_lightendarken = Entry(Point(1261, 429), 16)
    brightness_text_lightendarken = Text(Point(1261, 399), "Lighten/Darken (l/d)")
    brightness_field_strength = Entry(Point(1261, 499), 16)
    brightness_text_strength = Text(Point(1261, 469), "Strength (0-255)")
    contrast_field_contrastsoften = Entry(Point(1261, 429), 16)
    contrast_text_contrastsoften = Text(Point(1261, 399), "Contrast/Soften (c/s)")
    contrast_field_strength = Entry(Point(1261, 499), 16)
    contrast_text_strength = Text(Point(1261, 469), "Strength (0-255)")
    filter_field_filter = Entry(Point(1261, 429), 16)
    filter_text_filter = Text(Point(1261, 399), "Greyscale/Invert/Blur (g/i/b)")
    fill_field_color = Entry(Point(1261, 429), 16)
    fill_text_color = Text(Point(1261, 399), "Fill Color (000000-ffffff)")
    load_field_filename = Entry(Point(1261, 429), 16)
    load_text_filename = Text(Point(1261, 399), "Load from (filename)")
    save_field_filename = Entry(Point(1261, 429), 16)
    save_text_filename = Text(Point(1261, 399), "Save as (filename)")
    button_execute = Button(window, Point(1209, 599), Point(1314, 649), 3, "Execute", "#9d9d9d", "#000000", "#000000")
    bad_input_indicator = Text(Point(1189, 624), "!")
    bad_input_indicator.setFill("#ff0000")
    bad_input_indicator.setSize(30)
    bad_input_indicator.setStyle("bold")
    #image placeholder definition
    img = "NOT LOADED"
    #background definition
    image_field_background = Rectangle(Point(0,0),Point(1123,799))
    toolbar_background = Rectangle(Point(1124,0),Point(1399,799))
    image_field_background.setFill("#9d9d9d")
    toolbar_background.setFill("#4d4d4d")
    image_field_background.setWidth(0)
    toolbar_background.setWidth(0)
    placeholder_text = Text(Point(568, 399), "No image loaded")
    #draw background 
    image_field_background.draw(window)
    toolbar_background.draw(window)
    placeholder_text.draw(window)
    #draw tool buttons
    tool_selected = "pen"
    button_pen.setBorderWeight(8)
    button_pen.draw()
    button_replace.draw()
    button_brightness.draw()
    button_contrast.draw()
    button_filter.draw()
    button_fill.draw()
    button_load.draw()
    button_save.draw()
    #draw tool icons
    icon_pen.draw(window)
    icon_replace.draw(window)
    icon_brightness.draw(window)
    icon_contrast.draw(window)
    icon_filter.draw(window)
    icon_fill.draw(window)
    icon_load.draw(window)
    icon_save.draw(window)
    #draw argument interface
    button_execute.draw()
    pen_field_size.draw(window)
    pen_text_size.draw(window)
    pen_field_color.draw(window)
    pen_text_color.draw(window)
    while(True):
        click = window.getMouse()
        if(button_pen.isClick(click)):
            if(tool_selected == "replace"):
                button_replace.undraw()
                button_replace.setBorderWeight(3)
                button_replace.draw()
                icon_replace.undraw()
                icon_replace.draw(window)
                replace_field_color_find.undraw()
                replace_text_color_find.undraw()
                replace_field_replace_color.undraw()
                replace_text_replace_color.undraw()
                replace_field_leniency.undraw()
                replace_text_leniency.undraw()
            elif(tool_selected == "brightness"):
                button_brightness.undraw()
                button_brightness.setBorderWeight(3)
                button_brightness.draw()
                icon_brightness.undraw()
                icon_brightness.draw(window)
                brightness_field_lightendarken.undraw()
                brightness_text_lightendarken.undraw()
                brightness_field_strength.undraw()
                brightness_text_strength.undraw()
            elif(tool_selected == "contrast"):
                button_contrast.undraw()
                button_contrast.setBorderWeight(3)
                button_contrast.draw()
                icon_contrast.undraw()
                icon_contrast.draw(window)
                contrast_field_contrastsoften.undraw()
                contrast_text_contrastsoften.undraw()
                contrast_field_strength.undraw()
                contrast_text_strength.undraw()
            elif(tool_selected == "filter"):
                button_filter.undraw()
                button_filter.setBorderWeight(3)
                button_filter.draw()
                icon_filter.undraw()
                icon_filter.draw(window)
                filter_field_filter.undraw()
                filter_text_filter.undraw()
            elif(tool_selected == "fill"):
                button_fill.undraw()
                button_fill.setBorderWeight(3)
                button_fill.draw()
                icon_fill.undraw()
                icon_fill.draw(window)
                fill_field_color.undraw()
                fill_text_color.undraw()
            elif(tool_selected == "load"):
                button_load.undraw()
                button_load.setBorderWeight(3)
                button_load.draw()
                icon_load.undraw()
                icon_load.draw(window)
                load_field_filename.undraw()
                load_text_filename.undraw()
            elif(tool_selected == "save"):
                button_save.undraw()
                button_save.setBorderWeight(3)
                button_save.draw()
                icon_save.undraw()
                icon_save.draw(window)
                save_field_filename.undraw()
                save_text_filename.undraw()
            if(tool_selected != "pen"):
                tool_selected = "pen"
                button_pen.undraw()
                button_pen.setBorderWeight(8)
                button_pen.draw()
                icon_pen.undraw()
                icon_pen.draw(window)
                pen_field_size.draw(window)
                pen_text_size.draw(window)
                pen_field_color.draw(window)
                pen_text_color.draw(window)
        elif(button_replace.isClick(click)):
            if(tool_selected == "pen"):
                button_pen.undraw()
                button_pen.setBorderWeight(3)
                button_pen.draw()
                icon_pen.undraw()
                icon_pen.draw(window)
                pen_field_size.undraw()
                pen_text_size.undraw()
                pen_field_color.undraw()
                pen_text_color.undraw()
            elif(tool_selected == "brightness"):
                button_brightness.undraw()
                button_brightness.setBorderWeight(3)
                button_brightness.draw()
                icon_brightness.undraw()
                icon_brightness.draw(window)
                brightness_field_lightendarken.undraw()
                brightness_text_lightendarken.undraw()
                brightness_field_strength.undraw()
                brightness_text_strength.undraw()
            elif(tool_selected == "contrast"):
                button_contrast.undraw()
                button_contrast.setBorderWeight(3)
                button_contrast.draw()
                icon_contrast.undraw()
                icon_contrast.draw(window)
                contrast_field_contrastsoften.undraw()
                contrast_text_contrastsoften.undraw()
                contrast_field_strength.undraw()
                contrast_text_strength.undraw()
            elif(tool_selected == "filter"):
                button_filter.undraw()
                button_filter.setBorderWeight(3)
                button_filter.draw()
                icon_filter.undraw()
                icon_filter.draw(window)
                filter_field_filter.undraw()
                filter_text_filter.undraw()
            elif(tool_selected == "fill"):
                button_fill.undraw()
                button_fill.setBorderWeight(3)
                button_fill.draw()
                icon_fill.undraw()
                icon_fill.draw(window)
                fill_field_color.undraw()
                fill_text_color.undraw()
            elif(tool_selected == "load"):
                button_load.undraw()
                button_load.setBorderWeight(3)
                button_load.draw()
                icon_load.undraw()
                icon_load.draw(window)
                load_field_filename.undraw()
                load_text_filename.undraw()
            elif(tool_selected == "save"):
                button_save.undraw()
                button_save.setBorderWeight(3)
                button_save.draw()
                icon_save.undraw()
                icon_save.draw(window)
                save_field_filename.undraw()
                save_text_filename.undraw()
            if(tool_selected != "replace"):
                tool_selected = "replace"
                button_replace.undraw()
                button_replace.setBorderWeight(8)
                button_replace.draw()
                icon_replace.undraw()
                icon_replace.draw(window)
                replace_field_color_find.draw(window)
                replace_text_color_find.draw(window)
                replace_field_replace_color.draw(window)
                replace_text_replace_color.draw(window)
                replace_field_leniency.draw(window)
                replace_text_leniency.draw(window)
        elif(button_brightness.isClick(click)):
            if(tool_selected == "pen"):
                button_pen.undraw()
                button_pen.setBorderWeight(3)
                button_pen.draw()
                icon_pen.undraw()
                icon_pen.draw(window)
                pen_field_size.undraw()
                pen_text_size.undraw()
                pen_field_color.undraw()
                pen_text_color.undraw()
            elif(tool_selected == "replace"):
                button_replace.undraw()
                button_replace.setBorderWeight(3)
                button_replace.draw()
                icon_replace.undraw()
                icon_replace.draw(window)
                replace_field_color_find.undraw()
                replace_text_color_find.undraw()
                replace_field_replace_color.undraw()
                replace_text_replace_color.undraw()
                replace_field_leniency.undraw()
                replace_text_leniency.undraw()
            elif(tool_selected == "contrast"):
                button_contrast.undraw()
                button_contrast.setBorderWeight(3)
                button_contrast.draw()
                icon_contrast.undraw()
                icon_contrast.draw(window)
                contrast_field_contrastsoften.undraw()
                contrast_text_contrastsoften.undraw()
                contrast_field_strength.undraw()
                contrast_text_strength.undraw()
            elif(tool_selected == "filter"):
                button_filter.undraw()
                button_filter.setBorderWeight(3)
                button_filter.draw()
                icon_filter.undraw()
                icon_filter.draw(window)
                filter_field_filter.undraw()
                filter_text_filter.undraw()
            elif(tool_selected == "fill"):
                button_fill.undraw()
                button_fill.setBorderWeight(3)
                button_fill.draw()
                icon_fill.undraw()
                icon_fill.draw(window)
                fill_field_color.undraw()
                fill_text_color.undraw()
            elif(tool_selected == "load"):
                button_load.undraw()
                button_load.setBorderWeight(3)
                button_load.draw()
                icon_load.undraw()
                icon_load.draw(window)
                load_field_filename.undraw()
                load_text_filename.undraw()
            elif(tool_selected == "save"):
                button_save.undraw()
                button_save.setBorderWeight(3)
                button_save.draw()
                icon_save.undraw()
                icon_save.draw(window)
                save_field_filename.undraw()
                save_text_filename.undraw()
            if(tool_selected != "brightness"):
                tool_selected = "brightness"
                button_brightness.undraw()
                button_brightness.setBorderWeight(8)
                button_brightness.draw()
                icon_brightness.undraw()
                icon_brightness.draw(window)
                brightness_field_lightendarken.draw(window)
                brightness_text_lightendarken.draw(window)
                brightness_field_strength.draw(window)
                brightness_text_strength.draw(window)
        elif(button_contrast.isClick(click)):
            if(tool_selected == "pen"):
                button_pen.undraw()
                button_pen.setBorderWeight(3)
                button_pen.draw()
                icon_pen.undraw()
                icon_pen.draw(window)
                pen_field_size.undraw()
                pen_text_size.undraw()
                pen_field_color.undraw()
                pen_text_color.undraw()
            elif(tool_selected == "replace"):
                button_replace.undraw()
                button_replace.setBorderWeight(3)
                button_replace.draw()
                icon_replace.undraw()
                icon_replace.draw(window)
                replace_field_color_find.undraw()
                replace_text_color_find.undraw()
                replace_field_replace_color.undraw()
                replace_text_replace_color.undraw()
                replace_field_leniency.undraw()
                replace_text_leniency.undraw()
            elif(tool_selected == "brightness"):
                button_brightness.undraw()
                button_brightness.setBorderWeight(3)
                button_brightness.draw()
                icon_brightness.undraw()
                icon_brightness.draw(window)
                brightness_field_lightendarken.undraw()
                brightness_text_lightendarken.undraw()
                brightness_field_strength.undraw()
                brightness_text_strength.undraw()
            elif(tool_selected == "filter"):
                button_filter.undraw()
                button_filter.setBorderWeight(3)
                button_filter.draw()
                icon_filter.undraw()
                icon_filter.draw(window)
                filter_field_filter.undraw()
                filter_text_filter.undraw()
            elif(tool_selected == "fill"):
                button_fill.undraw()
                button_fill.setBorderWeight(3)
                button_fill.draw()
                icon_fill.undraw()
                icon_fill.draw(window)
                fill_field_color.undraw()
                fill_text_color.undraw()
            elif(tool_selected == "load"):
                button_load.undraw()
                button_load.setBorderWeight(3)
                button_load.draw()
                load_field_filename.undraw()
                load_text_filename.undraw()
            elif(tool_selected == "save"):
                button_save.undraw()
                button_save.setBorderWeight(3)
                button_save.draw()
                icon_save.undraw()
                icon_save.draw(window)
                save_field_filename.undraw()
                save_text_filename.undraw()
            if(tool_selected != "contrast"):
                tool_selected = "contrast"
                button_contrast.undraw()
                button_contrast.setBorderWeight(8)
                button_contrast.draw()
                icon_contrast.undraw()
                icon_contrast.draw(window)
                contrast_field_contrastsoften.draw(window)
                contrast_text_contrastsoften.draw(window)
                contrast_field_strength.draw(window)
                contrast_text_strength.draw(window)
        elif(button_filter.isClick(click)):
            if(tool_selected == "pen"):
                button_pen.undraw()
                button_pen.setBorderWeight(3)
                button_pen.draw()
                icon_pen.undraw()
                icon_pen.draw(window)
                pen_field_size.undraw()
                pen_text_size.undraw()
                pen_field_color.undraw()
                pen_text_color.undraw()
            elif(tool_selected == "replace"):
                button_replace.undraw()
                button_replace.setBorderWeight(3)
                button_replace.draw()
                icon_replace.undraw()
                icon_replace.draw(window)
                replace_field_color_find.undraw()
                replace_text_color_find.undraw()
                replace_field_replace_color.undraw()
                replace_text_replace_color.undraw()
                replace_field_leniency.undraw()
                replace_text_leniency.undraw()
            elif(tool_selected == "brightness"):
                button_brightness.undraw()
                button_brightness.setBorderWeight(3)
                button_brightness.draw()
                icon_brightness.undraw()
                icon_brightness.draw(window)
                brightness_field_lightendarken.undraw()
                brightness_text_lightendarken.undraw()
                brightness_field_strength.undraw()
                brightness_text_strength.undraw()
            elif(tool_selected == "contrast"):
                button_contrast.undraw()
                button_contrast.setBorderWeight(3)
                button_contrast.draw()
                icon_contrast.undraw()
                icon_contrast.draw(window)
                contrast_field_contrastsoften.undraw()
                contrast_text_contrastsoften.undraw()
                contrast_field_strength.undraw()
                contrast_text_strength.undraw()
            elif(tool_selected == "fill"):
                button_fill.undraw()
                button_fill.setBorderWeight(3)
                button_fill.draw()
                icon_fill.undraw()
                icon_fill.draw(window)
                fill_field_color.undraw()
                fill_text_color.undraw()
            elif(tool_selected == "load"):
                button_load.undraw()
                button_load.setBorderWeight(3)
                button_load.draw()
                icon_load.undraw()
                icon_load.draw(window)
                load_field_filename.undraw()
                load_text_filename.undraw()
            elif(tool_selected == "save"):
                button_save.undraw()
                button_save.setBorderWeight(3)
                button_save.draw()
                icon_save.undraw()
                icon_save.draw(window)
                save_field_filename.undraw()
                save_text_filename.undraw()
            if(tool_selected != "filter"):
                tool_selected = "filter"
                button_filter.undraw()
                button_filter.setBorderWeight(8)
                button_filter.draw()
                icon_filter.undraw()
                icon_filter.draw(window)
                filter_field_filter.draw(window)
                filter_text_filter.draw(window)
        elif(button_fill.isClick(click)):
            if(tool_selected == "pen"):
                button_pen.undraw()
                button_pen.setBorderWeight(3)
                button_pen.draw()
                icon_pen.undraw()
                icon_pen.draw(window)
                pen_field_size.undraw()
                pen_text_size.undraw()
                pen_field_color.undraw()
                pen_text_color.undraw()
            elif(tool_selected == "replace"):
                button_replace.undraw()
                button_replace.setBorderWeight(3)
                button_replace.draw()
                icon_replace.undraw()
                icon_replace.draw(window)
                replace_field_color_find.undraw()
                replace_text_color_find.undraw()
                replace_field_replace_color.undraw()
                replace_text_replace_color.undraw()
                replace_field_leniency.undraw()
                replace_text_leniency.undraw()
            elif(tool_selected == "brightness"):
                button_brightness.undraw()
                button_brightness.setBorderWeight(3)
                button_brightness.draw()
                icon_brightness.undraw()
                icon_brightness.draw(window)
                brightness_field_lightendarken.undraw()
                brightness_text_lightendarken.undraw()
                brightness_field_strength.undraw()
                brightness_text_strength.undraw()
            elif(tool_selected == "contrast"):
                button_contrast.undraw()
                button_contrast.setBorderWeight(3)
                button_contrast.draw()
                icon_contrast.undraw()
                icon_contrast.draw(window)
                contrast_field_contrastsoften.undraw()
                contrast_text_contrastsoften.undraw()
                contrast_field_strength.undraw()
                contrast_text_strength.undraw()
            elif(tool_selected == "filter"):
                button_filter.undraw()
                button_filter.setBorderWeight(3)
                button_filter.draw()
                icon_filter.undraw()
                icon_filter.draw(window)
                filter_field_filter.undraw()
                filter_text_filter.undraw()
            elif(tool_selected == "load"):
                button_load.undraw()
                button_load.setBorderWeight(3)
                button_load.draw()
                icon_load.undraw()
                icon_load.draw(window)
                load_field_filename.undraw()
                load_text_filename.undraw()
            elif(tool_selected == "save"):
                button_save.undraw()
                button_save.setBorderWeight(3)
                button_save.draw()
                icon_save.undraw()
                icon_save.draw(window)
                save_field_filename.undraw()
                save_text_filename.undraw()
            if(tool_selected != "fill"):
                tool_selected = "fill"
                button_fill.undraw()
                button_fill.setBorderWeight(8)
                button_fill.draw()
                icon_fill.undraw()
                icon_fill.draw(window)
                fill_field_color.draw(window)
                fill_text_color.draw(window)
        elif(button_load.isClick(click)):
            if(tool_selected == "pen"):
                button_pen.undraw()
                button_pen.setBorderWeight(3)
                button_pen.draw()
                icon_pen.undraw()
                icon_pen.draw(window)
                pen_field_size.undraw()
                pen_text_size.undraw()
                pen_field_color.undraw()
                pen_text_color.undraw()
            elif(tool_selected == "replace"):
                button_replace.undraw()
                button_replace.setBorderWeight(3)
                button_replace.draw()
                icon_replace.undraw()
                icon_replace.draw(window)
                replace_field_color_find.undraw()
                replace_text_color_find.undraw()
                replace_field_replace_color.undraw()
                replace_text_replace_color.undraw()
                replace_field_leniency.undraw()
                replace_text_leniency.undraw()
            elif(tool_selected == "brightness"):
                button_brightness.undraw()
                button_brightness.setBorderWeight(3)
                button_brightness.draw()
                icon_brightness.undraw()
                icon_brightness.draw(window)
                brightness_field_lightendarken.undraw()
                brightness_text_lightendarken.undraw()
                brightness_field_strength.undraw()
                brightness_text_strength.undraw()
            elif(tool_selected == "contrast"):
                button_contrast.undraw()
                button_contrast.setBorderWeight(3)
                button_contrast.draw()
                icon_contrast.undraw()
                icon_contrast.draw(window)
                contrast_field_contrastsoften.undraw()
                contrast_text_contrastsoften.undraw()
                contrast_field_strength.undraw()
                contrast_text_strength.undraw()
            elif(tool_selected == "filter"):
                button_filter.undraw()
                button_filter.setBorderWeight(3)
                button_filter.draw()
                icon_filter.undraw()
                icon_filter.draw(window)
                filter_field_filter.undraw()
                filter_text_filter.undraw()
            elif(tool_selected == "fill"):
                button_fill.undraw()
                button_fill.setBorderWeight(3)
                button_fill.draw()
                icon_fill.undraw()
                icon_fill.draw(window)
                fill_field_color.undraw()
                fill_text_color.undraw()
            elif(tool_selected == "save"):
                button_save.undraw()
                button_save.setBorderWeight(3)
                button_save.draw()
                icon_save.undraw()
                icon_save.draw(window)
                save_field_filename.undraw()
                save_text_filename.undraw()
            if(tool_selected != "load"):
                tool_selected = "load"
                button_load.undraw()
                button_load.setBorderWeight(8)
                button_load.draw()
                icon_load.undraw()
                icon_load.draw(window)
                load_field_filename.draw(window)
                load_text_filename.draw(window)
        elif(button_save.isClick(click)):
            if(tool_selected == "pen"):
                button_pen.undraw()
                button_pen.setBorderWeight(3)
                button_pen.draw()
                icon_pen.undraw()
                icon_pen.draw(window)
                pen_field_size.undraw()
                pen_text_size.undraw()
                pen_field_color.undraw()
                pen_text_color.undraw()
            elif(tool_selected == "replace"):
                button_replace.undraw()
                button_replace.setBorderWeight(3)
                button_replace.draw()
                icon_replace.undraw()
                icon_replace.draw(window)
                replace_field_color_find.undraw()
                replace_text_color_find.undraw()
                replace_field_replace_color.undraw()
                replace_text_replace_color.undraw()
                replace_field_leniency.undraw()
                replace_text_leniency.undraw()
            elif(tool_selected == "brightness"):
                button_brightness.undraw()
                button_brightness.setBorderWeight(3)
                button_brightness.draw()
                icon_brightness.undraw()
                icon_brightness.draw(window)
                brightness_field_lightendarken.undraw()
                brightness_text_lightendarken.undraw()
                brightness_field_strength.undraw()
                brightness_text_strength.undraw()
            elif(tool_selected == "contrast"):
                button_contrast.undraw()
                button_contrast.setBorderWeight(3)
                button_contrast.draw()
                icon_contrast.undraw()
                icon_contrast.draw(window)
                contrast_field_contrastsoften.undraw()
                contrast_text_contrastsoften.undraw()
                contrast_field_strength.undraw()
                contrast_text_strength.undraw()
            elif(tool_selected == "filter"):
                button_filter.undraw()
                button_filter.setBorderWeight(3)
                button_filter.draw()
                icon_filter.undraw()
                icon_filter.draw(window)
                filter_field_filter.undraw()
                filter_text_filter.undraw()
            elif(tool_selected == "fill"):
                button_fill.undraw()
                button_fill.setBorderWeight(3)
                button_fill.draw()
                icon_fill.undraw()
                icon_fill.draw(window)
                fill_field_color.undraw()
                fill_text_color.undraw()
            elif(tool_selected == "load"):
                button_load.undraw()
                button_load.setBorderWeight(3)
                button_load.draw()
                icon_load.undraw()
                icon_load.draw(window)
                load_field_filename.undraw()
                load_text_filename.undraw()
            if(tool_selected != "save"):
                tool_selected = "save"
                button_save.undraw()
                button_save.setBorderWeight(8)
                button_save.draw()
                icon_save.undraw()
                icon_save.draw(window)
                save_field_filename.draw(window)
                save_text_filename.draw(window)
        elif(button_execute.isClick(click)):
            bad_input_indicator.undraw()
            if(tool_selected == "pen"):#incomplete
                pass
            elif(tool_selected == "replace"):
                try:
                    assert(255 >= int(replace_field_leniency.getText()) >= 0)
                    img = replace(img, replace_field_color_find.getText(), replace_field_replace_color.getText(), int(replace_field_leniency.getText()))
                    img.undraw()
                    img.draw(window)
                except:
                    bad_input_indicator.draw(window)
            elif(tool_selected == "brightness"):
                try:
                    assert(brightness_field_lightendarken.getText() in ["l", "d"])
                    assert(255 >= int(brightness_field_strength.getText()) >= 0)
                    selection = brightness_field_lightendarken.getText()
                    if(selection == "l"):
                        img = lighten(img, int(brightness_field_strength.getText()))
                        img.undraw()
                        img.draw(window)
                    elif(selection == "d"):
                        img = darken(img, int(brightness_field_strength.getText()))
                        img.undraw()
                        img.draw(window)
                except:
                    bad_input_indicator.draw(window)
            elif(tool_selected == "contrast"):#soften doesnt work so fix that
                try:
                    assert(contrast_field_contrastsoften.getText() in ["c", "s"])
                    assert(255 >= int(contrast_field_strength.getText()) >= 0)
                    selection = contrast_field_contrastsoften.getText()
                    if(selection == "c"):
                        img = contrast(img, int(contrast_field_strength.getText()))
                        img.undraw()
                        img.draw(window)
                    elif(selection == "s"):
                        img = soften(img, int(contrast_field_strength.getText()))
                        img.undraw()
                        img.draw(window)
                except:
                    bad_input_indicator.draw(window)
            elif(tool_selected == "filter"):#blur is incomplete so do that
                try:
                    selection = filter_field_filter.getText()
                    if(selection == "g"):
                        img = greyscale(img)
                        img.undraw()
                        img.draw(window)
                    elif(selection == "i"):
                        img = invert(img)
                        img.undraw()
                        img.draw(window)
                    elif(selection == "b"):
                        img = blur(img)
                        img.undraw()
                        img.draw(window)
                    else:
                        assert(False)
                except:
                    bad_input_indicator.draw(window)
            elif(tool_selected == "fill"):
                try:
                    assert(len(fill_field_color.getText()) == 6)
                    img = fill(img, fill_field_color.getText())
                    img.undraw()
                    img.draw(window)
                except:
                    bad_input_indicator.draw(window)
            elif(tool_selected == "load"):
                try:
                    img = Image(Point(568, 399), load_field_filename.getText())
                    assert(img.getWidth() <= 1087)
                    assert(img.getHeight() <= 750)
                    img.undraw()
                    img.draw(window)
                    placeholder_text.undraw()
                except:
                    bad_input_indicator.draw(window)
            elif(tool_selected == "save"):#save is actually save and quit
                try:
                    img.save(save_field_filename.getText())
                    window.close()
                    quit()
                except:
                    bad_input_indicator.draw(window)
                    
if(__name__ == "__main__"):
    main()






















    
