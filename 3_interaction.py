from gamestart import *

fill('desert')
actor('monster')

# create a monster at the center of the mouse
def mousedown():
    actor('monster', mouse.x, mouse.y)

# move the monster when clicked
monster2 = actor('monster')

def monster_mousedown():
    monster2.x -= 20

monster2.mousedown = monster_mousedown

# handle key event
def keydown():
    if key.space:
        monster2.x = 100

start()