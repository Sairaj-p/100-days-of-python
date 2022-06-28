import turtle
import pandas
screen = turtle.Screen()
mod = turtle.Turtle()
mod.hideturtle()
mod.penup()
screen.title("Indian States Game")
img = r"E:\100-days-of-python\Day_25\India_Map.gif"
screen.addshape(img)
screen.setup(600,600) 
turtle.shape(img)
data = pandas.read_csv(r"E:\100-days-of-python\Day_25\States_Data.csv")
state_names = data.state.to_list()
gussed_states =[]
while len(gussed_states)<28:
    answer = screen.textinput(title=f"Guess state no. {len(gussed_states)+1}",prompt="Enter the state you want to guess").title()

    if answer in state_names and answer not in gussed_states:
        cor = data[data.state==answer]
        mod.goto(int(cor.x),int(cor.y))
        mod.write(answer)
        gussed_states.append(answer)


turtle.mainloop()