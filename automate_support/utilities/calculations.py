def calculate_midpoint(win, text):
    """
    Returns x y midpoint
    """
    max_y, max_x = win.getmaxyx()
    half = int(max_x / 2)
    return int(half - (len(text) / 2)), int(max_y / 2)


def win_half(win):
    _, max_x = win.getmaxyx()
    return int(max_x / 2)
