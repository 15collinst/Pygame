import pygame

def spawn(clicked, screen, mx ,my,element_number):
    elements = ["H", "He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar"]
    font = pygame.font.Font("assets/sprites/Roboto-Regular.ttf", 32)
    img = font.render(elements[element_number -1], True, (255,255,255))
    sprite_centre_x = mx - img.get_width() / 2
    sprite_centre_y = my - img.get_height() / 2  
    screen.blit(img, (sprite_centre_x, sprite_centre_y))


