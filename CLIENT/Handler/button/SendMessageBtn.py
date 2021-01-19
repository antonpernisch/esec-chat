# -------------------------------------
#
# client-side handler
#
# group: Button
# class: SendMessageBtn
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

import wx
import wx.richtext as rt
from Translation.English import English as Locale
import time

class SendMessageBtn:
    def __init__(self, event):
        from Class.gui.ChatboxPanel import ChatboxPanel
        from GUI import Initialization

        current_message = ChatboxPanel.messagebox.GetValue()

        if current_message != "":
            username_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u"Ebrima")
            message_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u"Ebrima")


            ChatboxPanel.chatbox.BeginParagraphSpacing(0, 0)
            ChatboxPanel.chatbox.BeginFontSize(12)
            ChatboxPanel.chatbox.WriteText("\n")
            ChatboxPanel.chatbox.BeginBold()
            ChatboxPanel.chatbox.WriteText("esec" + ": ")
            ChatboxPanel.chatbox.EndBold()
            ChatboxPanel.chatbox.WriteText(current_message)
            ChatboxPanel.chatbox.ShowPosition(ChatboxPanel.chatbox.GetLastPosition())

            ChatboxPanel.messagebox.SetValue("")
            ChatboxPanel.messagebox.SetHint(Locale.send_message)
            ChatboxPanel.messagebox.SetFocus()
        else:
            ChatboxPanel.messagebox.SetFocus()
            return