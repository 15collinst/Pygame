import pygame
import button

#create display window
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

#pygame config
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Periodic Table')

#position of the table
PERIODIC_TABLE_X = (SCREEN_WIDTH - 1152) / 2 #centers the periodic table - 1151 = width of periodic table
PERIODIC_TABLE_Y = (SCREEN_HEIGHT - 500) #520 = height of periodic table

#coordinates of table
TABLE = [[1,18],
[1,2,13,14,15,16,17,18],
[1,2,13,14,15,16,17,18],
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
[1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
[1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]]

#load element images, note: range = number of elements
E = 88
images = []

for i in range(E):
	i = str(i+1)
	temp = '1' #I havent made the images yet
	images.append(pygame.image.load('images/'+temp+'.png').convert_alpha())

#create element instances, positioning elements
elements = []
p = 0
row = 0

for r in TABLE:
	row = row + 1
	for c in r:
	   x = PERIODIC_TABLE_X + ((c - 1) * 64)
	   y = PERIODIC_TABLE_Y + ((row - 1) * 64)
	   elements.append(button.Button(x, y, images[p]))
	   p = p + 1

#game loop
run = True
while run:

	#nice blue background
	screen.fill((154, 199, 145))

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