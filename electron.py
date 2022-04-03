import math
import pygame

class Electron():
    def __init__(electron, parent_element):
        electron.parent = parent_element
        electron.angle = 0
        electron.colour = (255, 255, 255)
        electron.size = 5
        electron.bonded_element = None

    def set_angle(electron):
        x1, y1 = electron.parent.get_coordinates()
        x2, y2 = electron.bonded_element.get_coordinates()

        dx = x1 - x2
        dy = y1 - y2

        electron.angle = math.degrees(math.atan2(dx, dy))+180

    def set_bonded(electron, bonded_element):
        electron.bonded_element = bonded_element

    def get_position(electron, mx, my):
        orbit_radius = 75
        sine_of_orbit_degree = math.sin(electron.angle * 0.0174532925)
        x_coordinate = mx + (sine_of_orbit_degree * orbit_radius)

        cosine_of_orbit_degree = math.cos(electron.angle * 0.0174532925)
        y_coordinate = my + (cosine_of_orbit_degree * orbit_radius)

        return [x_coordinate, y_coordinate]

    def draw(electron, SCREEN, mx, my):
        if electron.bonded_element != None:
            electron.set_angle()
            
        orbit_pos = electron.get_position(mx, my)
        pygame.draw.circle(SCREEN, electron.colour, orbit_pos, electron.size, 0)

    def get_bonded(electron):
        return electron.bonded_element