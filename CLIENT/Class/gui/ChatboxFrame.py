# -------------------------------------
#
# client-side class
#
# group: GUI
# class: ChatboxFrame
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

import wx
from Class.gui.ChatboxPanel import ChatboxPanel

class ChatboxFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="esec chat - v1.0 patch 00000", size=(750, 750), style=wx.DEFAULT_FRAME_STYLE)
        self.panel = ChatboxPanel(self)
        self.Show()