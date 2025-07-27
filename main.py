# Example file showing a circle moving on screen
import pygame
import util

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
screenwidth = screen.get_width()
screenheight = screen.get_height()

centerpoint = screenwidth / 2
middlepoint = screenheight / 2

player_pos = pygame.Vector2(centerpoint, middlepoint)
linestartpos = pygame.Vector2(centerpoint, 0)
lineendpos = pygame.Vector2(centerpoint, screenheight)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    
    color = util.getColor(player_pos, centerpoint)
    
    pygame.draw.line(screen, "black", linestartpos, lineendpos, width=1)
   
    
    bluebase = pygame.draw.rect(screen, "blue", [20, middlepoint - 60, 60, 120], 3)
    redbase = pygame.draw.rect(screen, "red", [screenwidth - 80, middlepoint - 60, 60, 120], 3)
    bf1 = pygame.draw.rect(screen, "blue", [50, middlepoint - 40, 24, 16], 120)
    bf2 = pygame.draw.rect(screen, "blue", [30, middlepoint - 8, 24, 16], 120)
    bf3 = pygame.draw.rect(screen, "blue", [50, middlepoint + 24, 24, 16], 120)
    rf1 = pygame.draw.rect(screen, "red", [screenwidth - 72, middlepoint - 40, 24, 16], 120)
    rf2 = pygame.draw.rect(screen, "red", [screenwidth - 56, middlepoint - 8, 24, 16], 120)
    rf3 = pygame.draw.rect(screen, "red", [screenwidth - 72, middlepoint + 24, 24, 16], 120)

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
        player_pos.y -= 1
    elif player_pos.x < 1:
        player_pos.x += 1
    elif player_pos.x > screenwidth - 5:
        player_pos.x -= 1
        print(screenwidth)

    print("player_pos.x:", player_pos.x, "bf1.x: ", bf1.x)
    print("player_pos.y:", player_pos.y, "bf1.y: ", bf1.y)

    dragging = False
    
    # Check for dragging
    if player_pos.x > bf1.x and player_pos.x < bf1.x + 24 and player_pos.y > bf1.y and player_pos.y < bf1.y + 16:
        if keys[pygame.K_SPACE]:
            dragging_flag = True

    if not keys[pygame.K_SPACE]:
        dragging_flag = False

    if dragging_flag:
        bf1 = pygame.draw.rect(screen, "blue", [player_pos.x, player_pos.y, 24, 16], 120)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()