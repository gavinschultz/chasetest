import math
import os
import random
import pyglet
import render

class Horse():
    width = 64
    height = 64
    spritesheet_path = 'images/horse_skeleton_ss.png'
    render.sprite_manager.register_spritesheet(spritesheet_path, 1, 12)

    @staticmethod
    def create_random():
        horse = Horse()
        horse.x = random.randint(0, window.width - horse.width)
        horse.y = random.randint(0, window.height - horse.height)
        horse.index = random.randint(0, horse.image_tex_seq.columns-1)
        horse.speed = random.uniform(3.0, 4.5)
        return horse

    def __init__(self, image):
        self._sprite = render.sprite_manager.create(Horse.spritesheet_path)
        self.speed = 0
        self.frame_tick = 0
        self.x = 0
        self.y = 0
        self.index = 0
        self.image = self.image_tex_seq[self.index]
        self.tick = 0

    def update(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.tick += 1
        if self.tick > 1:
            self.tick = 0
            return
        self.advance_frame()

    def advance_frame(self):
        self.index += 1
#        if self.index >= self.image_tex_seq.columns:
#            self.index = 0
#        self.sprite.image = self.image_tex_seq[self.index]
#        print self.index
#            self.sprite.image = self.sprite_sheet.next()