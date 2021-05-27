import pygame, sys, random
from pygame.locals import *

w = 800
h = 600
introX = 
team1 = []
team2 = []

pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption ('Pokemon 3v3 sim')

while True:
    screen.fill(pygame.Color(0,0,0))

    while True:
        pygame.draw.rect(screen, pygame.Color, (800 ,0 , 
        introX = introX - 3

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
