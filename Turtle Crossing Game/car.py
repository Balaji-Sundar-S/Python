from turtle import Turtle
import random

car_colours = ["red", "black", "blue", "orange", "pink", "violet", "indigo", "brown"]


class Car():
	
	def __init__(self) :
		self.move_distance = 5
		self.cars = []
		
	def create_car( self ):
		random_chance = random.randint(1, 6)
		if random_chance == 1:
			new_car = Turtle()
			new_car.penup()
			new_car.shape("square")
			new_car.shapesize(stretch_wid=1, stretch_len=3)
			new_car.color(random.choice(car_colours))
			random_y = random.randint(-215, 230)
			new_car.goto(410, random_y)
			self.cars.append(new_car)
	
	def move(self):
		for car in self.cars:
			car.backward(self.move_distance)
			
