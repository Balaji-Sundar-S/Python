from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
	
	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]
		
	def create_snake(self):
		
		for pos in POSITION:
			new_turtle = Turtle(shape="square")
			new_turtle.color("white")
			new_turtle.shapesize(stretch_len=1, stretch_wid=1, outline=None)
			new_turtle.penup( )
			new_turtle.goto(pos)
			self.segments.append(new_turtle)
			
	def reset(self):
		for seg in self.segments:
			seg.goto(1000, 1000)
		self.segments.clear()
		self.create_snake()
		self.head = self.segments[0]
			
	def move(self):
		for seg in range(len(self.segments)-1, 0, -1):
			new_x = self.segments[ seg-1 ].xcor( )
			new_y = self.segments[ seg-1 ].ycor( )
			self.segments[ seg ].goto(new_x, new_y)
		self.head.fd(DISTANCE)
		
	def up(self):
		if int(self.head.heading()) != DOWN:
			self.head.setheading(UP)
		
	def down(self):
		if int(self.head.heading( )) != UP:
			self.head.setheading(DOWN)
		
	def left(self):
		if int(self.head.heading( )) != RIGHT:
			self.head.setheading(LEFT)
		
	def right(self):
		if int(self.head.heading( )) != LEFT:
			self.head.setheading(RIGHT)
			
	def increase_size(self, x):
		new_turtle = Turtle(shape="square")
		new_turtle.color("white")
		new_turtle.shapesize(stretch_len=1, stretch_wid=1, outline=None)
		new_turtle.penup()
		x += -20
		new_turtle.goto(x, 0)
		self.segments.append(new_turtle)
	