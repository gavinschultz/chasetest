import pyglet
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
#        self.textures = img
        pyglet.sprite.Sprite.__init__(self, img, x, y, blend_src, blend_dest, batch, group, usage)

    def set_frame(self, index):
        self.index = index
#        self.image = self.textures[index]

class SpriteManager:
    def __init__(self):
        self.all = pyglet.graphics.Batch()
        self.textures = {}

    def register_spritesheet(self, sprite_config):
        print('Registering spritesheet {}'.format(sprite_config.spritesheet_path))
        image = pyglet.image.load(sprite_config.spritesheet_path)
        image_seq = pyglet.image.ImageGrid(image, sprite_config.rows, sprite_config.columns)
        self.textures[sprite_config] = pyglet.image.TextureGrid(image_seq)

    def is_registered(self, sprite_config):
        return sprite_config in self.textures

    def create(self, sprite_config, start_index=0):
        if not self.is_registered(sprite_config):
            raise SpriteNotRegisteredError(sprite_config.spritesheet_path)
        texture = self.textures[sprite_config]
        anim_frames = [pyglet.image.AnimationFrame(img, 0.033) for img in texture]
        anim = pyglet.image.Animation(anim_frames)
        sprite = Sprite(anim, batch=self.all)
        return sprite

sprite_manager = SpriteManager()

def draw():
    sprite_manager.all.draw()