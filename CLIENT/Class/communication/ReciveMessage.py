# -------------------------------------
#
# client-side class
#
# group: communication
# class: ReciveMessage
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

import wx
import wx.richtext

class ReciveMessage:
    def __init__(sender, message):
        from Class.gui.ChatboxPanel import ChatboxPanel
        from Class.communication.SendMessage import SendMessage

        username_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u"Ebrima")
        message_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u"Ebrima")

        ChatboxPanel.chatbox.BeginParagraphSpacing(0, 0)
        ChatboxPanel.chatbox.BeginFontSize(12)
        ChatboxPanel.chatbox.BeginBold()
        ChatboxPanel.chatbox.WriteText("\n" + sender + ": ")
        ChatboxPanel.chatbox.EndBold()
        ChatboxPanel.chatbox.WriteText(message)
        ChatboxPanel.chatbox.ShowPosition(ChatboxPanel.chatbox.GetLastPosition())
        SendMessage.reserved = False

    def redText(sender, message):
        from Class.gui.ChatboxPanel import ChatboxPanel
        from Class.communication.SendMessage import SendMessage

        username_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u"Ebrima")
        message_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u"Ebrima")

        ChatboxPanel.chatbox.BeginParagraphSpacing(0, 0)
        ChatboxPanel.chatbox.BeginFontSize(12)
        ChatboxPanel.chatbox.BeginBold()
        ChatboxPanel.chatbox.BeginTextColour('red')
        ChatboxPanel.chatbox.WriteText("\n" + sender + ": ")
        ChatboxPanel.chatbox.EndBold()
        ChatboxPanel.chatbox.EndTextColour()
        ChatboxPanel.chatbox.WriteText(message)
        ChatboxPanel.chatbox.ShowPosition(ChatboxPanel.chatbox.GetLastPosition())
        SendMessage.reserved = False