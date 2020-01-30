from tkinter import *
from tkinter.messagebox import showinfo

win = Tk()
win.title("Temprature Converter")

def c_to_f():
    value = int(entry.get())
    answer = (value * 9/5) + 32
    showinfo("Answer",f"{value} C = {answer} F")

def f_to_c():
    value = int(entry.get())
    answer = (value - 32) * 5/9
    showinfo("Answer",f"{value} F = {answer} C")

label = Label(win,text="Enter Temorature Here :",font=('arial',15,'bold'))
label.grid(row=0,column=0)

entry = Entry(win,font=('arial',20,'bold'))
entry.grid(row=1,column=0)

button1 = Button(win,text="Calcius To Farnhite",font=('arial',15,'bold')
                ,command=c_to_f,bg="black",fg="yellow")
button1.grid(row=3,column=0)

button2 = Button(win,text="Farnhite To Calcius ",font=('arial',15,'bold')
                ,command=f_to_c,bg="black",fg="yellow")
button2.grid(row=4,column=0)

win.mainloop()