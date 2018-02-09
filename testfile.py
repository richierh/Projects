#!/usr/bin/python

import tkinter as tk

class MainFrame(object):

    """
    """
    def __init__(self,master):
        self.master = master

        self.sbox = tk.Spinbox(self.master,from_=0, to = 10,font=("Arial",12))
        self.sbox.grid(row=0,column=0)
        self.sbox.bind("<Button-1>",self.ok)

        self.but=tk.Button(self.master)
        self.but.grid(row=1,column=0)
        self.but.bind("<Button-1>",self.klik)

    def klik(self,event):
        print (self.sbox.get())

    
    def ok(self,event):
        print ("hello")
        print (self.sbox.get())


    


if __name__=="__main__":
    root = tk.Tk()
    runapp =  MainFrame(root)
    root.mainloop()