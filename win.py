import win32gui
import win32con
from pynput import keyboard


def get_active_window():
    return win32gui.GetForegroundWindow()


def get_active_window_size(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    rect_x, rect_y, rect_w, rect_h = rect[0], rect[1],\
        rect[2] - rect[0], rect[3] - rect[1]
        
    return [rect_x, rect_y, rect_w, rect_h]


def pin_window_on_top(hwnd):
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, *get_active_window_size(hwnd), 0)
    

def unpin_window(hwnd):
    win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, *get_active_window_size(hwnd), 0)


