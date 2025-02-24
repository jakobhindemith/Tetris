import pygame
import random
import time
import window

GRID_WIDTH = 10
GRID_HEIGHT = 20
GRID_SIZE = 40

left = 0
right = 0
fast = 0.0

#2D List of Lists
grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

#Matrix
shapes = {
    'I': [(0,0), (0,40), (0,80), (0,120)],
    'O': [(0,0), (0,40), (40,0), (40,40)],
    'T': [(0,0), (40,0), (80, 0), (40, 40)],
    'L': [(0, 0), (0,40), (0,80), (40,80)],
    'Z': [(0, 0), (40,0), (40,40), (80,40)]
}

def can_move_down(y, shape, x_off):
    for block_x, block_y in shape:
        grid_x = (x_off + block_x) // GRID_SIZE
        grid_y = (y + block_y) // GRID_SIZE + 1
        #print("grid_x:", grid_x, " grid_y:", grid_y)
        if grid_x < 0 or grid_x >= GRID_WIDTH or grid_y >= GRID_HEIGHT:
            return False
        if grid[grid_y][grid_x] is not None:
            return False
    return True

#write the tetromino 
def place_tetromino(y, shape, x_offset, color):
    for block_x, block_y in shape:
        grid_x = (x_offset + block_x) // GRID_SIZE
        grid_y = (y + block_y) // GRID_SIZE
        if 1 <= grid_y < GRID_HEIGHT:
           grid[grid_y][grid_x] = color
        print("grid_x: ", grid_x, "grid_y: ", grid_y)

def draw_tetromino(screen):
    screen.fill("black")
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x]:
                pygame.draw.rect(screen, grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    window.draw_grid(screen)

def tetromino(screen, x, y, left, right, fast):
    #random shape
    shape_key = random.choice(list(shapes.keys())) 
    shape = shapes[shape_key]
    color = random.choice(["green", "orange", "red", "blue", "yellow"])
    #while moving down draw tetrominos
    while can_move_down(y, shape, x + right - left):
        right = window.get_counter_right()
        left = window.get_counter_left()
        fast = window.get_counter_fast()
        window.update() #To Move Tetromino
        y += 10

        draw_tetromino(screen)
        for block_x, block_y in shape:
            pygame.draw.rect(screen, color, (x + right - left + block_x, y + block_y, GRID_SIZE, GRID_SIZE))

        pygame.display.flip()
        time.sleep(0.1 - fast)


    place_tetromino(y, shape, x + right - left, color)
    #after every round(falling tetromino) the counter is set back to 0
    window.reset_counters()
    print("place_tetromino", y, shape, x ,"+", right, "-", left, color)
