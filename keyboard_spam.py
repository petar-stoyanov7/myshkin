from pynput.keyboard import Key, Controller
import time, sys

param = sys.argv[1]
if hasattr(Key, param):
    key = Key[param]
else:
    key = param
delay = float(sys.argv[2]) or 0.1

keyboard = Controller()
max_duration = 20 #seconds, todo: make configurable
delta = time.time() + max_duration

while time.time() < delta:
    keyboard.press(key)
    keyboard.release(key)
    time.sleep(delay)
