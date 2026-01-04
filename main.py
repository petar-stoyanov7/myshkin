from pynput.mouse import Button, Listener
import subprocess, os, signal

#todo: debug
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
                pid = process_list[identifier]
                os.killpg(os.getpgid(pid), signal.SIGTERM)
                del(process_list[identifier])
            else:
                proc = subprocess.Popen(
                    "./.venv/bin/python3 mouse_spammer.py left", #todo: fix
                    shell=True,
                    preexec_fn=os.setsid
                )
                process_list[identifier] = proc.pid
        elif button == Button.button12:
            identifier = str(Button.button13)
            if identifier in process_list:
                pid = process_list[identifier]
                os.killpg(os.getpgid(pid), signal.SIGTERM)
                del(process_list[identifier])
            else:
                proc = subprocess.Popen(
                    "./.venv/bin/python3 ./keyboard_spammer.py alt", #todo: fix
                    shell=True,
                    preexec_fn=os.setsid
                )
                process_list[identifier] = proc.pid
        # else: #todo: for debugging
        #     print(button)

with Listener(
    on_click=parse_mouse_action
    # on_click=print_button
) as listener:
    listener.join()
