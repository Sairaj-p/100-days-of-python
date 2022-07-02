#Password Manager

from tkinter import *
from tkinter import messagebox
import Day_5

def gen_password():
    password_input.delete(0,END)
    password =Day_5.get_password(5,4,2)
    password_input.insert(0,password)

def save_data():
    password = password_input.get()
    username= username_input.get()
    website =website_input.get()
    if len(password)==0 or len(username)==0 or len(website) ==0:
        messagebox.showinfo(title="Warning",message="Some Feilds are empty")
    else:
        correct =messagebox.askokcancel(title=website,message=f"These are details {username} for {website} password {password}\nDo you want to save the details ?")
        if correct:
            with open(file=r"Passwords.txt",mode="a") as file:
                file.write(f"{website} | {username} | {password}\n")
            password_input.delete(0,END)
            website_input.delete(0,END)


window = Tk()
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
image_ = PhotoImage(file=r"E:\New folder\Password Manager\logo.png")
canvas.create_image(100,100,image=image_)
canvas.grid(row=0,column=1)
label =Label(text="Website")
label.grid(row=1,column=0)
website_input = Entry(width=43)
website_input.focus()

website_input.grid(row=1,column=1,columnspan=2)
label_Username = Label(text="Email/Username")
label_Username.grid(row=2,column=0)
username_input = Entry(width=43)
username_input.insert(0,"sairaj@gmail.com")

username_input.grid(row=2,column=1,columnspan=2)
password_label=Label(text="Password")
password_label.grid(row=3,column=0)
password_input =Entry(width=25)

password_input.grid(row=3,column=1)
password_button = Button(text="Generate Password",command=gen_password)
password_button.grid(row=3,column=2)
add_button =Button(text="Add",width=43,command=save_data)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
