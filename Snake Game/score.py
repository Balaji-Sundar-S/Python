from turtle import Turtle


class Score(Turtle):
	
	def __init__(self):
		super().__init__()
		self.score = 0
		self.high_score = 0
		self.color("white")
		self.penup()
		self.goto(0, 320)
		self.hideturtle()
		self.update_score()
		
	def update_score(self):
		self.clear()
		with open("high_score.txt") as file:
			self.high_score = file.read()
		self.write(f"Score = {self.score} High Score : {self.high_score}", move=False, align="center", font=("Ariel", 16, "bold"))
		
	def reset(self):
		if self.score > int(self.high_score):
			self.high_score = self.score
			with open("high_score.txt", "w") as file:
				file.write(str(self.high_score))
		self.score = 0
		self.update_score()
		
	def increase_score( self ):
		self.score += 1
		self.clear()
		self.update_score()
		