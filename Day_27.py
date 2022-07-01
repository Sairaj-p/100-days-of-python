#Pyhton GUI Tkinter

from tkinter import *

window = Tk()
window.title("Miles To Kms Coverter")
window.config(padx=10,pady=10)

input= Entry(width =7)
input.grid(column=1,row=0)

miles_Label = Label(text="Miles")
miles_Label.grid(column=2,row=0)

isequal = Label(text="Is equal to")
isequal.grid(column =0,row=3)

kilometer_label = Label(text="kms")
kilometer_label.grid(column=2,row=3)

kilo_Result =Label(text ="0")
kilo_Result.grid(column =1,row=3)

def Converter():
    result = float(input.get())
    result *= 1.609
    result = round(result,3)
    kilo_Result.config(text=f"{result}")
convert_b = Button(text="Convert",command=Converter)
convert_b.grid(column = 2,row =4)

mainloop()
