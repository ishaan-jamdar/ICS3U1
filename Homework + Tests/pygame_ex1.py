import pygame, sys
from pygame.locals import *
import random

def drawSm(x,y,r):
    #floor
    pygame.draw.rect(screen, pygame.Color(250,252,254), (0,y+r*5,800,400))
    #snowman circles
    pygame.draw.circle(screen, pygame.Color(250,252,254), (x,y), r)
    pygame.draw.circle(screen, pygame.Color(250,252,254), (x,y+r*2), r2)
    pygame.draw.circle(screen, pygame.Color(250,252,254), (x,y+r*4), r3)
    #eyes
    pygame.draw.circle(screen, pygame.Color(57,45,45), (int(x-20),int(y/1.05)), int(r/7))
    pygame.draw.circle(screen, pygame.Color(57,45,45), (int(x+20),int(y/1.05)), int(r/7))
    #carrot/nose
    pygame.draw.polygon(screen, pygame.Color(255,149,0), [(int(x-8),int(y*1.02)),(int(x+8),int(y*1.02)),(x,int(y*1.12))])
    #hat
    pygame.draw.rect(screen, pygame.Color(0,0,0), (int(x-r),y-r,r*2,10))
    pygame.draw.rect(screen, pygame.Color(0,0,0), (int(x-r*0.75),y-r-75,r*1.575,75))
    pygame.draw.rect(screen, pygame.Color(255,0,0), (int(x-r*0.75),y-r-10,r*1.575,10))
    #buttons
    pygame.draw.circle(screen, pygame.Color(57,45,45), (x, y+60), int(r/7))
    pygame.draw.circle(screen, pygame.Color(57,45,45), (x, y+90), int(r/7))
    pygame.draw.circle(screen, pygame.Color(57,45,45), (x, y+120), int(r/7))

w = 800
h = 600
xinc = 0
yinc = 0
x = 400
y = 200
r = 50
r2 = int(r*1.25)
r3 = int(r2*1.25)

pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption ('Snowmandem')

flakes = []

for i in range (50):
    flakes.append([random.randint(1,w),random.randint(1,h), random.randint(1,5)])

#main loop                        
while True:
    
    screen.fill (pygame.Color(194,223,252))

    #draws the snowman using the function
    print (drawSm(x,y,r))
    
    x = x + xinc
    #moves the x value to the otherside meaning once the snowman hits the side of the screen it will appear on the otherside of the screen
    if x < -78:
        x = 878
    elif x > 878:
        x = -78
    y = y + yinc
    #exit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == KEYDOWN):
            #increases x value, moving the snowman (moves slower when yinc value is 1)
            if (event.key == K_d):
                xinc = 3
                if yinc == 1:
                    xinc = 1
            #decreases x value, moving the snowman (moves slower when yinc value is 1)
            if (event.key == K_a):
                xinc = -3
                if yinc == 1:
                    xinc = -1
            #changes the yinc value which will turn the floor to lava
            if (event.key == K_s):
                yinc = 1
        if (event.type == KEYUP):
            xinc = 0
    
    #draws each snowflake
    for i in range (len(flakes)):
        pygame.draw.circle(screen, pygame.Color(250,252,254), (flakes[i][0],flakes[i][1]), 10)
        flakes[i][1] = flakes[i][1] + flakes[i][2]
        if (flakes[i][1] > h):
            flakes[i][1] = 0
            flakes[i][0] = random.randint(1,w)
            
    #the floor is lava!(Below snowflakes so it appears they melt once they hit it)
    if yinc == 1:
        pygame.draw.rect(screen, (pygame.Color(255,0,0)), (0,450,800,400))
        pygame.draw.rect(screen, (pygame.Color(255,165,0)),(22,475,160,10))
        pygame.draw.rect(screen, (pygame.Color(255,165,0)),(102,525,128,10))
        pygame.draw.rect(screen, (pygame.Color(255,165,0)),(34,575,156,10))
        pygame.draw.rect(screen, (pygame.Color(255,165,0)),(348,483,151,10))
        pygame.draw.rect(screen, (pygame.Color(255,165,0)),(328,522,116,10))
        pygame.draw.rect(screen, (pygame.Color(255,165,0)),(367,575,129,10))
        pygame.draw.rect(screen, (pygame.Color(255,165,0)),(591,551,154,10))
        pygame.draw.rect(screen, (pygame.Color(255,165,0)),(602,485,197,10))
        pygame.draw.rect(screen, (pygame.Color(255,165,0)),(613,589,164,10))
    
    pygame.display.update()
    fpsClock.tick(60)

