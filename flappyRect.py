import pygame
import random
pygame.init()
win = pygame.display.set_mode((1250,675))
pygame.display.set_caption('It\'ll be someday...')
x= 300
y= 335
x1 = 1250
rectSpeed = 3
jumpc = 10
isJump = False
score = 0
speed = 2
run = True
ran = random.randint(50,400)
x2 = 1250
while run:
    if x2 <= -100:
        x2 = x1
    x1 -= rectSpeed
    x2 -= rectSpeed
    y +=5
    keys = []
    pygame.time.delay(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        isJump = True
    if isJump:
        if jumpc >= -10:
            if jumpc < -2:
                y += (jumpc ** 2) /100
            else:
                y -= (jumpc ** 2) / 4
            jumpc -= 1
            y -= 5
        else:
            isJump = False
            jumpc = 10
    if (0 <= y <= ran and x1-50 <= x <= x1+150) or (ran+150<= y <= 675  and x1 - 50 <= x <= x1+150):
        run = False
    if x - 100 > x1:

        x1 = 1250
        score += 1
        print(score)
        rectSpeed += 1
        ran = random.randint(50,400)
    win.fill((92,177,230))
    pygame.draw.rect(win, (201,153,75), (x, y, 50, 50))
    pygame.draw.rect(win,(255,0,0),(x1,0,100,ran))
    pygame.draw.rect(win, (255, 0, 0), (x1, ran + 200, 100, 675 - ran-200))
    pygame.draw.rect(win, (255, 0, 0), (x2, 0, 100, ran))
    pygame.draw.rect(win, (255, 0, 0), (x2, ran + 200, 100, 675 - ran - 200))
    pygame.display.update()




