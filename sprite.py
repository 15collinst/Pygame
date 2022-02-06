import pygame
import electron

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

        for i in range(len(element.electrons)):
            rotation = i * (360 / len(element.electrons))
            element.electrons[i].draw(SCREEN, element.angle+rotation, mx, my)

        element.angle += 1


