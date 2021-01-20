# -------------------------------------
#
# client-side dialog
#
# group: Dialog
# class: ErrorDialog
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

import wx

class ErrorDialog:
    def __init__(self, title, message):
        dialog = wx.MessageBox(message, title, wx.CANCEL | wx.ICON_ERROR)