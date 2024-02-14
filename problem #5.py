###########################################
# Author: Keidy Lopez
# Filename: problem #5.py
# Description: DOLLAR TO EURO
###########################################
from graphics import *
import  time
import random

def main():
# graphic window
    w,h = 340,335
    win = GraphWin('Dollar To Euro',w,h)

# list with names of files
    ads = ['cola advertisement .png','advertisement.png','pepsi advertisment.png','perfume.png','second perfume.png']

# all objects that generate the UI
    myImage = Image(Point(w/2,h/5.4),'images.png')
    myImage2 = Image(Point(w / 2, h / 2), 'download.png')
    myImage3 = Image(Point(w / 2, h /4), 'euro.png')
    myImage4 = Image(Point(w / 2, h -40),random.choice(ads)) # advertisement lol

    title = Text(Point(w/2,h/6.5),'Dollar To Euro Converter')
    title.setSize(15)
    title.setFace('courier')
    title.setStyle('bold')

    titleRectangle = Rectangle(Point(w-320,h-300),Point(w-20,h-270))
    titleRectangle.setFill('dark khaki')
    titleRectangle.setOutline('olive')

    myText = Text(Point(w/2.38,h/2.5),'Dollar amount(zero to quit):')
    myText.setSize(10)
    myText.setFace('courier')
    myText.setStyle('bold')

    myResult = Text(Point(w/2,h/1.9), '')
    myResult.setStyle('bold')
    myResult.setFace('courier')

    dollarEntry = Entry(Point(w/1.25,h/2.5),5)
    dollarEntry.setFill(color_rgb(245,245,220))

    circle = Circle(Point(w/2+w/3.4,h-80),6)
    circle.setFill('black')

    Xline1= Line(Point(circle.getCenter().getX()+3,circle.getCenter().getY()+3),Point(circle.getCenter().getX()-3,
                                                                                      circle.getCenter().getY()-3))
    Xline1.setFill('white')
    Xline1.setWidth(2)

    Xline2 = Line(Point(circle.getCenter().getX()+ 3, circle.getCenter().getY() - 3),
                  Point(circle.getCenter().getX() - 3,
                        circle.getCenter().getY() + 3))
    Xline2.setFill('white')
    Xline2.setWidth(2)

# draws all objects
    myImage3.draw(win)
    myImage.draw(win)
    myImage2.draw(win)
    myImage4.draw(win)
    titleRectangle.draw(win)
    title.draw(win)
    myText.draw(win)
    dollarEntry.draw(win)
    circle.draw(win)
    Xline1.draw(win)
    Xline2.draw(win)

# sentinal variable for while loop
    run = True

# while run that takes dollar value and return euro value
    while run:

        # nested while loop that allows for user to input value
        keypressing = True
        number = []
        while keypressing:
            kp = win.getKey()
            number.append(kp)
            if 'Return' in number:
                keypressing = False

        # validates user input and allows them to quit if wanted
        dollar = dollarEntry.getText()
        if float(dollar) == 0.00:
            myResult.setText('Thank you for using my program <3')
            myResult.setSize(10)
            myResult.setStyle('bold')
            myResult.draw(win)
            time.sleep(2)
            run = False
        else:
            myResult.setText('The Euro value of $'+str(dollar)+' is €'+str(Dollar_to_Euro(float(dollar)))+'!')
            myResult.setSize(10)
            myResult.setStyle('bold')
            myResult.draw(win)
            time.sleep(5)
            myResult.undraw()

    win.close()

# converts dollar value to euro value
def Dollar_to_Euro(d):
    Euro = d * 0.85
    Euro2=round(Euro,2)
    return Euro2


if __name__=="__main__":
    main()