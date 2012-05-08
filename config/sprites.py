import config
from config import SpriteConfig, AnimationConfig, AnimationFrameConfig

ANIM_GALLOP_1 = config.add(AnimationConfig('Gallop 1', 'horse_skeleton_ss.png', 64,
    {
        1:AnimationFrameConfig(1/30.0),
        2:AnimationFrameConfig(1/30.0),
        3:AnimationFrameConfig(1/30.0),
        4:AnimationFrameConfig(1/30.0),
        5:AnimationFrameConfig(1/30.0),
        6:AnimationFrameConfig(1/30.0),
        7:AnimationFrameConfig(1/30.0),
        8:AnimationFrameConfig(1/30.0),
        9:AnimationFrameConfig(1/30.0),
        10:AnimationFrameConfig(1/30.0),
        11:AnimationFrameConfig(1/30.0),
        12:AnimationFrameConfig(1/30.0)
    }))
ANIM_GALLOP_2 = config.add(AnimationConfig('Gallop 1', 'horse_skeleton_ss.png', 64,
    {
        13:AnimationFrameConfig(1/30.0),
        14:AnimationFrameConfig(1/30.0),
        15:AnimationFrameConfig(1/30.0),
        16:AnimationFrameConfig(1/30.0),
        17:AnimationFrameConfig(1/30.0),
        18:AnimationFrameConfig(1/30.0),
        19:AnimationFrameConfig(1/30.0),
        20:AnimationFrameConfig(1/30.0),
        21:AnimationFrameConfig(1/30.0),
        22:AnimationFrameConfig(1/30.0),
        23:AnimationFrameConfig(1/30.0),
        24:AnimationFrameConfig(1/30.0)
    }))
BLEDAS_HORSE = config.add(SpriteConfig('Bleda\'s horse', 'horse_skeleton_ss.png', (ANIM_GALLOP_1,ANIM_GALLOP_2)))

class Animation:
    def __init__(self, name, spritesheet, frames, starting_index):
        self.name = name
        self.spritesheet = spritesheet
        self.frames = frames
        self.current_index = starting_index
        self.accumulator = 0.0

class AnimationFrame:
    def __init__(self, base_time, x, y, width, height):
        self.base_time = base_time
        self.transformed_timing = self.base_time
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __init__(self, base_time, size, index):
        pass

    def apply_timing_transformation(function):
        pass

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