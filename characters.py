import math
import os
import random
import pyglet
import render
import world
import config

class Horse(object):
    width = 64
    height = 64

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
        self._sprite.x = value

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value
        self._sprite.y = value

    @staticmethod
    def create_random():
        horse = Horse(config.BLEDAS_HORSE)
        horse.x = random.randint(0, world.rect.width - horse.width)
        horse.y = random.randint(0, world.rect.height - horse.height)
        horse.index = random.randint(0, 11)
        horse.speed = random.uniform(75.0, 100.0)
        return horse

    def __init__(self, sprite_config):
        self._sprite = sprite_config # render.sprite_manager.create(sprite_config)
        self.speed = 1
        self.frame_tick = 0
        self._x = 0
        self._y = 0
        self.index = 0

    def update(self, dt):
        self.advance_frame()

    def advance_frame(self):
        self.index += 1
        if self.index == 12:
            self.index = 0
        self._sprite.set_frame(self.index)
#        if self.index >= self.image_tex_seq.columns:
#            self.index = 0
#        self.sprite.image = self.image_tex_seq[self.index]
#        print self.index
#            self.sprite.image = self.sprite_sheet.next()