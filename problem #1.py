###########################################
# Author: Keidy Lopez
# Filename: problem #1.py
# Description: shows scales picture of Saint A's
###########################################
from graphics import *

def main():
# graphics window
    w,h=200,200
    win = GraphWin('Picture of Saint A\'s', w,h)
# image object
    myimage = Image(Point(w/2,h/2),'saint a\'s.png')
    myimage.draw(win)
# pauses screen to see image
    mp = win.getMouse()

if __name__ == "__main__":
    main()