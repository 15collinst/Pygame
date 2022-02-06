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

class Element():
    def __new__(cls, atomic_number):
        for i in range(atomic_number):
            ELECTRONS.append(Electron())
        return super(Element, cls).__new__(cls)
        
    def __init__(element, atomic_number):
        element.atomic_number = atomic_number
        element.electrons = []

    def draw(element, screen, mx ,my):
        elements = ["H", "He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar"]
        symbol = elements[element.atomic_number -1]
        font = pygame.font.Font("assets/sprites/Roboto-Regular.ttf", 32)
        img = font.render(symbol, True, (0,0,0))
        sprite_centre_x = mx - img.get_width() / 2
        sprite_centre_y = my - img.get_height() / 2  
        screen.blit(img, (sprite_centre_x, sprite_centre_y))
        

test_element = Element(2)

while run:
    mx,my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     ELECTRONS.append(Electron())

    screen.fill(bg)

    test_element.draw(screen, mx ,my)

    for i in range(len(ELECTRONS)):
        rotation = i * (360 / len(ELECTRONS))
        ELECTRONS[i].draw(angle+rotation)

    angle += ROTATION_SPEED

    pygame.display.update()

    clock.tick(120)

pygame.quit