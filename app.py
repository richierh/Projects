#!/usr/bin/python
import tkinter as tk
import timer

class controller(timer.FullScreenApp):

    def __init__(self,*args):
        timer.FullScreenApp.__init__(self,*args)

        self.setting()


        pass

    
    def masuk(self):
        pass

root=tk.Tk()
guitk = controller(root)
root.mainloop()