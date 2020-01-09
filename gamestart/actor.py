import os
import sys
import pygame
import gamestart.game as game

actor_image_buffer = {}

class Actor:
    visible = True
    def __init__(self, image_name=None, x=512, y=384, width=None):
        if image_name is None:
            image_name = self.image
        if image_name in actor_image_buffer:
            self._image = actor_image_buffer[image_name]
        else:
            if image_name.find('.') == -1:
                self._image = pygame.image.load(self._get_builtin_asset(image_name))
            else:
                image_path = os.path.abspath(os.path.dirname(sys.argv[0]))
                self._image = pygame.image.load(os.path.join(image_path, os.path.join(*image_name.split('/'))))
            actor_image_buffer[image_name] = self._image
        self.rect = self._image.get_rect().copy()
        self.rect.x = x
        self.rect.y = y
        self._transfromed_image = self._image
        if width is not None:
            self.rect.height = int(self.rect.height*width/self.rect.width)
            self.rect.width = width
            self._transfromed_image = pygame.transform.scale(self._image, (self.rect.width, self.rect.height))
        self.setup()

    def __getattr__(self, name):
        if name != 'rect' and hasattr(self.rect, name):
            return getattr(self.rect, name)

    def __setattr__(self, name, value):
        if name != 'rect' and hasattr(self.rect, name):
            setattr(self.rect, name, value)
        else:
            self.__dict__[name] = value

    def _get_builtin_asset(self, image_name):
        module_path = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(module_path, 'assets', 'actors', image_name+'.png')
    
    def draw(self, screen):
        screen.blit(self._transfromed_image, (self.rect.x, self.rect.y))

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def spawn(self):
        game.add_actor(self)
        return self

    def wrap(self):
        if self.rect.x + self.rect.width < 0:
            self.rect.x = game._screen_size[0] - self.width
        elif self.rect.x > game._screen_size[0]:
            self.rect.x = 0
        if self.rect.y + self.rect.height < 0:
            self.rect.y = game._screen_size[1] - self.height
        elif self.rect.y > game._screen_size[1]:
            self.rect.y = 0

    def setup(self):
        pass

    def show(self):
        self.visible = True
    
    def hide(self):
        self.visible = False

def actor(image_name, x=512, y=384, width=None):
    return Actor(image_name, x, y, width).spawn()
    