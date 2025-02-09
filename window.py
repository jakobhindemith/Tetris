import pygame
import tetris
import time
import random

def draw_grid(surface):
    for x in range(0, 400, 40):  #width
        for y in range(0, 600, 40): #height
            pygame.draw.rect(surface, ("white"), (x, y, 40, 40), 1)  #Gitterlinien

def create_window():

    pygame.init()
    pygame.display.set_caption("Tetris")
    #screen size
    screen = pygame.display.set_mode((400, 600))
    # Background
    screen.fill(("black"))
    draw_grid(screen)
    #set display
    pygame.display.flip()
    

    #tetromino initialize
    #tetris.tetromino(screen, random.randint(40, 360), 0)

    #Event-Loop
    running = True
    while running:
        for event in pygame.event.get():
            #tetromino initialize
            tetris.tetromino(screen, random.randint(40, 360), 0)

            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

