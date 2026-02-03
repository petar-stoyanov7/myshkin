from pynput.mouse import Button, Controller
import time, sys

button = Button[sys.argv[1]]
delay = float(sys.argv[2]) or 0.1
mouse = Controller()
max_duration = 20 #seconds, todo: make configurable
delta = time.time() + max_duration

while time.time() < delta:
    mouse.click(button)
    time.sleep(delay)
