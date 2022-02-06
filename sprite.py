import pygame
import math

from pygame.display import update

class Sprite():
    def __init__(self, atomic_number):
        self.elements = ["H", "He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar"]
        self.atomic_number = atomic_number
        self.font = pygame.font.Font("assets/sprites/Roboto-Regular.ttf", 32)
        self.electrons = []
        self.angle = 0
        self.rotate_speed = 1

    def draw(self, screen, X ,Y):
        img = self.font.render(self.elements[self.atomic_number -1], True, (255,255,255))
        sprite_centre_x = X - img.get_width() / 2
        sprite_centre_y = Y - img.get_height() / 2
        screen.blit(img, (sprite_centre_x, sprite_centre_y))

        for i in range(self.atomic_number):
            self.electrons.append(Electron())

        for i in range(self.atomic_number):
            rotation = i * (360 / self.atomic_number)
            self.electrons[i].draw(screen, self.angle+rotation, X, Y)

        self.angle += self.rotate_speed

        

class Electron():
    def get_position(self, X, Y, angle):
        sine_of_orbit_degree = math.sin(angle * 0.0174532925)
        x_coordinate = X + (sine_of_orbit_degree * self.ORBIT_RADIUS)

        cosine_of_orbit_degree = math.cos(angle * 0.0174532925)
        y_coordinate = Y + (cosine_of_orbit_degree * self.ORBIT_RADIUS)

        return [x_coordinate, y_coordinate]

    def draw(self,screen, angle, X, Y):
        orbit_pos = self.get_position(X, Y, angle)
        pygame.draw.circle(screen, (255,255,255), orbit_pos, self.ELECTRON_SIZE, 0)
