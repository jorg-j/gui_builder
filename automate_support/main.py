import curses
import pyautogui as pg
import time
import sys
import copy


def calculate_midpoint(win, text):
    '''
    Returns x y midpoint
    '''
    max_y, max_x = win.getmaxyx()
    half = int(max_x / 2)
    return int(half - (len(text)/ 2)), int(max_y/2)

def win_half(win):
    max_y, max_x = win.getmaxyx()
    return int(max_x / 2)   

def pyautogui_typer(win):
    text = ""
    title = 'Enter Text - "-" for backspace'
    while 1:

        title_start_x, title_start_y = calculate_midpoint(win, title)
        text_start_x, text_start_y = calculate_midpoint(win, text)

        win.erase()
        win.addstr(title_start_y+1, title_start_x, title)
        win.addstr(text_start_y-1, text_start_x, text)

        try:                 
            key = win.getkey()
            if str(key) == '\n':
                break
            elif str(key) == '-':
                text = text[:-1]
            else:
                text += str(key)
        except Exception as e:
            pass
    win.erase()
    return f"pyautogui.write('{text}')"



def pyautogui_hotkey(win):
    title = '--- Add Hotkey Combo ---'
    helptext = '[1] crtl | [2] alt | [3] shift | [4] esc | [0] copy | [9] paste'
    control_keys = {
    "ctrl": False,
    "alt": False,
    "shift": False,
    "esc": False,
    }

    keys_pressed = set()



    def build_checkbox(name, value):
        if value:
            return f"[x] - {name}"
        return f"[ ] - {name}"
    
    def toggle_control(control_keys, lookup):
        if control_keys[lookup]:
            control_keys[lookup] = False
        else:
            control_keys[lookup] = True
        return control_keys
    
    
    while 1:
        title_start_x, _ = calculate_midpoint(win, title)
        max_y, max_x = win.getmaxyx()

        win.erase()
        win.addstr(1, title_start_x, title)
        win.addstr(max_y-1, 1, helptext)

        half = win_half(win)

        key_status = [
            build_checkbox(k, v)
            for k, v in control_keys.items()
        ]
        key_max_len = max(len(i) for i in key_status)

        for i, value in enumerate(key_status, start=3):
            win.addstr(i, half - key_max_len, value)

        for i, value in enumerate(keys_pressed, start=3):
            win.addstr(i, half + 1, value)

    
        try:                 
            key = win.getkey()
            if str(key) == '\n':
                break
            elif key == '1':
                control_keys = toggle_control(control_keys, 'ctrl')
            elif key == '2':
                control_keys = toggle_control(control_keys, 'alt')
            elif key == '3':
                control_keys = toggle_control(control_keys, 'shift')
            elif key == '4':
                control_keys = toggle_control(control_keys, 'esc')
            elif key == '9':
                return "pyautogui.hotkey('ctrl', 'v')"
            elif key == '0':
                return "pyautogui.hotkey('ctrl', 'c')"
            else:
                if key in keys_pressed:
                    keys_pressed.remove(key)
                else:
                    keys_pressed.add(key)
           

        except Exception as e:
            if str(e) != 'no input':
                raise Exception(e)

    
    hotkeys = [
        k
        for k, v in control_keys.items()
        if v
    ]
    if hotkeys or keys_pressed:
        source = 'pyautogui.hotkey('
        for item in hotkeys:
            source += f"'{item}',"
        for item in keys_pressed:
            source += f"'{item}',"
        source = source[:-1]
        source += ')'
        return source
    win.erase()
    return ""


def pyautgui_menu(win):
    x, y = 0, 0

    saved = False
    start_time = None
    delay = 0.25
    delay_increment = 0.25


    actions_base = ["import time", "import pyautogui", ""]
    actions = copy.deepcopy(actions_base)
    while 1:
        max_y, max_x = win.getmaxyx()
        half = int(max_x / 2)
        x, y = pg.position()
        str_delay = "{:.2f}".format(delay)
        win.erase()
        win.addstr(1,half, "--- OUTPUT ---")
        win.addstr(1,1,"--- Pyautogui ---")
        win.addstr(2,1,f"1. Click at mouse position: {x} {y}")
        win.addstr(3,1,"2. Typewrite")
        win.addstr(4,1, "3. Add Hotkey")


        win.addstr(max_y-1, 1, f"[q] quit | [s] save | [c] clear | [d] delay ({str_delay}) +- increment")



        for i, action in enumerate(actions, 2):
            win.addstr(i, half, action)


        if saved:
            win.addstr(max_y-2, 1, "Saved to output.py")
            elapsed = time.time() - start_time
            if elapsed > 5:
                saved = False


        try:                 
           key = win.getkey()
           match key:
                case '1':
                   actions.append(f"pyautogui.click({x}, {y})")
                case '2':
                   text = pyautogui_typer(win)
                   actions.append(text)
                case '3':
                   hotkey = pyautogui_hotkey(win)
                   actions.append(hotkey)
                case 's':
                    with open('output.py', 'w')as f:
                        f.write('\n'.join(actions))
                    saved = True
                    start_time = time.time()

                case "+":
                   delay += delay_increment
                case "-":
                   if delay > 0.25:
                       delay -= delay_increment

                case "d":
                   actions.append(f'time.sleep({delay})')

                case 'c':
                   actions = actions_base
                case 'q':
                   sys.exit(0)
                   

        except Exception as e:
            if str(e) != 'no input':
                raise Exception(e)



def main(win):
    curses.curs_set(0)
    win.nodelay(True)
    win.clear()
    max_y, max_x = win.getmaxyx()
    half = int(max_x/2)

    key = ''

    win.addstr(1,1,"--- Automation Support ---\n")
    win.addstr(2,1,"1. Duckypad")
    win.addstr(3,1,"2. Pyautogui")
    win.refresh()
    while 1:
        try:                 
           key = win.getkey()
           match key:
                case '1':
                   pass
                case '2':
                   pyautgui_menu(win)
                   break

        except Exception as e:
            if str(e) != 'no input':
                raise Exception(e)

           
if __name__ == "__main__":
    curses.wrapper(main)
