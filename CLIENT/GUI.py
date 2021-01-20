# -------------------------------------
#
# client-side gui init script
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

import wx
from Class.gui.MainFrame import MainFrame
from Class.gui.ChatboxPanel import ChatboxPanel
from Handler.button.ConnectHandler import ConnectHandler

class Initialization:
    def __init__(self):
        # main init of GUI
        ConnectHandler.connected = False
        Initialization.app = wx.App()
        Initialization.chatbox_frame = MainFrame()
        Initialization.app.MainLoop()