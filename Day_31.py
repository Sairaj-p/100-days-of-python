#Flash Card App

from tkinter import *
import pandas
import random
bg_color="#B1DDC6"
c_word ={}


try:
    cards = pandas.read_csv(r"E:\New folder\Flash Card\data\Words_to_learn.csv")
except:
    cards = pandas.read_csv(r"E:\New folder\Flash Card\data\french_words.csv")
finally:
    tolearn = cards.to_dict(orient="records")


def Translate_word(c_word):
    canvas.itemconfig(card_img,image=fc_back)
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(words,text=c_word["English"],fill="white")


def change_word():
    global flip_time,c_word
    window.after_cancel(flip_time)
    c_word = random.choice(tolearn)
    canvas.itemconfig(card_img,image=fc_front)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(words,text=c_word["French"],fill="black")
    flip_time = window.after(3000,Translate_word,c_word)

    
def correct_ans():
    global tolearn
    tolearn.remove(c_word)
    data = pandas.DataFrame(tolearn)
    data.to_csv(r"E:\New folder\Flash Card\data\Words_to_learn.csv",index=False)
    
    change_word()

    
#__________________________________UI___________________________________#

window=Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=bg_color)
c_word = random.choice(tolearn)
flip_time = window.after(3000,Translate_word,c_word)
correct_b_img =PhotoImage(file=r"E:\New folder\Flash Card\images\right.png")
wrong_b_img =PhotoImage(file=r"E:\New folder\Flash Card\images\wrong.png")
canvas=Canvas(width=800,height=526,bg=bg_color,highlightthickness=0)
fc_back=PhotoImage(file=r"E:\New folder\Flash Card\images\card_back.png")
fc_front =PhotoImage(file=r"E:\New folder\Flash Card\images\card_front.png") 
card_img =canvas.create_image(400,268,image=fc_front)
title =canvas.create_text(400,150,text="French",font=("Ariel",25,"italic"))
words =canvas.create_text(400,263,text="Begin",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)
wrong_b = Button(image=wrong_b_img,bg=bg_color,highlightthickness=0,command=change_word)
wrong_b.grid(row=1,column=0)
correct_b = Button(image=correct_b_img,bg=bg_color,highlightthickness=0,command=correct_ans)
correct_b.grid(row=1,column=1)

window.mainloop()