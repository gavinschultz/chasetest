import pyglet
from pyglet.window import key
import random
import characters
import profile
import render
import config

window = pyglet.window.Window()
pyglet.gl.glClearColor(1, 1, 1, 1)

all_horses = []
fps_display = pyglet.clock.ClockDisplay()

config.install()

for i in range(10):
    all_horses.append(characters.Horse.create_random())

def update(dt):
    for horse in all_horses:
        horse.x -= horse.speed
        if horse.x + horse.width < 0:
            horse.speed = random.uniform(3.0, 4.5)
            horse.x = window.width
            horse.y = random.randint(0, window.height - horse.height)

@window.event()
def on_draw():
    window.clear()
    for s in all_horses:
        s.update()
    fps_display.draw()
    render.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        exit()
    if symbol == key.ENTER and (modifiers & key.MOD_ALT):
        window.set_fullscreen(not window.fullscreen)

def main():
    pyglet.clock.schedule(update)
    pyglet.app.run()

main()