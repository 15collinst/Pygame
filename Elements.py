import pygame
import button

#Element Class
class Element():
    def __init__(self):
        self.image = pygame.image.load('images/1.png').convert_alpha()
        self.button = button.Button(102, 399, self.image, 0.64)


Elements = []
for e in range(16):
    Elements.append(Element())

print(Elements)
    
