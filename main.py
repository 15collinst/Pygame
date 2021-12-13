import pygame
import setup
import sprite
import button
import time

# create display window
SCREEN_HEIGHT = 1024
SCREEN_WIDTH = 1440

# pygame config
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Periodic Table')

# position of the table
PERIODIC_TABLE_X = 40
PERIODIC_TABLE_Y = 375

REACTION_CHAMBER_X = (SCREEN_WIDTH - (618)) /2

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

# create reaction chamber
reaction_chamber_img = pygame.image.load("assets/misc/Reaction_Chamber.svg").convert_alpha()
reaction_chamber = button.Reaction_Chamber(REACTION_CHAMBER_X, 25, reaction_chamber_img, 1)

# create key
KEY_IMG = pygame.image.load("assets/misc/Key.svg").convert_alpha()
KEY = button.Reaction_Chamber(KEY_X, KEY_Y, KEY_IMG, 1)

# create other elements
OTHER_ELEMENTS_IMG = pygame.image.load("assets/misc/Other_elements.svg").convert_alpha()
OTHER_ELEMENTS = button.Reaction_Chamber(36, 625, OTHER_ELEMENTS_IMG, 1)


collide = 1

# game loop
run = True
spawn = False
mouse = False
in_box = False

while run:
	mx,my = pygame.mouse.get_pos()

	# grey background
	SCREEN.fill((34,61,92))

	# if player selects an element return element value
	if reaction_chamber.hover(SCREEN) and spawn and not mouse:
		clicked = str(clicked)
		print('Element['+clicked+'] has been selected')
		spawn = False

	KEY.draw(SCREEN)
	OTHER_ELEMENTS.draw(SCREEN)


	# if player lets go of mouse get rid of sprite
	if not mouse:
		spawn = False

	# loops over all elements drawing them and checking if they have been clicked
	for i in range(18):
		if elements[i].draw(SCREEN) and not spawn:
			element_number = i + 1
			spawn = True
			clicked = i + 1

	#creates a sprite which tracks the mouse when you hold down
	if spawn:
		sprite.spawn(clicked, SCREEN, mx, my,element_number)

	# event handler
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse = True
		if event.type == pygame.MOUSEBUTTONUP:
			mouse = False
		# quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()