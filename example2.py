#!python3

# Basic Class Object

import tkinter as tk
import random

w = tk.Tk()
w.geometry("500x400")
w.attributes("-topmost",True)

c = tk.Canvas(w,width=480,height=380)
c.pack()


class mainChar:
    parent = None
    me = None
    speed = 5

    def __init__(self,parent,speed=5):
        self.parent = parent
        self.speed = speed
        self.me = parent.create_rectangle(30,30,40,40,fill="#dddddd")
        self.parent.after(200,self.randColor)

    def randColor(self):
        n = "0123456789abcdef"
        tval = "#"
        for i in range(6):
            tval += n[random.randint(0,15)]
        self.parent.itemconfig(self.me,fill=tval)
        self.parent.after(200,self.randColor)

    def move(self,e):
        dirs = {"Right" : (1,0), "Left" : (-1,0), "Up" : (0,-1), "Down" : (0,1)}
        x = self.speed * dirs[e.keysym][0]
        y = self.speed * dirs[e.keysym][1]
        # note the difference in how we handled things with the next 2 lines
        #c.move(rectangle, x, y)
        self.parent.move( self.me , x , y)

r = mainChar(c)

w.bind("<Left>",r.move)
w.bind("<Right>",r.move)
w.bind("<Up>",r.move)
w.bind("<Down>",r.move)


w.mainloop()