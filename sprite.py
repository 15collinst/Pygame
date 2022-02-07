import pygame
import electron
import math

class Sprite():
    def __init__(element, atomic_number):
        element.atomic_number = atomic_number
        element.angle = 0
        num_of_electrons = atomic_number

        if atomic_number > 2:
            num_of_electrons = atomic_number - 2
        if atomic_number > 10:
            num_of_electrons = atomic_number - 10

        electrons = []
        for i in range(num_of_electrons):
            electrons.append(electron.Electron())
        element.electrons = electrons
        
    def draw(element, SCREEN, mx ,my):
        elements = ["H", "He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar"]
        symbol = elements[element.atomic_number -1]
        font = pygame.font.Font("assets/sprites/Roboto-Regular.ttf", 32)
        img = font.render(symbol, True, (255,255,255))
        sprite_centre_x = mx - img.get_width() / 2
        sprite_centre_y = my - img.get_height() / 2  
        SCREEN.blit(img, (sprite_centre_x, sprite_centre_y))
        pygame.draw.circle(SCREEN, (255,0,0), [mx, my], 150, 0)

        for i in range(len(element.electrons)):
            rotation = i * (360 / len(element.electrons))
            element.electrons[i].draw(SCREEN, element.angle+rotation, mx, my)

    def active(element, mx, my, static_elements):
        if not static_elements:
            element.angle += 1
        else:
            for static_element in static_elements:
                if math.sqrt(((static_element[1] - mx) ** 2) + ((static_element[2] - my) ** 2) ) > 300:
                    print(f"not colliding with {static_element}")
                else:
                    print(f"colliding with {static_element}")
        


