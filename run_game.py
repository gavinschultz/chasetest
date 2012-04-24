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
    renderer = render.Renderer()

    # main game loop
    while True:
        clock.tick(60)
        renderer.render()
        events.handle_events()

main()