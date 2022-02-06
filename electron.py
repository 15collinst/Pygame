import math
import pygame

class Electron():
    def __init__(electron):
        electron.angle = 0
        electron.reactivity = 0
        electron.colour = (255, 255, 255)
        electron.size = 5

    def get_position(electron, mx, my, angle):
        orbit_radius = 75
        sine_of_orbit_degree = math.sin(angle * 0.0174532925)
        x_coordinate = mx + (sine_of_orbit_degree * orbit_radius)

        cosine_of_orbit_degree = math.cos(angle * 0.0174532925)
        y_coordinate = my + (cosine_of_orbit_degree * orbit_radius)

        return [x_coordinate, y_coordinate]

    def draw(electron, SCREEN, angle, mx, my):
        orbit_pos = electron.get_position(mx, my, angle)
        pygame.draw.circle(SCREEN, electron.colour, orbit_pos, electron.size, 0)