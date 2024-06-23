from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)

def Conversion():
    mile = float(input.get())
    kilometer = round(mile)*1.609
    answer.config(text=kilometer)

input = Entry(width=10)
input.insert(END,string="0")
input.grid(column=1,row=0)

miles = Label(text="Miles")
miles.grid(column=2,row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0,row=1)

km = Label(text="Km")
km.grid(column=2,row= 1)

answer = Label(text="0")
answer.grid(column=1,row=1)

calcualate = Button(text="Calculate",command=Conversion)
calcualate.grid(column=1,row=2)

window.mainloop()
