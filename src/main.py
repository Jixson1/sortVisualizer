from tkinter import *
from rectangle import Rectangle
import numpy as np
from time import sleep

def genArray(arr: list[Rectangle]):
	for i in range(1, 101):
		arr.append(Rectangle(window, canvas, i))

def randomize(arr: list[Rectangle]):
	npArr = np.arange(0, 100)
	np.random.shuffle(npArr)
	index = 0
	for val in npArr:
		if index != val:
			tempVal = arr[index].getVal()
			arr[index].updateVal(arr[val].getVal())
			arr[val].updateVal(tempVal)
			index += 1
		# temp = arr[index]
		# arr[index] = arr[val]
		# arr[val] = temp
		# index += 1

if __name__ == "__main__":
	# Window initialization
	window = Tk()
	window.geometry('500x350')
	window.title('Sort Algorithm Visualizer')

	# Canvas initialization
	canvas = Canvas(window, bg = 'black', width='500', height='350')
	canvas.pack()
	# generate initial array
	arr: list[Rectangle] = []
	genArray(arr)
	window.bind('<KeyPress-Up>', lambda e: randomize(arr))
	
	window.mainloop()
