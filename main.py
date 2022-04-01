import pygame
import setup
import sprite
import image
import button
import math

pygame.init()
pygame.display.set_caption('Periodic Table')

# create display window
SCREEN_HEIGHT = 1024
SCREEN_WIDTH = 1440

# pygame config
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

# create key
KEY_IMG = pygame.image.load("assets/misc/Key.svg").convert_alpha()
KEY = image.Static_Image(KEY_X, KEY_Y, KEY_IMG, 1)

# create other elements
OTHER_ELEMENTS_IMG = pygame.image.load("assets/misc/Other_elements.svg").convert_alpha()
OTHER_ELEMENTS = image.Static_Image(36, 625, OTHER_ELEMENTS_IMG, 1)

# create refresh button
REFRESH_IMG = pygame.image.load("assets/misc/Refresh_Button.svg").convert_alpha()
REFRESH = button.Button((SCREEN_WIDTH / 2) - 61.5, 0, REFRESH_IMG, 1)

# creates instances of the images
IMAGES = []
setup.instance_imgs(IMAGES)

# create element instances, positions elements
ELEMENTS = []
setup.instance_elements(PERIODIC_TABLE_X, PERIODIC_TABLE_Y, TABLE, IMAGES, ELEMENTS)

# game loop
run = True
spawn = False
mouse = False
clock = pygame.time.Clock()

static_elements = []

def move_elements(mx, my, x, y, direction):
    dx = mx - x
    dy = my - y

    angle = math.atan2(dx,dy)

    #returns between 1 or -1 to adjust distance between
    mvx = math.sin(angle)  
    mvy = math.cos(angle)

    if direction == "pull":
        x += mvx * 2 #if the difference in charge is greater times by bigger number
        y += mvy * 2

    if direction == "push":
        x -= mvx * 2 #if the difference in charge is greater times by bigger number
        y -= mvy * 2

    return x,y

while run:
	# event handler
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONUP:
			# if player selects an element return element value
			if my < 369 and spawn:
				print(f"Element {clicked} has been selected")
				static_elements.append([active_element, mx, my])
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

	if REFRESH.draw(SCREEN):
		static_elements = []

	# loops over all elements drawing them and checking if they have been clicked
	for i in range(18):
		if ELEMENTS[i].draw(SCREEN) and not spawn:
			clicked = i + 1
			active_element = sprite.Sprite(clicked)
			spawn = True

	#creates a sprite which tracks the mouse when you hold down
	if spawn:
		active_element.draw(SCREEN, mx ,my)

	for i in range(len(static_elements)):
		static_elements[i][0].draw(SCREEN, static_elements[i][1] ,static_elements[i][2])

		if len(static_elements) >= 1 and spawn:
			x = static_elements[i][1]
			y = static_elements[i][2]

			distance_apart = int(math.sqrt((mx - x)**2 + (my - y)**2))
			
			if distance_apart >= (75 * 2):
				static_elements[i][1],static_elements[i][2] = move_elements(mx, my, x, y, "pull")

			if distance_apart < (75 * 2):
				static_elements[i][1],static_elements[i][2] = move_elements(mx, my, x, y, "push")

	pygame.display.update()

	clock.tick(120)

pygame.quit()