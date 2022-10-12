from tkinter import *

# Rectangle Class for each data point
class Rectangle:
    def __init__(self, window: Tk = None, canvas: Canvas = None, value: int = None):
        
        self.canvas = canvas
        self.value = value
        
        # initialize x and y coordinate
        self.x = (self.value * 5) - 5
        self.y = 350
    
        self.rectangle = self.canvas.create_rectangle(
            # top left corner
            self.x, self.y - (self.value * 2),
            # bottom right corner
            self.x + 5, self.y,
            fill = "white"
        )
        self.canvas.pack()

    # Returns the value of the Rectangle object
    # in this position
    def getVal(self):
        return self.value
    
    # Updates value of Rectangle object
    # in this position
    def updateVal(self, value):
        self.value = value
        newX = (self.value * 5) - 5
