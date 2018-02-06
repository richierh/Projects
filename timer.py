#!/usr/bin/python

import tkinter as tk

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master= master
        #self.master.overrideredirect(True)
  
        '''self.frames = {}
            for f in (HomeFrame, ExecuteFrame): # defined subclasses of BaseFrame
                frame = f(self.container, self)
            fram   e.grid(row=2, column=2, sticky=tk.NW+tk.SE)
            self.frames[f] = frame
            '''
    def setting(self):
        pad=3
        self._geom='200x200+0+0'
        self.master.geometry("{0}x{1}+0+0".format(
        self.master.winfo_screenwidth()-pad, self.master.winfo_screenheight()-pad))
        self.master.bind('<Escape>',self.toggle_geom) 
        self.master.configure(background='#26446b')
        self.master.title('PMC Software House')
        self.master.protocol("WM_DELETE_WINDOW", self.tahantutup)


      
        self.master.grid_rowconfigure(0,weight = 1)
        self.master.grid_columnconfigure(0,weight= 1) 
        self.master.grid_rowconfigure(1,weight = 1)
        self.master.grid_rowconfigure(2,weight = 1)

        durasi = "Selamat datang \nUntuk memulai \nSilahkan tentukan waktu\nTerlebih dahulu"
        self.Frame1 = tk.Frame(self.master)
        self.Frame1.grid(row=0,column=0)

        self.label = tk.Label(self.Frame1,text = durasi,font=("Arial",30),foreground="white")
        self.label.grid(row=0,column=0)
        self.label.configure(background='#26446b')


        self.Frame2 = tk.Frame(self.master)
        self.Frame2.grid(row=1,column=0)
        self.Frame2.configure(background='#26446b')

        self.label1=tk.Label(self.Frame2,foreground="white",text = " Masukkan durasi waktu dlm jam",font=("Arial",15))
        self.label1.grid(row=0,column=0)
        self.label1.configure(background='#26446b')
        
        
        self.lbox=tk.Spinbox(self.Frame2,foreground="white",from_=0,to=24,font=("Arial",30))
        self.lbox.grid(row=0,column=1)
        self.lbox.configure(background='#26446b')

        self.lbox2=tk.Spinbox(self.Frame2,foreground="white",values=(0,5,10,15,20,25,30,35,40,45,50,55),font=("Arial",30))
        self.lbox2.grid(row=1,column=1)
        self.lbox2.configure(background='#26446b')

        self.label2=tk.Label(self.Frame2,foreground="white",text = "Masukan durasi waktu dalam menit",font=("Arial",15))
        self.label2.grid(row=1,column=0)
        self.label2.configure(background='#26446b')
        
        self.button1=tk.Button(self.Frame2,text="Ok",font=("Arial",15),width=20,height=3)
        self.button1.grid(row=3,column=0)
        self.button1.bind("<Button-1>",self.masuk)

        self.button2=tk.Button(self.Frame2,text="hapus",font=("Arial",15),width=20,height=3)
        self.button2.grid(row=3,column=1)
        self.button2.bind("<Button-1>",self.hapus)
 
        self.Frame3 = tk.Frame(self.master)
        self.Frame3.grid(row=3,column=0)
        
        self.button3=tk.Button(self.Frame3,text="Admin",width=10,height=2)
        self.button3.grid(row=2,column=0)
        self.button3.bind("<Button-1>",self.show)
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


class RangkaAdmin(FullScreenApp):
    def __init__(self):
        FullScreenApp.__init__(self,master)
        self.utama= tk.Toplevel()
        self.utama.title("Pengaturan Admin")
        self.utama.wm_geometry("275x75")
        #self.utama.protocol("WM_DELETE_WINDOW", self.tahantutup)

        self.Frame=tk.Frame(self.utama)
        self.Frame.grid(row=0,column=0)
        self.label=tk.Label(self.Frame,text="Password ",anchor=tk.N)
        self.label.grid(row=0,column=0,sticky=tk.W)
        self.entry1 = tk.Entry(self.Frame)
        self.entry1.grid(row=0,column=1)
        

        self.label=tk.Label(self.Frame,text="Ganti password baru",anchor=tk.N)
        self.label.grid(row=1,column=0,sticky=tk.W)
        self.entry2 = tk.Entry(self.Frame)
        self.entry2.grid(row=1,column=1)
        
        self.button3=tk.Button(self.Frame,text="close",width=10,height=2)
        self.button3.grid(row=2,column=1)
        self.button3.bind("<Button-1>",self.tutup)

        self.button3=tk.Button(self.Frame,text="Ok",width=10,height=2)
        self.button3.grid(row=2,column=0)
        self.button3.bind("<Button-1>",self.passw)
    
    def passw(self,event):
        
        self.b = self.entry2.get()
        bukacsvpassword = simpanpassw(self.b)

        self.utama.destroy()
        self.master.update()
        self.master.deiconify()           

    def tutup(self,event):
        
        self.a = self.entry1.get()
        bukacsvpassword = simpanpassw(self.a)

        if self.a == "admin" :
            print (self.a)
            self.master.destroy()
        else :
            self.utama.destroy()
            self.master.update()
            self.master.deiconify()               
        pass

class RangkaBill(FullScreenApp):
    def __init__(self):
        FullScreenApp.__init__(self,master)
        self.utama=tk.Toplevel()
        self.utama.title("Durasi")
        self.utama.wm_geometry("275x75")
        self.utama.protocol("WM_DELETE_WINDOW", self.tahantutup)
   
        self.frame=tk.Frame(self.utama)
        self.frame.grid(row=0,column=0)
        
        self.label=tk.Label(self.frame,text="Waktu Start",anchor=tk.W)
        self.label.grid(row=0,column=0,sticky=tk.W)
        self.Entry1=tk.Entry(self.frame)
        self.Entry1.grid(row=0,column=1,sticky=tk.W)

        self.label=tk.Label(self.frame,text="Waktu Berakhir",anchor=tk.W)
        self.label.grid(row=1,column=0,sticky=tk.W)
        self.Entry1=tk.Entry(self.frame)
        self.Entry1.grid(row=1,column=1,sticky=tk.W)

        self.Button1=tk.Button(self.frame,text = "Selesai")
        self.Button1.grid(row=2,column=1)
        self.Button1.bind("<Button-1>",self.selesai)


    def tahantutup(self):
        pass        
    def selesai(self,event):
        self.utama.destroy()
        self.master.update()
        self.master.deiconify()           
        pass

class simpanpassw():
    def __init__(self,parent):

        print ("hello masuk simpan passw")
        self.nfile=parent
       
       
        pass
    
    def buatfile(self):
        pass


master=tk.Tk()
app=FullScreenApp(master)
app.setting()
master.mainloop()