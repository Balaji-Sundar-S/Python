from turtle import Turtle


class Ball(Turtle):
	
	def __init__(self):
		super().__init__()
		self.turtle_speed = 0
		self.shape("circle")
		self.penup()
		self.color("white")
		self.shapesize(stretch_wid=1, stretch_len=1)
		self.goto(0, 0)
		self.x_move = 2.5
		self.y_move = 2.5
		
	def move(self):
		self.speed(self.turtle_speed)
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)
		
	def bounce_y(self):
		self.y_move *= -1
		
	def bounce_x(self):
		self.x_move *= -1
		
	def reset_position(self):
		self.home()
		self.bounce_x()
	
