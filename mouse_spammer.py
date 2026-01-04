from pynput.mouse import Button, Controller
import time

#todo: make dynamic
button = Button.left
mouse = Controller()

while True:
    # print('spam')
    mouse.click(Button.left)
    time.sleep(0.1)
