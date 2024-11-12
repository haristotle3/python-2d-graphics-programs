from graphics import *

class Disk:
    "A class for the disks which will on the towers."
    
    def __init__(self, width, height, colour, center, window):
        self.rectWidth = width
        self.rectHeight = height
        self.window = window
        self.center = center.clone()
        
        x1, y1 = self.center.getX() - width/2, self.center.getY() - height/2
        x2, y2 = self.center.getX() + width/2, self.center.getY() + height/2
        
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        
        self.figure = Rectangle(p1, p2)
        self.figure.setWidth(2)
        self.figure.setFill(colour)
        self.figure.draw(self.window)
        
    def getHeight(self):
        return self.rectHeight
    
    def moveTo(self, givenTower):
        "This method moves the disk from one tower to another."
        
        dx = givenTower.getTopMostDiskCenter().getX() - self.center.getX()
        dy = givenTower.getTopMostDiskCenter().getY() - self.center.getY()
        
        self.figure.move(dx, dy)
        self.center.move(dx, dy)