#!/usr/bin/python

import tkinter as tk

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master= master
    
self.frames = {}
        for f in (HomeFrame, ExecuteFrame): # defined subclasses of BaseFrame
            frame = f(self.container, self)
            frame.grid(row=2, column=2, sticky=tk.NW+tk.SE)
            self.frames[f] = frame
    def setting(self):
        pad=3
        self._geom='200x200+0+0'
        self.master.geometry("{0}x{1}+0+0".format(
        self.master.winfo_screenwidth()-pad, self.master.winfo_screenheight()-pad))
        self.master.bind('<Escape>',self.toggle_geom) 
        self.master.grid_rowconfigure(0,weight = 1)
        self.master.grid_columnconfigure(0,weight= 1) 

        self.master.grid_rowconfigure(1,weight = 1)

        self.master.grid_rowconfigure(2,weight = 1)

        durasi = "Selamat datang \nUntuk memulai \nSilahkan tentukan waktu\nTerlebih dahulu"
        self.Frame1 = tk.Frame(self.master)
        self.Frame1.grid(row=0,column=0)
        self.label = tk.Label(self.Frame1,text = durasi,font=("Arial",30))
        self.label.grid(row=0,column=0)


        self.Frame2 = tk.Frame(self.master)
        self.Frame2.grid(row=1,column=0)
        self.label1=tk.Label(self.Frame2,text = " Masukkan durasi waktu dlm jam",font=("Arial",15))
        self.label1.grid(row=0,column=0)
        self.lbox=tk.Spinbox(self.Frame2,from_=1,to=24,font=("Arial",30))
        self.lbox.grid(row=0,column=1)

        self.lbox=tk.Spinbox(self.Frame2,values=(0,5,10,15,20,25,30,35,40,45,50,55),font=("Arial",30))
        self.lbox.grid(row=1,column=1)

        self.label2=tk.Label(self.Frame2,text = "Masukan durasi waktu dalam menit",font=("Arial",15))
        self.label2.grid(row=1,column=0)
        
        self.button1=tk.Button(self.Frame2,text="Ok",font=("Arial",15),width=20,height=3)
        self.button1.grid(row=3,column=0)
        self.button1.bind("<Button-1>",self.masuk)


        self.button2=tk.Button(self.Frame2,text="hapus",font=("Arial",15),width=20,height=3)
        self.button2.grid(row=3,column=1)
        self.button2.bind("<Button-1>",self.hapus)


        self.button3=tk.Button(self.Frame2,text="Admin",font=("Arial",15),width=20,height=3)
        self.button3.grid(row=4,column=0)
        self.button3.bind("<Button-1>",self.show)

        
        pass
    
    def hapus(self,event):
        print("digunakan untuk menghapus")

    def masuk(self,event):
        print ("digunakan untuk masuk")
        #self.master.withdraw()
        self.framebuka = frame(self)

    def show(self,event):
        self.master.update()
        self.master.deiconify()
        print ("hello")
    
    def frametop(self):
        pass
    
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

class frame(object):
    def __init__(self,master):
        #FullScreenApp.__init__(self,master)
        self.frametop = master




master=tk.Tk()
app=FullScreenApp(master)
app.setting()
master.mainloop()