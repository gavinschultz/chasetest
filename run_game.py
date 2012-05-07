import pyglet
from pyglet.window import key
import random
import characters
import profile
import render
import config

window = pyglet.window.Window(vsync=False)
pyglet.gl.glClearColor(1, 1, 1, 1)
all_horses = []
fps_display = pyglet.clock.ClockDisplay()
speed_per_tick = 0.0333333

config.install()

for i in range(50):
    all_horses.append(characters.Horse.create_random())

def update(dt):
#    print dt
    for horse in all_horses:
#        print (dt / speed_per_tick)
        horse.x -= horse.speed # * (dt / speed_per_tick)
#        print horse.x
        if horse.x + horse.width < 0:
            horse.speed = random.uniform(3.0, 4.5)
            horse.x = window.width
            horse.y = random.randint(0, window.height - horse.height)
            horse._sprite.x = horse.x
            horse._sprite.y = horse.y
#    window.invalid = True

@window.event()
def on_draw():
    draw()

def draw():
    window.clear()
    for s in all_horses:
        s.update()
    fps_display.draw()
    render.draw()
    window.flip()
#    window.invalid = False

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        exit()
    if symbol == key.ENTER and (modifiers & key.MOD_ALT):
        window.set_fullscreen(not window.fullscreen)
#    print window.vsync

def maximum_framerate_stub(dt):
    pass

def main():
    pyglet.clock.set_fps_limit(60)
    while True:
        dt = pyglet.clock.tick()
        if dt > 0.017 or dt < 0.016:
            print dt
        window.dispatch_events()
        update(dt)
        draw()
#    pyglet.clock.schedule(maximum_framerate_stub)
#    pyglet.clock.schedule_interval(update, 1.0/60.0)
    pyglet.app.run()

main()