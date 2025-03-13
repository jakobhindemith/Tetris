import pygame
import random
import time
import window

#grid size
GRID_WIDTH = 10
GRID_HEIGHT = 20
GRID_SIZE = 40

shape_key = ""
shape = []

#2D List of Lists
grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

#Matrix
shapes = {
    #main tetrominos
    #'I': [(0, -60), (0, -20), (0, 20), (0, 60)],
    #'O': [(0,0), (0,40), (40,0), (40,40)],
    'T': [(0, -20), (0, 0), (0, 20), (-20, 0)],
    #'L': [(0,0), (0,40), (0,80), (40,80)],
    #'Z': [(0,0), (40,0), (40,40), (80,40)],

    #diffrend positions
    #'-':  [(-60, 0), (-20, 0), (20, 0), (60, 0)],
    'TT': [(-20, 0), (0, 0), (20, 0), (0, 20)],
    'TTT': [(0,0), (40,0), (40,-40), (80,0)],
    'TTTT': [(0, -20), (0, 0), (0, 20), (20, 0)],
    #'LL': [(0,0), (40,0), (0,40), (80,0)],
    #'LLL': [(0,0), (0,40), (0,80), (-40,0)],
    #'LLLL': [(0,0), (40,0), (0,-40), (80,0)],
    #'ZZ':[(40,0), (40,40), (0,40), (0,80)],

    #mirrored 
    #'-L':[(0,0), (0,40), (0,80), (-40,80)],
    #'-LL':[(0,0), (-40,0), (0,40), (-80,0)],
    #'-LLL':[(0,0), (0,40), (0,80), (40,0)],
    #'-LLLL':[(0,0), (40,0), (0,-40), (80,0)],
    #'-Z': [(0,40), (40,40), (40,0), (80,0)],
    #'-ZZ': [(0,0), (0,40), (40,40), (40,80)]
}

#Stacking
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

#write the tetromino to the grid
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

def clear_rows():
    global grid
    #empty gamefield
    new_grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    new_row = GRID_HEIGHT - 1
    #iterate through gamefield
    for x in range(GRID_HEIGHT - 1, -1, -1):
        if None in grid[x]:
            #copy new grid
            new_grid[new_row] = grid[x]
            new_row -= 1
    grid = new_grid

def tetromino(screen, x, y, left, right, fast):
    global shape_key
    global shape
    shape_key = random.choice(list(shapes.keys())) 
    print("shape_key", shape_key)
    shape = shapes[shape_key]
    print("shape", shape)
    color = random.choice(["green", "orange", "red", "blue", "yellow"])
    while can_move_down(y, shape, x + right - left):
        right = window.get_counter_right()
        left = window.get_counter_left()
        fast = window.get_counter_fast()
        window.update()
        y += 10

        draw_tetromino(screen)
        for block_x, block_y in shape:
            pygame.draw.rect(screen, color, (x + right - left + block_x, y + block_y, GRID_SIZE, GRID_SIZE))

        pygame.display.flip()
        time.sleep(0.1 - fast)
        clear_rows()
        #window.stop()

    place_tetromino(y, shape, x + right - left, color)
    window.reset_counters()
    print("place_tetromino", y, shape, x ,"+", right, "-", left, color)
    
def rotate():
    global shape_key
    global shape

    if shape_key == 'I':
        shape = [(-60, 0), (-20, 0), (20, 0), (60, 0)]
        shape_key = '-'
    elif shape_key == '-':
        shape = [(0, -60), (0, -20), (0, 20), (0, 60)]
        shape_key = 'I'
    
    if shape_key == 'T':
        shape =  [(-20, 0), (0, 0), (20, 0), (0, 20)]
        shape_key = 'TT'
    elif shape_key == 'TT':
        shape = [(0, -20), (0, 0), (0, 20), (20, 0)]
        shape_key = 'TTT'
    elif shape_key == 'TTT':
        shape = [(-20, 0), (0, 0), (20, 0), (0, -20)]
        shape_key = 'TTTT'
    elif shape_key == 'TTTT':
        shape = [(0, -20), (0, 0), (0, 20), (-20, 0)]
        shape_key = 'T'

    if shape_key == 'L':
        shape = [(0,0), (40,0), (0,40), (80,0)]
        shape_key = 'LL'
    elif shape_key == 'LL':
        shape = [(0,0), (0,40), (0,80), (-40,0)]
        shape_key = 'LLL'
    elif shape_key == 'LLL':
        shape = [(0,0), (40,0), (0,-40), (80,0)]
        shape_key = 'LLLL'
    elif shape_key == 'LLLL':
        shape = [(0,0), (0,40), (0,80), (40,80)]
        shape_key = 'L'

    if shape_key == '-L':
        shape = [(0,0), (-40,0), (0,40), (-80,0)]
        shape_key = '-LL'  
    elif shape_key == '-LL':
        shape = [(0,0), (0,40), (0,80), (40,0)]
        shape_key = '-LLL'  
    elif shape_key == '-LLL':
        shape = [(0,0), (-40,0), (0,-40), (-80,0)]
        shape_key = '-LLLL'  
    elif shape_key == '-LLLL':
        shape = [(0,0), (0,40), (0,80), (-40,80)]
        shape_key = '-L'

    if shape_key == 'Z':
       shape = [(40,0), (40,40), (0,40), (0,80)]
       shape_key = 'ZZ'
    elif shape_key == 'ZZ':
       shape = [(0,0), (40,0), (40,40), (80,40)]
       shape_key = 'Z'

    if shape_key == '-Z':
        shape = [(0,0), (0,40), (40,40), (40,80)]
        shape_key = '-ZZ'
    elif shape_key == '-ZZ':
        shape = [(0,40), (40,40), (40,0), (80,0)]
        shape_key = '-Z'
    



