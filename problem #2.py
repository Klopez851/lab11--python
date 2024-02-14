###########################################
# Author: Keidy Lopez
# Filename: problem #2.py
# Description: program that draws squares on a specified point
###########################################
from graphics import *
import random

def main():
# graphic window
    w,h = 500,500
    win = GraphWin('Problem 2', w,h)
# text object
    message = Text(Point((w/2),(h/2)-(h/3)),'Click anywhere to draw a square :D')
    message.draw(win)
# list with colors
    color_list = ['green', 'blue', 'dark slate blue', 'yellow', 'red', 'purple', 'brown', 'pink', 'white',
                  'khaki', 'light blue']

# sentinal variale for while loop
    run = True

# counter to keep track of how many times a person clickes a screen
    counter = 0

# while loop that allows for five squares to be drawn on the screen
    while run:
        pt = win.checkMouse()
        if pt:
            mySquare = Rectangle(Point(pt.getX()-15,pt.getY()+15), Point(pt.getX()+15,pt.getY()-15))
            mySquare.setFill(random.choice(color_list))
            win.setBackground(random.choice(color_list))
            mySquare.draw(win)
            counter +=1
        if counter == 5:
            message.setText('click again to quit!')
            win.getMouse()
            run = False



if __name__ == "__main__":
    main()