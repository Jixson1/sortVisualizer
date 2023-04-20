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
		arr[index1], arr[index2] = arr[index2], arr[index1]

# generates a random numpy array and then 
# uses it to randomize the Rectangle array
def randomize():
	npArr = np.arange(0, N)
	np.random.shuffle(npArr)
	index = 0
	for randIndex in npArr:
		swap(index, randIndex)
		index += 1

# animation that plays when sort is complete
def sortComplete():
	for i in range(N):
		arr[i].changeColor('lime')
		canvas.update()
	sleep(.5)
	for i in range(N):
		arr[i].changeColor('white')
		canvas.update()
	
# runs the bubble sort algorithm on the current array
def bubbleSort():
	for i in range(N):
		for j in range(0, N-i-1):
			arr[j].changeColor('blue')
			arr[j+1].changeColor('red')
			if arr[j].getVal() > arr[j+1].getVal():
				swap(j, j+1)
			arr[j].changeColor('white')
			arr[j+1].changeColor('white')

		sleep(.0001)

# runs the selection sort algorithm on the current array
def selectionSort():
	for i in range(N):
		min_index = i

		for j in range((i + 1), N):
			if arr[j].getVal() < arr[min_index].getVal():
				min_index = j

		arr[i].changeColor('blue')
		arr[min_index].changeColor('red')

		swap(i, min_index)
		
		arr[i].changeColor('white')
		arr[min_index].changeColor('white')
		sleep(.0001)

# partition function utilized in quicksort()
def partition(low, high):
	pivot_item = arr[low]
	j = low
	for i in range(low, high+1):
		if arr[i].getVal() < pivot_item.getVal():
			j += 1
			arr[i].changeColor('blue')
			arr[j].changeColor('red')
			swap(i, j)
			arr[i].changeColor('white')
			arr[j].changeColor('white')
	pivot_point = j
	swap(low, pivot_point)
	return pivot_point

# runs the QuickSort algorithm on the current array
def quickSort(low, high):
	if high > low:
		p_index = partition(low, high)
		quickSort(low, (p_index - 1))
		quickSort((p_index + 1), high)

# runs the Merge Sort algorithm on the current array
# algorithm code sourced from:
# https://www.geeksforgeeks.org/merge-sort/
def mergeSort(subset: list[Rectangle]):
	if len(subset) > 1:
		mid = len(subset)//2

		L: list[Rectangle] = subset[:mid]
		R: list[Rectangle] = subset[mid:]
		mergeSort(L)
		mergeSort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i].getVal() <= R[j].getVal():
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


# handle keyboard input
def key_pressed(event):
	if event.char == 'r':
		print('Randomizing Array...')
		randomize()
		print('Randomizing Complete')
	if event.char == 'b':
		print('Running Bubble Sort...')
		bubbleSort()
		sortComplete()
		print('Bubble Sort Complete')
	if event.char == 's':
		print('Running Selection Sort...')
		selectionSort()
		sortComplete()
		print('Selection Sort Complete')
	if event.char == 'q':
		print('Running QuickSort...')
		quickSort(0, (N-1))
		sortComplete()
		print('QuickSort Complete')
	if event.char == 'm':
		print('Running Merge Sort...')
		mergeSort(arr)
		sortComplete()
		print('Merge Sort Complete')


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
