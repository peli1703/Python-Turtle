import turtle
import random
import time
import colorsys

t = turtle.Turtle()
s = turtle.Screen()

s.setup(width=1.0, height=1.0)
s.colormode(255)

# Giving screen a background colour

turtle.Screen().bgcolor("Black")

# setting colour of pen

t.pencolor('red')

# speed refers to the speed of the pen here, 0 is the max speed and 1 is minimum speed.
t.speed(0)

# This will help us to hide the cursor of the turtle.
t.hideturtle() 

# This determines the width of the pen.
t.pensize(4)

# This will create a rangoli design for our animation.
'''This function will create 10 circles,
and each time radius will be reduced to radius-4 '''


def draw(radius):
    for i in range(10):
        t.circle(radius)
        radius = radius-4


'''This function will call draw function 10 times
    and everytime the turtle will change its direction'''


def design():
    for i in range(10):
        draw(120)
        t.right(36)
    t.penup()


design()


time.sleep(2)
t.penup()

# And our program is ready!!! Let's run it and see the output
turtle.done()