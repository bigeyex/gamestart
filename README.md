# gamestart - a pygame wrapper for beginners and game jammers

This is a high level api wrapper for pygame, for making games with Python easier and quicker.

Heavily inspired by pygame-zero, Scratch, bitsbox, and game engines such as unity,  
I think there is an opportunity to design a set of API both satisfy the need of beginners  
and game makers who wish a quick result.

Some features: 
- some built-in assets for quick starting and code learning scenarios
- draw loops are managed, so users can focus on actor and scene building

# Quick minimal example

```python
from gamestart import *

actor('monster')

start()
```

This draws a monster on the screen...

# Why another pygame wrapper?

## Why not pygame-zero

Gamestart takes over draw loop management. This makes user code shorter and allowing  
future scene management features.

Gamestart also comes with some built-in asset, for starters and prototypers.  

Gamestart games are run with just Python - it is an option for pygame-zero, but a default in gamestart

## Why not processing.py

Gamestart is driven by Python, instead a Python-Java middle layer.  

Gamestart manages the draw loop.

# Some more examples

Look at the root folder - files like 1_quickstart.py are examples.





