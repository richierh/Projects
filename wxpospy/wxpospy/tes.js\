#!/usr/bin/env python

import wx

class MainFrame(wx.Frame):
    """
    """
    def __init__(self,*args,**kwds):
        super(MainFrame,self).__init__(*args,**kwds)
        self.SetTitle("PMC Comptuer")
        self.Centre()
        self.SetSize(500,300)
        self.__structure_of_frame()


    def __structure_of_frame(self):
        self.fgridsizer =  wx.FlexGridSizer(4,2,0,0)
        self.label1 = wx.StaticText(self,label = "nama")
        self.fgridsizer.Add(self.label1)
        self.SetSizer(self.fgridsizer)
        pass
    

    def __sizer__(self):
        pass




class MyApp(wx.App):

    def OnInit(self):
        self.MainW = MainFrame(None)
        self.MainW.Show()

        return True






if __name__=="__main__":
    App = MyApp(None)
    App.MainLoop() 