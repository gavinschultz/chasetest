import math
import os
import random
import pyglet
import render
import config.sprites

class Horse():
    width = 64
    height = 64

    @staticmethod
    def create_random():
        horse = Horse(config.sprites.BLEDAS_HORSE)
        horse.x = random.randint(0, 640 - horse.width)
        horse.y = random.randint(0, 480 - horse.height)
        horse._sprite.index = random.randint(0, 11)
        horse.speed = random.uniform(3.0, 4.5)
        return horse

    def __init__(self, sprite_config):
        self._sprite = render.sprite_manager.create(sprite_config)
        self.speed = 0
        self.frame_tick = 0
        self.x = 0
        self.y = 0
        self.index = 0
        self.image = self._sprite.image
        self.tick = 0

    def update(self):
        self.tick += 1
        if self.tick > 1:
            self.tick = 0
            return
        self.advance_frame()

    def advance_frame(self):
        self.index += 1
        self._sprite.set_frame(self.index)
#        if self.index >= self.image_tex_seq.columns:
#            self.index = 0
#        self.sprite.image = self.image_tex_seq[self.index]
#        print self.index
#            self.sprite.image = self.sprite_sheet.next()