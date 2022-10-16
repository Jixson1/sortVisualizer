from tkinter import *

# Rectangle Class for each data point
class Rectangle:
    def __init__(self, canvas: Canvas = None, value: int = None):
        
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

    # Returns the value of the Rectangle object
    # in this position
    def getVal(self):
        return self.value
    
    # Updates value of Rectangle object
    # and modifies its coordinates accordingly
    def updateVal(self, value: int):
        # grab current coordinates (corners of rectangle)
        x0, y0, x1, y1 = self.canvas.coords(self.rectangle)

        # modify coordinates based off changed value to resize rectangle in place
        self.value = value
        x0 = (self.value * 5) - 5
        y0 = 350 - (self.value * 2)
        x1 = x0 + 5
        # y2 is always 350 (or bottom of screen)
        self.canvas.moveto(self.rectangle, x0, y0)
        # update coordinates on canvas
        # self.canvas.coords(self.rectangle, x0, y0, x1, y1)
        # print('my value is', value, 'my new coords are:', x0, y0, x1, y1)
