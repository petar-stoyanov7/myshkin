from time import sleep
from pynput.keyboard import Key, Controller
import sys

if len(sys.argv) == 1:
    print("No arguments provided, exiting.")
    exit()

keyboard = Controller()
key_str=sys.argv[1]
if hasattr(Key, key_str):
    key = Key[key_str]
else:
    key = key_str

delay = sys.argv[2]
duration = int(sys.argv[3]) or 60

#todo: releasing is buggy, fix it!

keyboard.press(key)
sleep(duration)
keyboard.release(key)
