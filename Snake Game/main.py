from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

DELAY_TIME = 0
is_game_on = True

sc = Screen()
sc.setup(width=700, height=700)
sc.bgcolor("black")
sc.title("snake game")
sc.tracer(0)

game_mode = sc.textinput(title="user choice", prompt="choose the difficulty (easy / medium / hard)?")
if game_mode.lower() == "easy":
	DELAY_TIME = 0.4
elif game_mode.lower() == "medium":
	DELAY_TIME = 0.2
elif game_mode.lower() == "hard":
	DELAY_TIME = 0.1

snake = Snake()
food = Food()
score = Score()

if game_mode not in ["easy", "medium", "hard"]:
	print(f"you have chosen none of the option. you lost.")
	score.game_over()
	is_game_on = False

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")
	

while is_game_on:
	
	sc.update( )
	time.sleep(DELAY_TIME)
	snake.move()
	
	while snake.head.distance(food) < 15:
		food.refresh()
		snake.increase_size(-40)
		score.increase_score()
		
	if snake.head.xcor() > 320 or snake.head.xcor() < -320 or snake.head.ycor() > 320 or snake.head.ycor() < -320:
		score.reset()
		snake.reset()
		
	for seg in snake.segments[1:]:
		if snake.head.distance(seg) < 5:
			score.reset()

sc.exitonclick()
