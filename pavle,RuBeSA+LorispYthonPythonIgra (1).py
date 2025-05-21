import pygame
pygame.init()

SCREEN_WIDTH=1600
SCREEN_HEIGHT=900
# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moon escape")

# Fill the screen with a color
screen.fill((255, 255, 255))  # This fills the screen with blue
pygame.display.update()


# Player settings

# Create a surface and pass in a tuple containing its length and width
surf = pygame.Surface((50, 50))

# Give the surface a color to separate it from the background
surf.fill((0, 0, 0))
rect = surf.get_rect()
screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
pygame.display.flip()
# Put the center of surf at the center of the display
surf_center = (
    (SCREEN_WIDTH-surf.get_width())/2,
    (SCREEN_HEIGHT-surf.get_height())/2
)

# Draw surf at the new coordinates
screen.blit(surf, surf_center)
pygame.display.flip()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
