#!/usr/bin/env/python3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
import pyscreenshot as ImageGrab

#import drawPattern as draw


from tkinter.colorchooser import *
trace = 0 

class CanvasEventsDemo:
    
    def __init__(self, r,cb,parent=None):
        canvas = Canvas(r,height=1000,width=2000,bg=cb) 
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
            self.c=0
            self.kinds=canvas.create_oval
            canvas.bind('<ButtonPress-1>', self.onStart) 
            canvas.bind('<B1-Motion>',     self.onGrow)  
            canvas.bind('<Double-1>',      self.onClear) 
            canvas.bind('<ButtonPress-3>', self.onMove)
 
        def rect():
            self.kinds=canvas.create_rectangle
            self.c=0
            canvas.bind('<ButtonPress-1>', self.onStart) 
            canvas.bind('<B1-Motion>',     self.onGrow)  
            canvas.bind('<Double-1>',      self.onClear) 
            canvas.bind('<ButtonPress-3>', self.onMove)
 
        def line():
            self.c=1
            self.kinds=canvas.create_line
            canvas.bind('<ButtonPress-1>', self.onStart) 
            canvas.bind('<B1-Motion>',     self.onGrow)  
            canvas.bind('<Double-1>',      self.onClear) 
            canvas.bind('<ButtonPress-3>', self.onMove)
 
        def drawit():
            self.kinds=canvas.create_rectangle
            self.c=1
            canvas.bind('<ButtonPress-1>', self.dx) 
            canvas.bind('<B1-Motion>',     self.dx)  
            canvas.bind('<Double-1>',      self.dx) 
            canvas.bind('<ButtonPress-3>', self.dx)
            
        def cbg():
            cb=askcolor()
            canvas.configure(bg=cb[1])
        def col():
            cx=askcolor()
            self.cl=cx[1]
            return self.cl
            
        def getter():
            x2=r.winfo_rootx()+canvas.winfo_x()
            y2=r.winfo_rooty()+canvas.winfo_y()
            x1=x2+canvas.winfo_width()
            y1=y2+canvas.winfo_height()
            I=ImageGrab.grab().crop((x2,y2,x1,y1))
            
            filename=filedialog.askdirectory()
            print(filename)
            I.save(str(filename)+"/test.jpg")
            
        # Shapes
        b1=Menu(r,title="    Oval    ",font="ubuntu 10",background="dimgrey",foreground="snow")
        b1.add_command(label="       Oval         ",command=lambda: ova()) 
        b1.add_command(label="     Rectangle    ", command=lambda: rect()) 
        b1.add_command(label="       Line         ", command=lambda: line()) 
        b1.add_command(label="       Draw         ", command=lambda: drawit()) 
        b1.add_command(label="       Save          ",command=lambda:getter())
        b1.add_command(label="fill",command=lambda:canvas.bind('<B1-Motion>',     self.fill) ) 
        #separator
            #f=ttk.Separator(orient="vertical")
            #f.place(x=85, relheight=1)
            
        #shape colour
        b1.add_command(label="""  choose color  """,command=lambda: col())

        #bg color
        b1.add_command(label="""background      """,command=lambda: cbg())
        
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
            
        else:
            if self.c==1:
                objectId = self.shape(self.start.x, self.start.y,self.start.x+2,self.start.y+2)
            else:
                objectId = self.shape(self.start.x, self.start.y, event.x, event.y,outline=self.cl,width=(self.w.get()+1)/10)
            
            
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
    
    def dx(self,event):
        canvas=event.widget
        def paint(event):
            width=(self.w.get()+1)/20
            x1, y1 = ( event.x - width ), ( event.y - width  )
            x2, y2 = ( event.x +width  ), ( event.y + width  )
            canvas.create_rectangle( x1, y1, x2, y2, fill = self.cl,outline=self.cl )
        canvas.bind( "<B1-Motion>", paint )
        
"""    def fill(self,event):
        canvas=event.widget
        self.canvas.bind("<ButtonPress-1>", self.on_fill_color)
    
    def on_fill_color(self, event):
        
        self.filled = draw.fillColor(self.paper, (event.x, event.y), self.bgColor, self.chooseColor, self.paperWidth, self.paperHeight)
        self.canvas.create_image(self.paperWidth / 2, self.paperHeight / 2, image=self.filled)
        print("fill")
 """       
        
r=tk.Tk()
r.config(background="black")
cb="snow"

c=CanvasEventsDemo(r,cb)
r.mainloop()

