import pygame
import characters
import events
import world
import render
import random

def main():
    pygame.init()
    clock = pygame.time.Clock()

    renderer = render.Renderer()
    myworld = world.World()

    all_sprites = pygame.sprite.Group()

    for i in range(20):
        horse = characters.Horse()
        horse.rect.top = random.randint(0,renderer.screen.get_rect().height - horse.rect.height)
        horse.rect.left = random.randint(0,renderer.screen.get_rect().width)
        horse.spritesheet.index = random.randint(0, len(horse.spritesheet.images)-1)
        horse.speed = random.randint(3,4)
        all_sprites.add(horse)

    renderer.add_sprite_group(all_sprites)

    # main game loop
    while True:
        clock.tick(60)
        for horse in all_sprites:
            horse.rect.left -= horse.speed
            if horse.rect.right < 0:
                horse.speed = random.randint(3,4)
                horse.rect.left = renderer.screen.get_rect().right
                horse.rect.top = random.randint(0,renderer.screen.get_rect().height - horse.rect.height)
        renderer.render()
        events.handle_events()

main()