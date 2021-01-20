# -------------------------------------
#
# client-side class
#
# group: GUI
# class: ChatboxPanel
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

import wx
from Translation.English import English as Locale
from Handler.button.ConnectHandler import ConnectHandler

class LoginPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        login_sizer = wx.BoxSizer(wx.VERTICAL)

        heading_text = wx.StaticText(self, 0, Locale.login__heading)
        heading_text.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD))

        ipAddress_text = wx.StaticText(self, 0, Locale.login__enter_ip)
        ipAddress_text.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL))

        LoginPanel.ip_textctrl = wx.TextCtrl(self, 0, style=wx.TE_PROCESS_ENTER)
        LoginPanel.ip_textctrl.SetHint(Locale.login__ip_hint)
        LoginPanel.ip_textctrl.Bind(wx.EVT_TEXT_ENTER, ConnectHandler)

        pleaseLogin_text = wx.StaticText(self, 0, Locale.login__must_login)
        pleaseLogin_text.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL))

        LoginPanel.username_textctrl = wx.TextCtrl(self, 0, style=wx.TE_PROCESS_ENTER)
        LoginPanel.username_textctrl.SetHint(Locale.login__username_hint)
        LoginPanel.username_textctrl.Bind(wx.EVT_TEXT_ENTER, ConnectHandler)

        LoginPanel.connect_btn = wx.Button(self, 0, Locale.login__connect, size=(-1, 40))
        LoginPanel.connect_btn.Bind(wx.EVT_BUTTON, ConnectHandler)


        login_sizer.AddStretchSpacer()
        login_sizer.Add(heading_text, 0, wx.CENTER)
        login_sizer.Add(ipAddress_text, 0, wx.CENTER | wx.TOP, 24)
        login_sizer.Add(LoginPanel.ip_textctrl, 0, wx.CENTER | wx.TOP, 8)
        login_sizer.Add(pleaseLogin_text, 0, wx.CENTER | wx.TOP, 24)
        login_sizer.Add(LoginPanel.username_textctrl, 0, wx.CENTER | wx.TOP, 8)
        login_sizer.Add(LoginPanel.connect_btn, 0, wx.CENTER | wx.TOP, 32)
        login_sizer.AddStretchSpacer()

        self.SetSizer(login_sizer)