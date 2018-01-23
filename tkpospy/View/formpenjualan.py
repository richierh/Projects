#!/usr/bin/env python
try:
    import tkinter as tk
    from tkinter import ttk    # for Python2
except ImportError:
    import Tkinter as tk
    import ttk

class SaleForm(tk.Tk):
    """class of SaleForm GUI"""
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("+200+200")
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)
        
        """
        Frame Utama
        """       
        self.Frame = tk.Frame(self.root)
        self.Frame.grid(row=0,column=0,sticky = "nsew")

        self.Frame.grid_columnconfigure(0,weight=1)
        self.Frame.grid_columnconfigure(1,weight=1)

        self.Frame.grid_rowconfigure(0,weight=1)
        
        """
        Frame Kiri
        """

        self.Frame1 = tk.Frame(self.Frame)
        self.Frame1.grid(row=0,column=0,stick="nsew")

        self.Frame1.grid_columnconfigure(0,weight=1)
        self.Frame1.grid_rowconfigure(0,weight=0)
        self.Frame1.grid_rowconfigure(1,weight=0)
        self.Frame1.grid_rowconfigure(2,weight=1)



        """
        Frame Kiri Pertama
        """
        self.Frame1l= tk.Frame(self.Frame1)
        self.Frame1l.grid(row=0,column=0,sticky="nsew")

        self.Frame1l.grid_rowconfigure(0,weight=1)
        self.Frame1l.grid_columnconfigure(0,weight=1)

        self.Label = tk.Label(self.Frame1l, text = "TRANSAKSI PENJUALAN", font = ("Liberation Sans",20),anchor = "c")
        self.Label.grid(row=0,column=0,sticky="nsew")

        """
        Frame Kiri Kedua
        """
        self.Frame1l2=tk.Frame(self.Frame1)
        self.Frame1l2.grid(row=1,column=0,sticky="nsew")        
        
        self.Frame1l2.grid_columnconfigure(0,weight=1)
        self.Frame1l2.grid_rowconfigure(0,weight=1)

        self.Label = tk.Label(self.Frame1l2,text ="No Faktur",anchor = "e")
        self.Label.grid(row =0,column=0, sticky="nsew",padx=10 ,ipadx=5,ipady=5)

        self.labeloptions = ("BC332115456")

        self.label1 = tk.Label(self.Frame1l2,text = self.labeloptions,anchor="ce",font = ("arial",14))
        #self.Etry1.insert(0,"test")
        self.label1.grid(row =0,column=1, sticky="nsew",pady=5,ipady=5)


        """
        TreeVi kiri
        """
        self.TreeVi = ttk.Treeview(self.Frame1)
        self.TreeVi.grid(row=2,column=0,sticky="nsew")
        self.TreeVi.grid_rowconfigure(0,weight=1)
        self.TreeVi.grid_columnconfigure(0,weight=1)


        self.TreeVi["columns"]=["ID"]
        self.TreeVi["show"]=["headings"]
        self.TreeVi.heading("ID",text="ID")


        """
        Frame Kanan
        """
        self.Frame2 = tk.Frame(self.Frame)
        self.Frame2.grid(row=0,column=1,sticky="nsew")

        self.Frame2.grid_rowconfigure(0,weight=0)
        self.Frame2.grid_rowconfigure(1,weight=5)
        self.Frame2.grid_rowconfigure(2,weight=3)
        self.Frame2.grid_rowconfigure(3,weight=1)


        self.Frame2.grid_columnconfigure(0,weight=1)

        """
        Frame Kanan pertama
        """
        self.Frame2r = tk.Frame(self.Frame2)
        self.Frame2r.grid(row=0,column=0,sticky="nsew")
        
        self.Frame2r.grid_rowconfigure(0,weight=1)
        self.Frame2r.grid_columnconfigure(0,weight=1)
        self.Frame2r.grid_columnconfigure(1,weight=1)

        self.Label = tk.Label(self.Frame2r,text="Barcode Scan",anchor="w")
        self.Label.grid(row=0,column=1,sticky="nsew")
        self.Etr = tk.Entry(self.Frame2r)
        self.Etr.grid(row=0,column=0,sticky="nsew",pady=5,ipady=10)

        self.Label = tk.Label(self.Frame2r,text="Cari",anchor="w")
        self.Label.grid(row=1,column=1,sticky="nsew")
        self.Etr = tk.Entry(self.Frame2r)
        self.Etr.grid(row=1,column=0,sticky="nsew",pady = 3,ipady=5)


        self.TreeVi = ttk.Treeview(self.Frame2)
        
        self.TreeVi["columns"]=["ID"]
        self.TreeVi["show"]=["headings"]
        self.TreeVi.heading("ID",text="ID")

        self.TreeVi.grid(row=1,column=0,sticky="nsew")
        self.TreeVi.grid_rowconfigure(0,weight=1)
        self.TreeVi.grid_columnconfigure(0,weight=1)

        """
        Frame Kanan Kedua
        """

        self.LabelFrame2 = tk.LabelFrame(self.Frame2,text = "TOTAL SaleForm",font=("Liberation Sans",12))
        self.LabelFrame2.grid(row=2,column=0,sticky="nsew")

        self.LabelFrame2.grid_rowconfigure(0,weight=2)
        self.LabelFrame2.grid_rowconfigure(1,weight=1)
        self.LabelFrame2.grid_rowconfigure(3,weight=4)

        self.LabelFrame2.grid_columnconfigure(0,weight=1)
        self.LabelFrame2.grid_columnconfigure(1,weight=1)

        self.Label=tk.Label(self.LabelFrame2,text = "SubTotal",font=("liberation sans",14),anchor="e")
        self.Label.grid(row=0,column=0,sticky="nsew")
        self.Etry = tk.Entry(self.LabelFrame2,font=("Liberation Sans",14))
        self.Etry.grid(row=0,column=1,sticky="nsew")

        self.Label=tk.Label(self.LabelFrame2,text = "Pajak",font=("liberation sans",12),anchor="e")
        self.Label.grid(row=1,column=0,sticky="nsew")
        self.Etry = tk.Entry(self.LabelFrame2,font=("liberation sans",12))
        self.Etry.grid(row=1,column=1,sticky="nsew")

        self.Label=tk.Label(self.LabelFrame2,text = "Total",font=("liberation sans",20),anchor="e")
        self.Label.grid(row=3,column=0,sticky="nsew")
        self.Etry = tk.Entry(self.LabelFrame2,font=("liberation sans",20))
        self.Etry.grid(row=3,column=1,sticky="nsew")

        """
        Frame Kanan Ketiga
        """
        self.Frame2r3 = tk.Frame(self.Frame2)
        self.Frame2r3.grid(row=3,column=0,sticky="nsew")
        self.Frame2r3.grid_rowconfigure(0,weight=1)
        self.Frame2r3.grid_columnconfigure(0,weight=1)
        self.Frame2r3.grid_columnconfigure(1,weight=1)

        self.Button1=tk.Button(self.Frame2r3,text="Print",command = self.ButExe)
        self.Button1.grid(row=0,column=0,sticky="nsew")
        self.Button2=tk.Button(self.Frame2r3,text="Batal",command= self.ButCanc)
        self.Button2.grid(row=0,column=1,sticky="nsew")

    def mainloop(self):
        self.root.mainloop()

    def ButExe(self):
        print ("Execute working")
        pass
    
    def ButCanc(self):
        print ("Execute cancel is also working")
        pass

    def nofaktur(self):
        outputm=self.Etry.setvar("test")
        print (outputm)
        pass


if __name__=="__main__":
    K = SaleForm()
    K.mainloop()
    