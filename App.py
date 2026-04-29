import pygame
import random

# Initialize Pygame
pygame.init()

# Screen Settings
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gu-Khor Ohi Game")

# Colors
SKY_BLUE = (135, 206, 235)
BROWN = (101, 67, 33)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SKIN = (255, 224, 189)

# Game Constants
GRAVITY = 5
Ohi_SPEED = 8

# Fonts
font_small = pygame.font.SysFont("Arial", 22, bold=True)
font_large = pygame.font.SysFont("Arial", 36, bold=True)

class Poop:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = -50
        self.radius = 20

    def fall(self):
        self.y += GRAVITY

    def draw(self):
        # Drawing a simple poop shape using circles
        pygame.draw.circle(screen, BROWN, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, BROWN, (self.x, self.y - 15), self.radius - 5)
        pygame.draw.circle(screen, BROWN, (self.x, self.y - 25), self.radius - 12)

class Ohi:
    def __init__(self):
        self.width = 100
        self.height = 150
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 20

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= Ohi_SPEED
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
            self.x += Ohi_SPEED

    def draw(self):
        # Head
        pygame.draw.circle(screen, SKIN, (self.x + 50, self.y + 30), 30)
        # Open Mouth (Ha kora mukh)
        pygame.draw.ellipse(screen, BLACK, (self.x + 35, self.y + 35, 30, 20))
        # Body (Ganji)
        pygame.draw.rect(screen, WHITE, (self.x + 20, self.y + 60, 60, 80))
        # Text on Ganji
        label = font_small.render("OHI", True, RED)
        screen.blit(label, (self.x + 35, self.y + 85))

def main():
    clock = pygame.time.Clock()
    ohi = Ohi()
    poops = [Poop()]
    score = 0
    running = True

    while running:
        screen.fill(SKY_BLUE)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ohi.move(keys)
        ohi.draw()

        for p in poops[:]:
            p.fall()
            p.draw()

            # Collision Detection (Check if poop enters mouth area)
            mouth_rect = pygame.Rect(ohi.x + 35, ohi.y + 35, 30, 20)
            poop_rect = pygame.Rect(p.x - 15, p.y - 15, 30, 30)

            if mouth_rect.colliderect(poop_rect):
                score += 1
                poops.remove(p)
                poops.append(Poop())

            # Reset if poop falls off screen
            if p.y > HEIGHT:
                poops.remove(p)
                poops.append(Poop())

        # Display Score
        score_text = font_large.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (20, 20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
    
