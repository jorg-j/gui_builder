import curses

from utilities.calculations import calculate_midpoint, win_half


def pyautogui_hotkey(win):
    title = "--- Add Hotkey Combo ---"
    helptext = "[1] crtl | [2] alt | [3] shift | [4] esc | [5] enter | [6] backspace | [7] delete | [9] paste | [0] copy"
    control_keys = {
        "ctrl": False,
        "alt": False,
        "shift": False,
        "esc": False,
        "enter": False,
        "backspace": False,
        "delete": False,
    }

    keys_pressed = set()

    def build_checkbox(name, value):
        if value:
            return f"[x] - {name}"
        return f"[ ] - {name}"

    def toggle_control(control_keys, lookup):
        assert lookup in control_keys, f"Key not found: {lookup}"
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
        win.addstr(max_y - 1, 1, helptext)

        half = win_half(win)

        key_status = [build_checkbox(k, v) for k, v in control_keys.items()]
        key_max_len = max(len(i) for i in key_status)

        for i, value in enumerate(key_status, start=3):
            win.addstr(i, half - key_max_len, value)

        for i, value in enumerate(keys_pressed, start=3):
            win.addstr(i, half + 1, value)

        try:
            key = win.getkey()
            if str(key) == "\n":
                break
            elif key == "1":
                control_keys = toggle_control(control_keys, "ctrl")
            elif key == "2":
                control_keys = toggle_control(control_keys, "alt")
            elif key == "3":
                control_keys = toggle_control(control_keys, "shift")
            elif key == "4":
                control_keys = toggle_control(control_keys, "esc")
            elif key == "5":
                control_keys = toggle_control(control_keys, "enter")
            elif key == "6":
                control_keys = toggle_control(control_keys, "backspace")
            elif key == "7":
                control_keys = toggle_control(control_keys, "delete")
            elif key == "9":
                return "pyautogui.hotkey('ctrl', 'v')"
            elif key == "0":
                return "pyautogui.hotkey('ctrl', 'c')"
            else:
                if key in keys_pressed:
                    keys_pressed.remove(key)
                else:
                    keys_pressed.add(key)

        except Exception as e:
            if str(e) != "no input":
                raise Exception(e)

    hotkeys = [k for k, v in control_keys.items() if v]
    if hotkeys or keys_pressed:
        source = "pyautogui.hotkey("
        for item in hotkeys:
            source += f"'{item}',"
        for item in keys_pressed:
            clean_item = item.replace("KEY_", "").lower()
            source += f"'{clean_item}',"
        source = source[:-1]
        source += ")"
        win.erase()
        return source
    win.erase()
    return ""
