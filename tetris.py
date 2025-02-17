import pygame
import random
import time
import window

#list of shapes
shapes = ['I','O','T','L','Z']
#test shape
#shapes = ['I']

#define the pricks
def tetromino(screen, x, y):
    #counter down
    i = 0
    #counter right
    right = 0
    #counter left
    left = 0
    #random shape
    shape = random.choice(shapes)
    print(shape)   
    #drawing the tetromino
    match shape:
        case 'I':
            #until end
            while i <= 440:
                #get key input
                right = window.get_counter_right()
                left = window.get_counter_left()
                #update key input
                window.update()
                #draw the falling tetromino
                pygame.draw.rect(screen, ("green"), (x+(right)-(left), y+i, 40, 40))
                pygame.draw.rect(screen, ("green"), (x+(right)-(left), y+40+i, 40, 40))
                pygame.draw.rect(screen, ("green"), (x+(right)-(left), y+80+i, 40, 40))
                pygame.draw.rect(screen, ("green"), (x+(right)-(left), y+120+i, 40, 40))
                #show 
                pygame.display.flip()
                screen.fill(("black"))
                window.draw_grid(screen)
                #timer for faling
                time.sleep(0.05)      
                i = i + 10
        case 'O':
            while i <= 520:
                right = window.get_counter_right()
                left = window.get_counter_left()
                window.update()
                pygame.draw.rect(screen, ("orange"), (x+(right)-(left), y+i, 40, 40))
                pygame.draw.rect(screen, ("orange"), (x+(right)-(left), y+40+i, 40, 40))
                pygame.draw.rect(screen, ("orange"), (x+40+(right)-(left), y+i, 40, 40))
                pygame.draw.rect(screen, ("orange"), (x+40+(right)-(left), y+40+i, 40, 40))
                pygame.display.flip()
                screen.fill(("black"))
                window.draw_grid(screen)
                time.sleep(0.05)
                i = i + 10
        case 'T':
            while i <= 520:
                right = window.get_counter_right()
                left = window.get_counter_left()
                window.update()
                pygame.draw.rect(screen, ("red"), (x+(right)-(left), y+i, 40, 40))
                pygame.draw.rect(screen, ("red"), (x+40+(right)-(left), y+i, 40, 40))
                pygame.draw.rect(screen, ("red"), (x+80+(right)-(left), y+i, 40, 40))
                pygame.draw.rect(screen, ("red"), (x+40+(right)-(left), y+40+i, 40, 40))
                time.sleep(0.05)
                pygame.display.flip()
                screen.fill(("black"))
                window.draw_grid(screen)
                i = i + 10
        case 'L':
            while i <= 480:
                right = window.get_counter_right()
                left = window.get_counter_left()
                window.update()
                pygame.draw.rect(screen, ("blue"), (x+(right)-(left), y+i, 40, 40))
                pygame.draw.rect(screen, ("blue"), (x+(right)-(left), y+40+i, 40, 40))
                pygame.draw.rect(screen, ("blue"), (x+(right)-(left), y+80+i, 40, 40))
                pygame.draw.rect(screen, ("blue"), (x+40+(right)-(left), y+80+i, 40, 40))
                time.sleep(0.05)
                pygame.display.flip()
                screen.fill(("black"))
                window.draw_grid(screen)
                i = i + 10
        case 'Z':
            while i <= 520:
                right = window.get_counter_right()
                left = window.get_counter_left()
                window.update()
                pygame.draw.rect(screen, ("yellow"), (x+(right)-(left), y+i, 40, 40))
                pygame.draw.rect(screen, ("yellow"), (x+40+(right)-(left), y+i, 40, 40))
                pygame.draw.rect(screen, ("yellow"), (x+40+(right)-(left), y+40+i, 40, 40))
                pygame.draw.rect(screen, ("yellow"), (x+80+(right)-(left), y+40+i, 40, 40))
                time.sleep(0.05)
                pygame.display.flip()
                screen.fill(("black"))
                window.draw_grid(screen)
                i = i + 10