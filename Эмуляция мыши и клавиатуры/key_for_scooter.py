import keyboard
import pydirectinput
import time
global a
a = 0
keyboard.press('w')
while True:
    if keyboard.is_pressed('['):
        a = 1
    if keyboard.is_pressed(']'):
        a = 0
    if a == 1:
        ##
        '''pydirectinput.press('up')
        time.sleep(.011)
        keyboard.release('up')
        ##pydirectinput.press('w')
        time.sleep(.009)
        print('taped')'''
        pydirectinput.keyDown('space')
        time.sleep(.011)
        pydirectinput.keyUp('space')
        time.sleep(.009)
        print('taped')
