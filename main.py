# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
screenwidth = screen.get_width()
screenheight = screen.get_height()

centerpoint = screenwidth / 2

player_pos = pygame.Vector2(centerpoint, screenheight / 2)
linestartpos = pygame.Vector2(centerpoint, 0)
lineendpos = pygame.Vector2(centerpoint, screenheight)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    
    if player_pos.x > centerpoint:
        color = (0, 200, 0)
    else:
        color = (0, 255, 0)

    pygame.draw.line(screen, "black", linestartpos, lineendpos, width=1)
    player = pygame.draw.circle(screen, color, player_pos, 10)

    speed = 120
    keys = pygame.key.get_pressed()
    if player_pos.y > 0 and player_pos.x > 0 and player_pos.y < screenheight and player_pos.x < screenwidth:
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player_pos.y -= speed * dt
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player_pos.y += speed * dt
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_pos.x -= speed * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_pos.x += speed * dt
    elif player_pos.y < 1:
        player_pos.y += 1
    elif player_pos.y > screenheight - 5:
        #player_pos.y = player_pos.y
        player_pos.y -= 1
    elif player_pos.x < 1:
        player_pos.x += 1
    elif player_pos.x > screenwidth - 5:
        player_pos.x -= 1
        print(screenwidth)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()