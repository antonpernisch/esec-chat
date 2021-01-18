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
from Handler.button.SendMessageBtn import SendMessageBtn
from Translation.English import English as Locale

class ChatboxPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        chatbox_sizer = wx.BoxSizer(wx.VERTICAL)

        ChatboxPanel.chatbox = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_MULTILINE | wx.TE_READONLY)

        usermessage_hsizer = wx.BoxSizer(wx.HORIZONTAL)     
        ChatboxPanel.messagebox = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_MULTILINE)
        ChatboxPanel.messagebox.SetHint(Locale.send_message)
        ChatboxPanel.sendbutton = wx.Button(self, wx.ID_ANY, label=Locale.send_button)
        ChatboxPanel.sendbutton.Bind(wx.EVT_BUTTON, SendMessageBtn)
        usermessage_hsizer.Add(ChatboxPanel.messagebox, 6, wx.EXPAND | wx.RIGHT, 10)
        usermessage_hsizer.Add(ChatboxPanel.sendbutton, 1, wx.EXPAND)

        # add chatbox textarea to main sizer
        chatbox_sizer.Add(ChatboxPanel.chatbox, 6, wx.ALL | wx.EXPAND, 10)
        chatbox_sizer.Add(usermessage_hsizer, 1, wx.ALL | wx.EXPAND, 10)

        self.SetSizer(chatbox_sizer)