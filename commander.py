import json
import os
import shutil
import time
import uuid
from tkinter import *

import pyautogui

def newdoc():
    '''Writes a new Document called gui.py to the current directory'''
    with open('gui.py','w')as f:
        f.write("import pyautogui\nimport time\nimport location_handler")
        f.write("\n")

def writer(stringz):
    '''Write to file gui.py'''
    with open('gui.py','a')as f:
        f.write(stringz)
        f.write("\n")

def clickpos():
    '''Click at current position'''
    pyautogui.alert("Move to position then Press Enter","Notice","OK")
    mouseposx, mouseposy = pyautogui.position()
    st = "pyautogui.click(%s,%s)" %(mouseposx, mouseposy)
    writer(st)

def rclickpos():
    '''Right click at current position'''
    pyautogui.alert("Move to Position then Press Enter","Notice","OK")
    mouseposx, mouseposy = pyautogui.position()
    st = "pyautogui.click(%s,%s,button='right')" %(mouseposx, mouseposy)
    writer(st)


def dragpos():
    '''drag from pos to pos'''
    pyautogui.alert("Position 1 then Press Enter","Notice","OK")
    x, y, a, b = twopoint()
    st = "pyautogui.moveTo(%s,%s)" % (x, y)
    writer(st)
    st = "pyautogui.dragTo(%s,%s)" % (a, b)
    writer(st)

def typer():
    '''Type out text from prompt box'''
    text_prompt = pyautogui.prompt()
    st = "pyautogui.typewrite('%s')" %(text_prompt)
    writer(st)

def hotkey(key):
    '''Action Hotkey'''
    st = "pyautogui.hotkey('{}')".format(key)
    writer(st)

def timedelay(setting):
    '''adds time delay, 1 for default 1 second or 0 for prompt based delay'''
    if setting == 1:
        st = "time.sleep(1)"
        writer(st)
    if setting == 0:
        x = pyautogui.prompt()
        st = "time.sleep(%s)" %(x)
        writer(st)

def cfunt(com):
    '''ctrl functions'''
    st = "pyautogui.hotkey('ctrl','%s')" %(com)
    writer(st)

def afunt(com):
    '''alt functions'''
    st = "pyautogui.hotkey('alt','%s')" %(com)
    writer(st)

def direction(direct):
    '''arrow directions'''
    st = "pyautogui.hotkey('%s')" %(direct)
    writer(st)

def locate():
    '''screen grab of 2 points to later allow for locate image on screen'''
    fname = uuid.uuid4()
    filename = "locations/"+str(fname) + '.png'
    x, y, a, b = twopoint()
    a, b = a - x, b - y
    image = pyautogui.screenshot(region=(x, y, a, b))
    image.save(filename)
    prepstr = "location_handler.locate_image('{}')".format(filename)
    writer(prepstr)

def click():
    '''click'''
    writer("pyautogui.click()")

def relative():
    '''same as locate but with relative reference'''
    x, y, a, b = twopoint()
    movetoa, movetob = a - x, b - y
    writer("pyautogui.move({},{})".format(movetoa, movetob))

def twopoint():
    '''Two point return, returns on x y a b'''
    pyautogui.alert("Position 1 then Press Enter", "Notice", "OK")
    x, y = pyautogui.position()
    pyautogui.alert("Position 2 then Press Enter", "Notice", "OK")
    a, b = pyautogui.position()
    return x, y, a, b