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
font = pygame.font.SysFont('Monospace', 15)

centerpoint = screenwidth / 2
middlepoint = screenheight / 2

player_pos = pygame.Vector2(centerpoint, middlepoint)
linestartpos = pygame.Vector2(centerpoint, 0)
lineendpos = pygame.Vector2(centerpoint, screenheight)
bf1c = pygame.Vector2(50, middlepoint - 40)
bf2c = pygame.Vector2(30, middlepoint - 8)
bf3c = pygame.Vector2(50, middlepoint + 24)
rf1c = pygame.Vector2(screenwidth - 72, middlepoint - 40)
rf2c = pygame.Vector2(screenwidth - 56, middlepoint - 8)
rf3c = pygame.Vector2(screenwidth - 72, middlepoint + 24)
flags_captured_blue = 0
flags_captured_red = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    
    color = util.getColor(player_pos, centerpoint)
    statusblue = f"Score: {flags_captured_blue}"
    statusred = f"Score: {flags_captured_red}"
    text_width, text_height = font.size(statusred)
    # Begin:: Start calculating the score
    pygame.draw.line(screen, "black", linestartpos, lineendpos, width=1)
    textblue = font.render(statusblue, True, 'black')
    textred = font.render(statusred, True, 'black')

    bluebase = pygame.draw.rect(screen, "blue", [20, middlepoint - 60, 120, 120], 1)
    redbase = pygame.draw.rect(screen, "red", [screenwidth - 140, middlepoint - 60, 120, 120], 1)
    bf1 = pygame.draw.rect(screen, "blue", [bf1c.x, bf1c.y, 24, 16])
    bf2 = pygame.draw.rect(screen, "blue", [bf2c.x, bf2c.y, 24, 16])
    bf3 = pygame.draw.rect(screen, "blue", [bf3c.x, bf3c.y, 24, 16])
    rf1 = pygame.draw.rect(screen, "red", [rf1c.x, rf1c.y, 24, 16])
    rf2 = pygame.draw.rect(screen, "red", [rf2c.x, rf2c.y, 24, 16])
    rf3 = pygame.draw.rect(screen, "red", [rf3c.x, rf3c.y, 24, 16])

    player = pygame.draw.circle(screen, color, player_pos, 10)
    
    screen.blit(textblue, (2, 2))
    screen.blit(textred, (screenwidth - (text_width + 2), 2))

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
    
    # Begin::Check whether flags are in place
    
    rf1cd = False
    rf2cd = False
    rf3cd = False
    bf1cd = False
    bf2cd = False
    bf3cd = False
    

    if util.checkflagcap(rf1.x, rf1.y, bluebase.x, bluebase.y):
        rf1cd = True
    if util.checkflagcap(rf2.x, rf2.y, bluebase.x, bluebase.y):
        rf2cd = True
    if util.checkflagcap(rf3.x, rf3.y, bluebase.x, bluebase.y):
        rf3cd = True
    
    if util.checkflagcap(bf1.x, bf1.y, redbase.x, redbase.y):
        bf1cd = True
    if util.checkflagcap(bf2.x, bf2.y, redbase.x, redbase.y):
        bf2cd = True
    if util.checkflagcap(bf3.x, bf3.y, redbase.x, redbase.y):
        bf3cd = True
    
    # Count the score accordingly
    
    if rf1cd and rf2cd and rf3cd:
        flags_captured_blue = 3
        print("Blue Win")
    elif (rf1cd and rf2cd) or (rf1cd and rf3cd) or (rf2cd and rf3cd):
        flags_captured_blue = 2
    elif rf1cd or rf2cd or rf3cd:
        flags_captured_blue = 1
    else:
        flags_captured_blue = 0
    
    if bf1cd and bf2cd and bf3cd:
        flags_captured_red = 3
        print("Red Win")
    elif (bf1cd and rf2cd) or (bf1cd and bf3cd) or (bf2cd and bf3cd):
        flags_captured_red = 2
    elif bf1cd or bf2cd or bf3cd:
        flags_captured_red = 1
    else:
        flags_captured_red = 0
    
    # End::Check whether flags are in place
    
    # Check whether we are dragging a flag
    dragging = False

    dbf1 = False
    if player_pos.x > bf1.x and player_pos.x < bf1.x + 24 and player_pos.y > bf1.y and player_pos.y < bf1.y + 16 and not dragging:
        if keys[pygame.K_SPACE]:
            dbf1 = True
            dragging = True
    if not keys[pygame.K_SPACE]:
        dbf1 = False
        dragging = False
    if dbf1:
        bf1c = pygame.Vector2(player_pos.x - 12, player_pos.y - 8)

    dbf2 = False
    if player_pos.x > bf2.x and player_pos.x < bf2.x + 24 and player_pos.y > bf2.y and player_pos.y < bf2.y + 16 and not dragging:
        if keys[pygame.K_SPACE]:
            dbf2 = True
            dragging = True
    if not keys[pygame.K_SPACE]:
        dbf2 = False
        dragging = False
    if dbf2:
        bf2c = pygame.Vector2(player_pos.x - 12, player_pos.y - 8)

    dbf3 = False
    if player_pos.x > bf3.x and player_pos.x < bf3.x + 24 and player_pos.y > bf3.y and player_pos.y < bf3.y + 16 and not dragging:
        if keys[pygame.K_SPACE]:
            dbf3 = True
            dragging = True
    if not keys[pygame.K_SPACE]:
        dbf3 = False
        dragging = False
    if dbf3:
        bf3c = pygame.Vector2(player_pos.x - 12, player_pos.y - 8)
    
    drf1 = False
    if player_pos.x > rf1.x and player_pos.x < rf1.x + 24 and player_pos.y > rf1.y and player_pos.y < rf1.y + 16 and not dragging:
        if keys[pygame.K_SPACE]:
            drf1 = True
            dragging = True
    if not keys[pygame.K_SPACE]:
        drf1 = False
        dragging = False
    if drf1:
        rf1c = pygame.Vector2(player_pos.x - 12, player_pos.y - 8)
    
    drf2 = False
    if player_pos.x > rf1.x and player_pos.x < rf2.x + 24 and player_pos.y > rf2.y and player_pos.y < rf2.y + 16 and not dragging:
        if keys[pygame.K_SPACE]:
            drf2 = True
            dragging = True
    if not keys[pygame.K_SPACE]:
        drf2 = False
        dragging = False
    if drf2:
        rf2c = pygame.Vector2(player_pos.x - 12, player_pos.y - 8)
    
    drf3 = False
    if player_pos.x > rf3.x and player_pos.x < rf3.x + 24 and player_pos.y > rf3.y and player_pos.y < rf3.y + 16 and not dragging:
        if keys[pygame.K_SPACE]:
            drf3 = True
            dragging = True
    if not keys[pygame.K_SPACE]:
        drf3 = False
        dragging = False
    if drf3:
        rf3c = pygame.Vector2(player_pos.x - 12, player_pos.y - 8)

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()