from tkinter import *
##from tkinter.ttk import *
import os, json, shutil, time, datetime, pyautogui
import commander as c
import importlib


mouseposx = 0
mouseposy = 0
typeset = ''
bgcol = "Black"
fgcol = "White"
fonty = "Fixedsys"
###
window = Tk()

window.title("Program")
window.geometry('900x400')
statuss = ""
##Label
lbl_title = Label(window, text="", font=(fonty, 12))
lbl_title.grid(column=2, row=0)
##
lbl_status = Label(window, text=statuss, font=(fonty, 12))
lbl_status.grid(column=2, row=5)

def test():
    import gui
    importlib.reload(gui)

## Button
btn_time = Button(window, text="Time Sleep", bg=bgcol, fg=fgcol, font=fonty, command=c.timedelay)
btn_time.grid(column=2, row=1, sticky='EWNS')

btn_tsd = Button(window, text="Time Sleep Default", bg=bgcol, fg=fgcol, font=fonty, command=c.timedelayd)
btn_tsd.grid(column=1, row=1, sticky='EWNS')

btn_type = Button(window, text="Type", bg=bgcol, fg=fgcol, font=fonty, command=c.typer)
btn_type.grid(column=4, row=1, sticky='EWNS')

btn_clicker = Button(window, text="Click @ Pos", bg=bgcol, fg=fgcol, font=fonty, command=c.clickpos)
btn_clicker.grid(column=1, row=4, sticky='EWNS')

btn_rclicker = Button(window, text=" Right Click", bg=bgcol, fg=fgcol, font=fonty, command=c.rclickpos)
btn_rclicker.grid(column=1, row=5, sticky='ENS')

btn_drag = Button(window, text="Drag", bg=bgcol, fg=fgcol, font=fonty, command=c.dragpos)
btn_drag.grid(column=2, row=4, sticky='EWNS')


btn_newdoc = Button(window, text="New Doc", bg=bgcol, fg=fgcol, font=fonty, command=c.newdoc)
btn_newdoc.grid(column=1, row=8, sticky='EWNS')


btn_tab = Button(window, text="TAB", bg=bgcol, fg=fgcol, font=fonty, command=c.tab)
btn_tab.grid(column=1, row=6, sticky='EWNS')
btn_tabe = Button(window, text="ENTER", bg=bgcol, fg=fgcol, font=fonty, command=c.ent)
btn_tabe.grid(column=2, row=6, sticky='EWNS')

btn_tabc = Button(window, text="COPY", bg=bgcol, fg=fgcol, font=fonty, command= lambda: c.cfunt('c'))
btn_tabc.grid(column=3, row=3, sticky='EWNS')
btn_tabv = Button(window, text="PASTE", bg=bgcol, fg=fgcol, font=fonty, command= lambda: c.cfunt('v'))
btn_tabv.grid(column=4, row=3, sticky='EWNS')
btn_taba = Button(window, text="SEL ALL", bg=bgcol, fg=fgcol, font=fonty, command= lambda: c.cfunt('a'))
btn_taba.grid(column=5, row=3, sticky='EWNS')


btn_up = Button(window, text="UP", bg=bgcol, fg=fgcol, font=fonty, command= lambda: c.direction('up'))
btn_up.grid(column=5, row=5, sticky='EWNS')
btn_left = Button(window, text="LEFT", bg=bgcol, fg=fgcol, font=fonty, command= lambda: c.direction('left'))
btn_left.grid(column=4, row=6, sticky='EWNS')
btn_right = Button(window, text="RIGHT", bg=bgcol, fg=fgcol, font=fonty, command= lambda: c.direction('right'))
btn_right.grid(column=6, row=6, sticky='EWNS')
btn_down = Button(window, text="DOWN", bg=bgcol, fg=fgcol, font=fonty, command= lambda: c.direction('down'))
btn_down.grid(column=5, row=7, sticky='EWNS')

btn_alttab = Button(window, text="ALT+TAB", bg=bgcol, fg=fgcol, font=fonty, command= lambda: c.afunt('tab'))
btn_alttab.grid(column=6, row=1, sticky='EWNS')

btn_locate = Button(window, text="Locate Image", bg=bgcol, fg=fgcol, font=fonty, command= lambda: c.locate())
btn_locate.grid(column=6, row=8, sticky='EWNS')

btn_clik = Button(window, text="Click", bg=bgcol, fg=fgcol, font=fonty, command= lambda: c.click())
btn_clik.grid(column=6, row=9, sticky='EWNS')
btn_rel = Button(window, text="Relative", bg=bgcol, fg=fgcol, font=fonty, command= lambda: c.relative())
btn_rel.grid(column=7, row=9, sticky='EWNS')

btn_launch = Button(window, text="Test File", bg="Green", fg=fgcol, font=fonty, command= lambda: test())
btn_launch.grid(column=3, row=10, sticky='EWNS')

window.mainloop()