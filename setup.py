import pygame
import button

# creates instances of the images
def instance_imgs(arr):

    for i in range(18): # note: range = number of elements
        i = str(i+1)
        img = 'images/elements/'+i+'.png'
        arr.append(pygame.image.load(img).convert_alpha())

    return arr

# create element instances, positions elements
def instance_elements(px, py, table, imgs, arr):

    i = 0
    row = 0
    
    for r in table:
        row = row + 1
        for c in r:
            x = px + ((c - 1) * 70)
            y = py + ((row - 1) * 75)
            arr.append(button.Button(x, y, imgs[i], 0.25))
            i = i + 1

    return arr

