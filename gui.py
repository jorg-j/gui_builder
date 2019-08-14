import pyautogui, time, location_handler
pyautogui.hotkey('win')
pyautogui.typewrite('notepad')
time.sleep(0.2)
pyautogui.hotkey('enter')
time.sleep(0.1)
with open("text.txt","r")as f:
    text = f.read()
pyautogui.typewrite(text)
