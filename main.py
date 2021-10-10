import pygame
import setup
import sprite

# create display window
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

# pygame config
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Periodic Table')

# position of the table
PERIODIC_TABLE_X = (SCREEN_WIDTH - 1152) / 2 #centers the periodic table - 1151 = width of periodic table
PERIODIC_TABLE_Y = (SCREEN_HEIGHT - 500) #520 = height of periodic table

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

# game loop
run = True
spawn = False
while run:
	mx,my = pygame.mouse.get_pos()

	# nice green background
	screen.fill((154, 199, 145))

	# loops over all elements drawing them and checking if they have been clicked
	for i in range(88):
		if elements[i].draw(screen) and spawn == False:
			spawn = True
			clicked = i + 1
			print(clicked)

	#creates a sprite which tracks the mouse when you hold down
	if spawn:
		sprite.spawn(clicked, screen, mx, my)
		if event.type == pygame.MOUSEBUTTONUP:
			spawn = False

	# event handler
	for event in pygame.event.get():
		# quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()