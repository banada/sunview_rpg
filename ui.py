import sgc
from sgc.locals import *

class radio_set:
	def __init__(self, name, options, pos):
		self.radio_buttons = []
		pos_incr = 0
		for opt in options:
			self.radio_buttons.append(sgc.Radio(label=opt, label_side='right', group=name, pos=(pos[0],pos[1]+30*pos_incr)))
			pos_incr = pos_incr+1