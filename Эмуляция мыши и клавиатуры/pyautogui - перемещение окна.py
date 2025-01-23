import subprocess
import time
import pyautogui
import random
time.sleep(2)
np = pyautogui.getActiveWindow()
a, b = 0, 0
np.moveTo(0, 0)
while True:
    x, y = pyautogui.position()
    if abs(a - x + 690) < 100 and abs(b - y + 640) < 30:
        a, b = random.randrange(600), random.randrange(300)
        np.moveTo(a, b)
    #time.sleep(5)
