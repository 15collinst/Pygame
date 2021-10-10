import pygame
import button

#create display window
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

#position of the table
PERIODIC_TABLE_X = (SCREEN_WIDTH - 1152) / 2 #centers the periodic table
PERIODIC_TABLE_Y = 0

#number of elements
E = 18

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Periodic Table')

images = []

#load element images, note: range = number of elements
for i in range(E):
	i = str(i+1)
	temp = '1' #I havent made the images yet
	images.append(pygame.image.load('images/'+temp+'.png').convert_alpha())


#create element instances, positioning elements
elements = []

x = PERIODIC_TABLE_X
y = PERIODIC_TABLE_Y

for i in range(E):
	elements.append(button.Button(x, y, images[i]))
	x = x + 65

#game loop
run = True
while run:

	#nice blue background
	screen.fill((202, 228, 241))

	#loops over all elements drawing them and checking if they have been clicked
	for i in range(E):
		if elements[i].draw(screen):
			i = str(i+1)
			print('Click ['+i+']')

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()

