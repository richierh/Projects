#!/usr/bin/env python
import View.mainrun as mainrun

try:
    import tkinter as tk
    from tkinter import ttk    # for Python2
except ImportError:
    import Tkinter as tk
    import ttk


if __name__=="__main__":
    mainapp = mainrun.runapp()
    mainapp.run()
