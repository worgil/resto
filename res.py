from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Resaurant Managament System")

Tops = Frame(root,width = 1600,bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 800,height=700,bg="powder blue", relief=SUNKEN)
f1.pack(side=LEFT)

f1 = Frame(root,width = 300,height=700,bg="powder blue", relief=SUNKEN)
f1.pack(side=RIGHT)

root.mainloop()