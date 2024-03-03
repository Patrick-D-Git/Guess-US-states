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
guessed_state_list = []

while len(guessed_state_list) < len(state_list):

    answer_state = screen.textinput(title=f"{len(guessed_state_list)}/{len(state_list)} Guessed State",
                                    prompt="What's another state name?").title()

    if answer_state in state_list and answer_state not in guessed_state_list:

        s = turtle.Turtle()
        s.hideturtle()
        s.penup()
        state_data = data[data.state == answer_state]
        s.goto(int(state_data.x), int(state_data.y))
        s.write(f"{answer_state}", align="center")
        guessed_state_list.append(answer_state)

screen.exitonclick()
