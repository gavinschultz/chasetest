import pyglet
from pyglet.window import key
from pyglet.window import mouse
import characters
import render
import config
import world
from rect import Rect

class MainWindow(pyglet.window.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.fps_display = pyglet.clock.ClockDisplay()
        render.register_overlay(self.fps_display.label)

window = MainWindow()

def draw(dt):
    window.clear()
    render.draw()
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
    if button == mouse.LEFT:
        selected_horses = [h for h in world.horses if h.rect.includes(x, y)]
        if selected_horses: 
            render.selected_rect_and_text = selected_horses[0].rect, str(','.join(['{0:.2}'.format(f) for f in selected_horses[0]._sprite.frame_transforms['random with emphasis'][::3]]))

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