from turtle import *

class Disk():
    def __init__(name,x,y,height,width,color):
        self.name = name
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
    
    def showdisk(self):
        pu()
        goto(self.x,self.y)
        pd()
        fillcolor(self.color)
        begin_fill()
        fd(self.width/2)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width/2)
        end_fill()

    def newpos(self,x,y):
        cleardisk()
        self.x = x
        self.y = y
        showdisk()

    def cleardisk():
        pu()
        goto(self.x,self.y)
        pd()
        fillcolor("white")
        begin_fill()
        fd(self.width/2)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width/2)
        end_fill()
