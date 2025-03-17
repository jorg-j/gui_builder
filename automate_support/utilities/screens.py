import curses
import os

from utilities.calculations import calculate_midpoint, win_half


def text_entry_screen(win, heading="", notes="", text=""):

    title = 'Enter Text - "-" for backspace'
    while 1:
        heading_start_x, _ = calculate_midpoint(win, heading)

        title_start_x, title_start_y = calculate_midpoint(win, title)
        text_start_x, text_start_y = calculate_midpoint(win, text)

        win.erase()

        # Set the Heading
        win.addstr(1, heading_start_x, heading)

        # Set the typing field
        win.addstr(text_start_y - 1, text_start_x - 2, "-")
        win.addstr(text_start_y - 1, text_start_x, text + " -")

        # Set the title
        win.addstr(title_start_y + 1, title_start_x, title)

        # Set the Notes
        if notes:
            win.addstr(title_start_y + 2, title_start_x, str(notes))

        try:
            key = win.getkey()

            if str(key) == "\n":
                break
            elif str(key) == "-" or ord(key) == 127:
                text = text[:-1]
            else:
                text += str(key)
        except Exception as e:

            pass
    win.erase()

    return text
