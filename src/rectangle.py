from tkinter import *
from constants import WIDTH, HEIGHT, N

# Rectangle Class for each data point
class Rectangle:
    def __init__(self, canvas: Canvas = None, value: int = None):
        
        self.canvas = canvas
        self.value = value
        
        # initialize x and y coordinate
        self.x = (self.value * (WIDTH/N)) - WIDTH/N
        self.y = HEIGHT
    
        self.rectangle = self.canvas.create_rectangle(
            # top left corner
            self.x, self.y - (self.value * (HEIGHT/(N*1.5))) - 10,
            # bottom right corner
            self.x + (WIDTH/N), self.y,
            fill = 'white',
        )

    # Returns the value of the Rectangle object
    # in this position
    def getVal(self):
        return self.value

    # returns current position of rectangle
    def getPos(self):
        x, _, _, _ = self.canvas.coords(self.rectangle)
        return x

    # updates position of rectangle
    def updatePos(self, x: float):
        x0, _, _, _ = self.canvas.coords(self.rectangle)
        self.canvas.move(self.rectangle, x-x0, 0)
    
    # changes color of rectangle
    def changeColor(self, color):
        self.canvas.itemconfig(self.rectangle, fill = color)
        
