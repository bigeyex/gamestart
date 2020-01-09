from .actor import Actor
import gamestart.vendor.ptext as ptext

class Text(Actor):
    def __init__(self, text, x=0, y=0, font=None):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.setup()

    def draw(self, screen):
        ptext.draw(self.text, (self.x, self.y), antialias=True)

    def collidepoint(self, x, y):
        return False

def text(text, x=0, y=0, font=None):
    return Text(text, x, y, font).spawn()
