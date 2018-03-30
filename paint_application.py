#!/usr/bin/env python3
from tkinter import *
import tkinter as tk
from tkinter import ttk

from tkinter.colorchooser import *
trace = 0 

class CanvasEventsDemo:
    
    def __init__(self, x,cb,parent=None):
        canvas = Canvas(x,height=1000,width=2000,bg=cb) 
        canvas.grid(row=2,column=0,columnspan=2000)
        canvas.bind('<ButtonPress-1>', self.onStart) 
        canvas.bind('<B1-Motion>',     self.onGrow)  
        canvas.bind('<Double-1>',      self.onClear) 
        canvas.bind('<ButtonPress-3>', self.onMove)
        self.cl="black" 
        self.c=0
        x=IntVar()
        self.w=Scale(r,variable=x,orient="horizontal",background="dimgrey")
        self.w.grid(row=1,column=8)
        
        def ova():
            self.kinds=canvas.create_oval
        def rect():
            self.kinds=canvas.create_rectangle
            c=0
        def line():
            self.kinds=canvas.create_line
        def draw():
            self.kinds=canvas.create_rectangle
            c=1
        def cbg():
            cb=askcolor()
            canvas.configure(bg=cb[1])
        def col():
            cx=askcolor()
            self.cl=cx[1]
            return self.cl
        # Shapes
        b1=Menu(r,title="    Oval    ",font="ubuntu 15",background="dimgrey",foreground="deepskyblue")
        b1.add_command(label="     oval     ",command=lambda: ova()) 
        b1.add_command(label="     Rectangle     ", command=lambda: rect()) 
        b1.add_command(label="     Line    ", command=lambda: line()) 
        
        #separator
            #f=ttk.Separator(orient="vertical")
            #f.place(x=85, relheight=1)
            
        #shape colour
        b1.add_command(label="""  choose color  """,command=lambda: col())

        #bg color
        b1.add_command(label="""bg color""",command=lambda: cbg())
        
        r.config(menu=b1)
        self.canvas = canvas
        self.drawn  = None
        self.kinds = canvas.create_oval     # [canvas.create_rectangle]
        
    def onStart(self, event):
        self.shape = self.kinds             #[0]
        self.kinds = self.kinds             #[1:] + [:1]
        self.start = event
        self.drawn = None
        
    def onGrow(self, event):                         
        canvas = event.widget
        #print(self.cl)
        # deletes the previously made shape
        if self.drawn: 
            canvas.delete(self.drawn)
        if self.kinds==canvas.create_line:
            objectId = self.shape(self.start.x, self.start.y, event.x, event.y,fill=self.cl,width=(self.w.get()+1)/10)
            print(self.w.get())
        else:
            objectId = self.shape(self.start.x, self.start.y, event.x, event.y,outline=self.cl,width=(self.w.get()+1)/10)
            print(self.w.get())
#        if trace:
#            print (objectId)
        
        self.drawn = objectId
        
    def onClear(self, event):
        event.widget.delete('all')
        
    def onMove(self, event):
        if self.drawn:                               
            if trace: 
                print (self.drawn)
            canvas = event.widget
            diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
            canvas.move(self.drawn, diffX, diffY)
            self.start = event
            
r=tk.Tk()
r.config(background="black")
cb="snow"

c=CanvasEventsDemo(r,cb)
r.mainloop()


           
