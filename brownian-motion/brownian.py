from graphics import *
from math import pi, cos, sin
from random import random

def main():
    win = createWindow()
    
    introTxt = Text(Point(0,0), "Click anywhere to start" + '\n' +
                                "(Press x to quit)".center(len("Click anywhere to start"))).draw(win)
    introTxt.setFill("white")
    introTxt.setFace("courier")
    
    clickLocation = win.getMouse()
    
    introTxt.undraw()
    traceRandomWalk(win, clickLocation)
    
def createWindow():
    window = GraphWin(title = "Brownian Motion", width = 400, height = 400)
    window.setBackground("black")
    window.setCoords(-50, -50, 50, 50)

    return window

def particleWithinBoundary(molecule, dx, dy):
    "Checks if particle is within boundary"
    xcoord = molecule.getCenter().getX() + dx
    ycoord = molecule.getCenter().getY() + dy
    
    return ((-50 < xcoord < 50) and (-50 < ycoord < 50))

def drawPath(window, prevPoint, currPoint):
    path = Line(prevPoint, currPoint)
    path.draw(window)
    path.setFill("white")
        
def traceRandomWalk(window, clickedLocation):
    molecule = Circle(clickedLocation, 2)
    molecule.setFill("red")
    molecule.setOutline("white")
    molecule.setWidth(2)
    molecule.draw(window)
    
    prevPoint = molecule.getCenter()
    currPoint = molecule.getCenter()
    
    drawPath(window, prevPoint, currPoint)
    
    while True:
        
        while True:
            angle = 2 * pi * random()
            dx = cos(angle)
            dy = sin(angle)
            if particleWithinBoundary(molecule, dx, dy): break
        
        molecule.move(dx, dy)
        
        currPoint = molecule.getCenter()
        drawPath(window, prevPoint, currPoint)
        prevPoint = currPoint
        
        pressedKey = window.checkKey()
        
        if pressedKey == 'x':
            break
        
main()
        