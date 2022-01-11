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

angle = 0

class Electron():
    def __init__(self):
        self.angle = 0
        self.reactivity = 0

    def get_position(self, mx, my, angle):
        sine_of_orbit_degree = math.sin(angle * 0.0174532925)
        x_coordinate = mx + (sine_of_orbit_degree * ORBIT_RADIUS)

        cosine_of_orbit_degree = math.cos(angle * 0.0174532925)
        y_coordinate = my + (cosine_of_orbit_degree * ORBIT_RADIUS)

        return [x_coordinate, y_coordinate]

    def draw(self, angle):
        orbit_pos = self.get_position(mx, my, angle)
        pygame.draw.circle(screen, orbit_col, orbit_pos, ELECTRON_SIZE, 0)
    
    # def get_closest_electron(self,angle):

    #     closest_distance = ORBIT_RADIUS * 2 
    #     for i in range(len(ELECTRONS)):
    #         x1, y1 = self.get_position(mx,my,angle)
    #         x2, y2 = ELECTRONS[i].get_position(mx,my,angle)
    #         distance_to_neighbour = math.sqrt( ((x2 - x1) ** 2) + ((y2 - y1) ** 2) )

    #         if distance_to_neighbour < closest_distance:
    #             closest_distance = distance_to_neighbour
    #             closest_electron = ELECTRONS[i]

    #     pygame.draw.line(screen, RED, self.get_position(mx,my,angle), closest_electron.get_position(mx,my,angle), 5)

    #     R = ORBIT_RADIUS
    #     D = closest_distance
    #     angle_apart = math.degrees(2 * math.asin(D / (2 * R)))


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
        rotation = i * (360 / len(ELECTRONS))
        # print(ELECTRONS[i].get_position(mx, my))
        ELECTRONS[i].draw(angle+rotation)
        # if len(ELECTRONS) == 1:
        #     pass
        # else:
        #     ELECTRONS[i].get_closest_electron(angle)

    angle += ROTATION_SPEED

    pygame.display.update()

    clock.tick(120)

pygame.quit