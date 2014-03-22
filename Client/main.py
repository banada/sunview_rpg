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


class battlemap:
	def __init__(self, xsize, ysize):
		self.gridsize = (10, 8)
		self.cellsize = (60, 60)
		self.size = width, height = self.gridsize[0]*self.cellsize[0], self.gridsize[1]*self.cellsize[1]
		self.screen = pygame.display.set_mode(self.size)
		self.grid = [[0 for x in xrange(self.gridsize[1])] for x in xrange(self.gridsize[0])] 

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		self.screen.fill((0,0,0))

		## update grid objects in grid
		for x in xrange(self.gridsize[0]):
			for y in xrange(self.gridsize[1]):
				self.grid[x][y] = testgrid[x][y]

		## render new object set
		for x in xrange(self.gridsize[0]):
			for y in xrange(self.gridsize[1]):
				self.screen.blit(self.grid[x][y], (x*self.cellsize[0], y*self.cellsize[1]))

		## update frame
		pygame.display.flip()


bmap = battlemap(10,8)
while(1):
	bmap.update()