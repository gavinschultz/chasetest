import pygame
from pygame.locals import *
import sys

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
            sys.exit(0)
        else:
            pass
#            print event