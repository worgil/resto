from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Resaurant Managament System")

Tops = Frame(root,width = 1600,height=50,bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 800,height=700,bg="powder blue", relief=SUNKEN)
f1.pack(side=LEFT)

f1 = Frame(root,width = 300,height=700,bg="powder blue", relief=SUNKEN)
f1.pack(side=RIGHT)

localtime=time.asctime((time.localtime(time.time())))

lblInfo = Label(Tops, font=('arial',50,'bold'),text="Restaurant Managament System", fg="Steel Blue", bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial',50,'bold'),text=localtime, fg="Steel Blue", bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
root.mainloop()