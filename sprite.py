import pygame
import electron
import math

class Sprite():
    def __init__(element, atomic_number, x, y):
        # encapsulate the atomic number and coordinates
        element.atomic_number = atomic_number
        element.x = x
        element.y = y

        # set the elements starting angle and shared electrons
        element.angle = 0
        element.shared_electrons = 0

        # set the symbol of the electron
        elements = ["H", "He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar"]
        font = pygame.font.Font("assets/sprites/Roboto-Regular.ttf", 32)
        element.symbol = font.render(elements[atomic_number -1], True, (255,255,255))


        # deduce the number of outer shell electrons
        num_of_electrons = atomic_number
        if atomic_number > 2:
            num_of_electrons = atomic_number - 2
        if atomic_number > 10:
            num_of_electrons = atomic_number - 10


        # creates all the electrons for this element
        electrons = []
        for i in range(num_of_electrons):
            electrons.append(electron.Electron())
        element.electrons = electrons

        print(element.get_sharing_electrons())

    def set_coordinates(element, x, y):
        element.x = x
        element.y = y

    def get_coordinates(element):
        return element.x, element.y
        
    # draws the element on the screen
    def draw(element, SCREEN, x ,y):
        sprite_centre_x = x - element.symbol.get_width() / 2
        sprite_centre_y = y - element.symbol.get_height() / 2  
        SCREEN.blit(element.symbol, (sprite_centre_x, sprite_centre_y))

        # draw all of the electrons going around the element
        for i in range(len(element.electrons)):
            rotation = i * (360 / len(element.electrons))
            element.electrons[i].draw(SCREEN, element.angle+rotation, x, y)

        element.angle += 1


    def get_sharing_electrons(element):
        num_of_outer_electrons = len(element.electrons) + element.shared_electrons

        # exeption for H and He which are trying to achive an outer shell of 2
        if element.atomic_number <= 2:
            # element has a full outer shell and so no sharing electrons
            if num_of_outer_electrons == 2: return 0
            else: return num_of_outer_electrons
        else:
            # element has a full outer shell and so no sharing electrons
            if num_of_outer_electrons == 8: return 0
            else: return num_of_outer_electrons

    def move_element(mx, my, x, y, direction):
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


# if len(static_elements) >= 1 and spawn:
# 			x = static_elements[i][1]
# 			y = static_elements[i][2]

# 			distance_apart = int(math.sqrt((mx - x)**2 + (my - y)**2))
			
# 			if distance_apart >= (75 * 2):
# 				static_elements[i][1],static_elements[i][2] = move_elements(mx, my, x, y, "pull")

# 			if distance_apart < (75 * 2):
# 				static_elements[i][1],static_elements[i][2] = move_elements(mx, my, x, y, "push")




