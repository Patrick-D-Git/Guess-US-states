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


def save_file(guessed_list):
    to_review_data = []

    for state in state_list:
        if state not in guessed_list:
            to_review_data.append(state)

    max_length = len(state_list)
    to_review_data_padded = to_review_data + [None] * (max_length - len(to_review_data))
    guessed_list_padded = guessed_list + [None] * (max_length - len(guessed_list))

    df = pd.DataFrame({"To Review": to_review_data_padded, "Guessed States": guessed_list_padded})
    df.to_csv("states_to_review.csv", index=False)


while len(guessed_state_list) < len(state_list):

    answer_state = screen.textinput(title=f"{len(guessed_state_list)}/{len(state_list)} Guessed State",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        save_file(guessed_state_list)
        break

    if answer_state in state_list and answer_state not in guessed_state_list:

        s = turtle.Turtle()
        s.hideturtle()
        s.penup()
        state_data = data[data.state == answer_state]
        s.goto(int(state_data.x), int(state_data.y))
        s.write(f"{answer_state}", align="center")
        guessed_state_list.append(answer_state)
