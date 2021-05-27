# import libraries
import pygame, sys, time, random
from pygame.locals import *

# global variables
width = 800
height = 600
# (x, y, dir_x, dir_y)
balls = [[random.randint(10,width - 10), random.randint(10,height - 10), random.randint(1, 10), random.randint(1,10), pygame.Color(255,0,0)]]
r = 10

# initialization
pygame.init()
fpsClock = pygame.time.Clock()
windowSurfaceObject = pygame.display.set_mode((width,height))
pygame.display.set_caption ("Bounce - multiples")

# main loop
while True:
    # check for window driven events
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    # fill the screen with white           
    windowSurfaceObject.fill (pygame.Color(255,255,255))

    for ball in balls:
        # modify the location
        ball[0] = ball[0] + ball[2]
        ball[1] = ball[1] + ball[3]

        if ball[0] + r > width or ball[0] - r < 0:
            ball[2] = ball[2] * -1
            balls.append([random.randint(10, width - 10), random.randint(10, height - 10), random.randint(1, 10),random.randint(1, 10), pygame.Color((255), random.randint(0,50), random.randint(0, 50))])
            print (len(balls))
        if ball[1] + r > height or ball[1] - r < 0:
            ball[3] = ball[3] * -1

        # draw the ball
        pygame.draw.circle(windowSurfaceObject, ball[4],(ball[0],ball[1]),r)

    # update the screen
    pygame.display.update()
    # frames per second
    fpsClock.tick(60)
