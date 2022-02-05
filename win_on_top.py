import sys

from pynput import keyboard

import win
from decorators import toast_notify

@toast_notify('Window pinned on top!')
def on_active_a():
    active = win.get_active_window()
    win.pin_window_on_top(active)
    
@toast_notify('Window unpinned!')
def on_active_s():
    active = win.get_active_window()
    win.unpin_window(active)


def on_active_esc():
    sys.exit()


def main():
    with keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+a': on_active_a,
            '<ctrl>+<alt>+s': on_active_s,
            '<ctrl>+<alt>+q': on_active_esc}) as h:
        h.join()
        
        
if __name__ == '__main__':
    main()