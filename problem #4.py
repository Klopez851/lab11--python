###########################################
# Author: Keidy Lopez
# Filename: problem #4.py
# Description: dice game
###########################################
import random

from graphics import *
import os
import time

def main():
    # graphic window
    w,h = 500,500
    win = GraphWin('Dice game',w,h)
    win.setBackground('thistle')

    # game title
    message = Text(Point(w/2,h/10), 'Dice Game Against Computer')
    message.setSize(19)
    message.setFace('courier')
    message.setStyle('bold')
    message.draw(win)

    #sentinal variable for while loop
    run = True

    while run:
# prints die images on screen
        image_path = os.getcwd() + '/DieImages/'
        dice_imag = Image(Point(w / 2.9, h / 3), image_path + 'die_face_1_T_s.gif')
        dice_imag2 = Image(Point((w / 2) + (w / 6), h / 3), image_path + 'die_face_1_T_s.gif')

# displays choices for game
        message2 = Text(Point(w / 2, h / 1.89), '')
        message2.setText('What is your lucky guess?')
        message2.setSize(13)
        message2.setFace('courier')
        message2.setStyle('bold')

        menu_display = Text(Point(w / 2, h / 1.6), '')
        menu_display.setText('1.Over Seven\n2.Lucky Seven!\n3.Under seven  ')
        menu_display.setSize(12)
        menu_display.setFace('courier')
        menu_display.setStyle('italic')

# displays place to enter choice
        choiceText = Text(Point(w / 3, h / 1.2), '')
        choiceText.setText('Choice:')
        choiceText.setFace('courier')

        choiceEntry = Entry(Point(w / 2, h / 1.2), 10)
        choiceEntry.setFill('light gray')



# draws all objects
        dice_imag.draw(win)
        dice_imag2.draw(win)
        message2.draw(win)
        menu_display.draw(win)
        choiceText.draw(win)
        choiceEntry.draw(win)

# makes sure entry has input
        win.getKey()

# validates input
        if int(choiceEntry.getText()) > 3:
            invalid = Text(Point(w/2,h/1.1), 'Please enter a valid choice!')
            invalid.setFace('courier')
            invalid.draw(win)
            time.sleep(3)
            invalid.undraw()
            message2.undraw()
            menu_display.undraw()
            choiceText.undraw()
            choiceEntry.undraw()
            continue

# Dice roll
        message2.setText('Rolling Dice...')

        menu_display.undraw()
        dice_imag.undraw()
        dice_imag2.undraw()

        # simulates dice being rolled
        for i in range(12):
            time.sleep(.1)
            dice_imag3 = Image(Point(w/2.9,h/3),image_path+'die_face_'+str(random.randint(1,6))+'_T_s.gif')
            dice_imag4 = Image(Point((w/2)+(w/6),h/3),image_path+'die_face_'+str(random.randint(1,6))+'_T_s.gif')
            dice_imag3.draw(win)
            dice_imag4.draw(win)

        dice_imag3.undraw()
        dice_imag4.undraw()

# dice roll variables
        die1 = rollDie()
        die2 = rollDie()
        die3 = die1 + die2

# displays die images that matches dice roll
        dice_imag3 = Image(Point(w / 2.9, h / 3), image_path + 'die_face_' + str(die1) + '_T_s.gif')
        dice_imag4 = Image(Point((w / 2) + (w / 6), h / 3), image_path + 'die_face_' + str(die2) + '_T_s.gif')
        dice_imag3.draw(win)
        dice_imag4.draw(win)

# displays to user what was rolled
        message2.setText('You Rolled a '+str(die1)+' and a '+str(die2)+'!')

# winner display and allows to play again if desired
        choice = choiceEntry.getText()
        if isWinner(int(choice),die3)==True:
            menu_display.setText('You won!')
            menu_display.draw(win)

            time.sleep(3)
            choiceEntry.undraw()
            menu_display.setText('Would you like to play again?')


            choiceText.move(w/5.95,0)
            choiceText.setText('press Q to quit or any other key to continue!')

            answer = win.getKey()
            if answer.upper() == 'Q':
                message2.setText('Thank you for playing!')
                time.sleep(4)
                run = False
            else:
                dice_imag.undraw()
                dice_imag2.undraw()
                message2.undraw()
                menu_display.undraw()
                choiceText.undraw()
                choiceEntry.undraw()
                continue
        else:
            menu_display.setText('You Lost :(')
            menu_display.draw(win)

            time.sleep(3)
            choiceEntry.undraw()
            menu_display.setText('Would you like to play again?')


            choiceText.move(w/5.95,0)
            choiceText.setText('press Q to quit or any other key to continue!')

            answer = win.getKey()
            if answer.upper() == 'Q':
                message2.setText('Thank you for playing!')
                time.sleep(4)
                run = False
            else:
                dice_imag.undraw()
                dice_imag2.undraw()
                message2.undraw()
                menu_display.undraw()
                choiceText.undraw()
                choiceEntry.undraw()
                continue

        win.close()


# returns a die roll
def rollDie():
    roll = random.randint(1,6)
    return roll

# decides if the player won or not based on the roll and choice
def isWinner(choice:int, rollsum:int)->bool:
    if choice==1 and rollsum > 7:
        return True
    elif choice==2 and rollsum ==7:
        return True
    elif choice == 3 and rollsum < 7:
        return True
    elif choice==1 and rollsum <= 7:
        return False
    elif choice==2 and rollsum !=7:
        return False
    elif choice == 3 and rollsum >= 7:
        return False



if __name__ == "__main__":
    main()