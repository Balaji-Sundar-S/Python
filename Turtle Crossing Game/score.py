from turtle import Turtle


class Score(Turtle):
	
	def __init__(self):
		super().__init__()
		self.level = 1
		self.score_board(self.level)
		
	def level_up(self):
		self.level += 1
		self.score_board(self.level)
		
	def score_board(self, level):
		self.clear()
		self.penup()
		self.hideturtle()
		self.goto(-330, 250)
		self.write(f"Level : {level}", align="center", font=("cambria", 20, "normal"))
