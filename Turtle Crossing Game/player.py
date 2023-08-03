from turtle import Turtle


class Player(Turtle):
	
	def __init__(self):
		super().__init__()
		self.shape("turtle")
		self.penup()
		self.shapesize(stretch_wid=1.5, stretch_len=1.5)
		self.color("green")
		self.left(90)
		self.goto(0, -280)
		self.y_move = 20
		
	def move_up(self):
		y = self.ycor() + self.y_move
		self.goto(self.xcor(), y)
