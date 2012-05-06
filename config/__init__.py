import render
from collections import namedtuple

SpriteConfig = namedtuple('SpriteConfig', 'spritesheet_path, rows, columns')

class AnimationConfig:


spritesheets = []

def add(config_item):
    pass

def add_spritesheet(spritesheet_path, rows, columns):
    item = SpriteConfig(spritesheet_path, rows, columns)
    spritesheets.append(item)
    return item

##def add_animation(sprite_config, name, cells, )

def install():
    for sheet in spritesheets:
        render.sprite_manager.register_spritesheet(sheet)