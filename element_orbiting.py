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

orbits = [[0]] # start angle

class Electron():
    angle = 0
    def __init__(self):
        self.angle = 0
        self.reactivity = 0

    def get_angle(self):
        return self.angle

    def get_reactivity(reactivity):
        return reactivity

    def draw():
        orbit_pos = [x_position, y_position]

        pygame.draw.circle(screen, orbit_col, orbit_pos, ELECTRON_SIZE, 0)

        orbit[0] += ROTATION_SPEED
    
    def return_x():
        sine_of_orbit_degree = math.sin(orbit[0] * 0.0174532925)
        return mx + (sine_of_orbit_degree * ORBIT_RADIUS)

    def return_y():
        cosine_of_orbit_degree = math.cos(orbit[0] * 0.0174532925)
        return my + (cosine_of_orbit_degree * ORBIT_RADIUS)
    
    def calculate_angle(number_of_electrons):
        max_distance = 360 / number_of_electrons
        distance_to_neighbours = math.sqrt( ((x1 - x2) ** 2) + ((y1 - y2) ** 2))


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill(bg)

    for orbit in orbits:
        mx,my = pygame.mouse.get_pos()
        
        Electron.draw()

    pygame.display.update()

    clock.tick(120)


pygame.quit