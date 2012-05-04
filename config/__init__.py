import render
from collections import namedtuple

SpriteConfig = namedtuple('SpriteConfig', 'spritesheet_path, rows, columns')

spritesheets = []

def add_spritesheet(spritesheet_path, rows, columns):
    item = SpriteConfig(spritesheet_path, rows, columns)
    spritesheets.append(item)
    return item

def install():
    for sheet in spritesheets:
        render.sprite_manager.register_spritesheet(sheet)