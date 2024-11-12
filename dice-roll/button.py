from graphics import *

class Button:
    """ A button is a labeled rectange in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method returns true
    if the button is active and p in inside it. """
    
    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg: 
        qb = Button(windowName, centerPoint, width, height, 'textOnButton') """
        
        w, h = width/2, height/2
        x, y = center.getX(), center.getY()
        
        self.xmax, self.xmin = x+w , x-w
        self.ymax, self.ymin = y+h, y-h
        
        pointLL = Point(self.xmin, self.ymin)
        pointUR = Point(self.xmax, self.ymax)
        
        self.rect = Rectangle(pointLL, pointUR)
        self.rect.setFill("white")
        self.rect.draw(win)
        
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
        
    def clicked(self, clickedLocation):
        "Returns true if button is active and clickedLocation is inside"
        return (self.active 
                and
                self.xmin <= clickedLocation.getX() <= self.xmax 
                and
                self.ymin <= clickedLocation.getY() <= self.ymax)
    
    def getLabel(self):
        "Return the label string of this button."
        return self.label.getText()
    
    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill("black")
        self.rect.setFill("white")
        self.rect.setWidth(2)
        self.active = True
        
    def deactivate(self):
        "Sets this button to 'inactive'"
        self.label.setFill("white")
        self.rect.setFill("grey")
        self.rect.setWidth(1)
        self.active = False
