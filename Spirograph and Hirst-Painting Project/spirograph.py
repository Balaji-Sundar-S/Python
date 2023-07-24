import turtle
from turtle import *
from random import choice, randint

mack = Turtle()
sc = Screen()
turtle.colormode(255)

mack.speed(0)
mack.color("red", "black")


def return_color():
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)
	random_color = (r, g, b)
	return random_color

size = 1


for _ in range(int(360/size)):
	mack.pencolor(return_color())
	mack.circle(100)
	mack.left(size)


sc.exitonclick()
