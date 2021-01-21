# -------------------------------------
#
# client-side class
#
# group: communication
# class: SendMessage (aka Send)
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

# TODO: check current_message for ; (injection etc)

import wx
from Translation.English import English as Locale
import socket

class SendMessage:
    def __init__(self):
        from Class.gui.ChatboxPanel import ChatboxPanel
        from Class.gui.LoginPanel import LoginPanel

        current_message = ChatboxPanel.messagebox.GetValue()
        username = LoginPanel.username_textctrl.GetValue()

        username_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u"Ebrima")
        message_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u"Ebrima")

        if current_message != "":
            username = LoginPanel.username_textctrl.GetValue()
            host = LoginPanel.ip_textctrl.GetValue()
            port = 826

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect_ex((host, port))
                body = b'MES;' + bytes(username, 'utf-8') + b";" + bytes(current_message, 'utf-8')
                s.sendall(body)
                data = s.recv(1024)
            if data.decode("utf-8") == "ACK-MES":
                ChatboxPanel.messagebox.SetValue("")
                ChatboxPanel.messagebox.SetHint(Locale.send_message)
                ChatboxPanel.messagebox.SetFocus()
            else:
                # message was not ack'd by server
                ChatboxPanel.messagebox.SetFocus()
        else:
            ChatboxPanel.messagebox.SetFocus()
            return