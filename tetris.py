import pygame
import random

#list of shapes
shapes = ['I','O','T','L','Z']

#define the pricks
def tetromino(screen, x, y):
    #random shape
    shape = random.choice(shapes)
     
    #drawing the tetromino
    match shape:
        case 'I':
            pygame.draw.rect(screen, ("green"), (x, y, 40, 40))
            pygame.draw.rect(screen, ("green"), (x, y+40, 40, 40))
            pygame.draw.rect(screen, ("green"), (x, y+80, 40, 40))
            pygame.draw.rect(screen, ("green"), (x, y+120, 40, 40))
            pygame.display.flip()
        case 'O':
            pygame.draw.rect(screen, ("orange"), (x, y, 40, 40))
            pygame.draw.rect(screen, ("orange"), (x, y+40, 40, 40))
            pygame.draw.rect(screen, ("orange"), (x+40, y, 40, 40))
            pygame.draw.rect(screen, ("orange"), (x+40, y+40, 40, 40))
            pygame.display.flip()
        case 'T':
            pygame.draw.rect(screen, ("red"), (x, y, 40, 40))
            pygame.draw.rect(screen, ("red"), (x+40, y, 40, 40))
            pygame.draw.rect(screen, ("red"), (x+80, y, 40, 40))
            pygame.draw.rect(screen, ("red"), (x+40, y+40, 40, 40))
            pygame.display.flip()
        case 'L':
            pygame.draw.rect(screen, ("blue"), (x, y, 40, 40))
            pygame.draw.rect(screen, ("blue"), (x, y+40, 40, 40))
            pygame.draw.rect(screen, ("blue"), (x, y+80, 40, 40))
            pygame.draw.rect(screen, ("blue"), (x+40, y+80, 40, 40))
            pygame.display.flip()
        case 'Z':
            pygame.draw.rect(screen, ("yellow"), (x, y, 40, 40))
            pygame.draw.rect(screen, ("yellow"), (x+40, y, 40, 40))
            pygame.draw.rect(screen, ("yellow"), (x+40, y+40, 40, 40))
            pygame.draw.rect(screen, ("yellow"), (x+80, y+40, 40, 40))
            pygame.display.flip()


    
    


   