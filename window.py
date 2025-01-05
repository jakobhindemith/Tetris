import pygame

def draw_grid(surface):
    """Zeichnet ein Gitter auf die gegebene pygame-Surface."""
    for x in range(0, 400, 20):  # Rastergröße 20x20 Pixel
        for y in range(0, 600, 20):
            pygame.draw.rect(surface, ("white"), (x, y, 20, 20), 1)  # Schwarze Gitterlinien

def create_window():
    """Erstellt ein pygame-Fenster und zeigt ein Gitter."""
    # Initialisiere pygame
    pygame.init()
    pygame.display.set_caption("Tetris")
    
    # Fenstergröße
    screen = pygame.display.set_mode((400, 600))
    
    # Hintergrundfarbe setzen
    screen.fill(("black"))
    
    # Gitter zeichnen
    draw_grid(screen)
    
    # Aktualisiere das Display
    pygame.display.flip()
    
    # Event-Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Beenden des Fensters
                running = False
    
    # Beende pygame
    pygame.quit()

