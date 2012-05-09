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
    min_speed = 75.0
    max_speed = 120.0

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
        horse.index = random.randint(0, len(horse._sprite.frames))
        horse.speed = random.uniform(horse.min_speed, horse.max_speed)
        return horse

    def __init__(self, sprite_config):
        self._sprite = render.AnimatedSprite(sprite_config)
        render.register_sprite(self._sprite)
        self.speed = 1
        self.frame_tick = 0
        self._x = 0
        self._y = 0
        self.index = 0

    def update(self, dt):
        self._sprite.animate(dt)