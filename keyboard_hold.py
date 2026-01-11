from pynput.keyboard import Key, Controller

keyboard = Controller()

def toggle_keyboard_hold(key_str, action):
    if hasattr(Key, key_str):
        key = Key[key_str]
    else:
        key = key_str

    if action == "hold":
        keyboard.press(key)
    else:
        keyboard.release(key)
