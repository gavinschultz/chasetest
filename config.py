import pyglet
from render import AnimatedSprite
from rect import Rect
#import config
#from config import SpriteConfig, AnimationConfig, AnimationFrameConfig

pyglet.resource.path = ['images']
pyglet.resource.reindex()

frames_per_second = 75.0
updates_per_second = 60.0
world_rect = Rect(0,0,640,480)
window_rect = world_rect

_horse_basic1 = pyglet.resource.image('horse_skeleton_ss.png') 

BLEDAS_HORSE = AnimatedSprite('Gallop 1', _horse_basic1, 64, [1/30.0 for x in range(12)])
#config.add(BLEDAS_HORSE)
#ANIM_GALLOP_2 = AnimatedSprite('Gallop 2', _horse_basic1, 64,
#    {
#        13:AnimationFrameConfig(1/30.0),
#        14:AnimationFrameConfig(1/30.0),
#        15:AnimationFrameConfig(1/30.0),
#        16:AnimationFrameConfig(1/30.0),
#        17:AnimationFrameConfig(1/30.0),
#        18:AnimationFrameConfig(1/30.0),
#        19:AnimationFrameConfig(1/30.0),
#        20:AnimationFrameConfig(1/30.0),
#        21:AnimationFrameConfig(1/30.0),
#        22:AnimationFrameConfig(1/30.0),
#        23:AnimationFrameConfig(1/30.0),
#        24:AnimationFrameConfig(1/30.0)
#    })
#BLEDAS_HORSE = config.add(SpriteConfig('Bleda\'s horse', 'horse_skeleton_ss.png', (ANIM_GALLOP_1,)))

#class Animation:
#    def __init__(self, name, spritesheet, frames, starting_index):
#        self.name = name
#        self.spritesheet = spritesheet
#        self.frames = frames
#        self.current_index = starting_index
#        self.accumulator = 0.0
#
#class AnimationFrame:
#    def __init__(self, base_time, x, y, width, height):
#        self.base_time = base_time
#        self.transformed_timing = self.base_time
#        self.x = x
#        self.y = y
#        self.width = width
#        self.height = height
#
#    def __init__(self, base_time, size, index):
#        pass
#
#    def apply_timing_transformation(function):
#        pass

##horse
##    animation 1 - name = 'gallop 1', spritesheet = 'horse_skeleton_ss.png'
##        frame 1 - index 1 - base_time = 1/30.0 - transformed_timing = 1/30.0
##        frame 2 - index 2 - base_time = 1/30.0 - transformed_timing = 1/30.0
##        frame 3 - index 3
##        frame 4 - index 4
##        frame 5 - index 5
##        frame 6 - index 6
##        frame 7 - index 7
##        frame 8 - index 8
##        frame 9 - index 9
##        frame 10 - index 10
##        frame 11 - index 11
##        frame 12 - index 12
##    animation 2 - name = 'gallop 2', spritesheet = 'horse_skeleton_ss.png'
##        frame 1 - index 13
##        frame 2 - index 14
##        frame 3 -
##        frame 4 -
##        frame 5 -
##        frame 6 -
##        frame 7 -
##        frame 8 -
##        frame 9 -
##        frame 10 -
##        frame 11 -
##        frame 12 -
##    animation 3 - 'trot 1'
##    animation 4 - 'trot 2'