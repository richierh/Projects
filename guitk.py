#!/usr/bin/python

import tkinter as tk
import timer

class GuiFrame(FullScreenApp):
    def __init__(self):
        FullScreenApp.__init__(self,master)
        pass

    def tahantutup(self):
        pass       
    def hapus(self,event):
        print("digunakan untuk menghapus")

    def masuk(self,event):
        
        print ("digunakan untuk masuk")
        self.master.withdraw()
        self.bukaframe = RangkaBill()

    def show(self,event):
        self.master.withdraw()
        self.buka = RangkaAdmin()
 
    def tutup(self,event):
        self.master.destroy()
        pass
    
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


root =tk.Tk()
guitk = timer.FullScreenApp(root)
guitk.setting
root.mainloop()