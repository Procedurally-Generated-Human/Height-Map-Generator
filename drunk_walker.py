import random

class DrunkWalker:
	""" Creates a drunk walker and moves it """
	def __init__(self, start_x, start_y):
		self.start_x = start_x
		self.start_y = start_y
		self.x = start_x
		self.y = start_y
		self.directions = ((-1,0),(1,0),(0,1),(0,-1))


	def drunk_step(self, world):
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


	def drunk_walk(self, world, number_of_steps):
		for step in range(0, number_of_steps):
			self.drunk_step(world)


	def move_to_start(self):
		self.x = self.start_x
		self.y = self.start_y