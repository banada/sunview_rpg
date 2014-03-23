import os, sys, pygame
from classes import *
import msvcrt as m
import glob
from helper import *
from ui import *
import sgc
import socket
from sgc.locals import *
from pygame.locals import *

pygame.display.init()
pygame.font.init()

socket.accept()

def loadImageDict():
	global imgDict
	imgDict = {}
	for file in glob.glob("./Client/lib/*.png"):
		temp = pygame.image.load(file).convert()
		temp.set_colorkey((255,255,255))
		imgDict[os.path.basename(file)[:-4]] = temp

class battlemap:
	def __init__(self, xsize, ysize, isdm):
		self.gridsize = (xsize, ysize)
		self.cellsize = (30, 30)
		if isdm:
			self.size = width, height = self.gridsize[0]*self.cellsize[0]+ 200, self.gridsize[1]*self.cellsize[1]
		else:
			self.size = width, height = self.gridsize[0]*self.cellsize[0], self.gridsize[1]*self.cellsize[1]
		self.screen = sgc.surface.Screen(self.size)
		loadImageDict()
		self.grid = [[0 for x in xrange(self.gridsize[1])] for x in xrange(self.gridsize[0])] 
		self.testgrid = [[0 for x in xrange(self.gridsize[1])] for x in xrange(self.gridsize[0])] 
		self.charlist = []
		self.testcharlist = []

		if isdm:	
			self.rad = radio_set("dmSelect",["wall","door","enemy","player"], (self.size[0]-150, 100))
			for rad in self.rad.radio_buttons:
				rad.add(0)
			

		self.create_inigrid()

	def create_inigrid(self):
		## update grid objects in grid
		for x in xrange(self.gridsize[0]):
			for y in xrange(self.gridsize[1]):
				if (y*x)%3 == 0:
					self.grid[x][y] = terrain(x,y,'water')
				elif (y*x)%3 == 1:
					self.grid[x][y] = terrain(x,y,'door')
				elif (y*x)%3 == 2:
					self.grid[x][y] = terrain(x,y,'wall')
 				self.grid[x][y].post()
 				print "added cell " + str(x) +"_"+ str(y)

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		self.screen.fill((150,150,150))

		## update grid objects in grid
		for x in xrange(self.gridsize[0]):
			for y in xrange(self.gridsize[1]):
				self.grid[x][y].get()



		## render new object set
		for x in xrange(self.gridsize[0]):
			for y in xrange(self.gridsize[1]):
				self.screen.blit(imgDict[self.grid[x][y].ttype], (x*self.cellsize[0], y*self.cellsize[1]))

		## GET FULL CHARLIST
		self.charlist = self.testcharlist

		for x in xrange(len(self.charlist)):
			self.screen.blit(imgDict[self.charlist[x].ctype],(self.charlist[x].x*self.cellsize[0],self.charlist[x].y*self.cellsize[1]))


	def movecurchar(self, key):
		direction = key
		if direction is 113:
			if self.charlist[0].x-1 >= 0 and self.charlist[0].y-1 >= 0:
				self.testcharlist[0].update(self.charlist[0].x-1,self.charlist[0].y-1)
		elif direction is 119:
			if self.charlist[0].y-1 >= 0:
				self.testcharlist[0].update(self.charlist[0].x,self.charlist[0].y-1)
		elif direction is 101:
			if self.charlist[0].x+1 < self.gridsize[0] and self.charlist[0].y-1 >= 0:
				self.testcharlist[0].update(self.charlist[0].x+1,self.charlist[0].y-1)
		elif direction is 97:
			if self.charlist[0].x-1 >= 0:
				self.testcharlist[0].update(self.charlist[0].x-1,self.charlist[0].y)
		elif direction is 100:
			if self.charlist[0].x+1 < self.gridsize[0]:
				self.testcharlist[0].update(self.charlist[0].x+1,self.charlist[0].y)
		elif direction is 122:
			if self.charlist[0].x-1 >= 0 and self.charlist[0].y+1 < self.gridsize[1]:
				self.testcharlist[0].update(self.charlist[0].x-1,self.charlist[0].y+1)
		elif direction is 120:
			if self.charlist[0].y+1 < self.gridsize[1]:
				self.testcharlist[0].update(self.charlist[0].x,self.charlist[0].y+1)
		elif direction is 99:
			if self.charlist[0].x+1 < self.gridsize[0] and self.charlist[0].y+1 < self.gridsize[1]:
				self.testcharlist[0].update(self.charlist[0].x+1,self.charlist[0].y+1)

	def endturn(self):
		oldchar = self.charlist.pop(0)
		self.charlist.append(oldchar)

def main():
	clock = pygame.time.Clock()
	bmap = battlemap(5,5,1)
	while(1):
		time = clock.tick(30)
		for event in pygame.event.get():
			print event
			sgc.event(event)
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:			
				return
			elif event.type == pygame.KEYDOWN and event.key == 13:#enter	
				bmap.endturn()
			elif event.type == pygame.KEYDOWN:
				bmap.movecurchar(event.key)
		bmap.update()
		sgc.update(time)
		## update frame
		pygame.display.flip()


main()