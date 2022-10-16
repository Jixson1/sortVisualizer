from tkinter import *
from rectangle import Rectangle
import numpy as np
# from time import sleep <--- not used yet
from constants import WIDTH, HEIGHT

# initialize/generate array of a range of elements
# in this case range of 1-101 exclusive
def genArray(arr: list[Rectangle]):
	for i in range(1, 101):
		arr.append(Rectangle(canvas, i))

# swaps two elements in the array
# as long as they are not the same element
def swap(index1: int, index2: int):
	if index1 != index2:
		tempVal = arr[index1].getVal()
		arr[index1].updateVal(arr[index2].getVal())
		arr[index2].updateVal(tempVal)

# generates a random numpy array and then 
# uses it to randomize the Rectangle array
def randomize():
	npArr = np.arange(0, 100)
	np.random.shuffle(npArr)
	index = 0
	for randIndex in npArr:
		swap(index, randIndex)
		index += 1

# handle key press
def key_pressed(event):
	print(event)
	if event.char == 'r':
		randomize()


if __name__ == "__main__":
	# Window initialization

	# WIDTH, HEIGHT = 
	window = Tk()
	window.geometry(f'{WIDTH}x{HEIGHT}')
	window.title('Sort Algorithm Visualizer')

	# Canvas initialization
	canvas = Canvas(window, bg = 'black', width=f'{WIDTH}', height=f'{HEIGHT}')
	canvas.pack()
	# generate initial array
	arr: list[Rectangle] = []
	genArray(arr)
	window.bind('<Key>', key_pressed)
	
	window.mainloop()
