import render
from collections import namedtuple

SpriteConfig = namedtuple('SpriteConfig', 'spritesheet_path, rows, columns')

class AnimationConfig:
    pass

spritesheets = []

def add(config_item):
    if isinstance(config_item, SpriteConfig):
        return add_spritesheet(config_item)

def add_spritesheet(item):
#    item = SpriteConfig(s.spritesheet_path, rows, columns)
    spritesheets.append(item)
    return item

##def add_animation(sprite_config, name, cells, )

def install():
    for sheet in spritesheets:
        render.sprite_manager.register_spritesheet(sheet)