import os, sys, pygame
from db_init import *
import glob
pygame.init()

def loadImageDict():
	global imgDict
	imgDict = {}
	for file in glob.glob("./Client/lib/*.png"):
		temp = pygame.image.load(file).convert()
		temp.set_colorkey((255,255,255))
		imgDict[os.path.basename(file)[:-4]] = temp
	print imgDict

class battlemap:
	def __init__(self, xsize, ysize):
		self.gridsize = (10, 8)
		self.cellsize = (60, 60)
		self.size = width, height = self.gridsize[0]*self.cellsize[0], self.gridsize[1]*self.cellsize[1]
		self.screen = pygame.display.set_mode(self.size)
		loadImageDict()
		self.grid = [[0 for x in xrange(self.gridsize[1])] for x in xrange(self.gridsize[0])] 
		self.testgrid = [[0 for x in xrange(self.gridsize[1])] for x in xrange(self.gridsize[0])] 
		self.charlist = []

		self.create_testgrid()

	def create_testgrid(self):
		## update grid objects in grid
		for x in xrange(self.gridsize[0]):
			for y in xrange(self.gridsize[1]):
				if (y+x)%3 == 0:
					self.testgrid[x][y] = terrain(x,y,'water')
				elif (y+x)%3 == 1:
					self.testgrid[x][y] = terrain(x,y,'grass')
				elif (y+x)%3 == 2:
					self.testgrid[x][y] = terrain(x,y,'wall')

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		self.screen.fill((0,0,0))

		## update grid objects in grid
		for x in xrange(self.gridsize[0]):
			for y in xrange(self.gridsize[1]):
				self.grid[x][y] = self.testgrid[x][y]

		## render new object set
		for x in xrange(self.gridsize[0]):
			for y in xrange(self.gridsize[1]):
				self.screen.blit(imgDict[self.grid[x][y].ttype], (x*self.cellsize[0], y*self.cellsize[1]))

		for x in xrange(len(self.charlist)):
			self.screen.blit(imgDict[self.charlist[x].img])

		## update frame
		pygame.display.flip()


bmap = battlemap(10,8)
while(1):
	bmap.update()