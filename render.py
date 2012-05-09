import pyglet
from pyglet.gl import gl

class SpriteNotRegisteredError(Exception):
    def __init__(self, name):
        self.message = 'Missing spritesheet with name {}'.format(name)

class AnimatedSprite(pyglet.sprite.Sprite):
    def __init__(self,
                 (name, spritesheet, size, frames),
                 starting_frame=0,
                 blend_src=gl.GL_SRC_ALPHA,
                 blend_dest=gl.GL_ONE_MINUS_SRC_ALPHA,
                 batch=None,
                 group=None,
                 usage='dynamic'):
        self.name = name
        self.spritesheet = spritesheet
        self.size = size
        self.dt_accumulator = 0.0
        self.frames = frames
        self.current_frame = starting_frame
        
        cell_count = spritesheet.width // size
        self.spritesheet = pyglet.image.ImageGrid(spritesheet, 1, cell_count).get_texture_sequence()
#        self._set_texture(pyglet.image.TextureGrid(image_seq))
        
        pyglet.sprite.Sprite.__init__(self, self.spritesheet[self.current_frame], 0, 0, blend_src, blend_dest, batch, group, usage)

    def set_frame(self, frame):
        self.current_frame = frame
        self.image = self.spritesheet[frame]
        
    def animate(self, dt):
        self.dt_accumulator += dt
        frame_increment, self.dt_accumulator = divmod(self.frames[self.current_frame], dt)
        self.current_frame = int(divmod(self.current_frame + frame_increment, len(self.frames)-1)[0])
        print((dt, self.dt_accumulator, frame_increment, self.current_frame)) 

class SpriteManager:
    def __init__(self):
        self.all = pyglet.graphics.Batch()
        self.texture = {}

    def register_sprite(self, sprite_config):
        print('Registering sprite {0}'.format(sprite_config.name))
#        image = pyglet.resource.image(sprite_config.image_path)
        

    def is_registered(self, sprite_config):
        return sprite_config in self.texture

    def create(self, sprite_config, start_index=0):
        pass
#        if not self.is_registered(sprite_config):
#            raise SpriteNotRegisteredError(sprite_config.image_path)
#        texture = self.texture[sprite_config]
#        anim_frames = [pyglet.image.AnimationFrame(img, 0.033) for img in texture]
#        anim = pyglet.image.Animation(anim_frames)
#        sprite = AnimatedSprite(texture, batch=self.all)
#        return sprite

sprite_manager = SpriteManager()
overlays = []
sprites = pyglet.graphics.Batch()

def register_sprite(sprite):
    sprite.batch = sprites

def init():
    gl.glClearColor(1, 1, 1, 1)
#    for sheet in config.spritesheets:
#        sprite_manager.register_sprite(sheet)

def draw():
#    sprite_manager.all.draw()
    sprites.draw()
    for overlay in overlays:
        overlay.draw()