#Pomodoro Timer

from tkinter import *
import time

reps=0
rep =""
pink ="#e2979c"
red ="#e7305b"
green = "#9bdeac"
yellow="#f7f5dd"
font_n = "Courier"
Work_t =25
s_break=5
L_break=20
timer = None


def Mech_t(count_m,count_s):
    global timer
    if count_s<10:
        canvas.itemconfig(timer_text,text=f"{count_m}:0{count_s}")
    else:
        canvas.itemconfig(timer_text,text=f"{count_m}:{count_s}")
    if count_s =="00":
        count_s =0
    if count_s>0:
        timer =window.after(1000,Mech_t,count_m,count_s-1)
    else:
        if count_m>0:
            timer= window.after(1000,Mech_t,count_m-1,59)
        else:
            start_timer()
            
def reset_t():
    global reps,rep,timer
    window.after_cancel(timer)
    reps =0
    rep=""
    check_marks.config(text=rep)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Timer")
        
def start_timer():
    global reps,rep,Work_t,s_break,L_break
    reps += 1
    if reps<9:
        if  reps ==8:
            Mech_t(L_break,0)
            label.config(text="Big Break",fg =red)
            reset_t()
        
        elif reps%2==0 :
            Mech_t(s_break,0)
            label.config(text="Break",fg =pink)
        else:
            label.config(text="Work",fg =green)
            Mech_t(Work_t,0)
            rep +="✔"
            check_marks.config(text=rep)


#Main Setup 

window =Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg=yellow)

label = Label(text="Timer",fg=green,bg=yellow,font=(font_n,25,"bold"))
label.grid(column=1,row=0)
canvas = Canvas(width=200,height=224,bg=yellow,highlightthickness=0)
Tomato_img =PhotoImage(file=r"E:\New folder\Pomodoro\tomato.png")
canvas.create_image(100,112,image=Tomato_img)
timer_text=canvas.create_text(100,135,text="00:00",fill="white",font=(font_n,23,"bold"))
canvas.grid(column=1,row=1)
start_b = Button(text="Start",highlightthickness=0,command=start_timer)
start_b.grid(column=0,row=2)
reset_b=Button(text="Reset",highlightthickness=0,command=reset_t)
reset_b.grid(column=2,row=2)
check_marks = Label(text=rep,fg=green,bg=yellow,highlightthickness=0)
check_marks.grid(column=1,row=3)
window.mainloop()