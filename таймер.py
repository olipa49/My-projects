#from tkinter import *
import time
#root = Tk()
#label = Label(root, text="", font="Helvetica, 20")
#label.pack()
minutes = 0
clock_min = 0
clock_hour = 0
f = open("time.txt", "r")
minutes = int(f.read())
while True:
    clock_hour = minutes // 60
    clock_min = minutes - minutes // 60 * 60##эквивалентно clock_min = minutes % 60
    #label.config(text=str(clock_hour) + ":" + str(clock_min))
    print(str(clock_hour) + ":" + str(clock_min))
    #root.update()
    minutes = minutes + 1
    f = open("time.txt", "w")
    f.write(str(minutes))
    f.close()
    time.sleep(60)
#root.mainloop()
