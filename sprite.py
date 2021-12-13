import pygame

def spawn(clicked, screen, mx ,my,element_number):
    element_number = str(element_number)
    sprite_img = pygame.image.load('assets/sprites/Sprite_'+element_number+'.svg').convert_alpha()
    sprite_centre_x = mx - sprite_img.get_width() / 2
    sprite_centre_y = my - sprite_img.get_height() / 2
    screen.blit(sprite_img, (sprite_centre_x, sprite_centre_y))


