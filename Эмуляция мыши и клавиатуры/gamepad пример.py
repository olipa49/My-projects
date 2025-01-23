import vgamepad as vg
from time import sleep
from ahk import AHK

global flag_w
flag_w = 0

def press_w():
    global flag_w
    if flag_w == 0:
        print(1)
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        gamepad.update()
        flag_w = 1
    else:
        print(0)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        gamepad.update()
        flag_w = 0

ahk = AHK()
gamepad = vg.VX360Gamepad()
sleep(1)
ahk.add_hotkey('^w', callback=press_w)
ahk.start_hotkeys()
