import pygame
import button

# creates instances of the images
def instance_imgs(arr):

    for i in range(88): # note: range = number of elements
        i = str(i+1)
        temp = '1' # note: I havent made the images yet
        arr.append(pygame.image.load('images/buttons/'+temp+'.png').convert_alpha())

    return arr

# create element instances, positions elements
def instance_elements(px, py, table, imgs, arr):

    i = 0
    row = 0
    
    for r in table:
        row = row + 1
        for c in r:
            x = px + ((c - 1) * 64)
            y = py + ((row - 1) * 64)
            arr.append(button.Button(x, y, imgs[i], 0.64))
            i = i + 1

    return arr

