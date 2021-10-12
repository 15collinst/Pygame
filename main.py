import pygame
import setup
import sprite
import button

# create display window
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

# pygame config
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Periodic Table')

# position of the table
PERIODIC_TABLE_X = (SCREEN_WIDTH - 1152) / 2 #centers the periodic table
PERIODIC_TABLE_Y = (SCREEN_HEIGHT - 500) 

REACTION_CHAMBER_X = (SCREEN_WIDTH - 400) / 2

# coordinates of table
TABLE = [[1,18],
[1,2,13,14,15,16,17,18],
[1,2,13,14,15,16,17,18],
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
[1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
[1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]]

# creates instances of the images
images = []
setup.instance_imgs(images)

# create element instances, positions elements
elements = []
setup.instance_elements(PERIODIC_TABLE_X, PERIODIC_TABLE_Y, TABLE, images, elements)

#create reaction chamber
reaction_chamber_img = pygame.image.load("images/reaction_chamber.png").convert_alpha()
reaction_chamber = button.Button(REACTION_CHAMBER_X, 30, reaction_chamber_img, 1)

collide = 1

# game loop
run = True
spawn = False
mouse = False
in_box = False

while run:
	mx,my = pygame.mouse.get_pos()

	# nice green background
	screen.fill((154, 199, 145))

	# if player selects an element return element value
	if reaction_chamber.hover(screen) and spawn and not mouse:
		print(clicked)
		spawn = False

	# loops over all elements drawing them and checking if they have been clicked
	for i in range(88):
		if elements[i].draw(screen) and not spawn:
			spawn = True
			clicked = i + 1

	#creates a sprite which tracks the mouse when you hold down
	if spawn:
		sprite.spawn(clicked, screen, mx, my)

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