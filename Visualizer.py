from numpy import arange
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random
from bubbleSort import bubbleSort
from mergeSort import mergeSort
from quickSort import quickSort
from insertionSort import insertionSort
from selectionSort import selectionSort
from radixSort import radixSort
from heapSort import heapSort


#initialising the tk object and setting window size
root = Tk()

height, width = 800, 1600
root.maxsize(width, height)


bgColour = '#5A8F96'
root.config(bg= bgColour)


#GUI layout
frameHeight = 480
frameWidth = 150
paddingx, paddingy = 10, 5

UIframe = Frame(root, width=frameWidth, height=frameHeight, bg='grey')
UIframe.grid(row=0, column=0, padx=paddingx, pady=paddingy)
UIframe.pack_propagate(0)


#global variables
array = []
title = ""
boo = True
epochs = [0]
selected_alg = StringVar()


#defining the graph
fig, ax = plt.subplots()
ax.set_title(title)
barRec = ax.bar(range(len(array)), array, align='edge')
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)


#canvas to dipslay graph
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(column=1, row=0, padx=5, pady=5)


#fundction to draw graph based on array
def draw(array, title):
    global barRec
    global text
    ax.clear()
    barRec = ax.bar(range(len(array)), array, align='edge')
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    ax.set_title(title)
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    canvas.draw()
    root.update_idletasks()


#called when user generates a new array
def generate():
    global boo
    global epochs
    global array
    global title
    global array

    epochs[0] = 0
    boo = False
    #makes sure the user doesn't make illegal entries
    try:
        size = int(sizeEntry.get())
    except:
        size = 15

    if size < 0:
        size = 1

    title = str(algDropDown.get())

    #delete old array whenever user wants to generate a new one
    del array[:]

    #crate new array and shuffle
    array = [i + 1 for i in range(size)]
    random.shuffle(array)

    draw(array, title)


#changes the graph in real time as algorithm changes array
def updatePlot(array, rec, epochs):
    global text
    for rec, val in zip(rec, array):
        rec.set_height(val)
    epochs[0] += 1
    text.set_text("No.of operations: {}".format(epochs[0]))
    print(epochs[0])



def sortAlgo():
    global boo
    global array
    global barRec
    global epochs

    epochs = [0]
    boo = True
    
    try:
        size = int(sizeEntry.get())
    except:
        size = 15
    if size < 0:
        size = 1

    #change the value of the speed selected 
    s = 1001 - speed.get()

    #decide the algo
    if algDropDown.get() == "Merge Sort":
        algo = mergeSort(array, 0, size-1)
    elif algDropDown.get() == "Bubble Sort":
        algo = bubbleSort(array)
    elif algDropDown.get() == "Quick Sort":
        algo = quickSort(array, 0, size-1)
    elif algDropDown.get() == "Insertion Sort":
        algo = insertionSort(array)
    elif algDropDown.get() == "Selection Sort":
        algo = selectionSort(array)
    elif algDropDown.get() == "Heap Sort":
        algo = heapSort(array)
    elif algDropDown.get() == "Radix Sort":
        algo = radixSort(array)

    #start animation
    anima = anim.FuncAnimation(fig, func=updatePlot, fargs=(barRec, epochs), frames=algo, interval=s, repeat=False, blit=False)
    anima._start()
   

    


#UI
labelColour = 'grey'
buttonColour = 'red'
Label(UIframe, text="Algorithm: ", bg=labelColour).grid(row=0, column=0, padx=5, pady=5, sticky=NE)
algDropDown = ttk.Combobox(UIframe, textvariable=selected_alg, values=['Bubble Sort', 'Merge Sort', 'Quick Sort', "Insertion Sort", "Selection Sort", "Heap Sort", "Radix Sort"])
algDropDown.grid(row=0, column=1, padx=5, pady=5)
algDropDown.current(0)
Button(UIframe, text="Generate", command=generate, bg=buttonColour).grid(row=0, column=2, padx=5, pady=5)
speed = Scale(UIframe, from_=1, to=1000, length=200, digits=2, resolution=0.2, orient='horizontal', label="Select speed")
speed.grid(row=3, column=1, padx=5, pady=5)
Button(UIframe, text="Start", command=sortAlgo, bg=buttonColour).grid(row=3, column=2, padx=5, pady=5)
Label(UIframe, text="Size: ", bg=labelColour).grid(row=1, column=0, padx=5, pady=5, sticky=NE)
sizeEntry = Entry(UIframe)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)



root.mainloop()
