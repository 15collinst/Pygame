import pygame
import element

class Static_Image(element.Button):
	def __init__(self, x, y, image, scale):
		super().__init__(x, y, image, scale)
	
	def draw(self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))

	


