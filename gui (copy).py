from tkinter import *
import pyautogui

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

x,y = pyautogui.position()
lbl_title = Label(window, text="", font=(fonty, 12))
lbl_title.grid(column=2, row=0)
w.create_line(x, y, x+5, y+5)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")

mainloop()
## Test