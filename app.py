#!/usr/bin/python
import tkinter as tk
import timer
import clock

class controller(timer.FullScreenApp):

    def __init__(self,*args):
        timer.FullScreenApp.__init__(self,*args)
        self.setting()
    
    def tahantutup(self):

        pass       

    def hapus(self,event):
        #print("digunakan untuk menghapus")
        pass
        
    def masuk(self,event):
        print ("digunakan untuk masuk")
        self.master.withdraw()
        self.bukaframe = timer.RangkaBill(self.master)
        pass
        
    def show(self,event):
        print ("masuk admin")
        self.master.withdraw()
        self.buka = timer.RangkaAdmin(self.master)
        pass

    def tutup(self,event):
        self.master.destroy()
        pass
    
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
        pass

root=tk.Tk()
guitk = controller(root)
root.mainloop()