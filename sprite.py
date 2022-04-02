import pygame
import electron
import math

class Sprite():
    def __init__(element, atomic_number, x, y):
        # encapsulate the atomic number and coordinates
        element.atomic_number = atomic_number
        element.x = x
        element.y = y

        # set the electrons starting angle and shared electrons
        element.angle = 0

        # set the symbol of the electron
        element.symbols = ["H", "He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar"]
        element.font = pygame.font.Font("assets/sprites/Roboto-Regular.ttf", 32)
        element.symbol = element.font.render(element.symbols[element.atomic_number -1], True, (255,255,255))

        # lists to store elements electrons
        element.unbonded_electrons = []
        element.bonded_electrons = []
        element.borrowed_electrons = []

        # deduce the number of outer shell electrons
        num_of_electrons = atomic_number
        if atomic_number > 2:
            num_of_electrons = atomic_number - 2
        if atomic_number > 10:
            num_of_electrons = atomic_number - 10

        # creates all the electrons for this element and adds them to the unbonded list
        for i in range(num_of_electrons):
            element.unbonded_electrons.append(electron.Electron())


    # set the elements coordinates
    def set_coordinates(element, x, y):
        element.x = x
        element.y = y

    # get the elements coordinates
    def get_coordinates(element):
        return element.x, element.y

    def get_num_of_electrons(element):
        return len(element.unbonded_electrons) + len(element.bonded_electrons) + len(element.borrowed_electrons)
        
    # draws the element on the screen
    def draw(element, SCREEN):
        sprite_centre_x = element.x - element.symbol.get_width() / 2
        sprite_centre_y = element.y - element.symbol.get_height() / 2  
        SCREEN.blit(element.symbol, (sprite_centre_x, sprite_centre_y))

        element.draw_electrons(SCREEN)
        
    def get_sharing_electrons(element):
        num_of_outer_electrons = element.get_num_of_electrons()

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

                # if element is unreactive the push an extra 100px away
                if element.get_num_of_electrons() == 8 or element.get_num_of_electrons() == 2: 
                    if distance_apart < ((75 * 2) + 100):
                        x,y = element.move_element(ex, ey, ox, oy, "push")
                        other_element.set_coordinates(x,y) 
                        
                    
                # if the element is bonded and too close to something else then push apart to a 100px distance
                if element.get_sharing_electrons() == None or other_element.get_sharing_electrons() == None: 
                    if distance_apart < (75 * 2):
                        x,y = element.move_element(ex, ey, ox, oy, "push")
                        other_element.set_coordinates(x,y) 
                        

                # if elements both have a free electron then move closer together and if theyre touching theyre bonded
                if element.get_sharing_electrons() != None and other_element.get_sharing_electrons() != None:
                    if distance_apart > (75 * 2):
                         x,y = element.move_element(ex, ey, ox, oy, "pull")
                         other_element.set_coordinates(x,y)  
                         
                    if distance_apart < (75 * 2):
                        x,y = element.move_element(ex, ey, ox, oy, "push")
                        other_element.set_coordinates(x,y) 
                        
                    if distance_apart == (75 * 2):
                        element.set_bonded(other_element)
                        other_element.set_bonded(element)
                        for i in range(len(element.unbonded_electrons)):
                            element.unbonded_electrons[i].angle += 1
                
    def draw_electrons(element, SCREEN):
        #draw unbonded electrons
        for electron in element.unbonded_electrons:
            electron.draw(SCREEN, element.x, element.y)
        # draw bonded electrons
        for electron in element.bonded_electrons:
            electron.draw(SCREEN, element.x, element.y)

    def set_bonded(element, other_element):
        # move unbonded electron to bonded electrons
        element.bonded_electrons.append(element.unbonded_electrons[0])
        element.unbonded_electrons.pop(0)

        # move bonded electron to other elements borrowed electrons
        other_element.bonded_electrons.append(element.bonded_electrons[0])
        
        element.symbol = element.font.render(element.symbols[element.atomic_number -1], True, (255,0,255))

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

    def rotate_electrons(element, other_element):
        for electron in element.electrons:
            if not electron.get_bonded():
                electron.colour = (255, 0, 0)
                electron.rotate_electron(other_element.x, other_element.y, element.x, element.y)
