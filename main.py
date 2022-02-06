import pygame
import setup
import sprite
import button

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

# game loop
run = True
spawn = False
mouse = False

while run:
	# get the positions of the mouse
	mx,my = pygame.mouse.get_pos()

	# blue background
	SCREEN.fill((34,61,92))

	# draw the static images
	KEY.draw(SCREEN)
	OTHER_ELEMENTS.draw(SCREEN)

	# loops over all elements drawing them and checking if they have been clicked
	for i in range(18):
		if elements[i].draw(SCREEN) and not spawn:
			element_number = i + 1
			spawn = True
			clicked = i + 1

	#creates a sprite which tracks the mouse when you hold down
	if spawn:
		sprite.spawn(SCREEN, mx, my,element_number)

	# event handler
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse = True
		if event.type == pygame.MOUSEBUTTONUP:
			# if player selects an element return element value
			if my < 369 and spawn:
				clicked = str(clicked)
				print('Element['+clicked+'] has been selected')
			spawn = False
			
		# quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()