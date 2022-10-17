from tkinter import *
from rectangle import Rectangle
import numpy as np
from time import sleep 
from constants import WIDTH, HEIGHT, N

# initialize/generate array of a range of elements
# in this case range of 1-101 exclusive
def genArray(arr: list[Rectangle]):
	for i in range(1, N+1):
		arr.append(Rectangle(canvas, i))

# swaps two elements in the array
# as long as they are not the same element
def swap(index1: int, index2: int):
	if index1 != index2:
		canvas.update()
		x1 = arr[index1].getPos()
		x2 = arr[index2].getPos()
		arr[index1].updatePos(x2)
		arr[index2].updatePos(x1)
		tempRect: Rectangle = arr[index1]
		arr[index1] = arr[index2]
		arr[index2] = tempRect

		

# generates a random numpy array and then 
# uses it to randomize the Rectangle array
def randomize():
	print('Randomizing Array...')
	npArr = np.arange(0, N)
	np.random.shuffle(npArr)
	index = 0
	for randIndex in npArr:
		swap(index, randIndex)
		index += 1
	print('Randomizing Complete')

# animation that plays when sort is complete
def sortComplete():
	for i in range(N):
		arr[i].changeColor('lime')
		canvas.update()
		sleep(.00001)
	sleep(.5)
	for i in range(N):
		arr[i].changeColor('white')
		canvas.update()
	
# runs the bubble sort algorithm on the current array
def bubbleSort():
	print('Running BubbleSort...')
	for i in range(N):
		for j in range(0, N-i-1):
			arr[j].changeColor('blue')
			arr[j+1].changeColor('red')
			if arr[j].getVal() > arr[j+1].getVal():
				swap(j, j+1)
			arr[j].changeColor('white')
			arr[j+1].changeColor('white')

	sortComplete()
	print('BubbleSort Complete')
	

			

# handle key press
def key_pressed(event):
	if event.char == 'r':
		randomize()
	if event.char == 'b':
		bubbleSort()


if __name__ == "__main__":
	# Window initialization

	window = Tk()
	window.geometry(f'{WIDTH}x{HEIGHT}')
	window.title('Sort Algorithm Visualizer')

	# Canvas initialization
	canvas = Canvas(window, bg = 'black', width=f'{WIDTH}', height=f'{HEIGHT}')
	canvas.pack()
	# generate initial array
	arr: list[Rectangle] = []
	genArray(arr)

	# initialize labels
	data = StringVar()
	data_label = Label(canvas, 
		anchor=NW, 
		justify=LEFT,
		bg='black', 
		fg='white',
		textvariable=data,
		height='20',
		width='100'
		)
	data.set('Comparisons:')
	# data_label.pack()

	# listen for keyboard input
	window.bind('<Key>', key_pressed)
	window.mainloop()
