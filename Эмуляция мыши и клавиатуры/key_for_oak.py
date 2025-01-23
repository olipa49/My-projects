import mouse
import time
time.sleep(5)
mouse.press(button='right')
while True:
    mouse.move(0, -30 , False)
    time.sleep(1)
    mouse.move(0, -30 , False)
    time.sleep(1)
"""from pynput.mouse import Button, Controller
import time
mouse = Controller()
while True:
    mouse.move(5, -5)
    time.sleep(1)
"""
