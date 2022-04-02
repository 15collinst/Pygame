import math
import pygame

class Electron():
    def __init__(electron):
        electron.angle = 0
        electron.colour = (255, 255, 255)
        electron.size = 5
        electron.bonded = False

    def get_angle(electron, other_x, other_y, ex, ey):
        x, y = electron.get_position(ex, ey)
        dx = x - other_x
        dy = y - other_y

        adjustment = math.degrees(math.atan2(dx, dy))+90

    def get_position(electron, mx, my):
        orbit_radius = 75
        sine_of_orbit_degree = math.sin(electron.angle * 0.0174532925)
        x_coordinate = mx + (sine_of_orbit_degree * orbit_radius)

        cosine_of_orbit_degree = math.cos(electron.angle * 0.0174532925)
        y_coordinate = my + (cosine_of_orbit_degree * orbit_radius)

        return [x_coordinate, y_coordinate]

    def draw(electron, SCREEN, mx, my):
        orbit_pos = electron.get_position(mx, my)
        pygame.draw.circle(SCREEN, electron.colour, orbit_pos, electron.size, 0)

    def get_bonded(electron):
        return electron.bonded