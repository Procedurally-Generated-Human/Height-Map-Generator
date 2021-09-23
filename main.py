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
for e in range(350):
	walker.biased_walk(rodinia, 100000, [0.2,0.2,0.5,0.5])
	walker.move_to_position(rd.randint(150,850), rd.randint(300,1700))


# show un-smoothened map
rodinia.show_elevation_map()



for e in range(30):
	rodinia.smoothen_land()
rodinia.show_elevation_map()
