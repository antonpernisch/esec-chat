# -------------------------------------
#
# client-side gui init script
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

import wx
from Class.gui.ChatboxFrame import ChatboxFrame
from Class.gui.ChatboxPanel import ChatboxPanel

class Initialization:
    def __init__(self):
        # main init of GUI
        Initialization.app = wx.App()
        Initialization.chatbox_frame = ChatboxFrame()
        Initialization.app.MainLoop()