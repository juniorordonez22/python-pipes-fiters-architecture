from tkinter import Tk , Toplevel

def CenterWindow(Window: Tk | Toplevel , window_width: int , window_height: int) -> str:
    screen_width = Window.winfo_screenwidth()
    screen_height = Window.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    return f"{window_width}x{window_height}+{x}+{y}"