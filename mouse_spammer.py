from pynput.mouse import Button, Controller
import time, sys

button = Button[sys.argv[1]]
mouse = Controller()

while True:
    mouse.click(button)
    time.sleep(0.1) #todo: make configurable
