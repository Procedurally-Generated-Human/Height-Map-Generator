import numpy as np
from PIL import Image
from matplotlib import cm
from functions import nest_list, world_info

class World(object):
	""" World Object that creates and changes map """
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.world_map = np.zeros([height, width])
		self.states = []


	def water_to_land(self, x, y):
		self.world_map[x,y] = 1.0


	def show(self):
		im = Image.fromarray(np.uint8(cm.gist_earth(self.world_map)*255))
		im.show()


	def save(self, file_name):
		im = Image.fromarray(np.uint8(cm.gist_earth(self.world_map)*255))
		im.save('{}.png'.format(file_name))


	def smoothen_land(self):
		info = nest_list(world_info(self.world_map),self.height,self.width)

		for row in range(self.height):
			for col in range(self.width):
				if 4 <= info[row][col]['ones_around'] >= 8  :
					info[row][col]['change'] = 1
				if 4 <= 8-(info[row][col]['ones_around']) >= 8  :
					info[row][col]['change'] = 0 
		for row in range(self.height):
			for col in range(self.width):
				self.world_map[row][col] = info[row][col]['change']


		