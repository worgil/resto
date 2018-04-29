from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Resaurant Managament System")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)
##########################ZAMAN###########################
localtime = time.asctime((time.localtime(time.time())))
##################BİLGİ###################################

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Restaurant Managament System", fg="Steel Blue", bd=10,
                anchor='w')
lblInfo.grid(row=0, column=0)
lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)


######################HESAP MAKINESI####################
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""
def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)
def qExit():
    root.destroy()
def Reset():
    rand.set("")
    cay.set("")
    kahve.set("")
    kola.set("")
    msuyu.set("")
    nescafe.set("")
    drinks.set("")
    cost.set("")
    service.set("")
    statetax.set("")
    totalcost.set("")


txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="7", bg="powder blue", command=lambda: btnClick(7)).grid(row=2, column=0)
btn8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="8", bg="powder blue", command=lambda: btnClick(8)).grid(row=2, column=1)
btn9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="9", bg="powder blue", command=lambda: btnClick(9)).grid(row=2, column=2)
Addition = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="+", bg="powder blue", command=lambda: btnClick("+")).grid(row=2, column=3)
# ----------------------------------------------------------------------------------------------#
btn4 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="4", bg="powder blue", command=lambda: btnClick(4)).grid(row=3, column=0)
btn5 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="5", bg="powder blue", command=lambda: btnClick(5)).grid(row=3, column=1)
btn6 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="6", bg="powder blue", command=lambda: btnClick(6)).grid(row=3, column=2)
Addition = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="-", bg="powder blue", command=lambda: btnClick("-")).grid(row=3, column=3)

# ---------------------------------------------------------------------------------------------#

btn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="1", bg="powder blue", command=lambda: btnClick(1)).grid(row=4, column=0)
btn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="2", bg="powder blue", command=lambda: btnClick(2)).grid(row=4, column=1)
btn3 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="3", bg="powder blue", command=lambda: btnClick(3)).grid(row=4, column=2)
Addition = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="*", bg="powder blue", command=lambda: btnClick("*")).grid(row=4, column=3)

# ----------------------------------------------------------------------------------------------#
btn0 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="0", bg="powder blue", command=lambda: btnClick(0)).grid(row=5, column=0)
btnClear = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="C", bg="powder blue", command=btnClearDisplay).grid(row=5, column=1)
btnEquals = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                   text="=", bg="powder blue", command=btnEqualsInput).grid(row=5, column=2)
Division = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="/", bg="powder blue", command=lambda: btnClick("/")).grid(row=5, column=3)
#----------------------------------------Menu Info 1----------------------------------------------------------#
rand=StringVar()
cay=StringVar()
kahve=StringVar()
kola=StringVar()
msuyu=StringVar()
nescafe=StringVar()
drinks=StringVar()
cost=StringVar()
service=StringVar()
statetax=StringVar()
totalcost=StringVar()

lblReference=Label(f1,font=('arial', 16, 'bold'),text="   Referans",bd=16,anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial', 16, 'bold'),textvariable=rand, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtReference.grid(row=0,column=1)
#--------------------------------------------------------------------------------------
lblCay=Label(f1,font=('arial', 16, 'bold'),text="Küçük Cay",bd=16,anchor='w')
lblCay.grid(row=1,column=0)
txtCay=Entry(f1,font=('arial', 16, 'bold'),textvariable=cay, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtCay.grid(row=1,column=1)
#--------------------------------------------------------------------------------------
lblKahve=Label(f1,font=('arial', 16, 'bold'),text="T. Kahvesi",bd=16,anchor='w')
lblKahve.grid(row=2,column=0)
txtKahve=Entry(f1,font=('arial', 16, 'bold'),textvariable=kahve, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtKahve.grid(row=2,column=1)
#--------------------------------------------------------------------------------------
lblKola=Label(f1,font=('arial', 16, 'bold'),text="Fanta / Cola",bd=16,anchor='w')
lblKola.grid(row=3,column=0)
txtKola=Entry(f1,font=('arial', 16, 'bold'),textvariable=kola, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtKola.grid(row=3,column=1)

#--------------------------------------------------------------------------------------
lblMsuyu=Label(f1,font=('arial', 16, 'bold'),text="Meyve Suyu",bd=16,anchor='w')
lblMsuyu.grid(row=4,column=0)
txtMsuyu=Entry(f1,font=('arial', 16, 'bold'),textvariable=msuyu, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtMsuyu.grid(row=4,column=1)

#--------------------------------------------------------------------------------------
lblNescafe=Label(f1,font=('arial', 16, 'bold'),text="Nescafe",bd=16,anchor='w')
lblNescafe.grid(row=5,column=0)
txtNescafe=Entry(f1,font=('arial', 16, 'bold'),textvariable=nescafe, bd=10, insertwidth=4,
                   bg="powder blue", justify='right')
txtNescafe.grid(row=5,column=1)

#========================================Menu Info 2======================================#

lblDrinks=Label(f1,font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial', 16, 'bold'),textvariable=drinks, bd=10, insertwidth=4,
                   bg="#fff", justify='right')
txtDrinks.grid(row=0,column=3)

#--------------------------------------------------------------------------------------
lblCost=Label(f1,font=('arial', 16, 'bold'),text="Cost",bd=16,anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial', 16, 'bold'),textvariable=cost, bd=10, insertwidth=4,
              bg="#fff", justify='right')
txtCost.grid(row=1,column=3)

#--------------------------------------------------------------------------------------
lblService=Label(f1,font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor='w')
lblService.grid(row=2,column=2)
txtService=Entry(f1,font=('arial', 16, 'bold'),textvariable=service, bd=10, insertwidth=4,
                 bg="#fff", justify='right')
txtService.grid(row=2,column=3)

#--------------------------------------------------------------------------------------
lblStateTax=Label(f1,font=('arial', 16, 'bold'),text="Tate Tax",bd=16,anchor='w')
lblStateTax.grid(row=3,column=2)
txtStateTax=Entry(f1,font=('arial', 16, 'bold'),textvariable=statetax, bd=10, insertwidth=4,
                  bg="#fff", justify='right')
txtStateTax.grid(row=3,column=3)

#--------------------------------------------------------------------------------------
lblSubTotal=Label(f1,font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor='w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('arial', 16, 'bold'),textvariable=msuyu, bd=10, insertwidth=4,
                  bg="#fff", justify='right')
txtSubTotal.grid(row=4,column=3)

#--------------------------------------------------------------------------------------
lblTotalCost=Label(f1,font=('arial', 16, 'bold'),text="Total",bd=16,anchor='w')
lblTotalCost.grid(row=5,column=2)
txtTotalCost=Entry(f1,font=('arial', 16, 'bold'),textvariable=totalcost, bd=10, insertwidth=4,
                   bg="#fff", justify='right')
txtTotalCost.grid(row=5,column=3)
#============================BUTONLAR==============================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text="Toplam",bg="powder blue",command=Ref).grid(row=7,column=1)
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,
                text="Çıkış",bg="powder blue",command=qExit).grid(row=7,column=3)






root.mainloop()
