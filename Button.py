#button.py
# save as button.py

from graphics import *

class Button:

    def __init__(self,win,center,width,height,label):
        w,h = width/2.0,height/2.0
        x,y = center.getX(),center.getY()
        self.xmax, self.xmin = x + w,x - w
        self.ymax, self.ymin = y + h,y - h
        p1 = Point(self.xmin,self.ymin)
        p2 = Point(self.xmax,self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill("blue")
        self.rect.draw(win)
        self.label = Text(center,label)
        self.label.draw(win)
        self.deactivate()
        
    def clicked(self, p):
        return self.active == True and\
                self.xmin <=p.getX() <= self.xmax and\
                self.ymin <=p.getY() <= self.ymax
               

        
    def getLabel(self):
        return self.label.getText()

        
    def activate(self):
        self.label.setFill("white")
        self.rect.setWidth(2)
        self.active = True
        
    def deactivate(self):
        self.label.setFill("black")
        self.rect.setWidth(.5)
        self.active = False
    def changeLabel(self,text):
        self.label.setText(text)

    def changeLabelColor(self,color):
        self.label.setFill(color)

    def changeLabelStyle(self,style):
        self.label.setStyle(style)

    def changeLabelSize(self,size):
        self.label.setSize(size)
        
    def getColor(self):
        return self.rect.getColor()

    def buttonUndraw(self):
        self.active = False
        self.rect.undraw()
        self.label.undraw()

    def setColor(self,color):
        self.rect.setFill(color)
                      
