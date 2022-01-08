import math
import pygame

pygame.init()

bg = (255, 255, 255)
orbit_col = (0, 0, 0)

orbits = [[100, 1, 90, 0, 0], [50, 0.5, 180, 0, 0], [10, 1, 0, 0, 0], [5, 1, 250, 0, 0]]
position = [0, 0]
positions = []

size = [1000, 1000]
screen = pygame.display.set_mode(size)
screen.fill(bg)
pygame.display.set_caption("Orbits")

done = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(bg)

    for orbit in orbits:
        if orbit == orbits[0]:
            orbit_pos = pygame.mouse.get_pos()
        else:
            orbit_parent = orbits[orbits.index(orbit) - 1]
            radius_of_parent_orbit = orbit_parent[0]

            orbit_parent_position_x = orbit_parent[3]
            sine_of_orbit_degree = math.sin(orbit[2] * 0.0174532925)
            x_position = orbit_parent_position_x + (sine_of_orbit_degree * radius_of_parent_orbit)

            orbit_parent_position_y = orbit_parent[4]
            cosine_of_orbit_degree = math.cos(orbit[2] * 0.0174532925)
            y_position = orbit_parent_position_y + (cosine_of_orbit_degree * radius_of_parent_orbit)

            orbit_pos = [x_position, y_position]

        pygame.draw.circle(screen, orbit_col, orbit_pos, orbit[0], 1)

        orbit[2] += orbit[1] # rotate the orbit by the speed

        x,y = orbit_pos
        orbit[3] = x
        orbit[4] = y

    pygame.display.update()


pygame.quit