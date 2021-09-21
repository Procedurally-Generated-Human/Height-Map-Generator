from drunk_walker import DrunkWalker
from world import World


pandora = World(height = 1000, width = 1000)

bob = DrunkWalker(start_x = 500, start_y = 500)

for e in range(20):
	bob.drunk_walk(pandora, 100000)
	bob.move_to_start()
	
pandora.show()
for e in range(10):
	pandora.smoothen_land()

pandora.show()



