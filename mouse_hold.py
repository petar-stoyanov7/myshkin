from pynput.mouse import Button, Controller
import sys

button = Button[sys.argv[1]]
mouse = Controller()

#todo: rework
while True:
    mouse.press(button)
