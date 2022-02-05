from functools import wraps
from win10toast import ToastNotifier

toaster = ToastNotifier()

def toast_notify(text: str):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            f(*args, **kwargs)
            toaster.show_toast('Window Pinner', 
                text, icon_path=None,
                duration=2, threaded=True)
            return
        return wrapper
    return decorator

