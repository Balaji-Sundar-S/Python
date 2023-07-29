from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

paddle_position = [(420, 0), (-420, 0)]
turtle_speed = 0

screen = Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)

r_paddle = Paddle(paddle_position[0], 4, 1)
l_paddle = Paddle(paddle_position[1], 4, 1)
x = 0
y = -300
for i in range(30):
	pad1 = Paddle((x, y), 1, 0.3)
	y += 30
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "a")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
	time.sleep(0.01)
	screen.update()
	
	new_x = ball.xcor() + 1
	new_y = ball.ycor() + 1
	ball.move()
	
	if ball.ycor() > 330 or ball.ycor() < -330:
		ball.bounce_y()
		
	if ball.distance(r_paddle) < 60 and ball.xcor() > 400 or ball.distance(l_paddle) < 60 and ball.xcor() < -400:
		ball.bounce_x()
		ball.turtle_speed += 1
		
	if ball.xcor() > 440:
		ball.reset_position()
		score.l_point()
		
	if ball.xcor() < -440:
		ball.reset_position()
		score.r_point()

screen.exitonclick()
