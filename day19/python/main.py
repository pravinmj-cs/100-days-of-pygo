from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput(
    title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")

screen.exitonclick()
