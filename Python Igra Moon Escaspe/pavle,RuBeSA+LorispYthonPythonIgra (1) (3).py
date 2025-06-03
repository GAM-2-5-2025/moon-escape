import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moon Escape")  # Renamed window

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Load images safely with fallback color surfaces if missing
def load_image(filename, fallback_color, size=None):
    try:
        img = pygame.image.load(filename).convert_alpha()
        if size:
            img = pygame.transform.scale(img, size)
        return img
    except pygame.error:
        # Return colored surface fallback if image not found
        surf = pygame.Surface(size if size else (50, 50))
        surf.fill(fallback_color)
        return surf

background_img = load_image("background.png", (0, 0, 64), (SCREEN_WIDTH, SCREEN_HEIGHT))
player_img = load_image("player.png", (255, 0, 0), (50, 50))
enemy_img_raw = load_image("enemy.png", (0, 255, 255), (50, 50))  # We'll scale per enemy size later

player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 5

class Enemy:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        # Scale enemy image to size dynamically
        self.image = pygame.transform.scale(enemy_img_raw, (width, height))

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

enemies = []

def spawn_enemy(current_speed):
    width = random.randint(30, 80)
    height = random.randint(30, 80)
    x_pos = random.randint(0, SCREEN_WIDTH - width)
    y_pos = -height
    enemies.append(Enemy(x_pos, y_pos, width, height, current_speed))

running = True
spawn_timer = 0
base_spawn_delay = 30
spawn_delay = base_spawn_delay
start_ticks = pygame.time.get_ticks()

base_enemy_speed = 3
speed_increase_per_second = 0.05

while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    screen.blit(background_img, (0, 0))
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    screen.blit(player_img, player_rect)

    elapsed_seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    current_enemy_speed = base_enemy_speed + speed_increase_per_second * elapsed_seconds
    spawn_delay = max(base_spawn_delay - int(elapsed_seconds * 2), 5)

    spawn_timer += 1
    if spawn_timer >= spawn_delay:
        spawn_enemy(current_enemy_speed)
        spawn_timer = 0

    for enemy in enemies[:]:
        enemy.move()
        enemy.draw(screen)

        if player_rect.colliderect(enemy.rect):
            print("Game Over!")
            running = False

        if enemy.rect.y > SCREEN_HEIGHT:
            enemies.remove(enemy)

    timer_text = font.render(f"Time: {int(elapsed_seconds)}s", True, (255, 255, 255))
    screen.blit(timer_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
