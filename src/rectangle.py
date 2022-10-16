from tkinter import *
from constants import WIDTH, HEIGHT

# Rectangle Class for each data point
class Rectangle:
    def __init__(self, canvas: Canvas = None, value: int = None):
        
        self.canvas = canvas
        self.value = value
        
        # initialize x and y coordinate
        self.x = (self.value * WIDTH/100) - WIDTH/100
        self.y = HEIGHT
    
        self.rectangle = self.canvas.create_rectangle(
            # top left corner
            self.x, self.y - (self.value * 3),
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
        # update value
        self.value = value
        
        # grab current coordinates (corners of rectangle)
        x0, y0, x1, y1 = self.canvas.coords(self.rectangle)

        # modifying absolute x value
        x0 = (self.value * WIDTH/100) - WIDTH/100
        
        # update coordinates on canvas
        self.canvas.moveto(self.rectangle, x0, y0)
        
