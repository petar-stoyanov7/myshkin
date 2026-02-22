from pynput.mouse import Button, Controller
import time, sys

if len(sys.argv) == 1:
    print("No arguments provided, exiting.")
    exit()

button = Button[sys.argv[1]]
delay = sys.argv[2] #redundant
duration = int(sys.argv[3]) or 60
mouse = Controller()

#todo: releasing is buggy, fix it!

mouse.press(button)
time.sleep(duration)
mouse.release(button)
