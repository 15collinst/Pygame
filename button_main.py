import pygame
import button

#create display window
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

#Position of the table
PERIODIC_TABLE_X = 100
PERIODIC_TABLE_Y = 100


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

images = []

#load element images, note: range = number of elements
for i in range(1):
	i = str(i+1)
	temp = 1 #I havent made the images yet
	images.append(pygame.image.load('images/'+temp+'.png').convert_alpha())

x = PERIODIC_TABLE_X
y = PERIODIC_TABLE_Y

#create button instances, positioning elements

elements = []

for i in range(1):
    x = x + 65
    elements.append(button.Button(x, y, images[i]))

#game loop
run = True
while run:

	screen.fill((202, 228, 241)) #nice blue colour

	i = 0

	if elements[0].draw(screen):
		print('Click')

	#if elements[7].draw(screen):
	#	print('Click 2')

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()

