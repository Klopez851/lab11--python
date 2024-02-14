###########################################
# Author: Keidy Lopez
# Filename: problem #3.py
# Description: draws a triangle with three gtiven points
###########################################
from graphics import *
import random

def main():
# graphics window
    w,h=300,300
    win = GraphWin('Problem 3',w,h)
    color_list = ['green', 'blue', 'dark slate blue', 'yellow', 'red', 'purple', 'brown', 'pink', 'white',
                  'khaki', 'light blue']

# text objects
    message = Text(Point(w/2,h-50),'')
    message.setSize(14)
    message.setText('Click on three points')

    message.draw(win)

# allows user to click three points on the window
    mp1 = win.getMouse()
    mp1.draw(win)
    win.setBackground(random.choice(color_list))
    mp2 = win.getMouse()
    mp2.draw(win)
    win.setBackground(random.choice(color_list))
    mp3 = win.getMouse()
    mp3.draw(win)
    win.setBackground(random.choice(color_list))

# draws polygon with thhe three given points
    myPolygon = Polygon(Point(mp1.getX(),mp1.getY()),Point(mp2.getX(),mp2.getY()), Point(mp3.getX(),mp3.getY()))
    myPolygon.draw(win)

# lets user know how to quit the program
    message.setText('click anywhere to quit')
    mp = win.getMouse()
    win.close()






if __name__ == "__main__":
    main()