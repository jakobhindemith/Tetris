import pygame

def draw_grid(surface):
    """Zeichnet ein Gitter auf die gegebene pygame-Surface."""
    for x in range(0, 400, 40):  #gridsize 20x20 Pixel width
        for y in range(0, 600, 40): #gridsize 20x20 Pixel height
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
    
    # Event-Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

