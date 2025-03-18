import copy
import curses
import sys
import time

import pyautogui as pg

from utilities.calculations import calculate_midpoint, win_half
from utilities.hotkeys import pyautogui_hotkey
from utilities.screens import text_entry_screen
from utilities.locate_on_screen import window_locate_image


def pyautogui_outputfile(win, output_filename):
    text = text_entry_screen(
        win,
        heading="Output File Name",
        notes=f"Current Output Filename: {output_filename}",
        text="",
    )

    if not text:
        return output_filename
    return str(text)


def pyautogui_comment(win):
    text = text_entry_screen(win, heading="Add Code Comment")
    return f"# {text}"


def pyautogui_typer(win):
    text = text_entry_screen(win, heading="Type into Field")
    return f"pyautogui.write('{text}')"


def pyautgui_menu(win):
    x, y = 0, 0

    saved = False
    start_time = None
    delay = 0.25
    delay_increment = 0.25
    output_filename = "output.py"

    actions_base = ["import time", "import pyautogui", "import location_handler", "", "DEFAULTDELAY = 0.5"]
    actions = copy.deepcopy(actions_base)
    while 1:
        max_y, max_x = win.getmaxyx()
        half = int(max_x / 2)
        x, y = pg.position()
        str_delay = "{:.2f}".format(delay)
        win.erase()
        win.addstr(1, half, "--- OUTPUT ---")
        win.addstr(1, 1, "--- Pyautogui ---")
        win.addstr(2, 1, f"1. Click at mouse position: {x} {y}")
        win.addstr(3, 1, "2. Typewrite")
        win.addstr(4, 1, "3. Add Hotkey")
        win.addstr(5, 1, "4. Add Comment")
        win.addstr(6, 1, "5. Locate Image")

        win.addstr(
            max_y - 1,
            1,
            f"[q] quit | [s] save | [c] clear | [d] default delay | [w] custom delay ({str_delay}) +- increment | [f] Output: {output_filename}",
        )

        # Write out the actions
        # GIVEN len actions is greater than the length of the screen
        # THEN ROWS at the TOP will not be displayed and all text will push up
        printed_actions = copy.deepcopy(actions)

        if len(printed_actions) > max_y - 3:
            diff = max_y - 3 - len(printed_actions) 
            printed_actions = printed_actions[diff:]
            
        for i, action in enumerate(printed_actions, 2):
            win.addstr(i, half, action)

        if saved:
            win.addstr(max_y - 2, 1, f"Saved to {output_filename}")
            elapsed = time.time() - start_time
            if elapsed > 5:
                saved = False

        try:
            key = win.getkey()
            match key:
                case "1":
                    actions.append(f"pyautogui.click({x}, {y})")
                case "2":
                    text = pyautogui_typer(win)
                    actions.append(text)
                case "3":
                    hotkey = pyautogui_hotkey(win)
                    actions.append(hotkey)
                case "4":
                    comment = pyautogui_comment(win)
                    actions.append(comment)
                case "5":
                    action = window_locate_image(win)
                    if action:
                        actions.append(action)
                case "f":
                    output_filename = pyautogui_outputfile(win, output_filename)

                case "s":
                    with open(str(output_filename), "w") as f:
                        f.write("\n".join(actions))
                    saved = True
                    start_time = time.time()

                case "+":
                    delay += delay_increment
                case "-":
                    if delay > 0.25:
                        delay -= delay_increment

                case "d":
                    actions.append(f"time.sleep(DEFAULTDELAY)")

                case "w":
                    actions.append(f"time.sleep({delay})")

                case "c":
                    actions = copy.deepcopy(actions_base)
                case "q":
                    sys.exit(0)

        except Exception as e:
            if str(e) != "no input":
                raise Exception(e)


def main(win):
    curses.curs_set(0)
    win.nodelay(True)
    win.clear()

    pyautgui_menu(win)
    # max_y, max_x = win.getmaxyx()
    # half = int(max_x/2)

    # key = ''

    # win.addstr(1,1,"--- Automation Support ---\n")
    # win.addstr(2,1,"1. Duckypad")
    # win.addstr(3,1,"2. Pyautogui")
    # win.refresh()
    # while 1:
    #     try:
    #        key = win.getkey()
    #        match key:
    #             case '1':
    #                pass
    #             case '2':
    #                pyautgui_menu(win)
    #                break

    #     except Exception as e:
    #         if str(e) != 'no input':
    #             raise Exception(e)


if __name__ == "__main__":
    curses.wrapper(main)
