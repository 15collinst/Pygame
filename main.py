import pygame
import setup
import sprite
import button
import math

pygame.init()

# create display window
SCREEN_HEIGHT = 1024
SCREEN_WIDTH = 1440

# pygame config
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Periodic Table')

# position of the table
PERIODIC_TABLE_X = 40
PERIODIC_TABLE_Y = 375

# position of the key
KEY_X = (SCREEN_WIDTH - (1086)) / 2
KEY_Y = SCREEN_HEIGHT - 40

# coordinates of table
TABLE = [[1,18],
[1,2,13,14,15,16,17,18],
[1,2,13,14,15,16,17,18]]

# creates instances of the images
images = []
setup.instance_imgs(images)

# create element instances, positions elements
elements = []
setup.instance_elements(PERIODIC_TABLE_X, PERIODIC_TABLE_Y, TABLE, images, elements)

# create key
KEY_IMG = pygame.image.load("assets/misc/Key.svg").convert_alpha()
KEY = button.Static_Image(KEY_X, KEY_Y, KEY_IMG, 1)

# create other elements
OTHER_ELEMENTS_IMG = pygame.image.load("assets/misc/Other_elements.svg").convert_alpha()
OTHER_ELEMENTS = button.Static_Image(36, 625, OTHER_ELEMENTS_IMG, 1)

orbit_col = (255, 255, 255)

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
        pygame.draw.circle(SCREEN, orbit_col, orbit_pos, ELECTRON_SIZE, 0)

class Element():
    def __init__(element, atomic_number):
        element.atomic_number = atomic_number

        num_of_electrons = atomic_number
        
        if atomic_number > 2:
            num_of_electrons = atomic_number - 2
        if atomic_number > 10:
            num_of_electrons = atomic_number - 10

        electrons = []
        for i in range(num_of_electrons):
            electrons.append(Electron())
        element.electrons = electrons
        

    def draw(element, screen, mx ,my):
        elements = ["H", "He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar"]
        symbol = elements[element.atomic_number -1]
        font = pygame.font.Font("assets/sprites/Roboto-Regular.ttf", 32)
        img = font.render(symbol, True, (255,255,255))
        sprite_centre_x = mx - img.get_width() / 2
        sprite_centre_y = my - img.get_height() / 2  
        screen.blit(img, (sprite_centre_x, sprite_centre_y))

        for i in range(len(element.electrons)):
            rotation = i * (360 / len(element.electrons))
            element.electrons[i].draw(angle+rotation)

# game loop
run = True
spawn = False
mouse = False

active_element = Element(1)

while run:
	# event handler
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse = True
		if event.type == pygame.MOUSEBUTTONUP:
			# if player selects an element return element value
			if my < 369 and spawn:
				clicked = str(clicked)
				active_element = sprite.Element(clicked)
			spawn = False
			
		# quit game
		if event.type == pygame.QUIT:
			run = False

	# get the positions of the mouse
	mx,my = pygame.mouse.get_pos()

	# blue background
	SCREEN.fill((34,61,92))

	# draw the static images
	KEY.draw(SCREEN)
	OTHER_ELEMENTS.draw(SCREEN)

	#creates a sprite which tracks the mouse when you hold down
	# if spawn:
	active_element.draw(SCREEN, mx ,my)
	
	#spin element
	angle += ROTATION_SPEED

	# loops over all elements drawing them and checking if they have been clicked
	for i in range(18):
		if elements[i].draw(SCREEN) and not spawn:
			element_number = i + 1
			spawn = True
			clicked = i + 1

	pygame.display.update()

pygame.quit()