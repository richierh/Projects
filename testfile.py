#!/usr/bin/python

import tkinter as tk
import datetime
class MainFrame(object):

    """
    """
    def __init__(self,master):
        self.master = master

        self.sbox = tk.Spinbox(self.master,from_=0, to = 10,font=("Arial",12))
        self.sbox.grid(row=0,column=0)
        self.sbox.bind("<Button-1>",self.ok)

        self.but=tk.Button(self.master,text = "Tekanlah")
        self.but.grid(row=1,column=0)
        self.but.bind("<Button-1>",self.klik)

    def klik(self,event):
        self.sboxget = int(self.sbox.get()) * 60
        self.datenow = datetime.datetime.strptime("00:00:00" ,"%H:%M:%S")\
        +datetime.timedelta(minutes=self.sboxget)
        self.datenow = self.datenow.strftime("%H:%M:%S")
        print ("jumlah menit sekarang adalah {}".format(self.datenow))

    
    def ok(self,event):
        print ("hello")
        print (self.sbox.get())


    


if __name__=="__main__":
    root = tk.Tk()
    runapp =  MainFrame(root)
    root.mainloop()