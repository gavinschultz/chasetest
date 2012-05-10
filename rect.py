from collections import namedtuple

Point = namedtuple('Point', 'x y')

class Rect:
    def __init__(self, left, bottom, width, height):
        self.left = left
        self.bottom = bottom
        self.width = width
        self.height = height
    
    @property
    def right(self):
        return self.left + self.width
    
    @property
    def top(self):
        return self.bottom + self.height
    
    def includes(self, x, y):
        return (x > self.left and x < self.right and y > self.bottom and y < self.top)
    
    def __repr__(self):
        return repr((self.left, self.bottom, self.width, self.height))