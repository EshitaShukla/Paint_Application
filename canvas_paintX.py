from tkinter import*
import tkinter

import random
root = tkinter.Tk()


w = tkinter.Canvas( bg="snow")
w1= tkinter.Canvas( bg="snow")

canvas_width = 500
canvas_height = 150


def x(col):
    
    def paint(event):
        print (col)
        python_green = col
        x1, y1 = ( event.x - 4 ), ( event.y - 4 )
        x2, y2 = ( event.x +4 ), ( event.y + 4 )
        w.create_rectangle( x1, y1, x2, y2, fill = python_green,outline=col)

    def paint2(event):
        print (col)
        python_green = red
        x1, y1 = ( event.x - 4 ), ( event.y - 4 )
        x2, y2 = ( event.x +4 ), ( event.y + 4 )
        w.create_rectangle( x1, y1, x2, y2, fill = python_green,outline=col )
        
    w.bind( "<B1-Motion>", paint )




master = Tk()
master.title( "Painting using Ovals" )
w = Canvas(master, height=600,width=2000)
w.grid(row=0,columnspan=26)
w.bind( "<B1-Motion>", x("black") )

w.grid()


# Making buttons (individually)
b1=Button(master,text="     ",bg="red")
b1["command"]=lambda:x("red")
b1.grid(row=1,column=0)

b2=Button(master,text="     ",bg="crimson")
b2["command"]=lambda:x("crimson")
b2.grid(row=2)

b3=Button(master,text="     ",bg="salmon")
b3["command"]=lambda:x("salmon")
b3.grid(row=3)

b4=Button(master,text="     ",bg="darkred")
b4["command"]=lambda:x("darkred")
b4.grid(row=4,column=0)

b13=Button(master,text="     ",bg="pink")
b13["command"]=lambda:x("pink")
b13.grid(row=1,column=1)

b5=Button(master,text="     ",bg="hotpink")
b5["command"]=lambda:x("hotpink")
b5.grid(row=2,column=1)

b6=Button(master,text="     ",bg="deeppink")
b6["command"]=lambda:x("deeppink")
b6.grid(row=3,column=1)

b7=Button(master,text="     ",bg="mediumvioletred")
b7["command"]=lambda:x("mediumvioletred")
b7.grid(row=4,column=1)

b8=Button(master,text="     ",bg="orangered")
b8["command"]=lambda:x("orangered")
b8.grid(row=1,column=2)

b9=Button(master,text="     ",bg="tomato")
b9["command"]=lambda:x("tomato")
b9.grid(row=2,column=2)

b10=Button(master,text="     ",bg="coral")
b10["command"]=lambda:x("coral")
b10.grid(row=3,column=2)

b11=Button(master,text="     ",bg="darkorange")
b11["command"]=lambda:x("darkorange")
b11.grid(row=4,column=2)

b12=Button(master,text="     ",bg="orange")
b12["command"]=lambda:x("orange")
b12.grid(row=1,column=3)

b14=Button(master,text="     ",bg="gold")
b14["command"]=lambda:x("gold")
b14.grid(row=2,column=3)

b15=Button(master,text="     ",bg="yellow")
b15["command"]=lambda:x("yellow")
b15.grid(row=3,column=3)

b16=Button(master,text="     ",bg="lemonchiffon")
b16["command"]=lambda:x("peachpuff")
b16.grid(row=4,column=3)

b17=Button(master,text="     ",bg="lemonchiffon")
b17["command"]=lambda:x("plum")
b17.grid(row=1,column=4)

b18=Button(master,text="     ",bg="violet")
b18["command"]=lambda:x("violet")
b18.grid(row=2,column=4)

b19=Button(master,text="     ",bg="magenta")
b19["command"]=lambda:x("magenta")
b19.grid(row=3,column=4)

b20=Button(master,text="     ",bg="darkorchid")
b20["command"]=lambda:x("darkorchid")
b20.grid(row=4,column=4)

b21=Button(master,text="     ",bg="darkviolet")
b21["command"]=lambda:x("darkviolet")
b21.grid(row=1,column=5)

b22=Button(master,text="     ",bg="purple")
b22["command"]=lambda:x("purple")
b22.grid(row=2,column=5)

b23=Button(master,text="     ",bg="darkmagenta")
b23["command"]=lambda:x("darkmagenta")
b23.grid(row=3,column=5)

b24=Button(master,text="     ",bg="indigo")
b24["command"]=lambda:x("indigo")
b24.grid(row=4,column=5)

b25=Button(master,text="     ",bg="lightcyan")
b25["command"]=lambda:x("lightcyan")
b25.grid(row=1,column=7)

b26=Button(master,text="     ",bg="aqua")
b26["command"]=lambda:x("aqua")
b26.grid(row=2,column=7)

b27=Button(master,text="     ",bg="aquamarine")
b27["command"]=lambda:x("aquamarine")
b27.grid(row=3,column=7)

b28=Button(master,text="     ",bg="turquoise")
b28["command"]=lambda:x("turquoise")
b28.grid(row=4,column=7)

b29=Button(master,text="     ",bg="skyblue")
b29["command"]=lambda:x("skyblue")
b29.grid(row=1,column=8)

b30=Button(master,text="     ",bg="lightskyblue")
b30["command"]=lambda:x("lightskyblue")
b30.grid(row=2,column=8)

b31=Button(master,text="     ",bg="cornflowerblue")
b31["command"]=lambda:x("cornflowerblue")
b31.grid(row=3,column=8)

b32=Button(master,text="     ",bg="royalblue")
b32["command"]=lambda:x("royalblue")
b32.grid(row=4,column=8)

b33=Button(master,text="     ",bg="darkblue")
b33["command"]=lambda:x("darkblue")
b33.grid(row=1,column=9)

b34=Button(master,text="     ",bg="deepskyblue")
b34["command"]=lambda:x("deepskyblue")
b34.grid(row=2,column=9)

b35=Button(master,text="     ",bg="dodgerblue")
b35["command"]=lambda:x("dodgerblue")
b35.grid(row=3,column=9)

b36=Button(master,text="     ",bg="midnightblue")
b36["command"]=lambda:x("midnightblue")
b36.grid(row=4,column=9)

b37=Button(master,text="     ",bg="cornsilk")
b37["command"]=lambda:x("cornsilk")
b37.grid(row=1,column=10)

b38=Button(master,text="     ",bg="peachpuff")
b38["command"]=lambda:x("peachpuff")
b38.grid(row=2,column=10)

b39=Button(master,text="     ",bg="navajowhite")
b39["command"]=lambda:x("navajowhite")
b39.grid(row=3,column=10)

b40=Button(master,text="     ",bg="tan")
b40["command"]=lambda:x("tan")
b40.grid(row=4,column=10)

b41=Button(master,text="     ",bg="sandybrown")
b41["command"]=lambda:x("sandybrwn")
b41.grid(row=1,column=11)

b42=Button(master,text="     ",bg="chocolate")
b42["command"]=lambda:x("chocolate")
b42.grid(row=2,column=11)

b43=Button(master,text="     ",bg="saddlebrown")
b43["command"]=lambda:x("saddlebrown")
b43.grid(row=3,column=11)

b44=Button(master,text="     ",bg="maroon")
b44["command"]=lambda:x("maroon")
b44.grid(row=4,column=11)

b45=Button(master,text="     ",bg="snow")
b45["command"]=lambda:x("snow")
b45.grid(row=1,column=12)

b46=Button(master,text="     ",bg="honeydew")
b46["command"]=lambda:x("honeydew")
b46.grid(row=2,column=12)

b47=Button(master,text="     ",bg="antiquewhite")
b47["command"]=lambda:x("aquamarine")
b47.grid(row=3,column=12)

b48=Button(master,text="     ",bg="mistyrose")
b48["command"]=lambda:x("mistyrose")
b48.grid(row=4,column=12)

b49=Button(master,text="     ",bg="seashell")
b49["command"]=lambda:x("seashell")
b49.grid(row=1,column=13)

b50=Button(master,text="     ",bg="aliceblue")
b50["command"]=lambda:x("aliceblue")
b50.grid(row=2,column=13)

b51=Button(master,text="     ",bg="lightgray")
b51["command"]=lambda:x("lightgray")
b51.grid(row=3,column=13)

b52=Button(master,text="     ",bg="silver")
b52["command"]=lambda:x("silver")
b52.grid(row=4,column=13)

b53=Button(master,text="     ",bg="darkgray")
b53["command"]=lambda:x("darkgray")
b53.grid(row=1,column=14)

b54=Button(master,text="     ",bg="gray")
b54["command"]=lambda:x("gray")
b54.grid(row=2,column=14)

b55=Button(master,text="     ",bg="dimgray")
b55["command"]=lambda:x("dimgray")
b55.grid(row=3,column=14)

b56=Button(master,text="     ",bg="black")
b56["command"]=lambda:x("black")
b56.grid(row=4,column=14)

b57=Button(master,text="     ",bg="greenyellow")
b57["command"]=lambda:x("greenyellow")
b57.grid(row=1,column=6)

b58=Button(master,text="     ",bg="lime")
b58["command"]=lambda:x("lime")
b58.grid(row=2,column=6)

b59=Button(master,text="     ",bg="springgreen")
b59["command"]=lambda:x("springgreen")
b59.grid(row=3,column=6)

b60=Button(master,text="     ",bg="darkgreen")
b60["command"]=lambda:x("darkgreen")
b60.grid(row=4,column=6)



message = Label( master, text = "Press and Drag the mouse to draw" )
message.grid(columnspan=8)


root.mainloop()




