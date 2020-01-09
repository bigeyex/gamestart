from .actor import *
import gamestart.game as game
import pygame

class Fill(Actor):
    def __init__(self, image_name):
        if image_name not in pygame.colordict.THECOLORS:
            self.color = None
            super().__init__(image_name, 0, 0)
        else:
            self.color = image_name

    def spawn(self):
        game.set_fill(self)

    def _get_builtin_asset(self, image_name):
        module_path = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(module_path, 'assets', 'fills', image_name+'.jpg')

    def draw(self, screen):
        if self.color is None:
            super().draw(screen)
        else:
            screen.fill(pygame.Color(self.color), rect=screen.get_rect())
        

def fill(image_name):
    Fill(image_name).spawn()