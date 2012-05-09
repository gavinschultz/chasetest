import characters
import config
import random
from rect import Rect

horses = []
rect = Rect(0,0,0,0)

def init():
    global rect
    rect = config.world_rect
    for i in range(2):
        horses.append(characters.Horse.create_random())

def set_rect(new_rect):
    global rect
    rect = new_rect

def update(dt):
    for horse in horses:
        horse.x -= horse.speed * dt
        if horse.x + horse.width < 0:
            horse.speed = random.uniform(horse.min_speed, horse.max_speed)
            horse.x = rect.width
            horse.y = random.randint(0, rect.height - horse.height)
        horse.update(dt)