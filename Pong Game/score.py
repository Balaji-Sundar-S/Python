from turtle import Turtle


class Score(Turtle):
	
	def __init__( self ):
		super( ).__init__( )
		self.color("white")
		self.penup()
		self.hideturtle()
		self.l_score = 0
		self.r_score = 0
		self.update()
	
	def update( self ):
		self.clear()
		self.goto(-150, 260)
		self.write(self.l_score, align="center", font=("ariel", 50, "normal"))
		self.goto(150, 260)
		self.write(self.r_score, align="center", font=("ariel", 50, "normal"))
	
	def l_point( self ):
		self.l_score += 1
		self.update()
		
	def r_point( self ):
		self.r_score += 1
		self.update()
