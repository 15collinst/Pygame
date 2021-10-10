import pygame
import button

#create display window
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

#position of the table
PERIODIC_TABLE_X = 100
PERIODIC_TABLE_Y = 100

#number of elements
e = 7


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

images = []

#load element images, note: range = number of elements
for i in range(e):
	i = str(i+1)
	temp = '1' #I havent made the images yet
	images.append(pygame.image.load('images/'+temp+'.png').convert_alpha())


#create element instances, positioning elements
elements = []

x = PERIODIC_TABLE_X
y = PERIODIC_TABLE_Y

for i in range(e):
    x = x + 65
    elements.append(button.Button(x, y, images[i]))

#game loop
run = True
while run:

	screen.fill((202, 228, 241)) #nice blue colour

	for i in range(e):
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

