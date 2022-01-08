import math
import pygame

pygame.init()

bg = (255, 255, 255)
orbit_col = (0, 0, 0)

orbit_start_pos = [500, 500]
orbits = [[100, 1, 90], [50, 0.5, 180], [10, 1, 0]]
position = [0, 0]
positions = []

size = [1000, 1000]
screen = pygame.display.set_mode(size)
screen.fill(bg)
pygame.display.set_caption("Orbits")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(bg)
    
    for c in range(0, len(orbit_col), 1):
        if c > 0:
            position = math.floor(positions[len(positions) - 1][0] + (math.sin(orbits[c][2] * 0.0174532925) * (orbits[c -1][0]))),
            math.floor(positions[len(positions) - 1][1] + (math.cos(orbits[c][2] * 0.0174532925) * (orbits[c - 1][0])))

        else:
            positions = orbit_start_pos

        pygame.draw.circle(screen, orbit_col, position, orbits[c][0], 1)

        orbits[c][2] += orbits[c][1]
        positions.append(position)

    positions = []

    pygame.display.update()

    clock.tick(60)

pygame.quit