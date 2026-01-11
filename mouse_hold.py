from pynput.mouse import Button, Controller

mouse = Controller()

def toggle_mouse_hold(button, action):
    if action == "hold":
        mouse.press(button)
    else:
        mouse.release(button)
