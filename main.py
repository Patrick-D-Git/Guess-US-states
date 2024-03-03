import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=800, height=600)

df = pd.read_csv("50_states.csv")
state_list = df["state"].tolist()

screen.exitonclick()
