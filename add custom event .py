import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Keyboard Trigger Example")

# Define colors
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Create a Sprite class
class CustomSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Create two sprites
sprite1 = CustomSprite(COLORS[0], 100, 100, 200, 250)
sprite2 = CustomSprite(COLORS[1], 100, 100, 500, 250)

# Add sprites to a group
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Define a custom event
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Trigger custom event using the keyboard
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT))
        
        if event.type == CHANGE_COLOR_EVENT:
            # Change the colors of the sprites randomly
            sprite1.image.fill(random.choice(COLORS))
            sprite2.image.fill(random.choice(COLORS))

    # Clear the screen
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
