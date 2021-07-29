import colorgram
import turtle
import random

colors = colorgram.extract('hirst.jpg', 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

turtle.colormode(255)
t = turtle.Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
dots = 100
for ct in range(1, dots+1):
    t.dot(20, random.choice(rgb_colors))
    t.forward(50)

    if ct % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen = turtle.Screen()

screen.exitonclick()
