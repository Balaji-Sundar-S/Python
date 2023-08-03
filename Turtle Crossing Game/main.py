from turtle import Screen
from player import Player
from car import Car
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car = Car()
score = Score()

screen.listen()
screen.onkey(player.move_up, "Up")

is_game_on = True
while is_game_on:
	time.sleep(0.05)
	screen.update()
	
	car.create_car()
	car.move()
	
	for box in car.cars:
		if box.distance(player) < 25:
			score.goto(0, 0)
			score.write("GAME OVER 😫", align="center", font=("cambria", 25, "bold"))
			is_game_on = False
			
	if player.ycor() > 270:
		score.level_up()
		player.goto(0, -280)
		car.move_distance += 5

screen.exitonclick()
