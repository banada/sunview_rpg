import json

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
    def set_character(self, x_new=-1, y_new=-1, speed_new=-1):
        if x_new > 0:
            self.x = x_new
        if y_new > 0:
            self.y = y_new
        if speed_new > 0:
            self.speed = speed_new
        print("Updated character "+str(self.name)+": (" \
              +str(self.x)+","+str(self.y)+"), "+str(self.speed)+" speed")
ptf = character("Perezoso the Folivore", 0, 0, 1)
ptf.set_character(1,1,0)
