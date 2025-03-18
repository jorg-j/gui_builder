import uuid
import pyautogui as pg
from pathlib import Path
import curses
import os

from utilities.calculations import calculate_midpoint, win_half


def window_locate_image(win):
    title1 = "Locate Image on Screen"
    title2 = "Move your mouse to the top left of the area you would like to capture then press (1)"
    title3 = "Move your mouse to the bottom right of the area you would like to capture then press (2)"
    title4 = "Press [s] to save"

    pos_1 = ()
    pos_2 = ()


    while 1:
        x, y = pg.position()
        win.erase()

        # Set the Heading
        win.addstr(1, 1, title1)
        win.addstr(2, 1, title2)
        win.addstr(3, 1, title3)
        win.addstr(4, 1, title4)

        # Set the cursor position
        win.addstr(5, 1, f"Cursor: {x}, {y}")
        if pos_1:
            win.addstr(6, 1, f"Position 1: {pos_1[0]}, {pos_1[1]}")
        if pos_2:
            win.addstr(7, 1, f"Position 2: {pos_2[0]}, {pos_2[1]}")

        try:
            key = win.getkey()

            if str(key) == "1":
                pos_1 = pg.position()
            elif str(key) == "2":
                pos_2 = pg.position()
                w = (pos_2[0] - pos_1[0])
                h = (pos_2[1] - pos_1[1])
            elif str(key) == 's':
                break
        except Exception as e:
            pass

    if pos_1 and pos_2:
        fname = uuid.uuid4()
        filename = "locations/"+str(fname) + '.png'
        image = pg.screenshot(region=(pos_1[0], pos_1[1], w, h))
        Path('locations').mkdir(exist_ok=True)
        image.save(filename)
        win.erase()
        return "location_handler.locate_image('{}')".format(filename)
    win.erase()

    return ""
