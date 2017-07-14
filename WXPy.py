# coding=utf-8

"""
@version: ??
@author: AA-ldc
@file: WXPy_DB.py
@time: 2016/10/31 9:25
<p>创建一个文本框的窗口来显示鼠标的位置</p>
"""
import wx
import reSizeOfPic


class MyFrame(wx.Frame):
    def __init__(self):
        """wxpython 中文前加u"""
        wx.Frame.__init__(self, None, -1, u"修改图片大小", size=(400, 400))
        panel = wx.Panel(self, -1)
        self.text = wx.StaticText(panel, -1, u"Path:", pos=(10, 12))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(60, 10), style=wx.TE_READONLY)
        self.buttonRe = wx.Button(panel, label=u"选择图片路径", pos=(200, 10), size=(100, 25))
        self.text = wx.StaticText(panel, -1, u"Size:", pos=(10, 50))
        self.posSize = wx.TextCtrl(panel, -1, "", pos=(60, 50), style=wx.TE_WORDWRAP)
        self.button = wx.Button(panel, label=u"修改", pos=(200, 50), size=(50, 25))
        self.posSave = wx.TextCtrl(panel, -1, "", pos=(0, 100), size=(400, 300), style=wx.TE_MULTILINE)
        # 绑定按钮单击事件
        self.Bind(wx.EVT_BUTTON, self.OnUpdate, self.button)
        self.Bind(wx.EVT_BUTTON, self.OnChoose, self.buttonRe)

    def OnUpdate(self, event):
        path = self.posCtrl.GetValue()
        reSizeOfPic.new_width = int(self.posSize.GetValue())
        try:
            b = reSizeOfPic.BFS_Dir(path, reSizeOfPic.printDir, reSizeOfPic.printFile)
            temp = reSizeOfPic.result
            t = ""
            while temp:
                t = t+temp[0]+u"\n"
                temp = temp[1:]
            t = t+u"\r\n          **********\r\n" + u"*********图片处理完毕*********" + u"\r\n          **********\r\n"
            self.posSave.SetValue(t)
            reSizeOfPic.Py_Log(
                "\r\n          **********\r\n" + "*********图片处理完毕*********" + "\r\n          **********\r\n")
        except:
            print "Unexpected error:", reSizeOfPic.sys.exc_info()
            self.posSave.SetValue("Unexpected error:"+reSizeOfPic.sys.exc_info())


    def OnChoose(self, event):
        dlg = wx.DirDialog(self, u"选择文件夹", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            print dlg.GetPath()  # 文件夹路径
            self.posCtrl.SetValue("%s" % dlg.GetPath())
        dlg.Destroy()
        # print 'Cancel'


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
