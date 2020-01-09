from gamestart import *

fill('desert')

# sometimes you want to define your own actors
# and separate them in different files
class Monster(Actor):
    image = 'monster'

    def setup(self):
        self.x = 200
        self.y = 200

    def loop(self):
        self.x += 10
        self.wrap()

    def mousedown(self):
        song('meow')

Monster().spawn()

start()