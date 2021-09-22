import random
from functions import biase

class RandomWalker:
	""" Creates a random walker and moves it """
	def __init__(self, start_x, start_y):
		self.x = start_x
		self.y = start_y
		self.directions = ((-1,0),(1,0),(0,1),(0,-1))


	def random_step(self, world):
		direction = random.choice(self.directions)
		self.x = self.x + direction[0]
		self.y = self.y + direction[1]
		if self.x == world.height:
			self.x += -1
		elif self.x == 0:
			self.x += 1
		if self.y == world.width:
			self.y += -1
		elif self.y == 0:
			self.y += 1
		world.water_to_land(self.x, self.y)


	def random_walk(self, world, number_of_steps):
		for step in range(0, number_of_steps):
			self.random_step(world)


	def biased_step(self, world, bias):
		biased_directions = biase(self.directions, bias)
		biased_direction = random.choice(biased_directions)
		self.x = self.x + biased_direction[0]
		self.y = self.y + biased_direction[1]
		if self.x == world.height:
			self.x += -1
		elif self.x == 0:
			self.x += 1
		if self.y == world.width:
			self.y += -1
		elif self.y == 0:
			self.y += 1
		world.water_to_land(self.x, self.y)


	def biased_walk(self, world, number_of_steps, bias):
		for step in range(0, number_of_steps):
			self.biased_step(world, bias)


	def move_to_position(self, x, y):
		self.x = x
		self.y = y
