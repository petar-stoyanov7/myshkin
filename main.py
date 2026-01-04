from pynput.mouse import Button, Controller, Listener
import subprocess, os, signal, time

def print_button(x, y, button, pressed):
    action = "clicked" if pressed else "released"
    print("Mouse button {} {} at {} {}".format(button, action, x, y))

process_list = {}

def parse_mouse_action(x,y,button,pressed):
    #on release of the button
    if not pressed:
        #todo: make dynamic, based on config
        if button == Button.button13:
            identifier = str(Button.button13)
            if identifier in process_list:
                print('stopping')
                process = process_list[identifier]
                os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                del(process_list[identifier])
            else:
                print('starting')
                process_list[identifier] = subprocess.Popen(
                    "python ./mouse_clicker.py",
                    shell=True,
                    preexec_fn=os.setsid
                )
        elif button == Button.button12:
            subprocess.run(
                "python ./keyboard_clicker.py",
                shell=True
            )
        else:
            print(button)

with Listener(
    on_click=parse_mouse_action
    # on_click=print_button
) as listener:
    listener.join()
