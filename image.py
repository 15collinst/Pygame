import pygame
import button

class Static_Image(button.Button):
	def __init__(self, x, y, image, scale):
		super().__init__(x, y, image, scale)
	
	def draw(self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))

	


