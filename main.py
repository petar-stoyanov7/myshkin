from pynput.mouse import Button, Listener
import subprocess, os, sys, signal, json

script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

#todo: replace with user home dir
with open('{}/macros.json'.format(script_dir)) as file:
    macro_data = json.load(file)

def print_button(x, y, button, pressed):
    action = "clicked" if pressed else "released"
    print("Mouse button {} {} at {} {}".format(button, action, x, y))

process_list = {}

def parse_mouse_action(x,y,button,pressed):
    #skip left, right, middle entirely
    if button == Button.left or button == Button.right or button == Button.middle:
        return

    #on release of the button
    if not pressed and str(button) in macro_data:
        button_str = str(button)
        macro = macro_data[button_str]
        exec_file = "{}/{}_{}.py".format(script_dir, macro['target_type'], macro['macro_type'])

        if not os.path.isfile(exec_file) or not check_macro(macro):
            print("invalid macro")
            return

        if button_str in process_list:
            pid = process_list[button_str]
            os.killpg(os.getpgid(pid), signal.SIGTERM)
            del(process_list[button_str])
        else:
            proc = subprocess.Popen(
                "{}/.venv/bin/python3 {} {} {} {}".format(
                    script_dir,
                    exec_file,
                    macro['target'],
                    macro['delay'],
                    macro['duration']
                ),
                shell=True,
                preexec_fn=os.setsid
            )
            process_list[button_str] = proc.pid

def check_macro(macro_obj):
    if (
            'macro_type' not in macro_obj or
            'target_type' not in macro_obj or
            'target' not in macro_obj or
            'delay' not in macro_obj
        ):
        return False
    return True

with Listener(
    on_click=parse_mouse_action
    # on_click=print_button
) as listener:
    listener.join()
