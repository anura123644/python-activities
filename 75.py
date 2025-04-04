import pygame

pygame.init()

screen = pygame.display.set_mode((300, 400))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # Fill the background with a color
    screen.fill((0, 0, 0))  # Black background
    
    # Draw a rectangle
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
    
    # Update the display
    pygame.display.flip()

pygame.quit()
