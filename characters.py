import math
import os
import pygame

__author__ = 'gavin.schultz-ohkubo'

class SpriteSheet:
    def __init__(self, path, dimensions):
        self.sheet = pygame.image.load(path).convert_alpha()
#        print self.sheet, self.sheet.get_at((0,0))
        self.dimensions = dimensions
        self.images = self.get_all_images()
        self.index = 0

    def get_all_images(self):
        images = []
        for i, r in enumerate(range(0, self.sheet.get_rect().width, self.dimensions[0])):
            rect = pygame.Rect((r, 0), (self.dimensions[0], self.dimensions[1]))
#            print i, rect, self.dimensions
            image = pygame.Surface(self.dimensions, pygame.SRCALPHA, 32)
#            print image
            image.blit(self.sheet, (0,0), rect)
            image.convert_alpha()
#            image.set_alpha(self.sheet.get_alpha())
#            image.set_colorkey(self.sheet.get_at((0,0)), pygame.RLEACCEL)
#            pygame.image.save()
            images.append(image)
        return images

    def current(self):
        return self.images[self.index]

    def next(self):
        if self.index == len(self.images) - 1:
            self.index = 0
        else:
            self.index += 1
        return self.current()

class Horse(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        dimensions = (64, 64)
        self.rect = pygame.Rect((0, 0), dimensions)
        self.spritesheet = SpriteSheet(os.path.join('images', 'horse_skeleton_ss.png'), dimensions)
        self.speed = 1
        self.frame_tick = 0
        self.image = self.spritesheet.current()

    def update(self):
        self.advance_frame()

    def advance_frame(self):
        self.frame_tick += 1
        if self.frame_tick == 2:
            self.frame_tick = 0
            self.image = self.spritesheet.next()