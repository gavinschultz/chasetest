import pyglet
from pyglet.window import key
from pyglet.window import mouse
import characters
import render
import config
import world
from rect import Rect
import debug

class MainWindow(pyglet.window.Window):
    def __init__(self):
        super(MainWindow, self).__init__()

window = MainWindow()

def draw(dt):
    window.clear()
    render.draw()
#    window.fps_display.draw()
    window.flip()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        exit()
    if symbol == key.ENTER and (modifiers & key.MOD_SHIFT):
        window.set_fullscreen(not window.fullscreen)
        world.set_rect(Rect(0,0,window.width,window.height))

@window.event    
def on_mouse_press(x, y, button, modifiers):
    debug.handle_mouse_press(x, y, button, modifiers)

def main():
    render.init()
    world.init()

    pyglet.app.event_loop.idle = idle
    pyglet.clock.schedule_interval(world.update, 1.0/config.updates_per_second)
    pyglet.clock.schedule_interval(draw, 1.0/config.frames_per_second)
##    pyglet.clock.schedule(draw)
    pyglet.app.run()

# override app event loop to prevent unwanted draws
def idle():
    pyglet.clock.tick(poll=True)
    return pyglet.clock.get_sleep_time(sleep_idle=True)

main()