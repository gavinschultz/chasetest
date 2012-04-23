import pygame
import os

def get_screen_resolution():
    info = pygame.display.Info()
    return info.current_w, info.current_h

def create_window_dimensions():
    """
    Returns two tuples containing the size and position of the window to create
    i.e. ((x, y), (w, h))
    """
    screen_res = get_screen_resolution()
    window_res = int(screen_res[0] * 0.75), int(screen_res[1] * 0.25)
    position = int((screen_res[0] - window_res[0])/2), int((screen_res[1] - window_res[1])/3)
    return position, window_res

def init():
    pygame.display.init()

    window = create_window_dimensions()
    os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(window[0][0], window[0][1])
    return pygame.display.set_mode(window[1])

def render(screen):
    screen.fill((0,0,0))
    pygame.display.flip()
