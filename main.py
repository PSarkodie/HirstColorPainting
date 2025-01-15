from turtle import Turtle, Screen
from random import choice

"""Creates a GUI of a Hurt Color Painting using random rgb colors from a list of tuples"""
color_list = [(208, 158, 96), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]

def screen_configs(turtle_screen):
    screen.colormode(255)
    screen.setup(500, 500, 0, 0)
    screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

def paint(turtle):
    turtle.shape("circle")
    y_coordinate = 0
    for x in range(10):
        turtle.goto(0,y_coordinate)
        turtle.pendown()
        for y in range(10):
            turtle.color(choice(color_list))
            turtle.stamp()
            turtle.penup()
            if (turtle.xcor()+50 < screen.canvwidth):
                turtle.forward(50)
        turtle.penup()
        y_coordinate += (screen.canvheight/10)

screen = Screen()
screen_configs(screen)

turtle = Turtle()
paint(turtle)

screen.exitonclick()
