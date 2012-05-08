import pyglet
import config
from pyglet.gl import gl

class SpriteNotRegisteredError(Exception):
    def __init__(self, name):
        self.message = 'Missing spritesheet with name {}'.format(name)

class Sprite(pyglet.sprite.Sprite):
    def __init__(self,
                 img, x=0, y=0,
                 blend_src=gl.GL_SRC_ALPHA,
                 blend_dest=gl.GL_ONE_MINUS_SRC_ALPHA,
                 batch=None,
                 group=None,
                 usage='dynamic'):
        self.index = 0
        self.textures = img
        pyglet.sprite.Sprite.__init__(self, self.textures[self.index], x, y, blend_src, blend_dest, batch, group, usage)

    def set_frame(self, index):
        self.index = index
        self.image = self.textures[index]

class SpriteManager:
    def __init__(self):
        self.all = pyglet.graphics.Batch()
        self.textures = {}

    def register_spritesheet(self, sprite_config):
        print('Registering spritesheet {0}'.format(sprite_config.spritesheet_path))
        image = pyglet.resource.image(sprite_config.spritesheet_path)
        image_seq = pyglet.image.ImageGrid(image, sprite_config.rows, sprite_config.columns)
        self.textures[sprite_config] = pyglet.image.TextureGrid(image_seq)

    def is_registered(self, sprite_config):
        return sprite_config in self.textures

    def create(self, sprite_config, start_index=0):
        if not self.is_registered(sprite_config):
            raise SpriteNotRegisteredError(sprite_config.spritesheet_path)
        texture = self.textures[sprite_config]
#        anim_frames = [pyglet.image.AnimationFrame(img, 0.033) for img in texture]
#        anim = pyglet.image.Animation(anim_frames)
        sprite = Sprite(texture, batch=self.all)
        return sprite

sprite_manager = SpriteManager()
overlays = []

def init():
    gl.glClearColor(1, 1, 1, 1)
    for sheet in config.spritesheets:
        sprite_manager.register_spritesheet(sheet)

def draw():
    sprite_manager.all.draw()
    for overlay in overlays:
        overlay.draw()