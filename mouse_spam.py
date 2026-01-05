from pynput.mouse import Button, Controller
import time, sys

button = Button[sys.argv[1]]
delay = float(sys.argv[2]) or 0.1
mouse = Controller()

while True:
    mouse.click(button)
    time.sleep(delay) #todo: make configurable
