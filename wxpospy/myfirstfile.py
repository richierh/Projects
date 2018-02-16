#!/usr/bin/python

import wx



class Frame(wx.Frame):
    """
    """
    def __init__(self,*args,**kwds):
        super(Frame,self).__init__(*args,**kwds)
        self.__properties()
        self.__set_layout()


    def __properties(self):
        self.SetTitle("PMC Computer")
        self.SetSize(600,400)
        self.Centre()
        self.border = 5

        pass

    def __set_layout(self):
        """
        Pengaturan Menu Bar
        """
        self.menubar = wx.MenuBar()

        self.menu1 = wx.Menu()

        menuitem = wx.MenuItem(self.menu1,id=1,text="Koneksi")
        self.menu1.Append(menuitem)

        menuitem2 = wx.MenuItem(self.menu1,id=2,text="Putus Koneksi")
        self.menu1.Append(menuitem2)

        menuitem3 = wx.MenuItem(self.menu1,id=3,text="Keluar")
        self.menu1.Append(menuitem3)
        self.Bind(wx.EVT_MENU,self.keluar,id=3)

        self.menubar.Append(self.menu1,"Berkas")



        menu2 = wx.Menu()
        menuitem = wx.MenuItem(menu2,id=1,text="test")
        menu2.Append(menuitem)

        menuitem2 = wx.MenuItem(menu2,id=3,text="test3")
        menu2.Append(menuitem2)
        
        self.menubar.Append(menu2,"Pengaturan")

        self.SetMenuBar(self.menubar)

        """
        Tampilan sizer (panel utama)
        """
        sizer = wx.BoxSizer(wx.VERTICAL)

        panel1 = wx.Panel(self)
        sizer.Add(panel1,0,1,5)

        sizer1 = wx.BoxSizer(wx.VERTICAL)
        st_text = wx.StaticText(panel1,label = "PMC")
        
        st_text.SetFont(wx.Font(wx.FontInfo(20).FaceName("Magneto")))
        sizer1.Add(st_text,0,wx.ALIGN_CENTER_HORIZONTAL,5)
        panel1.SetSizer(sizer1)
        #st_text.Centre()
        

        
        fgridsizer = wx.FlexGridSizer(4,2,0,0)
        sizer.Add(fgridsizer,0,0)

        label1 =  wx.StaticText(self,id=wx.ID_ANY,label ="tes")
        fgridsizer.Add(label1,1,self.border)
       
        TextC =  wx.TextCtrl(self,id=wx.ID_ANY)
        fgridsizer.Add(TextC,0,0,self.border)

        label1 =  wx.StaticText(self,id=wx.ID_ANY,label ="tes")
        fgridsizer.Add(label1,0,0,wx.ALL,5)
       
        TextC =  wx.TextCtrl(self,id=wx.ID_ANY)
        fgridsizer.Add(TextC,0,0,self.border)

        label1 =  wx.StaticText(self,id=wx.ID_ANY,label ="tes")
        fgridsizer.Add(label1,0,1,5)
       
        TextC =  wx.TextCtrl(self,id=wx.ID_ANY)
        fgridsizer.Add(TextC,0,0,self.border)

        label1 =  wx.StaticText(self,id=wx.ID_ANY,label ="tes")
        fgridsizer.Add(label1,0,1,5)
       
        TextC =  wx.TextCtrl(self,id=wx.ID_ANY)
        fgridsizer.Add(TextC,0,0,self.border)

        self.SetSizer(sizer)

        pass

    def keluar(self,event):
        """
        Berhasil Keluar
        """
        print (Frame.keluar.__doc__)

        return self.Close()
        

class RunApp(wx.App):
    """
    """
    def OnInit(self):
        runFrame = Frame(None)
        runFrame.Show()
        return True


if __name__=="__main__":
    start = RunApp()
    start.MainLoop()
    
