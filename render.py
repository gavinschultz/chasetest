import pyglet

class SpritesheetRegistrationError(Exception):
    def __init__(self, name):
        self.message = 'Missing spritesheet with name {}'.format(name)

class Sprite(pyglet.sprite.Sprite):
    pass

class SpriteManager:
    def __init__(self):
        self.all = pyglet.graphics.Batch()
        self._ss_dic = {}

    def register_spritesheet(self, path, rows, columns):
        if path in self._ss_dic:
            return
        image = pyglet.image.load('images/horse_skeleton_ss.png')
        image_seq = pyglet.image.ImageGrid(image, rows, columns)
        self._ss_dic[path] = pyglet.image.TextureGrid(self.image_seq)

    def create(self, spritesheet_path, start_index=0):
        if spritesheet_path not in self._ss_dic:
            raise SpritesheetRegistrationError
        image = _ss_dic[spritesheet_path]
        sprite = pyglet.sprite.Sprite(image, batch=sprite_manager.all)
        return sprite

sprite_manager = SpriteManager()

def draw():
    sprite_manager.all.draw()