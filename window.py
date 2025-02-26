import pygame
import tetris
import random
import time

counter_right = 0
counter_left =  0
count_fast = 0.0

GRID_WITH = 400
GRID_LENGH = 800
BLOCK = 40

def reset_counters():
    global count_fast, counter_left, counter_right
    counter_right = 0
    counter_left =  0
    count_fast = 0.0

#get counter
def get_counter_fast():
    return count_fast

def get_counter_right():
    return counter_right

def get_counter_left():
    return counter_left

#inc key action
def inc_counter_right():
    global counter_right
    counter_right +=40

def inc_counter_left():
    global counter_left
    counter_left += 40

def counter_fast():
    global count_fast
    count_fast += 0.1

def draw_grid(surface):
    for x in range(0, GRID_WITH, BLOCK):
        for y in range(0, GRID_LENGH, BLOCK):
            pygame.draw.rect(surface, ("white"), (x, y, BLOCK, BLOCK), 1)
    
def create_window():
    pygame.init()
    pygame.display.set_caption("Tetris")
    #screen size
    screen = pygame.display.set_mode((GRID_WITH, GRID_LENGH))
    # Background
    screen.fill(("black"))
    draw_grid(screen)
    #set display
    pygame.display.flip()

    #Game-Loop
    running = True
    while running:
        tetris.tetromino(screen, 80, 0, 0, 0, 0.0)
        update()

#stop the game -> esc
def stop():
    time.sleep(10000)
             
def update():
    #keyboard events
    for event in pygame.event.get():
            #reading Arowkeys
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    inc_counter_right()
                if event.key == pygame.K_LEFT:
                    inc_counter_left()
                #if event.key == pygame.K_UP: #to rotate tetrominos
                   # tetris.rotate()
                if event.key == pygame.K_DOWN:
                    counter_fast()
                if event.key == pygame.K_ESCAPE:
                    stop()
        elif event.type == pygame.QUIT:
              pygame.quit()
              exit()