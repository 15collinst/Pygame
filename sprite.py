import pygame

def spawn(clicked, screen, mx ,my):
    sprite_img = pygame.image.load('images/sprites/1.1.png').convert_alpha()
    screen.blit(sprite_img, (mx-50, my-50))
