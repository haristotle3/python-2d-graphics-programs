from initializationUtil import *

MOVES_PER_SECOND = 5

def towersOfHanoi(numDisks):
    windowWidth = 5 * MAX_DISKS
    
    hanoiWindow = GraphWin("Towers of Hanoi", 600, 600)
    hanoiWindow.setCoords(0, 0, windowWidth, windowWidth)
    
    sourceTower, destinationTower, auxiliaryTower = initializeTowersOfHanoi(numDisks, hanoiWindow)
    
    uiText = Text(Point(windowWidth/2, 5*windowWidth/6), "Click anywhere to Start!")
    uiText.setFace("courier")
    uiText.setSize(18)
    uiText.draw(hanoiWindow)
    
    hanoiWindow.getMouse()
    uiText.undraw()
    
    moveTowers(numDisks, sourceTower, destinationTower, auxiliaryTower)
    
    uiText.setText("Click anywhere to exit!")
    uiText.draw(hanoiWindow)
    hanoiWindow.getMouse()
    hanoiWindow.close()
    
def moveTowers(N, source, destination, auxiliary):
    "Recursive function exactly like a non-graphical program"
    if N == 1:
        update(MOVES_PER_SECOND)
        source.moveTopDiskTo(destination)
    else:
        moveTowers(N-1, source, auxiliary, destination)
        moveTowers(1, source, destination, auxiliary)
        moveTowers(N-1, auxiliary, destination, source)

