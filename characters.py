import math

__author__ = 'gavin.schultz-ohkubo'

class Horse:
    def __init__(self):
        self.pos = [0, 0]
        self.velocity = [0, 0]
        self.box = [0,0, 0,0] # bottom, left, top, right
