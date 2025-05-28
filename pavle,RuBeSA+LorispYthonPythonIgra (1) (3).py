import pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Moon Escape")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color
    screen.fill((0, 0, 255))  # This fills the screen with blue
    pygame.display.update()

    # Player settings
    player_x = 370
    player_y = 480
    player_speed = 0.3

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
       
        # Moving the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed       
        # Fill the screen
        screen.fill((0, 0, 255))
       
        # Draw the player
        pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 50, 50))
    
        pygame.display.update()

pygame.quit()
