import pygame
import os

class Renderer:
    def __init__(self):
        pygame.display.init()

        window = self.create_window_dimensions()
        os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(window[0][0], window[0][1])

        self.screen = pygame.display.set_mode(window[1])
        self.grid_size = (20,20)
        self.grid_color = (100, 100, 100)

    def get_screen_resolution(self):
        info = pygame.display.Info()
        return info.current_w, info.current_h

    def create_window_dimensions(self):
        """
        Returns two tuples containing the size and position of the window to create
        i.e. ((x, y), (w, h))
        """
        screen_res = self.get_screen_resolution()
        window_res = int(screen_res[0] * 0.75), int(screen_res[1] * 0.25)
        position = int((screen_res[0] - window_res[0])/2), int((screen_res[1] - window_res[1])/3)
        return position, window_res

    def render(self):
        self.screen.fill((0,0,0))
        draw_grid(self.screen, self.grid_color, self.grid_size)
        pygame.display.flip()

def draw_grid(surface, color, grid_size):
    surface_size = surface.get_size()
    for x in range(0, surface_size[0], grid_size[0]):
        pygame.draw.line(surface, color, (x, 0), (x, surface_size[1]))
    for y in range(surface_size[1], 0, -grid_size[1]):
        pygame.draw.line(surface, color, (0, y), (surface_size[0], y))
