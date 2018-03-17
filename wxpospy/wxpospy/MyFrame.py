# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0b3 on Wed Feb 14 17:53:42 2018
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.text_ctrl_3 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_4 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_5 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_6 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_7 = wx.TextCtrl(self, wx.ID_ANY, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("frame"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        grid_sizer_1 = wx.FlexGridSizer(0, 2, 0, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, _("label_4"))
        grid_sizer_1.Add(label_4, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_3, 0, 0, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, _("label_5"))
        grid_sizer_1.Add(label_5, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_4, 0, 0, 0)
        label_6 = wx.StaticText(self, wx.ID_ANY, _("label_6"))
        grid_sizer_1.Add(label_6, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_5, 0, 0, 0)
        label_7 = wx.StaticText(self, wx.ID_ANY, _("label_7"))
        grid_sizer_1.Add(label_7, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_6, 0, 0, 0)
        label_8 = wx.StaticText(self, wx.ID_ANY, _("label_8"))
        grid_sizer_1.Add(label_8, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_7, 0, 0, 0)
        self.SetSizer(grid_sizer_1)
        self.Layout()
        # end wxGlade

# end of class MyFrame
