from random import randrange
from graphics import GraphWin, Point
from button import Button
from dieView import DieView

def main():
    win = GraphWin("Dice Roller", 400, 400)
    win.setCoords(0,0,10,10)
    win.setBackground("green2")
    
    die1 = DieView(win, Point(3,7), 2)
    die2 = DieView(win, Point(7,7), 2)
    
    rollButton = Button(win, Point(5, 4.5), 6, 1, "Roll Dice")
    rollButton.activate()
    
    quitButton = Button(win, Point(5,1), 2, 1, "Quit")
    
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            die1.setValue(randrange(1,7))
            die2.setValue(randrange(1,7))
            quitButton.activate()
        pt = win.getMouse()
    
    win.close()


main()