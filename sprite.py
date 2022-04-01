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
        element.symbols = ["H", "He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar"]
        element.font = pygame.font.Font("assets/sprites/Roboto-Regular.ttf", 32)
        element.symbol = element.font.render(element.symbols[element.atomic_number -1], True, (255,255,255))

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

    # set the elements coordinates
    def set_coordinates(element, x, y):
        element.x = x
        element.y = y

    # get the elements coordinates
    def get_coordinates(element):
        return element.x, element.y
        
    # draws the element on the screen
    def draw(element, SCREEN):
        sprite_centre_x = element.x - element.symbol.get_width() / 2
        sprite_centre_y = element.y - element.symbol.get_height() / 2  
        SCREEN.blit(element.symbol, (sprite_centre_x, sprite_centre_y))

        # draw all of the electrons going around the element
        for i in range(len(element.electrons)):
            rotation = i * (360 / len(element.electrons))
            element.electrons[i].draw(SCREEN, element.angle+rotation, element.x, element.y)

        element.angle += 1


    def get_sharing_electrons(element):
        num_of_outer_electrons = len(element.electrons) + element.shared_electrons

        # exeption for H and He which are trying to achive an outer shell of 2
        if element.atomic_number <= 2:
            # element has a full outer shell and so no sharing electrons
            if num_of_outer_electrons == 2: return None
            else: return num_of_outer_electrons
        else:
            # element has a full outer shell and so no sharing electrons
            if num_of_outer_electrons == 8: return None
            else: return num_of_outer_electrons


    def bond_element(element, list_of_elements):
        for other_element in list_of_elements:

            # if its not looking at itself
            if element != other_element:

                ex, ey = element.get_coordinates()
                ox, oy = other_element.get_coordinates()
            
                distance_apart = int(math.sqrt((ex - ox)**2 + (ey - oy)**2)) 
                    
                # if the element is bonded and too close to something else then push apart to a 100px distance
                if element.get_sharing_electrons() == None or other_element.get_sharing_electrons() == None: 
                    if distance_apart < (75 * 2):
                        x,y = element.move_element(ex, ey, ox, oy, "push")
                        other_element.set_coordinates(x,y) 

                if element.get_sharing_electrons() != None and other_element.get_sharing_electrons() != None:
                    if distance_apart > (75 * 2):
                         x,y = element.move_element(ex, ey, ox, oy, "pull")
                         other_element.set_coordinates(x,y)  
                    if distance_apart < (74 * 2):
                        x,y = element.move_element(ex, ey, ox, oy, "push")
                        other_element.set_coordinates(x,y) 

                    if distance_apart == (75 * 2):
                        element.shared_electrons += 1
                        other_element.shared_electrons += 1
                        element.symbol = element.font.render(element.symbols[element.atomic_number -1], True, (255,255,0))
                        other_element.symbol = other_element.font.render(other_element.symbols[other_element.atomic_number -1], True, (255,255,0))


    def move_element(element, mx, my, x, y, direction):
        dx = mx - x
        dy = my - y

        angle = math.atan2(dx,dy)

        #returns between 1 or -1 to adjust distance between
        mvx = math.sin(angle)  
        mvy = math.cos(angle)

        if direction == "pull":
            x += mvx * 1 #if the difference in charge is greater times by bigger number
            y += mvy * 1

        if direction == "push":
            x -= mvx * 1 #if the difference in charge is greater times by bigger number
            y -= mvy * 1

        return x,y




