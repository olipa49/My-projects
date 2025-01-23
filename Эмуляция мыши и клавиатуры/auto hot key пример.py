from ahk import AHK
from time import sleep
ahk = AHK()

'''ahk.mouse_move(x=100, y=100, blocking=True)  # Blocks until mouse finishes moving (the default)
ahk.mouse_move(x=150, y=150, speed=10, blocking=True) # Moves the mouse to x, y taking 'speed' seconds to move
print(ahk.mouse_position)  #  (150, 150)'''
sleep(1)
while True:
    ahk.key_down('w')
    sleep(.1)
    ahk.key_up('w')
    sleep(.1)
