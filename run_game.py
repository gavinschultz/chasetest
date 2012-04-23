import pygame
import characters
import events
import world
import render

def main():
    pygame.init()
    clock = pygame.time.Clock()

    myworld = world.World()
    horse = characters.Horse()

    screen = render.init()

    # main game loop
    while True:
        clock.tick(60)
        render.render(screen)
        events.handle_events()

main()