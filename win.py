import win32gui
import win32con
from decorators import toast_notify


class Window:
    def __init__(self) -> None:
        self.window = Window.get_active_window()
        self.name = win32gui.GetWindowText(self.window)
        self.rect = self.get_window_size()
        self.on_top = False


    def set_window_pos(self) -> None:
        @toast_notify(f'{self.name} is now '+('pinned!.' if not self.on_top else 'unpinned!.'))
        def _set_window_pos():
            self.rect = self.get_window_size()
            
            if not self.on_top:
                win32gui.SetWindowPos(self.window, win32con.HWND_TOPMOST, *self.rect, 0)
                self.on_top = True
            elif self.on_top:
                win32gui.SetWindowPos(self.window, win32con.HWND_NOTOPMOST, *self.rect, 0)
                self.on_top = False
        _set_window_pos()


    def get_window_size(self) -> list:
        rect = win32gui.GetWindowRect(self.window)
        rect_x, rect_y, rect_w, rect_h = rect[0], rect[1],\
        rect[2] - rect[0], rect[3] - rect[1]
        
        return [rect_x, rect_y, rect_w, rect_h]
    

    @staticmethod
    def get_active_window():
        return win32gui.GetForegroundWindow()

    @staticmethod
    def get_active_window_name() -> str:
        return win32gui.GetWindowText(Window.get_active_window())
