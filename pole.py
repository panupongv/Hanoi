from turtle import *

class Pole:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.stack = []
        self.top_position = 0
        self.thickness = 30
        self.length = 210

    def showpole(self):
        speed(0)
        pu()
        color("black")
        goto(self.x, self.y)
        seth(0)
        pd()
        begin_fill()
        fd(self.thickness/2)
        lt(90)
        fd(self.length)
        lt(90)
        fd(self.thickness)
        lt(90)
        fd(self.length)
        lt(90)
        fd(self.thickness/2)
        end_fill()

    def pushdisk(self, disk):
        self.stack.append(disk)
        disk.newpos(x, y + disk.thickness * len(self.stack))

    def popdisk(self):
        disk = stack.pop(len(stack) - 1)
        disk.newpos(x, self.length + 50)
        
