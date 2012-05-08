import render
from collections import namedtuple
from rect import Rect

## EDITABLE ITEMS -------------------------------------------

frames_per_second = 75.0
updates_per_second = 60.0
world_rect = Rect(0,0,640,480)
window_rect = world_rect

## ----------------------------------------------------------

SpriteConfig = namedtuple('SpriteConfig', 'name, image_path, animations')
AnimationConfig = namedtuple('AnimationConfig', 'name, spritesheet, size, frames')
AnimationFrameConfig = namedtuple('AnimationFrameConfig', 'base_time')

spritesheets = []
##animations = []

def add(config_item):
    if isinstance(config_item, SpriteConfig):
        return add_spritesheet(config_item)
##    elif isinstance(config_item, AnimationConfig):
##        return add_animation(config_item)

def add_spritesheet(item):
    spritesheets.append(item)
    return item

##def add_animation(item):
##    animations.append(item)
##    return item