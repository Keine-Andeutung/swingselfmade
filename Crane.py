# provides the Crane class. The Crane always holds a Ball and has a position (int, 0 to 7).

from Balls import *
from pygame import Rect, Surface
from Constants import cranearea_ballcoord, cranearea_x_perCol, ballsize

class Crane:
	"""Information about the Crane. Has x (int, 0 <= x <= 7) and current_Ball (Ball).
	Also holds a local var surf, surface to draw on, returned when draw() is called on it.
	Constructor expects size of that surface."""
	
	def __init__(self, size):
		self.x = 0
		self.current_Ball = generate_starting_Ball()
		self.size = size
		self.surf = Surface(size)
		self.changed = True # True if redraw needed. If the Crane changed since the last tick.
		
	def draw(self):
		"""draws the Crane and its current_Ball to surface at position, returns surface"""
		self.surf.fill((127,127,127))
		
		
		xcoord = cranearea_ballcoord[0] + self.x*cranearea_x_perCol
		#print("crane xcoord: ",xcoord)
		# draw Ball, then an ellipse on top of it
		self.current_Ball.draw(self.surf, (xcoord, cranearea_ballcoord[1]))
		
		pixelpos_rect = Rect((xcoord,cranearea_ballcoord[1]), ballsize)
		pygame.draw.ellipse(self.surf, (0,0,0), pixelpos_rect, width=3)
		
		return self.surf
		