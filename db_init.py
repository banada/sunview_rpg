import json

#Players and Enemies
class character:
    def __init__(self, name, x, y, speed, is_player=0):
        self.name = name
        self.x = x
        self.y = y
        self.speed = speed
        self.is_player = is_player
        print("Character "+str(self.name)+" created: (" \
               +str(self.x)+","+str(self.y)+"), "+str(self.speed)+" speed")
    
    #Change character position/stats - all args optional
    def update(self, x_new=-1, y_new=-1, speed_new=-1):
        if x_new >= 0:
            self.x = x_new
        if y_new >= 0:
            self.y = y_new
        if speed_new >= 0:
            self.speed = speed_new
        print("Updated character "+str(self.name)+": (" \
              +str(self.x)+","+str(self.y)+"), "+str(self.speed)+" speed")

#Points on the grid
class terrain:
    def __init__(self, x, y, ttype):
        self.x = x
        self.y = y
        self.ttype = ttype
        print("Terrain point created at: (" \
               +str(self.x)+","+str(self.y)+"), type: "+str(self.ttype))
    
    def update(self, ttype_new):
        self.ttype = ttype_new
        print("Terrain point (" \
               +str(self.x)+","+str(self.y)+"), is now type: "+str(self.ttype))
    
#Map: 2D set of terrain points
def create_map(x_dim, y_dim):
    map = []
    for i in range(0,x_dim):
        x = []
        for ii in range(0,y_dim):
            x.append(terrain(i, ii, "grass"))
        map.append(x)
    print map

#Testing
ptf = character("Perezoso the Folivore", 0, 0, 1)
ptf.update(1,1,0)

t1 = terrain(0,0,"wall")
t1.update("door")

create_map(5,5)
