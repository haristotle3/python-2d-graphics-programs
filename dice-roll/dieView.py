from graphics import *

class DieView:
    """ DieView is a widget that displays a graphical representation of a 
    standard six-sided die."""
    
    def __init__(self, win, center, size):
        """ Create a view of a die, e.g.:
            d1 = DieView(myWindow, Point(40,50), 20)
        creates a die centered at (40,50) having side lengths 
        of 20 """
        
        self.win = win              
        self.background = "white"   # colour of die face
        self.foreground = "black"   # colour of the die pips
        self.psize = 0.1*size       # radius of each pip
        hsize = size/2              # half the length of die (needed later)
        offset = 0.6*hsize          # distance from the center to the outer pips
        
        # create a square for the face
        cx, cy = center.getX(), center.getY()
        pointLL = Point(cx-hsize, cy-hsize)
        pointUR = Point(cx+hsize, cy+hsize)
        rect = Rectangle(pointLL, pointUR)
        rect.draw(win)
        rect.setFill(self.background)
        
        # create 7 circles for standard pip locations
        self.pips = [self.__makePip(cx-offset, cy-offset),
                    self.__makePip(cx-offset, cy),
                    self.__makePip(cx-offset, cy+offset),
                    self.__makePip(cx, cy),
                    self.__makePip(cx+offset, cy-offset),
                    self.__makePip(cx+offset, cy),
                    self.__makePip(cx+offset, cy+offset)]
        
        self.pipIndices = {1:[3],
                           2:[0,6],
                           3:[0,3,6],
                           4:[0,2,4,6],
                           5:[0,2,3,4,6],
                           6:[0,1,2,4,5,6]}
        
        # Draw some initial value
        self.setValue(1)
        
    def __makePip(self, x, y):
        'Internal helper method to draw a pip at (x,y)'
        pip = Circle(Point(x,y), radius = self.psize)
        pip.setFill(self.foreground)
        pip.setOutline(self.foreground)
        
        return pip
    
    def setValue(self, value):
        "Set this die to display value."
        # turn all pips off
        for i in range(len(self.pips)): 
            self.pips[i].undraw()
            
        for i in self.pipIndices[value]:
            self.pips[i].draw(self.win)
        