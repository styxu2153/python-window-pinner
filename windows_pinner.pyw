import sys
from pynput import keyboard
from win import Window

windows = []

def on_active_a() -> None:
    active_window = Window()

    for window in windows:
        if Window.get_active_window() == window.window:
            window.set_window_pos()
            return
    active_window.set_window_pos()
    windows.append(active_window)
    return


def on_active_esc():
    sys.exit()


def main():
    with keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+a': on_active_a,
            '<ctrl>+<alt>+q': on_active_esc}) as h:
        h.join()


if __name__ == '__main__':
    windows.append(Window())
    main()