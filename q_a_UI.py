import os
import sys
import wx
import time

class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # 仅有1行的编辑控件
        self.lblname = wx.StaticText(self, label='Qusetion 1:', pos=(20, 30))
        self.editname = wx.TextCtrl(self, value='Enter your answer here:',
                                    pos=(150, 30), size=(200, -1))

        self.lblname1 = wx.StaticText(self, label='Qusetion 2:', pos=(20, 60))
        self.editname1 = wx.TextCtrl(self, value='Enter your answer here:',
                                    pos=(150, 60), size=(200, -1))


        self.lblname2 = wx.StaticText(self, label='Qusetion 3:', pos=(20, 90))
        self.editname2 = wx.TextCtrl(self, value='Enter your answer here:',
                                    pos=(150, 90), size=(200, -1))


        # 一个按钮                          
        self.button = wx.Button(self, label='Click to take a photo', pos=(20, 120))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)


    def OnClick(self, event):
        print('question 1:', self.editname.GetLineText(0))
        print('question 2:', self.editname1.GetLineText(0))
        print('question 3:', self.editname2.GetLineText(0))

        # 添加回应部分 下面的re为机器人给人类的回应，目前随便写了一段话，如果正式过程中请注释掉re那一行，然后完善上面的部分

        # TO DO
        # os.system("")
        # time.sleep(300)
        # with open('answer.txt') as f:
        #     lines = f.readlines()
        # re = lines[0]

        re = 'asdasdasdasdasdafsafas' #注释掉
        dlg = wx.MessageDialog(self, re, "Respone!", wx.OK) 
        dlg.ShowModal()
        dlg.Destroy()


    
if __name__=='__main__':
    app = wx.App(False)
    frame = wx.Frame(None)
    panel = ExamplePanel(frame)
    frame.Show()
    app.MainLoop()