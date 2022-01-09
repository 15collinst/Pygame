import math
import pygame

pygame.init()

bg = (255, 255, 255)
orbit_col = (0, 0, 0)

size = [1000, 1000]
screen = pygame.display.set_mode(size)
screen.fill(bg)
pygame.display.set_caption("Orbits")

run = True

clock = pygame.time.Clock()

ORBIT_RADIUS = 100
ELECTRON_SIZE = 5
ROTATION_SPEED = 1
ELECTRONS = []

number_of_electrons = 0

class Electron():
    def __init__(self):
        self.angle = 0
        self.reactivity = 0

    def draw(self):
        mx,my = pygame.mouse.get_pos()
        orbit_pos = [self.get_x(mx), self.get_y(my)]
        pygame.draw.circle(screen, orbit_col, orbit_pos, ELECTRON_SIZE, 0)

        self.angle += ROTATION_SPEED
    
    def get_x(self, mx):
        sine_of_orbit_degree = math.sin(self.angle * 0.0174532925)
        return mx + (sine_of_orbit_degree * ORBIT_RADIUS)

    def get_y(self, my):
        cosine_of_orbit_degree = math.cos(self.angle * 0.0174532925)
        return my + (cosine_of_orbit_degree * ORBIT_RADIUS)
    
    def get_angle(self, number_of_electrons):
        mx,my = pygame.mouse.get_pos()
        closest_distance = ORBIT_RADIUS * 2
        for i in range(number_of_electrons):
            x1 = self.get_x(mx)
            y1 = self.get_y(my)
            y2 = ELECTRONS[i].get_x()
            x2 = ELECTRONS[i].get_y()
            distance_to_neighbour = math.sqrt( ((x2 - x1) ** 2) + ((y2 - y1) ** 2))
            if distance_to_neighbour < closest_distance:
                closest_distance = distance_to_neighbour
        


ELECTRONS.append(Electron())

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ELECTRONS.append(Electron())

    screen.fill(bg)

    for i in range(len(ELECTRONS) - 1):
        ELECTRONS[i].draw()

    pygame.display.update()

    clock.tick(120)


pygame.quit
print(len(ELECTRONS))