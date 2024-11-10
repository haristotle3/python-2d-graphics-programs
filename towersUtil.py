from graphics import *

DISK_HEIGHT = 1

class Tower:
    "A class for the towers of hanoi."
    
    def __init__(self, width, height, window, baseCenter):
        self.width = width
        self.height = height
        self.window = window
        self.baseCenter = baseCenter
        self.diskStack = []
        
        x0, y0 = self.baseCenter.getX(), self.baseCenter.getY() + DISK_HEIGHT/2
        self.topMostDiskCenter = Point(x0, y0)
        
        x1, y1 = self.baseCenter.getX() - width/2, self.baseCenter.getY()
        x2, y2 = self.baseCenter.getX() + width/2, self.baseCenter.getY() + height
        
        self.pole = Rectangle(Point(x1, y1), Point(x2, y2))
        self.pole.setWidth(2)
        self.pole.draw(self.window)
        
        baseHeight = self.width
        baseWidth = self.height
        
        x3, y3 = self.baseCenter.getX() - baseWidth/2, self.baseCenter.getY() - baseHeight
        x4, y4 = self.baseCenter.getX() + baseWidth/2, self.baseCenter.getY()
        
        self.base = Rectangle(Point(x3, y3), Point(x4, y4))
        self.pole.setWidth(2)
        self.base.setFill("black")
        self.base.draw(self.window)
        
    def getDiskStack(self):
        return self.diskStack[:]
    
    def getTopMostDisk(self):
        return self.diskStack[-1]
    
    def getTopMostDiskCenter(self):
        return self.topMostDiskCenter
    
    def diskPush(self, newDisk):
        "Pushes the new disk on to this tower"
        
        self.diskStack.append(newDisk)
        self.diskStack[-1].moveTo(self)
        self.topMostDiskCenter.move(0, DISK_HEIGHT)
        
    def getWindow(self):
        return self.window
        
    def diskPop(self):
        "Pops the topmost disk from this tower"
        
        self.topMostDiskCenter.move(0, -DISK_HEIGHT)
        return self.diskStack.pop()
    
    def moveTopDiskTo(self, givenTower):
        "Moves the topmost disk of this tower, to the given tower."
        givenTower.diskPush(self.diskPop())
