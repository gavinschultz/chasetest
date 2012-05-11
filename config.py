import pyglet
from render import AnimatedSprite
from rect import Rect

pyglet.resource.path = ['images']
pyglet.resource.reindex()

frames_per_second = 75.0
updates_per_second = 60.0
world_rect = Rect(0,0,1000,256)
window_rect = world_rect

_horse_basic1 = pyglet.resource.image('horse_skeleton_ss.png')
_bg_texture = pyglet.resource.image('bg1.png')

BLEDAS_HORSE = ('Bleda\'s Horse', _horse_basic1, 64, [1/30.0 for x in range(12)])
BG1 = _bg_texture

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