import pyglet
from pyglet.window import key
import random
import characters
import profile
import render
import config

window = pyglet.window.Window(vsync=True)
pyglet.gl.glClearColor(1, 1, 1, 1)
all_horses = []
fps = 75.0
updates_per_second = 60.0
fps_display = pyglet.clock.ClockDisplay()
dt_display = pyglet.text.Label('', font_size=12, y=window.height - 20, x=10, color=(0,0,0,255))
horse_speed_display = pyglet.text.Label('', font_size=12, y=dt_display.y - 20, x=10, color=(0,0,0,255))
multiplier_display = pyglet.text.Label('', font_size=12, y=horse_speed_display.y - 20, x=10, color=(0,0,0,255))

config.install()

for i in range(50):
    all_horses.append(characters.Horse.create_random())

def update(dt):
#    print dt
    multiplier = (1 / updates_per_second)
    for horse in all_horses:
#        print (dt / speed_per_tick)
        horse.x -= horse.speed * dt
        if horse.x + horse.width < 0:
            horse.speed = random.uniform(35.0, 45.0)
            horse.x = window.width
            horse.y = random.randint(0, window.height - horse.height)
            horse._sprite.x = horse.x
            horse._sprite.y = horse.y
#    window.invalid = True
    dt_display.text = 'dt = {0:.4f}'.format(dt)
    horse_speed_display.text = 'horse speed = {0:.4f}'.format(horse.speed)
    multiplier_display.text = ' * multiplier = {0:.4f} = {1:.4f}'.format(multiplier, horse.speed * dt)
#    dt_display.text = '{0}'.format(dt * (1000 / fps))

@window.event()
def on_draw():
    draw()

def draw(dt):
    window.clear()
    for s in all_horses:
        s.update()
    fps_display.draw()
    dt_display.draw()
    multiplier_display.draw()
    horse_speed_display.draw()
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
#    pyglet.clock.set_fps_limit(60)
#    while True:
#        dt = pyglet.clock.tick()
#        if dt > 0.017 or dt < 0.016:
#            print dt
#        window.dispatch_events()
#        update(dt)
#        draw()
#    pyglet.clock.schedule(maximum_framerate_stub)
#    pyglet.clock.schedule_interval(update, 1.0/60.0)
    pyglet.app.event_loop.idle = idle
    pyglet.clock.schedule_interval(update, 1/updates_per_second)
    pyglet.clock.schedule_interval(draw, 1/fps)
    pyglet.app.run()

def idle():
    pyglet.clock.tick(poll=True)
    return pyglet.clock.get_sleep_time(sleep_idle=True)

main()