from gamestart import *

# NOT IMPLEMENTED YET

# move and size may take time
boy = actor('boy', 500, 500)
boy.move(2000, 500, 2)

# use delay
def step2():
    boy.move(50, 500, 3)
    
delay(2, step2)
