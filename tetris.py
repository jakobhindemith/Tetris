import pygame
import random
import time
import window

#list of shapes
shapes = ['I','O','T','L','Z']
#shapes = ['I']

#define the pricks
def tetromino(screen, x, y):
    i = 0
    #random shape
    shape = random.choice(shapes)
    print(shape)
     
    #drawing the tetromino
    match shape:
        case 'I':
            #for i in range(440):
            while i <= 440:
                pygame.draw.rect(screen, ("green"), (x, y+i, 40, 40))
                pygame.draw.rect(screen, ("green"), (x, y+40+i, 40, 40))
                pygame.draw.rect(screen, ("green"), (x, y+80+i, 40, 40))
                pygame.draw.rect(screen, ("green"), (x, y+120+i, 40, 40))
                pygame.display.flip()
                screen.fill(("black"))
                window.draw_grid(screen)
                time.sleep(0.05)      
                i = i + 10  
        case 'O':
            while i <= 520:
                pygame.draw.rect(screen, ("orange"), (x, y+i, 40, 40))
                pygame.draw.rect(screen, ("orange"), (x, y+40+i, 40, 40))
                pygame.draw.rect(screen, ("orange"), (x+40, y+i, 40, 40))
                pygame.draw.rect(screen, ("orange"), (x+40, y+40+i, 40, 40))
                pygame.display.flip()
                screen.fill(("black"))
                window.draw_grid(screen)
                time.sleep(0.05)
                i = i + 10
        case 'T':
            while i <= 520:
                pygame.draw.rect(screen, ("red"), (x, y+i, 40, 40))
                pygame.draw.rect(screen, ("red"), (x+40, y+i, 40, 40))
                pygame.draw.rect(screen, ("red"), (x+80, y+i, 40, 40))
                pygame.draw.rect(screen, ("red"), (x+40, y+40+i, 40, 40))
                time.sleep(0.05)
                pygame.display.flip()
                screen.fill(("black"))
                window.draw_grid(screen)
                i = i + 10
        case 'L':
            while i <= 480:
                pygame.draw.rect(screen, ("blue"), (x, y+i, 40, 40))
                pygame.draw.rect(screen, ("blue"), (x, y+40+i, 40, 40))
                pygame.draw.rect(screen, ("blue"), (x, y+80+i, 40, 40))
                pygame.draw.rect(screen, ("blue"), (x+40, y+80+i, 40, 40))
                time.sleep(0.05)
                pygame.display.flip()
                screen.fill(("black"))
                window.draw_grid(screen)
                i = i + 10
        case 'Z':
            while i <= 520:
                pygame.draw.rect(screen, ("yellow"), (x, y+i, 40, 40))
                pygame.draw.rect(screen, ("yellow"), (x+40, y+i, 40, 40))
                pygame.draw.rect(screen, ("yellow"), (x+40, y+40+i, 40, 40))
                pygame.draw.rect(screen, ("yellow"), (x+80, y+40+i, 40, 40))
                time.sleep(0.05)
                pygame.display.flip()
                screen.fill(("black"))
                window.draw_grid(screen)
                i = i + 10