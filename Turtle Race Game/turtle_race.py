import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
sc = Screen()
sc.setup(width=700, height=600)
number_players = sc.numinput(title = "number of players", prompt="how many players")
player_colour = []
for _ in range(int(number_players)):
	colour = sc.textinput(title="colour", prompt=f"enter colour of player{_+1}")
	player_colour.append(colour)
colours = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_pos = [0, 35, -35, 70, -70, 105, -105]
all_turtle = []

for i in range(int(number_players)):
	new_turtle = Turtle(shape="turtle")
	new_turtle.speed(2)
	new_turtle.color(player_colour[i])
	new_turtle.penup()
	new_turtle.goto(-335, y_pos[i])
	all_turtle.append(new_turtle)
	
is_race_on = True
while is_race_on:
	for turtle in all_turtle:
		if turtle.xcor() > 320:
			for col in range(len(player_colour)):
				if player_colour[col] == turtle.pencolor():
					print(f"Turtle {turtle.pencolor()} : player{col+1} has won the match")
					is_race_on = False
			
		turtle.fd(random.randint(1, 5))

sc.exitonclick()
