import math
import pygame

pygame.init()

bg = (255, 255, 255)
orbit_col = (0, 0, 0)
RED = (255,0,0)

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

class Electron():
    def __init__(self):
        self.angle = 0
        self.reactivity = 0

    def get_position(self, mx, my):
        sine_of_orbit_degree = math.sin(self.angle * 0.0174532925)
        x_coordinate = mx + (sine_of_orbit_degree * ORBIT_RADIUS)

        cosine_of_orbit_degree = math.cos(self.angle * 0.0174532925)
        y_coordinate = my + (cosine_of_orbit_degree * ORBIT_RADIUS)

        return [x_coordinate, y_coordinate]

    def draw(self):
        orbit_pos = self.get_position(mx, my)
        pygame.draw.circle(screen, orbit_col, orbit_pos, ELECTRON_SIZE, 0)

        self.angle += ROTATION_SPEED
    
    def get_angle(self):
        for i in range(len(ELECTRONS)):
            x1, y1 = self.get_position(mx,my)
            x2, y2 = ELECTRONS[i].get_position(mx,my)
            distance_to_neighbour = math.sqrt( ((x1 - x2) ** 2) + ((y1 - y2) ** 2) )
            pygame.draw.line(screen, RED, [x1, y1], [x2, y2], 5)

        
        


ELECTRONS.append(Electron())

while run:
    mx,my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ELECTRONS.append(Electron())

    screen.fill(bg)

    for i in range(len(ELECTRONS)):
        # print(ELECTRONS[i].get_position(mx, my))
        ELECTRONS[i].draw()
        if len(ELECTRONS) == 1:
            pass
        else:
            ELECTRONS[i].get_angle()

    

    

    pygame.display.update()

    clock.tick(120)


pygame.quit