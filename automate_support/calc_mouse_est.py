import sys
import time
import curses
import os
import pyautogui as pg





def calculate_position(x, y):
    dx = x * 0.505
    dy = (2159 -  y) * 0.505
    return int(round(dx, 0)), int(round(dy,0))

def register_position(x, y, positions):
    dx, dy = calculate_position(x, y)
    positions.append((dx, dy))
    return positions

def calculate_offset(a, b):
    '''
    >>> calculate_offset(100, 150)
    50
    >>> calculate_offset(280, 240)
    -40
    '''
    
    if a < b:
        return b - a
    
    c = a - b
    return c - (c*2)


def calculate_ducky_coord(positions):
    '''
    calculate_ducky_coord([(100, 200), (50, 250), (3000, 0)])
    [(-9999, -9999), (100, 200), (-50, 50), (2950, -250)]
    calculate_ducky_coord([(100, 200), (50, 250), "cake", "bacon", (3000, 0)])
    [(-9999, -9999), (100, 200), (-50, 50), "cake", "bacon" (2950, -250)]
    '''
    mapping = [(-9999, -9999)]
    if not positions:
        return []
    mapping.append(positions[0])
    positions.pop(0)

    m_offset = -1


    for pos in positions:
        if isinstance(pos[0], int):
            previous_x, previous_y = mapping[m_offset]
            m_offset = -1
            x, y = pos
            n_x = calculate_offset(previous_x, x)
            n_y = calculate_offset(previous_y, y)
            mapping.append((n_x, n_y))
        else:
            mapping.append(pos)
            m_offset -= 1
    return mapping


def print_ducky(win, current_positions):
    DEFAULTDELAY = 250
    new_pos = calculate_ducky_coord(positions=current_positions)
    payload = ''

    for i in new_pos:
        if isinstance(i[0], int):
            payload += f"MOUSE_MOVE {i[0]} {i[1]}\nDELAY {DEFAULTDELAY}\n"

    with open('ducky_mouse.txt', 'w')as f:
        f.write(payload)

    win.clear()
    win.addstr("--- Results ---\n")
    win.addstr(payload)
    win.addstr("\n\n Press q\n")
    while 1:
        try:
            key = win.getkey()
            if key == 'q':
                break
        except:
            pass
    win.clear()

def custom_ducky(win, positions):
    """
    A function to build a custom command via a curses interface and append it to positions.

    >>> class MockWindow:
    ...     def __init__(self, keys):
    ...         self.keys = iter(keys)
    ...     def erase(self): pass
    ...     def addstr(self, text): pass
    ...     def getkey(self):
    ...         return next(self.keys)
    ...     def clear(self): pass

    >>> custom_ducky(MockWindow(['a', '\\n']), [])
    ['a']
    >>> custom_ducky(MockWindow(['\\n']), [])
    []
    >>> custom_ducky(MockWindow(['a', 'b', '\\n']), [])
    ['ab']
    >>> custom_ducky(MockWindow(['a', "'", '\\n']), [])
    []
    >>> custom_ducky(MockWindow(['x', 'y', "'", 'z', '\\n']), [])
    ['xz']
    """
    cust = ""
    while 1:
        win.erase()
        win.addstr("--- Add custom ducky script --- NOTE: ' is backspace\n")

        win.addstr(f"Custom Command: {cust}")

        try:
            key = win.getkey()
            if key == '\n':
                break
            if str(key) == "'":
                cust = cust[:-1]
            else:
                cust += str(key)
        except:
            pass
    win.clear()
    if cust:
        positions.append(cust)

    return positions

            # if key in ('KEY_BACKSPACE', '\b', '\x7f'):
            #     cust += "fofofo"
            # else:
            #     cust += key
def main(win):
    prevx = 0
    prevy = 0

    positions = []

    win.nodelay(True)
    win.clear()
    key = ''
    ex = ''

    while 1:          
        x, y = pg.position()
        y_adjusted = 2159 - y
        
        ducky_x, ducky_y = calculate_position(x, y_adjusted)

        win.erase()
        win.addstr("Calculate Duckypad mouse position\n")
        win.addstr(f'Original: X: {x} | Y: {y}\n')
        win.addstr(f"Mapped  : X: {ducky_x} | Y: {ducky_y}\n\n")
        win.addstr("---- | r = record position")
        win.addstr(" | 1 = left click")
        win.addstr(" | c = custom")
        win.addstr(" | p = print")
        win.addstr(" | y = reset")
        win.addstr(" | q = quit | ----\n\n")
        win.addstr(ex)
        for p in positions:
            if isinstance(p[0], int):
                win.addstr(f"x: {p[0]} y: {p[1]}\n")
            else:
                win.addstr(p + '\n')
        try:                 
           key = win.getkey()
           match key:
                case 'r':
                   positions = register_position(x, y, positions)
                case 'q':
                   sys.exit(0)
                case 'y':
                   positions = []
                case 'p':
                   print_ducky(win, positions)
                case 'c':
                   positions = custom_ducky(win, positions)
                case '1':
                   positions.append("LMOUSE")
                
        except Exception as e:
            if str(e) != 'no input':
                ex = str(e)
           # No input   
           
if __name__ == "__main__":
    curses.wrapper(main)
   