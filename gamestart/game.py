import pygame
import inspect
import time

_actor_list = []
_current_fill = None

def add_actor(actor):
    global _actor_list
    _actor_list.append(actor)

def set_fill(fill):
    global _current_fill
    _current_fill = fill

def get_pygcolor(color):
    if isinstance(color, str):
        return pygame.Color(color)
    else:
        return pygame.Color(*color)

class Key:
    def __getattr__(self, key_name):
        full_name = 'K_' + key_name.upper()
        return pygame.key.get_pressed()[getattr(pygame, full_name)]

key = Key()

class Mouse:
    _pos = (0, 0)
    def __getattr__(self, attr_name):
        if attr_name == 'x':
            return Mouse._pos[0]
        if attr_name == 'y':
            return Mouse._pos[1]

mouse = Mouse()

class Window:
    _size = (1024, 768)
    @property
    def height(self):
        return Window._size[1]
    @property
    def width(self):
        return Window._size[0]

window = Window()

def start():
    pygame.init()
    screen = pygame.display.set_mode((window.width, window.height))
    clock = pygame.time.Clock()
    done = False

    def get_parent_frame_function(func_name):
        frame = inspect.stack()[2]
        module = inspect.getmodule(frame[0])
        members = inspect.getmembers(module)
        funcs = [item for item in members if item[0]==func_name]
        if(len(funcs)) == 0:
            return None
        else:
            return funcs[0][1]
    mousedown_func = get_parent_frame_function('mousedown')
    keydown_func = get_parent_frame_function('keydown')
    loop_func = get_parent_frame_function('loop')

    last_time = 0
    while not done:
        this_time = time.time()
        if this_time - last_time > 0.016: # do game loop at 60fps, but draw as fast as it can
            last_time = this_time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if keydown_func is not None:
                        keydown_func()
                    for actor in _actor_list:
                        if 'keydown' in dir(actor):
                            actor.keydown()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    Mouse._pos = event.pos
                    x, y = event.pos
                    actor_captured_mousedown = False # if an actor is clicked, disable global mousedown hook
                    for actor in _actor_list:
                        if 'mousedown' in dir(actor) and actor.collidepoint(x, y):
                            actor.mousedown()
                            actor_captured_mousedown = True
                    if not actor_captured_mousedown and mousedown_func is not None:
                        mousedown_func()

            for actor in _actor_list:
                if 'loop' in dir(actor):
                    actor.loop()

            if loop_func is not None:
                loop_func()

        if _current_fill is not None:
            _current_fill.draw(screen)
        else:
            screen.fill((0, 0, 0))

        for actor in _actor_list:
            if actor.visible:
                actor.draw(screen)
        pygame.display.flip()
        clock.tick(60)