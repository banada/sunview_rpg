import sys, pygame
pygame.init()

wall = pygame.image.load("./lib/wall.png")
enemy = pygame.image.load("./lib/redtri.png")
air = pygame.image.load("./lib/blank.png")
water = pygame.image.load("./lib/blue.png")

testgrid = [[wall,wall,wall,water,wall,wall,wall,wall],
		    [wall,air ,wall,water,wall,wall,wall,wall],
		    [wall,air ,air ,water,wall ,wall,wall,wall],
		    [wall,air ,wall,water,air ,enemy ,air ,wall],
		    [wall,air ,wall,water,enemy ,air ,air ,wall],
		    [wall,air ,wall,water,air ,air ,enemy ,wall],
		    [wall,air ,wall,water,air ,air ,air ,wall],
		    [wall,air ,air ,air ,air ,wall,wall,wall],
		    [wall,wall,wall,water,wall,wall,wall,wall],
		    [wall,wall,wall,water,wall,wall,wall,wall]]




gridsize = (10, 8)
cellsize = (60, 60)

size = width, height = gridsize[0]*cellsize[0], gridsize[1]*cellsize[1]

screen = pygame.display.set_mode(size)

wall = pygame.image.load("./lib/wall.png")
wallrect = wall.get_rect()

grid = [[0 for x in xrange(gridsize[1])] for x in xrange(gridsize[0])] 

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill((0,0,0))

	## update grid objects in grid
	for x in xrange(gridsize[0]):
		for y in xrange(gridsize[1]):
			grid[x][y] = testgrid[x][y]

	## render new object set
	for x in xrange(gridsize[0]):
		for y in xrange(gridsize[1]):
			screen.blit(grid[x][y], (x*cellsize[0], y*cellsize[1]))

	## update frame
	pygame.display.flip()
