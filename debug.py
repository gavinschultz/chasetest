import pyglet
from pyglet.window import mouse
import render
import world

_selected_rect = None
_text = None
_fps_display = pyglet.clock.ClockDisplay()
#render.register_overlay(_fps_display.label)

def handle_mouse_press(x, y, button, modifiers):
    global _selected_rect
    global _text
    if button == mouse.LEFT:
        selected_horses = [h for h in world.horses if h.rect.includes(x, y)]
        if selected_horses:
            _selected_rect = selected_horses[0].rect
            _text = str(','.join(['{0:.2}'.format(f) for f in selected_horses[0]._sprite.frame_transforms['random with emphasis'][::3]]))

def draw():
    if _selected_rect:
        _draw_rect_and_text(_selected_rect, _text)
    pyglet.gl.glPushMatrix()
    pyglet.gl.glLoadIdentity()
    _fps_display.draw()
    pyglet.gl.glPopMatrix()

def _draw_rect_and_text(rect, text):
    pyglet.graphics.gl.glPolygonMode(pyglet.gl.GL_FRONT_AND_BACK, pyglet.gl.GL_LINE)
    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_QUADS,
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
    pyglet.graphics.gl.glPolygonMode(pyglet.gl.GL_FRONT_AND_BACK, pyglet.gl.GL_FILL)
    pyglet.text.Label(text, font_size=8, color=(255, 0, 0, 255), x=rect.left, y=rect.top).draw()

render.register_draw_func(draw)