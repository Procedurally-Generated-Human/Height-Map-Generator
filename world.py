import numpy as np
from PIL import Image
from matplotlib import cm
from functions import nest_list, world_info

class World(object):
	""" World Object that creates and changes map """
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.elevation_map = np.zeros([height, width])


	def increase_elevation(self, x, y):
		self.elevation_map[x,y] = self.elevation_map[x,y] + 0.01


	def show_elevation_map(self):
		im = Image.fromarray(np.uint8(cm.gist_earth(self.elevation_map)*255))
		im.show()


	def smoothen_land(self):
		info = nest_list(world_info(self.elevation_map),self.height,self.width)
		for row in range(self.height):
			for col in range(self.width):
				self.elevation_map[row][col] = info[row][col]['change']

