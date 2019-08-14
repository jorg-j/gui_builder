import os, json, shutil, time, pyautogui
from tkinter import *
import uuid


def newdoc():
    with open('gui.py','w')as f:
        f.write("import pyautogui, time, location_handler")
        f.write("\n")

def writer(stringz):
    with open('gui.py','a')as f:
        f.write(stringz)
        f.write("\n")

def clickpos():
    pyautogui.alert("Move to position then Press Enter","Notice","OK")
    global mouseposx
    global mouseposy
    mouseposx, mouseposy = pyautogui.position()
    st = "pyautogui.click(%s,%s)" %(mouseposx, mouseposy)
    writer(st)

def rclickpos():
    pyautogui.alert("Move to Position then Press Enter","Notice","OK")
    global mouseposx
    global mouseposy
    mouseposx, mouseposy = pyautogui.position()
    st = "pyautogui.click(%s,%s,button='right')" %(mouseposx, mouseposy)
    writer(st)


def dragpos():
    pyautogui.alert("Position 1 then Press Enter","Notice","OK")
    global mouseposx
    global mouseposy
    mouseposx, mouseposy = pyautogui.position()
    st = "pyautogui.moveTo(%s,%s)" %(mouseposx, mouseposy)
    writer(st)
    print('mark1')
    pyautogui.alert("Position 2 then Press Enter","Notice","OK")
    mouseposx, mouseposy = pyautogui.position()
    st = "pyautogui.dragTo(%s,%s)" %(mouseposx, mouseposy)
    writer(st)


def typer():
    x = pyautogui.prompt()
    st = "pyautogui.typewrite('%s')" %(x)
    writer(st)

    
def tab():
    st = "pyautogui.hotkey('tab')"
    writer(st)

    
def ent():
    st = "pyautogui.hotkey('enter')"
    writer(st)
 

def timedelay():
    x = pyautogui.prompt()
    st = "time.sleep(%s)" %(x)
    writer(st)


def timedelayd():
    st = "time.sleep(1)"
    writer(st)


def cfunt(com):
    st = "pyautogui.hotkey('ctrl','%s')" %(com)
    writer(st)
  

def direction(direct):
    st = "pyautogui.hotkey('%s')" %(direct)
    writer(st)


def afunt(com):
    st = "pyautogui.hotkey('alt','%s')" %(com)
    writer(st)


def locate():
    pyautogui.alert("Position 1 then Press Enter","Notice","OK")
    mouseposx, mouseposy = pyautogui.position()
    pyautogui.alert("Position 2 then Press Enter","Notice","OK")
    mouseposa, mouseposb = pyautogui.position()
    a,b = mouseposa - mouseposx, mouseposb - mouseposy
    fname = uuid.uuid4()
    filename = "locations/"+str(fname) + '.png'
    im = pyautogui.screenshot(region=(mouseposx,mouseposy, a,b))
    im.save(filename)
    prepstr = "location_handler.locate_image('{}')".format(filename)
    writer(prepstr)

def click():
    writer("pyautogui.click()")

def relative():
    pyautogui.alert("Position 1 then Press Enter","Notice","OK")
    mouseposx, mouseposy = pyautogui.position()
    pyautogui.alert("Position 2 then Press Enter","Notice","OK")
    mouseposa, mouseposb = pyautogui.position()
    a,b = mouseposa - mouseposx, mouseposb - mouseposy
    writer("pyautogui.move({},{})".format(a,b))