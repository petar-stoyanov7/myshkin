from pynput.mouse import Button, Controller
import time, sys

if len(sys.argv) == 1:
    print("No arguments provided, exiting.")
    exit()

button = Button[sys.argv[1]]
delay = float(sys.argv[2]) or 0.1
duration = int(sys.argv[3]) or 60
mouse = Controller()
delta = time.time() + duration

while time.time() < delta:
    mouse.click(button)
    time.sleep(delay)
