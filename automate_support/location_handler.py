import time

import pyautogui


def locate_image(image):
    retries = 30
    for i in range(retries):
        location = image
        try:
            location = pyautogui.locateOnScreen(image, grayscale=True)
            centre = pyautogui.center(location)
            pyautogui.moveTo(centre)
            break
        except:
            location = location
            time.sleep(1)
        

def locate_image_drag(image):
    retries = 30
    for i in range(retries):
        location = image
        try:
            location = pyautogui.locateOnScreen(image, grayscale=True)
            centre = pyautogui.center(location)
            pyautogui.moveTo(centre)
            return centre
            break
        except:
            location = location
            time.sleep(1)
