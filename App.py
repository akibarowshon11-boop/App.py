import pygame
import random
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("💩 Catch the Poop Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKIN = (255, 220, 180)
BLUE = (0, 120, 255)
BROWN = (139, 69, 19)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Player
player_x = 350
player_y = 500
player_speed = 7

# Poop
poop_x = random.randint(50, 750)
poop_y = 0
poop_speed = 5

score = 0

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 100:
        player_x += player_speed

    # Falling poop
    poop_y += poop_speed

    # Reset poop
    if poop_y > HEIGHT:
        poop_y = 0
        poop_x = random.randint(50, 750)

    # Collision (mouth)
    mouth_rect = pygame.Rect(player_x + 30, player_y + 20, 40, 20)
    poop_rect = pygame.Rect(poop_x, poop_y, 30, 30)

    if poop_rect.colliderect(mouth_rect):
        score += 1
        poop_y = 0
        poop_x = random.randint(50, 750)

    # Draw player
    pygame.draw.circle(screen, SKIN, (player_x + 50, player_y + 40), 40)   # head
    pygame.draw.rect(screen, BLUE, (player_x + 15, player_y + 80, 70, 60)) # shirt

    # Eyes
    pygame.draw.circle(screen, BLACK, (player_x + 35, player_y + 30), 4)
    pygame.draw.circle(screen, BLACK, (player_x + 65, player_y + 30), 4)

    # Mouth open
    pygame.draw.ellipse(screen, BLACK, (player_x + 30, player_y + 50, 40, 20))

    # Shirt text
    text_ohi = font.render("OHI", True, WHITE)
    screen.blit(text_ohi, (player_x + 20, player_y + 95))

    # Draw poop
    pygame.draw.circle(screen, BROWN, (poop_x + 15, poop_y + 15), 15)

    # Score
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)
