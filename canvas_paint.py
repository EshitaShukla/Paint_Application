from tkinter import*
from tkinter.colorchooser import *
import tkinter

import random
root = tkinter.Tk()

w = tkinter.Canvas( bg="snow")

canvas_width = 500
canvas_height = 150


def x(col):
    
    def paint(event):
        print (col)
        python_colour= col
        x1, y1 = ( event.x - 4 ), ( event.y - 4 )
        x2, y2 = ( event.x +4 ), ( event.y + 4 )
        w.create_rectangle( x1, y1, x2, y2, fill = python_green,outline=col)

    w.bind( "<B1-Motion>", paint )

def getColor():
    col =askcolor()
    x(col[1])

master = Tk()
master.title( "Paint Application" )
w = Canvas(master, height=600,width=2000)
w.grid(row=0,columnspan=13)
w.bind( "<B1-Motion>", x("black") )

w.grid()

while True:
    getColor()

message = Label( master, text = """Press and Drag the mouse to draw.
To change color, select the color of your chaoice and press 'OK'""" )
message.grid(columnspan=8)

root.mainloop()






