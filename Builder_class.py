import datetime
import importlib
import json
import os
import shutil
import time
from tkinter import *

import pyautogui

import commander as c

def test():
    import gui
    importlib.reload(gui)

default_location = 'EWNS'

bgcol, fgcol, fonty = "Black", "White", "Fixedsys"

###
window = Tk()
window.title("Program")
window.geometry('900x400')

class button_maker():
    def __init__(self, txt, cmd, pos1, pos2):
        self.txt = txt
        self.cmd = cmd
        self.pos1 = pos1
        self.pos2 = pos2
        self.button = Button(window, text=self.txt, bg=bgcol, fg=fgcol, font=fonty, command=self.cmd)
        self.button.grid(column=pos1, row=pos2, sticky=default_location)

## Button
time_button = button_maker("Time Sleep", lambda: c.timedelay(0), 2, 1)
time_delay_button = button_maker("Time Sleep Default", lambda: c.timedelay(1), 1, 1)
type_text_button = button_maker("Type", c.typer, 4, 1)
click_at_pos = button_maker("Click @ Pos", c.clickpos, 1, 4)
right_click = button_maker("Right Click", c.rclickpos, 1, 5)
drag_button = button_maker("Drag", c.dragpos, 2, 4)
new_doc = button_maker("New Doc", c.newdoc, 1, 8)
tab_button = button_maker("Tab", c.hotkey('TAB'), 1, 6)
enter_button = button_maker("Enter", c.hotkey('enter'), 2, 6)
copy_button = button_maker("Copy", lambda: c.cfunt('c'), 3, 3)
paste_button = button_maker("Paste", lambda: c.cfunt('v'), 4, 3)
select_all = button_maker("Sel All", lambda: c.cfunt('a'), 5, 3)
btn_up = button_maker("UP", lambda: c.direction('up'), 5, 5)
btn_left = button_maker("LEFT", lambda: c.direction('left'), 4, 6)
btn_right = button_maker("RIGHT", lambda: c.direction('right'), 6, 6)
btn_down = button_maker("DOWN", lambda: c.direction('down'), 5, 7)
btn_alttab = button_maker("ALT+TAB", lambda: c.afunt('tab'), 6, 1)
btn_locate = button_maker("Locate Image", lambda: c.locate(), 6, 8)
btn_clik = button_maker("Click", lambda: c.click(), 6, 9)
btn_rel = button_maker("Relative", lambda: c.relative(), 7, 9)
btn_launch = button_maker("Test File", lambda: test(), 3, 10)

window.mainloop()