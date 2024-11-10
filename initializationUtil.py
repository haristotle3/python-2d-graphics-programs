from graphics import *
from diskUtil import *
from towersUtil import *

MAX_DISKS = 10

def initializeTowersOfHanoi(numDisks, hanoiWindow):
    "creates a 3 towers, source, destination and auxiliary and returns them"
    
    windowWidth = 5 * MAX_DISKS
    
    towerWidth = 1
    towerHeight = towerBase = MAX_DISKS + 2
    towerBaseGap = 2.5
    
    centerPoint = Point(windowWidth/2 - (towerBase + towerBaseGap), windowWidth/2)
    sourceTower = Tower(towerWidth, towerHeight, hanoiWindow, centerPoint)
    
    centerPoint = Point(windowWidth/2, windowWidth/2)
    auxiliaryTower = Tower(towerWidth, towerHeight, hanoiWindow, centerPoint)
    
    centerPoint = Point(windowWidth/2 + (towerBase + towerBaseGap), windowWidth/2)
    destinationTower = Tower(towerWidth, towerHeight, hanoiWindow, centerPoint)
    
    initializeSourceTower(numDisks, sourceTower)
    return sourceTower, destinationTower, auxiliaryTower

def initializeSourceTower(N, sourceTower):
    """ Creates N disks of hanoi, of varying colours and 
    and pushes them onto source Tower."""
    
    colours = ["red", "orange", "yellow"]
    for diskWidth in range(N+1, 1, -1): # width of disk starts from N+1, decreasing down to 1
        sourceTower.diskPush(Disk(diskWidth,
                                  DISK_HEIGHT,
                                  colours[diskWidth % len(colours)],
                                  sourceTower.getTopMostDiskCenter(),
                                  sourceTower.getWindow()))

def validInput(someInteger):
    return 0 < someInteger <= MAX_DISKS
        

def initializerUI():
    inputWin = GraphWin("Input number of Towers", 300, 300)
    windowWidth = windowHeight = 20
    inputWin.setCoords(0,0,windowWidth,windowHeight)
    
    inputEntry = Entry(Point(windowWidth/2, windowHeight/2), 2) 
    inputEntry.setText("3")
    inputEntry.draw(inputWin)
    
    # windowWidth/2 + x because inputEntry occupies the same place.
    navigationText = Text(Point(windowWidth/2, windowWidth/2 + 3), "Enter number of Disks")
    navigationText.setFace("courier")
    navigationText.draw(inputWin)
    
    while True:
        pressedKey = inputWin.getKey()
        if pressedKey == 'Return':
            try:
                userInput = int(inputEntry.getText())
                if validInput(userInput):
                    numDisks = userInput
                    break
                else:
                    navigationText.setText("Number of disks\n" + "should be atleast 1\n" + "and less than {0}".format(MAX_DISKS + 1))
            except ValueError:
                navigationText.setText("Please enter a number.")
        
    return numDisks
