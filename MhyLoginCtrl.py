import wx
import MhyFrame
import random
import string

generated = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

class LoginControl (MhyFrame.LoginFrame):
    def __init__(self, parent):
        super().__init__(parent)

    def goLogin(self, event):
        uname = self.uname_text.GetValue()
        pwd = self.pwd_text.GetValue()
        sv = self.server_sel.GetStringSelection()
        print(uname, pwd, sv)
        wx.MessageBox(f' Username : {uname} \n Nickname : Lumine \n Server : {sv} \n Redem Code : {generated}')

app = wx.App()
frame = LoginControl(None)
frame.Show()
app.MainLoop()