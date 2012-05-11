import math
import os
import random
import pyglet
import render
import world
import config
import itertools
from rect import Rect

class Horse(object):
    width = 64
    height = 64
    min_speed = 85.0
    max_speed = 200.0
    median_speed = ((min_speed + max_speed) / 2)
    
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
        self._sprite.x = value
        self.rect.left = value

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value
        self._sprite.y = value
        self.rect.bottom = value

    @staticmethod
    def create_random():
        horse = Horse(config.BLEDAS_HORSE)
        horse.x = random.randint(0, world.rect.width - horse.width)
        horse.y = random.randint(0, world.rect.height - horse.height)
        horse._sprite.set_frame(random.randint(0, len(horse._sprite.frames)-1))
        horse.speed = random.uniform(horse.min_speed, horse.max_speed)
        
#        horse._sprite.frames = [1/random.uniform(10.0, 40.0) for x in range(12)]
#        horse._sprite.register_frame_transform('random', [1/random.uniform(0.25, 2.0) for x in range(12)])
#        horse._sprite.register_frame_transform('front_emphases', [0.8, 0.8, 0.8, 3.1, 3.1, 3.1, 1.4, 1.4, 1.4, 1.1, 1.1, 1.1])
        horse._sprite.register_frame_transform('random with emphasis', Horse._random_with_emphasis())
        horse._sprite.register_frame_transform('speed', horse._random_by_speed())
        
        return horse

    @staticmethod
    def _random_with_emphasis():
        # build from 2 sets of fast triples and 2 sets of slow triples
        # good: SFSF 
        # okay: FFSS
        # bad: SFFS, FSSF
        fast_triplets = [[random.uniform(0.85, 0.9)] * 3, [random.uniform(0.9, 0.95)] * 3, [random.uniform(0.95, 1.0)] * 3]
        slow_triplets = [[random.uniform(1.0, 1.1)] * 3, [random.uniform(1.1, 1.15)] * 3, [random.uniform(1.15, 1.25)] * 3]
        items = [random.choice(fast_triplets), random.choice(fast_triplets), random.choice(slow_triplets), random.choice(slow_triplets)]
        random.shuffle(items)
        return list(itertools.chain(*items))
    
    def _random_by_speed(self):
        return [self.median_speed / (self.speed + ((self.median_speed - self.speed)/2))] * len(self._sprite.frames)

    def __init__(self, image):
        self._sprite = render.AnimatedSprite(image)
        render.register_sprite(self._sprite)
        self.speed = 1
        self.frame_tick = 0
        self._x = 0
        self._y = 0
        self.rect = Rect(self._x, self._y, self.width, self.width)

    def update(self, dt):
        self._sprite.animate(dt)