# overlay.py

import threading
import tkinter as tk

_overlay_window = None
_overlay_thread = None

COLORS = {
    "1": "#00FF00",  # AllClear - Green
    "2": "#FFFF00",  # Yellow
    "4": "#FF0000",  # Red
}

def _create_overlay(color):
    global _overlay_window

    if _overlay_window:
        _overlay_window.destroy()

    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.configure(bg=color)

    # Hide cursor and make window black on exit
    root.config(cursor="none")

    _overlay_window = root
    root.after(2000, root.destroy)  # Auto-close after 2s
    root.mainloop()

def show_color(status_code):
    color = COLORS.get(status_code)
    if not color:
        return

    global _overlay_thread

    if _overlay_thread and _overlay_thread.is_alive():
        # Skip if overlay is still showing
        return

    _overlay_thread = threading.Thread(target=_create_overlay, args=(color,), daemon=True)
    _overlay_thread.start()
