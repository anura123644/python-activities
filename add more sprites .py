import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mouse Movement Collision Counter")

# Clock
clock = pygame.time.Clock()

# Player
player_size = 50
player = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, player_size, player_size)

# Enemies
enemy_size = 50
enemies = [pygame.Rect(random.randint(0, SCREEN_WIDTH-enemy_size), 
                       random.randint(0, SCREEN_HEIGHT-enemy_size), 
                       enemy_size, enemy_size) for _ in range(7)]

# Collision counter
collisions = 0

# Function to display a message
def display_message(text, screen):
    font = pygame.font.Font(None, 48)
    message = font.render(text, True, (0, 0, 0))
    text_rect = message.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    screen.blit(message, text_rect)
    pygame.display.flip()
    pygame.time.delay(1000)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player position to follow mouse pointer
    mouse_x, mouse_y = pygame.mouse.get_pos()
    player.center = (mouse_x, mouse_y)

    # Check collisions
    for enemy in enemies:
        if player.colliderect(enemy):
            collisions += 1
            # Reposition the enemy randomly
            enemy.x = random.randint(0, SCREEN_WIDTH-enemy_size)
            enemy.y = random.randint(0, SCREEN_HEIGHT-enemy_size)

            # Check if we reached a new century
            if collisions % 100 == 0:
                display_message("Good Job!", screen)

    # Drawing everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Display collision count
    font = pygame.font.Font(None, 36)
    text = font.render(f"Collisions: {collisions}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
