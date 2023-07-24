import turtle
from turtle import *
from random import choice, randint

x = -230
y = 230
color_list = [(105, 105, 105), (0, 0, 128), (0, 191, 255), (0, 255, 255), (127, 255, 212), (46, 139, 87), (205, 133, 63),
              (139, 69, 19), (255, 215, 0), (128, 0, 0), (138, 43, 226), (75, 0, 130), (173, 255, 47), (255, 20, 147), (0, 0, 0)]

mack = Turtle()
sc = Screen()

turtle.colormode(255)

mack.speed(0)
mack.hideturtle()
mack.penup()
mack.goto(x, y)
mack.pendown()

for row in range(10):
	for col in range(10):
		mack.dot(20, choice(color_list))
		mack.penup()
		mack.fd(50)
	y = y - 50
	mack.goto(x, y)
	mack.pendown()

sc.exitonclick()
