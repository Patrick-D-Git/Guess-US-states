import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=800, height=600)

data = pd.read_csv("50_states.csv")
state_list = data.state.to_list()

answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?")

if answer_state in state_list:
    s = turtle.Turtle()
    s.hideturtle()
    s.penup()
    state_data = data[data.state == answer_state]
    s.goto(int(state_data.x), int(state_data.y))
    s.write(f"{answer_state}", align="center")

screen.exitonclick()
