import time

import pyautogui

import location_handler

pyautogui.hotkey('win')
time.sleep(0.25)
pyautogui.typewrite('notepad')
time.sleep(0.25)
pyautogui.hotkey('enter')
time.sleep(0.25)
with open("input.txt", "r")as f:
    intype = f.read()
pyautogui.typewrite(intype, interval=0.001)
