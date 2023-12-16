import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game - By: Mayank")

clock = pygame.time.Clock()

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 80))
        self.image.fill((0, 0, 21))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 5
        self.direction = 0

    def update(self):
        self.rect.x += self.direction * self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((random.randint(30, 60), 40))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
            self.rect.centerx = random.randint(30, WIDTH - 30)

all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

car = Car()
all_sprites.add(car)

running = False
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = True

    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(FPS)

for _ in range(10):
    obstacle = Obstacle(random.randint(30, WIDTH - 30), random.randint(-HEIGHT, 0))
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car.direction = -1
    elif keys[pygame.K_RIGHT]:
        car.direction = 1
    else:
        car.direction = 0

    all_sprites.update()

    hits = pygame.sprite.spritecollide(car, obstacles, False)
    if hits:
        running = False

    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
