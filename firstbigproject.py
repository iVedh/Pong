import pygame, sys

import random


screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pong with AI")

clock = pygame.time.Clock()

start_img = pygame.image.load("start_btn.png").convert_alpha()
quit_img = pygame.image.load("exit_btn.png").convert_alpha()
title_img = pygame.image.load("pong.png").convert_alpha()

player = pygame.Rect(10,50,50,10)
player.x = 225
player.y = 400

ai = pygame.Rect(10, 50, 50, 10)
ai.x = 225
ai.y = 50

line = pygame.Rect(5, 500, 500, 5)
line.x = 0
line.y = 237

ball = pygame.Rect(20,20,20,20)
ball.x = 240
ball.y = 230

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw(self):
        action = False
        
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
    
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
        
start_button = Button(190, 200, start_img, 0.5)
quit_button = Button(202, 350, quit_img, 0.5)
title_button = Button(145, 50, title_img, 0.2)

screencolor = (122, 211, 255)

playclicked = False

ml = False
mr = False

direction = "down"

xright = random.randint(50, 450)
xleft = random.randint(50, 450)

interval = 2

while True:
    
    clock.tick(60)
    
    screen.fill(screencolor)
    
    if playclicked == False:
        if start_button.draw():
            screencolor = (0, 0, 0)
            playclicked = True
        if quit_button.draw():
            pygame.quit()
            sys.exit()
        if title_button.draw():
            pass
    elif playclicked:
        screencolor = (0,0,0)
        pygame.draw.rect(screen, (255,255,255), player)
        pygame.draw.rect(screen, (255,255,255), ai)
        pygame.draw.rect(screen, (255,255,255), ball)
        pygame.draw.rect(screen, (255,255,255), line)
        
        if ball.colliderect(player):
            direction = "up"
        if ball.colliderect(ai):
            direction = "down"
        if direction == "up":
            ball.y -= 5
            ball.x += interval
            if ball.x >= xright:
                interval = -2
                xright = random.randint(200, 400)
            if ball.x <= xleft:
                interval = 2
                xleft = random.randint(50, 450)                         
        if direction == "down":
            ball.y += 5
            ball.x += interval
            if ball.x <= xright:
                interval = -2
                xright = random.randint(50, 450)
            if ball.x >= xleft:
                interval = 2
                xleft = random.randint(50, 450) 
        if ai.x >= ball.x:
            ai.x -= 5
        if ai.x <= ball.x:
            ai.x += 5
        if ball.x >= 480:
            interval = -2
        elif ball.x <= 20:
            interval = 2
        if ball.y >= 500:
            playclicked = False
            screencolor = (122, 211, 255)
        
    if ml:
        player.x -= 5
    if mr:
        player.x += 5
    
        
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ml = True
            if event.key == pygame.K_RIGHT:
                mr = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ml = False
            if event.key == pygame.K_RIGHT:
                mr = False
    
    pygame.display.update()