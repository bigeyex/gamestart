import pygame
from .actor import Actor
from .game import get_pygcolor

class Box(Actor):
    def __init__(self, x, y, width, height, fill_color='green', stroke_color=None, pen_size=1):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = fill_color
        self.stroke_color = stroke_color
        self.pen_size = pen_size
        self.setup()

    def draw(self, screen):
        if self.fill_color is not None:
            screen.fill(get_pygcolor(self.fill_color), rect=self.rect)
        if self.stroke_color is not None and self.pen_size != 0:
            pygame.draw.rect(screen, get_pygcolor(self.stroke_color), self.rect, self.pen_size)

def box(x, y, width, height, fill_color='green', stroke_color=None, pen_size=1):
    return Box(x, y, width, height, fill_color, stroke_color, pen_size).spawn()


class Circle(Actor):
    def __init__(self, x, y, radius, fill_color='green', stroke_color=None, pen_size=1):
        self.rect = pygame.Rect(x-radius, y-radius, 2*radius, 2*radius)
        self.radius = radius
        self.fill_color = fill_color
        self.stroke_color = stroke_color
        self.pen_size = pen_size
        self.setup()

    def draw(self, screen):
        center = (self.rect.x + self.radius, self.rect.y + self.radius)
        if self.fill_color is not None:
            pygame.draw.circle(screen, get_pygcolor(self.fill_color), center, self.radius)
        if self.stroke_color is not None and self.pen_size != 0:
            pygame.draw.circle(screen, get_pygcolor(self.stroke_color), center, self.radius, self.pen_size)

def circle(x, y, radius, fill_color='green', stroke_color=None, pen_size=1):
    return Circle(x, y, radius, fill_color, stroke_color, pen_size).spawn()

class Line(Actor):
    def __init__(self, x1, y1, x2, y2, color='green', pen_size=1):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.color = color
        self.pen_size = pen_size
        self.setup()

    def draw(self, screen):
        pygame.draw.line(screen, get_pygcolor(self.color), (self.x1, self.y1), (self.x2, self.y2), self.pen_size)

def line(x1, y1, x2, y2, color='green', pen_size=1):
    return Line(x1, y1, x2, y2, color, pen_size).spawn()