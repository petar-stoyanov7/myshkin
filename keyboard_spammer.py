from pynput.keyboard import Key, Controller
import time, sys

param = sys.argv[1]
if hasattr(Key, param):
    key = Key[param]
else:
    key = param

keyboard = Controller()

while True:
    keyboard.press(key)
    keyboard.release(key)
    time.sleep(0.1) #todo: make configurable
