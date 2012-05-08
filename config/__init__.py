import render
from collections import namedtuple
from rect import Rect

## EDITABLE ITEMS -------------------------------------------

frames_per_second = 75.0
updates_per_second = 60.0
world_rect = Rect(0,0,640,480)
window_rect = world_rect

## ----------------------------------------------------------

SpriteConfig = namedtuple('SpriteConfig', 'spritesheet_path, rows, columns')

spritesheets = []

def add(config_item):
    if isinstance(config_item, SpriteConfig):
        return add_spritesheet(config_item)

def add_spritesheet(item):
    spritesheets.append(item)
    return item