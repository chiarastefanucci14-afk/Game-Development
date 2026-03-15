import pygame

#1. Initialize pgame
pygame.init()
#2. Create game window
WIDTH, HEIGHT= 600, 400
screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Press the right and left key arrows to move the box.")
#3. Colors
PURPLE= (255,0,0)
BLUE= (173,216,230)
#4. Square properties
x= 250
y= 150
size= 50
speed= 2
#5. Game Loop
running= True
while running:
    screen.fill(BLUE)
    pygame.draw.rect(screen, PURPLE, (x,y,size,size))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys= pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < WIDTH - size:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < HEIGHT - size:
        y += speed
    pygame.display.update()
pygame.quit()