import pygame
import tetris
import random

counter_right = 0
counter_left =  0

#get counter
def get_counter_right():
    return counter_right

def get_counter_left():
    return counter_left

#inc right key
def inc_counter_right():
    global counter_right
    counter_right +=40

def inc_counter_left():
    global counter_left
    counter_left += 40


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

    #Event-Loop
    running = True
    while running:
        
        #starting falling tetrominos
        tetris.tetromino(screen, 80, 0)
        print("laeuft..")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                 running = False

def update():
    #keyboard events
    for event in pygame.event.get():
            #reading Arowkeys
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("Right") 
                    inc_counter_right()
                if event.key == pygame.K_LEFT:
                    print("Left")
                    inc_counter_left()
    

