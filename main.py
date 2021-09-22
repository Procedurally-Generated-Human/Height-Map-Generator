from drunk_walker import RandomWalker
from world import World
import random as rd

'''example of the creation of a simple world'''

# init
world_height = 1000
world_width  = 2000
center_x = int(world_height/2)
center_y = int(world_width/2)
rodinia = World(height = world_height, width = world_width)
walker = RandomWalker(start_x = center_x, start_y = center_y)

# draw big continent in the middle
for e in range(50):
	walker.biased_walk(rodinia, 80000, [0.2,0.2,0.5,0.5])
	walker.move_to_position(center_x, center_y)

# draw a few small islands
for e in range(6):
	walker.move_to_position(rd.randint(0,999), rd.randint(0,1999))
	walker.random_walk(rodinia, rd.randint(12000,15000))

# draw many very small islands
for e in range(25):
	walker.move_to_position(rd.randint(0,999), rd.randint(0,1999))
	walker.random_walk(rodinia, rd.randint(3000,10000))

# show un-smoothened map
rodinia.show()

# smoothen map using cellular automata
for e in range(20):
	rodinia.smoothen_land()

# show smoothed map
rodinia.show()

