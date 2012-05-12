import pyglet
from pyglet.window import mouse
from pyglet.gl import *
import render
import world

_selected_rect = None
_selected_rect_label = None
_fps_display = pyglet.clock.ClockDisplay()
#render.register_overlay(_fps_display.label)

def handle_mouse_press(x, y, button, modifiers):
    global _selected_rect
    global _selected_rect_label
    if button == mouse.LEFT:
        selected_horses = [h for h in world.horses if h.rect.includes(x, y)]
        if selected_horses:
            _selected_rect = selected_horses[0].rect
            text = str(','.join(['{0:.2}'.format(f) for f in selected_horses[0]._sprite.frame_transforms['random with emphasis'][::3]]))
            _selected_rect_label = pyglet.text.Label(text, font_size=8, color=(255, 0, 0, 255), x=_fps_display.label.x, y=_fps_display.label.height)

def draw():
    if _selected_rect:
        _draw_rect_and_text(_selected_rect, _selected_rect_label)
    glPushMatrix()
    glLoadIdentity()
    _fps_display.draw()
    glPopMatrix()

def _draw_rect_and_text(rect, label):
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    pyglet.graphics.draw_indexed(4, GL_QUADS,
                          [0, 1, 2, 3],
                         ('v2f', (rect.left, rect.bottom, 
                                  rect.left, rect.top, 
                                  rect.right, rect.top, 
                                  rect.right, rect.bottom))
                         ,('c3B', (255, 0, 0, 
                                  255, 0, 0, 
                                  255, 0, 0, 
                                  255, 0, 0))
    )
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    if label:
        label.draw()

render.register_draw_func(draw)