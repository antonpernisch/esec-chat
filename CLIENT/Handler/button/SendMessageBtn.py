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
from Class.communication.SendMessage import SendMessage as Send
import time

class SendMessageBtn:
    def __init__(self, event):
        Send()