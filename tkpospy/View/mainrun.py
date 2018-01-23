#!usr/bin/env python

try:
    import tkinter as tk
    from tkinter import ttk    # for Python2
except ImportError:
    import Tkinter as tk
    import ttk


class runapp():
    
    def run(self):
        root = tk.Tk()
        root.mainloop()