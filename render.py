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
        cell_count = spritesheet.width // size
        
        self.name = name
        self.spritesheet = spritesheet
        self.dt_accumulator = 0.0
        self.frames = frames
        self.current_frame = starting_frame
        self.frame_transforms = {}
        self.spritesheet = pyglet.image.ImageGrid(spritesheet, 1, cell_count).get_texture_sequence()
        
        pyglet.sprite.Sprite.__init__(self, self.spritesheet[self.current_frame], 0, 0, blend_src, blend_dest, batch, group, usage)

    def register_frame_transform(self, name, frame_transform):
        self.frame_transforms[name] = frame_transform

    def set_frame(self, frame):
        self.current_frame = frame
        self.image = self.spritesheet[frame] 
    
    def animate(self, dt):
        frames = self.frames
#        print frames
        for frame_transform in self.frame_transforms.values():
            frames = [a*b for a, b in zip(frames, frame_transform)]
#        print frames
        self.dt_accumulator += dt
        frame_increment, self.dt_accumulator = divmod(self.dt_accumulator, frames[self.current_frame])
        self.set_frame(int(divmod(self.current_frame + frame_increment, len(frames)-1)[1]))
#        print((dt, self.dt_accumulator, frame_increment, self.current_frame)) 

overlays = pyglet.graphics.Batch()
sprites = pyglet.graphics.Batch()

def register_sprite(sprite):
    sprite.batch = sprites
    
def register_overlay(overlay):
    overlay.batch = overlays

def init():
    gl.glClearColor(1, 1, 1, 1)

def draw():
    sprites.draw()
    overlays.draw()